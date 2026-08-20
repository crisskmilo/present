# PRESENTE - And Remember You Are Not Alone

Digital accompaniment platform for mental health, providing responsible, vetted content across psychological well-being, pastoral/spiritual support, and curated lived experiences.

## Project Sources & Documentation

- **Live Source (Google Docs):** [PRESENTE - MVP Proposal Document](https://docs.google.com/document/d/1ITIkSfXrBsBcQUikDZKATdGbFsCSNM7so-M235DBM1I/edit?usp=sharing)
- **Local Synchronized Document:** [`docs/present-mvp-proposal.md`](./docs/present-mvp-proposal.md)

## BMAD Framework Integration

- **Sync Skill:** `.agents/skills/bmad-sync-source-docs/SKILL.md` (fetches the live Google Doc prior to PRD & planning runs).
- **PRD Workflow Customization:** `_bmad/custom/bmad-prd.toml` (auto-triggers `bmad-sync-source-docs` and injects `docs/present-mvp-proposal.md` as persistent context).
- **Planning Artifacts:** `_bmad-output/planning-artifacts/`