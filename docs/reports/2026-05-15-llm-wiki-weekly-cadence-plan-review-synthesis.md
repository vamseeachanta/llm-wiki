# LLM Wiki Weekly Cadence Plan Review Synthesis — 2026-05-15

## Scope

This synthesis covers the weekly-cadence / usefulness issue wave created from the llm-wiki repository review:

- #75 — Weekly freshness control loop
- #76 — `llms.txt` entrypoints and curated domain manifests
- #77 — Public-safe knowledge graph / link graph
- #78 — RAG evaluation benchmark
- #79 — Weekly OSS engineering tool watchlist
- #80 — CLI/MCP query surface

No implementation was performed. This artifact records adversarial review outcomes and the binding hardening now patched into each local plan.

## Review outcome summary

| Issue | Topic | Review verdict before hardening | Patched status | Residual risk | Approval posture |
|---:|---|---|---|---|---|
| #75 | Weekly freshness control loop | MINOR | Plan patched with JSON baseline/report contract, checked-in issue-routing source, bounded output, confidence/reason codes | Low | Ready for user approval |
| #76 | `llms.txt` entrypoints/manifests | MINOR | Plan patched with strict manifest section contract, deterministic hybrid authorship, caps, routing smoke tests | Low | Ready for user approval |
| #77 | Public-safe knowledge graph | MAJOR until schema/input scope hardened | Plan patched with two-layer graph contract, allowlisted inputs, versioned schema, provenance locators, negative tests | Medium | Ready for user approval if narrowed v1 is accepted |
| #78 | RAG evaluation benchmark | MAJOR until benchmark methodology frozen | Plan patched with benchmark-first scope, adapter contract, JSON fixtures, corpus versioning, refusal cases, thresholds | Medium | Ready for user approval if benchmark-first scope is accepted |
| #79 | Weekly OSS engineering tool watchlist | MAJOR until state/network contracts frozen | Plan patched with static config vs mutable state split, fixture/live modes, scan/render split, per-tool signal strategy | Medium | Ready for user approval if fixture-first/live-optional stance is accepted |
| #80 | CLI/MCP query surface | MAJOR until v1 narrowed | Plan patched with CLI-only v1, gated command matrix, query-source registry, structured response envelope, MCP deferred | Medium | Ready for user approval if CLI-only v1 is accepted |

## Cross-issue sequencing recommendation

Recommended approval/execution order:

1. **#75** — creates weekly control loop and report cadence.
2. **#76** — creates agent-readable entrypoints that make the repo cheaper to navigate.
3. **#79** — adds external concept/tool freshness input, but fixture-first to avoid noisy automation.
4. **#77** — builds structured relationship substrate after entrypoints and freshness contracts exist.
5. **#78** — benchmarks usefulness once retrieval surfaces are stable enough to score.
6. **#80** — exposes deterministic query surface; MCP remains follow-on after CLI contract is stable.

Parallelization note: #75, #76, and #79 can be implemented independently after approval. #77, #78, and #80 should be sequenced or explicitly feature-gated because they depend on artifact contracts created by the first wave.

## Binding constraints added across plans

- Prefer checked-in JSON contracts and fixture-backed tests for v1.
- Keep default validation offline/no-network.
- Separate live update scanning from deterministic report rendering.
- Do not expose private/client/vendor raw material; outputs must be public-safe summaries and path-bounded evidence.
- Use schema versions and stable artifact paths for every machine-readable output.
- Make gated/downstream behavior explicit instead of partially implementing hidden dependencies.

## Files patched

- `docs/plans/2026-05-15-issue-75-weekly-freshness-control-loop.md`
- `docs/plans/2026-05-15-issue-76-llms-entrypoints-domain-manifests.md`
- `docs/plans/2026-05-15-issue-77-public-safe-knowledge-graph.md`
- `docs/plans/2026-05-15-issue-78-rag-evaluation-benchmark.md`
- `docs/plans/2026-05-15-issue-79-weekly-oss-engineering-tool-watchlist.md`
- `docs/plans/2026-05-15-issue-80-cli-mcp-query-surface.md`

## Next gate

Post this synthesis to the six GitHub issues, move each issue to `status:plan-review`, and surface a compact approval packet to the user with links and recommended order.
