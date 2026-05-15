---
title: "Issue #80 plan — CLI-first query surface for llm-wiki manifests and retrieval"
issue: 80
status: plan-review
created: 2026-05-15
last_updated: 2026-05-15
public_safety: query only over committed public-safe manifests/reports; no raw/private paths, vendor/client content, copied standards text, or secret-bearing outputs
---

# Issue #80 Plan — CLI-First Query Surface for llm-wiki Manifests and Retrieval

## Approval-gate note

- GitHub issue: [vamseeachanta/llm-wiki#80](https://github.com/vamseeachanta/llm-wiki/issues/80)
- Local plan status: `plan-review`
- Implementation status: **planning only; no CLI, MCP server, or retrieval code implemented in this pass**
- This artifact does **not** authorize code changes beyond this plan file, GitHub issue edits, label changes, comments, or MCP server implementation.
- Per repo workflow, implementation should begin only after explicit user approval and the issue is advanced to the approved state by the main agent.

## Summary

Issue #80 should define a **CLI-first, JSON-stable query surface** for `llm-wiki` so agents can ask bounded questions against curated manifests, graph outputs, and retrieval fixtures without scraping repository prose ad hoc.

The recommended implementation order is:

1. ship a local repo CLI over committed, public-safe artifacts first;
2. stabilize command names, input arguments, output schemas, and safety rules;
3. document how agents in `workspace-hub` / `digitalmodel` should consume the CLI;
4. only then add a thin MCP wrapper that exposes the same stable contract as MCP resources/tools.

This keeps #80 narrow and practical: the first milestone is **safe query access to existing/generated artifacts**, not a general retrieval platform, not networked serving, and not a broad GraphRAG system.

## Current evidence / intelligence

Fresh inspection on 2026-05-15 covered the live issue, adjacent roadmap issues, and the exact repo files most relevant to manifests, graph outputs, safety validation, and query-surface precedent.

### Live issues inspected

1. [#80](https://github.com/vamseeachanta/llm-wiki/issues/80) — target issue; requires CLI-first architecture, MCP/resource candidates after schema stabilization, strict public-safety filters, and agent-consumption docs.
2. [#13](https://github.com/vamseeachanta/llm-wiki/issues/13) — roadmap umbrella; #80 should remain a child execution lane, not a replacement umbrella.
3. [#76](https://github.com/vamseeachanta/llm-wiki/issues/76) — `llms.txt` entrypoints; relevant upstream discovery surface that #80 should query/reference rather than re-encode.
4. [#77](https://github.com/vamseeachanta/llm-wiki/issues/77) — public-safe knowledge-graph/link-graph manifests; primary structured-artifact dependency for graph-backed query commands.
5. [#78](https://github.com/vamseeachanta/llm-wiki/issues/78) — retrieval benchmark; query surface should support benchmark context lookup later but must not absorb benchmark design.
6. [#79](https://github.com/vamseeachanta/llm-wiki/issues/79) — weekly OSS watchlist; future queryable feed, but watchlist ingestion/scanning stays out of scope here.

### Exact repo files inspected

Repo/governance/plan surfaces:

1. `README.md` — repo purpose, layout, license split, and public/private boundary.
2. `CLAUDE.md` — repo-local agent firewall and routing constraints.
3. `docs/plans/README.md` — canonical plan workflow and approval-gate/public-safety rules.
4. `docs/plans/2026-05-15-issue-76-llms-entrypoints-domain-manifests.md` — adjacent manifest-entrypoint plan and explicit non-overlap with #80.
5. `docs/plans/2026-05-15-issue-77-public-safe-knowledge-graph.md` — graph artifact contract and explicit dependency note that #80 should wait for stable schema.
6. `docs/governance/service-provider-data-routing.md` — six-route matrix for what must remain off-repo or URL-only.
7. `docs/reports/2026-05-11-llm-wiki-completion-control-plane.md` — practical-completion rules, raw/private boundary, and repo-local verification contract.

Existing query-relevant content/artifact surfaces:

8. `wikis/cross-links-tier1.md` — existing code/data/results/governance link map.
9. `wikis/marine-engineering/wiki/code-results-links.md` — concrete implementation/result link page pattern.
10. `wikis/engineering/wiki/public-data-software-links.md` — concrete data/software link page pattern.
11. `wikis/marine-engineering/wiki/index.md` — confirms very large domain scale (`page_count: 19214`, `source_count: 19169`) that justifies a query surface.
12. `wikis/engineering/wiki/index.md` — smaller domain index useful for first-pass deterministic query fixtures.
13. `wikis/engineering-standards/wiki/index.md` — standards-heavy domain index for metadata and standards-lookup operations.

Script/test precedent surfaces:

14. `scripts/llm_wiki_strengthening_scorecard.py` — dependency-light parser/report pattern over committed markdown.
15. `scripts/validate_completion_artifacts.py` — validator pattern for required phrases/links plus forbidden path and secret scanning.
16. `scripts/validate_governance_artifacts.py` — deterministic artifact validator precedent.
17. `tests/test_completion_artifacts.py` — importlib-based validator regression pattern.
18. `tests/test_governance_artifacts.py` — deterministic path/phrase validation tests.
19. `tests/test_scan_source_families_safe.py` — safety-test precedent for no path leakage and redaction behavior.

Repo-structure check:

20. search for `llms*.txt` returned no current files, confirming #76 is still planning-stage and #80 cannot assume manifests already exist.
21. search for `pyproject.toml`, `uv.lock`, `requirements*`, `pytest.ini`, `tox.ini` returned no matches, reinforcing the current repo pattern of dependency-light scripts executed directly via `uv run python ...`.

### Key intelligence derived from inspection

- `llm-wiki` already has **public-safe link/report artifacts** but no canonical query contract; agents still have to infer where to look.
- #76 and #77 define the most important future machine-consumable inputs, but neither issue defines how an agent should ask questions against them; #80 closes that gap.
- The repo strongly prefers **deterministic, local, dependency-light Python scripts and validators** rather than heavy frameworks; #80 should follow that shape for v1.
- Safety rules are already strong and repeated across README/governance/validators: query outputs must stay **repo-relative, metadata-only, and secret/path-safe**.
- The marine domain is too large for naive traversal, so #80 adds the most value when it lets agents ask targeted questions like “where are code/result links for X?” or “which standards page matches this code id?”
- Because `llms.txt` and graph artifacts are not yet implemented, #80 should define a **layered dependency model**: ship CLI contract/tests first, but gate graph-backed and manifest-backed commands on the schemas approved in #76/#77.

## Problem statement specific to #80

Today, an agent that wants to answer a bounded question about `llm-wiki` typically has to:

- inspect README and governance docs manually;
- search indexes and link pages heuristically;
- scrape markdown to discover standards, code/result links, or blockers;
- reimplement retrieval logic in each downstream repo or agent session.

That is slow, inconsistent, and risky for a public-safe repo with explicit boundaries.

Issue #80 should provide a **small, canonical query layer** so agents can ask focused questions like:

- what domains are available?
- where should I start for a topic?
- what page summarizes concept X?
- what public code/result links operationalize this topic?
- what standards metadata applies to code ID Y?
- what public clearance blockers are documented for a page/topic?
- what benchmark context or expected citations exist for question Z?

The first version should answer those questions from **committed manifests and reports**, not from raw corpus traversal and not from any private data source.

## Scope boundaries

### In scope

- Define a repo-local CLI contract for querying committed public-safe manifests/reports.
- Standardize JSON response schemas, exit-code behavior, and repo-relative path rules.
- Support CLI operations that align directly with the issue body:
  - list domains;
  - search concepts/pages;
  - get page summary;
  - get code/result links;
  - get standards metadata;
  - explain clearance blockers;
  - retrieve benchmark context.
- Add public-safety filters and path allowlists for both inputs and outputs.
- Add validator/tests proving stable JSON and no unsafe/private path leakage.
- Document how agents should consume the CLI locally.
- Define MCP resources/tools only as a **thin wrapper over the stable CLI contract**.

### Out of scope

- No implementation of root/domain `llms.txt` manifests themselves — belongs to [#76](https://github.com/vamseeachanta/llm-wiki/issues/76).
- No generation of graph/link-graph manifests — belongs to [#77](https://github.com/vamseeachanta/llm-wiki/issues/77).
- No benchmark gold set, scorer, or evaluation harness design — belongs to [#78](https://github.com/vamseeachanta/llm-wiki/issues/78).
- No OSS watchlist crawling or weekly update scan — belongs to [#79](https://github.com/vamseeachanta/llm-wiki/issues/79).
- No broad GraphRAG/vector DB/embedding/reranking stack.
- No network daemon, hosted service, auth layer, or remote multi-user API in v1.
- No direct queries over raw `/mnt/ace` or any private/off-repo archive.
- No copied standards text, vendor brochure text, client/project results, credentials, or path-rich manifests.

## Proposed architecture

### Design principle

**CLI first, MCP second, shared contract throughout.**

The CLI should be the canonical implementation surface. MCP should not invent a second schema or second retrieval stack; it should expose the already-proven CLI contract as MCP tools/resources.

### Recommended data-source precedence

The query layer should resolve answers in this order:

1. **Approved query manifests / `llms.txt` entrypoints** from #76 when available.
2. **Approved graph/node-edge artifacts** from #77 when available.
3. **Committed report/link-map artifacts** already in the repo (`wikis/cross-links-tier1.md`, code/result link pages, completion/governance reports).
4. **Repo indexes** (`wikis/*/wiki/index.md`) for fallback discovery only where a dedicated manifest/graph artifact does not yet exist.

Important: v1 should prefer querying **derived artifacts** over scraping raw markdown bodies wherever possible. If fallback parsing is temporarily needed before #76/#77 land, it should be narrow, documented, and treated as an interim compatibility layer.

### Recommended CLI shape

The plan should standardize subcommands rather than one-off scripts. A likely contract:

- `domains list`
- `pages search --query <text> [--domain <domain>] [--kind <kind>]`
- `pages get --path <repo-relative-path>` or `pages get --id <page-id>`
- `links get --path <repo-relative-path> [--link-type code|result|data|governance|all]`
- `standards get --code-id <code_id>`
- `blockers explain --path <repo-relative-path>` or `--id <page-id>`
- `benchmark context --question-id <id>` or `--topic <text>`
- `manifests inspect --surface llms|graph|benchmark|watchlist`

All commands should support a default machine format:

- `--format json` as the default for automation;
- optional `--format text` only for human-friendly local use.

### JSON response contract

Every successful CLI response should use a stable top-level envelope such as:

```json
{
  "query_surface_version": "v1",
  "command": "pages get",
  "status": "ok",
  "data": {"...": "..."},
  "warnings": [],
  "sources": ["repo-relative/path.md"],
  "public_safety": {
    "is_safe": true,
    "filtered_fields": []
  }
}
```

Error responses should remain JSON and machine-readable, e.g. `status: error`, `error_code`, `message`, `hints`.

### Minimal command-level schemas

#### `domains list`
Returns:
- domain slug
- title/label
- primary entrypoint path
- available query surfaces (`index`, `llms`, `graph`, `links`, `benchmark`)
- size hints (`page_count`, `source_count`) when known

#### `pages search`
Returns a ranked list of repo-relative page matches with:
- page ID/path
- title
- domain
- kind (`concept`, `entity`, `standard`, `source`, `workflow`, `report`, `link_map`)
- short summary/snippet
- evidence source (`llms`, `graph`, `index`, `link_map`)

#### `pages get`
Returns a bounded page summary with:
- page ID/path
- title
- domain/kind
- frontmatter metadata safe for publication
- short abstract/summary
- related entrypoints/links
- linked code/results/standards if available via artifacts

#### `links get`
Returns public-safe implementation/result/data/governance links associated with a page/topic, including:
- target repo or repo-relative artifact
- relationship type (`implements`, `validates`, `public-result`, `governance`)
- source evidence path

#### `standards get`
Returns:
- `code_id`
- title
- publisher
- revision
- jurisdiction if available
- supersedes if publicly represented
- repo-relative page path
- related concepts/pages if graph/manifests support it

#### `blockers explain`
Returns only **explicit public blockers** found in committed docs/issues, such as:
- clearance issue references
- approval-gate references
- public-safety reasons for withheld data

It must never infer or expose hidden/private blockers.

#### `benchmark context`
Returns only benchmark metadata approved by #78, such as:
- question ID/topic
- expected citation paths
- allowed context sources
- unacceptable-answer notes

Before #78 lands, this command should either be absent or return a structured “not available yet” response.

## MCP design recommendation

MCP should be explicitly **phase 2** of #80, after the CLI contract is stable.

### Candidate MCP tools/resources

Recommended MCP resources/tools after CLI stabilization:

- resource: `llm-wiki://domains`
- tool: `search_pages`
- tool: `get_page_summary`
- tool: `get_related_links`
- tool: `get_standard_metadata`
- tool: `explain_clearance_blockers`
- tool: `get_benchmark_context`

### MCP rule

Each MCP tool/resource should internally map to one CLI command and reuse the same validation, path allowlists, and JSON schema. That prevents CLI/MCP drift.

## Implementation phases

### Phase 0 — contract freeze and dependency gating

- Finalize the command set, naming, response envelopes, and error contract.
- Decide which commands can ship immediately from existing committed artifacts versus which require #76/#77/#78/#79 outputs.
- Define explicit gating notes in docs/tests, for example:
  - graph-backed page/relationship queries depend on #77 artifact schema;
  - benchmark-context queries depend on #78 fixtures;
  - watchlist queries depend on #79 manifest structure.
- Lock public-safety rules before any implementation begins.

### Phase 1 — CLI skeleton and safety validator

- Add the base CLI entry point and argument parsing.
- Add a shared output envelope and shared error format.
- Add a dedicated validator for path safety, forbidden terms, and repo-relative output enforcement.
- Write failing tests first for stable JSON, exit codes, no path leakage, and unsupported-command behavior.

### Phase 2 — artifact adapters over existing repo content

Implement thin adapters that query already-committed safe surfaces first:

- domain/index discovery from `README.md` and `wikis/*/wiki/index.md`;
- code/result/data/governance links from `wikis/cross-links-tier1.md`, `wikis/marine-engineering/wiki/code-results-links.md`, and `wikis/engineering/wiki/public-data-software-links.md`;
- blocker/approval explanations from `docs/reports/2026-05-11-llm-wiki-completion-control-plane.md` and governance docs.

This phase gives immediate value before #76/#77/#78/#79 fully land.

### Phase 3 — manifest and graph integration

After #76 and #77 stabilize:

- add `llms.txt`-aware discovery/resolution;
- add graph-backed page relationship lookups;
- prefer machine manifests over markdown scraping;
- update tests to assert expected consumption of graph/manifest fixtures rather than index-only fallbacks.

### Phase 4 — benchmark and watchlist integration

After #78/#79 artifacts exist and are approved:

- add benchmark-context lookup;
- optionally add watchlist query support if useful to agents;
- keep these as separate adapters, not as reasons to redesign the core CLI.

### Phase 5 — MCP wrapper and agent docs

- Add a thin MCP server/wrapper that mirrors the CLI contract.
- Document usage patterns for `workspace-hub` and `digitalmodel` agents:
  - prefer CLI/MCP query first;
  - fall back to direct markdown inspection only when the query surface returns no result;
  - treat all outputs as public-safe metadata, not as permission to inspect private raw sources.

## Proposed file map

### New files expected

- `scripts/llm_wiki_query.py` — primary CLI entry point
- `scripts/validate_llm_wiki_query_surface.py` — validator for output contract and safety rules
- `tests/test_llm_wiki_query_surface.py` — CLI contract and safety tests
- `tests/fixtures/query_surface/` — minimal deterministic manifests/link pages/report fixtures
- `docs/query-surface.md` — human/agent usage guide for CLI contract

### Conditional new files

- `scripts/llm_wiki_mcp_server.py` or equivalent thin wrapper only after CLI contract is stable
- `tests/test_llm_wiki_mcp_server.py` only if/when MCP wrapper lands
- `artifacts/retrieval/query-surface/` only if the implementation chooses to emit cached indexes/summaries rather than purely on-demand responses

### Existing files likely to change during implementation

- `README.md` — add a short “agent query surface” section
- `scripts/llm_wiki_strengthening_scorecard.py` — only if shared parser/helper extraction is clearly justified
- `docs/plans/2026-05-15-issue-76-llms-entrypoints-domain-manifests.md` — only if later coordination notes are needed; not part of initial #80 scope
- `docs/plans/2026-05-15-issue-77-public-safe-knowledge-graph.md` — same caveat; not part of initial #80 scope

### Files that should remain untouched unless explicitly approved later

- domain wiki content under `wikis/*/wiki/**/*.md` except for small documentation links if absolutely necessary
- governance checklists for #43-#48
- weekly-freshness automation scope for #75
- benchmark design files for #78
- watchlist ingestion files for #79

## Tests and validation

### TDD checklist

Minimum tests before implementation:

- `test_domains_list_returns_stable_json_and_repo_relative_entrypoints`
- `test_pages_search_returns_expected_fields_without_private_paths`
- `test_pages_get_rejects_non_allowlisted_or_absolute_paths`
- `test_links_get_returns_only_public_safe_targets`
- `test_standards_get_returns_metadata_without_copied_standards_text`
- `test_blockers_explain_only_uses_explicit_public_issue_or_doc_evidence`
- `test_benchmark_context_returns_structured_not_available_before_issue_78_artifacts_exist`
- `test_query_surface_rejects_forbidden_secret_and_raw_archive_patterns`
- `test_query_surface_output_is_deterministic_for_fixture_inputs`
- `test_mcp_wrapper_matches_cli_schema` (only when MCP layer is added)

### Validation commands after implementation

Run from repo root:

- `uv run python scripts/validate_llm_wiki_query_surface.py`
- `uv run pytest tests/test_llm_wiki_query_surface.py -q`
- later, if MCP wrapper lands: `uv run pytest tests/test_llm_wiki_mcp_server.py -q`

### Validation rules

The validator should fail on:

- absolute filesystem paths in output
- `/mnt/ace` or `/mnt/ace-data` leakage
- secrets/credential-like patterns
- non-existent repo-relative paths emitted as canonical answers
- unstable/missing required JSON fields
- copied standards text or oversize raw excerpts in result payloads

## Public-safety and secrets constraints

This issue is safety-sensitive because it creates an agent-facing access layer.

### Hard constraints

- Query only **committed public-safe repo content** and approved generated artifacts.
- Emit **repo-relative paths only**.
- Never expose raw archive paths, private manifests, client/project filenames, or local machine-specific paths.
- Never emit copied standards clauses, tables, formulas, or vendor marketing prose.
- Never infer hidden/private blockers; only report public blockers documented in committed docs/issues.
- If a requested answer would require private/off-repo data, return a safe structured refusal or “not available in public-safe surface” response.

### Allowlist model

The plan should require a path/input allowlist such as:

- `README.md`
- `docs/governance/**/*.md`
- `docs/reports/**/*.md` only where explicitly approved as query sources
- `wikis/*/wiki/index.md`
- `wikis/cross-links-tier1.md`
- `wikis/*/wiki/*links*.md`
- #76/#77/#78/#79 generated manifests/artifacts once they exist and are approved

Anything outside the allowlist should be ignored by default.

## Risks and mitigations

1. **Dependency drift risk**  
   #80 can overreach if #76/#77 schemas are not stable yet.  
   **Mitigation:** split the work into a stable CLI contract plus adapters; gate graph/manifest-heavy commands on approved upstream schemas.

2. **Scope-creep risk**  
   CLI/MCP work can easily balloon into GraphRAG, search infra, hosting, or benchmark design.  
   **Mitigation:** keep v1 local, deterministic, artifact-backed, and JSON-only.

3. **Safety leakage risk**  
   A query surface can accidentally expose absolute paths, raw references, or copied restricted text.  
   **Mitigation:** validator + tests + explicit allowlist + filtered output envelope.

4. **Schema-fragmentation risk**  
   CLI and MCP can drift into different response shapes.  
   **Mitigation:** make CLI canonical and MCP a thin wrapper only.

5. **Fallback-parser risk**  
   If #80 relies too heavily on markdown scraping before #76/#77 land, later rework will be large.  
   **Mitigation:** isolate fallback adapters and mark them temporary compatibility layers.

6. **False-authority risk**  
   Query results may appear authoritative even when only partial artifacts exist.  
   **Mitigation:** include `warnings`, `sources`, and `surface_used` fields whenever results come from fallback/index-only data.

## Acceptance criteria mapping

| Issue #80 acceptance criterion | Plan response |
|---|---|
| Plan identifies CLI-first architecture, resource schema, public-safety constraints, and integration points. | This plan makes CLI canonical, defines command families/JSON envelopes, sets allowlist/safety rules, and stages integration with #76/#77/#78/#79 artifacts. |
| Implementation issue(s) are split if needed into CLI manifest query, MCP server wrapper, and agent integration docs. | The phased plan already separates CLI contract/adapters, later MCP wrapper, and separate documentation; follow-up split is recommended only if implementation size warrants it. |
| Tests cover no unsafe path leakage and stable JSON responses. | Dedicated validator plus TDD checklist explicitly requires path/secret rejection and deterministic JSON contracts. |
| README or docs page explains intended agent use. | `docs/query-surface.md` plus `README.md` update are called out in the proposed file map and implementation phases. |

## Adversarial review synthesis and accepted hardening

Three independent plan reviews completed on 2026-05-15. Consensus verdict: **MAJOR until v1 is narrowed and dependency gating is explicit; revised plan is approval-candidate with Medium residual risk**. The following changes are binding.

### Accepted changes from review
- **CLI-only v1:** MCP is phase 2 / follow-on after the CLI contract is stable. MCP work is not part of v1 done criteria.
- **Narrow v1 command surface:** v1 should ship only deterministic artifact/entrypoint inspection commands, such as:
  - `domains list`
  - `pages get`
  - `links get`
  - `manifests inspect`
  Optional `pages search`, `standards get`, `blockers explain`, and `benchmark context` are gated until the required #76/#77/#78 artifacts exist and have tests.
- **Query-source registry required:** add a checked-in registry such as `data/query_sources.json` listing approved artifacts, exposed fields, schema versions, and public-safety notes.
- **Fallback parser bounded:** any pre-#76/#77 fallback parser must name exact input files, exact extractable fields, and an explicit deprecation path once structured artifacts land.
- **Command availability matrix:** docs/tests must declare which commands are available now, gated on #76, gated on #77, gated on #78, or gated on #79. Gated commands return structured `not_available` responses rather than ad hoc behavior.
- **Response envelope strengthened:** JSON responses include `schema_version`, `surface_used`, `artifact_versions`, `match_type`, `result_confidence` or deterministic score, `ambiguity`, `warnings`, and `result_count`.
- **No synthesized summaries in v1:** `pages get` may extract authored frontmatter/title/lead/abstract text only; no LLM-generated summary or free-form synthesis.
- **Benchmark tie-in:** selected CLI command outputs should become fixtures for #78 once benchmark artifacts exist.

### Residual risk
Medium. The query surface is user-facing and downstream of #76/#77/#78. Risk is controlled by narrowing v1 to deterministic structured lookup and deferring MCP/open search until contracts stabilize.

## Dependencies

### Hard dependencies

- **Schema decisions from #76 and #77 for full-value querying.**  
  #80 can define and partially implement a CLI contract before they land, but manifest-aware and graph-aware query fidelity depends on their approved output structures.

### Soft / sequencing dependencies

- [#13](https://github.com/vamseeachanta/llm-wiki/issues/13) — roadmap anchor and sequencing umbrella.
- [#76](https://github.com/vamseeachanta/llm-wiki/issues/76) — curated `llms.txt` entrypoints improve discovery/routing queries.
- [#77](https://github.com/vamseeachanta/llm-wiki/issues/77) — structured graph manifests unlock page/relationship lookup without prose scraping.
- [#78](https://github.com/vamseeachanta/llm-wiki/issues/78) — benchmark-context query lane depends on benchmark fixtures.
- [#79](https://github.com/vamseeachanta/llm-wiki/issues/79) — optional future watchlist queries depend on watchlist manifest format.
- Existing validator/test patterns in this repo — the implementation should reuse them instead of inventing a heavier framework.

## Follow-up issues likely needed after approval

- **No immediate new follow-up issue is required during planning.**
- If implementation becomes too large, the only clean split is:
  1. **CLI contract + validators/tests** as the main #80 implementation;
  2. **MCP wrapper parity** as a follow-on child issue;
  3. **agent-consumer integration notes/examples** only if README + `docs/query-surface.md` prove insufficient.

Any such split should happen only during approved implementation planning, not during this planning-only pass.

## Recommended execution order once approved

1. Approve #76 and #77 artifact contracts or at least freeze their expected schemas.
2. Implement #80 CLI contract and tests against fixtures plus existing committed link/report surfaces.
3. Add validator and enforce no-path-leak / stable-JSON guarantees.
4. Document agent usage in `docs/query-surface.md` and `README.md`.
5. Only then add the MCP wrapper, reusing the CLI contract unchanged.
6. After #78/#79 mature, add benchmark/watchlist adapters without redesigning the core surface.

## Review-ready conclusion

Issue #80 is best framed as an **agent-access contract** problem, not a search-infrastructure problem. The canonical first step is a local, deterministic, public-safe CLI that queries approved `llm-wiki` artifacts and returns stable JSON. MCP should follow only as a thin wrapper once that contract is proven. Keeping #80 tightly scoped this way avoids overlap with #75-#79 while still making those issues materially more useful to downstream agents.
