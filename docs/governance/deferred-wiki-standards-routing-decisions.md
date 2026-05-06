---
title: "Deferred Wiki Standards Routing Decisions"
created: 2026-05-06
last_updated: 2026-05-06
related_issue: 15
---

# Deferred Wiki Standards Routing Decisions

This record resolves the post-#2615 deferred standards-routing questions for `maritime-law`, `lng-projects`, and `acma-projects`.

## Decisions

| Wiki | Decision | Rationale | Follow-up |
|------|----------|-----------|-----------|
| `maritime-law` | Sanction `wiki/standards/` routing | IMO/ILO conventions and codes are standards-like governance instruments even when their frontmatter uses `consolidated_edition` rather than `revision`. | Follow-up implementation issue: #41. |
| `lng-projects` | Sanction `wiki/standards/` routing | LNG project pages will need stable routing for codes such as CSA-Z276, NFPA 59A, and the IGC Code as public-safe standards metadata is promoted. | Follow-up implementation issue: #42. |
| `acma-projects` | Defer indefinitely | The wiki is intentionally thin, and canonical firm/project copy remains outside this public repository. Standards routing is not worth sanctioning until a later explicit public scope exists. | No standards-routing implementation issue now. |

## Boundary

These decisions authorize public routing metadata only. They do not authorize copying raw PDFs, private archives, vendor standards text, convention/code excerpts, credentials, private mount paths, or private project material into this public repository.

## Implementation Notes

- Sanctioned standards pages should use the local wiki schema plus the standards-page extra fields where applicable.
- `maritime-law` may use `consolidated_edition` when that is the correct public metadata field for an IMO/ILO convention or code.
- `lng-projects` standards pages must remain metadata-only unless a separate issue explicitly approves public synthesis from committed public sources.
- `acma-projects` remains concepts/entities/sources only for standards-like material unless a future user-approved issue changes that decision.
