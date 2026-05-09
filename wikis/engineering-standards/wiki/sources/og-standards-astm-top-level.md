---
title: "O&G Standards catalog — ASTM top-level loose (B/C/F/other committees)"
slug: og-standards-astm-top-level
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
sources:
  - /mnt/ace/O&G-Standards/ASTM/*.pdf (top-level only; excludes A/D/E/G-Series sub-folders)
ingested: 2026-05-09
tags: ["astm", "top-level", "b-series", "c-series", "f-series", "non-series", "og-standards-ingest", "publisher-catalog"]
---

# O&G Standards catalog — ASTM top-level loose (B/C/F/other committees)

> Metadata-first source page for the residual top-level slice of the ASTM library at `/mnt/ace/O&G-Standards/ASTM/*.pdf`, excluding files already filed under `A-Series/`, `D-Series/`, `E-Series/`, or `G-Series/`. Generated 2026-05-09 from `/mnt/ace/O&G-Standards/_catalog.json` (catalog version 1.0.0, generated 2025-12-25).
> **Vendor PDFs do not enter this repo** per spinout 2026-05-05 governance — only publisher facts (titles, document IDs, revision years, file paths) are recorded here.

## Summary

This page covers the 9,136 ASTM PDFs that sit at the top level of the ASTM mount and were never filed into a per-letter sub-folder. It is a residual / overflow bucket dominated by ASTM committees that do not (yet) have their own series sub-folder: F (specific products & fasteners), C (cement & concrete), and B (non-ferrous metals), with smaller D and E stragglers that escaped the series sweep. Filename quality is degraded — roughly 54.7% of files carry a corrupted base64-ish trailing token (e.g. `B 327 - 01 _QJMYNW_.pdf`) decoded from PDF metadata during an earlier ingest, so any downstream code-extraction pass must normalize aggressively before joining against ASTM's published catalog.

## Metadata

| Field | Value |
|-------|-------|
| id | og-standards-astm-top-level |
| publisher | ASTM International |
| document_count | 9,136 |
| total_size_bytes | 745,768,087 |
| total_size_mb | 711.2 |
| total_size_gb | 0.69 |
| extension_breakdown | .pdf: 9,136 |
| parent_root | /mnt/ace/O&G-Standards/ASTM (filter: top-level only — excludes `/A-Series/`, `/D-Series/`, `/E-Series/`, `/G-Series/` sub-paths) |
| committee_letter_breakdown | F: 3,376; C: 2,818; B: 1,708; D: 685; E: 521; A: 18; P/R/S/W: 10 |
| year_range | 1970–2024 (from filename parse, n=7,668; modal years 2000–2003) |
| top_year_buckets | 2002: 796, 2003: 754, 2001: 738, 2000: 721, 1998: 634, 1999: 565, 1997: 533, 1996: 509, 1995: 463 |
| filename_quality | degraded; base64-corrupted suffixes on ~54.7% of files (5,001 of 9,136 carry `_Q…_` or `_R…_` tokens); 100% of a 50-doc random sample yield a parseable `<letter><digits>` code after normalization |
| catalog_source | /mnt/ace/O&G-Standards/_catalog.json |
| ocr_text_root | /mnt/ace/O&G-Standards/_ocr_text |
| inventory_db | /mnt/ace/O&G-Standards/_inventory.db (sqlite) |
| raw_source_policy | link-only; do not copy raw bulk data into git/wiki raw folders |
| extract_priority | metadata-only (per #2536 deep-extraction queue) |
| ingest_loop | docs/sessions/2026-05-08-llm-wiki-completeness-loop.md (E13) |

## Committee letter histogram

Leading-committee letter parsed from each filename (handles `B 327 - 01`, `B_327_-_01`, `A370-02`, `F1738-08`, `ASTM_F519-08`, and parenthesized `(C1138)` patterns):

| Letter | Files | Notes |
|--------|-------|-------|
| F | 3,376 | Specific Products — fasteners, plastic pipe, surgical implants, geomembranes, security |
| C | 2,818 | Cement, Concrete, Aggregates, Refractories, Lime, Gypsum |
| B | 1,708 | Non-Ferrous Metals — copper, aluminum, brass, bronze, magnesium, zinc, nickel |
| D | 685 | Petroleum, Plastics, Rubber, Soil & Rock, Water — overflow from D-Series |
| E | 521 | NDE, Materials Test Methods, Statistical Quality — overflow from E-Series |
| A | 18 | Steel, Stainless, Iron Castings — overflow from A-Series |
| P | 4 | (small / mis-prefix; verify against title) |
| R | 4 | (small / mis-prefix) |
| S | 1 | (single document) |
| W | 1 | (single document) |
| **Total** | **9,136** | 100% of files yield a leading-letter classification |

## Per-committee scope

### F-Series (Specific Products) — 3,376 files, 1,703 unique codes

ASTM Committee F covers a wide span of specific products: fasteners (F468, F467, F436, F1554, F606, F959, F1789, F1891, F3125), plastic piping systems (F876, F877, F1281, F1282, F1960, F1974, F2080), surgical implants & medical (F138, F75, F799), geomembranes & geosynthetics, footwear, security & home protection, and consumer products. Top by edition count in this bucket:

| Code | Files | Subject |
|------|-------|---------|
| F468 | 13 | Nonferrous Bolts, Hex Cap Screws, Socket Head Cap Screws & Studs (general purpose) |
| F467 | 12 | Nonferrous Nuts (general purpose) |
| F1789 | 10 | Standard Terminology for F16 (Mechanical Fasteners) |
| F876 | 10 | Crosslinked Polyethylene (PEX) Tubing |
| F1891 | 9 | Aluminized Para-Aramid Protective Clothing |
| F879 | 8 | Stainless Steel Socket Button & Flat Countersunk Head Cap Screws |
| F880 | 8 | Stainless Steel Socket Set Screws |
| F959 | 8 | Compressible-Washer-Type Direct Tension Indicators (for Use with Structural Fasteners) |
| F1281 | 7 | PEX-Aluminum-PEX Pressure Pipe |
| F1282 | 7 | Polyethylene/Aluminum/Polyethylene Composite Pressure Pipe |
| F1667 | 7 | Driven Fasteners: Nails, Spikes, Staples |
| F1960 | 7 | Cold Expansion Fittings with PEX Reinforcing Rings |
| F1974 | 7 | Metal Insert Fittings for PEX-AL-PEX & PE-AL-PE Pipe |
| F436 | 7 | Hardened Steel Washers (Inch and Metric Dimensions) |
| F606 | 7 | Mechanical Properties of Externally and Internally Threaded Fasteners |

### C-Series (Cement, Concrete & Aggregates) — 2,818 files, 1,207 unique codes

ASTM Committee C covers hydraulic cement (C150), concrete (C39, C31), aggregates (C33, C136), refractories (C113), lime, gypsum, masonry units (C90), thermal insulation (C578), and concrete pipe (C76, C443, C478, C497). Top by edition count:

| Code | Files | Subject |
|------|-------|---------|
| C990 | 12 | Joints in Concrete Pipe & Manholes Using Preformed Flexible Sealants |
| C1504 | 10 | Manufacture of Precast Reinforced Concrete Three-Sided Structures for Culverts & Storm Drains |
| C11 | 9 | Terminology Relating to Gypsum and Related Building Materials |
| C1433 | 9 | Precast Reinforced Concrete Box Sections for Culverts, Storm Drains & Sewers |
| C270 | 9 | Mortar for Unit Masonry |
| C1103 | 8 | Joint Acceptance Testing of Installed Precast Concrete Pipe |
| C443 | 8 | Joints for Concrete Pipe & Manholes Using Rubber Gaskets |
| C478 | 8 | Circular Precast Reinforced Concrete Manhole Sections |
| C497 | 8 | Test Methods for Concrete Pipe, Manhole Sections, or Tile |
| C578 | 8 | Rigid Cellular Polystyrene Thermal Insulation |
| C67 | 8 | Sampling & Testing Brick and Structural Clay Tile |
| C717 | 8 | Terminology of Building Seals and Sealants |
| C76 | 8 | Reinforced Concrete Culvert, Storm Drain & Sewer Pipe |
| C877 | 8 | External Sealing Bands for Concrete Pipe, Manholes & Precast Box Sections |
| C119 | 7 | Terminology Relating to Dimension Stone |

### B-Series (Non-Ferrous Metals) — 1,708 files, 695 unique codes

ASTM Committee B covers copper alloys (B16, B62, B584), aluminum alloys (B209, B210, B211, B221, B234, B247), brass and bronze castings, magnesium, nickel and nickel alloys (B163, B338), zinc, lead, and tin. The committee is the canonical reference for non-ferrous tube, sheet, plate, rod, bar, forging, and casting specifications used across O&G valve trim, heat exchangers, and pump components. Top by edition count:

| Code | Files | Subject |
|------|-------|---------|
| B209 | 12 | Aluminum & Aluminum-Alloy Sheet and Plate |
| B243 | 10 | Terminology of Powder Metallurgy |
| B211 | 8 | Aluminum & Aluminum-Alloy Rolled or Cold-Finished Bar, Rod, and Wire |
| B248 | 8 | General Requirements for Wrought Copper & Copper-Alloy Plate, Sheet, Strip, and Rolled Bar |
| B899 | 8 | Terminology Relating to Non-Ferrous Metals & Alloys |
| B108 | 7 | Aluminum-Alloy Permanent Mold Castings |
| B210 | 6 | Aluminum & Aluminum-Alloy Drawn Seamless Tubes |
| B221 | 6 | Aluminum & Aluminum-Alloy Extruded Bars, Rods, Wire, Profiles, and Tubes |
| B234 | 6 | Aluminum & Aluminum-Alloy Drawn Seamless Tubes for Condensers and Heat Exchangers |
| B247 | 6 | Aluminum-Alloy Die Forgings, Hand Forgings & Rolled Ring Forgings |
| B338 | 6 | Seamless & Welded Titanium & Titanium-Alloy Tubes for Condensers and Heat Exchangers |
| B557 | 6 | Tension Testing Wrought & Cast Aluminum & Magnesium-Alloy Products |
| B88 | 6 | Seamless Copper Water Tube |
| B135 | 5 | Seamless Brass Tube |
| B163 | 5 | Seamless Nickel & Nickel-Alloy Condenser & Heat-Exchanger Tubes |

### Other (D, E, A, and minor letters) — 1,229 files

- **D-Series stragglers (685 files, 685 unique codes):** Single-edition copies of D-Committee codes that escaped filing into `ASTM/D-Series/`. Spread across petroleum (D1015, D1016, D1091, D1217, D1218, D1250), plastics & rubber, soil & rock, and water. Each is a one-off — investigation should determine whether these are duplicates of D-Series entries or distinct revisions worth preserving.
- **E-Series stragglers (521 files, 520 unique codes):** Single-edition copies of E-Committee NDE & test-method codes. E186 has 2 copies; the rest are one-offs. Same investigation pattern as D.
- **A-Series stragglers (18 files):** A small set of A-Committee steel codes that escaped the A-Series sweep (A29, A193, A194, A240, A336, A370, A388, A487, A508, A541, A694, A703, A707, A751, A788, A962, F519-listed-as-A, plus the `ASTM-2004_full_index.pdf` library index).
- **P/R/S/W (10 files):** Likely OCR-corrupted leading characters or non-ASTM strays; verify against title before promoting.

## Bucket purity sample

Random sample of 50 files (seed=42) — code parseability after normalization:

| Outcome | Count | Fraction |
|---------|-------|----------|
| Parseable code (`<letter><digits>` extracted) | 50 | 100% |
| Fully unparseable filename | 0 | 0% |

After applying the multi-pattern extractor (`B 327 - 01 _Q…`, `B_327_-_01_Q…`, `A370-02`, `F1738-08`, `ASTM_F519-08`, `(C1138)`), every file in the 50-doc sample yields a code. **However**, 5,001 of 9,136 files (54.7%) still carry a base64-corrupted trailing token like `_QJMYNW_` or `_RJEWMA_` that is decorative — it carries no semantic value but inflates filename length and breaks naive substring matching. A filename-cleanup pass (see follow-ups) would strip these tokens.

## Verification

- Document count cross-check: catalog reports `statistics.by_organization.ASTM = 25,537`. Series sub-folders contain A=2,147 + D=10,379 + E=3,559 + G=316 = 16,401. Expected loose = 25,537 − 16,401 = **9,136**. Actual loose = **9,136**. Match exact.
- Filter rule: `relative_path.startswith('ASTM/') AND not any(s in relative_path for s in ['/A-Series/', '/D-Series/', '/E-Series/', '/G-Series/'])`.
- Total size derived from `file_size` field, summed across the 9,136 filtered records.
- Year range derived from filename parse (4-digit `19[7-9]\d|20[0-2]\d` and 2-digit `[\s_\-]\d{2}[\s_\-\.]` patterns); 7,668 of 9,136 files (84.0%) yielded a year token.
- Letter histogram derived from filename leading character after normalization; classification rate is 100%.
- DRM status: see `/mnt/ace/O&G-Standards/drm_protected_files.txt` for ASTM files flagged as DRM-protected.
- `_inventory.db` provides per-page OCR text for all PDFs (consume via SQLite, do not copy into wiki).

## Recommended follow-ups

1. **Filename-cleanup pass** — write a normalizer that (a) strips `_Q[A-Z0-9]+_` and `_R[A-Z0-9]+_` base64-ish suffixes, (b) collapses `B 327 - 01` ↔ `B_327_-_01` ↔ `B327-01` to a canonical `<letter><digits>-<2yr>` form, (c) emits the canonical code into a sidecar mapping for join against ASTM's published catalog. Block any per-code page promotion until normalized filenames are available.
2. **Sub-folder the residuals** — promote `B-Series/`, `C-Series/`, and `F-Series/` to first-class folders alongside the existing `A/D/E/G-Series/`. The B/C/F slices alone account for 7,902 of 9,136 files (86.5%); after that move, the residual `top-level loose` bucket drops to ~1,234 files (D/E/A stragglers + minor-letter strays) and becomes a true exception list.
3. **Reconcile D and E stragglers** — for the 685 D-codes and 521 E-codes here that have single-copy presence, check against `ASTM/D-Series/` and `ASTM/E-Series/` for duplicates. Likely outcome: many are revision-distinct copies that should be merged into the series folder; some are exact duplicates that should be deleted (with hash-equal verification via `_inventory.db`).
4. **Promote per-code pages for high-edition codes** — codes with 6+ revision/copy presence here are candidates for `wiki/standards/astm-<code-id>.md`:
   - **B-Series**: B16 / B62 / B584 (copper alloys & castings — O&G valve trim), B209 / B221 / B234 (aluminum sheet & extrusion), B338 (titanium heat-exchanger tube), B88 (copper water tube)
   - **C-Series**: C39 (concrete compressive strength), C150 (Portland cement), C76 (RC sewer pipe), C270 (masonry mortar), C578 (XPS thermal insulation)
   - **F-Series**: F436 (hardened steel washers), F1554 (anchor rods — structural & O&G foundations), F468 / F467 (non-ferrous fasteners), F876 (PEX tubing)
5. **Topical concept cross-links** — link this source into existing concepts/ for fasteners (F436, F1554, F468), concrete & cement (C39, C150), copper-alloy valve trim (B16, B62), aluminum heat-exchanger tube (B234), and titanium heat-exchanger tube (B338).
6. **Index update** — add this page to `wiki/index.md` under Sources, and append an ingest entry to `wiki/log.md` under `[2026-05-09] ingest | ASTM top-level loose catalog`.
