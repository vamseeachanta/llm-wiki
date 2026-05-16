# RAG benchmark

Issue [#78](https://github.com/vamseeachanta/llm-wiki/issues/78) adds a deterministic v1 benchmark for measuring whether llm-wiki is useful as a code-development retrieval surface.

## What it measures

- **Retrieval**: file-level hit@1, hit@3, and hit@k against expected repo-relative paths.
- **Citation discipline**: answers must cite required committed llm-wiki paths.
- **Answer rubric**: required facts must appear and expected-refusal questions must preserve public-safety boundaries. The deterministic v1 answer synthesizer may use only retrieved context snippets; gold fixture fields (`expected_paths`, `required_citations`, `required_facts`) remain evaluator inputs only.
- **Safety/integrity**: fixture and scorecards reject private mounts, secret-like tokens, and unsafe absolute paths. Scorecards include a full-file corpus manifest digest so validators detect stale artifacts even when retrieval-token windows are unchanged.
- **Gate strength**: validators enforce aggregate thresholds plus per-domain floors (`min_domain_*`) so a green scorecard cannot hide an entirely red domain slice.

## Run

```bash
uv run scripts/llm_wiki_rag_benchmark.py \
  --fixture tests/fixtures/rag-benchmark/questions.json \
  --output-json artifacts/retrieval/rag-benchmark/latest-scorecard.json \
  --output-md docs/reports/$(date +%F)-llm-wiki-rag-benchmark.md
```

## Validate

```bash
uv run scripts/validate_rag_benchmark.py \
  tests/fixtures/rag-benchmark/questions.json \
  docs/reports/$(date +%F)-llm-wiki-rag-benchmark.md \
  artifacts/retrieval/rag-benchmark/latest-scorecard.json
```

The benchmark is intentionally offline and stdlib-only. Do not add a model judge, external API calls, private corpus reads, or a scheduler in v1.
