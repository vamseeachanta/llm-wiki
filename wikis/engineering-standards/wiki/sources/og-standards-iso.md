---
title: "O&G Standards catalog — ISO"
slug: og-standards-iso
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
sources:
  - /mnt/ace/O&G-Standards/ISO
ingested: 2026-05-09
tags: ["og-standards-ingest", "iso", "standards", "publisher-catalog", "offshore", "subsea-risers", "materials", "thermal-spray", "drawing-conventions"]
---

# O&G Standards catalog — ISO

> Metadata-first source page for the ISO slice of the O&G-Standards consolidated library at `/mnt/ace/O&G-Standards/ISO/`. Generated 2026-05-09 from `/mnt/ace/O&G-Standards/_catalog.json` (catalog version 1.0.0, generated 2025-12-25).
> **Vendor PDFs do not enter this repo** per spinout 2026-05-05 governance — only publisher facts (titles, document IDs, edition years, file paths) are recorded here.

## Summary

ISO catalog covers four organized series subfolders (`13xxx`, `14xxx`, `15xxx`, `19xxx`) plus a large top-level dump that contains both legitimate ISO standards and ~200 misclassified personal/business documents (a known catalog hygiene issue, see Verification). After filtering, ~112 of the 308 raw entries are bona-fide ISO standards spanning 1975–2016. The offshore- and petroleum-relevant content concentrates in **ISO 19900 series** (offshore structures: 19901 metocean/seismic/topsides, 19902 fixed steel, 19905 jack-up, 19906 ice loads), the **ISO 13628 family** (subsea umbilicals, control systems, completion/workover risers, ROV interfaces) plus drilling-riser standards 13624/13625, **ISO 15156** (sour-service materials, all 3 parts), and **ISO 14224** (reliability data collection, 2016 edition). Ancillary coverage spans the 14xxx thermal-spray series (ten parts), 128/129/406/2768/5457/6410/7200/7519 drawing/dimensioning conventions, and metallic-materials testing (148 Charpy, 1099 axial fatigue, 6892 tensile, 7438 bend, 7539 SCC). Publication years skew 1999–2003 (early ISO petroleum-industry codification) and 2007–2012 (post-19900-series harmonization with API).

## Metadata

| Field | Value |
|-------|-------|
| id | og-standards-iso |
| publisher | ISO (International Organization for Standardization) |
| document_count_raw | 308 |
| document_count_legit | ~112 (filename matches `ISO_<num>` or `BS/DIN_EN_ISO_<num>`) |
| document_count_pollution | ~196 (BVI/personal/business documents misfiled into ISO/ top-level) |
| total_size_bytes | 770,979,678 |
| total_size_mb | 771.0 |
| total_size_legit_mb | ~549 |
| extension_breakdown | .pdf: 249, .doc: 44, .xls: 9, .docx: 4, .xlsx: 2 |
| sub_category_breakdown | TOP-LEVEL: 269, 13xxx: 17, 14xxx: 15, 15xxx: 5, 19xxx: 2 |
| year_range | 1975–2016 (modal years 1999, 2001, 2003, 2011, 2012) |
| top_year_buckets | 1999: 12, 2001: 9, 2003: 5, 2011: 5, 2002: 4, 2012: 4, 1991: 4 |
| modified_date_span | 2000-04-13 to 2017-09-13 |
| parent_root | /mnt/ace/O&G-Standards/ISO |
| catalog_source | /mnt/ace/O&G-Standards/_catalog.json |
| ocr_text_root | /mnt/ace/O&G-Standards/_ocr_text |
| inventory_db | /mnt/ace/O&G-Standards/_inventory.db (6.8 GB sqlite) |
| raw_source_policy | link-only; do not copy raw bulk data into git/wiki raw folders |
| extract_priority | metadata-only (per #2536 deep-extraction queue) |
| ingest_loop | docs/sessions/2026-05-08-llm-wiki-completeness-loop.md (E13) |

## Topical coverage map

ISO codes referenced by document ID, grouped by series. Edition coverage shown where multiple files for the same code exist.

### 19xxx — Offshore structures (petroleum & natural gas industries)

| Code | Subject | Editions/parts present |
|------|---------|------------------------|
| ISO 19901 | Specific requirements for offshore structures (metocean, seismic, topsides, geotechnical) | Parts 1–4, FDIS submitted 2003-era (4 files) |
| ISO 19902 | Fixed steel offshore structures | Annex C DIS, Clause 26 DIS (2 files) |
| ISO 19905-1 | Site-specific assessment of mobile offshore units (jack-ups) | CD 2007, DIS, FDIS-vs-2012-vs-FDIS-2015 comparison (10 files) |
| ISO 19906 | Arctic offshore structures (ice loads) | Future-version draft, FDIS (2 files) |

### 13xxx — Subsea production & drilling-riser equipment

| Code | Subject | Editions/parts present |
|------|---------|------------------------|
| ISO 13624-1 | Design and operation of marine drilling-riser equipment | DIN EN 2007-11, ISO 2009 (2 files) |
| ISO 13624-2 | Marine drilling-riser methodologies (Technical Report) | TR (1 file) |
| ISO 13625 | Drilling and production equipment | 1st Ed 2002 (1 file) |
| ISO 13628 | Subsea production systems (multi-part family) | Parts 1, 5 (1st/2nd Ed 2002, 2009), 6 (2006), 7 (DRAFT 2000, DRAFT 2003, 1st Ed 2005), 8 (DRAFT 2001), 12 (DRAFT 2011), 15 (Subsea Structures & Manifolds) — 11 files |
| ISO 13665 | Seamless and welded steel tubes for pressure | 1st Ed 1997 (1 file) |
| ISO 13679 | Procedures for testing casing and tubing connections | 1st Ed 2002 (1 file) |
| ISO 13819-2 | Fixed steel structures (precursor to 19902) | 1st Ed 1995 (1 file) |

### 14xxx — Thermal-spray coatings & QM

| Code | Subject | Editions present |
|------|---------|------------------|
| ISO 14224 | Petroleum/natural-gas — collection of equipment reliability and maintenance data | 2016 (1 file) |
| ISO 14231 | Thermal spraying — acceptance inspection of equipment | 1st Ed 2000 |
| ISO 14232 | Thermal spraying — powders, composition, technical supply | 1st Ed 2000 |
| ISO 14916 | Thermal spraying — determination of tensile adhesive strength | 1st Ed 1999 |
| ISO 14917 | Thermal spraying — terminology, classification | 1st Ed 1999 |
| ISO 14918 | Thermal spraying — approval testing of thermal sprayers | 1st Ed 1998 |
| ISO 14919 | Thermal spraying — wires, rods, cords for flame and arc spraying | 1st Ed 2001 (2 files) |
| ISO 14920 | Thermal spraying — spraying and fusing of self-fluxing alloys | 1st Ed 1999 |
| ISO 14921 | Thermal spraying — procedures for application of sprayed coatings | 1st Ed 2001 (2 files) |
| ISO 14922 | Thermal spraying — quality requirements (Pts 1, 2) | 1st Ed 1999 (2 files) |

### 15xxx — Sour-service materials, fracture toughness

| Code | Subject | Editions/parts present |
|------|---------|------------------------|
| ISO 15156 | Petroleum/natural-gas — materials for use in H₂S-containing environments | Pts 1, 2, 3 — 1st Ed 2001/2003 (3 files) |
| ISO 15653 | Quasi-static fracture-toughness test for metallic materials | 1st Ed 2010 (1 file) |

### 11xxx, 12xxx, 16xxx — Materials, transport, risk-based limit-state

| Code | Subject | Editions present |
|------|---------|------------------|
| ISO 11846 | Corrosion resistance — aluminium alloys | 1st Ed 1995 |
| ISO 11881 | Corrosion of metals — exfoliation corrosion test | 1st Ed 1999 + Corrigendum (4 files) |
| ISO 12736 | Wet thermal insulation coatings (subsea) | DRAFT, 2012 Appendix (2 files) |
| ISO 16389 | Dynamic risers for floating production installations | 2003 (2 files) |
| ISO 16708 | Pipeline transportation systems — reliability-based limit-state methods | 1st Ed 2006 (1 file) |

### 10xxx — Steel-tube inspection, casing calculations

| Code | Subject | Editions present |
|------|---------|------------------|
| ISO TR 10400 | Equations and calculations for casing/tubing properties | 1st Ed 2007 (1 file) |
| ISO 10474 | Steel and steel products — inspection documents | 1st Ed 1991 (1 file) |
| ISO 10893-1 | Non-destructive testing of steel tubes | 1st Ed 2011 (1 file) |

### 100s, 2xxx, 5xxx, 6xxx, 7xxx — Drawing conventions, dimensioning, metallic-material tests

| Code | Subject | Editions present |
|------|---------|------------------|
| ISO 128 | Technical drawings — general principles of presentation | Pts 1, 20, 21, 22, 23, 24, 25, 30, 33, 34/40 — 1996–2003 (10 files) |
| ISO 129 | Technical drawings — dimensioning, general principles | 1st Ed 1985 + BS ISO 129 (1985) + Pt 1 2004 (4 files) |
| ISO 148 | Charpy V-notch impact test | 1st Ed 1983 (2 files) |
| ISO 406 | Tolerancing of linear and angular dimensions | 2nd Ed 1987 (2 files) |
| ISO 1099 | Metallic materials — axial-load fatigue testing | 1975, DRAFT 2002, DIS (3 files) |
| ISO 1101 | Geometrical tolerancing — form, orientation, location, runout | 1st Ed 1983 (1 file) |
| ISO 2063 | Metallic and other inorganic coatings — thermal spraying | 2nd Ed 1991 (1 file) |
| ISO 2768 | Tolerances for linear, angular dimensions, geometric features | Pts 1, 2 — 1989, 1993 (5 files) |
| ISO 2902 | ISO metric trapezoidal screw threads | 1st Ed 1977 (2 files) |
| ISO 3183 | Petroleum/natural gas — line pipe (Pt 3) | 1st Ed 1999 (1 file) |
| ISO 4200 | Plain-end steel tubes, welded and seamless | 4th Ed 1991 (1 file) |
| ISO 5456 | Technical drawings — projection methods | Pt 1 1996 (1 file) |
| ISO 5457 | Technical product documentation — sizes and layout of drawing sheets | 2nd Ed 1999 (1 file) |
| ISO 6410 | Technical drawings — screw threads, threaded parts | Pt 1 1993 (1 file) |
| ISO 6892 | Metallic materials — tensile testing at ambient temperature | 2nd Ed 1998 (1 file) |
| ISO 7200 | Technical drawings — title blocks | 1st Ed 1984 (2 files) |
| ISO 7438 | Metallic materials — bend test | 1st Ed 1985 (1 file) |
| ISO 7519 | Construction drawings — general principles | 1st Ed 1991 (1 file) |
| ISO 7539-7 | Stress-corrosion cracking — slow strain-rate test | 1st Ed 1989 (1 file) |
| ISO 7573 | Technical drawings — item lists | 1st Ed 1983 (1 file) |
| ISO 8492 | Metallic materials — tube flattening test | 2nd Ed 1998 (1 file) |

## Verification

- Document count cross-checked against `_catalog.json` `statistics.by_organization.ISO = 308`
- Sub-category counts match `organizations.ISO`: General=269, 13xxx=17, 14xxx=15, 15xxx=5, 19xxx=2
- **Catalog-hygiene caveat**: ~196 files in the top-level `ISO/` directory are misclassified personal/business documents (BVI legal correspondence, bank reference letters, BVI domestic fees, pet import rules, etc.) — these inflate the raw 308 count and the 771 MB byte total. Filtering by filename prefix (`ISO_<num>`, `DIN_EN_ISO_<num>`, `BS_ISO_<num>`, or 5-digit `19xxx_` patterns from the 19902/19905 DIS files) yields ~112 legitimate ISO standards totalling ~549 MB.
- ISO 19900 already has prior wiki/standards/ treatment from W3 work (#2595)
- DRM status: see `/mnt/ace/O&G-Standards/drm_protected_files.txt` for any ISO files flagged as DRM-protected
- `_inventory.db` provides per-page OCR text for all PDFs (consume via SQLite, do not copy into wiki)

## Recommended follow-ups

1. **Catalog reclassification pass**: file a hygiene issue against `_catalog.json` to relabel the ~196 BVI/personal documents currently tagged `organization=ISO`. They were almost certainly placed in an `ISO` archive folder by accident at source-collection time. The reclassification should set `organization=Unknown` or a new `Personal` bucket so the legitimate ISO count surfaces cleanly in `statistics.by_organization`.
2. **Per-code standards/ pages for offshore-relevant ISO**:
   - **ISO 13628 family** (11 files spanning Pts 1, 5, 6, 7, 8, 12, 15) is the highest-coverage subsea-equipment series in the catalog and warrants `wiki/standards/iso-13628-<part>.md` pages.
   - **ISO 19901 / 19902 / 19905 / 19906** (offshore structures: metocean, fixed steel, jack-ups, ice loads) — single consolidated page or per-part pages following the DNV pattern.
   - **ISO 15156 Pts 1-3** (sour-service materials) — single page covering all three parts; high cross-reference value to NACE MR0175.
   - **ISO 14224:2016** (reliability data collection) — anchor page for cross-references from any reliability/RAM-engineering concept page.
3. **Cross-references into existing concepts/**: subsea umbilicals (13628 Pt 5), drilling risers (13624, 13625, TR 13624-2), completion/workover risers (13628 Pt 7), pipeline limit-state reliability (16708), thermal-spray coatings (14xxx series), tensile/Charpy/bend testing (148, 6892, 7438), SCC slow-strain-rate testing (7539-7).
4. **Edition-history index for ISO 13628 and 19905-1**: the catalog holds both DRAFT and 1st-Ed copies for several Pts of 13628, plus a 19905-1 2012-vs-FDIS-2015 comparison artefact — a comparison table would close the version-tracking gap and is unusual provenance worth surfacing.
5. **API ↔ ISO twin-coding map**: many ISO 19xxx and 13xxx codes are twinned with API standards (e.g. ISO 13628 Pt 4 ↔ API 17D, ISO 13628 Pt 5 ↔ API 17E, ISO 19901-7 ↔ API 2SK). A `comparisons/api-iso-twin-codes.md` page would make these crosswalks explicit and is a high-leverage reader-facing artefact.
