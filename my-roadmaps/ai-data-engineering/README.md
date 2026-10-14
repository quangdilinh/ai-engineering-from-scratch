# AI Data Engineering — Optional Specialization

**Status:** Backlog, not started. **Reviewed:** 2026-10-14.

**Objective:** Prepare accurate, fresh, authorized and traceable data for retrieval, model integration and evaluation; complement existing SQL/data-pipeline experience rather than recreate an entire distributed data platform.

References:

- [AI Data Systems learning path](../../learning-paths/ai-data-engineer.json)
- [Data management](../../phases/00-setup-and-tooling/09-data-management)
- [Embeddings](../../phases/11-llm-engineering/04-embeddings)
- [RAG](../../phases/11-llm-engineering/06-rag)
- [Advanced RAG](../../phases/11-llm-engineering/07-advanced-rag)
- [Evaluation](../../phases/11-llm-engineering/10-evaluation)
- [LLM observability](../../phases/17-infrastructure-and-production/13-llm-observability)

## Milestones

1. **Source and contract:** define permitted datasets, schema, quality tests, ownership and retention.
2. **Ingest and version:** demonstrate incremental updates, deletion propagation, idempotency and provenance.
3. **Retrieve:** build simple keyword/vector baselines, then justify hybrid search/reranking with measured improvements.
4. **Permission enforcement:** filter documents or rows by identity **before retrieval**, with negative security tests.
5. **Evaluate and operate:** regression suite for quality/freshness, storage cost, monitoring and restart/recovery behavior.

**Candidate project:** [RAG Freshness Pipeline](../../projects/rag-freshness-pipeline) or [Retrieval Evaluation Lab](../../projects/retrieval-evaluation-lab).

**Exit evidence:** repeatable pipeline and versioned tests handling new, changed, deleted, denied and stale sources. Data & AI Platform infrastructure is optional; introducing Kafka, Spark, Flink or a catalog needs a concrete workload.
