# llm-wiki weekly freshness report — 2026-05-16

## Run metadata
- Date: 2026-05-16
- Schema version: `weekly-freshness/v1`
- Baseline run date: 2026-05-15
- Roadmap anchor: https://github.com/vamseeachanta/llm-wiki/issues/13
- Public-safety note: public-safe metadata-only report; no raw/private/vendor/client content.
- Data sources: committed `wikis/` markdown, `data/concept_watchlist.json`, and `data/issue_routing_map.json` only.

## Repo freshness summary
| Metric | Value | Delta vs baseline |
|---|---:|---:|
| Total pages | 19964 | +12 |
| Missing frontmatter | 0 | +0 |
| Missing `last_updated` | 0 | +0 |
| Stale pages | 19275 | +0 |
| Broken internal markdown links | 10 | +9 |

## Domain coverage deltas
First weekly run is an absolute baseline. Future runs compare against the previous JSON artifact with the same schema version.

| Domain | Pages | Δ pages | Missing frontmatter | Δ missing FM | Missing `last_updated` | Δ missing updated | Stale pages | Δ stale | Broken links | Δ broken |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| acma-projects | 4 | +0 | 0 | +0 | 0 | +0 | 0 | +0 | 0 | +0 |
| asset-management | 25 | +0 | 0 | +0 | 0 | +0 | 0 | +0 | 0 | +0 |
| drilling-engineering | 128 | +0 | 0 | +0 | 0 | +0 | 0 | +0 | 1 | +0 |
| engineering | 128 | +0 | 0 | +0 | 0 | +0 | 74 | +0 | 3 | +3 |
| engineering-standards | 216 | +0 | 0 | +0 | 0 | +0 | 0 | +0 | 0 | +0 |
| lng-projects | 29 | +0 | 0 | +0 | 0 | +0 | 0 | +0 | 6 | +6 |
| marine-engineering | 19222 | +0 | 0 | +0 | 0 | +0 | 19165 | +0 | 0 | +0 |
| maritime-law | 82 | +0 | 0 | +0 | 0 | +0 | 0 | +0 | 0 | +0 |
| naval-architecture | 76 | +0 | 0 | +0 | 0 | +0 | 36 | +0 | 0 | +0 |
| production-engineering | 54 | +12 | 0 | +0 | 0 | +0 | 0 | +0 | 0 | +0 |

## Stale pages and structural findings
| Path | Last updated | Age days | Reason |
|---|---:|---:|---|
| `wikis/marine-engineering/wiki/concepts/cathodic-protection-system.md` | 2026-04-07 | 39 | last_updated older than 30 days |
| `wikis/marine-engineering/wiki/concepts/coating-breakdown.md` | 2026-04-07 | 39 | last_updated older than 30 days |
| `wikis/marine-engineering/wiki/concepts/corrosion-control.md` | 2026-04-07 | 39 | last_updated older than 30 days |
| `wikis/marine-engineering/wiki/concepts/long-period-swell-resonance.md` | 2026-04-07 | 39 | last_updated older than 30 days |
| `wikis/marine-engineering/wiki/concepts/mooring-line-failure.md` | 2026-04-07 | 39 | last_updated older than 30 days |
| `wikis/marine-engineering/wiki/concepts/process-safety.md` | 2026-04-07 | 39 | last_updated older than 30 days |
| `wikis/marine-engineering/wiki/concepts/sour-service.md` | 2026-04-07 | 39 | last_updated older than 30 days |
| `wikis/marine-engineering/wiki/entities/anode.md` | 2026-04-07 | 39 | last_updated older than 30 days |
| `wikis/marine-engineering/wiki/entities/compressor.md` | 2026-04-07 | 39 | last_updated older than 30 days |
| `wikis/marine-engineering/wiki/entities/flange.md` | 2026-04-07 | 39 | last_updated older than 30 days |
| `wikis/marine-engineering/wiki/entities/float-collar.md` | 2026-04-07 | 39 | last_updated older than 30 days |
| `wikis/marine-engineering/wiki/entities/float-shoe.md` | 2026-04-07 | 39 | last_updated older than 30 days |
| `wikis/marine-engineering/wiki/entities/gasket.md` | 2026-04-07 | 39 | last_updated older than 30 days |
| `wikis/marine-engineering/wiki/entities/lng-carrier-mooring.md` | 2026-04-07 | 39 | last_updated older than 30 days |
| `wikis/marine-engineering/wiki/entities/separator.md` | 2026-04-07 | 39 | last_updated older than 30 days |
| `wikis/marine-engineering/wiki/sources/001.md` | 2026-04-07 | 39 | last_updated older than 30 days |
| `wikis/marine-engineering/wiki/sources/001gs.md` | 2026-04-07 | 39 | last_updated older than 30 days |
| `wikis/marine-engineering/wiki/sources/002on.md` | 2026-04-07 | 39 | last_updated older than 30 days |
| `wikis/marine-engineering/wiki/sources/003.md` | 2026-04-07 | 39 | last_updated older than 30 days |
| `wikis/marine-engineering/wiki/sources/004.md` | 2026-04-07 | 39 | last_updated older than 30 days |
| `wikis/marine-engineering/wiki/sources/004a.md` | 2026-04-07 | 39 | last_updated older than 30 days |
| `wikis/marine-engineering/wiki/sources/004b.md` | 2026-04-07 | 39 | last_updated older than 30 days |
| `wikis/marine-engineering/wiki/sources/005.md` | 2026-04-07 | 39 | last_updated older than 30 days |
| `wikis/marine-engineering/wiki/sources/005es.md` | 2026-04-07 | 39 | last_updated older than 30 days |
| `wikis/marine-engineering/wiki/sources/006a.md` | 2026-04-07 | 39 | last_updated older than 30 days |

### Broken internal markdown links
| Source | Target | Reason |
|---|---|---|
| `wikis/drilling-engineering/wiki/concepts/jackup-rig.md` | `../entities/maersk-drilling-fleet.md` | missing-md-target |
| `wikis/engineering/wiki/concepts/canonical-spec-semantic-equivalence.md` | `../../../../../docs/maps/digitalmodel-orcawave-orcaflex-operator-map.md` | missing-md-target |
| `wikis/engineering/wiki/workflows/orcawave-orcaflex-fixture-expansion-cookbook.md` | `../../../../../docs/maps/digitalmodel-orcawave-orcaflex-operator-map.md` | missing-md-target |
| `wikis/engineering/wiki/workflows/orcawave-orcaflex-fixture-expansion-cookbook.md` | `../../../../../docs/maps/digitalmodel-orcawave-orcaflex-operator-map.md` | missing-md-target |
| `wikis/lng-projects/wiki/standards/csa-z276.md` | `../../../../../.claude/rules/calc-citation-contract.md` | missing-md-target |
| `wikis/lng-projects/wiki/standards/en-1473.md` | `../../../../../.claude/rules/calc-citation-contract.md` | missing-md-target |
| `wikis/lng-projects/wiki/standards/ibc-code.md` | `../../../../../.claude/rules/calc-citation-contract.md` | missing-md-target |
| `wikis/lng-projects/wiki/standards/igc-code.md` | `../../../../../.claude/rules/calc-citation-contract.md` | missing-md-target |
| `wikis/lng-projects/wiki/standards/nfpa-59a.md` | `../../../../../.claude/rules/calc-citation-contract.md` | missing-md-target |
| `wikis/lng-projects/wiki/standards/phmsa-49-cfr-193.md` | `../../../../../.claude/rules/calc-citation-contract.md` | missing-md-target |

## Concept watchlist
| Concept | Why it matters | Public reference |
|---|---|---|
| llms.txt | Agent-friendly repo/site entrypoints and curated markdown manifests. | https://llmstxt.org/ |
| Model Context Protocol (MCP) | Standard tool/context protocol for agent query surfaces and future llm-wiki integrations. | https://modelcontextprotocol.io/ |
| GraphRAG / LightRAG | Graph-backed retrieval patterns for entity, community, and citation-aware knowledge navigation. | https://github.com/microsoft/graphrag |
| RAG evaluation | Faithfulness, context precision/recall, and answer-correctness checks for downstream code-assistant usefulness. | https://docs.ragas.io/ |

## Issue recommendations
| Action | Issue | Issue route | Reason code | Confidence | Title | Public-safe summary |
|---|---|---|---|---|---|---|
| comment-on-roadmap | [#13](https://github.com/vamseeachanta/llm-wiki/issues/13) | `portfolio-roadmap` | `portfolio-weekly-summary` | high | Roadmap anchor update | Post weekly freshness summary and domain deltas to the roadmap anchor instead of opening a duplicate umbrella. Route stale metadata, missing frontmatter, and broken-link deltas through the existing roadmap queue for prioritization. |
| comment-on-roadmap | [#13](https://github.com/vamseeachanta/llm-wiki/issues/13) | `llms-entrypoints` | `concept-llms-entrypoints` | high | llms.txt entrypoints | Track curated public concept `llms.txt` through `llms-entrypoints`; #75 reports the signal but does not implement adjacent feature scope. |
| comment-on-roadmap | [#13](https://github.com/vamseeachanta/llm-wiki/issues/13) | `oss-watchlist` | `concept-oss-watchlist` | medium | Weekly OSS engineering-tool watchlist | Track curated public concept `RAG evaluation` through `oss-watchlist`; #75 reports the signal but does not implement adjacent feature scope. |

## Blocked / approval-gated lanes
- [#76](https://github.com/vamseeachanta/llm-wiki/issues/76), [#77](https://github.com/vamseeachanta/llm-wiki/issues/77), [#78](https://github.com/vamseeachanta/llm-wiki/issues/78), [#79](https://github.com/vamseeachanta/llm-wiki/issues/79), and [#80](https://github.com/vamseeachanta/llm-wiki/issues/80) are adjacent lanes. #75 reports on their status categories but does not implement their feature scope.
- Approval-gated or unapproved lanes must stay as issue recommendations only until explicitly moved through the repo workflow.

## Validation evidence
- `uv run pytest tests/test_llm_wiki_weekly_freshness.py tests/test_weekly_freshness_artifacts.py -q`
- `uv run python scripts/llm_wiki_weekly_freshness.py --date 2026-05-16 --write`
- `uv run python scripts/validate_weekly_freshness_report.py docs/reports/2026-05-16-llm-wiki-weekly-freshness-report.md && uv run python scripts/validate_issue_route_state.py data/issue_routing_map.json data/oss_tool_issue_map.json`

## Public-safety guardrail
This artifact is public-safe: it contains summary metadata, repo-relative committed paths, public issue links, and public concept URLs only.
