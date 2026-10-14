# Personal AI Engineering Roadmaps

Status: **Planned / learning only**. Last reviewed: 2026-10-14.

## Goal

Build transferable skills for **deploying reliable AI solutions in enterprises** without committing prematurely to one job title. Business outcomes come first; software engineering, machine learning and LLM foundations remain compulsory.

| Roadmap | Role | Status |
|---|---|---|
| [Enterprise AI Delivery](enterprise-ai-delivery/README.md) | **Primary:** discover, design, validate, integrate and roll out AI workflows | Planned |
| [Engineering Foundations](engineering-foundations/README.md) | **Required parallel track:** Python, APIs, testing, data, ML/LLM basics, security | Planned |
| [AI Data Engineering](ai-data-engineering/README.md) | Optional specialization in ingestion, RAG data and provenance | Backlog |
| [AI Platform & LLMOps](ai-platform-llmops/README.md) | Optional specialization in serving, reliability, security and cost | Backlog |

## Maintenance contract

- **One roadmap = one folder**. New roadmaps do not need a separate long-lived Git branch.
- Each roadmap links to existing `phases/`, `learning-paths/` and `projects/` rather than copying lesson content.
- Keep upstream-owned directories unchanged initially. Use short-lived `feat/<topic>` branches, PR into **this fork's** `main`.
- Course material is a study resource. Passing an upstream lesson is not proof of production readiness.
- Do not automatically deploy sample software or allow agents privileged access to homelab infrastructure.
- Each roadmap owns its scope, milestones, evidence, status and next decision.
- The canonical infrastructure state stays in the separate `homelab-doc` repository. This fork owns learning plans and exercises, **not** operational host facts.
- Preserve the upstream MIT LICENSE and copyright notice.

## Shared completion rubric

1. **Explain:** what problem the technique solves, trade-offs, failure modes.
2. **Implement:** reproducible code and tests on authorized/public/synthetic data.
3. **Evaluate:** explicit baseline, metrics and regression set.
4. **Secure:** identify authorization, data-exposure and untrusted-input risks.
5. **Operate:** run privately, observe failure, recover and roll back.

## Learning artifacts

Keep non-secret artifacts (evaluation fixtures, design notes, metrics summaries) with the owning roadmap or a separate project repository. Never commit credentials, customer/private employer data, full raw prompts containing PII, or sensitive infrastructure exports.

## Next action

Begin [Enterprise AI Delivery milestone 1](enterprise-ai-delivery/README.md#milestone-1--find-and-scope-a-real-business-problem) and assess gaps in [Engineering Foundations](engineering-foundations/README.md). Prioritize a single end-to-end use case before adding stacks and frameworks.
