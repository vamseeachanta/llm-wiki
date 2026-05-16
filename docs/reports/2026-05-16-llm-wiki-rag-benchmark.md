# llm-wiki RAG benchmark scorecard — 2026-05-16

## Summary

- Schema: `rag-benchmark-scorecard/v1`
- Fixture: `rag-benchmark/v1` / `2026-05-16`
- Questions: 22
- Corpus files: 20051
- Corpus manifest SHA-256: `b832f5e076c70a57b6a8f4380f07e947b518108f71593d2b1411804c96a2e94e`

## Metric thresholds

- citation_pass_rate: 0.7
- hit_at_5: 0.8
- min_domain_citation_pass_rate: 0.6
- min_domain_hit_at_5: 0.6
- min_domain_rubric_pass_rate: 0.6
- rubric_pass_rate: 0.8

## Retrieval metrics

- hit_at_1: 0.6364
- hit_at_3: 0.7727
- hit_at_5: 0.8182

## Citation metrics

- citation_pass_rate: 0.7727

## Answer rubric metrics

- fact_pass_rate: 0.8182
- refusal_pass_rate: 1.0
- rubric_pass_rate: 0.8182

## Domain breakdown

| Domain | Count | hit@k | Citation pass | Rubric pass |
|---|---:|---:|---:|---:|
| code-results | 5 | 0.8 | 0.8 | 0.8 |
| governance | 3 | 1.0 | 1.0 | 1.0 |
| marine-offshore | 5 | 0.8 | 0.8 | 0.8 |
| production-engineering | 5 | 0.8 | 0.6 | 0.8 |
| standards | 4 | 0.75 | 0.75 | 0.75 |

## Failed questions

- `marine-002` hit@k=False citation=False rubric=False
- `standards-003` hit@k=False citation=False rubric=False
- `production-001` hit@k=False citation=False rubric=False
- `code-results-004` hit@k=False citation=False rubric=False
- `routing-002` hit@k=True citation=False rubric=True

## Public-safety statement

public-safe fixture/scorecard: repo-relative paths only; no private mounts, secrets, client/vendor/raw content.
