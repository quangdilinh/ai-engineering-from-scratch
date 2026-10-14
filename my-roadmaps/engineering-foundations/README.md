# Engineering Foundations — Required Parallel Roadmap

**Status:** Planned / initial assessment pending. **Reviewed:** 2026-10-14.

These foundations remain compulsory for Enterprise AI Delivery. Prior hands-on experience should be **assessed**, not automatically assumed sufficient or reset to zero.

| Area | Lessons and references | Evidence / acceptance |
|---|---|---|
| Python and development | [Python for AI](../../phases/00-setup-and-tooling/13-python-for-ai-engineering), [environments](../../phases/00-setup-and-tooling/06-python-environments), [debugging](../../phases/00-setup-and-tooling/12-debugging-and-profiling) | Typed, tested Python package/API; dependencies reproducible |
| Git and Linux | [Git](../../phases/00-setup-and-tooling/02-git-and-collaboration), [Linux](../../phases/00-setup-and-tooling/11-linux-for-ai) | Feature branch, review, reproducible shell tasks and rollback |
| Containers and operational practice | [Docker for AI](../../phases/00-setup-and-tooling/07-docker-for-ai), [SRE](../../phases/17-infrastructure-and-production/23-sre-for-ai) | Nonprivileged service, bounded resources, health check, observable failures |
| API and data contracts | [APIs/keys](../../phases/00-setup-and-tooling/04-apis-and-keys), [tool interfaces](../../phases/13-tools-and-protocols/01-the-tool-interface), [tool schema](../../phases/13-tools-and-protocols/05-tool-schema-design) | Typed request/response, error/retry/idempotency and authentication tests |
| Data/SQL | [Data management](../../phases/00-setup-and-tooling/09-data-management), [ML pipelines](../../phases/02-ml-fundamentals/13-ml-pipelines) | Schema tests, update/delete, source provenance, SQL authorization |
| Statistics and ML | [Model evaluation](../../phases/02-ml-fundamentals/09-model-evaluation), [feature engineering](../../phases/02-ml-fundamentals/08-feature-engineering) | Explain precision/recall, leakage, overfitting, uncertainty and baseline comparisons |
| LLM internals | [Self-attention](../../phases/07-transformers-deep-dive/02-self-attention-from-scratch), [tokenizers](../../phases/10-llms-from-scratch/01-tokenizers), [quantization](../../phases/10-llms-from-scratch/11-quantization) | Explain inference, tokens, context, embeddings, latency and model limits |
| Secure engineering | [Guardrails](../../phases/11-llm-engineering/12-guardrails), [security and audit](../../phases/17-infrastructure-and-production/25-security-secrets-audit) | Negative authorization tests, secret handling, no public admin access |

Curriculum reference: [Software Engineering Fundamentals](../../learning-paths/software-engineering-fundamentals.json).

## How to study

1. Take a short baseline assessment and record **Proven / Needs practice / Not yet learned** for every area.
2. Study the missing fundamentals **in parallel** with the next Enterprise AI Delivery milestone.
3. Use implementation and tests as proof; reading/watching is not sufficient.
4. Avoid unnecessary full deep-learning research prerequisites; learn how inference/retrieval works before trying complex training or fine-tuning.

## First deliverable

Build a minimal typed Python API using synthetic inputs with automated tests, a Docker Compose deployment, explicit permissions and a basic latency/error report. Use it as the base for the first Enterprise AI project.
