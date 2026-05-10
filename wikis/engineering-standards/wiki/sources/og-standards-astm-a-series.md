---
title: "O&G Standards catalog — ASTM A-Series (Iron & Steel)"
slug: og-standards-astm-a-series
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
sources:
  - /mnt/ace/O&G-Standards/ASTM/A-Series
ingested: 2026-05-09
tags:
  - og-standards-ingest
  - astm
  - a-series
  - standards
  - publisher-catalog
  - steel
  - structural-steel
  - plate
  - pipe-steel
  - fasteners
  - pressure-vessel
  - stainless-steel
  - duplex
  - reinforcing-bar
---

# O&G Standards catalog — ASTM A-Series (Iron & Steel)

> Metadata-first source page for the ASTM A-Series slice of the O&G-Standards consolidated library at `/mnt/ace/O&G-Standards/ASTM/A-Series/`. Generated 2026-05-09 from `/mnt/ace/O&G-Standards/_catalog.json` (catalog version 1.0.0, generated 2025-12-25).
> **Vendor PDFs do not enter this repo** per spinout 2026-05-05 governance — only publisher facts (titles, document IDs, revision years, file paths) are recorded here.

## Summary

ASTM International's **A-committee covers Iron and Steel Products** — the metallurgical substrate for pressure-vessel, offshore-structural, pipeline, drilling-equipment, and refinery fabrication across the petroleum industry. The A-Series defines material chemistry, mechanical properties, heat-treatment, qualification testing, and product-form requirements (plate, pipe, tube, bar, shape, fastener, casting, forging, reinforcing bar, sheet, strip) that ASME BPV Section II references by name and that API Spec 5L / 6A / 17D and DNV-OS-F101 / E301 invoke as upstream material specs. With **2,147 documents (~231.6 MB)** in this catalog spanning **publication years 1960–2008** across **~655 distinct A-numbers**, the A-Series slice is the single deepest publisher bucket by code count in the corpus — a multi-edition archive of the steels (A36, A106, A240, A370, A516, A572, A992, etc.) every offshore EPC procurement specification ultimately resolves to. The slice is metadata-only here; PDFs remain at `/mnt/ace/O&G-Standards/`.

## Metadata

| Field | Value |
|-------|-------|
| id | og-standards-astm-a-series |
| publisher | ASTM International (Committee A — Iron and Steel Products) |
| document_count | 2,147 |
| total_size_bytes | 242,864,300 |
| total_size_mb | 231.6 |
| extension_breakdown | .pdf: 2,147 (100%) |
| sub_category_breakdown (catalog `doc_type`) | A-Series: 41, E-Series: 11, D-Series: 1, uncoded: 2,094 |
| filename_letter_prefix | A: 1,956; D: 82; F: 36; E: 35; C: 21; B: 12; G: 3; other: 2 |
| unique_a_numbers_detected | ~655 distinct A-codes (filename heuristic, range A1–A1036) |
| publication_year_range (filename-derived) | 1960–2008 (modal years 2000–2003) |
| top_publication_years (filename) | 2003: 274, 2001: 251, 2000: 236, 2002: 220, 1998: 155, 2004: 145, 1995: 144, 1999: 128, 1996: 108, 1997: 99 |
| modified_date_range | 2002–2014 (top: 2008: 1,299; 2006: 800) |
| parent_root | /mnt/ace/O&G-Standards/ASTM/A-Series |
| catalog_source | /mnt/ace/O&G-Standards/_catalog.json |
| ocr_text_root | /mnt/ace/O&G-Standards/_ocr_text/ASTM (71 OCR text files for the entire ASTM bucket; ASTM/A-Series subdirectory not yet split out) |
| inventory_db | /mnt/ace/O&G-Standards/_inventory.db (6.8 GB sqlite, per-page text for all extracted PDFs) |
| drm_protected_count_for_astm_a_series | 0 (zero `ASTM/A-Series/` paths in `drm_protected_files.txt`) |
| raw_source_policy | link-only; do not copy raw bulk data into git/wiki raw folders |
| extract_priority | metadata-only (per #2536 deep-extraction queue) |
| ingest_loop | docs/sessions/2026-05-08-llm-wiki-completeness-loop.md (E13 iter-9) |
| bucket_purity_estimate | ~91.2% (1,957 of 2,147 filenames lead with `A`; 190 misfiled with B/C/D/E/F/G prefixes — see Verification) |

## Series breakdown

ASTM A-numbers are an unstructured registry — the number is assigned at first publication and does not encode subject. The table below groups the catalog by major A-code with subject, edition-coverage strength, and document count from the filename heuristic. Codes with `M` suffix (e.g., A 240/A 240M) are the metric companions issued under the same standard; counts include both customary and metric editions where present.

| Code | Subject | Editions / coverage | Sample doc count |
|------|---------|---------------------|------------------|
| **A6 / A6M** | General requirements for rolled structural steel bars, plates, shapes, and sheet piling | Multi-edition | 12 |
| **A20 / A20M** | General requirements for steel plates for pressure vessels | Multi-edition | 9 |
| **A36 / A36M** | Carbon structural steel (workhorse mild steel, Fy=36 ksi) | Multi-edition | 7 |
| **A53 / A53M** | Pipe, steel, black and hot-dipped, zinc-coated, welded and seamless | Multi-edition | 5 |
| **A105 / A105M** | Carbon steel forgings for piping applications | Multi-edition | 6 |
| **A106 / A106M** | Seamless carbon steel pipe for high-temperature service | Multi-edition | 5 |
| **A123 / A123M** | Zinc (hot-dip galvanized) coatings on iron and steel products | Multi-edition | 6 |
| **A153 / A153M** | Zinc coating (hot-dip) on iron and steel hardware | Multi-edition | 6 |
| **A179 / A179M** | Seamless cold-drawn low-carbon steel heat-exchanger and condenser tubes | Few editions | 2 |
| **A192 / A192M** | Seamless carbon steel boiler tubes for high-pressure service | Multi-edition | 4 |
| **A193 / A193M** | Alloy-steel and stainless steel bolting for high-temperature/pressure service | Multi-edition | 8 |
| **A194 / A194M** | Carbon and alloy steel nuts for high-pressure/high-temperature bolting | Multi-edition | 7 |
| **A210 / A210M** | Seamless medium-carbon steel boiler/superheater tubes | Multi-edition | 4 |
| **A213 / A213M** | Seamless ferritic/austenitic alloy-steel boiler/superheater/heat-exchanger tubes | Multi-edition | 8 |
| **A234 / A234M** | Piping fittings of wrought carbon and alloy steel for moderate-to-high-temp service | Multi-edition | 7 |
| **A240 / A240M** | Chromium and chromium-nickel stainless steel plate, sheet, strip for pressure vessels | Deep multi-edition | **12** |
| **A249 / A249M** | Welded austenitic steel boiler / superheater / heat-exchanger / condenser tubes | Multi-edition | 7 |
| **A269 / A269M** | Seamless and welded austenitic stainless steel tubing for general service | Multi-edition | 5 |
| **A276 / A276M** | Stainless steel bars and shapes | Multi-edition | 7 |
| **A285 / A285M** | Pressure vessel plates, carbon steel, low- and intermediate-tensile | Multi-edition | 5 |
| **A312 / A312M** | Seamless, welded, heavy cold-worked austenitic stainless steel pipes | Multi-edition | 8 |
| **A325 / A325M** | Structural bolts, steel, heat treated, 120/105 ksi minimum tensile (heavy-hex) | Multi-edition | 4 |
| **A333 / A333M** | Seamless and welded steel pipe for low-temperature service | Multi-edition | 4 |
| **A350 / A350M** | Carbon/low-alloy steel forgings, requiring notch toughness for piping | Multi-edition | 7 |
| **A370** | Mechanical testing of steel products (test method standard — referenced by every A-spec) | Multi-edition | 5 |
| **A376 / A376M** | Seamless austenitic steel pipe for high-temperature central-station service | Multi-edition | 6 |
| **A403 / A403M** | Wrought austenitic stainless steel piping fittings | Multi-edition | 6 |
| **A420 / A420M** | Piping fittings of wrought carbon/alloy steel for low-temperature service | Multi-edition | 7 |
| **A479 / A479M** | Stainless steel bars and shapes for use in boilers and other pressure vessels | Multi-edition | 6 |
| **A480 / A480M** | General requirements for flat-rolled stainless and heat-resisting steel plate/sheet/strip | Deep multi-edition | **12** |
| **A494 / A494M** | Castings, nickel and nickel alloy | Multi-edition | 7 |
| **A500 / A500M** | Cold-formed welded/seamless carbon steel structural tubing in rounds and shapes | Multi-edition | 8 |
| **A516 / A516M** | Pressure vessel plates, carbon steel, for moderate- and lower-temperature service | Multi-edition | 6 |
| **A529 / A529M** | High-strength carbon-manganese steel of structural quality | Multi-edition | 6 |
| **A564 / A564M** | Hot-rolled and cold-finished age-hardening stainless steel bars and shapes | Multi-edition | 6 |
| **A572 / A572M** | High-strength low-alloy columbium-vanadium structural steel (Gr 42/50/60/65) | Multi-edition | 8 |
| **A615 / A615M** | Deformed and plain carbon-steel bars for concrete reinforcement | Multi-edition | 9 |
| **A633 / A633M** | Normalized high-strength low-alloy structural steel plates | Few editions | 3 |
| **A653 / A653M** | Steel sheet, zinc-coated (galvanized) by the hot-dip process | Multi-edition | 8 |
| **A693** | Precipitation-hardening stainless and heat-resisting steel plate, sheet, strip | Multi-edition | 6 |
| **A703 / A703M** | Steel castings, common requirements for pressure-containing parts | Multi-edition | 8 |
| **A706 / A706M** | Low-alloy steel deformed and plain bars for concrete reinforcement | Multi-edition | 8 |
| **A707 / A707M** | Forged carbon and alloy steel flanges for low-temperature service | Few editions | 2 |
| **A709 / A709M** | Structural steel for bridges (umbrella spec; Gr 36/50/HPS-50W/70W/100W) | Multi-edition | 11 |
| **A781 / A781M** | General requirements for steel castings (common requirements) | Multi-edition | 9 |
| **A788 / A788M** | General requirements for steel castings (cross-cutting) | Multi-edition | 6 |
| **A789 / A789M** | Seamless/welded ferritic-austenitic (duplex) stainless steel tubing | Multi-edition | 6 |
| **A790 / A790M** | Seamless/welded ferritic-austenitic (duplex 2205, 2507) stainless steel pipe | Multi-edition | 7 |
| **A792 / A792M** | Steel sheet, 55% Al-Zn alloy-coated (Galvalume) by the hot-dip process | Multi-edition | 6 |
| **A815 / A815M** | Wrought ferritic, ferritic/austenitic, martensitic stainless steel piping fittings | Multi-edition | 6 |
| **A875 / A875M** | Steel sheet, zinc-5% aluminum alloy-coated by the hot-dip process | Multi-edition | 6 |
| **A923** | Detection of detrimental intermetallic phase in duplex/superduplex stainless (test method) | Multi-edition | 5 |
| **A934 / A934M** | Epoxy-coated prefabricated steel reinforcing bars | Multi-edition | 6 |
| **A941** | Standard terminology relating to steel, stainless steel, related alloys, and ferroalloys | Multi-edition | 6 |
| **A955 / A955M** | Deformed and plain stainless-steel bars for concrete reinforcement | Multi-edition | 8 |
| **A960 / A960M** | General requirements for forged steel pipe flanges, fittings, valves | Multi-edition | 7 |
| **A985 / A985M** | General requirements for steel castings, alloy, for pressure-containing parts | Multi-edition | 7 |
| **A992 / A992M** | Structural steel shapes (Fy=50 ksi — modern wide-flange building-steel default) | Multi-edition | 6 |
| **A996 / A996M** | Rail-steel and axle-steel deformed bars for concrete reinforcement | Multi-edition | 9 |
| **A1008 / A1008M** | Steel sheet, cold-rolled, carbon, structural / HSLA / HSLAS | Multi-edition | 8 |
| **A1011 / A1011M** | Steel sheet and strip, hot-rolled, carbon, structural / HSLA / HSLAS | Multi-edition | 8 |
| **A1018 / A1018M** | Steel sheet, hot-rolled, carbon, commercial / drawing / structural | Multi-edition | 6 |

> **Reading the editions column.** "Multi-edition" = ≥4 distinct catalog files for the code; "Deep multi-edition" = ≥10. The catalog has **24 A-codes with ≥8 documents**, **58 with ≥6**, and **164 with ≥4** — a long tail well-suited to per-code wiki pages. The full ~655-code inventory is preserved in `_catalog.json`; this table surfaces the codes most consequential for offshore / pressure-vessel / pipeline cross-reference.

## Verification

- **Document count.** `_catalog.json` `relative_path` filter `^ASTM/A-Series/` = **2,147** docs. All `.pdf` (no Office artefacts in this slice, in contrast to API).
- **Bucket purity sample (30 random docs).** 27 / 30 lead with `A<digit>` (real ASTM A-series numbering); 3 / 30 are ambiguous or wrong-letter (one stray `F 319`). Across the full slice, **189 / 2,147 (~8.8%) filenames lead with B/C/D/E/F/G** — clearly misfiled docs from sister ASTM committees (B = Nonferrous Metals, C = Cement/Concrete/Masonry, D = Miscellaneous Materials, E = General Methods/Instrumentation, F = Materials for Specific Applications, G = Corrosion). **Bucket purity estimate: ~91.2%**. A future ingest-hygiene action should move these 190 docs to their correct `ASTM/<letter>-Series/` directory before per-code page promotion.
- **Year range.** Filename-derived publication years span **1960–2008**, with the modal cluster in **2000–2003** (274 docs in 2003 alone — the peak ASTM A-spec republication wave). The catalog's `modified_date` peaks in 2008 (1,299 docs) and 2006 (800 docs), reflecting two bulk-rescan operations rather than publication waves.
- **OCR coverage.** `_ocr_text/ASTM/` contains **71 OCR text files** for the entire ASTM bucket (A + B + C + D + E + F + G series combined). An ASTM/A-Series subdirectory is **not yet split out**. Coverage on the A-Series slice is therefore **<3.3%** at the per-doc level; OCR for A-series PDFs is queued behind API in #2536. Per-page text for all extracted PDFs is available via `_inventory.db` (6.8 GB SQLite); never copy contents into the wiki repo.
- **DRM check.** `grep -c 'ASTM/A-Series' /mnt/ace/O&G-Standards/drm_protected_files.txt = 0`. Zero ASTM A-Series PDFs are flagged DRM-protected — consistent with ASTM's encryption-free distribution policy and matching the API slice (also zero DRM).
- **Catalog `doc_type` gap.** Only 41 of 2,147 docs (~1.9%) carry `doc_type=A-Series`; 2,094 have no `doc_type` in the catalog, and 53 are mis-typed as `E-Series` / `D-Series`. The `doc_type` field is not the source of truth for this slice — filename parsing is.

## Recommended follow-ups

Top promotion candidates for `wiki/standards/<code-id>.md` pages, ranked by (multi-edition coverage in this catalog) × (downstream cross-reference frequency from API/ASME/DNV pages already in the wiki). All ten codes have ≥6 catalog editions and are first-class normative anchors:

1. **astm-a370** — Mechanical testing of steel products. Referenced by *every* other A-spec and by API Spec 5L, 6A, ASME BPV Section II Part A. The single highest cross-reference fan-in in the A-series. Multi-edition (5 docs).
2. **astm-a106** — Seamless carbon steel pipe for high-temperature service. Anchored from API Spec 5L (line pipe distinction), ASME B31.3 (process piping), and offshore-topsides piping specs. Multi-edition (5 docs).
3. **astm-a240** — Stainless steel plate/sheet/strip for pressure vessels. Anchored from ASME BPV Section VIII Div 1/2, API Spec 6A (PSL-3/4 trim), and DNV-OS-C101. **Deepest A-Series coverage in catalog (12 docs)**.
4. **astm-a516** — Carbon-steel pressure-vessel plate for moderate/lower-temperature service. The default plate spec for low-temperature offshore vessels and storage tanks (cited by API Std 650). Multi-edition (6 docs).
5. **astm-a572** — HSLA columbium-vanadium structural steel (Gr 50/60/65). Workhorse of jacket and topsides primary structure; anchored from API RP 2A-WSD, AISC 360. Multi-edition (8 docs).
6. **astm-a790** — Duplex/superduplex stainless steel pipe (2205, 2507). Anchored from DNV-RP-F112, NORSOK M-630, NACE MR0175 / ISO 15156 sour-service work. Multi-edition (7 docs).
7. **astm-a923** — Detection of detrimental intermetallic phase in duplex/superduplex stainless (test method). The qualification method invoked by every duplex procurement spec. Multi-edition (5 docs).
8. **astm-a193** — Alloy/stainless bolting for high-temperature/pressure service (B7, B8, B16, etc.). Anchored from API Spec 6A flange-stud requirements and ASME B16.5 / B16.34. Multi-edition (8 docs).
9. **astm-a36** — Carbon structural steel (Fy=36 ksi). The baseline mild-steel reference; anchored from AISC 360 and almost every offshore-jacket secondary-structure spec. Multi-edition (7 docs).
10. **astm-a992** — Structural steel shapes (Fy=50 ksi). The modern default for wide-flange building / topsides-deck steel; anchored from AISC 360 (W-shape default). Multi-edition (6 docs).

**Concept-page cross-links to add or update**:
- **plate metallurgy** (cross-link A6, A20, A240, A285, A480, A516) — the umbrella concept for pressure-vessel and hull-plate specification.
- **pipe-steel metallurgy** (cross-link A53, A106, A312, A333, A376, A789, A790) — pipe-form A-codes by service-temperature regime.
- **fastener metallurgy** (cross-link A193, A194, A325, A490) — high-strength bolting for flanged joints and structural connections.
- **stainless steel — duplex** (cross-link A789, A790, A815, A923, A928) — duplex-family qualification path.
- **reinforcing bar metallurgy** (cross-link A615, A706, A934, A955, A996) — concrete-reinforcement steel specs.
- **steel terminology** (cross-link A941) — controlled vocabulary used across the A-series.

**Catalog-hygiene actions** (out-of-scope for this page; for the ingest-loop owner): (a) move the **190 mis-filed B/C/D/E/F/G-series PDFs** out of `ASTM/A-Series/` into their correct sibling directories; (b) populate `doc_type` for the 2,094 uncoded entries via filename parsing (the regex `^A[\s_-]?\d{1,4}M?` recovers ~91% on a single pass); (c) split the ASTM OCR bucket by sub-committee letter so A-Series OCR coverage can be tracked independently.

## Cross-references

Standards pages already promoted from this A-Series slice (each should cite this source page for catalog provenance):

- [`standards/astm-a370`](../standards/astm-a370.md) — Mechanical testing of steel products; the highest cross-reference fan-in in the A-Series.
- [`standards/astm-a335`](../standards/astm-a335.md) — Seamless ferritic alloy-steel pipe for high-temperature service.
- [`standards/astm-a553`](../standards/astm-a553.md) — Pressure-vessel plates, alloy-steel, quenched and tempered, 8% / 9% nickel for low-temperature service.

Concept pages that should cite this source when invoking A-Series-published material specs:

- [`concepts/sour-service-materials`](../concepts/sour-service-materials.md) — A-Series duplex (A790, A815, A923) and bolting (A193) specs are the procurement anchors for NACE MR0175 / ISO 15156 qualification.
- [`concepts/welding-procedures-and-acceptance`](../concepts/welding-procedures-and-acceptance.md) — A370 mechanical testing underpins ASME BPVC IX welder-qualification mechanical-test acceptance.
- [`concepts/fracture-toughness-measurement`](../concepts/fracture-toughness-measurement.md) — A370 Charpy + A553 8/9 Ni-steel feed low-temperature pressure-vessel toughness.
- [`concepts/hydrogen-embrittlement`](../concepts/hydrogen-embrittlement.md) — A193 high-strength bolting and A540 quench-and-temper materials are HE-susceptible specs.
- [`concepts/atmospheric-corrosion`](../concepts/atmospheric-corrosion.md) — A123 / A153 / A653 / A792 / A875 zinc and Galvalume coatings for atmospheric-exposure protection.
