<!--
  Template: lng-projects/wiki/standards/<code-id>.md
  ----------------------------------------------------
  Use this template when authoring a NEW standards-page in the lng-projects
  wiki. This is the precedent setter — the lng-projects wiki has zero
  standards/ pages as of 2026-05-09. Subsequent standards/ pages should
  follow this shape unless the schema evolves.

  AUTHORING RULES (non-negotiable):
    1. Public OSS repo (MIT + CC-BY-4.0). Vendor-PDF firewall: include only
       publisher facts (code_id, publisher, revision, public_url). Never
       reproduce clause text, formulas, tables, figures, or transcribed
       passages from a vendor PDF. Cite the publisher catalog instead.
    2. Frontmatter required fields: title, tags, added, last_updated, domain,
       code_id, publisher, revision  (see lng-projects/CLAUDE.md schema).
    3. Optional 3-value `methodology_status` vocabulary (engineering-standards
       imported convention):
          - stale-as-of-publisher-cycle    (revision on disk lags catalog)
          - catalog-absent-publisher-only  (no local copy; metadata only)
          - current                        (matches publisher catalog)
    4. Filename = lowercase-slug of code_id (e.g. `csa-z276.md`,
       `nfpa-59a.md`, `igc-code.md`). Replace this file's name when copying.
    5. Bidirectional cross-references: any concepts/* page you link MUST
       gain a return link in its own "Cross-references" section.
    6. Keep this template body as `_<author: ...>_` italic placeholders so
       future authors fill in the blanks. Do NOT pre-fill with a real code.
-->

---
title: "<CODE-ID> — <Short title> (bounded summary)"
slug: <code-id-lowercase>
tags: ["<publisher-lowercase>", "standards", "lng", "metadata-only"]
added: YYYY-MM-DD
last_updated: YYYY-MM-DD
domain: lng-projects
# --- standards-page extra fields (engineering-standards-imported convention) ---
code_id: <code-id-lowercase>           # e.g. csa-z276, nfpa-59a, igc-code, sigtto-lng-stdg
publisher: <Publisher>                 # e.g. CSA Group, NFPA, IMO, SIGTTO, OCIMF
revision: "<edition-or-year>"          # e.g. "2023", "5e-2024"; use "not-on-disk" if catalog-absent
revision_source: <publisher-catalog-url-or-disk-path>
verified_on: YYYY-MM-DD
public_url: <publisher-public-catalog-url>
# methodology_status: current | stale-as-of-publisher-cycle | catalog-absent-publisher-only
# jurisdiction: <regulatory-or-geographic-scope-if-applicable>     # optional
# supersedes: ["<prior-code-id>"]                                   # optional
sources:
  - <link-to-lng-projects-sources-page-or-future-promotion>
extraction_policy: metadata-only
raw_copy_allowed: false
---

# <CODE-ID> — <Short title>

## Scope

_<author: 1–2 paragraphs describing what the standard covers and which
LNG-projects regime it governs. Pick from: siting / regulatory / safety /
construction / shipping / mooring / operations. Bound the page as
metadata-only; do not paraphrase clauses or reproduce numbered
requirements. End with the locally-cached revision and a re-pin reminder
for downstream consumers.>_

## Why this page exists

_<author: state the resolver role. If this page backs a `Citation`
instance under `.claude/rules/calc-citation-contract.md`, name the
calc module(s) that resolve here (frontmatter fields code_id /
publisher / revision). If purely informational, say so.>_

## Edition history

_<author: table of editions present in catalog OR publisher-current.
If no local copy exists, set `revision: not-on-disk` in frontmatter and
populate the catalog row only. Cite the lng-projects `_catalog.json`
doc-id where available.>_

| Edition / revision | Year | On disk? | Catalog doc-id | Notes |
|--------------------|------|----------|----------------|-------|
| _<e.g. 1st ed>_    | YYYY | yes/no   | _<doc-id>_     | _<note>_ |
| _<current>_        | YYYY | _<...>_  | _<...>_        | _<...>_ |

## Key sections

_<author: bullet outline of the most-cited Articles / Parts / Sections.
Section *titles only* — no clause text. Link out to the publisher
catalog for full text. Aim for 5–12 bullets.>_

- §_<n>_ _<section title>_ — _<one-line topic>_
- §_<n>_ _<section title>_ — _<one-line topic>_
- _<...>_

## Cross-references

_<author: bidirectional links. Any concepts/* page linked here MUST
get a return link in its own Cross-references section.>_

**Sibling lng-projects standards** _(populate as more standards/ pages land)_
- _<e.g. [[csa-z276]] — bulk LNG production/storage/handling>_
- _<e.g. [[nfpa-59a]] — US LNG facility safety>_
- _<e.g. [[igc-code]] — international LNG carrier construction/equipment>_

**lng-projects concepts** _(8 pages exist as of 2026-05-09; link the relevant ones)_
- [[lng-project-lifecycle]](../concepts/lng-project-lifecycle.md)
- [[lng-project-shapes]](../concepts/lng-project-shapes.md)
- [[lng-regulatory-framework]](../concepts/lng-regulatory-framework.md)
- [[lng-process-safety]](../concepts/lng-process-safety.md)
- [[lng-liquefaction-processes]](../concepts/lng-liquefaction-processes.md)
- [[lng-storage-tanks]](../concepts/lng-storage-tanks.md)
- [[lng-marine-transfer-systems]](../concepts/lng-marine-transfer-systems.md)
- [[lng-boil-off-gas-management]](../concepts/lng-boil-off-gas-management.md)

**Cross-wiki (engineering-standards)** _(only when materially relevant)_
- _<e.g. ASME B31.4 / B31.8 — for LNG export/import pipelines (../../engineering-standards/wiki/standards/asme-b31-8.md)>_
- _<e.g. API 510 / 570 — for inservice inspection of LNG-facility pressure vessels and piping>_
- _<e.g. DNV-RP-C203 — fatigue, when LNG terminals tie into offshore steel structures>_

**International / regulatory parallels**
- _<e.g. IMO IGC Code — gas-carrier construction; pair with national codes>_
- _<e.g. SIGTTO publications — operational best practice complement to formal codes>_
- _<e.g. EU Seveso III / US 49 CFR 193 — jurisdictional siting overlay>_

## Sources

_<author: link the lng-projects sources/ catalog page summarizing
the publisher catalog or the locally-cached revision. If no sources/
page exists yet, file a future-promotion stub here and create the
sources/ page when raw-corpus indexing reaches this code.>_

- _<e.g. [[lng-projects-sources-csa-z276]](../sources/<slug>.md) — sources/* catalog summary>_
- [Calc citation contract](../../../../.claude/rules/calc-citation-contract.md)
- Publisher catalog: <public_url>
