---
title: "O&G Standards catalog — ASCE"
slug: og-standards-asce
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
sources:
  - /mnt/ace/O&G-Standards/ASCE
ingested: 2026-05-09
tags: ["og-standards-ingest", "asce", "standards", "publisher-catalog", "wind-loads", "seismic-loads", "copri-mre"]
---

# O&G Standards catalog — ASCE

> Metadata-first source page for the ASCE (American Society of Civil Engineers) slice of the O&G-Standards consolidated library at `/mnt/ace/O&G-Standards/`. Generated 2026-05-09 from `/mnt/ace/O&G-Standards/_catalog.json` (catalog version 1.0.0, generated 2025-12-25).
> **Vendor PDFs do not enter this repo** per spinout 2026-05-05 governance — only publisher facts (titles, document IDs, revision years, file paths) are recorded here.

## Summary

ASCE (American Society of Civil Engineers) is the publisher of the ASCE 7 design-loads standard and a host of civil-engineering practice manuals. The ASCE slice of this catalog is **predominantly working-group / committee correspondence**, not standards: of 32 token-matched entries totaling ~204 MB, only **4 are ASCE-authored standards documents** (ASCE 7-98, ASCE 7-05, ASCE 7-02 wind-loads workbook, and one derivative wind-loads PDF). The remaining 28 entries are ASCE-COPRI Marine Renewable Energy (MRE) Committee meeting minutes, rosters, abstracts, and a CV — i.e., a snapshot of one practitioner's involvement in COPRI MRE governance from 2011 to 2015, which is committee-process material rather than published standards.

## Metadata

| Field | Value |
|-------|-------|
| id | og-standards-asce |
| publisher | ASCE (American Society of Civil Engineers) |
| document_count | 32 (token-matched); **4 standards documents**, 28 committee/working-group artifacts |
| total_size_bytes | 213,365,242 |
| total_size_mb | 203.5 |
| extension_breakdown | .pdf: 7, .docx: 17, .xlsx: 4, .doc: 3, .xls: 1 |
| sub_category_breakdown | ASCE-7 standard (PDF/XLS): 4, COPRI MRE Committee Minutes (.doc/.docx): 16, COPRI MRE rosters/policy/format (.xlsx/.doc/.docx/.pdf): 7, abstracts/correspondence/CV (.pdf/.doc): 5 |
| year_range | 1998–2015 (1998 and 2002/2005 are ASCE-7 standard editions; 2011–2015 are committee minutes) |
| top_year_buckets | 2012: 7, 2015: 5, 2013: 3, 2014: 3 (all committee-minutes years); 2007: 1; 2011: 1 |
| parent_root | (no `ASCE/` folder exists — files live under `/mnt/ace/O&G-Standards/Unknown/` (29), `/mnt/ace/O&G-Standards/OnePetro/` (2), `/mnt/ace/O&G-Standards/ISO/` (1)) |
| catalog_source | /mnt/ace/O&G-Standards/_catalog.json |
| ocr_text_root | /mnt/ace/O&G-Standards/_ocr_text |
| inventory_db | /mnt/ace/O&G-Standards/_inventory.db (6.8 GB sqlite) |
| raw_source_policy | link-only; do not copy raw bulk data into git/wiki raw folders |
| extract_priority | metadata-only (per #2536 deep-extraction queue) |
| ingest_loop | docs/sessions/2026-05-08-llm-wiki-completeness-loop.md (E13) |

## Topical coverage map

ASCE documents in this catalog grouped by code/series:

| Code / Series | Subject | Editions present | Representative filename |
|---------------|---------|------------------|-------------------------|
| ASCE 7-98 | Seismic and Wind Design of Concrete Buildings | 1998 | `ASCE_7-98_Seismic_and_Wind_Design_of_Concrete_Buildings.pdf` (184 MB — likely scanned) |
| ASCE 7-05 | Minimum Design Loads for Buildings and Other Structures | 2005 | `ASCE_7-05_Minimum_Design_Loads_for_buildings_and_other_Struc.pdf` |
| ASCE 7-05 (derivative) | Determination of Wind Loads — ASCE 7-05 (third-party derivative) | 2005-aligned | `DETERMINATION_OF_WIND_LOADS_ASCE_7-05.pdf` |
| ASCE 7-02 | Wind Loads (workbook) | 2002 | `Wind_Loads_ASCE_7-02.xls` |
| COPRI MRE Committee Minutes | ASCE-COPRI Marine Renewable Energy committee meeting minutes | 16 monthly minutes 2011-12 → 2015-08 | `2012_07_02_ASCE_COPRI_MRE_Committee_Minutes.docx` |
| COPRI MRE working papers | Roster, policy update, proposed meeting format, MRE Guide abstract, GoM oil spill statement | 2012–2015 | `Browne_ASCE_MRE_Guide_Abstract_25Jan2012.doc`, `2015_ASCE_COPRI_Policy_update.xlsx`, `New_ASCE_COPRI_MRE_COMMITTEE_MEETING_PROPOSED_FORMAT.docx`, `Bil_Stewart_Revised_Proposed_ASCE_COPRI_statement_on_the_Gulf_of_Mexico_Oil_Spill.docx` |
| ASCE-OTC special sessions | OTC special-session planning rosters | 2014 | `ASCE_OTC_Special_Sessions_1-Oct-14.xlsx`, `Senanayake_Monopile_ASCE_OTC_Special_Sessions_1-Oct-14.xlsx` |
| Practitioner CV / correspondence | (non-standard artifacts) | n/a | `V_Rapoport_CV_(asce).pdf`, `Gmail_-_ASCE_MRE_Guide_Document_-_Preliminary_Schedule.pdf`, `Master_Card_ASCE_2007a.pdf` |

## Verification

- **Catalog statistics anomaly**: `statistics.by_organization` does **not** list "ASCE" — the by_organization buckets are ASTM, Unknown, API, ISO, DNV, OnePetro, BSI, Norsok, MIL, NEMA, SNAME. ASCE documents above were located by filename token search; all 32 are mis-tagged as `Unknown` (29), `OnePetro` (2), or `ISO` (1).
- **Standards-vs-committee split**: only 4 of 32 entries are ASCE-published standards documents (ASCE 7-98, ASCE 7-05 PDF, ASCE 7-05 wind-loads derivative, ASCE 7-02 workbook). The remaining 28 are COPRI MRE committee process artifacts and a CV — they are ASCE-affiliated by metadata but should not be promoted as standards content.
- **ASCE 7-98 size flag**: the 184 MB ASCE 7-98 PDF is anomalously large for a single standards document and is almost certainly a high-DPI scan rather than a digital-native publication; OCR text in `_inventory.db` is the recommended consumption path.
- **Edition gap**: ASCE 7 has shipped 7-10 (2010), 7-16 (2016), and 7-22 (2022) since the latest catalogued edition (7-05). The catalog is roughly 20 years out of date for this code.
- **OCR availability**: `_inventory.db` provides per-page OCR text for all PDFs; `.docx`/`.xlsx` files require their own extractors.

## Recommended follow-ups

1. **Catalog re-classification**: file an issue against the catalog generator to re-bucket ASCE-authored files out of `Unknown/`, `OnePetro/`, and `ISO/` parents into a proper `ASCE/` parent root and to add ASCE to `statistics.by_organization`. Without this, ASCE coverage is invisible to any `organization`-filtered consumer.
2. **Per-code standards/ pages**: ASCE 7 is the only ASCE code with standards content present. A `wiki/standards/asce-7.md` page anchored on 7-05 (the most useful catalogued edition) with a revision-history note for 7-98 → 7-02 → 7-05 → (gap to 7-22) would consolidate the wind-load / minimum-design-loads thread. Cross-link into concepts/ for wind-loads and seismic-design.
3. **Working-group archive**: the 28 COPRI MRE committee artifacts (2011-12 → 2015-08) are not standards but **are** a coherent governance archive of one phase of the MRE Guide drafting. They should either be moved to a separate `wiki/governance-archives/copri-mre-2011-2015.md` page or excluded from standards-page indexing entirely. Do not surface them as standards content.
