---
name: bmad-project-rules
description: Enforces PRESENTE project guardrails: 100% English code/naming, English base documentation with optional Spanish translations, Clean Architecture with IoC in FastAPI, and $0 cost deployment topology.
---
# BMad Project Rules & Context Guardian

## Purpose
This skill ensures all AI agents and BMAD workflows adhere strictly to the foundational invariants of the **PRESENTE** repository.

## Non-Negotiable Invariants

### 1. English-First Rule
- **Code & Identifiers**: Variable names, function names, class names, file names, folder names, docstrings, and inline comments MUST be in **English**.
- **Documentation**: All formal planning artifacts (PRDs, Solution Architecture, Epics, Stories, Specifications) must be authored in **English** as the primary base language.
- **Translations**: Spanish documents are allowed strictly as translations with the `.es.md` extension (e.g., `present-mvp-proposal.es.md`).

### 2. Clean Architecture & IoC (FastAPI)
- Layers: `domain/`, `application/`, `infrastructure/`, `api/`, `core/`.
- Repositories must define abstract contracts (`abc.ABC`) in `domain/interfaces/`.
- Concrete persistence belongs in `infrastructure/repositories/`.
- Dependency injection must be wired via `src/api/deps.py` or `src/core/container.py`.

### 3. $0 Cost Budget Constraint
- Architecture must only rely on zero-cost tiers: Vercel/Cloudflare (Frontend), Render/Oracle Always Free (Backend), Supabase (Database), Google AI Studio (AI Tokens).
