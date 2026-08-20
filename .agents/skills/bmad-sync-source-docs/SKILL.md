---
name: bmad-sync-source-docs
description: Synchronizes live external Google Docs and source documentation into the local docs/ directory before running BMAD analysis, PRD creation, or architecture design.
---
# BMad Sync Source Docs

Synchronizes live project input sources (such as shared Google Docs) to ensure BMAD agents always work with real-time, updated documentation rather than stale local copies.

## Live Sources
- **PRESENTE MVP Document:** `https://docs.google.com/document/d/1ITIkSfXrBsBcQUikDZKATdGbFsCSNM7so-M235DBM1I/export?format=txt`
- **Target Local File:** `{project-root}/docs/present-mvp-proposal.md`

## Instructions for Agent
1. When activated, fetch the live text from the Google Doc export URL using `read_url_content` or HTTP GET:
   - URL: `https://docs.google.com/document/d/1ITIkSfXrBsBcQUikDZKATdGbFsCSNM7so-M235DBM1I/export?format=txt`
2. Inspect the latest fetched content for any updates, additions, or changes made by collaborators in the shared document.
3. Write or refresh the synchronized content into `{project-root}/docs/present-mvp-proposal.md`.
4. Provide a brief confirmation of sync status (date, key changes detected, or confirmation that the latest version is loaded) before handing off to the next BMAD workflow step (e.g. `bmad-prd`).
