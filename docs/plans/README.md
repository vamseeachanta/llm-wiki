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

## Review evidence

- [`docs/reports/codex/2026-05-11-issue-28-index-chunking-intel.md`](../reports/codex/2026-05-11-issue-28-index-chunking-intel.md) — Codex resource-intelligence scout for issue #28; identified actual paths, parser/counting risks, and TDD surface.
- [`docs/reports/codex/2026-05-11-issue-29-source-title-aliasing-intel.md`](../reports/codex/2026-05-11-issue-29-source-title-aliasing-intel.md) — Codex resource-intelligence scout for issue #29; identified deterministic metadata limits, ambiguity policy, and safety risks.
- [`scripts/review/results/2026-05-10-plan-issues-43-48-codex-round1.md`](../../scripts/review/results/2026-05-10-plan-issues-43-48-codex-round1.md) — MAJOR; initial blocker findings.
- [`scripts/review/results/2026-05-10-plan-issues-43-48-codex-round2.md`](../../scripts/review/results/2026-05-10-plan-issues-43-48-codex-round2.md) — MAJOR; validation-command refinement needed.
- [`scripts/review/results/2026-05-10-plan-issues-43-48-codex-round3.md`](../../scripts/review/results/2026-05-10-plan-issues-43-48-codex-round3.md) — MAJOR; exact touched-path placeholders remained.
- [`scripts/review/results/2026-05-10-plan-issues-43-48-codex-round4.md`](../../scripts/review/results/2026-05-10-plan-issues-43-48-codex-round4.md) — APPROVE; no remaining blocking findings.
