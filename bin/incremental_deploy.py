#!/usr/bin/env python3

"""
Incremental deployment helper.

Uploads only new or modified files to the remote host via SFTP. It keeps a local
manifest of file hashes so repeated deploys only transfer changed content.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import posixpath
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterator, Tuple

import paramiko
from dotenv import load_dotenv


EXCLUDED_FILENAMES = {".DS_Store", "Thumbs.db"}
MANIFEST_FILENAME = ".deploy_manifest.json"
REMOTE_NOTES_DIR_ENV = "REMOTE_NOTES_DIR"


def sha256_digest(path: Path) -> str:
    """Return the SHA256 hex digest for the given file."""
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def iter_files(source: Path) -> Iterator[Tuple[str, Path]]:
    """
    Yield (relative_path, absolute_path) for files inside source.

    Relative paths use POSIX separators for portability.
    """
    if source.is_file():
        rel_path = source.name
        if rel_path not in EXCLUDED_FILENAMES:
            yield rel_path, source
        return

    for path in sorted(source.rglob("*")):
        if not path.is_file():
            continue
        if path.name in EXCLUDED_FILENAMES:
            continue
        rel_path = path.relative_to(source).as_posix()
        yield rel_path, path


@dataclass
class TargetState:
    dest_prefix: str
    files: Dict[str, Dict[str, str]]


class DeployManifest:
    """Simple JSON-backed manifest storing hashes for deployed files."""

    def __init__(self, path: Path) -> None:
        self.path = path
        self._data = {"targets": {}}
        if self.path.exists():
            try:
                self._data = json.loads(self.path.read_text())
            except json.JSONDecodeError:
                # fall back to empty manifest on decode errors
                self._data = {"targets": {}}

    def target(self, key: str, dest_prefix: str) -> TargetState:
        target = self._data["targets"].setdefault(
            key, {"dest_prefix": dest_prefix, "files": {}}
        )
        # Normalise stored prefix in case the destination changes formatting (e.g. ./path/)
        target["dest_prefix"] = dest_prefix
        return TargetState(dest_prefix=dest_prefix, files=target["files"])

    def update_target(self, key: str, dest_prefix: str, files: Dict[str, Dict[str, str]]) -> None:
        self._data["targets"][key] = {"dest_prefix": dest_prefix, "files": files}

    def save(self) -> None:
        self.path.write_text(json.dumps(self._data, indent=2, sort_keys=True))


class IncrementalDeployer:
    def __init__(
        self,
        hostname: str,
        username: str,
        port: int,
        remote_root: str,
        key_filename: str | None = None,
    ) -> None:
        self.hostname = hostname
        self.username = username
        self.port = port
        self.remote_root = posixpath.normpath(remote_root)
        self.key_filename = key_filename
        self._ssh = None
        self._sftp = None
        self._known_dirs = set()

    def __enter__(self) -> "IncrementalDeployer":
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(
            self.hostname,
            port=self.port,
            username=self.username,
            key_filename=self.key_filename,
            allow_agent=True,
            look_for_keys=True,
        )
        self._ssh = ssh
        self._sftp = ssh.open_sftp()
        self._known_dirs.add(self.remote_root)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if self._sftp is not None:
            self._sftp.close()
        if self._ssh is not None:
            self._ssh.close()

    @property
    def sftp(self):
        if self._sftp is None:
            raise RuntimeError("SFTP connection is not open")
        return self._sftp

    def ensure_remote_dir(self, remote_path: str) -> None:
        directory = posixpath.dirname(remote_path)
        if not directory or directory == "/" or directory in self._known_dirs:
            return

        segments = []
        current = directory
        while current and current not in self._known_dirs and current != "/":
            segments.append(current)
            current = posixpath.dirname(current)

        for segment in reversed(segments):
            try:
                self.sftp.stat(segment)
            except IOError:
                self.sftp.mkdir(segment)
            self._known_dirs.add(segment)

    def upload(self, local_path: Path, remote_rel_path: str) -> None:
        remote_path = posixpath.normpath(
            posixpath.join(self.remote_root, remote_rel_path)
        )
        self.ensure_remote_dir(remote_path)
        self.sftp.put(local_path.as_posix(), remote_path)

    def remove(self, remote_rel_path: str) -> None:
        remote_path = posixpath.normpath(
            posixpath.join(self.remote_root, remote_rel_path)
        )
        try:
            self.sftp.remove(remote_path)
        except IOError:
            # If the file is already absent we can ignore the error.
            pass


def parse_webhost(webhost: str) -> Tuple[str, str]:
    """Split WEBHOST env var into username + hostname."""
    if "@" not in webhost:
        raise ValueError("WEBHOST must be in the format user@host")
    username, hostname = webhost.split("@", 1)
    return username, hostname


def normalise_destination(dest: str) -> str:
    if dest in ("", ".", "./"):
        return ""
    return dest.strip("/").replace("\\", "/")


def build_manifest_key(source: Path, root: Path, dest_prefix: str) -> str:
    try:
        source_rel = source.relative_to(root).as_posix()
    except ValueError:
        source_rel = source.as_posix()
    return f"{source_rel}->{dest_prefix or '.'}"


def deploy(
    source: Path,
    destination: str,
    manifest: DeployManifest,
    deployer: IncrementalDeployer,
    project_root: Path,
) -> Tuple[int, int]:
    dest_prefix = normalise_destination(destination)
    manifest_key = build_manifest_key(source, project_root, dest_prefix)
    target_state = manifest.target(manifest_key, dest_prefix)

    current_files: Dict[str, Dict[str, str]] = {}
    uploaded = 0
    removed = 0

    rel_to_remote_cache: Dict[str, str] = {}
    for rel_path, absolute_path in iter_files(source):
        rel_to_remote_cache[rel_path] = (
            rel_path if not dest_prefix else posixpath.join(dest_prefix, rel_path)
        )
        file_hash = sha256_digest(absolute_path)
        previous = target_state.files.get(rel_path)
        if not previous or previous.get("hash") != file_hash:
            deployer.upload(absolute_path, rel_to_remote_cache[rel_path])
            uploaded += 1
        try:
            source_rel = absolute_path.relative_to(project_root).as_posix()
        except ValueError:
            source_rel = absolute_path.as_posix()
        current_files[rel_path] = {
            "hash": file_hash,
            "remote_rel_path": rel_to_remote_cache[rel_path],
            "source": source_rel,
        }

    previous_rel_paths = set(target_state.files.keys())
    current_rel_paths = set(current_files.keys())
    stale_rel_paths = previous_rel_paths - current_rel_paths

    for rel_path in stale_rel_paths:
        remote_rel = target_state.files[rel_path]["remote_rel_path"]
        deployer.remove(remote_rel)
        removed += 1

    manifest.update_target(manifest_key, dest_prefix, current_files)
    manifest.save()

    return uploaded, removed


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Incremental SFTP deployment helper."
    )
    parser.add_argument("source", help="Local file or directory to deploy")
    parser.add_argument(
        "destination",
        help="Remote destination relative to PATHTODIR (use '.' for the root)",
    )
    parser.add_argument(
        "--manifest",
        default=MANIFEST_FILENAME,
        help="Path to the deployment manifest file (default: .deploy_manifest.json)",
    )
    parser.add_argument(
        "--identity",
        help="Optional SSH identity (private key) to use for authentication",
    )

    args = parser.parse_args()

    project_root = Path(__file__).resolve().parents[1]
    source = (Path(args.source)).resolve()
    if not source.exists():
        raise SystemExit(f"Source path does not exist: {source}")

    load_dotenv()

    webhost = os.environ.get("WEBHOST")
    port = int(os.environ.get("WEBPORT", "22"))
    remote_root = os.environ.get("PATHTODIR")
    # REMOTE_NOTES_DIR allows targeting a subdirectory (e.g. "notes") beneath PATHTODIR.
    remote_notes_dir = os.environ.get(REMOTE_NOTES_DIR_ENV, "").strip()

    if not webhost or not remote_root:
        raise SystemExit("WEBHOST and PATHTODIR must be set in the environment or .env")

    if remote_notes_dir:
        remote_notes_dir = normalise_destination(remote_notes_dir)
        if remote_notes_dir:
            remote_root = posixpath.join(remote_root.rstrip("/"), remote_notes_dir)

    username, hostname = parse_webhost(webhost)

    manifest_path = (Path(args.manifest)).resolve()
    manifest = DeployManifest(manifest_path)

    with IncrementalDeployer(
        hostname=hostname,
        username=username,
        port=port,
        remote_root=remote_root,
        key_filename=args.identity,
    ) as deployer:
        uploaded, removed = deploy(
            source=source,
            destination=args.destination,
            manifest=manifest,
            deployer=deployer,
            project_root=project_root,
        )

    print(
        f"Deployed {source} -> {args.destination}: "
        f"{uploaded} uploaded, {removed} removed."
    )


if __name__ == "__main__":
    main()
