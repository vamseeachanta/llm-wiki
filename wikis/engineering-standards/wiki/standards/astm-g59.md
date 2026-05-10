---
title: "ASTM G59 — Potentiodynamic Polarization Resistance Measurements (LPR)"
slug: astm-g59
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
code_id: astm-g59
publisher: ASTM
revision: latest
tags:
  - astm
  - g-series
  - corrosion
  - polarization-resistance
  - lpr
  - electrochemistry
sources:
  - ../sources/og-standards-astm-g-series.md
extraction_policy: metadata-only
raw_copy_allowed: false
---

# ASTM G59 — Standard Test Method for Conducting Potentiodynamic Polarization Resistance Measurements

> Bounded metadata-only standards page. Per llm-wiki spinout governance (2026-05-05), vendor PDFs are not copied into this repo; this page records only publisher facts and a domain-knowledge scope description.
> **code_id:** `astm-g59` &nbsp;•&nbsp; **publisher:** ASTM International (Committee G01 — Corrosion of Metals; Subcommittee G01.11 on Electrochemical Measurements in Corrosion Testing) &nbsp;•&nbsp; **revision:** latest publisher edition (the on-disk catalog holds G59-97 base and G59-97(R03) reapproval — see Edition history below).

## Scope

ASTM G59 prescribes the **procedure for conducting Linear Polarization Resistance (LPR) measurements** on metallic specimens in a conductive electrolyte. The method drives the working electrode through a small-amplitude potentiodynamic sweep symmetric about the open-circuit potential (OCP) and extracts the **polarization resistance `R_p`** (units of Ω·cm² when the slope is normalized by the working-electrode exposed area) from the slope of the current-density-vs-potential curve at OCP.

`R_p` is then combined with the anodic and cathodic Tafel slopes (`b_a`, `b_c`) via the **Stern-Geary equation** to yield an **instantaneous corrosion-current density `i_corr`** without destroying the specimen. This is the foundational laboratory workflow that underwrites every modern online corrosion-monitoring probe deployed in oil-and-gas, refining, water-treatment, and power-generation service.

The substrate scope of G59 covers four areas:

- **Apparatus.** A three-electrode cell — working electrode (WE, the specimen under test), counter electrode (CE, typically platinum or graphite of larger area than the WE), and reference electrode (RE, e.g., SCE / Ag/AgCl / Cu/CuSO4) — driven by a potentiostat with millivolt-resolution potential control and current-measurement floor below the expected `i_corr`.
- **Specimen preparation.** Per [astm-g1](astm-g1.md) for metallographic surface state, masking, and dimensional accounting; the exposed working area must be known to ±a few percent because `R_p` is normalized to it.
- **Sweep protocol.** Pre-sweep OCP stabilization, then a small-amplitude potentiodynamic sweep typically **±10 to ±30 mV around `E_corr`** at a slow scan rate (commonly **0.1 to 0.6 mV/s**), with the span chosen near-symmetric so the linearity of the i–E response can be verified.
- **`R_p` extraction.** The slope `dE/di` evaluated at `E = E_corr` (zero net current) is `R_p`; the validity of the linearization rests on small-amplitude perturbation, IR-drop correction, and verified linearity of the i–E response over the swept window.

G59 is the **measurement-side companion to [astm-g3](astm-g3.md)** (which fixes sign conventions and reporting format) and to **[astm-g102](astm-g102.md)** (which converts `i_corr` into a penetration rate in mm/yr or mpy via Faraday's law). A G59 measurement reported without G3-conformant axis conventions and without G102's equivalent-weight argument is not directly comparable to mass-loss data from [astm-g31](astm-g31.md) / [astm-g1](astm-g1.md).

## Edition history

The local O&G-Standards catalog at `/mnt/ace/O&G-Standards/ASTM/G-Series/` holds **two G59 PDFs** corresponding to the 1997 base and its 2003 reapproval:

| Edition | Filename (catalog) | Catalog presence | Notes |
|---------|-------------------|------------------|-------|
| G59-97 | `G_59_-_97_RZU5LTK3RTE_.pdf` | 1 file | 1997 base revision |
| G59-97 (R03) | `G_59_-_97_R03_RZU5.pdf` | 1 file | 2003 reapproval of the 1997 method |
| G59 (current) | not on disk | — | The publisher-current ASTM G59 edition is later than the 2003 reapproval (further reapproval cycles have been issued); calc-callers needing the current edition must obtain it from the ASTM catalog |

The publisher-catalog year-token sweep done for the [og-standards-astm-g-series](../sources/og-standards-astm-g-series.md) source page recorded G59 with **2 editions** in the local catalog, matching the file rows above. The G59-97 base procedure has been remarkably stable — successive reapprovals carry editorial-only changes — but a calc-module author needing the current edition must consult the publisher's site rather than rely on the on-disk corpus.

## Key sections

The procedural anchors that define a G59-compliant LPR test (consult the on-disk PDFs for clause-exact text — this page records only the design-of-test substrate):

| Parameter | Value / specification |
|-----------|----------------------|
| Cell configuration | **Three-electrode cell**: working electrode (specimen), counter electrode (Pt or graphite, area ≥ WE area to avoid polarization at the CE), reference electrode (SCE / Ag/AgCl / Cu/CuSO4) — reference must be explicitly stated per [astm-g3](astm-g3.md). A **Luggin capillary** is recommended to position the RE close to the WE surface and minimize uncompensated solution resistance. |
| Potentiostat | Millivolt-resolution potential control; current measurement floor below the expected `i_corr` (typical low-rate alloys require sub-µA/cm² resolution). |
| Specimen prep | Per [astm-g1](astm-g1.md) — grit-finish to the specified surface state, dimensional accounting for exposed area (cm²), mask non-exposed faces with an inert coating that does not creep under the test electrolyte. |
| OCP stabilization | Hold at open circuit before the sweep until `E_corr` drift is below a defined threshold (commonly **mV/min-class drift** over ≥ minutes); a non-stabilized OCP biases the small-amplitude sweep and corrupts the `R_p` slope. |
| Sweep amplitude | **Small amplitude around OCP**, typically **±10 to ±30 mV** (the smaller the better for linearity, the larger the better for signal-to-noise). The span must be **near-symmetric** about `E_corr` so the linearity check is meaningful. |
| Scan rate | **0.1 to 0.6 mV/s** as the typical published range; slower is better for steady-state-like response, faster reduces solution-chemistry drift over the sweep. The chosen rate must be **reported** with the result. |
| `R_p` extraction | Slope `dE/di` evaluated at the zero-current crossing (`E = E_corr`), normalized by the working-electrode exposed area to give **Ω·cm²**. |
| Validity criteria | (a) **Linearity** of the i–E response across the swept window — non-linearity invalidates the slope-at-origin extraction; (b) **IR (ohmic-drop) correction** applied or solution resistance demonstrably small — uncompensated `R_s` adds directly to `R_p` and biases `i_corr` low; (c) **Surface-area normalization** documented; (d) Reference-electrode and reporting per G3. |
| Pre-test checks | Stable OCP, verified linearity in a trial small-amplitude sweep, optionally a parallel [astm-g106](astm-g106.md)-style EIS measurement to confirm the high-frequency intercept that fixes `R_s` for IR correction. |

## Stern-Geary application

The downstream conversion from `R_p` to corrosion-current density is the **Stern-Geary equation**:

```
i_corr = B / R_p              where  B = (b_a · b_c) / [2.303 · (b_a + b_c)]
```

- `i_corr` is in A/cm² when `R_p` is in Ω·cm² and `B` is in V (or mA/cm² and Ω·cm² and mV — units must track).
- `b_a` and `b_c` are the **anodic and cathodic Tafel slopes** in V/decade (extracted from a separate Tafel-region scan per [astm-g3](astm-g3.md) / G5, or assumed from tabulated values for well-characterized alloy-environment pairs).
- The Stern-Geary constant `B` collapses the two Tafel slopes into a single proportionality. Typical tabulated values used in field practice:
  - **B ≈ 26 mV** for actively corroding carbon steel (often stated as "26 mV" or "0.026 V" in field-monitoring vendor documentation).
  - **B ≈ 52 mV** for passive metals or alloys exhibiting cathodic-controlled diffusion-limited behavior.
  - Per-alloy and per-environment `B` values are tabulated by [astm-g102](astm-g102.md) for common engineering material–electrolyte combinations.

Once `i_corr` is in hand, the **penetration rate** follows from G102:

```
CR (mm/yr) = i_corr · K · EW / ρ
```

where `K` is the unit-conversion / Faraday constant (G102 supplies `K = 3.27 × 10⁻³` for `i_corr` in µA/cm² producing mm/yr), `EW` is the alloy equivalent weight (G102 supplies a per-alloy table including a mole-fraction-weighted method for multi-element alloys), and `ρ` is the alloy density in g/cm³. This is the bridge from a G59 measurement to a uniform-corrosion penetration rate that is directly comparable to a [astm-g31](astm-g31.md) / [astm-g1](astm-g1.md) mass-loss number.

## Field application

LPR is the foundation of **online corrosion-monitoring probes** widely deployed in production, refining, and water-treatment service:

- **Two-electrode and three-electrode probes** built around the G59 measurement principle are inserted at high-risk corrosion-monitoring locations (CMLs) — separator outlets, dehydration units, amine-treating circuits, sour-water strippers, and overhead condensers.
- The probe drives a small-amplitude potential perturbation across its electrodes at a fixed cadence (commonly minutes to hours) and reports `R_p` (and a derived `i_corr` or "corrosion-rate" channel) to the **plant DCS / historian**.
- The online rate channel is interpreted in the framework of **NACE / AMPP SP0775** *Preparation, Installation, Analysis, and Interpretation of Corrosion Coupons in Oilfield Operations* — which sets the engineering practice for how online probes and inserted coupons are co-deployed and how their data is read by the integrity engineer.
- The instantaneous (LPR-derived) and accumulated (coupon-derived) rates are **cross-validated** against each other; sustained disagreement is a known signal of localized attack, scale formation, or non-Faradaic mass loss (mechanical erosion, dissolution of an alloying element).
- For **damage-mechanism context** ([api-rp-571](api-rp-571.md)), the LPR rate channel is one of several inputs that feed the asset-integrity decision — alongside ultrasonic thickness, intelligent-pig data, and specimen autopsy.

A calc-module emitting an online-monitoring rate without a documented G59 → G102 chain (sweep amplitude, scan rate, IR-correction status, Stern-Geary `B`, equivalent weight, density) is not defensible at a regulator or classification-society audit.

## Cross-references

- [astm-g3](astm-g3.md) — *Standard Practice for Conventions Applicable to Electrochemical Measurements in Corrosion Testing.* **Foundation:** sign conventions, reference-electrode reporting, and the canonical i–E plotting format that G59 cites without re-defining. A G59 result quoted without G3-conformant conventions is silently ambiguous.
- [astm-g102](astm-g102.md) — *Standard Practice for Calculation of Corrosion Rates and Related Information from Electrochemical Measurements.* **Downstream:** consumes G59's `i_corr` and emits a penetration rate in mm/yr or mpy via Faraday's law with an equivalent-weight argument and a tabulated Stern-Geary `B` library.
- **ASTM G5** — *Standard Reference Test Method for Making Potentiodynamic Anodic Polarization Measurements.* The wide-range Tafel-scan reference test on Type 430 stainless; supplies the anodic and cathodic Tafel slopes that close the Stern-Geary `B` calculation when the alloy–environment pair is not in G102's table.
- **ASTM G106** — *Standard Practice for Verification of Algorithm and Equipment for Electrochemical Impedance Measurements.* **Complementary:** EIS supplies the high-frequency `R_s` intercept that fixes the IR-correction term for a G59 sweep, and supplies a small-signal `R_p` cross-check at zero-frequency.
- [astm-g1](astm-g1.md) — *Standard Practice for Preparing, Cleaning, and Evaluating Corrosion Test Specimens.* **Validation:** the mass-loss baseline that every G59-derived `i_corr` should be calibrated against on first use of an alloy–environment pair.
- [astm-g31](astm-g31.md) — *Standard Guide for Laboratory Immersion Corrosion Testing of Metals.* **Validation:** long-exposure mass-loss substrate that calibrates G59-derived rates; routinely run on a parallel coupon set in the same vessel.
- **NACE / AMPP SP0775** — *Preparation, Installation, Analysis, and Interpretation of Corrosion Coupons in Oilfield Operations.* The practice document that frames how online LPR probes (built on the G59 principle) and inserted coupons are co-deployed and read together at production CMLs.
- [api-rp-571](api-rp-571.md) — *Damage Mechanisms Affecting Fixed Equipment in the Refining Industry.* Damage-mechanism context for the integrity engineer reading the LPR rate channel; identifies which mechanisms (uniform CO2 corrosion, sour-service H2S attack, naphthenic-acid attack, MIC, etc.) the LPR signal is and is not sensitive to.
- [ampp-tm-0177](ampp-tm-0177.md) — *Laboratory Testing of Metals for Resistance to Sulfide Stress Cracking and Stress Corrosion Cracking in H2S Environments.* SSC tensile-style testing in sour environments; the H2S sour-service cousin to G59-conformant electrochemical work, often run on the same heat of material.
- Concept anchor: [corrosion-rate-measurement](../concepts/corrosion-rate-measurement.md) — landing page that names **G59 as the primary LPR method** in the electrochemical measurement column underneath G3 (conventions) and feeding G102 (rate calculation).
- [Calc citation contract](../../../../../.claude/rules/calc-citation-contract.md) — emit a `Citation(...)` whenever a calc module hard-codes a G59-derived `R_p`, a Stern-Geary `B` constant, an LPR-probe sweep protocol, or an IR-correction default.

## Sources

- [og-standards-astm-g-series](../sources/og-standards-astm-g-series.md) — parent source page for the ASTM G-Series slice of the local catalog; records the two-edition G59 presence, the catalog file paths, and the metadata-only extraction policy that scopes this standards page.
- Publisher catalog (current edition for purchase, registration required): https://www.astm.org/g0059-97r20.html (or the latest reapproval listing on `astm.org`).
- On-disk raw PDFs (vendor-derivative, do not copy into git per spinout 2026-05-05 governance):
  - `/mnt/ace/O&G-Standards/ASTM/G-Series/G_59_-_97_RZU5LTK3RTE_.pdf`
  - `/mnt/ace/O&G-Standards/ASTM/G-Series/G_59_-_97_R03_RZU5.pdf`
