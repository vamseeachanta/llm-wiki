---
title: "ASME B31.4 — Pipeline Transportation Systems for Liquids and Slurries (bounded summary)"
tags: ["asme", "standards", "pipeline", "metadata-only"]
added: 2026-05-02
last_updated: 2026-05-09
domain: engineering-standards
code_id: asme-b31-4
publisher: ASME
revision: "2009"
revision_source: "/mnt/ace/O&G-Standards/ASME/ASME B31.4/ASME B31.4 (2009) Pipeline Transportation Systems for Liquid Hydrocarbons and Other Liquids.pdf"
publisher_current_edition: "2022"
methodology_status: "stale-as-of-publisher-cycle"
verified_on: 2026-05-02
public_url: https://www.asme.org/codes-standards/find-codes-standards/b31-4-pipeline-transportation-systems-liquids-slurries
sources:
  - /mnt/ace/O&G-Standards/ASME/ASME B31.4/ASME B31.4 (2009) Pipeline Transportation Systems for Liquid Hydrocarbons and Other Liquids.pdf
extraction_policy: metadata-only
raw_copy_allowed: false
---

# ASME B31.4 — Pipeline Transportation Systems for Liquids and Slurries (bounded summary)

## Scope

ASME B31.4 prescribes engineering requirements for piping systems transporting liquid hydrocarbons (crude oil, condensate, refined petroleum products), liquid alcohols, liquid anhydrous ammonia, carbon-dioxide, and slurries between producers, tank farms, plants, terminals, refineries, and delivery points. It addresses design pressure, materials, fabrication, examination, testing, inspection, operation, and maintenance for the in-scope piping. Coverage starts at the pipeline-side outlet flange of the producing-facility / tank-farm / plant boundary and ends at the receiving-facility inlet flange; piping inside the plant fence is the scope of ASME B31.3 (Process Piping). The companion code on the gas-transportation side is ASME B31.8 (Gas Transmission and Distribution Piping Systems); B31.4 + B31.8 together cover the universe of onshore hydrocarbon-transportation pipelines under U.S.-jurisdiction practice.

## Revision history

- **B31 family origin (1935)** — The original *Code for Pressure Piping* covered all pressure-piping scopes in one ANSI document.
- **B31.4 separation** — Liquid-pipeline transportation carved out from the unified B31 code as long-distance crude-oil and refined-product pipeline construction grew in mid-20th-century North America.
- **2009 edition** — On-disk reference revision (`/mnt/ace/O&G-Standards/ASME/ASME B31.4/ASME B31.4 (2009) Pipeline Transportation Systems for Liquid Hydrocarbons and Other Liquids.pdf`); published under the title *Pipeline Transportation Systems for Liquid Hydrocarbons and Other Liquids*.
- **Title change to "Liquids and Slurries"** — modern editions broadened the title to *Pipeline Transportation Systems for Liquids and Slurries*, formalising the long-standing practical scope that included slurry pipelines (mineral concentrate, coal-water, etc.).
- **2012 / 2016 / 2019 / 2022 editions** — Modern publication cycle on roughly a 3-4 year cadence; the 2022 edition is the currently active publisher edition. Users emitting calc citations against current projects should re-pin to the publisher's currently active edition. The on-disk 2009 artifact lags by approximately 13 years.

## Key sections

B31.4 is organised on a chapter structure parallel to the B31 family:

- **Chapter I — Scope and Definitions** — applicability, design conditions, fluid-service definitions, designer responsibility.
- **Chapter II — Design** — design pressure, hoop-stress design (`S_h = (P × D) / (2 × t)` capped against `F × E × T × SMYS`), longitudinal-stress check, combined-stress check, occasional loads (thermal expansion, water hammer, surge, seismic), pipe-support and anchor design.
- **Chapter III — Materials** — listed line-pipe specifications (API 5L PSL 1 / PSL 2 grades), low-temperature requirements, sour-service material selection cross-linking to AMPP MR0175.
- **Chapter IV — Dimensional Requirements** — dimensional standards for fittings, flanges, valves (ASME B16 family).
- **Chapter V — Construction, Welding, and Assembly** — welding qualification (API 1104), construction methods, inspection of welds, examination percentages.
- **Chapter VI — Inspection, Examination, and Testing** — hydrostatic test pressure (typically 1.25 × MAOP for liquid pipelines), test duration, leak-testing, pre-commissioning inspection.
- **Chapter VII — Operation and Maintenance Procedures** — operating procedures, integrity management programme requirements, in-service inspection, repair and replacement.
- **Chapter VIII / IX (Service-specific)** — Offshore liquid pipelines (Chapter IX in modern editions) and CO2-pipeline-specific requirements.
- **Mandatory and Non-Mandatory Appendices** — material-allowable-stress sources, supplementary references, sample calculations.

### Design factor F vs B31.8 class-location framework

A core distinction between B31.4 and B31.8: **B31.4 uses a uniform design factor `F` (typically 0.72) for liquid-pipeline hoop stress** rather than the population-density-driven Class-Location-driven design-factor scaling that B31.8 applies for gas pipelines. The design-factor difference reflects the difference in failure-mode consequence — gas-pipeline rupture produces ignition-source-and-thermal-radiation public-safety hazards that scale with population density (driving B31.8 Class 1 / 2 / 3 / 4 location-driven F = 0.72 / 0.60 / 0.50 / 0.40), while liquid-pipeline rupture produces environmental-spill hazards that are managed primarily through integrity-management programs and high-consequence-area (HCA) overlays under 49 CFR 195 rather than through location-driven design-factor scaling.

### Flexibility analysis

B31.4 includes a flexibility-analysis framework conceptually parallel to B31.3 — thermal-expansion stress, displacement-stress range, and SIF-based fitting-stress evaluation — but with the B31.4-specific allowable-stress framework keyed to API 5L SMYS rather than to ASME BPVC Section II Part D listed-material allowable stresses. The practical flexibility-analysis output drives anchor and pipe-support placement, river-crossing free-span design, and buried-pipe thermal-expansion management.

## Practitioner application

In practice, ASME B31.4 is the cited basis for:

- **Liquid-pipeline new-construction design** — pipeline operators (Enterprise, Energy Transfer, Plains, Marathon, Phillips 66, Williams, Enbridge, Kinder Morgan, etc.) cite B31.4 as the design-code basis on liquid-transmission-pipeline projects; the EPC contractors (Quanta, Primoris, Bechtel, etc.) build to B31.4 as the master design code.
- **Hoop-stress and longitudinal-stress design** — calc-side stress checks consume API 5L SMYS in the B31.4 design equation; the 0.72 design factor governs minimum wall thickness.
- **Hydrostatic-test pressure setting** — the pre-commissioning hydrostatic test is set at 1.25 × MAOP for liquid pipelines per B31.4 (vs B31.8 gas-pipeline hydrostatic-test rules), with test duration and acceptance criteria specified in Chapter VI.
- **Integrity management programmes** — B31.4 Chapter VII operations-and-maintenance requirements integrate with API 1160 (Managing System Integrity for Hazardous Liquid Pipelines) and the U.S. DOT 49 CFR 195 integrity management framework.
- **Regulatory consequence-tier overlays** — High-Consequence Area (HCA) overlays under 49 CFR 195.452 add stricter integrity-assessment intervals and reassessment requirements on top of the baseline B31.4 design / operate framework.

## Industry adoption

- **U.S. DOT 49 CFR Part 195** — Federal pipeline-safety regulations for hazardous-liquid pipelines incorporate ASME B31.4 by reference as the design-code basis for newly constructed transmission and gathering pipelines.
- **Canadian CSA Z662** — Canadian *Oil and gas pipeline systems* code is the Canadian counterpart to combined B31.4 / B31.8; it incorporates substantively similar liquid-pipeline rules and accepts API 5L line-pipe specifications.
- **Operators and EPCs** — pipeline owners and EPC contractors cite B31.4 as the design code on essentially all U.S.-jurisdiction liquid-transmission-pipeline new-construction projects.
- **Offshore liquid pipelines** — for offshore liquid-pipeline scope, B31.4 Chapter IX (and the companion API RP 1111 for limit-state-design alternative) governs; DNV-ST-F101 is the international competitor for offshore pipeline-system design when U.S. jurisdiction does not apply.
- **CO2 pipelines** — the modern editions explicitly cover dense-phase / supercritical CO2 pipelines, supporting the rapidly-growing CCUS-pipeline market.

## Why this page exists

Resolver target for digitalmodel `Citation` instances per `.claude/rules/calc-citation-contract.md`. Contains no clause text, no formulas, and no tables from the source. Downstream callers wire B31.4 hoop-stress and longitudinal-stress constants through this page rather than parsing the source PDF. Calc-side modules cite this code at high frequency for liquid-pipeline stress checks (17 internal references observed in `digitalmodel/src/`). The on-disk 2009 artifact lags the publisher's currently active 2022 edition by approximately 13 years; calc callers should treat the on-disk artifact as **stale-as-of-publisher-cycle** and re-pin to the current edition before emitting design-pressure or design-stress citations on active projects.

## Where to find the full text

- Raw PDF: `/mnt/ace/O&G-Standards/ASME/ASME B31.4/ASME B31.4 (2009) Pipeline Transportation Systems for Liquid Hydrocarbons and Other Liquids.pdf` (read-only, vendor-derivative; do not copy into git per #2482)
- Publisher catalog: https://www.asme.org/codes-standards/find-codes-standards/b31-4-pipeline-transportation-systems-liquids-slurries
- Internal callers: `digitalmodel/src/digitalmodel/` modules referencing `ASME B31.4` / `ASMEB314` symbols

## Cross-references

- [[asme-b31-3]] — process-piping sister code; B31.3 starts at the plant-fence inlet flange where B31.4 ends
- [[asme-b31-8]] — gas-pipeline sister code; B31.4 + B31.8 partition the U.S. onshore-pipeline-transportation universe by fluid phase
- [[asme-bpvc-ii-d]] — material allowable stresses sourced upstream
- [[api-spec-5l]] — line-pipe material specification consumed by B31.4 (SMYS in the hoop-stress equation)
- [[api-rp-1111]] — offshore hydrocarbon pipelines, limit-state-design alternative companion
- [[ampp-mr-0175-pt1]] — sour-service material selection (cross-linked for sour-hydrocarbon-pipeline material qualification)
- [Calc citation contract](../../../../../.claude/rules/calc-citation-contract.md)

## Cross-References

- **Cross-wiki (maritime-law)**: [MARPOL 73/78](../../../maritime-law/wiki/standards/marpol-73-78.md) — **bidirectional bridge**: ASME B31.4 (Pipeline Transportation Systems for Liquids and Slurries) governs design, construction, inspection, and operation of crude-oil, refined-product, and slurry pipelines including offshore liquid pipelines under Chapter IX (subsea-tieback flowlines, export trunklines, FPSO-to-shore pipelines). **Pipeline-integrity failures** — internal/external corrosion, third-party mechanical damage, fatigue cracking from pressure cycling, manufacturing-defect propagation, and stress-corrosion cracking — cause **oil-pollution incidents** regulated under **MARPOL Annex I** when releases reach the marine environment from offshore-pipeline scope or shore-based pipelines discharging to navigable waters. B31.4's design-pressure factors (`F = 0.72` for liquid pipelines), class-location-equivalent wall-thickness requirements, post-construction hydrotest acceptance (1.25 × MAOP), and Chapter VII operations-and-maintenance integrity-management programme feed directly into **pollution-prevention compliance analysis** under MARPOL Annex I survey, IOPP-certificate, and casualty-reporting regimes. **Sister bridge** to W157's API RP 571 ↔ MARPOL pairing: RP 571 catalogues post-incident damage mechanisms diagnosed during MARPOL Annex I casualty investigations; **B31.4 supplies the pre-incident design-prevention envelope** whose non-conformance the RP 571 mechanisms expose. Use the pairing for offshore-pipeline casualty digests linking design-code non-conformance to MARPOL Annex I reportable-release thresholds.
