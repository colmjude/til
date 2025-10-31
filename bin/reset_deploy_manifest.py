#!/usr/bin/env python3

"""
Remove specific entries from the deploy manifest so they are re-uploaded
on the next incremental deployment.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict, Iterable, Set

MANIFEST_FILENAME = ".deploy_manifest.json"
DEFAULT_PATHS = [
    "index.html",
    "weeknote/index.html",
    "tag/index.html",
    "tag/planning-applications/index.html",
    "tag/work/index.html",
    "tag/data/index.html",
]


def normalise(path: str) -> str:
    """Return a normalised manifest path (strip leading slash/backslash)."""
    return path.strip().lstrip("/\\")


def collect_targets(paths: Iterable[str]) -> Set[str]:
    """Return the set of remote paths to clear, falling back to defaults."""
    cleaned = [normalise(path) for path in paths if path and path.strip()]
    if cleaned:
        return set(cleaned)
    return {normalise(path) for path in DEFAULT_PATHS}


def remove_entries(data: Dict, targets_to_clear: Set[str]) -> int:
    """Remove entries matching provided remote paths across all targets."""
    removed = 0
    targets = data.get("targets", {})
    for target_name, target_data in targets.items():
        files = target_data.get("files", {})
        keys_to_remove = []
        for rel_path, file_info in files.items():
            remote_rel = normalise(file_info.get("remote_rel_path", rel_path))
            rel_norm = normalise(rel_path)
            if remote_rel in targets_to_clear or rel_norm in targets_to_clear:
                keys_to_remove.append(rel_path)
        for key in keys_to_remove:
            files.pop(key, None)
            removed += 1
        target_data["files"] = files
    return removed


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Clear entries from the deploy manifest so they deploy on the next run."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help=(
            "Remote relative paths to remove (e.g. 'index.html', 'weeknote/index.html'). "
            "Leading slashes are ignored. If omitted, a default preset is used."
        ),
    )
    parser.add_argument(
        "--manifest",
        default=MANIFEST_FILENAME,
        help=f"Path to the manifest file (default: {MANIFEST_FILENAME})",
    )
    args = parser.parse_args()

    manifest_path = Path(args.manifest).resolve()
    if not manifest_path.exists():
        raise SystemExit(f"Manifest file not found: {manifest_path}")

    try:
        data = json.loads(manifest_path.read_text())
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Manifest file is not valid JSON: {manifest_path}") from exc

    using_defaults = not args.paths
    targets_to_clear = collect_targets(args.paths)

    if using_defaults:
        print(
            "No paths supplied; using default preset: "
            + ", ".join(sorted(DEFAULT_PATHS))
        )

    removed = remove_entries(data, targets_to_clear)

    if removed:
        manifest_path.write_text(json.dumps(data, indent=2, sort_keys=True))
        print(
            f"Removed {removed} entr{'y' if removed == 1 else 'ies'} from {manifest_path}"
        )
    else:
        print("No matching entries found; manifest left unchanged.")


if __name__ == "__main__":
    main()
