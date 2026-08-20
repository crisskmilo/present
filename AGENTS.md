<!-- bmad:context -->
<!-- Verified 2026-08-20 against 8a5f616. Managed by bmad-project-context; edits inside this block are replaced on refresh. Keep anything you want preserved outside the markers. -->

## presente

Digital mental health accompaniment platform providing responsible, vetted content across psychological well-being, pastoral/spiritual support, and curated lived experiences. Python (FastAPI), SQLAlchemy 2.0 Async, PostgreSQL (Supabase), Angular + Capacitor for multiplatform delivery (Web/PWA, Android .apk, iOS .ipa). Planning lives in `docs/` and `_bmad-output/planning-artifacts/`.

## Language

- 100% English for all source code: variable names, function names, class names, type annotations, module names, docstrings, inline comments, test cases, and commit messages.
- File names, directory names, and folder paths must always be in English (`snake_case.py` for Python, `kebab-case.md` for Markdown/docs, `kebab-case.ext` for assets).
- All BMAD-generated deliverables in `_bmad-output/` are bilingual: English first (canonical source), Spanish second (direct translation).
- Auxiliary standalone translation files must use the `.es.md` suffix (e.g., `docs/present-mvp-proposal.es.md`).
- Monolingual output is not allowed for BMAD deliverables.

## Policy

- Strictly adhere to Clean Architecture layers (Domain -> Application -> Infrastructure -> Presentation).
- Zero external dependencies in `src/domain/`: pure business entities and abstract repository contracts (`abc.ABC`).
- Never commit secrets or credentials: `resources/credential_google_docs.json` must remain gitignored.
- Zero-cost deployment invariant ($0 USD): all infrastructure relies strictly on free tiers (Vercel/Cloudflare Pages, Render/Oracle Always Free, Supabase, Google AI Studio).
- Institutional guarantee: Clínica San Juan de Dios assumes zero financial, server, or maintenance costs.

## Where things are

- Project proposal & PRD source: `docs/present-mvp-proposal.md` (English base) and `docs/present-mvp-proposal.es.md` (Spanish translation)
- Technical architecture specification: `docs/architecture-clean-architecture.md`
- BMAD skill workflows: `.agents/skills/`
- Google Docs sync script: `_bmad/scripts/sync_to_google_docs.py`
- Word proposal generator: `docs/generate_docx.py`
- Diagram image generator: `docs/generate_diagram_images.py`

## Running and verifying

- Synchronize with Google Docs: `python _bmad/scripts/sync_to_google_docs.py`
- Re-generate diagram images: `python docs/generate_diagram_images.py`
- Re-generate executive proposal Word doc: `python docs/generate_docx.py`

## Conventions that differ from defaults

- Inversion of Control (IoC): Dependency injection wired via `FastAPI.Depends` in `src/api/deps.py` or container in `src/core/container.py`.
- Domain interfaces must be declared using `abc.ABC` with `@abstractmethod` in `src/domain/interfaces/`.
- Concrete repositories live in `src/infrastructure/repositories/` and inherit from domain interfaces.

## Known pitfalls

- Never create files or folders with Spanish names; all filesystem paths must be in English.
- Always check `AGENTS.md` and read project context before modifying code or planning artifacts.
- When generating deliverables, ensure English is primary and Spanish follows directly.

<!-- /bmad:context -->
