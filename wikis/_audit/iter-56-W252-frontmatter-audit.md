# iter-56 W252 — Cross-Wiki Frontmatter Schema-Vocabulary Audit

> **Scope:** All 3 in-spinout wikis (`engineering-standards`, `lng-projects`, `maritime-law`) — every `wiki/**/*.md` page.
> **Method:** Parse YAML frontmatter from each page; tabulate field usage, value-shapes, and per-wiki adoption rates; cross-check against canonical schema in each `CLAUDE.md`.
> **Scope-exclusions:** `_audit/` (this directory) and code-block frontmatter examples inside CLAUDE.md schemas.
> **Per V14 (W247) Option-B pivot:** vocabulary stalled at eng-stds-only adoption; lng + maritime spot-check ad-hoc. This audit quantifies that drift and proposes iter-57 batch actions.

---

## 1. Headline numbers

| Wiki | Total `.md` | With frontmatter | FM coverage |
|---|---:|---:|---:|
| engineering-standards | 218 | 217 | 99.5% |
| lng-projects | 33 | 30 | 90.9% |
| maritime-law | 81 | 79 | 97.5% |
| **Total** | **332** | **326** | **98.2%** |

**Distinct field names across all wikis:** **61** (a high number — see anomalies §3).

Section breakdown (eng-stds dwarfs the others on standards-page count):

| Wiki | standards/ | concepts/ | entities/ | sources/ |
|---|---:|---:|---:|---:|
| eng-stds | 161 | 35 | 0 | 19 |
| lng-projects | 10 | 12 | 0 | 8 |
| maritime-law | 25 | 27 | 24 | 2 |

---

## 2. Field-usage census — top-15 fields

Adoption is computed against pages-with-frontmatter for each wiki (217 / 30 / 79).

| Field | eng | lng | mar | Total | eng% | lng% | mar% | Shape(s) |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| `last_updated` | 217 | 30 | 79 | 326 | 100% | 100% | 100% | date |
| `title` | 215 | 29 | 78 | 322 | 99% | 97% | 99% | string |
| `added` | 215 | 29 | 77 | 321 | 99% | 97% | 97% | date |
| `tags` | 215 | 29 | 77 | 321 | 99% | 97% | 97% | **block_list, inline_list** |
| `domain` | 217 | 30 | 69 | 316 | 100% | 100% | 87% | string |
| `sources` | 214 | 29 | 53 | 296 | 99% | 97% | 67% | **block_list, inline_list** |
| `slug` | 138 | 16 | 24 | 178 | 64% | 53% | 30% | string |
| `extraction_policy` | 169 | 9 | 0* | 178 | 78% | 30% | 0%* | string |
| `raw_copy_allowed` | 165 | 9 | 0* | 174 | 76% | 30% | 0%* | bool |
| `code_id` | 161 | 9 | 4* | 174 | 74% | 30% | 5%* | string |
| `publisher` | 161 | 9 | 4* | 174 | 74% | 30% | 5%* | string |
| `revision` | 161 | 9 | 0 | 170 | 74% | 30% | 0% | string |
| `public_url` | 115 | 4 | 0 | 119 | 53% | 13% | 0% | string |
| `cross_links` | 12 | 22 | 71 | 105 | 6% | 73% | 90% | **block_list, inline_list** |
| `verified_on` | 74 | 4 | 0 | 78 | 34% | 13% | 0% | date |

*Asterisks: maritime-law numbers for `code_id`/`publisher`/`extraction_policy`/`raw_copy_allowed`/`instrument_type`/`consolidated_edition` understate true adoption — see §3.A.

Standards-page-only adoption rates (the population where these fields *should* fire):

| Field | eng-stds standards/ (n=161) | lng-projects standards/ (n=10) | maritime-law standards/ (n=25) |
|---|---:|---:|---:|
| `code_id` | 100% | 90% | **0% YAML / 72% pseudo-fence** |
| `publisher` | 100% | 90% | **0% YAML / 72% pseudo-fence** |
| `revision` | 100% | 90% | 0% (schema says "optional when applicable") |
| `extraction_policy` | 100% | 90% | **0% YAML / 72% pseudo-fence** |
| `raw_copy_allowed` | 100% | 90% | **0% YAML / 72% pseudo-fence** |
| `public_url` | 71% | 40% | 0% |
| `publisher_catalog_url` | 41% (W184) | 0% | 0% |
| `jurisdiction` | 32% | 90% | 0% (declared, unused) |
| `cross_links` | 6% | 90% | 96% |
| `verified_on` | 46% | 40% | 0% |
| `methodology_status` | 9% (W191) | 30% | 0% |

---

## 3. Anomalies and drift

### 3.A — **Critical: maritime-law double-fence ("pseudo-fence") frontmatter** (NEW finding)

18 of 25 maritime-law `standards/*.md` pages use a **non-YAML triple-block layout**:

```
---
title: "..."
tags: [...]
...
cross_links: []
--- maritime-law standards-page extra fields (treaty-flavored) ---
code_id: athens-convention-2002
publisher: IMO
instrument_type: treaty
consolidated_edition: "..."
amendment_status: "..."
extraction_policy: metadata-and-doctrinal-synthesis
raw_copy_allowed: false
---
```

The text after the second `---` line is **not parseable as YAML frontmatter** — every standard YAML/Pandoc/Hugo/MkDocs/lint tool will see only the first block. Hidden fields in the pseudo-fence (per page, n=18):

- `code_id`, `publisher`, `instrument_type`, `consolidated_edition`, `amendment_status`, `jurisdiction`, `effective_date`, `sources`, `extraction_policy`, `raw_copy_allowed` — all 18/18.
- `parent_instrument` — 17/18.

**Effective per-field adoption on maritime-law standards/ rises from 0% → 72%** when you include the pseudo-fence. The remaining 7 standards/ pages have neither the pseudo-fence nor the fields in YAML — true gaps.

**Two new fields invented inside the pseudo-fence and never declared in any CLAUDE.md schema:** `amendment_status`, `effective_date`, `parent_instrument`.

### 3.B — Value-shape drift (block_list ↔ inline_list)

| Field | Block-list pages | Inline-list pages | Notes |
|---|---:|---:|---|
| `tags` | 104 (96 eng + 8 lng) | 217 (119 eng + 21 lng + 77 mar) | Within eng-stds: 45% block / 55% inline split — internal inconsistency |
| `sources` | 282 (212 eng + 17 lng + 53 mar) | 14 (2 eng + 12 lng) | lng-projects is 41% inline — drift seam |
| `cross_links` | 72 (12 eng + 13 lng + 47 mar) | 33 (9 lng + 24 mar) | Used inconsistently in lng AND maritime |
| `supersedes` | 4 inline | 42 string | eng-stds: scalar string vs inline list — wrong shape if multiple supersedes |

### 3.C — Date-vs-string drift

| Field | date count | string count |
|---|---:|---:|
| `ingested` | 19 | 3 |
| `created` | 1 | 4 |

`created` is rarely used (5 pages total) and never declared in any schema. Drop or formalize.

### 3.D — Wiki-specific fields (37 of 61 fields appear in exactly one wiki)

**eng-stds-only (35 fields):** `legacy_code_id`(15), `legacy_publisher`(10), `legacy_slug`(5), `also_known_as`(9), `canonical_relationship`(4), `joint_publication`(4), `iso_equivalent`(8), `iso_relationship`(6), `bs_doc_number`(10), `abs_doc_number`(8), `nace_doc_number`(8), `norsok_doc_number`(6), `aws_doc_number`(6), `ampp_doc_number`(2), `prior_nace_doc_number`(1), `abs_part_section`(3), `instrument_type`(42), `publisher_full`(41), `publisher_current_edition`(37), `publisher_current_revision`(6), `publisher_catalog_url`(66), `revision_source`(74), `revision_source_status`(9), `revision_amendments_note`(8), `revision_in_catalog`(1), `superseded_by`(9), `superseded_by_note`(8), `supersession_note`(1), `multi_edition_note`(1), `withdrawn_year`(1), `lifecycle_status`(6), `cross_references`(6), `ledger_id`(30), `norsok_series`(6), `status`(2).

**maritime-law-only (3 fields, post-pseudo-fence):** `consolidated_edition`(4 YAML + 18 pseudo-fence), `source_file`(2), `embedded_in`(1) + the pseudo-fence-only fields `amendment_status`, `effective_date`, `parent_instrument`.

**lng-projects-only:** zero — every lng field also exists in eng-stds.

### 3.E — Fields used but **not declared in any CLAUDE.md schema**

Schema files declare 11 fields total (`title, tags, added, last_updated, sources, domain, cross_links` + standards: `code_id, publisher, revision, jurisdiction, supersedes`). The other **50 fields are undeclared**.

Highest-volume undeclared fields (cross-wiki risk):

| Field | Volume | Status |
|---|---:|---|
| `extraction_policy` | 178 | **De-facto canon — undeclared.** Should propagate. |
| `raw_copy_allowed` | 174 | **De-facto canon — undeclared.** Should propagate. |
| `slug` | 178 | Soft canon, dropped on many pages. |
| `public_url` | 119 | Should propagate. |
| `verified_on` | 78 | Should propagate. |
| `revision_source` | 78 | eng-stds-specific (private path). Keep wiki-specific. |
| `publisher_catalog_url` | 66 | W184 — eng-stds only. Should propagate to lng + mar. |
| `instrument_type` | 42 + 18 mar pseudo-fence | Should be cross-wiki for non-revision-based standards. |
| `methodology_status` | 17 | W191 — should propagate. |

---

## 4. Recommendations

### 4.A — Fields to formally promote to all-wiki canon (Tier-1, mandatory on standards-pages)

Update all 3 `CLAUDE.md` "Standards page extra fields" tables to add:

- `extraction_policy` (string; values: `metadata-only`, `metadata-and-doctrinal-synthesis`, `bounded-summary`, `none`) — **required**
- `raw_copy_allowed` (bool) — **required**
- `public_url` (string URL) — **required when a public publisher catalog/landing page exists**
- `publisher_catalog_url` (string URL) — recommended
- `verified_on` (date) — recommended (W184 pattern)
- `methodology_status` (string; values: `current`, `legacy`, `superseded`, `withdrawn`) — recommended (W191 pattern)
- `instrument_type` (string; values: `code`, `standard`, `treaty`, `mou`, `convention`, `recommended-practice`) — recommended

### 4.B — Wiki-specific fields (do NOT propagate)

- `legacy_code_id`, `legacy_publisher`, `legacy_slug`, `canonical_relationship`, `also_known_as`, `joint_publication` — **eng-stds-only by design** (rename history is a publisher-merger artifact specific to AMPP/NACE/ISO standards). W184/W185 origin.
- `<publisher>_doc_number` (8 variants) — eng-stds-only; publisher-internal cataloging.
- `revision_source`, `revision_in_catalog`, `revision_amendments_note` — eng-stds-only (private filesystem paths leak otherwise).
- `iso_equivalent`, `iso_relationship` — eng-stds-only (ISO-twinning is technical-standards specific).
- `consolidated_edition`, `amendment_status`, `parent_instrument`, `effective_date` — **maritime-law-specific**; declare them properly in `maritime-law/CLAUDE.md`.

### 4.C — Standardize value-shapes cross-wiki

Pick block-list everywhere (matches majority + supports trailing comments). Targets:
- `tags` — convert all 217 inline-list eng-stds + lng + mar pages to block-list.
- `sources` — convert 14 inline-list pages (mostly lng).
- `cross_links` — convert 33 inline-list pages.
- `supersedes` — always inline-list `[a, b]` (most "standards" supersede a single prior, but the schema must allow multiple).

### 4.D — **P0 fix: eradicate maritime-law pseudo-fence**

18 standards-pages use `--- maritime-law standards-page extra fields ... ---` which no parser will read. **Merge fields into the leading YAML frontmatter** and drop the pseudo-fence. This unblocks lint, search, and downstream consumers.

### 4.E — Declare undeclared fields

Add the Tier-1 list (§4.A) to all 3 `CLAUDE.md` schema tables. Track wiki-specific extensions (§4.B) as **optional in their owning wiki's schema only.**

---

## 5. iter-57 batch-action plan

Ordered by cost-of-defect-currently-shipping.

1. **W253 (P0, ~1 hr)** — Migrate 18 maritime-law pseudo-fence standards-pages to single-block YAML frontmatter. Mechanical regex replacement; verify 18/18 still parse. Touches `maritime-law/wiki/standards/*.md`.
2. **W254 (P0, ~30 min)** — Update `maritime-law/CLAUDE.md` schema to formally declare `instrument_type`, `consolidated_edition`, `amendment_status`, `effective_date`, `parent_instrument`, `extraction_policy`, `raw_copy_allowed`. Mark them required-when-applicable on `wiki/standards/*.md`.
3. **W255 (P1, ~1.5 hr)** — Cross-wiki promotion: edit `engineering-standards/CLAUDE.md`, `lng-projects/CLAUDE.md`, `maritime-law/CLAUDE.md` to add `extraction_policy`, `raw_copy_allowed`, `public_url`, `publisher_catalog_url`, `verified_on`, `methodology_status`, `instrument_type` to the standards-page extra-fields table.
4. **W256 (P1, ~2 hr)** — Value-shape normalization pass: `tags` and `sources` to block-list across all wikis; `cross_links` to block-list. Mechanical script + diff review. Defines a level-2 lint check that fires on inline `tags:`/`sources:` going forward.
5. **W257 (P2, ~1 hr)** — Add `extraction_policy`, `raw_copy_allowed`, `public_url` to the 7 maritime-law standards-pages and 1 lng-projects standards-page that lack them.
6. **W258 (P2)** — Decision item: drop `created`(5 uses) — replace with `added` everywhere; drop `status`(2 uses) — formalize as `methodology_status` instead. Drop `slug`-required-for-standards (already on 100% of eng-stds standards but only 30% of maritime). Either backfill or de-require.
7. **W259 (P3, post-iter-58)** — Promote the W184 ledger model (`legacy_code_id`, `also_known_as`, `canonical_relationship`, `joint_publication`) to a *separate* per-wiki rename-history table — clearly scoped to eng-stds; do NOT cross-wiki.

**Carry-over from V14 (W247) Option-B:** pivot held — vocabulary still drifts. The W253–W256 batch closes the schema-side of the gap; W257–W258 closes the data-side.

---

## 6. Sign-off / next-iter

- **Author:** iter-56 audit (W252).
- **Date:** 2026-05-10.
- **Cited memory:** project_llm_wiki_strategic_role, project_wiki_standards_path_decision, V14 (W247).
- **Audit ID:** iter-56-W252.
- **Next:** iter-57 W253–W256 mechanical batch (the P0+P1 items). iter-58 reruns this census; expectation is 61 distinct fields → ~25 declared canonical + ~10 wiki-specific = ~35.
