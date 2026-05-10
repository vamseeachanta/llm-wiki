---
title: "ASTM G3 — Conventions for Electrochemical Measurements in Corrosion Testing"
slug: astm-g3
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
code_id: astm-g3
publisher: ASTM
revision: latest
tags:
  - astm
  - g-series
  - corrosion
  - electrochemistry
  - conventions
  - polarization
sources:
  - ../sources/og-standards-astm-g-series.md
extraction_policy: metadata-only
raw_copy_allowed: false
---

# ASTM G3 — Standard Practice for Conventions Applicable to Electrochemical Measurements in Corrosion Testing

> Bounded metadata-only standards page. Per llm-wiki spinout governance (2026-05-05), vendor PDFs are not copied into this repo; this page records only publisher facts and a domain-knowledge scope description.
> **code_id:** `astm-g3` &nbsp;•&nbsp; **publisher:** ASTM International (Committee G01 — Corrosion of Metals; Subcommittee G01.11 on Electrochemical Measurements in Corrosion Testing) &nbsp;•&nbsp; **revision:** latest publisher edition (the on-disk catalog holds G3-89(R99) — see Edition history below).

## Scope

ASTM G3 defines the **sign conventions, graphical formats, and terminology** that every other electrochemical-corrosion test method in the G-series and the broader corrosion-engineering literature is meant to obey. It does not by itself specify a test procedure — instead, it is the **definitional substrate** that makes results from G5, G59, G61, G102, and G106 (and from any laboratory or vendor reporting that claims ASTM compatibility) directly comparable.

The practice covers four substrate areas:

- **Sign conventions for current.** Anodic current (oxidation, metal dissolution) is **positive**; cathodic current (reduction, e.g., hydrogen evolution or oxygen reduction) is **negative**. This is the "American convention" and is enforced uniformly by G3 across all G-series electrochemical methods.
- **Sign conventions for potential.** Potential is reported **versus a specified reference electrode** (saturated calomel SCE, standard hydrogen SHE, silver/silver-chloride Ag/AgCl, or copper/copper-sulfate Cu/CuSO4). The reference electrode must be explicitly stated; conversions between scales are tabulated in G3.
- **Graphical formats.** The **canonical polarization curve** plots potential **E** on the linear Y axis (anodic-up — increasing potential goes upward) and **log|i|** (decadal logarithm of absolute current density) on the X axis. Anodic and cathodic branches are plotted as separate limbs meeting at the open-circuit potential.
- **Terminology.** Defines `E_corr` (corrosion potential = open-circuit potential, OCP), `i_corr` (corrosion current density), `b_a` and `b_c` (anodic and cathodic Tafel slopes), `R_p` (polarization resistance), passive-region descriptors, and pitting/repassivation potentials, in a vocabulary that downstream methods then cite without re-defining.

G3 is the **provenance backbone** for any calc-module that converts a measured polarization curve, LPR sweep, or EIS spectrum into an engineering corrosion rate. A calc that emits an `i_corr` value without a G3-conformant axis convention and reference-electrode declaration is, in practice, ambiguous to peer reviewers.

## Edition history

The local O&G-Standards catalog at `/mnt/ace/O&G-Standards/ASTM/G-Series/` holds **one G3 PDF**:

| Edition | Filename (catalog) | Catalog presence | Notes |
|---------|-------------------|------------------|-------|
| G3-89(R99) | `G_3_-_89_R99_RZM_.pdf` | 1 file | 1989 revision, reapproved 1999 |
| G3 (current) | not on disk | — | The publisher-current ASTM G3 edition is later than the 1999 reapproval (multiple reapprovals have been issued in the post-2000 cycle); calc-callers needing the current edition must obtain it from the ASTM catalog |

The publisher catalog year-token sweep done for the [og-standards-astm-g-series](../sources/og-standards-astm-g-series.md) source page recorded G3 with **1 edition** in the local catalog, matching the file row above.

## Key conventions

- **Anodic current is positive** (oxidation, metal-into-solution); **cathodic current is negative** (reduction, e.g., 2H+ + 2e- → H2 or O2 + 2H2O + 4e- → 4OH-). Reversing this convention silently flips Tafel-slope signs and is a recurring source of `i_corr` reporting errors in non-ASTM-conformant data.
- **Potential is reported versus a specified reference electrode.** Always state the reference (SCE, SHE, Ag/AgCl, Cu/CuSO4). Standard-condition offsets at 25 °C: SCE ≈ +0.241 V vs SHE; saturated Ag/AgCl ≈ +0.197 V vs SHE; saturated Cu/CuSO4 ≈ +0.318 V vs SHE. Quoting `E_corr` without the scale is uninterpretable.
- **Polarization curves use potential on the Y axis (linear, anodic-up) and log|i| on the X axis (decadal log scale).** Anodic-up means increasing E (more noble) goes upward; this is the format consumers of G5 and G59 expect.
- **Anodic and cathodic branches are reported separately**; **Tafel slopes (b_a, b_c)** are extracted from the linear (in log|i|) portions of each branch, typically over at least one decade of current density displaced from `E_corr` to avoid mass-transport and polarization-resistance distortion near the origin.
- **Open-circuit potential (OCP) = `E_corr`**; the **corrosion-current density `i_corr`** is extracted at the intersection of the back-extrapolated Tafel lines (Tafel-extrapolation method) or, for small-overpotential sweeps, from polarization resistance `R_p` via the Stern-Geary equation `i_corr = B / R_p` where `B = (b_a · b_c) / [2.303 · (b_a + b_c)]`. The Stern-Geary calculation is the bridge to ASTM G102 corrosion-rate output.

## Reporting checklist

Every electrochemical-corrosion result that claims G3-conformant provenance should record:

- **Solution composition** (electrolyte chemistry, concentrations, pH, additive package).
- **Temperature** (°C, with control tolerance).
- **Flow / hydrodynamic state** (stagnant, stirred, rotating-disk RPM, flow loop velocity).
- **Dissolved-oxygen status** (aerated / deaerated / N2-purged / Ar-purged) — oxygen reduction is a major cathodic reaction and changes `i_corr` by orders of magnitude.
- **Reference electrode** (SCE / SHE / Ag-AgCl / Cu-CuSO4) and any salt-bridge / Luggin-capillary geometry.
- **Working-electrode area** (cm²) and surface preparation (grit, passivation, masking).
- **Scan rate** (mV/s) for potentiodynamic sweeps; **frequency range** for EIS.
- **IR (ohmic-drop) correction** — applied or not; method (positive-feedback compensation, post-test correction from EIS-measured solution resistance, or current-interrupt).
- **Pre-conditioning history** — duration of OCP stabilization before the sweep, any cathodic pre-polarization, and prior exposure history of the specimen.

A reported polarization curve missing any of these fields is not reproducible and cannot be cleanly cited by a downstream calc.

## Why these conventions matter

Different journals, vendor data sheets, and earlier (pre-G3) standards have historically reversed the current sign, plotted log|i| on the Y axis, or quoted `E_corr` without a reference electrode — making cross-source comparisons silently invalid. G3 is the **unifying reference** that downstream methods in the G-series cite by name:

- **G5** (potentiodynamic anodic polarization for stainless steels) cites G3 for axis conventions and Tafel-slope extraction.
- **G59** (linear polarization resistance, LPR) cites G3 for the small-overpotential sweep convention and the Stern-Geary linkage to `R_p`.
- **G102** (corrosion-rate calculation from electrochemical data) cites G3 for the `i_corr` provenance that its mass-loss-equivalent rate calc consumes.
- **G106** (EIS verification) cites G3 for the impedance-plot conventions and the OCP reporting requirement.

For calc-module authors: a numeric corrosion rate emitted without a G3-conformant upstream chain (axis convention + reference electrode + Tafel-region selection + IR correction) cannot pass peer review at a regulator (BSEE, HSE) or at a classification-society design audit (DNV, ABS, BV). G3 is the foundational citation that turns electrochemical data into defensible engineering output.

## Cross-references

- [astm-g5](astm-g5.md) — *Standard Reference Test Method for Making Potentiodynamic Anodic Polarization Measurements.* The canonical Tafel-scan procedure on Type 430 stainless reference material; cites G3 for axis and sign conventions.
- [astm-g59](astm-g59.md) — *Standard Test Method for Conducting Potentiodynamic Polarization Resistance Measurements.* The LPR procedure that delivers `R_p` for Stern-Geary `i_corr` extraction; G3 anchors the small-overpotential sweep convention.
- [astm-g102](astm-g102.md) — *Standard Practice for Calculation of Corrosion Rates and Related Information from Electrochemical Measurements.* Converts G3-conformant `i_corr` into engineering penetration rate (mm/yr or mpy) via Faraday's law with an equivalent-weight argument; the bridge from G3/G5/G59 measurements to mass-loss-equivalent rate.
- [astm-g106](astm-g106.md) — *Standard Practice for Verification of Algorithm and Equipment for Electrochemical Impedance Measurements.* EIS practice; cites G3 for impedance-plot conventions (Nyquist and Bode formats) and OCP reporting.
- [astm-g1](astm-g1.md) — *Standard Practice for Preparing, Cleaning, and Evaluating Corrosion Test Specimens.* Mass-loss baseline that every G3-derived `i_corr` should be calibrated against before being trusted as an in-situ rate sensor.
- [astm-g31](astm-g31.md) — *Standard Guide for Laboratory Immersion Corrosion Testing of Metals.* Long-exposure mass-loss substrate that calibrates electrochemical-derived rates.
- [ampp-tm-0177](ampp-tm-0177.md) — *Laboratory Testing of Metals for Resistance to Sulfide Stress Cracking and Stress Corrosion Cracking in H2S Environments.* SSC tensile-style testing in sour environments; the H2S sour-service cousin of G3-conformant electrochemical work.
- [ampp-tm-0284](ampp-tm-0284.md) — *Evaluation of Pipeline and Pressure Vessel Steels for Resistance to Hydrogen-Induced Cracking.* HIC test in NACE Solution A; the hydrogen-charging cousin to electrochemical methods that share G3's sign conventions for cathodic charging.
- Concept anchor: [corrosion-rate-measurement](../concepts/corrosion-rate-measurement.md) — landing page that cites G3 as the electrochemical-conventions foundation underneath the G5 / G59 / G102 / G106 measurement column.
- [Calc citation contract](../../../../../.claude/rules/calc-citation-contract.md) — emit a `Citation(...)` whenever a calc module hard-codes a G3-derived sign convention, reference-electrode offset, or Stern-Geary-style `B` constant.

## Sources

- [og-standards-astm-g-series](../sources/og-standards-astm-g-series.md) — parent source page for the ASTM G-Series slice of the local catalog; records the single-edition G3 presence, the catalog file path, and the metadata-only extraction policy that scopes this standards page.
- Publisher catalog (current edition for purchase, registration required): https://www.astm.org/g0003-14r19.html (or the latest reapproval listing on `astm.org`).
- On-disk raw PDFs (vendor-derivative, do not copy into git per spinout 2026-05-05 governance):
  - `/mnt/ace/O&G-Standards/ASTM/G-Series/G_3_-_89_R99_RZM_.pdf`
