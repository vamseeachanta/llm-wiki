---
title: "ASTM E647 — Fatigue Crack Growth Rate Measurement (da/dN)"
slug: astm-e647
code_id: astm-e647
publisher: ASTM
revision: "latest (catalog: 1999, 2000, 2005); current published edition E647-15e1 / -24 (ASTM)"
tags:
  - astm
  - e-series
  - fatigue
  - crack-growth
  - da-dn
  - paris-law
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
sources:
  - /mnt/ace/O&G-Standards/ASTM/E-Series
  - ../sources/og-standards-astm-e-series.md
extraction_policy: metadata-only
raw_copy_allowed: false
---

# ASTM E647 — Fatigue Crack Growth Rate Measurement (da/dN)

> **code_id:** `astm-e647` &nbsp;·&nbsp; **publisher:** ASTM International (Committee E08 — Fatigue & Fracture, Subcommittee E08.06 on Crack Growth Behavior) &nbsp;·&nbsp; **revision:** current published edition is E647-15e1 (re-approved through subsequent ballots, with E647-24 being the latest reaffirmation/revision); catalog holds three earlier editions (1999, 2000, 2005)

## Scope

ASTM E647 is the laboratory standard for measuring **constant-amplitude
fatigue-crack-growth (FCG) rate** `da/dN` as a function of the
stress-intensity-factor range `ΔK` in metallic materials. It defines the
test apparatus, specimen geometries, loading regimes, crack-length
monitoring, and data-reduction conventions needed to produce a defensible
`da/dN`–`ΔK` curve that spans the three classical regimes:

1. **Region I — near-threshold.** Below `ΔK_th`, growth is operationally
   non-existent (the standard's threshold convention is the `ΔK` at which
   `da/dN ≈ 10⁻¹⁰ m/cycle`, established via decreasing-`K` testing).
2. **Region II — Paris regime.** A power-law middle region where
   `da/dN = C · (ΔK)^m`. The Paris-law parameters `C` and `m` are fit
   from the linear (log–log) middle-region data; these are the canonical
   inputs to FFS fatigue life calculations.
3. **Region III — near-fracture.** Accelerating growth as `K_max`
   approaches the material's fracture toughness `K_c` / `K_Ic`; growth
   is no longer power-law and the test typically terminates at
   ligament-yield or specimen separation.

The Paris-law constants (`C`, `m`) and threshold (`ΔK_th`) extracted per
this standard are the dominant FCG inputs to **BS 7910 Annex M**,
**API 579 Part 14** (FFS fatigue), **DNV-RP-C203** (offshore S-N + FCG
combined assessment), and **R6** (UK nuclear FCG assessment). E647
quantifies *sub-critical* crack growth where the sibling standard
[astm-e1820](astm-e1820.md) quantifies *critical / initiation* fracture toughness;
the two are routinely run on the same heat to populate the full FFS
input set for a structural-integrity case.

## Edition history

Catalog entries observed under `/mnt/ace/O&G-Standards/ASTM/E-Series/`
(plus one mis-filed under `D-Series/`):

| Edition | Year | Catalog filename | Size (B) |
|---------|------|------------------|----------|
| E647-99 | 1999 | `E 647 - 99  _RTY0NY05OQ__.pdf` | 433,275 |
| E647-00 | 2000 | `E 647 - 00  _RTY0NW__.pdf` | 887,995 |
| E647 (2005) | 2005 | `ASTM E647 (2005) Std Test Method for Measurement of Fatigue Crack Growth Rates.pdf` | 712,935 |

Source-page summary records **3 editions** for E647 in the catalog. The
current published edition is **E647-15e1** (with subsequent revisions /
reaffirmations through to **E647-24** issued by ASTM); intermediate
editions E647-08, -08e1, -11, -13a, -13ae1, and -15 have been issued
between the 2005 catalog snapshot and the current edition. E647 was
first issued in 1978 and has been continuously maintained by E08.06
since; the methodology and validity criteria have been stable in
substance since the early 1990s, with later edition changes focused on
crack-length-monitoring options, pre-cracking residual-stress
mitigation, and `K_max`-controlled threshold testing as an alternative
to the classical decreasing-`K` shedding protocol.

## Key sections

The standard is organised around laboratory-execution flow. Section
identifiers vary slightly across editions; the topical groupings below
are stable.

- **Apparatus.** Servohydraulic (or resonance, or electromagnetic) load
  frame with closed-loop force or displacement control, force-verified
  per **ASTM E4**; cyclic-waveform generation (typically sinusoidal) at
  test frequencies that do not introduce specimen self-heating or
  environmental rate-dependence; **crack-length monitoring** by one of
  several sanctioned methods —
  - **Compliance** (CMOD or back-face strain), inferring `a/W` from the
    instantaneous unloading slope via a calibrated compliance function
    for the specimen geometry;
  - **DCPD** (direct-current potential drop), measuring the voltage
    rise across the crack as it grows and inverting via a Johnson-type
    or numerical calibration;
  - **ACPD** (alternating-current potential drop), the AC variant that
    confines current flow to a near-surface skin and offers improved
    sensitivity in some geometries;
  - **Optical** travelling-microscope or **video** measurement of the
    surface crack tip, typically used as a corroborating independent
    measure rather than a primary monitor.
- **Specimen geometries.** Three standardised geometries with
  documented `K`-calibration functions:
  - **Compact tension `C(T)`** — pin-loaded; the workhorse geometry for
    Paris-regime and threshold testing on machined material;
  - **Middle-tension `M(T)`** — centre-cracked panel loaded uniformly
    at the ends; preferred for thin sheet, weld metal, and where
    plane-stress or near-plane-stress conditions are wanted;
  - **Eccentrically-loaded single-edge tension `ESE(T)`** (also seen in
    earlier editions as `SE(T)`) — single-edge-notch tension geometry,
    used for product-form-representative testing (e.g., from pipe
    longitudinal strips).
  Pre-cracking by fatigue at decreasing `ΔK` is mandatory and shall
  terminate at a final `K_max` not greater than that to be applied at
  the start of the test record proper, to avoid load-history (overload)
  artefacts in the early `da/dN` data.
- **Test types.** Two complementary loading protocols:
  - **Decreasing-`K` (threshold) test.** `K_max` (or `ΔK`) is reduced
    on a logarithmic schedule (typically the `C = (1/K) · dK/da`
    *normalised K-gradient* held constant at a value between
    `−0.08 mm⁻¹` and `−0.02 mm⁻¹`) such that the plastic-zone size
    contracts smoothly into the prior cycle's wake; threshold
    `ΔK_th` is reported at the `da/dN ≈ 10⁻¹⁰ m/cycle` operational
    floor. Care: too aggressive a `K`-gradient causes premature
    arrest from residual closure (false-high `ΔK_th`).
  - **Increasing-`K` (Paris / upper-region) test.** Constant-`R`
    (`R = K_min / K_max`) loading with monotonically increasing
    `ΔK` as the crack lengthens at fixed force range; produces the
    Region II linear (log–log) Paris fit and continues into Region III
    until ligament-yield validity is breached or the specimen
    separates.
- **Data reduction.** `da/dN` is derived from the monitored crack
  length `a(N)` by either the **secant** method (two-point chord between
  successive `(a, N)` pairs — simple, but noisy and biased low at
  steep gradients) or the **incremental polynomial** method (typically a
  **7-point** sliding quadratic-in-`N` fit, returning `da/dN` analytically
  from the polynomial derivative — strongly preferred). `ΔK` is
  computed from the geometry's tabulated `K`-calibration as a function
  of `a/W` and the applied force range, with `R` reported alongside.
  The reduced `(ΔK, da/dN)` pairs are plotted on log–log axes; Paris-
  regime data are fit by ordinary least-squares regression in
  `log(da/dN)` vs. `log(ΔK)`.
- **Validity (small-scale yielding).** The dominant validity criterion
  is the **plane-strain plastic-zone constraint** that the remaining
  ligament `(W − a)` shall be large enough that small-scale yielding
  holds, conventionally
  - `K_max < 0.4 · σ_ys · √(W − a)` for `C(T)` and `ESE(T)` (an
    edition-dependent constant; some editions cite the form
    `(W − a) ≥ (4/π) · (K_max / σ_ys)²`, which is algebraically the
    same family);
  - an analogous net-section-stress limit for `M(T)` (typically that
    the remote stress shall not exceed `0.4·σ_ys` to keep the panel
    far from collapse).
  Additional validity boxes: crack-front-curvature limit (typically
  the difference between mean-through-thickness and surface crack
  lengths shall not exceed a fixed fraction); test-frequency limit to
  preclude self-heating (often a hand-touch or thermocouple check at
  the notch tip); environmental-control reporting (lab air vs.
  inert vs. controlled aqueous — relevant cross-link to
  **ASTM E1681**).

## Cross-references

- **ASTM E1820** — sibling fracture-toughness method (`K_Ic`, `J_Ic`,
  `J–R`, CTOD). E647 quantifies *sub-critical* FCG; E1820 quantifies
  *critical / initiation* toughness. Region III of an E647 curve
  asymptotes toward the `K_c` / `K_Ic` measured per E1820 on the same
  heat. See [astm-e1820](astm-e1820.md).
- **ASTM E1681** — *Determination of Threshold Stress Intensity Factor
  for Environment-Assisted Cracking of Metallic Materials*. The
  environmental-FCG companion: where E647 holds environment fixed and
  scans `ΔK`, E1681 holds load fixed (sustained or low-frequency) and
  measures the environmental threshold `K_IEAC` / `K_ISCC`. Both are
  required when characterising sour-service or H₂S-loaded FCG.
- **ASTM E399** — predecessor linear-elastic fracture-toughness method
  (`K_Ic`-only). E647 pre-cracking validity inherits the same
  small-scale-yielding philosophy. See E-series source page.
- **ASTM E466 / E468 / E739** — strain- and stress-life fatigue methods
  (S-N / ε-N). Complementary; E466/E468/E739 cover crack *initiation*
  life, E647 covers crack *propagation* life. The two combine into the
  total-life (initiation + propagation) decomposition used in
  fitness-for-service.
- **ASTM E561** — `K–R` curve method (thin-section / plane-stress
  fracture). Complementary to both E647 and E1820 for elastic-plastic
  thin-section work.
- **ASTM E4** — force-verification of testing machines; mandatory
  upstream calibration for any E647 test.
- **BS 7910 Annex M** — *Guide to methods for assessing the
  acceptability of flaws in metallic structures*, FCG annex. Consumes
  E647-derived Paris parameters (`C`, `m`) and threshold `ΔK_th` as
  the central inputs to flaw-growth life integration; provides
  conservative default `C`/`m` curves (Annex M tables for ferritic
  steel in air, ferritic steel in seawater with/without CP, austenitic
  steel) when E647 data on the actual heat are unavailable.
- **DNV-RP-C203** — *Fatigue design of offshore steel structures*.
  Combined S-N (initiation/early growth) and FCG (long-crack)
  assessment; FCG-route inputs cite E647-style `C`/`m`/`ΔK_th` per
  environment (air, seawater free-corrosion, seawater with cathodic
  protection).
- **API 579-1 / ASME FFS-1, Part 14** — *Fitness-for-Service*, fatigue
  assessment. Part 14's Level-2/3 FCG-driven flaw-growth path consumes
  E647 outputs directly. See [api-std-579](api-std-579.md).
- **R6** (UK nuclear) — *Assessment of the Integrity of Structures
  Containing Defects*. Procedure R6 Section III.6 / equivalent FCG
  appendix uses E647 Paris parameters for sub-critical-growth
  contributions to time-dependent failure-assessment-diagram (FAD)
  trajectories.
- **ISO 12108** — *Metallic materials — Fatigue testing — Fatigue crack
  growth method*. International parallel to E647; intentionally aligned
  in scope, geometry set, and data-reduction conventions, with minor
  differences in the threshold-test `K`-gradient default and the
  validity-box constants.

## Sources

- Source page: [og-standards-astm-e-series](../sources/og-standards-astm-e-series.md)[esrc] — catalog row
  `E647 | Fatigue Crack Growth Rate (da/dN vs. ΔK) | 3 editions in catalog`.
- Catalog provenance: `/mnt/ace/O&G-Standards/_catalog.json`
  (3 entries matching `E647`; three editions: 1999, 2000, 2005).
- Raw PDFs (read-only, vendor-derivative; do NOT copy into git per the
  spinout 2026-05-05 vendor-PDF firewall):
  - `/mnt/ace/O&G-Standards/ASTM/E-Series/E_647_-_99_RTY0NY05OQ_.pdf`
  - `/mnt/ace/O&G-Standards/ASTM/E-Series/E_647_-_00_RTY0NW_.pdf`
  - `/mnt/ace/O&G-Standards/ASTM/D-Series/ASTM_E647_(2005)_Std_Test_Method_for_Measurement_of_Fatigue_Crack_Growth_Rates.pdf`
    *(catalog mis-file under D-Series; subject is the E647 fatigue-
    crack-growth-rate method, not a D-series product spec.)*
- Publisher catalogue: <https://www.astm.org/e0647>

[esrc]: ../sources/og-standards-astm-e-series.md
