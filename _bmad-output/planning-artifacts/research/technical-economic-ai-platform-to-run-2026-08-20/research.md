---
title: 'technical research: Cost-effective AI platform for running BMAD in Antigravity for PRESENTE'
type: 'technical'
topic: 'Cost-effective AI platform for running BMAD in Antigravity for PRESENTE'
decision: 'Choose the most cost-effective and sustainable platform for developing the PRESENTE MVP with BMAD'
source: 'PRESENTE.docx and official sources consulted on 2026-08-20'
status: complete
preset: 'standard'
validation: normal
created: '2026-08-20'
updated: '2026-08-20'
---

# Technical research: cost-effective AI platform for PRESENTE

**Decision:** choose the AI platform to work with BMAD and build the PRESENTE MVP without compromising essential medical resources.

## Executive summary

**Main recommendation: continue with Antigravity using the free Google/Gemini tier, with Gemini Flash as the working model and explicit budgets per interaction.** This is the only option reviewed that combines the environment you already have, command execution, file reading and editing, web access, persistent context, and mounting of `AGENTS.md`/`.agents/skills`, which are precisely the surfaces BMAD needs [1].

Free access does not mean unlimited guaranteed tokens: Google defines free-rate and quota limits that may change. Agentic interactions can go through several reasoning, tool, and execution cycles, so a single complex task can consume much more than a simple chat response. The documentation allows setting `max_total_tokens`, which should be a mandatory rule to protect the budget [1].

**Alternatives:** GitHub Copilot Free is a good complement for autocompletion and small tasks, with 2,000 monthly completions and Copilot CLI, but the published data does not present it as a broad quota for agentic BMAD sessions [2]. OpenRouter offers free and paid models, but availability changes by provider and model; in addition, its terms shift the review of provider practices to the user, and some free models may allow training on prompts and outputs [3][4]. That is why it is not the first choice for a project related to mental health.

## PRESENTE context

The initial document describes a small, managed, progressive MVP: content catalog, multimedia, resources, collaborator profiles, administration, and roles. It initially excludes diagnosis, clinical functions, patient tracking, private chat, open forums, and unrestricted publication. The initial team is very small, and the initiative aims to minimize infrastructure with free or low-cost services.

This changes the selection criteria: the AI must help define, design, program, test, and document; it must not receive clinical stories, identifiable testimonials, patient names, diagnoses, audio from people, or any sensitive data. The AI also must not decide clinical content or replace professional review.

## Decision requirements

| Criterion | Type | Weight | Practical rule |
|---|---:|---:|---|
| Compatibility with Antigravity/BMAD | Hard | 30% | Files, commands, skills, rules, and iteration in the repository |
| Current cost | Hard | 30% | Start at USD 0; pay only when an explicit budget exists |
| Capacity for code and long tasks | Preference | 20% | Context, tools, testing, and continuity |
| Privacy and control | Hard | 15% | Do not send health data; prefer training-free or local use |
| Portability | Preference | 5% | Ability to switch providers without rewriting the project |

## Finalist evaluation

Indicative score out of 5. This is not an independent benchmark; it synthesizes the capabilities and conditions published by each provider.

| Option | Compatibility | Cost | Agentic work | Privacy | Portability | Notes |
|---|---:|---:|---:|---:|---:|---|
| Antigravity + free Gemini | 5 | 5 | 5 | 2 | 3 | Best fit to start; requires anonymization because unpaid usage may be used to improve products |
| GitHub Copilot Free | 3 | 5 | 2 | 3 | 3 | Useful complement; 2,000 completions/month and CLI, but not the main BMAD quota |
| OpenRouter free models `:free` | 2 | 4 | 3 | 1-3 | 5 | Experimental fallback; limits, providers, and terms change by model |
| Free ChatGPT/Claude | 1-2 | 5 | 2 | 2-3 | 3 | Useful for manual queries; not the integrated base for the Antigravity repository |

## Findings by dimension

### Integration and architecture

Antigravity provides Bash, Python, and Node execution, file management, web search, URL context, compact context for long sessions, remote MCP, and customization through `AGENTS.md` and `.agents/skills` [1]. This fits BMAD directly: artifacts live in the repository, and the agent can run project verifications.

There are relevant limits: the documentation marks the agent and API as preview; it does not support direct audio, video, or document input, and some tools like `file_search` and `computer_use` are unavailable [1]. Therefore, the PRESENTE requirements DOCX must be converted to text or Markdown for BMAD work, and PRESENTE multimedia should be treated as product content, not automatic agent input.

### Cost and limits

Google offers a free layer with access to AI Studio and free input/output tokens for certain models, but with limited access, rate limits, and quotas that can change [5]. The Antigravity agent is billed according to model and tool usage; the free tier includes usage limits, not an infinite session promise [1]. The lowest financial-risk option is to keep billing disabled while learning and use small budgets per task.

The paid Gemini API has a privacy advantage: Google says it does not use prompts or responses to improve products in Paid Services [6]. However, that advantage matters only if a budget exists in the future; it does not justify enabling billing without controls.

### Real implementation for BMAD

The recommended flow is:

1. Use a single BMAD session for one decision or one small artifact.
2. Read `AGENTS.md`, the sprint state, and the target artifact first.
3. Ask for a short plan before editing.
4. Set a conservative `max_total_tokens` for agentic tasks and split large tasks.
5. Run tests or validations after each change.
6. Save results in `_bmad-output` and avoid relying on chat memory.
7. Switch to manual work or wait for the quota to reset when the limit is reached, without opening duplicate accounts or trying to bypass limits.

### Ecosystem and provider risk

OpenRouter allows selecting hundreds of models and checking prices and capabilities via API; free models may disappear or change [3]. Its terms indicate the service does not guarantee model availability, each provider has its own terms, and some providers may use prompts and outputs for training [4]. It is useful as an experiment with synthetic code, but it should not be the default path for sensitive information or a future service aimed at vulnerable people.

## Verdict

### Winner: Antigravity + free Gemini

It wins because of alignment with the workflow you already use, not because it offers “infinite tokens.” It is the option that minimizes adoption cost and allows BMAD to be used with files, rules, skills, and commands. The condition is to operate in development mode with synthetic or anonymized data.

### Runner-up: GitHub Copilot Free

It wins when work is autocompletion, minor fixes, or quick queries inside VS Code. I would not choose it as the primary engine for BMAD because the published free offer is framed as completions and limited access, not broad multi-step agent capacity [2].

### Strongest argument against the recommendation

The free Antigravity quota may be depleted or change, and unpaid usage may include human review and use of content to improve products [6]. If the project ever handles personal or clinical information, the free mode would not be appropriate. The risk is mitigated by keeping sensitive content out of the development repository, using fictional data, and, only after funding exists, evaluating a paid service with contractual safeguards.

## Zero-cost usage plan

- **USD 0:** Antigravity/Gemini free for BMAD, documentation, architecture, code, and tests with fictional data.
- **USD 0:** YouTube for initial audiovisual content and initial storage/distribution under its terms; keep this decision separate from the AI platform.
- **USD 0:** GitHub public or private as needed, verifying limits and avoiding uploading personal data.
- **USD 0 optional:** GitHub Copilot Free as a completions supplement.
- **Not recommended as the main path:** free OpenRouter for non-sensitive code only, reviewing provider by provider.
- **When a budget exists:** activate billing only with alerts, monthly limits, and a separate account/project; start with the Flash/Lite model and use Pro only for complex decisions.

## Essential protections for PRESENTE

- Do not send any AI clinical stories, names, phone numbers, emails, identifiable testimonials, recordings, faces, diagnoses, or patient information.
- Do not ask the AI for diagnoses, clinical classification, triage, treatment, or personalized recommendations.
- Keep human review of psychology/pastoral content for all public-facing material.
- Keep the development repository separate from the future content repository and any user database.
- Add a data policy and consent process before accepting testimonials or comments.
- Treat all AI-generated content as a draft subject to review.

## Next actions

1. Confirm that Antigravity is using an account/project with no billing or with a strict maximum budget.
2. Add or review `AGENTS.md` with BMAD rules, privacy, and clinical limits.
3. Convert `PRESENTE.docx` into a Markdown requirements artifact without attaching personal data.
4. Run BMAD first on the MVP scope and architecture, not on clinical features.
5. Measure for a week how many tasks and tokens the real workflow consumes before deciding on any payment.

## Sources

[1] Google, “Antigravity agent”, official documentation, updated 2026-08-18. https://ai.google.dev/gemini-api/docs/antigravity-agent

[2] GitHub, “GitHub Copilot plans”, official pricing page, consulted 2026-08-20. https://github.com/features/copilot/plans

[3] OpenRouter, “Models”, official documentation and model catalog, consulted 2026-08-20. https://openrouter.ai/docs/guides/overview/models ; https://openrouter.ai/models?q=free

[4] OpenRouter, “Terms of Service” and “Privacy Policy”, updated 2026-07-29 and 2026-07-06. https://openrouter.ai/terms ; https://openrouter.ai/privacy

[5] Google, “Gemini Developer API pricing”, official documentation, updated 2026-08-13. https://ai.google.dev/gemini-api/docs/pricing

[6] Google, “Gemini API Additional Terms of Service”, effective 2026-03-23. https://ai.google.dev/gemini-api/terms

**Freshness note:** this report should be reviewed before acting if more than two quarters have passed, or immediately if Antigravity/Gemini changes its quota scheme, models, or data terms.
