---
title: "ASTM G5 — Standard Reference Test Method for Making Potentiodynamic Anodic Polarization Measurements (bounded resolver)"
slug: astm-g5
tags: ["astm", "g-series", "corrosion", "electrochemistry", "potentiodynamic", "polarization", "tafel", "test-method", "metadata-only"]
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
code_id: astm-g5
publisher: ASTM
revision: "G5-14e1 (publisher-current); local catalog holds G5-1994 (R2004)"
publisher_current_edition: "G5-14e1"
jurisdiction: "ASTM jurisdiction (US-origin, global adoption)"
instrument_type: test-method
supersedes: None
extraction_policy: metadata-only
raw_copy_allowed: false
sources:
  - ../sources/og-standards-astm-g-series.md
  - https://www.astm.org/g0005-14e01.html
public_url: https://www.astm.org/g0005-14e01.html
publisher_catalog_url: https://www.astm.org/
---

# ASTM G5 — Standard Reference Test Method for Making Potentiodynamic Anodic Polarization Measurements (bounded resolver)

> Bounded metadata-only standards page. Per llm-wiki spinout governance (2026-05-05), vendor PDFs are not copied into this repo; this page records only publisher facts and a domain-knowledge scope description. No clause text, scan-rate tables, reference-electrode offset values, or curve-shape reproductions are included.
> **code_id:** `astm-g5` &nbsp;•&nbsp; **publisher:** ASTM International (Committee G01 — Corrosion of Metals; Subcommittee G01.11 — Electrochemical Measurements in Corrosion Testing) &nbsp;•&nbsp; **revision:** G5-14e1 publisher-current; the local O&G-Standards catalog records G5 with one edition (1994 reapproved 2004 era).

## Scope

ASTM G5 is the **canonical reference test method** for executing a **potentiodynamic anodic polarization scan** in laboratory aqueous corrosion testing. It defines a fully prescriptive procedure — solution chemistry, specimen, electrode geometry, scan rate, reporting — applied to a **Type 430 ferritic stainless steel reference specimen in 1.0 N H2SO4 at 30 °C** so that any electrochemical-corrosion test rig can be **calibrated against a known-good polarization curve** before it is used to generate proprietary alloy data.

G5 is the canonical "Tafel scan" reference: it produces the active-passive-transpassive curve (anodic-up, log|i| on the X axis, per [astm-g3](astm-g3.md)) from which **Tafel slopes (b_a, b_c)**, **corrosion-current density i_corr**, **passivation potential E_pp**, **passive-current density i_p**, and **transpassive potential** are extracted. Once the test rig reproduces the G5 reference curve within the published tolerance, the same rig is trusted to characterize candidate alloys and environments. G5 thus operates simultaneously as a **rig-calibration standard** and the **procedural template** that virtually all in-house potentiodynamic procedures inherit.

The companion calculation-and-reporting standards [astm-g3](astm-g3.md) (conventions), [astm-g59](astm-g59.md) (LPR variant), [astm-g102](astm-g102.md) (rate calc), and [astm-g106](astm-g106.md) (EIS verification) form the natural cluster around G5: G3 sets the conventions, G5 defines the canonical scan, G59 gives the small-overpotential variant for in-service monitoring, G102 converts the result to engineering rate, and G106 is the AC-impedance complement.

## Revision history

- **Original publication** in the early ASTM G01 cycle as the rig-calibration reference for potentiodynamic polarization.
- **G5-94 (Reapproved 2004)** — recorded as the on-disk catalog edition for this G-series corpus (per [og-standards-astm-g-series](../sources/og-standards-astm-g-series.md), which lists G5 with one revision in the local catalog).
- **G5-14e1** — publisher-current edition incorporating editorial corrections; the technical procedure (Type 430 / 1 N H2SO4 / 30 °C / specified scan rate) has been stable across revision cycles.

## Key sections

The following are the procedural anchors that the practice prescribes (consult the on-disk PDF or publisher catalog for clause-exact text):

- **Specimen** — Type 430 ferritic stainless steel reference coupon at specified surface finish and area.
- **Electrolyte** — 1.0 N H2SO4 at 30 °C ± controlled tolerance, deaerated by N2 purge.
- **Cell** — three-electrode configuration with working, reference (saturated calomel SCE), and counter electrodes; Luggin capillary geometry for IR-drop minimization.
- **Pre-conditioning** — open-circuit-potential stabilization period and (in some variants) cathodic pre-polarization to reduce surface films before the scan.
- **Scan parameters** — start potential, end potential, scan direction (typically cathodic-to-anodic), and **scan rate** in mV/s (the prescribed rate is slow enough to approximate steady-state).
- **Reporting** — full polarization curve plotted per [astm-g3](astm-g3.md) conventions (E vs log|i|), reference-curve comparison metrics, and the standard reporting checklist (solution composition, temperature, dissolved-oxygen status, reference electrode, IR correction, scan rate).

## Practitioner application

- **Test-rig calibration** — every electrochemical-corrosion lab runs the G5 reference scan periodically (commissioning + scheduled re-verification) to establish that the potentiostat, cell, reference electrode, and control software produce the canonical Type 430 / 1 N H2SO4 curve within tolerance before any candidate-alloy work is reported.
- **Tafel-slope extraction** — the linear (in log|i|) portions of the anodic and cathodic branches give **b_a** and **b_c** for the Stern-Geary `B` constant used by [astm-g102](astm-g102.md) to convert [astm-g59](astm-g59.md) LPR R_p measurements into i_corr.
- **Active-passive screening** — the passivation potential E_pp, passive current density i_p, and the active-passive-nose current are the principal alloy-screening outputs. CRA candidates that exhibit a robust passive window and low passive current at the service environment are flagged for downstream pitting/crevice screening per [astm-g48](astm-g48.md).
- **Transpassive characterization** — the high-potential breakdown of the passive film gives the transpassive potential, relevant to pitting-resistance and trans-passive-dissolution-rate analyses.
- **Procedure template** — many in-house and project-specific potentiodynamic procedures inherit the G5 template (3-electrode cell, scan-rate guidance, reporting checklist) and substitute alternate electrolytes / specimen alloys / temperatures while keeping the G5 metrology backbone.

## Industry adoption

G5 is the **default rig-calibration reference** across academic, vendor, and industrial corrosion-testing labs that produce potentiodynamic data for offshore, refining, downstream, marine, and chemical-process applications. It is referenced from CRA-qualification programs (sour-service [ampp-mr-0175-pt3](ampp-mr-0175-pt3.md) / [iso-15156-3](iso-15156-3.md)), pitting-screening protocols ([astm-g48](astm-g48.md) consumers), corrosion-rate calc reports ([astm-g102](astm-g102.md) callers), and EIS verification programs ([astm-g106](astm-g106.md)). A polarization curve emitted without an upstream G5 calibration record is regularly flagged in reviewer comments at classification societies (DNV, ABS) and regulators (BSEE, HSE).

## Why this page exists

This page is the citation resolver target for `code_id = astm-g5` under `.claude/rules/calc-citation-contract.md`. W204 audit V9 surfaced `astm-g5` as the highest-traffic unmatched slug (4 broken-link instances) — referenced from [astm-g3](astm-g3.md), [astm-g102](astm-g102.md), [astm-g106](astm-g106.md), [astm-g1](astm-g1.md) Tafel extrapolation discussion, and the [electrochemical-corrosion](../concepts/electrochemical-corrosion.md) concept page passive-region anchor. The page anchors that link target without reproducing any clause text, scan parameters, or reference-curve numerical values.

## Where to find the full text

ASTM catalog (registration required for purchase): `https://www.astm.org/g0005-14e01.html`. The publisher-derivative full text is **not** stored in this repo per the vendor-derivative deny-list governance. Calc-citation callers resolve only against this page's frontmatter (`code_id`, `publisher`, `revision`); they do not require body text.

## Cross-references

- [astm-g3](astm-g3.md) — *Conventions Applicable to Electrochemical Measurements in Corrosion Testing.* Sign and axis conventions cited by every G5 plot; G5 cannot be interpreted without G3.
- [astm-g59](astm-g59.md) — *Conducting Potentiodynamic Polarization Resistance Measurements.* Small-overpotential LPR variant; G5's Tafel slopes feed the Stern-Geary `B` used by G59 → i_corr.
- [astm-g102](astm-g102.md) — *Calculation of Corrosion Rates from Electrochemical Measurements.* Converts G5-derived i_corr into engineering penetration / mass-loss rate via Faraday + equivalent-weight machinery.
- [astm-g106](astm-g106.md) — *Verification of Algorithm and Equipment for Electrochemical Impedance Measurements.* AC-complement to G5; both calibrate the same potentiostat hardware in different frequency regimes.
- [astm-g1](astm-g1.md) — *Preparing, Cleaning, and Evaluating Corrosion Test Specimens.* Mass-loss baseline that calibrates G5/G59/G102 electrochemical-derived rates.
- [astm-g48](astm-g48.md) — *Pitting and Crevice Corrosion in FeCl3.* Localized-corrosion follow-on screening for alloys flagged by G5 active-passive characterization.
- [electrochemical-corrosion](../concepts/electrochemical-corrosion.md) — concept anchor for the kinetics framework G5 measures (Butler-Volmer, mixed-potential, passivity).
- [corrosion-rate-measurement](../concepts/corrosion-rate-measurement.md) — concept anchor that places G5 in the measurement-methodology cluster (electrochemical column).
- [Calc citation contract](../../../../../.claude/rules/calc-citation-contract.md) — emit a `Citation(...)` whenever a calc module hard-codes a G5-derived reference Tafel slope, calibration scan-rate, or reference-curve tolerance value.

## Sources

- [og-standards-astm-g-series](../sources/og-standards-astm-g-series.md) — parent source page recording G5 with 1 edition in the local catalog and the metadata-only extraction policy.
- Publisher catalog (current edition for purchase, registration required): https://www.astm.org/g0005-14e01.html
