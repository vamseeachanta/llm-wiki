---
title: "ASME BPVC Section VIII Division 1 — Rules for Construction of Pressure Vessels (bounded summary)"
tags: ["asme", "bpvc", "standards", "pressure-vessels", "metadata-only"]
added: 2026-05-02
last_updated: 2026-05-09
domain: engineering-standards
code_id: asme-bpvc-viii-1
publisher: ASME
revision: "2010"
revision_source: "/mnt/ace/O&G-Standards/ASME/ASME VIII/ASME VIII DIV 1 (2010) Rules for Construction of High Pressure Vessels.pdf"
publisher_current_edition: "2023"
methodology_status: "unknown"
verified_on: 2026-05-02
public_url: https://www.asme.org/codes-standards/bpvc-standards
sources:
  - /mnt/ace/O&G-Standards/ASME/ASME VIII/ASME VIII DIV 1 (2010) Rules for Construction of High Pressure Vessels.pdf
extraction_policy: metadata-only
raw_copy_allowed: false
---

# ASME BPVC Section VIII Division 1 — Rules for Construction of Pressure Vessels (bounded summary)

## Scope

BPVC Section VIII Division 1 provides **design-by-rule** requirements for the construction of unfired pressure vessels operating above the lower pressure threshold (typically 15 psig / ~103 kPag internal, with a parallel external-pressure scope) and below the high-pressure boundary that delegates to Section VIII Division 3. Coverage includes minimum-thickness rules for shells, heads, nozzles, openings, reinforcement, supports, and bolted flanged connections, together with materials, fabrication, examination, testing, inspection, and stamping requirements for the in-scope vessels. Division 1 is the historical default for refining, petrochemical, chemical-process, oil-and-gas, and power-plant pressure-vessel construction worldwide; the design rules are formula-and-chart based and are paired with material allowable stresses sourced upstream from Section II Part D.

## Revision history

- **1914** — Inaugural BPVC ("Code-1") published in response to Brockton, MA shoe-factory boiler explosion (1905) and ensuing state-level legislation; established the multi-section structure and the Code-Stamp regime.
- **Section VIII first issued (1925)** — Pressure-vessel rules separated from boiler-section content; the design-by-rule formula-based methodology that Division 1 carries today traces to this period.
- **1968 — Division 2 introduced** — Alternative design-by-analysis route published for vessels where the Division 1 formula-based design is overly conservative or geometrically inapplicable.
- **1997 — Division 3 introduced** — High-pressure scope (typically above ~10,000 psi / ~70 MPa) split from Division 1 / Division 2 with its own fatigue and fracture-mechanics rules.
- **1999 — Mandatory Appendix 22** — Pressure-vessels-of-non-circular-cross-section formalised.
- **Biennial cycle (1986–2017)** — BPVC issued every two years (1986, 1989, …, 2015, 2017).
- **2019 onward** — Switched to a **two-year cycle anchored on odd-numbered years** (2019, 2021, 2023, 2025); with addenda discontinued in favour of integrated republication.
- **2023 edition** — Current published edition at the time the on-disk 2010 artifact's `publisher_current_edition` field was last verified (2026-05-02).

## Key sections

Division 1 is organised as a part-and-paragraph structure with mandatory and non-mandatory appendices.

- **Subsection A — General Requirements (Part UG)** — universal scope, design pressure / temperature, materials qualification reference into Section II, joint-efficiency factor `E`, allowable stress sourced from Section II Part D, design-by-rule formulas for cylindrical and spherical shells, formed and flat heads, nozzle reinforcement (area-replacement method), inspection and stamping.
- **Subsection B — Requirements for Methods of Fabrication of Pressure Vessels** — welded fabrication (Part UW), brazed fabrication (Part UB), forged construction (Part UF). Welding qualification cross-refers to Section IX.
- **Subsection C — Requirements for Classes of Materials** — carbon steel (UCS), non-ferrous (UNF), high-alloy steel (UHA), heat-treated steels (UHT), cast iron (UCI), cast nodular iron (UCD), low-temperature service (ULT), layered construction (ULW), ferritic steels with tensile properties enhanced by heat treatment (UHT).
- **Mandatory Appendices** — bolted flange design (Mandatory Appendix 2), Charpy-V impact-testing exemption-curve methodology (Mandatory Appendix 6), rules for stayed and braced flat plates (Mandatory Appendix 13), rules for jacketed vessels (Mandatory Appendix 9), rules for pressure-vessels-of-non-circular-cross-section (Mandatory Appendix 13/22 depending on edition), tube-to-tubesheet expansion (Mandatory Appendix 26), inspection and stamping (Mandatory Appendix 1 historically).
- **Non-Mandatory Appendices** — design considerations and good-practice guidance that supplements but does not over-rule the mandatory rules (Appendix A series).

The exact Mandatory-Appendix numbering shifts across editions; the on-disk 2010 numbering is not guaranteed to match the 2023 cycle.

## Practitioner application

In practice, Division 1 is the cited basis for:

- **Minimum-thickness calcs** for cylindrical-shell, spherical-shell, ellipsoidal-head, torispherical-head, flat-head, and conical-section pressure-vessel components — formula-based with allowable stress from Section II Part D and joint-efficiency from the welding examination class.
- **Nozzle reinforcement** by the area-replacement method for radial and oblique nozzles in shells and heads.
- **Bolted-flange design** via Mandatory Appendix 2 (Taylor-Forge methodology) for custom-flange geometries not covered by ASME B16.5 / B16.47 standard ratings.
- **MAWP determination** (Maximum Allowable Working Pressure) for new-construction stamping and for in-service re-rating under API 510.
- **Documentation deliverables** — Manufacturer's Data Report (Form U-1 / U-1A), Code-Stamp certification, and the documentation pack that authorised inspectors require for `U`-stamp issuance.

The choice between Division 1 (design-by-rule), Division 2 (design-by-analysis), and Division 3 (high-pressure) is itself an upstream engineering decision: Division 1 is the workhorse for moderate-pressure refining and petrochemical service; Division 2 is selected when the geometry or pressure demands a finite-element-grounded stress check, when fatigue is a credible failure mode, or when the lower design-margin (Division 2 Class 1 / Class 2 alternative rules) makes economic sense for the vessel weight; Division 3 is reserved for pressures above the ~10,000 psi / ~70 MPa boundary.

## Code cases and interpretations

ASME maintains two formal mechanisms for code evolution between published editions:

- **Code Cases** — alternative requirements that the Code accepts as equivalent to a published rule; commonly used to authorise newly-qualified materials, alternative non-destructive examination techniques, or alternative design / fabrication approaches before the next edition incorporates them. Code Cases are issued on a rolling basis and published in standalone Code-Case books.
- **Interpretations** — formal answers to inquiries on the meaning of a published rule; binding for the inquirer's context but not a substitute for a Code Case when the question is "may I do something different."

Both mechanisms are essential context for any Division 1 calc that pre-dates the on-disk artifact's edition; a stale calc may rely on a Code Case that has since been incorporated, withdrawn, or superseded.

## Industry adoption

- **Refining + petrochemical (global)** — Division 1 is the design substrate of record for fired-heater convection sections (where pressure parts not in Section I scope), reactors, distillation columns, knock-out drums, accumulators, and most static pressure equipment.
- **Oil-and-gas upstream + midstream** — separators, scrubbers, glycol contactors, and amine columns are typically Division 1; large NGL-fractionation columns may be Division 2.
- **Power generation** — most BOP (balance-of-plant) pressure equipment that is not boiler-proper (Section I scope) is Division 1.
- **Class-society delegation** — IACS unified requirements and individual class-society pressure-vessel rules (ABS, DNV, LR, BV, ClassNK) routinely import Division 1 by reference for shipboard unfired pressure vessels.
- **Regulatory acceptance** — Division 1 is named in U.S. state-level pressure-vessel laws, in the National Board Inspection Code (NBIC) for in-service inspection authority, and in the Canadian provincial CSA B51 regime; international acceptance is broad (Mexico, Brazil, Middle East, Asia-Pacific).

## Why this page exists

Resolver target for digitalmodel `Citation` instances per `.claude/rules/calc-citation-contract.md`. Contains no clause text, no formulas, and no tables from the source. Downstream callers wire VIII Division 1 minimum-thickness and joint-efficiency constants through this page rather than parsing the source PDF. The combined `ASME VIII` token is referenced 33 times across `digitalmodel/src/` (shared with Division 2). **Metadata-only** per spinout 2026-05-05 governance: no clause text, design formulas, allowable-stress tables, joint-efficiency tables, or appendix content reproduced.

## Where to find the full text

- Raw PDF: `/mnt/ace/O&G-Standards/ASME/ASME VIII/ASME VIII DIV 1 (2010) Rules for Construction of High Pressure Vessels.pdf` (read-only, vendor-derivative; do not copy into git per #2482)
- Publisher catalog: https://www.asme.org/codes-standards/bpvc-standards
- Internal callers: `digitalmodel/src/digitalmodel/` modules referencing `ASME VIII` / `ASME_VIII_DIV1` symbols

## Cross-references

- [[asme-bpvc-viii-2]] — alternative design-by-analysis route for moderate-to-high pressure vessels where formula-based design is uneconomic or geometrically inapplicable
- [[asme-bpvc-viii-3]] — high-pressure division (above ~10,000 psi / ~70 MPa) with its own fatigue + fracture-mechanics rules
- [[asme-bpvc-ii-d]] — material allowable stresses sourced upstream
- [[asme-bpvc-ix]] — welding qualification basis
- [[api-510]] — pressure-vessel in-service inspection code that uses Division 1 design rules as the new-construction basis and authorises RBI per RP 580 / RP 581 for alternative inspection intervals
- [[api-std-579]] — fitness-for-service evaluation invoked when in-service findings exceed Division 1 acceptance limits
- [Calc citation contract](../../../../../.claude/rules/calc-citation-contract.md)

## Cross-wiki bridges

- [SOLAS 1974](../../../maritime-law/wiki/standards/solas-1974.md)
  (maritime-law) — **bidirectional bridge**: BPVC Section VIII Division 1
  is the design-by-rule code that flag-state inspection regimes and
  IACS class-society rules import by reference for shipboard unfired
  pressure vessels under SOLAS Ch. II-1 (machinery installations) and
  Ch. II-2 (fire-protection-related pressure systems). For gas
  carriers under SOLAS Ch. VII Part C, the IGC Code Ch.5 process
  pressure vessels and Ch.8 vent / PRV systems likewise lean on
  Section VIII (Div. 1 and Div. 2) for cargo-tank, knock-out drum,
  and reliquefaction-plant pressure-vessel construction. SOLAS
  itself carries no numeric design rules for unfired pressure
  vessels — Section VIII is the engineering-standards substrate the
  treaty regime delegates to.
