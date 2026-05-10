---
title: "ASTM E1820 — Measurement of Fracture Toughness"
slug: astm-e1820
code_id: astm-e1820
publisher: ASTM
revision: "latest (catalog: 1999, 2001, 2006); current published edition E1820-23 (ASTM)"
tags:
  - astm
  - e-series
  - fracture-toughness
  - j-integral
  - ctod
  - single-specimen
  - multi-specimen
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
sources:
  - /mnt/ace/O&G-Standards/ASTM/E-Series
  - ../sources/og-standards-astm-e-series.md
extraction_policy: metadata-only
raw_copy_allowed: false
---

# ASTM E1820 — Measurement of Fracture Toughness

> **code_id:** `astm-e1820` &nbsp;·&nbsp; **publisher:** ASTM International (Committee E08 — Fatigue & Fracture) &nbsp;·&nbsp; **revision:** latest published edition is E1820-23; catalog holds three earlier editions (1999, 2001, 2006)

## Scope

ASTM E1820 is the unified test method for laboratory measurement of the
fracture toughness of metallic materials. It consolidates several earlier
single-parameter standards into a single procedure that returns whichever
toughness parameter is appropriate to the specimen's regime of behaviour:
linear-elastic plane-strain toughness (`K_Ic`), elastic-plastic
J-integral initiation toughness (`J_Ic`), J-resistance curves (`J–R`),
crack-tip opening displacement at initiation (`CTOD_c`, `δ_Ic`), and
CTOD-resistance curves (`δ–R`). Both **single-specimen** (elastic-compliance
unloading-compliance) and **multi-specimen** (heat-tinting / fractographic
crack-extension marking on a series of specimens loaded to different
displacements) approaches are sanctioned. Standardised specimen geometries
include compact tension `C(T)`, single-edge-notch bend `SE(B)`,
disk-shaped compact `DC(T)`, and arc-shaped `A(T)` / `A(B)` (typically
machined from pipe or tubular product). Critical-load definitions (e.g.,
`P_max`, the 5%-secant `P_5`, the deviation point on the force–CMOD
record) gate which parameter is reported and whether linear-elastic-only
validity per the predecessor `K_Ic`-only standard (ASTM E399) is satisfied.
The unified procedure is the dominant elastic-plastic toughness method
post-2000 and is the laboratory backbone of fitness-for-service (FFS)
toughness inputs.

## Edition history

Catalog entries observed under `/mnt/ace/O&G-Standards/ASTM/E-Series/`:

| Edition | Year | Catalog filename | Size (B) |
|---------|------|------------------|----------|
| E1820-99 | 1999 | `E 1820 - 99  _RTE4MJATOTLB.pdf` | 465,431 |
| E1820-99 (alt scan) | 1999 | `E 1820 - 99  _RTE4MJATUKVE.pdf` | 611,664 |
| E1820-01 | 2001 | `E 1820 - 01  _RTE4MJA_.pdf` | 717,057 |
| E1820 (2006) | 2006 | `ASTM E1820 (2006) Standard Test Method for Measurement of Fracture Toughness.pdf` | 728,871 |

Source-page summary records **3 editions** for E1820 (the two 1999 scans
are duplicate captures of the same edition). Current published edition is
**E1820-23** (not in catalog); intermediate editions E1820-08, -09, -11,
-13, -15, -16, -17, -18, -20, -20a, and -23 have been issued by ASTM
between the 2006 catalog snapshot and the current edition. E1820 itself
absorbed the (now-withdrawn) **E813** `J_Ic` standard in the late 1990s
and has progressively absorbed CTOD-only methodology that previously
lived in **E1290**.

## Key sections

The standard is organised by laboratory-execution flow. Section
identifiers vary slightly across editions; the topical groupings below
are stable.

- **Apparatus.** Calibrated load frame (force-verified per **ASTM E4**),
  displacement-measuring instrumentation — **CMOD** (crack-mouth opening
  displacement) gage at the load line for `C(T)` / `DC(T)`, **LLD**
  (load-line displacement) for `SE(B)` — environmental chamber for
  non-ambient testing, and the unloading-compliance hardware required
  for the single-specimen method.
- **Specimen preparation.** Geometry and proportional dimensioning of
  `C(T)`, `SE(B)`, `DC(T)`, and arc-shaped specimens; **machined notch**
  with controlled root radius; **side-grooves** (typically 5–10% of
  thickness per side, total 10–25% net-section reduction) to enforce
  straight crack-front advance and suppress shear-lip tunnelling;
  starter-notch geometry tolerances.
- **Pre-cracking by fatigue.** Sharp pre-crack introduced under
  load-controlled cyclic loading at decreasing `ΔK` to a controlled
  final `K_max`; pre-crack length, straightness, and front-curvature
  validity criteria (typical: `a₀/W` in the 0.45–0.70 window depending
  on edition and specimen type); environmental and frequency
  constraints to avoid altering material toughness.
- **Test execution.** Quasi-static monotonic loading with continuous
  digital recording of force vs. CMOD (or LLD); periodic
  partial-unload–reload sequences (typically 10–20% load excursions)
  for the **single-specimen elastic-compliance** method to infer
  instantaneous crack length from the unloading slope; alternative
  **multi-specimen** path loads several nominally identical specimens
  to a sequence of progressively increasing displacements, marks the
  crack front by heat-tinting or fatigue marker cycles, breaks open,
  and reads `Δa` fractographically.
- **Data reduction.** Raw force–displacement record converted to
  J vs. Δa or δ vs. Δa via the standard's η/γ functions for the
  selected geometry; **construction-line** (blunting line) plotted at
  `J = 2·σ_Y·Δa` (or equivalent for δ); offset construction lines at
  0.15 mm and 0.20 mm exclusion bound the qualified `Δa` window;
  **J_Q / J_Ic** read at the 0.2-mm offset intersection with the
  power-law-fit `J–R` curve; CTOD analogues (`δ_Q / δ_Ic`) computed in
  parallel; **K_Ic** path applied only when force–CMOD record is
  linear-elastic and E399-style 5%-secant criterion is met.
- **Validity criteria.** Specimen-size requirements relating thickness
  `B` and remaining ligament `b₀` to the candidate toughness and yield
  strength (the `J_Ic` constraint `B, b₀ ≥ 10·J_Q/σ_Y` is the canonical
  example); maximum qualified J/CTOD plateau set by ligament dimensions;
  crack-front-straightness requirement (typically each of nine equally
  spaced through-thickness positions within ±X% of the average);
  initial-crack-length validity; load-train alignment tolerances.

## Cross-references

- **ASTM E399** — *Linear-Elastic Plane-Strain Fracture Toughness K_Ic
  of Metallic Materials*. Narrower-scope predecessor restricted to the
  small-scale-yielding regime; E1820 absorbs and generalises the K-only
  path within its unified flow. See [E-Series source page][esrc].
- **ASTM E1290** — *Crack-Tip Opening Displacement Fracture Toughness
  Measurement*. CTOD-only method; partially superseded by E1820 as the
  unified standard added the CTOD-R curve path.
- **ASTM E1921** — *Reference Temperature T₀ for Ferritic Steels in the
  Transition Range (Master Curve)*. Downstream method that uses E1820
  / E399 toughness data points (typically C(T) or PCVN specimens) to
  fit the Master Curve and report `T₀`.
- **ASTM E647** — *Measurement of Fatigue Crack Growth Rates (da/dN
  vs. ΔK)*. Complementary fatigue-crack-growth method; E647 quantifies
  sub-critical crack growth where E1820 quantifies critical/initiation
  toughness.
- **ASTM E813** — (withdrawn) original `J_Ic` standard, fully absorbed
  into E1820 in the late 1990s.
- **ASTM E561** — `K–R` curve method for thin-section / plane-stress
  toughness; complementary to E1820's `J–R` / `δ–R` curves for the
  elastic-plastic regime.
- **ASTM E4** — Force-verification of testing machines; mandatory
  upstream calibration for any E1820 test.
- **BS 7448** — UK *Fracture mechanics toughness tests* (parts 1–4
  covering K, CTOD, J on parent metal and weldments). Parallel
  national standard; Annex K of BS 7910 historically required BS 7448
  data, with E1820 / ISO 12135 increasingly accepted as equivalent.
- **ISO 12135** — *Metallic materials — Unified method of test for the
  determination of quasistatic fracture toughness*. International
  parallel to E1820; intentionally aligned in scope and parameter set,
  with minor divergences in side-groove conventions and validity
  bounds.
- **API 579-1 / ASME FFS-1** — *Fitness-for-Service*. Consumes E1820
  outputs (J-based) as Part 9 toughness Option 2 / 3 input; see
  [api-std-579](api-std-579.md).
- **BS 7910** — *Guide to methods for assessing the acceptability of
  flaws in metallic structures* (BSI). UK FFS standard; Annex K
  toughness clause cites E1820 alongside BS 7448 / ISO 12135.
- **ASME BPVC** (Sections III, VIII, XI) — pressure-vessel and
  nuclear-component codes that consume E1820 toughness data via
  reference-temperature shifts (Master Curve, E1921) for brittle-
  fracture screening.

## Sources

- Source page: [og-standards-astm-e-series](../sources/og-standards-astm-e-series.md)[esrc] — catalog row
  `E1820 | J-Integral / Unified Fracture Toughness (J-R curve) | 3 editions in catalog`.
- Catalog provenance: `/mnt/ace/O&G-Standards/_catalog.json`
  (4 entries matching `E1820`; three editions: 1999, 2001, 2006).
- Raw PDFs (read-only, vendor-derivative; do NOT copy into git per
  the spinout 2026-05-05 vendor-PDF firewall):
  - `/mnt/ace/O&G-Standards/ASTM/E-Series/E 1820 - 99  _RTE4MJATOTLB.pdf`
  - `/mnt/ace/O&G-Standards/ASTM/E-Series/E 1820 - 01  _RTE4MJA_.pdf`
  - `/mnt/ace/O&G-Standards/ASTM/E-Series/ASTM E1820 (2006) Standard Test Method for Measurement of Fracture Toughness.pdf`
- Publisher catalogue: <https://www.astm.org/e1820>

[esrc]: ../sources/og-standards-astm-e-series.md
