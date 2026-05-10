---
title: "O&G Standards catalog — ASTM E-Series (Test Methods, NDE, Fracture)"
slug: og-standards-astm-e-series
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
sources:
  - /mnt/ace/O&G-Standards/ASTM/E-Series
ingested: 2026-05-09
tags: ["astm", "e-series", "fracture-mechanics", "nde", "fatigue", "metallography", "og-standards-ingest", "publisher-catalog"]
---

# O&G Standards catalog — ASTM E-Series (Test Methods, NDE, Fracture)

> Metadata-first source page for the ASTM E-Series slice of the O&G-Standards consolidated library at `/mnt/ace/O&G-Standards/ASTM/E-Series/`. Generated 2026-05-09 from `/mnt/ace/O&G-Standards/_catalog.json` (catalog version 1.0.0, generated 2025-12-25).
> **Vendor PDFs do not enter this repo** per spinout 2026-05-05 governance — only publisher facts (titles, document IDs, revision years, file paths) are recorded here.

## Summary

ASTM Committee E (general test methods) is the cross-industry test-method substrate. Its standards are not addressed at oil & gas directly, but they are the methodological backbone that fitness-for-service codes (API 579 / ASME FFS-1), pipeline-integrity codes (API 580/581, BS 7910), and pressure-vessel inspection codes (ASME BPVC Section V/IX, API 510/570/653) cite by reference for laboratory measurement of fracture toughness, fatigue crack growth, hardness, NDE qualification, metallographic examination, and thermal characterization. The 3,559 catalog entries span 1958–2004 (modal years 1995–2002) across roughly 1,800 distinct E-codes; the modal year distribution reflects the catalog's late-1990s/early-2000s acquisition window rather than the live revision state of the standards.

## Metadata

| Field | Value |
|-------|-------|
| id | og-standards-astm-e-series |
| publisher | ASTM International (Committee E — General Test Methods) |
| document_count | 3559 (catalog entries; filesystem walks return 3531 — see Verification) |
| total_size_bytes | 445,464,711 |
| total_size_mb | 424.8 |
| extension_breakdown | .pdf: 3559 (100%) |
| sub_committee_breakdown | E08 Fatigue & Fracture, E07 NDE, E04 Metallography, E37 Thermal Measurements, E13 Spectroscopy, E11 Statistical Methods, E15 Industrial & Specialty Chemicals, E20 Temperature Measurement, E21 Space Simulation, E27 Hazard Potential of Chemicals, E28 Mechanical Testing, E29 Particle Sizing, E33 Building & Environmental Acoustics, E34 Occupational Health & Safety, E35 Pesticides & Antimicrobials, E50 Environmental Assessment — see Subcommittee breakdown |
| year_range | 1958–2004 (modal years 1995–2002; top buckets 2002:344, 1998:332, 2000:301) |
| top_year_buckets | 2002: 344, 1998: 332, 2000: 301, 1997: 288, 1996: 273, 2001: 269, 1995: 253, 2003: 248, 1999: 248, 1994: 136 |
| unique_codes_observed | ~1,818 distinct E-codes (regex-extracted from filenames) |
| codes_with_multi_edition | ~1,103 codes appear with ≥2 editions in the catalog |
| top_files_per_code | E8: 12, E253: 11, E1623: 10, E1354: 8, E2061: 8, E1316: 7, E1519: 7, E176: 7, E284: 7, E609: 7 |
| parent_root | /mnt/ace/O&G-Standards/ASTM/E-Series |
| catalog_source | /mnt/ace/O&G-Standards/_catalog.json |
| ocr_text_root | /mnt/ace/O&G-Standards/_ocr_text |
| inventory_db | /mnt/ace/O&G-Standards/_inventory.db (6.37 GB sqlite) |
| drm_protected | 0 entries match `ASTM/E-Series/` in `drm_protected_files.txt` |
| raw_source_policy | link-only; do not copy raw bulk data into git/wiki raw folders |
| extract_priority | metadata-only (per #2536 deep-extraction queue) |

## Subcommittee breakdown

ASTM E-codes do not encode their subcommittee in the document number, so the grouping below is by subject-matter rather than by document-ID prefix. Counts are from the catalog (multiple editions per code add to the count).

### E08 — Fatigue & Fracture (the O&G-critical subcommittee)

| Code | Subject | Editions in catalog |
|------|---------|---------------------|
| E399 | Plane-strain Fracture Toughness K_IC of Metallic Materials | 1 |
| E647 | Measurement of Fatigue Crack Growth Rates (da/dN vs ΔK) | 2 |
| E1290 | Crack-Tip Opening Displacement (CTOD) Fracture Toughness | 3 |
| E1820 | J-Integral / Unified Fracture Toughness (J-R curve) | 3 |
| E1921 | Reference Temperature T₀ for Ferritic Steels (Master Curve) | 4 |
| E2899 | Failure Assessment of Cracks in Solids (elastic-plastic FAD) | (post-catalog publication; 2013+ — likely absent or sparse) |
| E561 | K-R Curve Determination | 1 |
| E813 | (withdrawn — superseded by E1820) J_IC Determination | 1 |
| E739 | Statistical Analysis of Linear/Linearized S-N and ε-N Data | 2 |
| E466 | Force-Controlled Constant-Amplitude Axial Fatigue Tests | 1 |
| E606 | Strain-Controlled Fatigue Testing | (likely present; not surfaced in top counts) |

E08 standards are the laboratory backbone behind BS 7910 Annex M, API 579-1/ASME FFS-1 Annex 9F (toughness), and DNV-RP-F108 fracture-control requirements. Master Curve (E1921) underpins reference-temperature shifts used in both ferritic-pressure-vessel and pipeline applications.

### E07 — Nondestructive Examination (NDE)

| Code | Subject | Editions in catalog |
|------|---------|---------------------|
| E94 | Standard Guide for Radiographic Examination | 3 |
| E709 | Standard Guide for Magnetic Particle Testing | 3 |
| E1316 | Standard Terminology for Nondestructive Examinations | 7 |
| E1417 | Standard Practice for Liquid Penetrant Testing | 1 |
| E1444 | Standard Practice for Magnetic Particle Testing | 3 |
| E165 | Standard Practice for Liquid Penetrant Examination (general industry) | 3 |
| E1419 | Standard Practice for Examination of Seamless, Gas-Filled, Pressure Vessels (UT) | 4 |

E07 is referenced by ASME BPVC Section V (Nondestructive Examination), API 510 / 570 / 653 (in-service inspection), and pipeline construction codes when qualifying examination procedures.

### E04 — Metallography

| Code | Subject | Editions in catalog |
|------|---------|---------------------|
| E3 | Standard Guide for Preparation of Metallographic Specimens | 3 |
| E45 | Determining the Inclusion Content of Steel | 1 |
| E112 | Determining Average Grain Size | 2 |
| E384 | Microhardness of Materials (Knoop / Vickers) | 2 |
| E140 | Standard Hardness Conversion Tables (Rockwell, Vickers, Brinell, Knoop, Scleroscope) | 5 |
| E92 | Vickers Hardness of Metallic Materials | 2 |
| E18 | Rockwell Hardness of Metallic Materials | 3 |
| E10 | Brinell Hardness of Metallic Materials | 3 |

E04 underpins material-quality acceptance for line-pipe, forgings, and weldments specified to API 5L, API 6A, ASTM A370, and many pressure-vessel grades.

### E37 — Thermal Measurements

| Code | Subject | Editions in catalog |
|------|---------|---------------------|
| E831 | Linear Thermal Expansion of Solid Materials by Thermomechanical Analysis (TMA) | 3 |
| E1131 | Compositional Analysis by Thermogravimetry (TGA) | 3 |
| E1356 | Glass Transition Temperatures by DSC (Tg) | 3 |
| E1269 | Specific Heat Capacity by DSC | (likely present) |
| E1640 | Glass Transition by DMA | (likely present) |

Used for elastomer / coating / polymer qualification — see DNV-RP-F102/F106 (pipeline coatings) and API 17J (flexible-pipe non-metallic-layer characterization).

### E13 — Spectroscopy

Atomic / molecular / mass / X-ray spectroscopic methods (E135 has 6 editions in catalog as terminology; E1019 has 4 editions for C/H/N/O analysis in steel). Cross-cuts material-composition verification used in heat-traceability for sour-service pipelines (NACE MR0175 / ISO 15156 hardness limits depend on chemistry).

### E11 — Statistical Methods

E178 (1994 edition in catalog) — Standard Practice for Dealing with Outlying Observations. Underpins data-trimming conventions in fatigue / fracture data reduction.

### E28 — Mechanical Testing

E4 (5 editions): Practices for Force Verification of Testing Machines. E8 (12 editions — top of catalog): Tension Testing of Metallic Materials. E21: Elevated-Temperature Tension Tests of Metallic Materials. E23 (5 editions): Notched Bar Impact Testing (Charpy/Izod). These are the universal-load-frame methods underlying every tensile / impact / yield-strength acceptance test for line-pipe, fittings, and structural steels.

### Other E-subcommittees represented

E15 (industrial chemicals), E20 (thermocouples / RTDs — E220, E230 series for thermocouple calibration), E21 (space simulation — peripheral to O&G), E27 (hazardous chemicals), E29 (particle sizing — relevant to drilling muds / proppants), E33 (acoustics), E34 (occupational health), E35 (pesticides), E50 (environmental assessment — relevant for site-characterization / Phase-I ESA on pipeline ROW). Most of these are catalog-incidental and rarely cited by O&G design codes.

## Bucket purity sample

30 random catalog entries from `ASTM/E-Series/`, code-extracted via filename regex (deterministic seed 20260509):

| Code | Filename | Size (B) |
|------|----------|----------|
| E715 | E 715 - 80 R96 _RTCXNS04MFI5NKUX.pdf | 17,604 |
| E112 | E 112 - 96 _RTEXMG__.pdf | 349,056 |
| E2136 | E 2136 - 01 _RTIXMZY_.pdf | 1,757,667 |
| E2016 | E 2016 - 99 _RTIWMTY_.pdf | 1,376,037 |
| E1439 | E 1439 - 98 _RTE0MZKTOTG_.pdf | 173,712 |
| E1890 | E 1890 - 97 _RTE4OTATUKVE.pdf | 41,527 |
| E557 | E 557 - 93 _RTU1NY05MW__.pdf | 105,330 |
| E2002 | E 2002 - 98 _RTIWMDITOTG_.pdf | 37,029 |
| E1026 | E 1026 - 03 _RTEWMJYTMDM_.pdf | 101,041 |
| E690 | E 690 - 98 _RTY5MC05OA__.pdf | 42,608 |
| E2040 | E 2040 - 03 _RTIWNDA_.pdf | 31,459 |
| E519 | E 519 - 00 _RTUXOS0WMA__.pdf | 83,863 |
| E1255 | E 1255 - 96 _RTEYNTUTOTY_.pdf | 77,961 |
| E1125 | E 1125 - 99 _RTEXMJU_.pdf | 62,581 |
| E394 | E 394 - 94 _RTM5NC1SRUQ_.pdf | 34,607 |
| E2198 | E 2198 - 02 _RTIXOTG_.pdf | 29,955 |
| E1498 | E 1498 - 92 R04 _RTE0OTG_.pdf | 135,653 |
| E1794 | E 1794 - 00 _RTE3OTQTUKVE.pdf | 24,312 |
| E238 | E 238 - 84 R02 _RTIZOA__.pdf | 81,757 |
| E1 | E 1 - 03 _RTETUKVE.pdf | 279,687 |
| E1021 | E 1021 - 95 R01 _RTEWMJE_.pdf | 59,403 |
| **(impurity)** | **Creep Of Concrete (C512).PDF** — ASTM **C**-Series file misfiled in E-Series | 67,099 |
| E1290 | E 1290 - 99 _RTEYOTATOTK_.pdf | 218,619 |
| E773 | E 773 - 01 _RTC3MW__.pdf | 95,443 |
| E1629 | E 1629 - 94 R01 _RTE2MJK_.pdf | 92,462 |
| E1005 | E 1005 - 97 _RTEWMDUTOTC_.pdf | 111,679 |
| E2263 | E 2263 - 04 _RTIYNJM_.pdf | 150,974 |
| E1845 | E 1845 - 96 _RTE4NDUTOTY_.pdf | 23,294 |
| E23 | E 23 - 01 _RTIZLTAXQQ__.pdf | 393,807 |
| E178 | E 178 - 94 _RTE3OC05NA__.pdf | 104,190 |

**Bucket purity:** 29/30 = ~97%. One impurity in this 30-doc sample (`Creep Of Concrete (C512).PDF` — an ASTM C-Series concrete-test PDF misfiled into E-Series). Top-of-directory listing shows additional misfiles (`Abrasion_Resistance_(C418).PDF`, `Admixture_2_(C260).PDF`, several `(C##)` concrete-test PDFs at root) — recommend a one-time reclass sweep against an `ASTM/C-Series/` bucket as a follow-up.

## Verification

- Document count cross-checked against `_catalog.json` filtered by `relative_path` starting with `ASTM/E-Series/` → 3,559 entries.
- Filesystem walk (`find … -type f -name '*.pdf'`) returns 3,531 PDFs. The +28 catalog-vs-filesystem gap likely reflects deduplication or hash-merge entries in the catalog that don't materialize as on-disk PDFs; deferred to a catalog-integrity audit (out of scope for metadata-first ingest).
- Year range derived from filename pattern `E NNNN - YY` with 2→4 digit normalization (yy ≤ 29 → 20YY, yy ≥ 50 → 19YY); 3,516 of 3,559 entries (98.8%) parsed cleanly.
- OCR coverage: per-page text expected available in `_inventory.db` (6.37 GB sqlite) for the full E-Series; spot-confirmed via existence of the inventory database and `_ocr_text` root directory. Per-document OCR-extraction status is not surfaced in `_catalog.json` and was not enumerated to keep this pass within the metadata-only contract.
- Bucket purity: ~97% (1 misfiled non-E doc in 30-sample); root-of-directory listing reveals additional `(C###)` concrete-test PDFs misfiled — full purity sweep deferred.
- Subcommittee assignments are derived from the published ASTM E-committee subcommittee scopes (E07 NDE, E08 Fatigue/Fracture, E04 Metallography, etc.); since ASTM filenames do not encode subcommittee, cross-check is by topic-keyword grouping of canonical codes.
- DRM status: 0 ASTM/E-Series/ entries appear in `drm_protected_files.txt`.

## Recommended follow-ups

Top E-codes to promote to `wiki/standards/<code-id>.md` pages, prioritized by O&G fitness-for-service / pipeline-integrity / pressure-vessel relevance:

1. **E399** — Plane-strain Fracture Toughness K_IC. Foundational fracture-mechanics method; cited by API 579/ASME FFS-1, BS 7910.
2. **E647** — Fatigue Crack Growth Rate da/dN. Underpins crack-growth life assessment in pipelines (DNV-RP-F108) and pressure vessels (API 579 Part 9).
3. **E1820** — J-Integral / Unified Fracture Toughness. Dominant elastic-plastic toughness method post-2000; supersedes E813.
4. **E1290** — CTOD Fracture Toughness. Required by BS 7910 Annex K; widely referenced for line-pipe weld qualification.
5. **E1921** — Master Curve T₀. Reference-temperature method for ferritic-steel toughness; central to RPV and HPHT pipeline assessments.
6. **E709** — Magnetic Particle Testing Guide. Cited by ASME BPVC V, API 510/570/653.
7. **E94** — Radiographic Examination Guide. Cited by ASME BPVC V Article 2.
8. **E1444** — Magnetic Particle Testing Practice. The acceptance-procedure companion to E709.
9. **E45** — Inclusion Content of Steel. Required for sour-service line-pipe qualification (NACE MR0175 / ISO 15156 chain).
10. **E112** — Average Grain Size. Required for HIC/SOHIC-resistant pipe and pressure-vessel forgings.
11. **E8** — Tension Testing of Metallic Materials (12 editions in catalog — top E-code by file count). Universal mechanical-acceptance method.
12. **E23** — Notched-Bar Impact (Charpy). Required by virtually every line-pipe, fitting, and pressure-vessel material specification.

**Concept-page cross-links to create or update:**
- `wiki/concepts/fracture-toughness.md` — link to standards pages for E399, E1290, E1820, E1921; note relationship to BS 7910 / API 579 acceptance criteria.
- `wiki/concepts/fatigue-crack-growth.md` — link E647 standards page; reference Paris-law parameters and ΔK_th conventions.
- `wiki/concepts/nde-methods.md` — index page covering E94 (RT), E709 (MT), E1417/E165 (PT), E1444 (MT practice); cross-link ASME BPVC V and API in-service codes.
- `wiki/concepts/master-curve-t0.md` — dedicated concept page for E1921 reference-temperature methodology.

**Catalog-hygiene follow-up:** sweep `ASTM/E-Series/` for misfiled non-E documents (observed: `(C###)` concrete-test PDFs at directory root). Either reclassify into a future `ASTM/C-Series/` bucket or note as known-impurities in the catalog.

## Cross-references

Standards pages already promoted from this E-Series slice (each should cite this source page for catalog provenance):

- [`standards/astm-e399`](../standards/astm-e399.md) — Plane-strain fracture toughness K_IC of metallic materials.
- [`standards/astm-e1820`](../standards/astm-e1820.md) — J-integral / unified fracture toughness (J-R curve).
- [`standards/astm-e1921`](../standards/astm-e1921.md) — Reference temperature T₀ for ferritic steels (Master Curve).
- [`standards/astm-e647`](../standards/astm-e647.md) — Measurement of fatigue crack growth rates (da/dN vs ΔK).

Concept pages that should cite this source when invoking E-Series-published methods:

- [`concepts/fracture-toughness-measurement`](../concepts/fracture-toughness-measurement.md) — E399 / E1820 / E1290 / E1921 are the laboratory backbone for fracture-toughness acceptance.
- [`concepts/mechanical-fatigue`](../concepts/mechanical-fatigue.md) — E647 (da/dN), E466 (force-controlled fatigue), E739 (S-N statistical analysis).
- [`concepts/engineering-critical-assessment`](../concepts/engineering-critical-assessment.md) — E1820 J-integral and E1921 Master Curve toughness inputs feed BS 7910 / API 579 ECA workflow.
- [`concepts/brittle-fracture`](../concepts/brittle-fracture.md) — E1921 Master Curve T₀ is the reference-temperature method for ferritic-steel brittle-fracture transition.
- [`concepts/welding-procedures-and-acceptance`](../concepts/welding-procedures-and-acceptance.md) — E94 (RT), E709 / E1444 (MT), E165 / E1417 (PT), and E45 / E112 (metallography) are NDE and metallurgical-acceptance methods cited by ASME BPVC V and API in-service codes.
