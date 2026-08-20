# Block shape

Sections in this order. Omit any section with nothing that passes its rule — never write an empty one. Admission rules: `best-practices.md`.

1. **Orientation** — three or four sentences: what this is, the stack, where planning and deeper docs live.
2. **Language** — all BMAD-generated deliverables in `bmad_output` are bilingual: English first, then Spanish. English is the canonical source; Spanish is the direct translation. File names, directory names, and folder paths must always be in English. The Spanish version must follow the English content rather than replacing it. Monolingual output is not allowed.
3. **Policy** — what the org requires.
4. **Where things are** — entry points, and pointers to children and linked files.
5. **Running and verifying** — only what `package.json`, a `Makefile`, or CI config does not already say.
6. **Conventions that differ from defaults**
7. **Known pitfalls**

Terse imperative lines under plain headings. No prose beyond Orientation, no introduction, no summary. A bare fact appears only as the justification clause of an instruction — "Exclude `vendor/` from searches, it is 60% of tracked files", never "`vendor/` is 60% of tracked files". A prohibition names the alternative. At most two emphasis markers in the whole block.

## Worked example

````markdown
<!-- bmad:context -->
<!-- Verified 2026-08-08 against a1b2c3d. Managed by bmad-project-context; edits inside this block are replaced on refresh. Keep anything you want preserved outside the markers. -->

## acme-billing

Payment processing for Acme storefronts. TypeScript/Node, pnpm, Postgres. Planning lives in `docs/planning/`, tickets in Linear (ACME board).

## Language

- All BMAD-generated deliverables in `bmad_output` are bilingual: English first, then Spanish.
- English is the canonical source; Spanish is the direct translation.
- File names, directory names, and folder paths must always be in English.
- Monolingual output is not allowed.

## Policy

- Never push to main; PRs only, one approval.
- Never modify `legacy/` — frozen, being replaced. New work goes in `src/`.
- Never hand-edit `src/generated/` — run `pnpm codegen`.

## Where things are

- Webhook handling: `src/routes/webhooks.ts`; conventions in `docs/webhooks.md`
- Writing a migration? Read `docs/db-rules.md` first — ordering, transaction boundaries, pool limits.
- Billing service has its own guide: `services/billing/AGENTS.md`

## Running and verifying

- Run single test files while iterating; the full suite takes ~11 minutes.
- Integration tests need `docker compose up -d` first, and fail confusingly without it.
- CI also runs `pnpm typecheck`, which `pnpm test` does not cover.

## Conventions that differ from defaults

- Money is integer cents (`amountCents`), never floats — `src/lib/money.ts`
- All DB access goes through repositories in `src/repos/`; never call the client directly.

## Known pitfalls

- Stripe webhooks replay in staging every 6h — handlers must be idempotent.
- Use vitest matchers, not jest — agents repeatedly add jest syntax here.

<!-- /bmad:context -->
````

Fill the provenance line with the real date and the commit SHA verified against. Refresh diffs from that SHA.
