---
title: "ASTM D86 — Distillation of Petroleum Products at Atmospheric Pressure"
slug: astm-d86
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
code_id: astm-d86
publisher: ASTM
revision: "2004 (latest in catalog)"
revision_source: /mnt/ace/O&G-Standards/_catalog.json
verified_on: 2026-05-09
public_url: https://www.astm.org/d0086-23.html
sources:
  - /mnt/local-analysis/workspace-hub/llm-wiki/wikis/engineering-standards/wiki/sources/og-standards-astm-d-series.md
extraction_policy: metadata-only
raw_copy_allowed: false
tags:
  - astm
  - d-series
  - d02
  - distillation
  - petroleum-products
  - fuel-quality
  - standards
---

# ASTM D86 — Standard Test Method for Distillation of Petroleum Products and Liquid Fuels at Atmospheric Pressure

> **Standard identity (L0 prose).** `code_id`: astm-d86 · `publisher`: ASTM · `revision`: 2004 (latest edition resident in `/mnt/ace/O&G-Standards/_catalog.json`). ASTM revises D86 on a roughly annual cadence; the publisher's currently-active edition is newer than the catalog's 2004 copy — see *Edition history* below.

## Scope

ASTM D86 specifies the **atmospheric-pressure batch distillation** procedure for petroleum products and liquid fuels in the light- and middle-distillate boiling range — including motor gasoline, aviation gasoline, aviation turbine (jet) fuel, kerosene, diesel fuel, marine fuel, distillate fuel oils, naphthas, and the lighter solvent / petroleum-spirit fractions. The method yields:

- **Initial Boiling Point (IBP)** — the vapor temperature at which the first drop of condensate falls from the condenser tube;
- **Volume-percent recovery vs. vapor-temperature curve** — temperatures recorded at 5%, 10%, 20%, 30%, 40%, 50%, 60%, 70%, 80%, 90%, and 95% recovery (the canonical "distillation curve");
- **Final Boiling Point (FBP)** — also called the End Point (EP), the maximum vapor temperature observed during the test;
- **Residue and loss** — residual liquid in the flask plus the difference between charge volume and total recovered + residue, taken as evaporative loss.

Results are corrected for **barometric pressure** (vapor-temperature readings shift with deviation from the standard 101.3 kPa atmosphere) and reported per the four-group classification defined by the standard. D86 is the **foundation distillation method** invoked by every ASTM downstream-fuel specification for front-end volatility, mid-range driveability / cetane behavior, and tail-end deposit-formation potential. Heavy residual fuels and lubricants whose end points exceed D86's apparatus envelope are tested instead by **ASTM D1160** (reduced pressure distillation) or by the GC-based **ASTM D2887** (simulated distillation).

D86 is **not** a specification — it does not set acceptance limits. Acceptance limits live in the product spec (D4814 for gasoline, D1655 for jet, D975 for diesel, etc.), which call out specific D86 result thresholds (e.g., "T10 max 70 °C, T50 110–250 °C, T90 max 360 °C, FBP max 400 °C") as part of the multi-property fuel-quality envelope.

## Edition history

ASTM D86 has an unusually long edition history (the standard dates to **1922**) and is reissued essentially **annually**. The local O&G-Standards catalog (`_catalog.json`, generated 2025-12-25) holds the following editions under `ASTM/D-Series/` (filename heuristic — filenames are vendor-obfuscated and carry only a `D 86 - YY` year tag):

| Edition | Catalog filename | Notes |
|---------|------------------|-------|
| D 86 – 00 | `D 86 - 00  _RDG2LTAWQQ__.pdf` | 2000 issue |
| D 86 – 01 | `D 86 - 01  _RDG2LTAX.pdf`, `D 86 - 01  _RDG2LTAXRTE_.pdf` | 2001 issue (two reprint variants) |
| D 86 – 02 | `D 86 - 02  _RDG2LTAY.pdf` | 2002 issue |
| D 86 – 03 | `D 86 - 03  _RDG2LTAZ.pdf` | 2003 issue |
| D 86 – 04 | `D 86 - 04  _RDG2.pdf`, `D 86 - 04  _RDG2LTA0.pdf`, `D 86 - 04  _RDG2LTA0QQ__.pdf`, `D 86 - 04  _RDG2LVJFRA__.pdf` | 2004 issue (four reprint / errata variants) — **latest in catalog** |

**9 catalog files across 5 distinct editions (2000, 2001, 2002, 2003, 2004).** Per the source-page guidance, the multiple `_R…` and `_RDG2…` filename suffixes likely encode reapproval-tag and base-vs-errata pairings rather than five fully distinct base documents per year; a content-hash dedup pass against `_inventory.db` is recommended before any consumer treats the 9-file count as 9 independent revisions. The publisher's currently-active edition (D86-23 or later) is newer than the catalog's 2004 copy; resolvers needing the live edition should consult the publisher catalog directly. Per spinout governance, vendor PDFs do not enter this repo — only the metadata above is recorded.

## Key sections

D86's procedural body has been structurally stable across the editions present in the catalog. The headings below track the long-running structure (section numbers shift slightly across revisions but the substantive content is preserved):

- **Apparatus.** The defining apparatus is a **125 mL distillation flask** of specified neck-and-side-arm geometry (the 100 mL nominal charge plus headspace), heated by an electric heater with **shielded heat-source enclosure**, vapor temperature measured by a **specified thermometer** (mercury-in-glass per the historical method, electronic temperature sensor per the modern automated variant) inserted at a fixed depth into the flask neck, condenser tube held in a **water bath** at 0–60 °C selected by sample group, and a 100 mL graduated receiver positioned to catch condensate at the condenser tube tip. **Automated D86 instruments** (e.g., per Annex A2 / A3 of recent editions) integrate flask heating, vapor-temperature acquisition, drop-sensing for IBP, and volume tracking under a single PID-controlled loop and are now the predominant laboratory implementation; manual D86 remains the reference procedure.
- **Sample groups (Group 1 through Group 4).** Samples are pre-classified into one of four groups by **vapor pressure / volatility** before the test, because charge-cooling, condenser-bath temperature, flask support-disc hole size, and heat-rate prescription all depend on the group:
  - **Group 1** — high-volatility products (e.g., aviation gasoline, motor gasoline, light naphtha). Sample chilled before charging; condenser bath cold (0–4 °C).
  - **Group 2** — moderate volatility; condenser bath cold-to-cool.
  - **Group 3** — moderate-to-low volatility (e.g., kerosene, jet fuel, light diesel). Condenser bath cool-to-warm.
  - **Group 4** — low-volatility products (e.g., heavier diesel, distillate fuel oils, gas oils). Condenser bath warm (0–60 °C, set so condensate flows freely without solidifying).
- **Procedure.** Charge 100 mL of sample to the flask at the group-specific charging temperature; assemble the apparatus with thermometer / sensor at the fixed insertion depth; apply heat at the prescribed rate (typically 5–15 mL/min recovery rate, group-dependent, with explicit IBP-to-5%-recovery time window and 5%-to-FBP recovery-rate window); record vapor temperature at IBP (first drop), at each prescribed % recovery, and at FBP; cool, measure residue and compute loss (loss = 100 − recovered − residue).
- **Pressure correction.** Vapor temperatures observed during the test are corrected to the standard atmosphere (**101.3 kPa**) using a tabulated correction (a function of barometric pressure deviation and observed vapor temperature) before being reported. This is the principal source of inter-laboratory bias when ignored.
- **Reporting.** The full distillation curve (IBP, %-recovery temperatures, FBP) plus residue and loss volumes, with corrections applied; group designation; and any deviations (cracking observed, decomposition, condensate dripping abnormalities). The standard prescribes a precision statement (repeatability and reproducibility) for each product class.
- **Relationship to simulated distillation.** **ASTM D2887** is a **separate parallel method** that reproduces the boiling-range distribution by **gas chromatography on a non-polar column**, calibrated against an n-paraffin retention-time vs. boiling-point ladder. D2887 and D86 are not interchangeable: D86 measures the physical vapor-liquid distillation under group-specific conditions; D2887 measures a chromatographic boiling-range distribution that correlates with — but is not identical to — the D86 curve. Many fuel specs allow D2887 as an *alternative* for specific recovery points, with a published bias correlation (e.g., D2887-to-D86 conversion is documented in **ASTM D7345** and in spec footnotes).

## Application

D86 is invoked by **essentially every ASTM downstream petroleum-products specification** to define the front-end / mid-range / tail-end volatility envelope:

- **ASTM D4814** — Standard Specification for Automotive Spark-Ignition Engine Fuel (motor gasoline). D86 sets the T10 / T50 / T90 / FBP envelope per volatility class (Class A through Class E) and seasonal vapor-pressure / volatility-index combinations.
- **ASTM D1655** — Standard Specification for Aviation Turbine Fuels (Jet A, Jet A-1). D86 sets T10 max 205 °C and FBP max 300 °C (typical) for the kerosene-range jet-fuel cut.
- **ASTM D975** — Standard Specification for Diesel Fuel Oils. D86 sets the T90 envelope (e.g., 282–338 °C for Grade No. 2-D) used to bound deposit-formation potential.
- **ASTM D396** — Standard Specification for Fuel Oils. D86 sets distillation limits for the lighter Grade No. 1 / No. 2 fuel oils; heavier residual grades (No. 4 / No. 5 / No. 6) are characterized by viscosity and flash, not D86.
- **ASTM D6751** — Standard Specification for Biodiesel Fuel Blend Stock (B100). D86 fixes T90 max 360 °C for B100 to bound the methyl-ester boiling-range tail.
- **ASTM D7467** — Standard Specification for Diesel Fuel Oil, Biodiesel Blend (B6 to B20). D86 carries through from D975 to the blended fuel.
- **ASTM D3699 / D3699M** — Standard Specification for Kerosene. D86 sets the kerosene-cut volatility envelope.
- **Ad hoc refining and custody-transfer practice.** D86 is also the primary boiling-range diagnostic in refinery yield-and-quality monitoring (crude unit cut points, blend control), pipeline / terminal custody-transfer disputes (off-spec fuel claims), and incident investigations (contamination, mis-blending, wrong-grade delivery).

The frequency-of-citation across the downstream-fuels spec lattice is why the source page identified **D86 as the #1 promotion candidate** in the entire ASTM D-Series slice (alongside D975, with which it shares the highest catalog-edition count of 9).

## Cross-references

**Companion / alternative distillation methods**
- **ASTM D2887** — Boiling Range Distribution of Petroleum Fractions by Gas Chromatography (simulated distillation, "SimDist"). Parallel method via GC; D86-equivalent recovery points obtainable by published correlations.
- **ASTM D1160** — Distillation of Petroleum Products at Reduced Pressure. Used for heavy fractions (vacuum gas oil, residual fuel oil) whose end point exceeds D86's atmospheric-pressure envelope.
- **ASTM D7345** — Distillation of Petroleum Products and Liquid Fuels at Atmospheric Pressure (Micro Distillation Method). Small-volume variant for limited-sample situations.

**Downstream product specifications (call D86 normatively)**
- **ASTM D4814** (gasoline), **ASTM D1655** (jet A / A-1), **ASTM D975** (diesel), **ASTM D396** (fuel oils), **ASTM D6751** (B100 biodiesel), **ASTM D7467** (B6–B20 biodiesel blends), **ASTM D3699** (kerosene).

**International / parallel methods**
- **EN 590** — Automotive fuels — Diesel — Requirements and test methods (EU diesel parallel to D975). EN 590 references **EN ISO 3405** for the distillation method (the ISO mirror of D86).
- **EN 228** — Automotive fuels — Unleaded petrol — Requirements and test methods (EU gasoline parallel to D4814). Also references EN ISO 3405.
- **ISO 3405** — Petroleum and related products from natural or synthetic sources — Determination of distillation characteristics at atmospheric pressure. The ISO equivalent of D86; results are taken as broadly interchangeable for spec purposes.
- **IP 123** — Institute of Petroleum (UK) distillation method, harmonized with D86 and ISO 3405.

**Custody-transfer and volume-correction infrastructure**
- **API MPMS Chapter 11** (Physical Properties Data) — The D86 distillation curve is one input into refined-products volume-correction calculations (alongside density per D1298 / D4052 and temperature) for custody-transfer accounting; MPMS 11.1 / 11.2 / 11.4 carry the volume-temperature-density correction tables.

**Wiki cross-links**
- [O&G Standards catalog — ASTM D-Series](../sources/og-standards-astm-d-series.md) — multi-edition coverage manifest; identifies D86 as **#1 promotion candidate** in the D-Series slice with 9 catalog files across 5 distinct editions (2000–2004).
- Calc citation contract: `.claude/rules/calc-citation-contract.md` — frontmatter contract (`code_id`, `publisher`, `revision`) this page satisfies for fail-closed citation resolution.

## Sources

- **Source page (this wiki).** [O&G Standards catalog — ASTM D-Series](../sources/og-standards-astm-d-series.md). Catalog manifest for the entire ASTM D-Series slice; 10,361 documents at `/mnt/ace/O&G-Standards/ASTM/D-Series/`, of which 9 catalog files across 5 editions (2000, 2001, 2002, 2003, 2004) are D86. D86 is identified there as the #1 promotion candidate for `wiki/standards/<code-id>.md` (tied with D975 at 9 editions and the highest cross-reference fan-in across U.S. downstream fuel-quality specs).
- **Catalog manifest (read-only).** `/mnt/ace/O&G-Standards/_catalog.json` (catalog version 1.0.0, generated 2025-12-25) — filtered with `organization == 'ASTM' AND relative_path startswith 'ASTM/D-Series/' AND filename matches /\bD[\s_]?0*86\b/i` returns the 9 entries enumerated under *Edition history*.
- **Vendor PDFs (link-only; do NOT copy into git).** Latest editions in catalog under `/mnt/ace/O&G-Standards/ASTM/D-Series/D 86 - 04 *.pdf`. Per spinout 2026-05-05 governance and `.claude/rules/calc-citation-contract.md` deny-list, vendor-derivative PDFs remain at their `/mnt/ace/` location and are not republished here.
- **Publisher catalog.** ASTM International — D86 product page (search "D86" at <https://www.astm.org>; current designation D86-23 or later).
