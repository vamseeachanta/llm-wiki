---
title: "ASTM G106 — Electrochemical Impedance Measurements (EIS) Verification"
slug: astm-g106
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
code_id: astm-g106
publisher: ASTM
revision: latest
tags:
  - astm
  - g-series
  - corrosion
  - eis
  - impedance
  - equivalent-circuit
sources:
  - ../sources/og-standards-astm-g-series.md
extraction_policy: metadata-only
raw_copy_allowed: false
---

# ASTM G106 — Standard Practice for Verification of Algorithm and Equipment for Electrochemical Impedance Measurements

> Bounded metadata-only standards page. Per llm-wiki spinout governance (2026-05-05), vendor PDFs are not copied into this repo; this page records only publisher facts and a domain-knowledge scope description.
> **code_id:** `astm-g106` &nbsp;•&nbsp; **publisher:** ASTM International (Committee G01 — Corrosion of Metals; Subcommittee G01.11 on Electrochemical Measurements in Corrosion Testing) &nbsp;•&nbsp; **revision:** latest publisher edition (the on-disk catalog holds G106-89(R99) — see Edition history below).

## Scope

ASTM G106 is the **verification practice** for **Electrochemical Impedance Spectroscopy (EIS)** equipment and the algorithms that fit measured spectra to equivalent-circuit models. The practice does not specify a corrosion test on its own — it specifies how a laboratory **demonstrates that its potentiostat / frequency-response analyzer (FRA) and its curve-fitting software produce correct impedance values** before that hardware/software stack is used to characterize a real specimen.

EIS itself applies a **small-amplitude AC perturbation** (typically 5–10 mV rms about the open-circuit potential, OCP) over a **broad frequency range** — conventionally **100 kHz down to 10 mHz**, six decades — and records the complex impedance `Z(ω) = Z'(ω) + j·Z''(ω)` at each frequency. Fitting `Z(ω)` to a physically motivated equivalent circuit yields:

- **Solution resistance** `R_s` (the high-frequency real-axis intercept).
- **Polarization resistance** `R_p` (the low-frequency real-axis intercept minus `R_s`), feeding Stern-Geary `i_corr` per [[astm-g3]] and [[astm-g102]].
- **Double-layer capacitance** `C_dl` (or constant-phase element `Q`, `α`), reporting electrode-surface area and adsorbed-film coverage.
- **Diffusion impedance** (Warburg branch `Z_W = σ·ω⁻¹/²·(1−j)`) for mass-transport-limited reactions.
- **Coating layers** — pore resistance `R_pore` and coating capacitance `C_c` — for painted, anodized, or 3LPE-coated specimens.

G106's verification scope addresses **both ends of the measurement chain**: the **hardware** (potentiostat amplitude/phase accuracy across the swept frequency band) and the **software** (the non-linear least-squares fitter that maps measured `Z(ω)` to equivalent-circuit parameters). A laboratory that omits this verification cannot defensibly cite EIS-derived `R_p` or `i_corr` in a regulatory submission.

## Edition history

The local O&G-Standards catalog at `/mnt/ace/O&G-Standards/ASTM/G-Series/` holds **one G106 PDF**:

| Edition | Filename (catalog) | Catalog presence | Notes |
|---------|-------------------|------------------|-------|
| G106-89(R99) | `G_106_-_89_R99_RZEWNG_.pdf` | 1 file | 1989 revision, reapproved 1999 |
| G106 (current) | not on disk | — | The publisher-current ASTM G106 edition is later than the 1999 reapproval; calc-callers needing the current edition must obtain it from the ASTM catalog |

The publisher catalog year-token sweep done for the [[og-standards-astm-g-series]] source page recorded G106 with **1 edition** in the local catalog, matching the file row above.

## Key sections

- **Apparatus verification with a passive RC dummy cell.** The verification specimen is a known-value resistor-capacitor network (typically a parallel `R_p ‖ C_dl` placed in series with `R_s`) — not a corroding electrode. The dummy cell's components are measured independently with a calibrated LCR meter; the EIS instrument is required to reproduce the impedance spectrum within a tolerance band (commonly ±1% on |Z| and ±1° on phase across the working frequency range). Drift outside this band indicates potentiostat amplitude error, FRA phase error, or a stale calibration.
- **Test conditions for live specimens.** Rest the working electrode at OCP until `dE/dt` drops below ~1 mV/min before starting the sweep — drift during the low-frequency decade is the dominant source of EIS noise. The conventional sweep covers **at least six frequency decades** (100 kHz to 10 mHz); fewer decades truncate either the `R_s` extraction (high-frequency limit) or the `R_p` extraction (low-frequency limit). Perturbation amplitude is kept small (5–10 mV rms) to stay within the linear regime where `Z(ω)` is independent of amplitude.
- **Data presentation.** Two canonical plot families, both anchored on the [[astm-g3]] convention substrate:
  - **Nyquist plot** — `−Z''(ω)` on the Y axis vs `Z'(ω)` on the X axis (both linear, equal scale on both axes so semicircles render as circles). Each frequency is one point on the curve; the high-frequency end sits on the left near `R_s` and the low-frequency end sits on the right near `R_s + R_p`.
  - **Bode plot** — `log|Z(ω)|` and `phase angle θ(ω)` plotted separately against `log(f)`. Bode magnitude is read for `R_s` (high-f plateau) and `R_p` (low-f plateau); Bode phase peaks reveal the number of distinct time constants in the system.
- **Kramers-Kronig (KKT) consistency check.** Real and imaginary parts of `Z(ω)` are mathematically constrained by causality: each can be reconstructed from the other via the Kramers-Kronig integral transforms. G106 requires a KKT residual check on every measured spectrum — residuals exceeding ~1% indicate non-stationary behavior (drift), non-linear response (perturbation amplitude too large), or instrument artifacts; such spectra fail the practice and cannot be reported.
- **Equivalent-circuit fitting.** The fitter is required to be **non-linear least squares** (Levenberg-Marquardt or equivalent), to report **parameter uncertainty estimates**, and to be verified against the dummy-cell network whose values are independently known. Common circuits:
  - **Randles cell** — `R_s + (R_p ‖ C_dl)`, the textbook one-time-constant model for an actively corroding bare electrode.
  - **Voigt circuit** — series of `R_n ‖ C_n` blocks for systems with multiple resolvable time constants.
  - **Transmission-line / porous-electrode** — distributed-element model for porous coatings, fuel-cell electrodes, and battery composites where the active surface is buried inside a porous matrix.
  - **Constant-phase element (CPE)** — `Z_CPE = 1 / [Q·(jω)^α]` substituted for `C_dl` to capture surface-roughness-induced frequency dispersion (`α = 1` recovers an ideal capacitor).

## EIS vs. LPR

ASTM G106 (EIS) and ASTM G59 (LPR) are the two electrochemical practices that deliver `R_p` for Stern-Geary `i_corr` extraction. They differ in measurement bandwidth and in what other system parameters they expose:

| Aspect | LPR (G59) | EIS (G106) |
|--------|-----------|------------|
| Output | `R_p` only | `R_p` + `R_s` + `C_dl` + diffusion + coating layers |
| Measurement time | seconds | minutes (set by the low-frequency limit; 10 mHz ≈ 100 s/cycle) |
| Field deployment | yes (online corrosion probes) | mostly lab (R&D) |
| Diffusion-controlled corrosion | poor accuracy (DC sweep cannot separate Warburg from `R_p`) | accurate (Warburg branch resolves at low f) |
| Coated specimens | low sensitivity (coating dominates DC resistance) | excellent (capacitance + `R_pore` evolution tracked separately) |
| IR (ohmic) drop handling | requires post-test correction or current-interrupt | `R_s` measured directly at the high-frequency intercept |
| Linearity check | implicit (small overpotential) | explicit (KKT residuals) |
| Hardware demand | potentiostat only | potentiostat + frequency-response analyzer |

The practical consequence: LPR is the **online-monitoring** tool (NACE SP0775 production probes), while EIS is the **diagnostic** tool — when an LPR probe drifts or shows anomalous `R_p`, an EIS scan on the same specimen is what reveals whether the change is real corrosion-rate evolution, coating breakdown, biofilm formation, or a transport-limited regime change.

## Application

- **Passive-film characterization on CRAs** — repassivation kinetics on stainless steels, duplex/super-duplex, and Ni-base alloys after mechanical disruption; anodization-quality verification on aluminum (anodic-film thickness shows up directly as a low-frequency capacitance shift); RPV cladding integrity in nuclear primary-loop water.
- **Coating-degradation tracking** — epoxy, FBE (fusion-bonded epoxy), and 3LPE (three-layer polyethylene) pipeline coatings monitored via `R_pore` evolution (water uptake drops `R_pore` orders of magnitude before any visible blistering) and coating capacitance `C_c` (a direct proxy for water-permeation depth via the Brasher-Kingsbury relation).
- **Biofilm and scale-layer monitoring** — biofilm formation on heat-exchanger tubes and water-injection lines registers as a low-frequency capacitance shift and an additional time constant in the Bode-phase plot, often visible weeks before downstream consequences (under-deposit corrosion, MIC).
- **Battery and fuel-cell corrosion** — different application domain but the same physics; G106's apparatus-verification protocol is widely adopted in Li-ion solid-electrolyte interphase (SEI) characterization and PEM fuel-cell membrane-electrode-assembly (MEA) diagnostics, with the equivalent-circuit topology adapted (transmission-line for porous electrodes, Warburg-short for finite-thickness diffusion).

## Cross-references

- [[astm-g3]] — *Conventions for Electrochemical Measurements in Corrosion Testing.* G106 cites G3 for impedance-plot conventions (Nyquist sign convention `−Z''` upward; Bode log-frequency axis) and OCP reporting.
- [[astm-g59]] — *Linear Polarization Resistance (LPR) Measurements.* DC sibling to G106; both deliver `R_p` for Stern-Geary `i_corr`. EIS supersedes LPR when `R_s`, diffusion, or coating layers are non-negligible.
- [[astm-g5]] — *Potentiodynamic Anodic Polarization Measurements.* Tafel scan on a Type 430 reference electrode; G106 is the AC complement to G5's DC measurement.
- [[astm-g102]] — *Calculation of Corrosion Rates from Electrochemical Measurements.* Converts G106-derived `i_corr` into engineering penetration rate (mm/yr or mpy) via Faraday's law with an equivalent-weight argument.
- [[astm-g1]] — *Preparing, Cleaning, and Evaluating Corrosion Test Specimens.* Mass-loss baseline that every G106-derived `i_corr` should be calibrated against before being trusted as an in-situ rate sensor.
- [[astm-g31]] — *Laboratory Immersion Corrosion Testing of Metals.* Long-exposure mass-loss substrate that calibrates electrochemical-derived rates including EIS.
- [[ampp-mr-0175-pt1]] / [[ampp-mr-0175-pt2]] / [[ampp-mr-0175-pt3]] — sour-service material-qualification framework; EIS is increasingly used to characterize CRA passive films under H2S/CO2 partial pressures within MR0175 envelopes.
- NACE SP0775 — *Preparation, Installation, Analysis, and Interpretation of Corrosion Coupons in Oilfield Operations.* Online-monitoring practice in which EIS-based probes are increasingly deployed alongside coupons and LPR probes; G106 is the equipment-verification anchor for those EIS probes.
- [[api-rp-571]] — *Damage Mechanisms Affecting Fixed Equipment in the Refining Industry.* Damage-mechanism context for the corrosion modes (CUI, MIC, sour cracking, naphthenic-acid attack) that EIS is deployed to characterize in the field.
- Concept anchor: [corrosion-rate-measurement](../concepts/corrosion-rate-measurement.md) — landing page that cites G106 as the EIS primary, alongside G5/G59/G102 in the electrochemical-measurement column.
- [Calc citation contract](../../../../../.claude/rules/calc-citation-contract.md) — emit a `Citation(...)` whenever a calc module hard-codes an EIS-derived `R_p`, `C_dl`, or coating `R_pore` value with G106 provenance.

## Sources

- [[og-standards-astm-g-series]] — parent source page for the ASTM G-Series slice of the local catalog; records the single-edition G106 presence, the catalog file path, and the metadata-only extraction policy that scopes this standards page.
- Publisher catalog (current edition for purchase, registration required): https://www.astm.org/g0106-89r15.html (or the latest reapproval listing on `astm.org`).
- On-disk raw PDFs (vendor-derivative, do not copy into git per spinout 2026-05-05 governance):
  - `/mnt/ace/O&G-Standards/ASTM/G-Series/G_106_-_89_R99_RZEWNG_.pdf`
