---
title: "Issue #45 Plan — HSE dataset clearance checklist"
created: 2026-05-10
last_updated: 2026-05-10
issue: 45
status: plan-review
public_safety: source-family metadata only; no raw private/vendor/client data
---

# Issue #45 Plan — HSE dataset clearance checklist

## Decision

Route this issue as a **planning/governance prerequisite**, not as raw extraction or wiki-promotion execution. The deliverable is a checked-in public-safe checklist/input-restoration plan plus parent-issue linkage. Implementation work remains blocked until explicit user approval moves the issue to `status:plan-approved`.

## Owned paths

- `docs/governance/` for durable checklist/input-readiness artifacts.
- `docs/plans/2026-05-10-issue-45-*.md` for this plan.

## Read-only context

- GitHub issue `vamseeachanta/llm-wiki#45` (Issue #45 Plan — HSE dataset clearance checklist) body and linked parent issues.
- `docs/reports/2026-05-10-llm-wiki-practical-completion-roadmap.md`.
- Existing `wikis/**` navigation only for context; no source promotion in this issue.

## Forbidden paths / actions

- Do not read, copy, OCR, summarize, or ingest raw source files from private `/mnt/ace` source trees.
- Do not commit vendor standards text, formulas, tables, figures, private archive contents, credentials, personal/admin data, client/project-sensitive details, or path-rich private manifests.
- Do not create wiki source stubs or domain pages from raw material in this issue.

## Source family / parent blocker

- Parent blocker: `vamseeachanta/llm-wiki#19` — feat(llm-wiki): plan offshore raw-source family wiki backfill candidates from /mnt/ace-data
- Source/input family: HSE/safety dataset metadata and wiki candidates
- Sensitive class to guard: raw incident/safety rows, PII, sensitive incident records, private derived summaries

## Deliverable

Create `docs/governance/hse-dataset-clearance-checklist.md` with:

1. Purpose and parent-blocker statement.
2. Raw/private/vendor/client boundary statement.
3. Required clearance/input-readiness fields.
4. Allowed vs disallowed evidence/output types.
5. Future implementation issue template.
6. Validation checklist and exact commands.
7. Parent-issue update requirement stating that the parent remains blocked.

## Required fields

- `dataset/artifact id`
- `dataset citation/source-family label`
- `aggregation level`
- `PII/sensitive incident flag`
- `raw-row exclusion proof`
- `allowed aggregate/public metadata`
- `disallowed row-level fields`
- `approval owner/date`
- `target wiki page type`
- `secret/PII scan result`

## Validation plan

- Deterministic content check: checklist artifact contains parent issue link, source-family label, required fields, allowed/disallowed evidence sections, future issue template, and explicit raw/private/vendor/client boundary.
- Public-safety scan over exact touched artifacts only; broad directory scans are secondary evidence, not a substitute:

```bash
TOUCHED='docs/governance/hse-dataset-clearance-checklist.md docs/plans/2026-05-10-issue-45-hse-dataset-clearance-checklist.md'
grep -RInE 'BEGIN (RSA|OPENSSH|PRIVATE) KEY|password[[:space:]]*=|secret[[:space:]]*=|api[_-]?key[[:space:]]*=|social security|SSN|bank account' $TOUCHED
```

Expected result: no matches for the concrete issue-owned files above. Do not scan broad historical directories as the only pass; optional broader repo safety scans may be added, but scoped touched-file validation is mandatory.

## Acceptance traceability

- Checklist names required fields -> `Required fields` table/list in the governance artifact.
- Checklist distinguishes public metadata/authored synthesis from disallowed raw/private/vendor/client material -> `Allowed evidence` and `Disallowed evidence` sections.
- Future implementation issue template and approval gate -> `Future implementation issue template` section.
- Boundary statement -> `Raw/private boundary` section.
- Parent issue remains blocked -> GitHub comment on repo-qualified parent and child issue; no parent closeout in this pass.

## Execution mode after approval

Central execution is preferred. The six governance/input-restoration issues can be batched only if each checklist artifact has a non-overlapping filename under `docs/governance/`. The orchestrator owns final validation, commit, push, and GitHub comments.

## Approval request

This plan is ready for review. Implementation should not begin until the user approves the plan and the issue is moved to `status:plan-approved`.
