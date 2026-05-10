---
title: "ASTM A370 — Mechanical Testing of Steel Products"
slug: astm-a370
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
code_id: astm-a370
publisher: ASTM
revision: "2011 (latest in catalog)"
revision_source: /mnt/ace/O&G-Standards/_catalog.json
verified_on: 2026-05-09
public_url: https://www.astm.org/a0370-24.html
sources:
  - /mnt/local-analysis/workspace-hub/llm-wiki/wikis/engineering-standards/wiki/sources/og-standards-astm-a-series.md
  - /mnt/ace/O&G-Standards/ASTM/A-Series/ASTM_A370_(2011)_Std_Test_Methods_and_Definitions_for_Mechanical_Testing_of_Steel_Products.pdf
extraction_policy: metadata-only
raw_copy_allowed: false
tags:
  - astm
  - a-series
  - mechanical-testing
  - tension-test
  - charpy
  - hardness
  - bend-test
  - standards
---

# ASTM A370 — Standard Test Methods and Definitions for Mechanical Testing of Steel Products

> **Standard identity (L0 prose).** `code_id`: astm-a370 · `publisher`: ASTM · `revision`: 2011 (latest edition resident in `/mnt/ace/O&G-Standards/_catalog.json`; ASTM reissues A370 on a roughly biennial cadence, current published edition at the publisher is newer — see *Edition history* below).

## Scope

ASTM A370 is the umbrella **test-method-and-definitions** standard for mechanical testing of wrought and cast steel products. It consolidates the procedures every ASTM A-series product specification (plate, pipe, tube, bar, shape, forging, casting, fastener, reinforcing bar) calls out by reference for property-of-record qualification:

- **Tension testing** of round, flat, full-section, and tubular specimens — yield strength, ultimate tensile strength, elongation, reduction of area;
- **Charpy V-notch impact testing** — absorbed energy, lateral expansion, percent shear-area at specified test temperature;
- **Hardness testing** — Brinell and Rockwell methods and conversions;
- **Bend testing** — guided-bend and free-bend, mandrel diameter ratios and bend angle;
- **Specimen geometry** — full-size, sub-size, longitudinal vs. transverse orientation, heat-treatment-condition reporting;
- **Machine calibration, gripping, gauge-length marking, and report content** — including provisions for round-robin verification.

A370 does **not** specify acceptance criteria — those live in the product specification (A106, A516, A572, etc.). A370 specifies **how** the test is performed and **what** is reported, so that any A-series product spec is interpretable against a single, fixed measurement protocol. This makes A370 the most-referenced normative anchor in the A-Series catalog: every other A-spec invokes it, and API Spec 5L / 6A / 17J and ASME BPVC Section II-A invoke it directly for line-pipe, wellhead, flexible-pipe, and pressure-vessel material qualification.

## Edition history

ASTM A370 is reissued on a roughly biennial cadence. The local O&G-Standards catalog (`_catalog.json`, generated 2025-12-25) holds the following editions under `ASTM/A-Series/` (filename heuristic):

| Edition | Catalog filename | Notes |
|---------|------------------|-------|
| A 370 – 01 | `A_370_01_;QTM3MC0WMQ_.pdf` | 2001 issue |
| A 370 – 02 | `A_370_02_;QTM3MC0WMKUX.pdf` | 2002 issue (also: `ASTM_A370_(2002)_...`) |
| A 370 – 03 | `A_370_03_;QTM3MA_.pdf`, `A_370_03_;QTM3MC0WMW_.pdf`, `A_370_03_;QTM3MC1SRUQ_.pdf` | 2003 issue (multiple reprint variants) |
| A 370 – 08a | `ASTM_A370-08a_Prove_meccaniche.pdf` | 2008a issue (Italian-titled scan) |
| A 370 – 11 | `ASTM_A370_(2011)_Std_Test_Methods_and_Definitions_for_Mechanical_Testing_of_Steel_Products.pdf` | 2011 issue — **latest in catalog** |

**8 catalog files across 5 distinct editions (2001, 2002, 2003, 2008a, 2011).** The publisher's currently-active edition is newer than the catalog's 2011 copy (ASTM continues to maintain A370); resolvers needing the live edition should consult the publisher catalog directly. Per spinout governance, vendor PDFs do not enter this repo — only the metadata above is recorded.

## Key sections

A370 is organized into a body covering the universal test-method requirements followed by annexes that specialize the procedure for specific product forms. Section numbering below follows the long-stable structure carried across the editions present in the catalog (the headings are stable across editions even when section numbers shift slightly):

- **Section 5 — Tension test.** Procedure for round, flat, and full-section specimens. Strain rate, gauge-length marking, yield-point determination (offset, extension-under-load, halt-of-pointer methods), reporting of yield strength, tensile strength, elongation, and reduction of area.
- **Section 7 — Sub-size specimens.** Geometry and use rules when full-size specimens cannot be machined from the product (typical for thin plate, small-diameter tubing, sheet). Cross-section dimensions and parallel-length requirements; reporting requires explicit sub-size declaration.
- **Section 9 — Charpy V-notch impact testing.** Specimen geometry (10 × 10 × 55 mm full-size; sub-size 10 × 7.5, 10 × 6.7, 10 × 5, 10 × 3.3, 10 × 2.5 mm), notch geometry, machine calibration against NIST reference specimens, test temperature control, and reporting of absorbed energy, lateral expansion, and percent shear (ductile) fracture appearance.
- **Section 11 — Hardness testing.** Brinell (HBW) and Rockwell (HRB, HRC) methods, indenter and load selection, location of indentations, and conversion tables. Defers to ASTM E10 / E18 / E140 for the underlying procedure and conversions.
- **Section 12 — Bend test.** Guided-bend procedure, mandrel diameter as a multiple of specimen thickness, bend angle (typically 180°), acceptance based on outer-fiber crack-free condition.
- **Annex A1 — Steel tubular products.** Specialized tension-test and flattening-test procedures for pipe and tube; full-section vs. strip-from-pipe specimens.
- **Annex A2 — Steel castings.** Specimen orientation and machining from cast keel-blocks or integrally-cast test coupons.
- **Annex A3 — Round rod, plate, and bar.** Specimen orientation (longitudinal vs. transverse), location across product cross-section, and identification.
- **Annex A4 — Forged / rolled stainless steel.** Adaptations of the test methods for stainless and heat-resisting product forms.
- **Annex A5 / A6 — Sampling.** Number of specimens per heat or per lot, location within the product, and re-test rules when an initial specimen fails.

The annex structure means A370 is a **superset standard**: a downstream A-spec can invoke "A370" without further qualification and inherit the entire test-method library, or invoke a specific annex when the product form demands it.

## Cross-references

A370 sits at the convergence of the ASTM **E-committee** (general test methods) and the **A-committee** (iron and steel products). Its upstream and downstream relationships:

**Upstream test-method standards (A370 defers to these for the underlying procedure)**
- **ASTM E8 / E8M** — Standard test methods for tension testing of metallic materials. The parent test-method standard for tension testing across all metallic materials; A370 specializes E8 to steel and adds the Charpy / hardness / bend methods on top.
- **ASTM E23** — Standard test methods for notched bar impact testing of metallic materials. The parent Charpy standard; A370 §9 cites E23 for the V-notch procedure and machine-calibration provisions.
- **ASTM E18** — Standard test methods for Rockwell hardness of metallic materials. Parent for HRB / HRC.
- **ASTM E10** — Standard test method for Brinell hardness of metallic materials. Parent for HBW.
- **ASTM E140** — Standard hardness conversion tables for metals. Cited by A370 §11 for Brinell ↔ Rockwell ↔ Vickers conversions.

**Downstream product specifications and codes (call A370 for mechanical-property qualification)**
- **API Spec 5L** — Line pipe. A370 is the qualifying test method for tension, Charpy, and hardness on line-pipe body and weld-seam material.
- **API Spec 6A** — Wellhead and Christmas tree equipment. A370 is invoked for material qualification on PSL-1 through PSL-4 trim, including notch-toughness Charpy testing of wellhead bodies and bonnets.
- **API Spec 17J** — Specification for unbonded flexible pipe. A370 is the qualification standard for the carbon-steel and stainless-steel armor-wire and pressure-vault tension tests.
- **ASME BPVC Section II-A** — Ferrous material specifications. A370 is the test-method anchor for the SA-versions of A-series specs that BPVC Section II-A republishes (SA-106, SA-516, etc.).
- **AISC 360** — Specification for structural steel buildings. Indirectly cites A370 via the A6 / A572 / A992 family of structural steel specs.
- **DNV-OS-F101** — Submarine pipeline systems. References A370 (alongside ISO 6892, ISO 148, EN 10002) for tension / Charpy / hardness methods on linepipe-grade steel.

**Wiki cross-links**
- [O&G Standards catalog — ASTM A-Series](../sources/og-standards-astm-a-series.md) — multi-edition coverage manifest and bucket-purity audit; sanctioned A-series promotion list (A370 is **#1 promotion candidate** by cross-reference fan-in).
- [API RP 2A-WSD](api-rp-2a-wsd.md) — fixed offshore platform planning; depends on A572 / A992 structural steels whose mechanical properties are A370-qualified.
- Calc citation contract: `.claude/rules/calc-citation-contract.md` — frontmatter contract (`code_id`, `publisher`, `revision`) this page satisfies for fail-closed citation resolution.

## Sources

- **Source page (this wiki).** [O&G Standards catalog — ASTM A-Series](../sources/og-standards-astm-a-series.md). Catalog manifest for the entire ASTM A-Series slice; 2,147 documents at `/mnt/ace/O&G-Standards/ASTM/A-Series/`, of which 8 catalog files across 5 editions (2001, 2002, 2003, 2008a, 2011) are A370. A370 is identified there as the highest cross-reference-fan-in code in the slice and the #1 promotion candidate for `wiki/standards/<code-id>.md`.
- **Catalog manifest (read-only).** `/mnt/ace/O&G-Standards/_catalog.json` (catalog version 1.0.0, generated 2025-12-25) — filtered with `organization == 'ASTM' AND relative_path startswith 'ASTM/A-Series/' AND filename matches /\bA[\s_]?370\b/i` returns the 8 entries enumerated under *Edition history*.
- **Vendor PDFs (link-only; do NOT copy into git).** Latest edition in catalog: `/mnt/ace/O&G-Standards/ASTM/A-Series/ASTM_A370_(2011)_Std_Test_Methods_and_Definitions_for_Mechanical_Testing_of_Steel_Products.pdf`. Per spinout 2026-05-05 governance and `.claude/rules/calc-citation-contract.md` deny-list, vendor-derivative PDFs remain at their `/mnt/ace/` location and are not republished here.
- **Publisher catalog.** ASTM International — A370 product page (search "A370" at <https://www.astm.org>).
