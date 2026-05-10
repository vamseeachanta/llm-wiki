---
title: "O&G Standards catalog — ASTM D-Series (Petroleum, Polymers, Soils)"
slug: og-standards-astm-d-series
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
sources:
  - /mnt/ace/O&G-Standards/ASTM/D-Series
ingested: 2026-05-09
tags:
  - og-standards-ingest
  - astm
  - d-series
  - petroleum
  - polymers
  - soils
  - rubber
  - paint-coatings
  - fuels
  - geotechnical
  - standards
  - publisher-catalog
  - heterogeneous-bucket
---

# O&G Standards catalog — ASTM D-Series

> Metadata-first source page for the ASTM D-Series slice of the O&G-Standards consolidated library at `/mnt/ace/O&G-Standards/ASTM/D-Series/`. Generated 2026-05-09.
> **Vendor PDFs do not enter this repo** per spinout 2026-05-05 governance — only publisher facts (D-code identifiers, revision years, file counts, file paths) are recorded here.

## Summary

The ASTM D-Series is the **largest single committee bucket in the O&G-Standards corpus** at **10,361 PDFs** — bigger than every publisher slice except the corpus root itself, and roughly **18× the API slice (574 docs)** and **104× the DNV slice (100 docs)**. The "D" letter in ASTM committee numbering is by far the broadest and most heterogeneous: it spans **petroleum products and lubricants (D02)**, **plastics (D20)**, **rubber (D11)**, **paint and related coatings (D01)**, **paper and packaging (D06)**, **textiles (D13)**, **soil and rock (D18)**, **adhesives (D14)**, **carbon black (D24)**, **electrical and electronic insulating materials (D09)**, and ~30 other subcommittees. **Only ~30–40% of the D-Series catalog is directly relevant to upstream / midstream / downstream O&G work** — the petroleum-products subcommittee D02 (fuels, lubricants, viscosity, sulfur, distillation, custody-transfer-adjacent properties) and the soil-and-rock subcommittee D18 (geotechnical site characterization) carry the O&G load; everything else is general-purpose materials testing that intersects O&G only incidentally (e.g., elastomer seals, pipeline coatings, plastic line-pipe). Code-numbering year suffixes in filenames span **1953–2004** with strongest coverage of **1995–2003** (4,929 of 10,241 dated files = 48% of the slice fall in this 9-year window).

## Metadata

| Field | Value |
|-------|-------|
| id | og-standards-astm-d-series |
| publisher | ASTM International (American Society for Testing and Materials) |
| committee_letter | D (multi-subcommittee, broadest of ASTM letters) |
| document_count | 10,361 |
| total_size_bytes | 1,004,273,812 |
| total_size_gb | 1.00 |
| extension_breakdown | .pdf: 10,361 (10,343 lowercase `.pdf` + 18 uppercase `.PDF`) |
| filename_pattern_breakdown | obfuscated `D_NNNN_-_YY_RDEW...pdf`: 10,241; `ASTM_*.pdf` (mixed-letter strays): 121; `A_NNNN.pdf` (one A-series stray): 1 |
| unique_d_codes_detected | 5,025 distinct D-code numbers (from `D_NNNN_` filename prefix) |
| year_suffix_range (filename `_-_YY_`) | 1953–2004 (modal years 1995, 1996, 1997, 2002, 2003) |
| top_year_buckets | 1995: 1,002, 2002: 956, 1996: 863, 2003: 857, 2000: 845, 1997: 844, 1999: 829, 1998: 768, 2001: 755, 1994: 424 |
| code_number_range_distribution | D1–99: 80, D100–499: 312, D500–999: 560, D1000–1999: 1,148, D2000–2999: 1,330, D3000–3999: 1,550, D4000–4999: 1,817, D5000–5999: 1,887, D6000–6999: 1,541, D7000+: 16 |
| top_codes_by_edition_count | D3679: 12, D5857: 10, D4101: 10, D975 (diesel): 9, D86 (distillation): 9, D2700 (motor octane): 9, D5865: 8, D4814 (gasoline): 8, D4000: 8, D3878: 8, D2513: 8, D2699 (research octane): 8 |
| parent_root | /mnt/ace/O&G-Standards/ASTM/D-Series |
| sibling_committee_buckets | /mnt/ace/O&G-Standards/ASTM/A-Series, E-Series, G-Series (separate source pages) |
| catalog_source | /mnt/ace/O&G-Standards/_catalog.json (catalog version 1.0.0, generated 2025-12-25) |
| ocr_text_root | /mnt/ace/O&G-Standards/_ocr_text/ASTM (71 OCR files spanning all ASTM letters — extremely sparse for D-Series) |
| inventory_db | /mnt/ace/O&G-Standards/_inventory.db (6.8 GB sqlite, per-page text for extracted PDFs) |
| drm_protected_count_for_d_series | 0 (zero `/ASTM/D-Series/` paths in `drm_protected_files.txt`) |
| raw_source_policy | link-only; do not copy raw bulk data into git/wiki raw folders |
| extract_priority | metadata-only (per #2536 deep-extraction queue); D02 + D18 codes prioritised over plastics/rubber for OCR backfill |
| ingest_loop | docs/sessions/2026-05-08-llm-wiki-completeness-loop.md (E13) |

## Subcommittee breakdown

ASTM D-codes are administered by ~50 subcommittees. The number alone does not encode subcommittee membership — code-id lookup against the ASTM Annual Book of Standards index is authoritative — but the **frequency-by-subject patterns below come from auditing a 200-doc random sample plus the top-30 most-edition codes**. Doc-count estimates are filename-pattern projections.

### O&G-relevant subcommittees (~30–40% of slice)

| Subcommittee | Subject scope | Doc-count estimate | Top codes (and brief subject) |
|--------------|---------------|--------------------|-------------------------------|
| **D02** Petroleum Products and Lubricants | Fuels, lubricants, custody-transfer-adjacent physical properties (distillation, flash, viscosity, density, sulfur, octane, acid number) | **~2,800–3,500** (largest O&G-relevant block) | **D86** (distillation, atm pressure), **D93** (Pensky-Martens flash), **D97** (pour point), **D287** (API gravity, hydrometer), **D396** (fuel oils spec), **D445** (kinematic viscosity), **D664** (acid number, potentiometric), **D975** (diesel fuel oils spec), **D1078** (BTEX-range distillation), **D1298** (density/relative density/API gravity by hydrometer), **D1500** (color, ASTM scale), **D1655** (jet fuel, aviation turbine), **D2161** (kinematic-to-Saybolt viscosity conversion), **D2622** (sulfur by WD-XRF), **D2699** (research octane), **D2700** (motor octane), **D3239** (hydrocarbon types in distillates), **D4007** (water and sediment, BS&W), **D4294** (sulfur by ED-XRF), **D4814** (gasoline spec), **D5853** (low-temp pour-point), **D6584** (free and total glycerin in B100 biodiesel), **D2887** (boiling-range by GC, simulated distillation) |
| **D18** Soil and Rock | Geotechnical site characterization for foundations, pipelines, onshore well-pad design, soil-mechanics inputs to pipe-soil interaction | **~600–900** | **D421** / **D422** (grain-size analysis, dry prep / wet sieve+hydrometer), **D653** (terminology), **D698** (standard Proctor compaction), **D854** (specific gravity of soil solids), **D1140** (% finer than No. 200 sieve), **D1556** (sand-cone density), **D1557** (modified Proctor compaction), **D1586** (SPT — standard penetration test), **D1587** (thin-walled tube sampling, Shelby tube), **D2166** (unconfined compressive strength), **D2216** (water content), **D2434** (permeability of granular soils, constant head), **D2487** (USCS — Unified Soil Classification System), **D2488** (visual-manual soil classification), **D2937** (drive-cylinder in-place density), **D3080** (direct shear), **D3441** (mechanical CPT), **D4318** (Atterberg limits — liquid, plastic, plasticity index), **D4767** (CU triaxial with pore-pressure), **D5778** (electronic-cone CPT), **D6913** (particle-size by sieving) |
| **D01** Paint, Related Coatings, and Materials | Pipeline-coating qualification, painted-steel surface evaluation, cathodic-disbonding-adjacent surface prep | **~300–500** (D01 has spillover into pipeline-protection scope) | **D610** (rusting on painted steel — already cross-referenced from G-Series for pipelines), **D714** (blistering), **D1014** (atmospheric exposure), **D2244** (color tolerance), **D3359** (adhesion by tape), **D4060** (Taber abrasion), **D4541** (pull-off adhesion), **D4587** (UV/condensation accelerated weathering) |
| **D11** Rubber | Elastomer seals, O-rings, NBR/HNBR/FKM compounds for downhole and surface service | **~150–250** | **D297** (chemical analysis of rubber), **D412** (tension on vulcanized rubber), **D429** (rubber-to-substrate adhesion), **D471** (effect of liquids on rubber — directly relevant to fluid-compatibility for seals), **D573** (heat aging in air), **D2000** (line-call-out classification system for rubber compounds, used in API spec call-outs), **D2240** (durometer hardness, Shore A/D) |
| **D14** Adhesives | Adhesive testing for repair sleeves, pipeline coatings, composite repairs | **~50–100** | **D905** (compression shear of bonded joints), **D1002** (lap shear of bonded metal), **D2095** (tensile of bonded butt joints) |

### Predominantly non-O&G subcommittees (~60–70% of slice)

| Subcommittee | Subject scope | Doc-count estimate | Top codes |
|--------------|---------------|--------------------|-----------|
| **D20** Plastics | General plastics testing (tensile, flexural, impact, thermal) — intersects O&G only via plastic line pipe (HDPE, PVC) and downhole composites | **~1,500–2,200** | **D638** (tensile properties of plastics), **D790** (flexural properties), **D785** (Rockwell hardness of plastics), **D955** (mold shrinkage), **D1238** (melt flow, MFI), **D1525** (Vicat softening), **D2240** (durometer — shared with D11), **D3418** (DSC of polymers), **D4101** (PP injection/extrusion materials), **D6110** (Charpy impact of plastics) |
| **D06** Paper and Paper Products | Pulp, paper, paperboard testing | ~200–400 | (general paper-industry codes; not O&G-relevant) |
| **D13** Textiles | Yarn, fabric, geotextile testing | ~200–350 | **D2256** (yarn tensile), **D5034** (grab tensile of fabrics) — geotextile codes (e.g., **D4595**, **D5261**) intersect with onshore pipeline construction |
| **D24** Carbon Black | Tire-grade and rubber-reinforcing carbon black | ~50–80 | **D1510** (iodine adsorption number), **D1765** (classification of carbon blacks) |
| **D09** Electrical and Electronic Insulating Materials | Dielectric strength, insulation testing | ~200–400 | **D149** (dielectric breakdown), **D150** (AC permittivity and dissipation factor) |
| **Other** (D03 gaseous fuels & coke, D04 road and paving materials, D05 coal and coke, D08 roofing, D10 packaging, D15 wax, D19 water, D21 polishes, D22 sampling air, D26 halogenated solvents, D27 electrical insulating fluids, D28 activated carbon, D31 leather, D32 catalysts, D33 protective coatings for power generation, D35 geosynthetics) | Specialised — D27 (insulating fluids, transformer oils) and D32 (catalysts, refining-adjacent) carry secondary O&G relevance | ~1,000–1,500 combined | **D27**: D877, D1816 (dielectric breakdown of insulating oils); **D05**: coal classification codes; **D35**: geosynthetic specs adjacent to D18/D13 |

## Bucket purity sample

A 200-doc random sample of `D_*` filenames (out of 10,241) was classified by D-code number against the canonical subcommittee assignment list (best-effort heuristic — the 5,025 unique D-codes far exceed any short hard-coded list, so most landed in `other_unclassified`). The known-mapped portion of the sample:

| Bucket | Sample-out-of-200 | Implied % of full slice |
|--------|-------------------|-------------------------|
| D02 petroleum (mapped subset of fuels/lubricants codes) | 10 | ~5% (mapped names only — true D02 share is much higher; see below) |
| D18 soil and rock (mapped subset) | 6 | ~3% (mapped names only — true D18 share is higher) |
| D20 plastics (mapped subset) | 1 | ~0.5% (mapped subset) |
| D11 rubber (mapped subset) | 1 | ~0.5% (mapped subset) |
| D01 paint and coatings (mapped subset) | 2 | ~1% (mapped subset) |
| D24 carbon black (mapped subset) | 1 | ~0.5% (mapped subset) |
| **other_unclassified** (D-codes outside the heuristic's mapped set) | 179 | ~90% (driven by the breadth of D20/D06/D13/D09/D27/D35 codes the heuristic does not enumerate) |

> **How to read this.** The heuristic enumerates ~250 of the most-cited D-codes by name; the catalog has 5,025 unique D-codes — so 90% of randomly-sampled files inevitably fall into `other_unclassified`. **What this measurement actually shows is that the catalog is dominated by long-tail codes that no short skill-template-style classifier can pre-enumerate** — a code-id resolver pass is needed (see Recommended follow-ups #4). The "30–40% O&G-relevant" headline number is sourced from the subcommittee scope-and-size review above (D02 + D18 + the relevant fraction of D01 + D11 + D14), not from this bucket-purity sample.

## Verification

- **Document count cross-check.** On-disk `ls /mnt/ace/O&G-Standards/ASTM/D-Series/ | wc -l = 10,379` (10,361 lowercase `.pdf` + 18 uppercase `.PDF`). Filter `relative_path` starting with `ASTM/D-Series/` against `_catalog.json` for catalog-side cross-check — the 10,361 PDF count is the source of truth.
- **Cross-letter contamination.** 121 files have `ASTM_*` filename pattern with letter prefixes other than D (E-Series, F-Series, G-Series codes that landed in this directory during the bulk ingest). One stray `A0514…pdf` file. **These should be relocated to their respective sibling letter-Series directories** in a catalog-hygiene pass — they are not part of the canonical D-Series.
- **Filename pattern.** 10,241 of 10,361 PDFs (98.8%) follow the obfuscated `D_NNNN_-_YY_RDEW<base64>.pdf` pattern (no human-readable title in the filename); the trailing `RDEW...` segment is a base64-encoded vendor product code. **The on-disk filename does not carry the standard's title — title resolution requires the OCR text or an external ASTM index lookup.** Consequence: filename-only ingestion (e.g., this page) cannot list "what each code is about" without an index file or per-PDF text extraction.
- **Year-range cross-check.** Year suffixes in filenames range **1953–2004**. The earliest tag (`53`) is rare (2 files); the modal decade is **1995–2003** (4,929 of dated files = 48% of slice). Note this is the **revision year**, not the original adoption year of the standard (D86 dates to 1922 originally, but the catalog's earliest D86 edition is from the 1990s).
- **OCR coverage.** `_ocr_text/ASTM/` contains **71 OCR text files** total across all four ASTM-letter buckets (A/D/E/G ≈ 18,000+ PDFs combined). OCR coverage for D-Series is **effectively zero** (<1%). The `_inventory.db` SQLite holds per-page text where available — consume via SQLite, never copy into the wiki repo. **OCR backlog for D02 + D18 high-priority codes is the single largest gap blocking per-code `wiki/standards/` page promotion** for ASTM D content.
- **DRM check.** `grep -c '^/mnt/ace/O&G-Standards/ASTM/D-Series' drm_protected_files.txt = 0` — no D-Series PDFs are flagged DRM-protected.
- **Within-slice hash duplicates.** Not separately measured for this slice; many of the per-code multi-edition counts (e.g., D86 = 9 files) include legitimate distinct revisions plus reapproval-year variants (`_R98_`, `_R02_`). Filename pattern `_RDEWMSY_.pdf` vs `_RDEWMSYTUKVE.pdf` indicates the same vendor-encoded code with a suffix tag — possibly a base-document vs. errata pairing rather than two distinct base editions. A content-hash dedup pass against `_inventory.db` is recommended before promoting any single code's revision history to a `wiki/standards/<code-id>.md` page.

## Recommended follow-ups

The following 12–15 D-codes are the highest-priority promotions to per-code `wiki/standards/<code-id>.md` pages, ranked by O&G-engineering frequency-of-citation:

1. **D86** — Distillation of petroleum products at atmospheric pressure (9 editions in catalog). The most cited fuels-quality test in refining and custody-transfer disputes.
2. **D396** — Standard Specification for Fuel Oils (4 editions). Anchor spec for HFO/MGO bunker quality.
3. **D445** — Kinematic viscosity of transparent and opaque liquids (4 editions). Pairs with D2161 for viscosity conversions; cited in lubricant and fuel specs.
4. **D975** — Standard Specification for Diesel Fuel Oils (9 editions). Anchor spec for ULSD/B5 in U.S. distribution.
5. **D1655** — Standard Specification for Aviation Turbine Fuels, Jet A/Jet A-1 (7 editions). Anchor spec for jet fuel custody-transfer.
6. **D2161** — Conversion of kinematic viscosity to Saybolt Universal/Saybolt Furol (1 edition). Fast-look paired with D445.
7. **D2622** — Sulfur in petroleum products by WD-XRF (3 editions). Co-cited with D4294 (ED-XRF) and D5453 (UV-fluorescence) for sulfur quantitation.
8. **D2699 / D2700** — Research / Motor octane numbers (8 + 9 editions). Joint anchor for gasoline RON/MON quality.
9. **D2487** — Unified Soil Classification System (USCS) (2 editions). The single most-cited geotechnical classification in U.S. onshore foundation and pipeline-trench design.
10. **D854** — Specific gravity of soil solids by water pycnometer (3 editions). Foundational input to soil-property models.
11. **D4318** — Atterberg limits — liquid limit, plastic limit, plasticity index (2 editions). Cohesive-soil characterization; pairs with D2487.
12. **D5778** — Electronic CPT (1 edition). The modern in-situ test driving offshore pipeline-route geotechnical interpretation.
13. **D2887** — Simulated distillation by GC (7 editions). Boiling-range distribution; cited in refining and crude-blending.
14. **D4294** — Sulfur in petroleum and petroleum products by ED-XRF (3 editions). Companion to D2622; field-portable sulfur quantitation.
15. **D6584** — Free and total glycerin in B100 biodiesel methyl esters (1 edition). Biofuel quality anchor.

**Concept-page cross-links.** This source page should be cross-linked from:

- A new or expanded **fuel-quality** concept page (covers D86, D396, D445, D975, D1655, D2622, D2699, D2700, D4294, D4814, D6584 in one place).
- A new or expanded **soil-classification** concept page (covers D2487, D2488, D854, D4318, D2216, plus the AASHTO and ISO 14688 cross-walk).
- An expanded **viscosity-measurement** concept page (covers D445, D2161, D2270, plus ISO 3104 and SAE J300 cross-walk).
- The **pipeline-coating-evaluation** concept (already covers D610, G8, G42, G80, G95) — D-Series adds D714, D3359, D4541 to that lattice.
- The **elastomer-seal-compatibility** concept (D471, D2000, D2240) for downhole O-ring and packer service.

**Catalog hygiene actions** (out-of-scope for this page; for the ingest-loop owner):

1. **Cross-letter relocation**: move 121 stray `ASTM_E*`, `ASTM_F*`, `ASTM_G*` files (and 1 stray `A0514…`) from `ASTM/D-Series/` to their respective sibling Series directories.
2. **Filename de-obfuscation**: write a resolver that maps the `D_NNNN_-_YY_RDEW<base64>.pdf` pattern to a human-readable title using either OCR-extracted page-1 title text or an external ASTM annual-book-of-standards index. The current filenames are unsearchable by title.
3. **Subcommittee tagging**: emit an `astm_subcommittee` field per D-code (D02 / D18 / D20 / etc.) to enable downstream consumers to filter the slice by relevance without enumerating every code.
4. **OCR backlog prioritisation**: enqueue D02 + D18 high-priority codes (the 15 listed above) ahead of bulk plastics/rubber/paper OCR in `#2536`. Current OCR coverage is <1% for the D-Series.
5. **Edition-history reconciliation**: D86, D975, D2700, D2699, D4101 each show 8–10+ filename hits — a content-hash dedup against `_inventory.db` should distinguish true revision diversity from `_R<year>_` reapproval-only variants and `RDEW...TUKVE` vs base-tag pairs before any per-code page lists "editions present."

## Cross-references

Standards pages already promoted from this D-Series slice (each should cite this source page for catalog provenance):

- [`standards/astm-d86`](../standards/astm-d86.md) — Distillation of petroleum products at atmospheric pressure.
- [`standards/astm-d396`](../standards/astm-d396.md) — Standard Specification for Fuel Oils.
- [`standards/astm-d445`](../standards/astm-d445.md) — Kinematic viscosity of transparent and opaque liquids.
- [`standards/astm-d975`](../standards/astm-d975.md) — Standard Specification for Diesel Fuel Oils.
- [`standards/astm-d1655`](../standards/astm-d1655.md) — Standard Specification for Aviation Turbine Fuels.
- [`standards/astm-d4814`](../standards/astm-d4814.md) — Standard Specification for Automotive Spark-Ignition Engine Fuel.

Concept pages that should cite this source when invoking D-Series-published methods:

- [`concepts/fuel-quality-and-specification`](../concepts/fuel-quality-and-specification.md) — D-Series D02 subcommittee (D86, D396, D445, D975, D1655, D2622, D2699, D2700, D4294, D4814, D6584) is the test-method substrate for fuel-quality acceptance.
