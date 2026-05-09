---
title: "O&G Standards catalog — ABS"
slug: og-standards-abs
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
sources:
  - /mnt/ace/O&G-Standards/ABS
ingested: 2026-05-09
tags: ["og-standards-ingest", "abs", "standards", "publisher-catalog", "offshore", "fpso", "fatigue", "dynamic-positioning"]
---

# O&G Standards catalog — ABS

> Metadata-first source page for the ABS (American Bureau of Shipping) slice of the O&G-Standards consolidated library at `/mnt/ace/O&G-Standards/`. Generated 2026-05-09 from `/mnt/ace/O&G-Standards/_catalog.json` (catalog version 1.0.0, generated 2025-12-25).
> **Vendor PDFs do not enter this repo** per spinout 2026-05-05 governance — only publisher facts (titles, document IDs, revision years, file paths) are recorded here.

## Summary

ABS (American Bureau of Shipping) is one of the IACS classification societies and a primary publisher of class rules and guides for offshore floating production, mobile offshore drilling units, and marine engineering systems. The ABS slice of this catalog is small and shallow — six PDF entries totaling ~13 MB, **none of which are filed under an `ABS/` parent folder**; instead they are scattered across `API/` and `BSI/` directories due to mis-classification at scan time. Coverage is limited to three Guidance (GUI) documents (Thrusters & DP, FPSO classification, Fatigue Assessment) and one OTC-2001 ABS-FPSO papers compilation.

## Metadata

| Field | Value |
|-------|-------|
| id | og-standards-abs |
| publisher | ABS (American Bureau of Shipping) |
| document_count | 6 |
| total_size_bytes | 13,896,265 |
| total_size_mb | 13.3 |
| extension_breakdown | .pdf: 6 |
| sub_category_breakdown | GUI (Guidance Notes / Guides): 4, generic Guide: 1, conference compilation (OTC): 1 |
| year_range | 1994–2010 (publication years on title pages); modified-date range 2000–2012 |
| top_year_buckets | 1994: 2 (GUI 00, GUI 002), 2003: 1 (GUI 115 1st ed), 2010: 1 (GUI 115 revised) |
| parent_root | (no `ABS/` folder exists — files live under `/mnt/ace/O&G-Standards/API/` and `/mnt/ace/O&G-Standards/BSI/`) |
| catalog_source | /mnt/ace/O&G-Standards/_catalog.json |
| ocr_text_root | /mnt/ace/O&G-Standards/_ocr_text |
| inventory_db | /mnt/ace/O&G-Standards/_inventory.db (6.8 GB sqlite) |
| raw_source_policy | link-only; do not copy raw bulk data into git/wiki raw folders |
| extract_priority | metadata-only (per #2536 deep-extraction queue) |
| ingest_loop | docs/sessions/2026-05-08-llm-wiki-completeness-loop.md (E13) |

## Topical coverage map

ABS documents in this catalog by document ID (as derived from filename), with edition coverage:

| Code | Subject | Editions present | Filename |
|------|---------|------------------|----------|
| GUI 00 | Guide for Thrusters and Dynamic Positioning Systems | 1994 | `ABS_GUI_00_(1994)_Guide_for_Thrusters_and_Dynamic_Positioning_Systems.pdf` |
| GUI 002 | Guide for Building and Classing Floating Production Storage Systems (FPSO) | 1994 | `ABS_GUI_002_(1994)_Guide_for_Building_and_Classing_Floating_Production_Storage_Systems.pdf` |
| GUI 115 | Guide for Fatigue Assessment of Offshore Structures | 2003, 2010 | `ABS_GUI_115_(2003)_...pdf`, `ABS_GUI_115_(2010)_...pdf` |
| (untitled) | ABS Guide Feb94 (generic; doc-id absent in filename) | 1994 | `ABS_Guide_Feb94.pdf` |
| OTC compilation | OTC 2001 ABS FPSO Papers (conference papers, not a standard) | 2001 (conference) | `OTC%202001_ABS_FPSO_Papers.pdf` |

## Verification

- **Catalog statistics anomaly**: `statistics.by_organization` does **not** list "ABS" — the by_organization buckets are ASTM, Unknown, API, ISO, DNV, OnePetro, BSI, Norsok, MIL, NEMA, SNAME. ABS documents above were located by filename token search (`^ABS[ _\-]`), not by the `organization` field. All six are mis-tagged: 2 as `API`, 4 as `BSI`. This is a catalog-builder defect worth filing as a follow-up issue.
- **Document count**: 6 (1 generic ABS Guide + 4 GUI series + 1 OTC paper compilation). Five are likely true ABS publications; the OTC compilation is a third-party assembly of ABS-authored conference papers and does not carry its own document number.
- **Edition pairs**: GUI 115 has both a 2003 and 2010 edition present — useful for revision-history work on offshore-structure fatigue.
- **DRM status**: see `/mnt/ace/O&G-Standards/drm_protected_files.txt` for any ABS files flagged as DRM-protected.
- **OCR availability**: `_inventory.db` provides per-page OCR text for all PDFs; consume via SQLite, do not copy into wiki.

## Recommended follow-ups

1. **Catalog re-classification**: file an issue against the catalog generator to re-bucket ABS-authored files out of `API/` and `BSI/` parents into a proper `ABS/` parent root and to add ABS to `statistics.by_organization`. The current state silently hides ABS coverage from any consumer that filters on `organization`.
2. **Per-code standards/ pages**: GUI 115 (Fatigue Assessment of Offshore Structures, 2003 → 2010) is the strongest candidate for a `wiki/standards/abs-gui-115.md` page consolidating the two editions; it complements DNV-RP-C203 in the fatigue-design landscape. GUI 002 (FPSO classification, 1994) warrants a standalone page given the persistent industry use of ABS FPSO class.
3. **Coverage gap**: the modern ABS Rules for Building and Classing Floating Production Installations (2014, 2018, 2020 revisions), Rules for Mobile Offshore Drilling Units (MODU), and Guide for Building and Classing Subsea Pipeline Systems are **absent** from this catalog. If those become available outside the vendor-PDF firewall (e.g., publisher datasheets, regulatory submissions), they would be the highest-value gap-fills for offshore-class coverage.
