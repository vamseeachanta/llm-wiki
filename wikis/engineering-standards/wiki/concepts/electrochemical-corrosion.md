---
title: "Electrochemical Corrosion — Mixed-Potential Theory and Polarization Kinetics"
slug: electrochemical-corrosion
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
tags:
  - electrochemical-corrosion
  - mixed-potential-theory
  - polarization
  - tafel-kinetics
  - butler-volmer
  - exchange-current-density
  - eis
  - lpr
  - astm-g-series
sources:
  - sources/og-standards-astm-g-series.md
extraction_policy: metadata-and-doctrinal-synthesis
cross_links:
  - concepts/corrosion-rate-measurement.md
  - concepts/cathodic-protection.md
  - concepts/galvanic-corrosion.md
  - concepts/sour-service-materials.md
  - concepts/hydrogen-embrittlement.md
  - concepts/brittle-fracture.md
---

# Electrochemical Corrosion — Mixed-Potential Theory and Polarization Kinetics

> Concept anchor for the electrochemical-kinetics framework that underlies every laboratory corrosion-rate test, every [cathodic-protection](cathodic-protection.md) design calculation, and every [galvanic-corrosion](galvanic-corrosion.md) couple analysis. Distinct from [corrosion-rate-measurement](corrosion-rate-measurement.md), which is the engineering-output metric — this page is the kinetics-substrate that makes the rate calculation defensible. Bidirectional with the ASTM G-series electrochemical-test standards ([astm-g3](../standards/astm-g3.md), [astm-g59](../standards/astm-g59.md), [astm-g102](../standards/astm-g102.md), [astm-g106](../standards/astm-g106.md)).

## Scope

**Electrochemical corrosion** is the spontaneous degradation of a metal in an ionically conducting environment via coupled half-cell reactions: an anodic half-cell that liberates metal cations and electrons, and a cathodic half-cell that consumes the same electrons through reduction of an oxidant in solution (typically dissolved O2, H+, or H2O). The framework codified by this concept page covers:

- **Half-cell reactions.** Anodic dissolution (M → M^n+ + n e−) coupled to one or more cathodic reductions (O2 + 2 H2O + 4 e− → 4 OH−; 2 H+ + 2 e− → H2; 2 H2O + 2 e− → H2 + 2 OH−).
- **Mixed-potential theory.** The Wagner–Traud framework: anodic and cathodic reactions proceed simultaneously on a single corroding surface; the surface adopts a mixed (corrosion) potential E_corr at which the net current is zero, and the matched anodic and cathodic partial currents at E_corr equal the corrosion current density i_corr.
- **Polarization curves.** Anodic + cathodic + mixed (Evans diagram) representations on a log|i| – E plane; identification of activation, mass-transport (concentration-polarization), and passive regimes.
- **Exchange current density and Tafel slopes.** The kinetic constants i_0, β_a, β_c that parameterise the Butler–Volmer equation and the asymptotic Tafel form used for E_corr → i_corr extrapolation.
- **From i_corr to penetration rate.** Faraday-equivalent conversion of measured current density into mass-loss rate or thickness-loss rate per [astm-g102](../standards/astm-g102.md).

The page deliberately does not reproduce specific Tafel-slope values, equilibrium-potential tables, or coefficient nomograms; for normative use, cite the relevant ASTM, AMPP, or ISO publication directly.

## Doctrinal evolution

The kinetics framework current practitioners use was assembled across a century-and-a-half of progressive synthesis:

- **Faraday (1834)** — quantitative relationship between charge passed and mass of metal deposited or dissolved (Faraday's laws of electrolysis); the conversion factor that ASTM G102 still operationalises.
- **Nernst (1889)** — equilibrium-potential dependence on activity of dissolved species; the thermodynamic reference frame for half-cell reactions.
- **Pourbaix (1938, formalised in the 1945 *Atlas*)** — potential-pH diagrams that map immunity, corrosion, and passivation regions for each metal-water system; the thermodynamic-screening tool that frames every kinetics calculation.
- **Wagner and Traud (1938)** — mixed-potential theory; the recognition that the corroding surface hosts simultaneous anodic and cathodic partial reactions whose intersection on the Evans diagram defines E_corr and i_corr.
- **Butler–Volmer equation (consolidated 1930s)** — the kinetic law i = i_0 [exp(α_a F η / RT) − exp(−α_c F η / RT)] linking current density to overpotential η for an electrochemical reaction under activation control.
- **Stern and Geary (1957)** — derivation of the linear-polarization-resistance (LPR) relationship i_corr = B / R_p (B = β_a β_c / 2.303 (β_a + β_c)); the basis for [astm-g59](../standards/astm-g59.md) and for routine field corrosion-monitoring probes.
- **Electrochemical impedance spectroscopy (EIS, 1970s onward)** — small-amplitude AC perturbation across a frequency sweep; resolves charge-transfer resistance, double-layer capacitance, diffusion impedance, and coating impedance simultaneously. Codified by [astm-g106](../standards/astm-g106.md).
- **Modern era** — galvanic-corrosion mapping under [astm-g71](../standards/) (where present), localised-electrochemistry probes (SVET, SECM), and computational coupling of Butler–Volmer kinetics with finite-element CP design (per [cathodic-protection](cathodic-protection.md)).

## Mixed-potential theory

The Wagner–Traud framework is the load-bearing abstraction that makes kinetics tractable for engineering use. Its claims:

1. **Multiple reactions, single surface.** A corroding metal surface in an electrolyte hosts at least one anodic reaction (metal dissolution) and at least one cathodic reaction (oxidant reduction), proceeding simultaneously on adjacent sites of the same electrode.
2. **Charge balance enforces a mixed potential.** Because no net current flows from an isolated freely corroding electrode, the surface adjusts its potential until the sum of anodic partial currents equals the sum of cathodic partial currents. This common potential is the **corrosion potential E_corr**.
3. **The matched partial current is i_corr.** At E_corr, the absolute value of the anodic partial current density equals the absolute value of the cathodic partial current density, and this matched value is the **corrosion current density i_corr** — the engineering-relevant kinetic output.
4. **Evans diagram visualisation.** Plotting each partial reaction as a straight line on a semi-log E vs. log|i| diagram (the Tafel asymptote), the intersection of the steepest anodic line with the steepest cathodic line locates (E_corr, i_corr) graphically. The framework generalises to multiple anodic or cathodic reactions by summing currents at each potential.

The framework's power is that it decomposes a coupled, kinetically complex surface into independent half-cell elements that can each be studied — and perturbed — separately. Cathodic protection is mixed-potential theory in reverse: an external current source forces the structure's potential below E_corr, suppressing the anodic partial current to a negligible value (see [cathodic-protection](cathodic-protection.md)).

## Tafel kinetics and polarization

Under activation control (charge-transfer-rate-limited) and at overpotential η = E − E_corr large compared to RT/F (~25 mV at room temperature), the Butler–Volmer equation collapses to its Tafel asymptotes:

- **Anodic branch** (η > 0): log|i_a| ≈ log|i_corr| + η / β_a, where β_a is the anodic Tafel slope (V/decade).
- **Cathodic branch** (η < 0): log|i_c| ≈ log|i_corr| + |η| / β_c, where β_c is the cathodic Tafel slope (V/decade).

Three regimes appear on a real polarization curve:

- **Activation control** — Tafel-linear behaviour; slope set by the electron-transfer step's symmetry factor and the number of electrons transferred. Typical β values of 60–120 mV/decade.
- **Concentration polarization (mass-transport limit)** — when oxidant supply to the surface (e.g. dissolved O2 reaching a buried-pipe steel surface) cannot keep pace with electron consumption, the cathodic branch flattens to a limiting-current plateau i_L. This is the dominant cathodic regime for atmospheric and natural-water service.
- **Mixed (combined) control** — both activation and mass-transport contribute over a finite overpotential range; the curve transitions smoothly between Tafel slope and limiting current.

A fourth regime — **passivity** — applies to the anodic branch for stainless steels, Ni-base alloys, Ti, and other passivating metals: above a critical passivation potential E_pp the anodic current collapses by 3–6 orders of magnitude as a protective oxide film forms, and remains low across a passive window before rising again at the transpassive potential. The passive-window width and the active-passive nose current are the principal alloy-screening outputs of a potentiodynamic scan per [astm-g5](../standards/) (when that page is added) or [astm-g59](../standards/astm-g59.md).

## Test methods and standards

Bidirectional cross-references — each standards page below should cross-link back to this concept page once the convention propagates.

- [astm-g3](../standards/astm-g3.md) — *Conventions Applicable to Electrochemical Measurements in Corrosion Testing.* Reference electrodes, sign conventions, polarization-curve plotting conventions; the metrology preface to the rest of the G-series electrochemical methods.
- [astm-g59](../standards/astm-g59.md) — *Conducting Potentiodynamic Polarization Resistance Measurements.* The LPR procedure: small-amplitude scan around E_corr, polarization resistance R_p extraction, Stern–Geary conversion to i_corr.
- [astm-g102](../standards/astm-g102.md) — *Calculation of Corrosion Rates and Related Information from Electrochemical Measurements.* The conversion machinery from i_corr to mass-loss rate or thickness-loss rate via Faraday's law, including equivalent-weight conventions for alloys.
- [astm-g106](../standards/astm-g106.md) — *Verification of Algorithm and Equipment for Electrochemical Impedance Measurements.* EIS measurement integrity: dummy-cell verification, frequency-range coverage, linearity-and-stability checks.
- [ampp-sp0775](../standards/ampp-sp0775.md) — *Preparation, Installation, Analysis, and Interpretation of Corrosion Coupons in Oilfield Operations.* Electrical-resistance and LPR-probe field-deployment counterpart to the laboratory G-series.
- [ampp-tm-0177](../standards/ampp-tm-0177.md) — *Laboratory Testing of Metals for Resistance to Sulfide Stress Cracking and Stress Corrosion Cracking in H2S Environments.* SSC test methods that depend on a defined sour-service electrochemistry.
- [iso-15156](../standards/iso-15156.md) — *Materials for use in H2S-containing environments in oil and gas production.* Sour-service zoning whose pH-pH2S envelope is a Pourbaix-derived stability map.

Standards referenced but not yet present as first-class wiki pages — candidates for future ingest:

- **ASTM G5** — *Reference Test Method for Making Potentiodynamic Anodic Polarization Measurements.* The active-passive scan procedure; primary tool for stainless-steel and Ni-alloy screening.
- **ASTM G15** — Corrosion-and-related terminology consolidated into ASTM G193; relevant for definitional consistency.
- **ASTM G193** — *Standard Terminology and Acronyms Relating to Corrosion.*
- **ISO 17475** — *Corrosion of metals and alloys — Electrochemical test methods — Guidelines for conducting potentiostatic and potentiodynamic polarization measurements.* International counterpart to the ASTM G3/G5/G59 family.

## Practitioner application

Electrochemical-corrosion kinetics is invoked by:

- **Corrosion engineers** specifying alloys, inhibitor doses, and CP system parameters during design; the polarization-curve toolkit is what converts a thermodynamic Pourbaix screen into an actionable rate prediction.
- **Materials scientists** qualifying new alloy chemistries; potentiodynamic scans per ASTM G5 distinguish active, active-passive, and noble-passive families.
- **Integrity-management teams** running on-line field corrosion-monitoring (LPR probes, ER probes, EIS in-line monitors) to detect rate excursions in real time, complementing the periodic UT thickness surveys described in [corrosion-rate-measurement](corrosion-rate-measurement.md).

Industry contexts where the framework is load-bearing: oil-and-gas production (sour and sweet service), refining and petrochemical (sulfidation, caustic, amine systems), offshore subsea (CP design and HISC management — see [hydrogen-embrittlement](hydrogen-embrittlement.md) and [sour-service-materials](sour-service-materials.md)), water and wastewater (galvanic effects in mixed-metallurgy networks), and power generation (steam-generator and condenser-tube selection).

## Industry adoption

The kinetics framework is normatively embedded in:

- **AMPP (formerly NACE)** — standard practices SP0775 (oilfield coupon and probe practice), TM0177 (sour-service test cells), TM0284 (HIC test method), all of which require defined electrochemical environments and reference electrodes.
- **ASTM G-series** — the primary US methodology suite for laboratory electrochemical corrosion measurement; codified in G3, G5, G59, G102, G106 (above) plus the broader specimen-prep and immersion-test family (G1, G31).
- **ISO 17475 and ISO 16773 (EIS)** — international counterparts that harmonise potentiodynamic and impedance measurement procedures across jurisdictions.
- **ISO 15156 / NACE MR0175** — sour-service zoning whose pH-pH2S envelope is a thermodynamic-electrochemical map of metal stability in H2S-bearing electrolytes.

## Cross-references

- [corrosion-rate-measurement](corrosion-rate-measurement.md) — engineering output metric: the LTCR/STCR pair and the three measurement modalities (mass-loss, electrochemical, in-service thickness). This page is the substrate; that page is the consumer.
- [cathodic-protection](cathodic-protection.md) — the most consequential engineering application of mixed-potential theory: external current depresses E_corr below the immunity threshold, suppressing the anodic partial current.
- [galvanic-corrosion](galvanic-corrosion.md) — two-metal mixed-potential problem; the seawater galvanic series and area-ratio rule are direct corollaries of mixed-potential theory applied to dissimilar-metal couples.
- [sour-service-materials](sour-service-materials.md) — H2S-modified electrochemistry; the cathodic reaction set expands to include H2S reduction and H atom recombination/absorption, which couples kinetics to [hydrogen-embrittlement](hydrogen-embrittlement.md).
- [hydrogen-embrittlement](hydrogen-embrittlement.md) — overprotected-cathode boundary: too-negative a structure-to-electrolyte potential drives the cathodic H-evolution reaction into H-uptake territory, producing HISC in high-strength steels and CRAs.
- [brittle-fracture](brittle-fracture.md) — downstream consequence channel: hydrogen produced electrochemically is the bridge from kinetics to fracture-mechanics-controlled failure.

## Source materials

- [og-standards-astm-g-series](../sources/og-standards-astm-g-series.md) — parent source page for the ASTM G-series corpus; underpins the G3 / G59 / G102 / G106 references in the test-methods section.

## Notes

- This is a concept page, not a standards page. No specific Tafel-slope values, exchange current densities, equivalent-weight tables, or Butler–Volmer α-factor numerics are reproduced here. For normative use cite the publisher edition of the relevant ASTM, AMPP, or ISO document directly.
- The Wagner–Traud framework is the load-bearing kinetic abstraction; it is not a substitute for either Pourbaix thermodynamic screening (which scopes the question) or in-service rate trending (which validates the answer).
- Rate predictions from electrochemical methods (LPR, EIS, potentiodynamic extrapolation) require calibration against mass-loss for the specific environment; see [corrosion-rate-measurement](corrosion-rate-measurement.md) for the lab-versus-field reconciliation framework.
