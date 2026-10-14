# Enterprise AI Delivery — Primary Roadmap

**Status:** Planned / not started. **Reviewed:** 2026-10-14.

## Outcome

Be able to take a business workflow from discovery through an evaluated, integrated, secure pilot and an operational handoff. Do not assume every workflow requires a large language model, RAG or autonomous agent.

Parallel prerequisite: [Engineering Foundations](../engineering-foundations/README.md). Skip a lesson only when its competency is demonstrated through evidence, not familiarity.

Reference curricula (reuse, do not copy):

- [Customer AI Deployment](../../learning-paths/forward-deployed-ai-engineer.json)
- [LLM Product Engineering](../../learning-paths/applied-ai-engineer.json)
- [Building and Deploying AI Applications](../../learning-paths/building-and-deploying-ai-applications.json)
- [Product Judgment and Delivery](../../learning-paths/shaping-the-build.json)
- [AI Evaluation and Reliability](../../learning-paths/ai-evaluation-reliability-engineer.json)

## Milestone 1 — Find and scope a real business problem

Learn discovery and decision-making using:

- [Outcomes before output](../../phases/14-agent-engineering/47-outcomes-before-output)
- [Discover the actual workflow](../../phases/14-agent-engineering/48-discover-the-real-workflow)
- [Map assumptions and risks](../../phases/14-agent-engineering/49-map-assumptions-and-risk)
- [Choose the smallest testable slice](../../phases/14-agent-engineering/50-choose-the-smallest-testable-slice)
- [Write an executable specification](../../phases/14-agent-engineering/51-write-specifications-that-preserve-judgment)

**Evidence:** Two use-case briefs, documented current workflows, baseline metrics, data permission boundaries, owner/decision maker, cost-of-error, non-AI alternatives. Choose **one** problem.

**Gate:** Do not proceed if outcome, permitted dataset, baseline and success criteria remain undefined.

## Milestone 2 — Build the smallest useful AI feature

- [Prompt engineering](../../phases/11-llm-engineering/01-prompt-engineering)
- [Structured outputs](../../phases/11-llm-engineering/03-structured-outputs)
- [Embeddings](../../phases/11-llm-engineering/04-embeddings)
- [Context engineering](../../phases/11-llm-engineering/05-context-engineering)
- [RAG](../../phases/11-llm-engineering/06-rag)
- [Function calling](../../phases/11-llm-engineering/09-function-calling)
- [Evaluation](../../phases/11-llm-engineering/10-evaluation)

**Suggested first project:** [Document Q&A with Citations](../../projects/doc-qa-with-citations), extended with versioned ingestion, document deletion/update handling, permission-filtered retrieval, citations and explicit abstention. Use **public or synthetic** content only until the legal owner authorizes anything else.

**Gate:** Baseline comparison, golden cases, grounded-answer tests, missing/deleted document tests and forbidden-document access tests pass.

## Milestone 3 — Integrate into enterprise systems safely

- [Tool interface](../../phases/13-tools-and-protocols/01-the-tool-interface)
- [Tool schema design](../../phases/13-tools-and-protocols/05-tool-schema-design)
- [MCP fundamentals (optional protocol)](../../phases/13-tools-and-protocols/06-mcp-fundamentals)
- [Tool-poisoning risk](../../phases/13-tools-and-protocols/15-mcp-security-tool-poisoning)
- [Tool contracts and content](../../phases/13-tools-and-protocols/28-mcp-tool-contracts-and-content)
- [Reliability, cancellation and flow control](../../phases/13-tools-and-protocols/29-mcp-reliability-cancellation-and-flow-control)
- [Workflow patterns](../../phases/14-agent-engineering/12-anthropic-workflow-patterns)
- [Prompt injection defense](../../phases/14-agent-engineering/27-prompt-injection-defense)

**Evidence:** Typed API/tool contracts, application-side authentication and authorization, least-privilege read-only integration, audit events, retries/idempotency/timeout handling, prompt-injection negative tests.

**Gate:** The LLM cannot authorize itself; untrusted documents/tool results cannot change privilege; consequential actions require a separate explicit approval boundary. Avoid autonomous agents when a deterministic workflow works.

## Milestone 4 — Evaluate quality and business impact

- [Evaluation](../../phases/11-llm-engineering/10-evaluation)
- [Agent evaluation](../../phases/14-agent-engineering/30-eval-driven-agent-development)
- [Failure modes](../../phases/14-agent-engineering/26-failure-modes-agentic)
- [Success metrics](../../phases/14-agent-engineering/52-design-success-metrics)

**Evidence:** Versioned representative eval set (including stale data, unauthorized requests and adversarial inputs), retrieval metrics separated from answer quality, cost per successful business task, failure analysis and comparison with a non-AI workflow.

**Gate:** Risk-adjusted success criteria were set *before* the final run and met; security bypass tests pass.

## Milestone 5 — Ship and operate a limited pilot

- [Production app](../../phases/11-llm-engineering/13-production-app)
- [LLM observability](../../phases/17-infrastructure-and-production/13-llm-observability)
- [Security, secrets, audit](../../phases/17-infrastructure-and-production/25-security-secrets-audit)
- [Shadow/canary rollout](../../phases/17-infrastructure-and-production/20-shadow-canary-progressive)
- [SRE for AI](../../phases/17-infrastructure-and-production/23-sre-for-ai)
- [Prototype, pilot or production](../../phases/14-agent-engineering/53-prototype-pilot-or-production)

**Evidence:** Reproducible deployment (Docker Compose is sufficient), private/VPN access, telemetry (quality, p95 latency, cost, errors), an owner, runbook, rollback demo and measured user feedback.

**Gate:** Deployment does not grant model/agent administrative access to SSH, Docker socket, Proxmox, routers or databases; experiment cannot starve critical homelab services.

## Milestone 6 — Demonstrate and decide

- [Build the feedback loop](../../phases/14-agent-engineering/54-build-the-feedback-ratchet)

Produce a concise case study: user problem, alternatives, architecture, baseline, business metric, evaluations, threats/mitigations, cost/latency, failures, rollout and next iteration. Review relevant job listings before deciding whether to lean into AI delivery, AI data or LLMOps.

## Progress

See [PROGRESS](PROGRESS.md). Milestones are evidence-gated rather than time-gated. Do not label a hobby proof-of-concept an enterprise production deployment.
