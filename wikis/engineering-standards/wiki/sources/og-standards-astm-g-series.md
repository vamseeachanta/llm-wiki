---
title: "O&G Standards catalog — ASTM G-Series (Corrosion)"
slug: og-standards-astm-g-series
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
sources:
  - /mnt/ace/O&G-Standards/ASTM/G-Series
ingested: 2026-05-09
tags: ["astm", "g-series", "corrosion", "cathodic-protection", "sour-service", "electrochemistry"]
---

# O&G Standards catalog — ASTM G-Series (Corrosion)

> Metadata-first source page for the ASTM G-Series slice of the O&G-Standards consolidated library at `/mnt/ace/O&G-Standards/ASTM/G-Series/`. Generated 2026-05-09 from `/mnt/ace/O&G-Standards/_catalog.json` (filtered on `relative_path` prefix `ASTM/G-Series/`).
> **Vendor PDFs do not enter this repo** per spinout 2026-05-05 governance — only publisher facts (titles, document IDs, revision years, file paths) are recorded here.

## Summary

The ASTM G-committee (G01) writes the metals-corrosion test-method substrate that every offshore corrosion calculation ultimately rests on — weight-loss coupons, electrochemical polarization, stress-corrosion cracking, atmospheric exposure, pitting/crevice ranking, galvanic series, and cathodic-protection disbondment. G-series methods are heavily cross-referenced from DNV-RP-B401 (cathodic-protection design), NACE MR0175/ISO 15156 (sour service), API 510/570/653 (in-service inspection), and AMPP (NACE) TM0177 (sulfide-stress-cracking laboratory testing), making this slice the highest cross-traffic node in the offshore corrosion stack.

## Metadata

| Field | Value |
|-------|-------|
| id | og-standards-astm-g-series |
| publisher | ASTM International (Committee G01 — Corrosion of Metals) |
| document_count | 316 |
| document_count_in_scope | 307 (excludes 9 non-G-series files mis-shelved into the directory — see Bucket purity sample) |
| total_size_bytes | 32,790,523 |
| total_size_mb | 31.3 |
| extension_breakdown | .pdf: 316 |
| unique_g_codes_present | 165 (range G1–G179 with gaps) |
| year_range | 1972–2004 (based on filename revision-year tokens) |
| top_year_buckets | 1996: 38, 1995: 33, 1998: 30, 2000: 28, 2003: 24, 1997: 24, 2002: 18, 1999: 18, 2001: 17, 1988: 12 |
| parent_root | /mnt/ace/O&G-Standards/ASTM/G-Series |
| catalog_source | /mnt/ace/O&G-Standards/_catalog.json |
| ocr_text_root | /mnt/ace/O&G-Standards/_ocr_text |
| inventory_db | /mnt/ace/O&G-Standards/_inventory.db (6.8 GB sqlite) |
| raw_source_policy | link-only; do not copy raw bulk data into git/wiki raw folders |
| extract_priority | metadata-only (per #2536 deep-extraction queue) |
| ingest_loop | docs/sessions/2026-05-08-llm-wiki-completeness-loop.md (E13) |

## Topical coverage map

G-codes referenced by document number, with edition multiplicity in this catalog. Real document IDs were sampled from filenames; multiple revisions exist for several methods (e.g., G15 with 5 dated revisions, G48 with 4, G85 with 4).

| Subject area | G-codes present | Editions in catalog | Offshore relevance |
|--------------|-----------------|---------------------|--------------------|
| Weight-loss / mass-loss methods | G1, G31 | G1 ×3, G31 ×2 | Coupon-based corrosion-rate measurement; baseline for sour-service mass-loss tests |
| Electrochemical methods | G3, G5, G15, G59, G61, G102, G105, G106 | G3 ×1, G5 ×1, G15 ×5, G59 ×2, G61 ×2, G102 ×1, G105 ×3, G106 ×1 | Polarization, Tafel-slope extraction, EIS, localized-corrosion (G61) — feeds CP design |
| Stress-corrosion cracking (SCC) | G36, G38, G39, G44, G47, G64 | G36 ×1, G38 ×3, G39 ×1, G44 ×1, G47 ×2, G64 ×1 | Boiling MgCl2 (G36), C-ring (G38), bent-beam (G39), alternate immersion (G44), Al-alloy SCC (G47, G64) |
| Atmospheric / outdoor exposure | G50, G84, G85 | G50 ×2, G84 ×1, G85 ×4 | Topside structural-steel exposure characterization; salt-fog/cyclic test design (G85) |
| Cathodic protection | G8, G42, G95 | G8 ×1, G42 ×1, G95 (catalog-present) | G8 disbondment of pipeline coatings, G42 SCC under cathodic polarization — direct DNV-RP-B401 inputs |
| Sour-service / mass-loss in aggressive media | G1, G31 | (see weight-loss row) | Used jointly with NACE MR0175 / AMPP TM0177 for laboratory mass-loss in H2S environments |
| Pitting / crevice corrosion | G46, G48, G78 | G46 ×1, G48 ×4, G78 ×3 | G46 pit-rating, G48 ferric-chloride pitting/crevice resistance (the canonical CRA screening test), G78 crevice in seawater |
| Galvanic / dissimilar metals | G71, G82 | G71 ×2, G82 ×2 | Galvanic-series ranking and laboratory galvanic corrosion measurement — subsea dissimilar-metal interfaces |
| General methodology / terminology / statistics | G15, G16, G102 | G15 ×5 (terminology), G16 ×2 (statistical analysis), G102 ×1 (corrosion-rate calc from electrochemical data) | Definitional substrate cited across all corrosion calc-modules |

> Cross-reference sinks: cathodic-protection methods anchor [DNV-RP-B401](og-standards-dnv.md) sacrificial-anode design; SCC methods (G36/G38/G39/G44) are referenced from NACE MR0175 / ISO 15156 sour-service qualification; pitting/crevice methods (G48/G78) underpin CRA selection in subsea production.

## Bucket purity sample

High purity. Of 316 files in the directory:
- **307 in scope** — files matching `(?:ASTM_)?G\d+` filename pattern, all corrosion-of-metals methods.
- **9 out of scope** — concrete-test C-codes mis-shelved (e.g., `Aggregates_for_Radiation-Shielding_Concrete1_(C637).PDF`, `Bleeding_of_Conc.(C232).PDF`, `Capping_of_Cylindrical_Specimens_(C617).PDF`, `Conc_Making_(C685).PDF`, `Constituents_of_Aggregates_for_Radiation-Shielding_(C638).PDF`, `Freezing_&_Thawing_(C666).PDF`, `Making_&_Curing_Conc._Tests_(C31C31M).PDF`, `Making_&_Curing_Conc._in_Lab_(C192C192).PDF`) and one ship-stability F-code (`Inclining_Experiment_F1321.epyr8463.pdf`).
- **Purity ratio** ≈ 97.2% (307 / 316). The 9 strays should be reshelved to ASTM/C-Series/ and ASTM/F-Series/ respectively in a future inventory pass.

## Verification

- **Document count cross-check**: 316 catalog entries matched the directory `ls | wc -l = 316` exactly. The brief-stated 308 figure is superseded by the live catalog count.
- **Year range**: 1972–2004 from filename revision tokens (matched 306 of 316 files via regex `G\s*\d+[_-]\s*(\d{2})` with century pivot at 30: `00-30 → 2000s`, `31-99 → 1900s`). Modal year 1996 (38 files), reflecting heavy revision activity in the mid-90s ASTM cycle.
- **Unique codes**: 165 distinct G-numbers from G1 to G179, no duplicates within a code+year tuple beyond expected reapproval reissues.
- **OCR coverage**: `_inventory.db` provides per-page OCR text for all PDFs (consume via SQLite, do not copy into wiki). OCR estimate: ~95% machine-readable based on the post-1990 ASTM authoring stack; pre-1990 scans (~8% of catalog) likely have lower OCR fidelity.
- **DRM status**: see `/mnt/ace/O&G-Standards/drm_protected_files.txt` for any G-Series files flagged as DRM-protected.

## Recommended follow-ups

Top 10 G-codes to promote to `wiki/standards/<code-id>.md` (priority-ordered for offshore-corrosion calc relevance):

1. **astm-g1** — Standard practice for preparing, cleaning, and evaluating corrosion test specimens (mass-loss baseline; cited from every coupon-based protocol).
2. **astm-g3** — Standard practice for conventions applicable to electrochemical measurements in corrosion testing (sign conventions, reporting).
3. **astm-g5** — Standard reference test method for making potentiodynamic anodic polarization measurements (the canonical Tafel scan).
4. **astm-g31** — Standard guide for laboratory immersion corrosion testing of metals.
5. **astm-g36** — Standard practice for evaluating SCC resistance of metals in boiling magnesium chloride.
6. **astm-g48** — Standard test methods for pitting and crevice corrosion resistance of stainless steels and related alloys by use of ferric chloride solution (the CRA screening backbone).
7. **astm-g102** — Standard practice for calculation of corrosion rates and related information from electrochemical measurements (turns G5 output into engineering corrosion rate).
8. **astm-g16** — Standard guide for applying statistics to analysis of corrosion data.
9. **astm-g46** — Standard guide for examination and evaluation of pitting corrosion (rating chart; cited everywhere pitting depths are reported).
10. **astm-g15** — Standard terminology relating to corrosion and corrosion testing (definitional anchor).

Concept-page cross-links to land or update:
- [cathodic-protection](../concepts/cathodic-protection.md) — anchor G8, G42, G95 alongside DNV-RP-B401 and DNV-RP-F103.
- [sour-service-materials](../concepts/sour-service-materials.md) — anchor G1, G31 mass-loss methods alongside NACE MR0175 / ISO 15156 and AMPP TM0177.
- [corrosion-rate-measurement](../concepts/corrosion-rate-measurement.md) — anchor G3, G5, G59, G61, G102, G106 as the measurement-methodology cluster.
- [electrochemical-corrosion](../concepts/electrochemical-corrosion.md) — kinetics-substrate concept (Wagner-Traud / Butler-Volmer / Tafel / passivity) underlying the G3/G5/G59/G102/G106 measurement column; W207 iter-44 authored.
- Optional: [pitting-and-crevice-corrosion](../concepts/pitting-and-crevice-corrosion.md) for G46/G48/G78 and [stress-corrosion-cracking](../concepts/stress-corrosion-cracking.md) for G36/G38/G39/G44.

Edition-history index: G15 (5 revisions), G48 (4 revisions), G85 (4 revisions), G1 (3 revisions), G38 (3 revisions), G78 (3 revisions), G105 (3 revisions) — multi-edition codes warrant a revision-history table on the per-code standards page.
