---
title: "ASTM G102 — Calculation of Corrosion Rates from Electrochemical Measurements"
slug: astm-g102
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
code_id: astm-g102
publisher: ASTM
revision: latest
tags:
  - astm
  - g-series
  - corrosion-rate
  - electrochemistry
  - stern-geary
  - faraday
sources:
  - ../sources/og-standards-astm-g-series.md
extraction_policy: metadata-only
raw_copy_allowed: false
---

# ASTM G102 — Standard Practice for Calculation of Corrosion Rates and Related Information from Electrochemical Measurements

> Bounded metadata-only standards page. Per llm-wiki spinout governance (2026-05-05), vendor PDFs are not copied into this repo; this page records only publisher facts and a domain-knowledge scope description.
> **code_id:** `astm-g102` &nbsp;•&nbsp; **publisher:** ASTM International (Committee G01 — Corrosion of Metals; Subcommittee G01.11 on Electrochemical Measurements in Corrosion Testing) &nbsp;•&nbsp; **revision:** latest publisher edition (the on-disk catalog holds G102-89(R99) — see Edition history below).

## Scope

ASTM G102 is the **calc-bridge standard** that converts a corrosion-current density `i_corr` (μA/cm²), measured by a [astm-g3](astm-g3.md)-conformant electrochemical method, into an engineering-grade **corrosion rate** in penetration units (mm/yr, mils/yr) or mass-loss units (mg/dm²/day, g/m²/day). It does not specify how to obtain `i_corr` — that responsibility lives upstream in [astm-g5](astm-g5.md) (potentiodynamic Tafel extrapolation), [astm-g59](astm-g59.md) (linear polarization resistance, LPR), or [astm-g106](astm-g106.md) (electrochemical impedance spectroscopy, EIS). G102 is the terminal step that turns those measurements into a number a piping/vessel/CRA-selection engineer can act on.

The practice covers four substrate areas:

- **Faraday-law conversion** of `i_corr` to penetration rate or mass-loss rate, using the metal's **equivalent weight (EW)** and **density (ρ)** as the only material inputs.
- **Stern-Geary linkage** between polarization resistance `R_p` (from G59) and `i_corr`, providing the proportionality constant `B` in terms of the anodic and cathodic Tafel slopes (`b_a`, `b_c`) measured per G3/G5 conventions.
- **Equivalent-weight calculation for alloys** — Annex 1 of G102 tabulates composition-weighted EW values for common engineering alloys (carbon steel, austenitic and duplex stainless steels, Ni-based alloys, copper alloys, aluminum, titanium) and provides the calculation procedure for non-listed alloys from chemical composition + assumed-valence assignments.
- **Penetration-rate vs. surface-evolution-rate distinction** — the Faraday-derived rate is a **uniform-corrosion** equivalent. For non-uniform attack (pitting, crevice, intergranular, dealloying), the calculated rate underrepresents local penetration and must be combined with localized-corrosion morphology data (pit-depth statistics per [astm-g46](astm-g46.md), crevice severity per G48, etc.).

For a calc-module author: G102 is the **output schema** for any corrosion-rate sensor or calc that begins with an electrochemical measurement. A reported corrosion rate that does not declare which Faraday constant (K1 for mm/yr vs K2 for mg/dm²/day), which EW (alloy-specific or single-metal), and which `i_corr` provenance (Tafel extrapolation vs LPR-derived) was used is not auditable. G102 is the citation that closes that loop.

## Edition history

The local O&G-Standards catalog at `/mnt/ace/O&G-Standards/ASTM/G-Series/` holds **one G102 PDF**:

| Edition | Filename (catalog) | Catalog presence | Notes |
|---------|-------------------|------------------|-------|
| G102-89(R99) | `G_102_-_89_R99_RZEWMG_.pdf` | 1 file | 1989 revision, reapproved 1999 |
| G102 (current) | not on disk | — | The publisher-current ASTM G102 edition is later than the 1999 reapproval (additional reapprovals have been issued in the post-2000 cycle); calc-callers needing the current edition must obtain it from the ASTM catalog |

The publisher catalog year-token sweep done for the [og-standards-astm-g-series](../sources/og-standards-astm-g-series.md) source page recorded G102 with **1 edition** in the local catalog, matching the file row above.

## Key equations

All equations below use SI-consistent units except where the standard's empirical constant `K1` or `K2` absorbs a unit conversion explicitly.

- **Faraday penetration rate** (the headline G102 output):

  $$\mathrm{CR}\ (\mathrm{mm/yr}) = K_1 \cdot \frac{i_{\mathrm{corr}} \cdot \mathrm{EW}}{\rho}$$

  where `K1 = 3.27 × 10⁻³` (mm·g/μA·cm·yr), `i_corr` in μA/cm², `EW` is dimensionless (g/equivalent), and `ρ` is in g/cm³. A parallel `K3 = 0.129` constant gives mils/yr (mpy) when used with the same `i_corr`/EW/ρ inputs.

- **Faraday mass-loss rate** (alternate output for coupon-rate cross-validation per [astm-g1](astm-g1.md)):

  $$\mathrm{MR}\ (\mathrm{mg/dm^2/day}) = K_2 \cdot i_{\mathrm{corr}} \cdot \mathrm{EW}$$

  where `K2 = 0.0894` (mg·cm²/μA·dm²·day), `i_corr` in μA/cm². The mass-loss form is independent of density and is the form used to compare an in-situ electrochemical sensor reading against a parallel weight-loss coupon.

- **Stern-Geary equation** (the bridge from LPR per [astm-g59](astm-g59.md) to `i_corr`):

  $$i_{\mathrm{corr}}\ (\mu\mathrm{A/cm^2}) = \frac{B}{R_p}$$

  with the proportionality constant

  $$B = \frac{b_a \cdot b_c}{2.303 \cdot (b_a + b_c)}$$

  where `b_a`, `b_c` are the anodic and cathodic Tafel slopes (V/decade or mV/decade — keep units consistent with `R_p`), and `R_p` is the polarization resistance (Ω·cm²) from a small-overpotential LPR sweep. `B` typically lies in the range 0.013–0.052 V for activation-controlled corrosion in aqueous systems; G102 recommends measuring `b_a` and `b_c` directly per [astm-g5](astm-g5.md) rather than assuming a default `B`.

- **Equivalent weight (single metal):**

  $$\mathrm{EW} = \frac{W}{n}$$

  where `W` is the atomic weight (g/mol) and `n` is the assumed valence (number of electrons transferred per dissolved atom — e.g., Fe → Fe²⁺ gives `n = 2`).

- **Equivalent weight (alloy)** — composition-weighted reciprocal sum (G102 Annex 1):

  $$\mathrm{EW}_{\mathrm{alloy}} = \left[\sum_i \frac{f_i \cdot n_i}{W_i}\right]^{-1}$$

  where `f_i` is the mass fraction of element *i* in the alloy, `n_i` is its assumed valence in the corrosion environment, and `W_i` is its atomic weight. Annex 1 tabulates the result for common alloys (see EW table below).

- **Penetration rate vs. surface-evolution rate.** The G102 `CR` is a **uniform-thickness-loss equivalent** — the rate at which a flat surface would recede if all the dissolved charge were uniformly distributed. For non-uniform attack (pitting, crevice, dealloying, intergranular SCC initiation), local penetration can exceed the G102 `CR` by 1–3 orders of magnitude; pair G102 output with a localized-corrosion morphology assessment ([astm-g46](astm-g46.md) pit rating, G48 crevice/pitting depth) before using the rate for remaining-life forecasts.

## EW table

ASTM G102 Annex 1 tabulates equivalent-weight values for engineering alloys. Selected values (composition-weighted per the alloy formula above; assumed valences from G102 Annex 1):

| Alloy | EW (g/equivalent) | Typical density ρ (g/cm³) | Notes |
|-------|------------------|---------------------------|-------|
| Carbon steel (UNS G10180) | 27.92 | 7.86 | Fe valence assumed 2 (Fe²⁺ predominant in near-neutral aqueous corrosion) |
| 304 stainless (UNS S30400) | 25.12 | 7.94 | Fe/Cr/Ni weighted; Cr at +3, Ni at +2, Fe at +2 |
| 316 stainless (UNS S31600) | 25.50 | 7.98 | Adds Mo at +3 vs. 304 |
| Alloy 400 (Ni-Cu, UNS N04400) | 28.97 | 8.80 | Monel; Ni +2, Cu +2 |
| Alloy 600 (Ni-Cr-Fe, UNS N06600) | 26.41 | 8.42 | Inconel 600 |
| Alloy 625 (Ni-Cr-Mo-Nb, UNS N06625) | 27.21 | 8.44 | High-Mo Ni-base CRA, common subsea cladding |
| Alloy 825 (Ni-Fe-Cr-Mo, UNS N08825) | 27.13 | 8.14 | Sour-service CRA, NACE MR0175 qualified |
| Alloy C-276 (Ni-Cr-Mo-W, UNS N10276) | 27.42 | 8.89 | Hastelloy C-276; aggressive-acid service |
| Copper (UNS C11000) | 31.77 | 8.94 | Cu valence 2 |
| 70-30 brass (UNS C26000) | 32.04 | 8.53 | Cu/Zn weighted |
| Aluminum (UNS A91100) | 8.99 | 2.71 | Al valence 3 |
| Titanium (UNS R50400) | 11.97 | 4.51 | Ti valence 4 |

Use the alloy-specific EW from G102 Annex 1 whenever possible. For a non-listed proprietary alloy, compute EW from mill-cert composition + G102 valence assumptions; record the assumption set in the calc citation so peer reviewers can reproduce.

## Acceptance limits

Stern-Geary `i_corr = B / R_p` is **valid only when corrosion is activation-controlled (Wagner-Traud regime)** — i.e., the overall rate is limited by the charge-transfer kinetics at the metal/electrolyte interface, both Tafel branches are observable, and the polarization resistance reflects the linear small-overpotential portion of the polarization curve. Outside this regime the G102 calc breaks down:

- **Diffusion-controlled corrosion** (mass-transport-limited oxygen reduction, low-velocity flow, or high-temperature scale-forming systems) does not give a meaningful `b_c`; the cathodic branch is a current plateau rather than a Tafel line. Use [astm-g106](astm-g106.md) EIS with Cole-Cole / equivalent-circuit analysis to extract a charge-transfer resistance separately from the diffusion impedance, and report the `i_corr` decomposition explicitly.
- **Mixed-control or passivation transitions** (e.g., stainless steels traversing the active-passive transition) violate the constant-`B` assumption; report `B` as a function of potential or fall back to direct Tafel extrapolation per [astm-g5](astm-g5.md).
- **Localized corrosion** (pitting, crevice) produces a uniform-rate-equivalent `i_corr` that does not represent the local penetration; G102 output is a lower bound on remaining-life impact.
- **Coupling area mismatch.** `i_corr` is a current-per-unit-area measurement on the working-electrode area; for galvanic couples (per G71) the calc must be applied to the anode area, not the wetted-coupon area.
- **Cross-validation expectation.** G102 explicitly recommends periodic cross-validation against [astm-g1](astm-g1.md) mass-loss coupon data — disagreement >2× is a flag that the activation-controlled assumption is failing.

## Cross-references

- [astm-g3](astm-g3.md) — *Standard Practice for Conventions Applicable to Electrochemical Measurements in Corrosion Testing.* Sign conventions, reference-electrode reporting, and Tafel-slope extraction conventions that G102's inputs (`i_corr`, `b_a`, `b_c`) must obey to be auditable.
- [astm-g59](astm-g59.md) — *Standard Test Method for Conducting Potentiodynamic Polarization Resistance Measurements.* Primary `R_p` source for the Stern-Geary route into G102 (`i_corr = B / R_p`).
- [astm-g5](astm-g5.md) — *Standard Reference Test Method for Making Potentiodynamic Anodic Polarization Measurements.* Primary `i_corr` source via Tafel extrapolation, and the canonical procedure for measuring `b_a`, `b_c` that determine `B`.
- [astm-g106](astm-g106.md) — *Standard Practice for Verification of Algorithm and Equipment for Electrochemical Impedance Measurements.* EIS-based alternative to LPR for `R_p` extraction; required when diffusion-controlled or mixed-control conditions invalidate the simple Stern-Geary form.
- [astm-g1](astm-g1.md) — *Standard Practice for Preparing, Cleaning, and Evaluating Corrosion Test Specimens.* Mass-loss baseline for cross-validating G102 electrochemical-derived rates.
- [astm-g46](astm-g46.md) — *Standard Guide for Examination and Evaluation of Pitting Corrosion.* Pit-depth morphology data that must be reported alongside G102 uniform-rate output whenever localized attack is suspected.
- [API RP 571](https://www.api.org/) — *Damage Mechanisms Affecting Fixed Equipment in the Refining Industry.* Damage-mechanism rate context (CO2/H2S/sulfidation/acid corrosion regimes) into which G102 numerical outputs are placed for fitness-for-service work.
- [NACE SP0775](https://www.ampp.org/) (now AMPP SP0775) — *Preparation, Installation, Analysis, and Interpretation of Corrosion Coupons in Oilfield Operations.* Online corrosion-monitoring corrosion-rate reporting that consumes G102-formatted output from in-line probes.
- Concept anchor: [corrosion-rate-measurement](../concepts/corrosion-rate-measurement.md) — landing page that cites G102 as the `i_corr` → engineering-rate calc bridge underneath the G5 / G59 / G106 measurement column.
- [Calc citation contract](../../../../../.claude/rules/calc-citation-contract.md) — emit a `Citation(...)` whenever a calc module hard-codes a G102 Faraday constant (K1, K2, K3), an alloy-specific EW from Annex 1, or a Stern-Geary `B` value derived per the equations above.

## Sources

- [og-standards-astm-g-series](../sources/og-standards-astm-g-series.md) — parent source page for the ASTM G-Series slice of the local catalog; records the single-edition G102 presence, the catalog file path, and the metadata-only extraction policy that scopes this standards page.
- Publisher catalog (current edition for purchase, registration required): https://www.astm.org/g0102-89r15e01.html (or the latest reapproval listing on `astm.org`).
- On-disk raw PDFs (vendor-derivative, do not copy into git per spinout 2026-05-05 governance):
  - `/mnt/ace/O&G-Standards/ASTM/G-Series/G_102_-_89_R99_RZEWMG_.pdf`
