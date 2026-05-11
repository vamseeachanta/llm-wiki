---
title: "HSE dataset clearance checklist"
created: 2026-05-11
last_updated: 2026-05-11
issues: [vamseeachanta/llm-wiki#45, vamseeachanta/llm-wiki#19]
status: active-governance-prerequisite
public_safety: source-family metadata only; no raw private/vendor/client data
---

# HSE dataset clearance checklist

## Purpose

This artifact implements the approved governance prerequisite for `vamseeachanta/llm-wiki#45` and keeps the parent blocker `vamseeachanta/llm-wiki#19` open until a separately approved implementation issue provides cleared inputs.

It is a public-safe input-readiness checklist only. It does not extract, copy, OCR, summarize, or ingest raw private/vendor/client material. The parent remains blocked until every required field below has an explicit approval/evidence value and a future implementation issue is approved.

## Source family / parent blocker

- Child governance issue: `vamseeachanta/llm-wiki#45`
- Parent blocker: `vamseeachanta/llm-wiki#19`
- Source family: HSE/safety dataset metadata and wiki candidates
- Sensitive class to guard: raw incident/safety rows, PII, sensitive incident records, private derived summaries

## Raw/private boundary

Do not read, copy, OCR, summarize, or ingest raw source files from private source trees while using this checklist. Public output must be limited to repo-qualified governance metadata, public citations, allowed metadata fields, and authored synthesis that is independently cleared for publication.

Disallowed material includes raw private/vendor/client data, vendor standards text, formulas copied from copyrighted sources, tables, figures/images, credentials, personal/admin data, client/project-sensitive details, raw rows, private manifests, and path-rich private archive listings.

## Required clearance/input-readiness fields

| Field | Requirement |
| --- | --- |
| `dataset/artifact id` | Required before any extraction/promotion issue can run. |
| `dataset citation/source-family label` | Required before any extraction/promotion issue can run. |
| `aggregation level` | Required before any extraction/promotion issue can run. |
| `PII/sensitive incident flag` | Required before any extraction/promotion issue can run. |
| `raw-row exclusion proof` | Required before any extraction/promotion issue can run. |
| `allowed aggregate/public metadata` | Required before any extraction/promotion issue can run. |
| `disallowed row-level fields` | Required before any extraction/promotion issue can run. |
| `approval owner/date` | Required before any extraction/promotion issue can run. |
| `target wiki page type` | Required before any extraction/promotion issue can run. |
| `secret/PII scan result` | Required before any extraction/promotion issue can run. |

## Allowed evidence/output types

- Public dataset citations and source-family labels.
- Aggregate counts/categories only after explicit clearance.
- Public-safe metadata fields and target wiki page type.
- Secret/PII scan result for exact touched files.

## Disallowed evidence/output types

- Row-level incident data, PII, sensitive incident narratives, private derived summaries, raw extracts, and path-rich manifests.

## Future implementation issue template

A future implementation issue may be created only after this checklist is completed. Use this template:

```markdown
Title: feat(llm-wiki): promote cleared HSE/safety dataset metadata and wiki candidates metadata into public wiki artifacts

Parent: vamseeachanta/llm-wiki#19
Governance prerequisite: vamseeachanta/llm-wiki#45
Checklist artifact: `docs/governance/hse-dataset-clearance-checklist.md`

Scope:
- Promote only the approved public metadata/authored synthesis named in the completed checklist.
- Keep raw files source-of-record outside this repository.
- Do not copy raw text, figures, tables, row-level data, private manifests, or path-rich archive listings.

Required inputs:
- dataset/artifact id
- dataset citation/source-family label
- aggregation level
- PII/sensitive incident flag
- raw-row exclusion proof
- allowed aggregate/public metadata
- disallowed row-level fields
- approval owner/date
- target wiki page type
- secret/PII scan result
- Completed public/raw boundary check.
- Named validator result and approval owner/date.

Acceptance criteria:
- Wiki/domain artifacts contain only approved public-safe content.
- Index/log/navigation are updated where applicable.
- Scoped public-safety scan over touched files returns no matches.
- Parent issue update states whether the parent remains blocked or what exact blocker was cleared.
```

## Parent issue update requirement

After this governance artifact is committed, post a progress update on both `vamseeachanta/llm-wiki#45` and `vamseeachanta/llm-wiki#19` stating:

- this checklist exists and is public-safe;
- no raw extraction or wiki promotion occurred;
- the parent remains blocked pending completed checklist fields and a separately approved future implementation issue;
- the exact validation commands used.

## Validation checklist

Run these commands from the repository root after editing this artifact:

```bash
uv run scripts/validate_governance_artifacts.py
TOUCHED='docs/governance/hse-dataset-clearance-checklist.md'
if grep -RInE 'BEGIN (RSA|OPENSSH|PRIVATE) KEY|password[[:space:]]*=|secret[[:space:]]*=|api[_-]?key[[:space:]]*=|social security|SSN|bank account|/mnt/ace(/|$)|/mnt/ace-data(/|$)' $TOUCHED \
  | grep -v 'grep -RInE'; then
  echo 'public-safety scan failed'
  exit 1
else
  echo 'public-safety scan passed'
fi
```

Expected result: the validator passes and the scoped public-safety scan returns `public-safety scan passed`. The second grep removes the literal validation-command line so the command does not self-match. Broad repository scans may be added as secondary evidence, but the touched-file scan above is mandatory.

