# Coding Agent Guide

## Overview
- Purpose: generate, curate, and publish personal “Today I Learned” notes and weeknotes for https://colmjude.com/notes.
- Core flow: markdown content in `docs/` → rendered HTML in `dist/notes/` via Jinja templates and markdown extensions.
- Key scripts: `render.py` for site generation, `application/redirects.py` for `.htaccess` redirects, and `bin/create_til.py` / `tilcli.py` for authoring.

## Repository Layout
- `docs/`: source markdown notes organised by topical folders (e.g. `docs/til/`, `docs/weeknote/`). Frontmatter drives metadata and rendering.
- `templates/`: Jinja templates for note pages (`note.html`), listing views (`list.html`), and tags (`tags.html`).
- `application/`: Python helpers (`markdown.py`, `jinja_setup.py`, `jinja_filters.py`, `redirects.py`) and reusable logic.
- `dist/notes/`: build output. Treat as generated; `render.py` populates it.
- `src/`: authoring source for styles (`scss/`) and JavaScript (`javascripts/`). Compiled assets land in `dist/static/`.
- `bin/`, `scripts/`, `Makefile`: convenience entry points for note creation, deployment, and build orchestration.

## Environment & Tooling
- Python 3.9+ recommended. Use a virtualenv (`python3 -m venv .venv && source .venv/bin/activate`) and install dependencies with `pip install -r requirements.txt`.
- Node 16+ recommended. Install front-end dependencies with `npm install` (depends on `colmjude-frontend` via Git).
- Environment variables live in `.env` (see `.env.example`). Tweet embeds require Twitter credentials; FTP deployment requires `WEBHOST`, `WEBPORT`, and `PATHTODIR`.
- Optional overrides go in `local.mk`, which is ignored by git but automatically included by the `Makefile`.

## Authoring Notes
- Create new notes with `python bin/create_til.py "Your Title"` or `python tilcli.py new`. Use `--folder <subdir>` to target folders such as `til` or `weeknote`.
- Frontmatter template:
  ```
  ---
  title: "Title Case"
  tags: tag-one, tag-two
  author: Colm Britton
  created: YYYY/MM/DD
  updated: YYYY/MM/DD
  ---
  ```
  `tags` is a comma-separated string that renders to lists and tag pages. Set `draft: true` to exclude a note from builds.
- WikiLinks `[[Some Note]]` link to other notes; target titles must match exactly and exist in the generated index.

## Rendering & Assets
- Primary build command: `python render.py`. It:
  - Loads markdown via `Note`/`Notes`, enriches frontmatter, and writes HTML to `dist/notes/<slug>/index.html`.
  - Generates tag pages (`/notes/tag/<tag>/`) and a weeknote index.
  - Calls `application/redirects.py` to build `dist/notes/weeknote/.htaccess` based on weeknote frontmatter `redirect` entries.
- Makefile shortcuts:
  - `make render` (runs `render.py` and redirects generation).
  - `make assets` → `npm run build:stylesheets` + `npm run build:javascripts`.
  - `make local` → copies images, renders notes, builds assets.
  - `make watch` → runs parallel asset/page watchers (requires chokidar & nps).
- Keep `dist/` outputs under version control as appropriate for deployment, but treat them as generated artefacts during development.

## Front-End Assets
- Styles live under `src/scss/` and leverage the shared `colmjude-frontend` package. Run `npm run build:stylesheets` after changes.
- JavaScript entry point is `src/javascripts/notes-search.js`; build with `npm run build:javascripts`.
- BrowserSync / watcher scripts exist but are optional; see `package.json` and `node_modules/colmjude-frontend/package-scripts.js` for definitions.

## Deployment
- Deployment scripts rely on FTP credentials in `.env`.
- `make deploy` runs `render`, copies images, and pushes notes plus stylesheet via `scripts/deploy.sh` / `scripts/deploy-images.sh`.
- Add SSH key (`ssh-add ~/.ssh/siteground`) before deploying; see `DEPLOY_NOTES.md` for server specifics.

## Utilities & Data
- `recent_updates.py` prints recently updated notes (`python recent_updates.py --from YYYY-MM-DD`).
- `dump.py` exports a SQLite database of notes (`make sqlite-db`).
- `application/markdown.py` exposes a reusable markdown factory when other scripts need consistent parsing.

## Quality Gates
- Formatting: `black .` (or `make black`), `isort --profile black .` (`make isort`).
- Linting: `flake8 .` (`make flake8`). `make lint` runs both formatting checks.
- No automated tests; rely on local rendering plus manual spot checks in `dist/notes/` (serve locally with `make serve`).

## Collaboration Notes
- Avoid editing `dist/` directly; regenerate via scripts instead.
- Preserve ASCII frontmatter and filenames (slugified, lower-case, hyphen-separated).
- Confirm new wiki links resolve by running `python render.py` and inspecting console output for missing note warnings.
- Document secrets or machine-specific tweaks in `LOCAL_NOTES.md` or `local.mk` rather than committing them.
