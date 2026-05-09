---
title: "O&G Standards catalog — ASME"
slug: og-standards-asme
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
sources:
  - /mnt/ace/O&G-Standards/ASME
ingested: 2026-05-09
tags: ["og-standards-ingest", "asme", "standards", "publisher-catalog", "pressure-vessels", "piping", "bpvc", "b31", "fitness-for-service"]
---

# O&G Standards catalog — ASME

> Metadata-first source page for the ASME slice of the O&G-Standards consolidated library at `/mnt/ace/O&G-Standards/ASME/`. Generated 2026-05-09 from a direct filesystem walk (the 2025-12-25 `_catalog.json` consolidation pass did not enumerate this folder; `statistics.by_organization` lists API/ASTM/BSI/DNV/ISO/MIL/NEMA/Norsok/OnePetro/SNAME/Unknown but not ASME).
> **Vendor PDFs do not enter this repo** per spinout 2026-05-05 governance — only publisher facts (titles, document IDs, revision years, file paths) are recorded here.

## Summary

ASME (American Society of Mechanical Engineers) is the primary US authority for pressure-vessel, piping, and fitness-for-service standards. The 88 deduplicated catalog entries cover the Boiler & Pressure Vessel Code (BPVC) Sections I, II, V, VIII (Div 1/2/3), and IX; the B31 pressure-piping code family (B31.1, B31.3, B31.4, B31.8, B31.G); the B16 pipe-fitting and flange series (B16.5, B16.9, B16.10, B16.11, B16.20, B16.34, B16.47, B16.48 and roughly a dozen related parts); B36.10M dimensional standards; FFS-1 (jointly with API as 579-1); PCC-1 bolted-flange post-construction guidance; STP-PT-049 line-pipe temperature derating; OM-E2004 operations & maintenance; Y14.5 dimensioning and tolerancing; and the Tada/Paris/Irwin "Stress Analysis of Cracks Handbook" (9 chapter PDFs, ASME Press). The 1985–2013 publication-date span captures the 2007 and 2010 BPVC editions plus the 2009/2012 B31.G updates.

## Metadata

| Field | Value |
|-------|-------|
| id | og-standards-asme |
| publisher | ASME (American Society of Mechanical Engineers) |
| document_count | 88 |
| total_size_bytes | 1,030,473,055 |
| total_size_mb | 1030.5 |
| extension_breakdown | .pdf: 88 |
| sub_category_breakdown | BS/ (mixed B16 + reference): 47, Stress Analysis of Cracks Handbook: 9, BPVC VIII: 8, ASME root: 5, B31.G: 3, FFS-1: 3, B31.3: 2, B31.4: 2, B31.8: 2, BPVC II: 2, BPVC IX: 2, BPVC V: 2, B36.10M: 1, PCC-1: 1, STP-PT-049: 1, Y14.5: 1 |
| year_range | 1985–2013 (modal years 2007–2010) |
| top_year_buckets | 2009: 10, 2007: 7, 2010: 7, 1996: 5, 2012: 4, 1992: 3, 2000: 3 |
| parent_root | /mnt/ace/O&G-Standards/ASME |
| catalog_source | filesystem walk (not in /mnt/ace/O&G-Standards/_catalog.json statistics.by_organization) |
| ocr_text_root | /mnt/ace/O&G-Standards/_ocr_text |
| inventory_db | /mnt/ace/O&G-Standards/_inventory.db (6.8 GB sqlite) |
| raw_source_policy | link-only; do not copy raw bulk data into git/wiki raw folders |
| extract_priority | metadata-only (per #2536 deep-extraction queue) |
| ingest_loop | docs/sessions/2026-05-08-llm-wiki-completeness-loop.md (E13) |

## Topical coverage map

ASME codes referenced by document ID, with edition coverage in this catalog:

| Code | Subject | Editions present |
|------|---------|------------------|
| BPVC Section I | Rules for Construction of Power Boilers | 2010 |
| BPVC Section II Part D | Materials — Properties (Metric/Customary) | 2010 |
| BPVC Section V | Nondestructive Examination | 2009 (Addendum), 2010 |
| BPVC Section VIII Div 1 | Rules for Construction of Pressure Vessels | 2010, 2011 (Addenda 1) |
| BPVC Section VIII Div 2 | Alternative Rules — Pressure Vessels | 2007, 2010 (with Addenda) |
| BPVC Section VIII Div 3 | High-Pressure Vessels | 2001, 2007, 2010 |
| BPVC Section IX | Welding and Brazing Qualifications | 2010 |
| B1.1 | Unified Inch Screw Threads | 2003 |
| B16.5 | Pipe Flanges and Flanged Fittings (NPS 1/2 – 24) | 1996, 2009, 2013 |
| B16.9 | Factory-Made Wrought Buttwelding Fittings | 2001, 2007 |
| B16.10 | Face-to-Face/End-to-End Dimensions of Valves | 1992, 2009 |
| B16.15 | Cast Copper-Alloy Threaded Fittings | 1985 |
| B16.20 | Metallic Gaskets for Pipe Flanges | 2000 |
| B16.21 | Non-Metallic Flat Gaskets for Pipe Flanges | 1992 |
| B16.25 | Buttwelding Ends | (year unspecified) |
| B16.28 | Wrought Steel Buttwelding Short-Radius Elbows and Returns | 1994 |
| B16.33 | Manually Operated Metallic Gas Valves | 2002 |
| B16.34 | Valves — Flanged, Threaded, and Welding End | 1996 |
| B16.38 | Large Metallic Valves for Gas Distribution | 1985 |
| B16.39 | Malleable Iron Threaded Pipe Unions | 1998 |
| B16.47 | Large Diameter Steel Flanges (NPS 26 – 60) | 1996 |
| B16.48 | Line Blanks (Spectacle Blinds) | 1997 |
| B31.1 | Power Piping | 2007 |
| B31.3 | Process Piping | 2012 |
| B31.4 | Pipeline Transportation Systems for Liquids and Slurries | 2002, 2009 |
| B31.8 | Gas Transmission and Distribution Piping Systems | 2003, 2007 |
| B31.G | Manual for Determining the Remaining Strength of Corroded Pipelines | 1991, 2009, 2012 |
| B36.10M | Welded and Seamless Wrought Steel Pipe | 2004 |
| FFS-1 | Fitness-for-Service (joint with API 579-1) | 2007 (2nd Ed), 2009 (Errata 1) |
| OM-E2004 | Operations & Maintenance — Pressure-Relief Devices | 2004 |
| PCC-1 | Guidelines for Pressure Boundary Bolted Flange Joint Assembly | 2000 |
| STP-PT-049 | Investigation of Temperature Derating Factors for High-Strength Line Pipe | 2012 |
| Y14.5 | Dimensioning and Tolerancing | 1994 (Y14.5M), 2009 |
| Stress Analysis of Cracks Handbook | Tada/Paris/Irwin reference (ASME Press, 9 chapter PDFs: fm, ch1–ch7, bm) | (3rd Ed) |

Notes:
- `BS/` subdirectory inside `ASME/` is misnamed — its contents are predominantly ASME B16 and B31 documents (47 files), plus three non-ASME reference items (an MSS SP-97 2006 valve standard and two McGraw-Hill reference books on B31 piping and pressure-relief devices). Reclassification candidate.
- `WinZip.pdf` is a non-content placeholder and should be excluded from any downstream extraction queue.

## Verification

- Document count cross-checked against direct filesystem walk: 88 PDFs in `/mnt/ace/O&G-Standards/ASME/` (matches user-stated expectation).
- Catalog gap: `_catalog.json` `statistics.by_organization` does not enumerate "ASME" — the consolidation pass on 2025-12-25 indexed only API, ASTM, BSI, DNV, ISO, MIL, NEMA, Norsok, OnePetro, SNAME, and Unknown. The ASME folder is dated 2022-06-23 (mtime), so it predates the consolidation but was skipped. Filing follow-up to extend the consolidation script.
- DRM status: see `/mnt/ace/O&G-Standards/drm_protected_files.txt` for any ASME files flagged as DRM-protected.
- OCR availability: ASME PDFs are present at `/mnt/ace/O&G-Standards/_ocr_text/ASME/` only if the consolidation pass picked them up — verify per-file before relying on OCR; use `_inventory.db` SQLite as authoritative.

## Recommended follow-ups

1. **Per-code standards/ pages**: codes with multi-edition coverage warrant a `wiki/standards/asme-<code-id>.md` page consolidating revision history. Highest-value: ASME B31.G (1991/2009/2012), B31.3 (2012), B31.4 (2002/2009), B31.8 (2003/2007), BPVC VIII Div 1/2/3 (2001/2007/2010/2011), B16.5 (1996/2009/2013), FFS-1 (2007/2009), Y14.5 (1994/2009).
2. **Topical concept pages**: cross-link this source into existing concepts/ for fitness-for-service (FFS-1 + B31.G), pressure-vessel design (BPVC VIII), pipeline integrity (B31.G corrosion-assessment Level 1/2), process piping (B31.3), welding qualification (BPVC IX), and bolted-flange assembly (PCC-1 + B16 series).
3. **Catalog repair**: file an issue against the O&G-Standards consolidation script to enumerate the ASME folder in the next pass so `statistics.by_organization.ASME` is populated and `relative_path` rewriting is consistent with the API/DNV slices.
4. **Reclassify `BS/` subfolder**: 47 ASME B16 and B31 files are nested under `ASME/BS/` (ambiguous folder name shared with the British Standards prefix); rename to `ASME/B16-collection/` or split into per-series folders to match the rest of the tree.
5. **Reference-book pruning**: three non-standard items in `BS/` (MSS SP-97 valve standard, McGraw-Hill simplified-piping book, McGraw-Hill pressure-relief-devices book) should move to a `references/` sibling so the ASME slice contains only ASME publications.
