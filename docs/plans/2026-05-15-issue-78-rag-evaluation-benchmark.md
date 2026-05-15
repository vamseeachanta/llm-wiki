---
title: "Issue #78 plan — llm-wiki RAG evaluation benchmark for code-development questions"
issue: 78
status: plan-review
created: 2026-05-15
last_updated: 2026-05-15
public_safety: benchmark fixtures, citations, and scorecards must remain public-safe; no raw/private paths, vendor/client material, copied standards text, or secret-bearing references
---

# Issue #78 Plan — llm-wiki RAG Evaluation Benchmark for Code-Development Questions

## Approval-gate note

- GitHub issue: [vamseeachanta/llm-wiki#78](https://github.com/vamseeachanta/llm-wiki/issues/78)
- Local plan status: `plan-review`
- Implementation status: **not started**
- This artifact is planning-only. It does **not** authorize code changes beyond this plan file, benchmark execution against private corpora, GitHub label/comment edits, or issue closure.
- Per repo workflow, implementation should begin only after explicit user approval and the main agent advances the issue through the normal approval gate.

## Summary

Issue #78 should add a **deterministic, repo-local retrieval/evaluation benchmark** that measures whether `llm-wiki` actually helps agents answer **code-development questions** with correct citations and safe boundaries.

The first version should stay narrow and regression-friendly:

1. define a gold question set grounded only in committed public repo content;
2. require exact or rubric-checked answer expectations plus required citation paths;
3. score retrieval relevance and citation correctness before attempting ambitious LLM-judge metrics;
4. emit both Markdown and JSON scorecards from a local `uv run` command;
5. enforce public-safety checks so benchmark fixtures never encode private paths, copied standards text, or unsafe references.

The benchmark should validate the repo’s practical utility for questions like:

- where is a workflow, module, or result linked from the wiki?
- which standard page applies to a concept or engineering workflow?
- which public result/demo validates a topic?
- what is explicitly blocked by approval or clearance?

## Current evidence / intelligence

### Live issues inspected

1. [#78](https://github.com/vamseeachanta/llm-wiki/issues/78) — target issue; defines the benchmark goal, minimum dataset size, local scorecard requirement, and safety acceptance criteria.
2. [#13](https://github.com/vamseeachanta/llm-wiki/issues/13) — roadmap anchor; #78 should remain a child lane and not create a replacement umbrella.
3. [#75](https://github.com/vamseeachanta/llm-wiki/issues/75) — weekly freshness loop; should consume benchmark outputs later, but benchmark generation itself belongs here.
4. [#76](https://github.com/vamseeachanta/llm-wiki/issues/76) — `llms.txt` entrypoints; useful future retrieval input, but not benchmark scope.
5. [#77](https://github.com/vamseeachanta/llm-wiki/issues/77) — public-safe graph/link manifests; useful future retrieval substrate, but benchmark definition must stay separable.
6. [#79](https://github.com/vamseeachanta/llm-wiki/issues/79) — OSS tool watchlist; unrelated to the first benchmark dataset.
7. [#80](https://github.com/vamseeachanta/llm-wiki/issues/80) — CLI/MCP query surface; should eventually consume benchmark-backed retrieval behavior, not be implemented here.
8. [#40](https://github.com/vamseeachanta/llm-wiki/issues/40) — reservoir-engineering plan; relevant because #78’s issue body mentions production/reservoir coverage, but the reservoir domain is not yet founded in repo content.

### Exact repo files inspected

1. `README.md` — confirms `llm-wiki` is the public content storehouse, lists repo layout, and defines the public/private boundary.
2. `docs/plans/README.md` — confirms the plan-review workflow and public-safety default for plan artifacts.
3. `docs/reports/2026-05-11-llm-wiki-completion-control-plane.md` — defines practical completeness, code/result linkage expectations, and blocked/approval-gated lanes.
4. `docs/reports/llm-wiki-strengthening-scorecard.md` — current repo metrics and evidence that deterministic, metadata-only reporting already exists.
5. `scripts/llm_wiki_strengthening_scorecard.py` — existing parser/reporting precedent for markdown-only analysis, link extraction, frontmatter parsing, and reproducible score output.
6. `scripts/validate_completion_artifacts.py` — validator precedent for required phrases/links and forbidden private-path scanning.
7. `scripts/validate_governance_artifacts.py` — validator precedent for artifact-specific content contracts plus secret/private-path checks.
8. `tests/test_completion_artifacts.py` — regression-test pattern for doc/control-plane validators.
9. `tests/test_governance_artifacts.py` — regression-test pattern for validator failure modes.
10. `tests/test_scan_source_families_safe.py` — safety-test pattern for “no sensitive/path leakage” guarantees.
11. `wikis/marine-engineering/wiki/code-results-links.md` — concrete public code/result link surface for code-development questions.
12. `wikis/engineering/wiki/public-data-software-links.md` — concrete public data/software link surface for engineering/repo-routing questions.
13. `wikis/drilling-engineering/wiki/index.md` — strong source for “which concept/standard/entity page implements X?” style benchmark questions.
14. `wikis/drilling-engineering/wiki/standards/norsok-d-010.md` — standards-page example with code ID, publisher, revision, concept links, and companion-standard cross-references.
15. `wikis/production-engineering/wiki/index.md` — shows production-engineering is founded and usable for production-side benchmark coverage.
16. `docs/plans/2026-05-15-issue-40-reservoir-engineering-literature.md` — confirms reservoir-engineering is still planning-only and should not be assumed as current benchmark corpus.
17. `docs/governance/service-provider-data-routing.md` — explicit routing rules that must constrain benchmark fixtures and unacceptable answers.

### Concrete intelligence derived from inspection

- There is already a strong **repo-local analytics pattern** (`scripts/llm_wiki_strengthening_scorecard.py`) but **no existing benchmark/eval harness** in current `scripts/*.py` and `tests/*.py` surfaces.
- The repo already contains **human-authored retrieval targets** for code/results and data/software links, which is ideal for a first benchmark focused on code-development questions.
- `docs/reports/2026-05-11-llm-wiki-completion-control-plane.md` explicitly says a wiki page is only practical-complete when it can answer what it is, where it came from, where it is implemented/validated, and what remains blocked by clearance or approval. That sentence is almost a direct benchmark design brief.
- Production-side benchmark coverage is possible now because `wikis/production-engineering/wiki/index.md` exists, but **reservoir-engineering is not yet founded**; issue #78 should not fabricate reservoir questions until a real reservoir corpus exists.
- Existing validators consistently treat **private path leakage and unsafe content** as hard failures, so benchmark fixtures and scorecards should inherit that posture.
- Adjacent issues #75-#77/#80 already partition freshness loops, entry manifests, graph substrates, and query interfaces. #78 should stay focused on **dataset + scoring + validation**, not absorb those lanes.

## Problem statement specific to #78

`llm-wiki` has many pages, cross-links, and link maps, but there is no deterministic way to answer:

- whether retrieval actually surfaces the right pages for code-development tasks,
- whether answers cite the right repo paths,
- whether retrieved context includes the evidence needed to avoid hallucinated engineering claims,
- whether agents can distinguish public implementation/result anchors from approval-gated or clearance-blocked areas.

Without a benchmark, repo growth can improve volume while degrading real utility.

## Scope boundaries

### In scope

- A gold benchmark dataset of at least **20 repo-grounded questions** centered on code-development and engineering-implementation use cases.
- Questions spanning the issue’s required content areas, interpreted against the current repo state as:
  - **marine/offshore**
  - **standards**
  - **production-side engineering**
  - **code/results links**
  - **governance / blocked-by-clearance boundaries**
- Exact expected citation paths for every question.
- Answer rubrics and unacceptable-answer criteria for every question.
- A local baseline retrieval/eval command runnable with `uv run`.
- Markdown and JSON scorecards.
- Tests that benchmark fixtures load, score deterministically, and reject unsafe/private references.
- Public-safe documentation describing how future issues (#75, #77, #80) should consume benchmark outputs.

### Explicitly out of scope

- No `llms.txt` manifest implementation from [#76](https://github.com/vamseeachanta/llm-wiki/issues/76).
- No graph/link-manifest generation from [#77](https://github.com/vamseeachanta/llm-wiki/issues/77).
- No weekly scheduling/report-posting automation from [#75](https://github.com/vamseeachanta/llm-wiki/issues/75).
- No OSS watchlist ingestion from [#79](https://github.com/vamseeachanta/llm-wiki/issues/79).
- No CLI/MCP serving layer from [#80](https://github.com/vamseeachanta/llm-wiki/issues/80).
- No broad LLM-judge infrastructure, hosted eval service, embeddings platform, or external vector database requirement for v1.
- No benchmark questions that depend on non-committed corpora, `/mnt/ace` content, vendor brochures, copied standards clauses, client/project archives, or unpublished repo knowledge.
- No invented reservoir-engineering questions until a real committed reservoir corpus exists; if reservoir coverage is still desired later, it should follow [#40](https://github.com/vamseeachanta/llm-wiki/issues/40) or its eventual implementation output.

## Recommended benchmark shape

### Primary benchmark objective

Measure whether a simple retrieval stack over committed repo content can support **engineering code-development questions** with:

1. correct source-page retrieval,
2. correct citation paths,
3. safe/public answer boundaries,
4. acceptable answer quality on deterministic rubric checks.

### Recommended v1 evaluation layers

#### Layer 1 — retrieval correctness (required)

For each question, score whether top-k retrieved contexts include the expected source paths.

Suggested metrics:

- `hit_at_1`
- `hit_at_3`
- `hit_at_5`
- `context_precision_at_k`
- `context_recall_at_k`

#### Layer 2 — citation correctness (required)

Given an answer generated from retrieved contexts or a baseline extraction pipeline, score:

- whether required citation paths appear,
- whether forbidden/irrelevant citations appear,
- whether citations refer only to committed public-safe repo paths.

#### Layer 3 — answer rubric correctness (required, lightweight)

Use deterministic rubric checks before adding LLM-judge dependence.

Per question, store:

- required facts/phrases or normalized fact tokens,
- required citation paths,
- unacceptable-answer conditions,
- optional alternates for wording variations.

#### Layer 4 — faithfulness / judge-style scoring (optional follow-on)

If later desired, add an optional LLM-judge mode or RAGAS-like scoring. This should be explicitly **optional** in v1 so the benchmark remains runnable offline or with minimal dependencies.

## Benchmark dataset design

### Question families to include

The issue body already suggests the right task families. The plan recommends structuring the 20+ questions across these buckets:

1. **Implementation locator**
   - “Which repo/doc/result page should I consult to implement or validate X?”
2. **Standards applicability**
   - “Which standards page applies to X, and what companion pages cross-reference it?”
3. **Public-result validation**
   - “Which public result/demo validates this workflow or topic?”
4. **Governance / clearance boundary**
   - “What is blocked by approval or clearance, and what public-safe substitute should be cited instead?”
5. **Cross-domain routing**
   - “Should this question route to drilling, production, marine, engineering, or a standards page?”

### Coverage recommendation for the first 20-question set

A concrete v1 split:

- 5 marine/offshore questions
- 4 standards questions
- 4 drilling/production code-development questions
- 4 code/results or data/software link questions
- 3 governance / blocked-by-clearance questions

This satisfies the issue’s intent without pretending reservoir coverage exists today.

### Fixture contract per question

Each benchmark fixture should include fields like:

- `question_id`
- `question`
- `intent_category`
- `domain`
- `expected_paths`
- `secondary_paths`
- `required_citations`
- `required_facts`
- `forbidden_patterns`
- `unacceptable_answer_criteria`
- `notes`

### Important scope clarification

Issue #78 mentions “production/reservoir,” but current repo inspection shows:

- `production-engineering` exists and is usable now;
- `reservoir-engineering` does not yet exist as a founded committed wiki domain.

So the canonical plan should interpret the acceptance target as:

- include **production-side coverage now**, and
- record **reservoir-specific extension** as a future follow-up after actual reservoir content lands.

## Implementation phases

### Phase 1 — lock the benchmark contract before coding

- Finalize benchmark fixture schema.
- Decide exact output locations for fixtures and scorecards.
- Define required metrics and deterministic pass/fail behavior.
- Write failing tests for fixture loading, schema validation, and safety scanning.
- Explicitly document that #78 consumes committed markdown/link artifacts only in v1.

### Phase 2 — assemble the gold question set

- Curate at least 20 questions from already committed pages.
- For each question, capture exact expected paths and unacceptable-answer rules.
- Keep questions operational and code-development-oriented rather than academic trivia.
- Prefer pages that already encode implementation/result/governance links.
- Exclude any question that requires private knowledge or copied standards details.

### Phase 3 — implement baseline retrieval and scoring

- Build a simple local retriever over markdown/link-manifest text.
- Score retrieval against expected paths.
- Add citation and answer-rubric evaluation.
- Emit machine-readable JSON plus a review-friendly Markdown summary.
- Keep the retrieval substrate simple enough that later #77 graph inputs can be plugged in without changing the benchmark contract.

### Phase 4 — validator and regression hardening

- Add fixture validator for schema completeness and safety constraints.
- Add regression tests for deterministic scoring.
- Add failure-mode tests for forbidden private paths, missing citations, and malformed fixtures.
- Ensure scorecards are reproducible from repo root via `uv run`.

### Phase 5 — downstream integration hooks (documentation only)

- Document how #75 can later record weekly score deltas.
- Document how #77 outputs could later become an alternate retrieval backend.
- Document how #80 should treat benchmark metrics as a readiness gate for CLI/MCP query behavior.

## Proposed file map

### New files likely to add during implementation

- `scripts/llm_wiki_rag_benchmark.py`
  - primary local benchmark runner
- `scripts/validate_rag_benchmark.py`
  - fixture/artifact validator with public-safety scan
- `tests/test_llm_wiki_rag_benchmark.py`
  - retrieval/scoring regression tests
- `tests/test_rag_benchmark_artifacts.py`
  - validator regression tests
- `tests/fixtures/rag-benchmark/questions.yaml`
  - gold question set
- `tests/fixtures/rag-benchmark/README.md`
  - fixture contract and authoring rules
- `artifacts/retrieval/rag-benchmark/latest-scorecard.json`
  - machine-readable benchmark output
- `docs/reports/<run-date>-llm-wiki-rag-benchmark.md`
  - human-readable benchmark scorecard

### Existing files likely to remain unchanged unless truly necessary

- `README.md`
- `docs/reports/2026-05-11-llm-wiki-completion-control-plane.md`
- `wikis/*/wiki/**/*.md`
- `docs/plans/2026-05-15-issue-75-weekly-freshness-control-loop.md`
- `docs/plans/2026-05-15-issue-76-llms-entrypoints-domain-manifests.md`
- `docs/plans/2026-05-15-issue-77-public-safe-knowledge-graph.md`
- issue plans or implementation surfaces for #79 and #80

### Optional refactor path only if duplication becomes material

- `scripts/_llm_wiki_retrieval_common.py`
  - only if the benchmark needs to share parsing logic with scorecard/graph work; avoid this unless duplication is real.

## Tests and validation

### TDD checklist

Minimum tests to write before implementation:

- `test_benchmark_fixture_schema_loads_and_is_complete`
- `test_benchmark_requires_at_least_20_questions`
- `test_benchmark_questions_have_expected_paths_and_unacceptable_answer_rules`
- `test_benchmark_validator_rejects_private_paths_and_secret_like_tokens`
- `test_retrieval_scoring_counts_expected_path_hits_deterministically`
- `test_citation_scoring_requires_repo_relative_public_safe_paths`
- `test_answer_rubric_flags_missing_required_facts`
- `test_scorecard_output_contains_markdown_and_json_sections`

### Validation commands expected after implementation

Run from repo root:

- `uv run pytest tests/test_llm_wiki_rag_benchmark.py tests/test_rag_benchmark_artifacts.py -q`
- `uv run python scripts/llm_wiki_rag_benchmark.py --output-json artifacts/retrieval/rag-benchmark/latest-scorecard.json --output-md docs/reports/YYYY-MM-DD-llm-wiki-rag-benchmark.md`
- `uv run python scripts/validate_rag_benchmark.py tests/fixtures/rag-benchmark/questions.yaml docs/reports/YYYY-MM-DD-llm-wiki-rag-benchmark.md artifacts/retrieval/rag-benchmark/latest-scorecard.json`

### Validation/report requirements

The Markdown scorecard should include:

- run metadata and benchmark version,
- question-count summary,
- retrieval metrics,
- citation correctness metrics,
- answer-rubric pass/fail summary,
- failed questions table with exact expected vs retrieved path deltas,
- public-safety statement,
- note on whether graph/manifests were or were not used as retrieval inputs.

## Public-safety / secrets constraints

- Benchmark fixtures must cite only committed public-safe repo paths.
- Do not include `/mnt/ace` subpaths, private manifests, vendor brochures, copied standards clauses/tables, client/project names, or credential-like strings.
- Governance questions may reference public blocker issues or governance docs, but must not expose hidden blockers or private evidence.
- Standards questions must test **metadata/routing/citation behavior**, not copied standards text.
- Scorecards must not embed raw retrieved passages if doing so would risk reproducing protected or unsafe content; path-level and short authored-summary output is safer for v1.
- If an optional judge mode is added later, it must operate on the same public-safe fixture set and never call external services by default without explicit approval.

## Risks

1. **Scope creep into adjacent retrieval work**
   - Risk: #78 expands into llms manifests, graph generation, or query-API design.
   - Mitigation: keep #78 limited to dataset, scoring, validation, and scorecards.

2. **Overweight dependence on future graph work**
   - Risk: #78 waits on #77 and stalls.
   - Mitigation: design the benchmark so v1 works over committed markdown/link pages directly; treat #77 as an optional alternate backend later.

3. **False confidence from weak answer grading**
   - Risk: purely lexical grading says answers are correct when they are not.
   - Mitigation: combine expected-path retrieval checks, required citations, and unacceptable-answer criteria; add optional judge mode only after deterministic checks are strong.

4. **Unsafe benchmark fixtures**
   - Risk: a question or expected answer accidentally encodes private-path or vendor-derived content.
   - Mitigation: dedicated validator and explicit forbidden-pattern tests.

5. **Acceptance-criteria mismatch around reservoir coverage**
   - Risk: the issue body’s “production/reservoir” phrase is interpreted literally despite reservoir content not existing yet.
   - Mitigation: document that v1 covers production now and records reservoir extension as a follow-up dependency on real reservoir corpus availability.

6. **Benchmark drift as repo grows**
   - Risk: paths or answer targets change and silently rot the dataset.
   - Mitigation: require exact-path validation plus future weekly consumption through #75.

## Acceptance criteria mapping

| Issue #78 acceptance criterion | Plan response |
|---|---|
| Benchmark has at least 20 repo-grounded questions spanning marine/offshore, standards, production/reservoir, code-results links, and governance boundaries | Phase 2 requires a 20+ question gold set spanning marine, standards, production-side, code/results links, and governance; reservoir is explicitly deferred until actual corpus exists |
| Each question has expected source paths and unacceptable-answer criteria | Fixture contract requires `expected_paths`, `required_citations`, and `unacceptable_answer_criteria` for every question |
| A local command produces a markdown/JSON scorecard | Phase 3 and validation commands specify a local `uv run` benchmark runner that emits both Markdown and JSON outputs |
| CI/local tests verify benchmark fixtures load and unsafe/private references are absent | Phase 4 adds validator/tests for fixture loading, deterministic scoring, and forbidden private-path/secret-pattern rejection |

## Adversarial review synthesis and accepted hardening

Three independent plan reviews completed on 2026-05-15. Consensus verdict: **MAJOR until methodology is frozen; revised plan is approval-candidate with Medium residual risk**. The following changes are binding and narrow the implementation.

### Accepted changes from review
- **Benchmark-first, backend-second:** #78 owns dataset/schema/validator/scorer. Baseline retrieval is a minimal adapter for proving the benchmark, not a broad retrieval product.
- **Backend adapter interface:** define a stable interface with input `question` and output `ranked_context[]`, optional `answer`, and `citations[]`. Future #77/#80 integrations must plug into this contract without changing benchmark semantics.
- **Retrieval unit frozen for v1:** use deterministic file-level or section-level chunk IDs; implementation must choose and document one before coding. Each run records the corpus surface and corpus manifest hash/date.
- **JSON fixtures preferred:** replace `questions.yaml` with `questions.json` for v1 unless a dependency manifest is added. The repo remains stdlib/dependency-light by default.
- **Fixture versioning:** every fixture set includes `benchmark_version`, `fixture_version`, `corpus_surface`, and a changelog policy.
- **Safety-sensitive question classes required:** include positive retrieval, no-answer/safe-refusal, ambiguity/disambiguation, and blocked-by-clearance/public-safe substitute cases.
- **Citation rigor:** expected citations should be chunk/anchor/path-level where feasible, not only broad repo paths.
- **Metrics thresholds:** define pass/fail thresholds and regression behavior for hit@k/path accuracy/citation accuracy/refusal accuracy before approval-to-execute handoff.
- **Offline default:** no external model, judge, network, or API dependency is required for default tests.

### Revised artifact contract
Expected v1 fixture path is `tests/fixtures/rag-benchmark/questions.json`. Expected run output includes `artifacts/retrieval/rag-benchmark/latest-scorecard.json` with benchmark/corpus versions and deterministic metrics.

### Residual risk
Medium. The main remaining risk is benchmark brittleness. It is controlled by explicit retrieval unit, versioned corpus surface, refusal cases, and deterministic baseline adapter.

## Dependencies and sequencing

### Hard dependencies

- None of #75, #76, #77, #79, or #80 should block defining the benchmark contract itself.
- The benchmark may proceed using current committed markdown/link pages as its first retrieval corpus.

### Soft dependencies / strong consumers

- [#75](https://github.com/vamseeachanta/llm-wiki/issues/75) should later consume score deltas and include them in weekly freshness reporting.
- [#76](https://github.com/vamseeachanta/llm-wiki/issues/76) may later improve retrieval entry surfaces, but should not change the benchmark contract.
- [#77](https://github.com/vamseeachanta/llm-wiki/issues/77) may later provide a stronger retrieval backend; benchmark fixtures and metrics should remain stable across backend swaps.
- [#80](https://github.com/vamseeachanta/llm-wiki/issues/80) should treat #78 metrics as one readiness signal for CLI/MCP query behavior.

### Content dependency note

- Reservoir-specific benchmark expansion should wait for actual reservoir content to land through [#40](https://github.com/vamseeachanta/llm-wiki/issues/40) or a later approved reservoir-domain implementation issue.

## Follow-up issues likely needed after #78

1. **Reservoir benchmark extension** — only after a committed reservoir-engineering corpus exists.
2. **Optional judge/RAGAS mode** — only if deterministic rubric scoring proves insufficient.
3. **Backend comparison mode** — compare raw-markdown retrieval vs #77 graph-backed retrieval once #77 is implemented.
4. **Weekly benchmark delta integration** — likely part of [#75](https://github.com/vamseeachanta/llm-wiki/issues/75), not a reason to expand #78.
5. **CLI readiness gate consumption** — likely part of [#80](https://github.com/vamseeachanta/llm-wiki/issues/80).

No follow-up issue should be opened during planning itself unless the main agent explicitly chooses to do so later.

## Recommended implementation order after approval

1. Freeze fixture schema and scoring contract.
2. Write failing tests and validator scaffolding.
3. Curate the first 20+ questions from committed pages only.
4. Implement baseline retrieval/scoring and produce initial scorecards.
5. Run tests/validator.
6. Only then let #75 or #80 consume the outputs, and only later compare against #77-backed retrieval.
