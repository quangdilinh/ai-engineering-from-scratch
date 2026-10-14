# AI Platform & LLMOps — Optional Specialization

**Status:** Backlog, not started. **Reviewed:** 2026-10-14.

**Objective:** Deploy, secure, benchmark, observe and recover an AI service. Learn portable operational principles first; do not equate enterprise deployment with self-hosting.

References:

- [Building and Deploying AI Applications](../../learning-paths/building-and-deploying-ai-applications.json)
- [AI Evaluation and Reliability](../../learning-paths/ai-evaluation-reliability-engineer.json)
- [Self-hosted serving selection](../../phases/17-infrastructure-and-production/28-self-hosted-serving-selection)
- [Inference metrics](../../phases/17-infrastructure-and-production/08-inference-metrics-goodput)
- [Quantization](../../phases/17-infrastructure-and-production/09-production-quantization)
- [Observability](../../phases/17-infrastructure-and-production/13-llm-observability)
- [Load testing](../../phases/17-infrastructure-and-production/22-load-testing-llm-apis)
- [Security, secrets and audit](../../phases/17-infrastructure-and-production/25-security-secrets-audit)
- [SRE for AI](../../phases/17-infrastructure-and-production/23-sre-for-ai)

## Milestones

1. **Architecture choice:** compare managed API, private inference and hybrid on data policy, reliability, operations and estimated cost.
2. **Reproducible private service:** pinned images, non-root where practical, bounded CPU/GPU/RAM, explicit networks, health checks, secrets outside Git.
3. **Benchmark:** report TTFT, p50/p95 latency, error rate, goodput, resource utilization and cost/task under stated load.
4. **Safety & reliability:** authentication, rate limits, threat model, monitoring, failure injection, restart/recovery and rollback tests.
5. **Controlled rollout:** describe shadow/canary or limited pilot, SLOs, change approval and human escalation.

**Candidate project:** [Local Model Evaluation Harness](../../projects/local-model-eval-harness), without assuming the home GPU or server is always available.

**Exit evidence:** reproducible deployment and load/evaluation report, security negative tests, and demonstrated rollback. Kubernetes and multi-node serving are deferred until clearly justified.
