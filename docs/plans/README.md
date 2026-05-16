# LLM-Wiki Issue Plans

This directory contains public-safe issue execution plans for the `llm-wiki` repository.

Workflow gate: an issue plan here is **not** implementation approval by itself. Issues remain blocked for implementation until GitHub has explicit user approval and the issue is moved from `status:plan-review` to `status:plan-approved`. Issues #43-#48 were verified as `status:plan-approved` on 2026-05-11.

Public-safety default: plans may reference source-family names and aggregate metadata, but must not copy raw `/mnt/ace` files, vendor standards text, client/project material, personal/admin data, credentials, private workspace memory, or path-rich private manifests.

## Active plans

| Issue | Plan | Status | Deliverable |
| --- | --- | --- | --- |
| [`#28`](https://github.com/vamseeachanta/llm-wiki/issues/28) | [`2026-05-11-issue-28-marine-index-chunking.md`](2026-05-11-issue-28-marine-index-chunking.md) | `plan-approved` | Marine-engineering canonical index chunking/pagination plan |
| [`#29`](https://github.com/vamseeachanta/llm-wiki/issues/29) | [`2026-05-11-issue-29-source-title-aliasing.md`](2026-05-11-issue-29-source-title-aliasing.md) | `plan-approved` | Canonical source-title aliasing plan for marine source pages |
| [`#43`](https://github.com/vamseeachanta/llm-wiki/issues/43) | [`2026-05-10-issue-43-sesa-extraction-clearance-checklist.md`](2026-05-10-issue-43-sesa-extraction-clearance-checklist.md) | `plan-approved` | SESA extraction clearance checklist governance artifact |
| [`#44`](https://github.com/vamseeachanta/llm-wiki/issues/44) | [`2026-05-10-issue-44-bsee-source-family-clearance-checklist.md`](2026-05-10-issue-44-bsee-source-family-clearance-checklist.md) | `plan-approved` | BSEE source-family clearance checklist governance artifact |
| [`#45`](https://github.com/vamseeachanta/llm-wiki/issues/45) | [`2026-05-10-issue-45-hse-dataset-clearance-checklist.md`](2026-05-10-issue-45-hse-dataset-clearance-checklist.md) | `plan-approved` | HSE dataset source-family clearance checklist governance artifact |
| [`#46`](https://github.com/vamseeachanta/llm-wiki/issues/46) | [`2026-05-10-issue-46-frontier-deepwater-clearance-checklist.md`](2026-05-10-issue-46-frontier-deepwater-clearance-checklist.md) | `plan-approved` | Frontier Deepwater source-family clearance checklist governance artifact |
| [`#47`](https://github.com/vamseeachanta/llm-wiki/issues/47) | [`2026-05-10-issue-47-batch-pack-1-approved-inputs.md`](2026-05-10-issue-47-batch-pack-1-approved-inputs.md) | `plan-approved` | Batch Pack 1 approved-input readiness governance artifact |
| [`#48`](https://github.com/vamseeachanta/llm-wiki/issues/48) | [`2026-05-10-issue-48-batch-pack-4-approved-inputs.md`](2026-05-10-issue-48-batch-pack-4-approved-inputs.md) | `plan-approved` | Batch Pack 4 approved-input readiness governance artifact |
| [`#40`](https://github.com/vamseeachanta/llm-wiki/issues/40) | [`2026-05-15-issue-40-reservoir-engineering-literature.md`](2026-05-15-issue-40-reservoir-engineering-literature.md) | `plan-review` | Reservoir-engineering wiki founding + corpus build. Claude review MINOR (scope-clarification on formation-eval vs RE-domain). Live issue label is `plan-approved` (predates plan; not downgraded per skill rule). |
| [`#73`](https://github.com/vamseeachanta/llm-wiki/issues/73) | [`2026-05-15-issue-73-pe-phase-2-completions.md`](2026-05-15-issue-73-pe-phase-2-completions.md) | `closed` | PE Phase 2 corpus build-out (completions). Closed after closeout evidence confirmed #82/#83 landed and Phase 3 was unblocked. |
| [`#74`](https://github.com/vamseeachanta/llm-wiki/issues/74) | [`2026-05-15-issue-74-pe-phase-3-stimulation.md`](2026-05-15-issue-74-pe-phase-3-stimulation.md) | `plan-review` | PE Phase 3 corpus build-out (stimulation). Claude review MINOR (API RP 39 too narrow; add SPE Mono 17). |
| [`#75`](https://github.com/vamseeachanta/llm-wiki/issues/75) | [`2026-05-15-issue-75-weekly-freshness-control-loop.md`](2026-05-15-issue-75-weekly-freshness-control-loop.md) | `plan-approved` | Weekly freshness control loop with JSON baseline/report artifacts and recommendation routing. |
| [`#76`](https://github.com/vamseeachanta/llm-wiki/issues/76) | [`2026-05-15-issue-76-llms-entrypoints-domain-manifests.md`](2026-05-15-issue-76-llms-entrypoints-domain-manifests.md) | `plan-approved` | Root/domain `llms.txt` manifests with validators and routing smoke tests. |
| [`#79`](https://github.com/vamseeachanta/llm-wiki/issues/79) | [`2026-05-15-issue-79-weekly-oss-engineering-tool-watchlist.md`](2026-05-15-issue-79-weekly-oss-engineering-tool-watchlist.md) | `plan-approved` | Fixture-first weekly OSS tool/concept watchlist with scan/render split. |
| [`#88`](https://github.com/vamseeachanta/llm-wiki/issues/88) | [`2026-05-16-issue-88-route-state-validation.md`](2026-05-16-issue-88-route-state-validation.md) | `plan-review` | Route-state validation so weekly cadence reports cannot target closed child issues by default. |

## Review evidence

- [`docs/reports/codex/2026-05-11-issue-28-index-chunking-intel.md`](../reports/codex/2026-05-11-issue-28-index-chunking-intel.md) — Codex resource-intelligence scout for issue #28; identified actual paths, parser/counting risks, and TDD surface.
- [`docs/reports/codex/2026-05-11-issue-29-source-title-aliasing-intel.md`](../reports/codex/2026-05-11-issue-29-source-title-aliasing-intel.md) — Codex resource-intelligence scout for issue #29; identified deterministic metadata limits, ambiguity policy, and safety risks.
- [`scripts/review/results/2026-05-10-plan-issues-43-48-codex-round1.md`](../../scripts/review/results/2026-05-10-plan-issues-43-48-codex-round1.md) — MAJOR; initial blocker findings.
- [`scripts/review/results/2026-05-10-plan-issues-43-48-codex-round2.md`](../../scripts/review/results/2026-05-10-plan-issues-43-48-codex-round2.md) — MAJOR; validation-command refinement needed.
- [`scripts/review/results/2026-05-10-plan-issues-43-48-codex-round3.md`](../../scripts/review/results/2026-05-10-plan-issues-43-48-codex-round3.md) — MAJOR; exact touched-path placeholders remained.
- [`scripts/review/results/2026-05-10-plan-issues-43-48-codex-round4.md`](../../scripts/review/results/2026-05-10-plan-issues-43-48-codex-round4.md) — APPROVE; no remaining blocking findings.
