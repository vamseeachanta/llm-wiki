---
title: "Frontier Deepwater clearance checklist"
created: 2026-05-11
last_updated: 2026-05-11
issues: [vamseeachanta/llm-wiki#46, vamseeachanta/llm-wiki#19]
status: active-governance-prerequisite
public_safety: source-family metadata only; no raw private/vendor/client data
---

# Frontier Deepwater clearance checklist

## Purpose

This artifact implements the approved governance prerequisite for `vamseeachanta/llm-wiki#46` and keeps the parent blocker `vamseeachanta/llm-wiki#19` open until a separately approved implementation issue provides cleared inputs.

It is a public-safe input-readiness checklist only. It does not extract, copy, OCR, summarize, or ingest raw private/vendor/client material. The parent remains blocked until every required field below has an explicit approval/evidence value and a future implementation issue is approved.

## Source family / parent blocker

- Child governance issue: `vamseeachanta/llm-wiki#46`
- Parent blocker: `vamseeachanta/llm-wiki#19`
- Source family: Frontier Deepwater/offshore operations source candidates
- Sensitive class to guard: copyrighted articles, figures/images, vendor/private offshore operations material

## Raw/private boundary

Do not read, copy, OCR, summarize, or ingest raw source files from private source trees while using this checklist. Public output must be limited to repo-qualified governance metadata, public citations, allowed metadata fields, and authored synthesis that is independently cleared for publication.

Disallowed material includes raw private/vendor/client data, vendor standards text, formulas copied from copyrighted sources, tables, figures/images, credentials, personal/admin data, client/project-sensitive details, raw rows, private manifests, and path-rich private archive listings.

## Required clearance/input-readiness fields

| Field | Requirement |
| --- | --- |
| `candidate artifact id` | Required before any extraction/promotion issue can run. |
| `bibliographic/public citation` | Required before any extraction/promotion issue can run. |
| `copyright class` | Required before any extraction/promotion issue can run. |
| `image/figure flag` | Required before any extraction/promotion issue can run. |
| `archive flag` | Required before any extraction/promotion issue can run. |
| `allowed metadata fields` | Required before any extraction/promotion issue can run. |
| `allowed authored synthesis scope` | Required before any extraction/promotion issue can run. |
| `disallowed copied text/figures` | Required before any extraction/promotion issue can run. |
| `approval owner/date` | Required before any extraction/promotion issue can run. |
| `validator result` | Required before any extraction/promotion issue can run. |

## Allowed evidence/output types

- Public bibliographic citation and source-family metadata.
- Copyright class and image/figure/archive flags.
- Cleared authored synthesis scope.
- Validator result for exact touched artifacts.

## Disallowed evidence/output types

- Copied article text, figures/images, tables, vendor/private offshore operations material, private archive contents, and path-rich manifests.

## Future implementation issue template

A future implementation issue may be created only after this checklist is completed. Use this template:

```markdown
Title: feat(llm-wiki): promote cleared Frontier Deepwater/offshore operations source candidates metadata into public wiki artifacts

Parent: vamseeachanta/llm-wiki#19
Governance prerequisite: vamseeachanta/llm-wiki#46
Checklist artifact: `docs/governance/frontier-deepwater-clearance-checklist.md`

Scope:
- Promote only the approved public metadata/authored synthesis named in the completed checklist.
- Keep raw files source-of-record outside this repository.
- Do not copy raw text, figures, tables, row-level data, private manifests, or path-rich archive listings.

Required inputs:
- candidate artifact id
- bibliographic/public citation
- copyright class
- image/figure flag
- archive flag
- allowed metadata fields
- allowed authored synthesis scope
- disallowed copied text/figures
- approval owner/date
- validator result
- Completed public/raw boundary check.
- Named validator result and approval owner/date.

Acceptance criteria:
- Wiki/domain artifacts contain only approved public-safe content.
- Index/log/navigation are updated where applicable.
- Scoped public-safety scan over touched files returns no matches.
- Parent issue update states whether the parent remains blocked or what exact blocker was cleared.
```

## Parent issue update requirement

After this governance artifact is committed, post a progress update on both `vamseeachanta/llm-wiki#46` and `vamseeachanta/llm-wiki#19` stating:

- this checklist exists and is public-safe;
- no raw extraction or wiki promotion occurred;
- the parent remains blocked pending completed checklist fields and a separately approved future implementation issue;
- the exact validation commands used.

## Validation checklist

Run these commands from the repository root after editing this artifact:

```bash
uv run scripts/validate_governance_artifacts.py
TOUCHED='docs/governance/frontier-deepwater-clearance-checklist.md'
if grep -RInE 'BEGIN (RSA|OPENSSH|PRIVATE) KEY|password[[:space:]]*=|secret[[:space:]]*=|api[_-]?key[[:space:]]*=|social security|SSN|bank account|/mnt/ace(/|$)|/mnt/ace-data(/|$)' $TOUCHED \
  | grep -v 'grep -RInE'; then
  echo 'public-safety scan failed'
  exit 1
else
  echo 'public-safety scan passed'
fi
```

Expected result: the validator passes and the scoped public-safety scan returns `public-safety scan passed`. The second grep removes the literal validation-command line so the command does not self-match. Broad repository scans may be added as secondary evidence, but the touched-file scan above is mandatory.

