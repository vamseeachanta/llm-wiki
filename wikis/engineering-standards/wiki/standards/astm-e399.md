---
title: "ASTM E399 — Plane-Strain Fracture Toughness (K_Ic)"
slug: astm-e399
code_id: astm-e399
publisher: ASTM
revision: "latest in catalog: E399-06 (2006); also E399-90(R97); current published edition E399-23 (ASTM)"
tags:
  - astm
  - e-series
  - fracture-toughness
  - kic
  - plane-strain
  - lefm
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
sources:
  - /mnt/ace/O&G-Standards/ASTM/E-Series
  - ../sources/og-standards-astm-e-series.md
extraction_policy: metadata-only
raw_copy_allowed: false
---

# ASTM E399 — Plane-Strain Fracture Toughness (K_Ic)

> **code_id:** `astm-e399` &nbsp;·&nbsp; **publisher:** ASTM International (Committee E08 — Fatigue & Fracture) &nbsp;·&nbsp; **revision:** latest published edition is E399-23; catalog holds two prior editions (E399-90(R97) and the 2006 edition)

## Scope

ASTM E399 is the original linear-elastic plane-strain fracture-toughness
test method for metallic materials. It returns a single critical
stress-intensity factor `K_Ic` that characterises the resistance to
unstable crack extension under conditions of small-scale yielding
(SSY) and predominantly plane-strain constraint at the crack tip. The
method's central premise is that the candidate toughness, the specimen
thickness `B`, the remaining ligament `(W − a)`, and the material yield
strength `σ_ys` jointly satisfy the **plane-strain validity envelope**

> `B, (W − a), a ≥ 2.5 · (K_Q / σ_ys)²`

so that the plastic zone is small relative to all in-plane and
through-thickness specimen dimensions and the K-field controls
crack-tip stresses. A second validity gate constrains the
load-record shape: the ratio `P_max / P_Q ≤ 1.10`, where `P_Q` is the
load read at the 5% secant offset on the force–CMOD record and `P_max`
is the peak load achieved during the test. When either gate fails the
test produces a candidate value `K_Q` that **does not qualify as
`K_Ic`**, and the operator must either re-test with a larger specimen
or migrate to the elastic-plastic methodology of [ASTM E1820](astm-e1820.md).
E399's regime of applicability is narrow but consequential: it is the
defensible toughness method for high-strength low-toughness alloys
(martensitic steels, high-strength aluminium alloys, titanium alloys)
and for ferritic steels operating below the brittle-ductile transition
where the K-controlled fracture path remains physically meaningful.

## Edition history

Catalog entries observed under `/mnt/ace/O&G-Standards/ASTM/E-Series/`:

| Edition | Year | Catalog filename | parent_root |
|---------|------|------------------|-------------|
| E399-90(R97) | 1990 (reapproved 1997) | `E_399_-_90_R97_RTM5OQ_.pdf` | `/mnt/ace/O&G-Standards/ASTM/E-Series` |
| E399-06 | 2006 | `ASTM E399 (2006) Std Test Method for Linear-Elastic Plane-Strain Fracture Toughness K of Metallic Materials.pdf` | `/mnt/ace/O&G-Standards/ASTM/D-Series` (catalog misfile — see [E-series source page][esrc] §"Bucket purity") |

Source-page tally records **1 edition** for E399 in the headline E08
table; the catalog actually retains **two distinct editions** (the 1990
R97 reapproval and the 2006 edition), with the 2006 PDF physically
mis-bucketed into the D-Series tree but correctly indexed by code in
the catalog. Current published edition is **E399-23** (not in
catalog); intermediate editions E399-08, -09, -12, -17, -20, and -22
have been issued by ASTM between the 2006 catalog snapshot and the
current edition. Historically E399 dates back to the early 1970s and
is the **ancestor** of every modern fracture-toughness test method;
[ASTM E1820](astm-e1820.md) absorbed and generalised the K-only path
into its unified flow but preserved a path back to E399-style
qualification when the load record is linear-elastic.

## Key sections

The standard is organised by laboratory-execution flow. Section
identifiers vary across editions; the topical groupings below are
stable.

- **Apparatus.** Calibrated load frame (force-verified per
  [ASTM E4](#cross-references)); a **clip-on CMOD gage** mounted at
  the crack-mouth knife edges to record the load–displacement trace
  that drives the 5%-secant construction; environmental chamber for
  non-ambient testing. Load-line alignment tolerances are tighter than
  for elastic-plastic methods because plane-strain-K validity is
  sensitive to bending and asymmetry.
- **Specimen geometries.** Standardised proportional specimens:
  compact tension `C(T)`, single-edge-notch bend `SE(B)`, disk-shaped
  compact `DC(T)`, and **arc-tension** specimens machined from
  cylindrical or tubular product. Geometric ratios (typical
  `W = 2·B`, `a/W` target 0.45–0.55) and machining tolerances on
  notch root radius, knife-edge geometry, and load-line eccentricity
  are tabulated per geometry.
- **Pre-cracking by fatigue.** Sharp pre-crack introduced under
  load-controlled cyclic loading at decreasing `ΔK` to a controlled
  final `K_max ≤ 0.6 · K_Ic` (estimated). Final crack length must lie
  in the **`a/W` = 0.45–0.55** window; pre-crack-front straightness
  and front-curvature gates are checked post-test on the broken
  specimen halves; environmental and frequency constraints prevent
  altering the material's fracture toughness during pre-cracking.
- **Test record and `P_Q` construction.** Quasi-static monotonic
  loading with continuous digital recording of force vs. **CMOD**.
  The **5%-secant** construction draws a line from the origin with
  slope 95% of the initial elastic loading slope; the load `P_Q` is
  the lower of (a) the intersection of the secant with the test
  record and (b) any earlier maximum load preceding the intersection.
  Candidate toughness `K_Q` is computed from `P_Q` and the
  standardised geometry-dependent K-calibration `f(a/W)`.
- **Validity criteria.** Two gates must hold for `K_Q` to qualify as
  `K_Ic`:
  1. **Load-ratio gate.** `P_max / P_Q ≤ 1.10` — bounds the amount
     of post-`P_Q` non-linear excursion permitted in the record.
  2. **Specimen-size gate.** `B, (W − a), a ≥ 2.5 · (K_Q / σ_ys)²`
     — enforces small-scale-yielding and predominantly plane-strain
     constraint.
  Crack-front-straightness checks (each of nine equally spaced
  through-thickness positions within prescribed ± tolerance of the
  average physical crack length) and pre-crack-validity checks
  (final-`K_max` history, surface vs. average crack-length offsets)
  apply in parallel. Failing any gate downgrades the result to a
  non-qualifying `K_Q`.

## When to use E399 vs. E1820

E399 and [E1820](astm-e1820.md) report toughness from the same family
of specimen geometries and overlapping pre-cracking procedures, but
they target different material-response regimes.

- **Use E399 when LEFM applies.** The material is high-strength
  and/or low-toughness such that the plane-strain validity envelope
  `B, (W − a), a ≥ 2.5 · (K/σ_ys)²` is satisfied at engineering
  specimen sizes; the load–CMOD record is essentially linear with
  only minor non-linearity at peak (P_max/P_Q ≤ 1.10). Typical
  candidates: **high-strength martensitic steels**, **brittle
  ferritic steels** below the transition, **high-strength aluminium
  and titanium alloys**, and **weldments / heat-affected zones** in
  embrittled condition. The deliverable `K_Ic` plugs directly into
  LEFM-only fitness-for-service paths and into Master-Curve
  reference-temperature data sets ([ASTM E1921](#cross-references)).
- **Use E1820 when ductile tearing or J-controlled growth dominates.**
  The material exhibits substantial plasticity prior to crack
  initiation, the load–CMOD record curves over well before the secant
  intersection, or the plane-strain size requirement would demand
  prohibitively large specimens. This is the regime of **modern
  pipeline steels (X65, X70, X80)**, **offshore structural plate
  (S355, EH36)**, and **most pressure-vessel ferritics on the upper
  shelf or in the upper transition**. E1820 returns `J_Ic`, `J–R`
  curves, and CTOD analogues; it preserves a K-only qualification
  path when the load record happens to be linear-elastic.

In practical fitness-for-service workflows after roughly 2010, E1820
is the default toughness method for offshore and onshore pressure-
containing steels; E399 is reserved for the materials where it
remains genuinely applicable and where its narrower output is exactly
what the downstream consumer (FAD, master curve, brittle-fracture
screening) requires.

## Cross-references

- **[ASTM E1820](astm-e1820.md)** — *Measurement of Fracture
  Toughness*. The unified post-2000 method that absorbs and
  generalises E399's K-only path while adding J-integral, J–R, CTOD,
  and CTOD–R outputs. E1820 is the modern default for materials that
  undergo ductile tearing; E399 remains the defensible method when
  LEFM validity is genuinely satisfied.
- **ASTM E1290** — *Crack-Tip Opening Displacement (CTOD) Fracture
  Toughness Measurement*. CTOD-only method, partially supplanted by
  E1820 as the unified standard added the CTOD-R-curve path; in many
  weldment-qualification programs E1290-style CTOD remains the
  contractual deliverable alongside (or in place of) E399 `K_Ic`.
- **ASTM E1921** — *Reference Temperature `T₀` for Ferritic Steels in
  the Transition Range (Master Curve)*. Downstream method that
  consumes E1820 and E399 toughness data points (typically C(T) or
  PCVN specimens) to fit the Master Curve and report `T₀`.
- **ASTM E561** — `K–R` curve method for thin-section / plane-stress
  toughness. Complementary to E399 in the geometry where plane-strain
  validity cannot be satisfied because `B` is small relative to the
  plastic-zone size.
- **ASTM E647** — *Measurement of Fatigue Crack Growth Rates (da/dN
  vs. ΔK)*. Complementary fatigue-crack-growth method; E647
  quantifies sub-critical crack growth where E399 quantifies critical
  toughness for unstable extension.
- **ASTM E4** — *Force Verification of Testing Machines*. Mandatory
  upstream calibration for any E399 test.
- **BS 7448** — UK *Fracture mechanics toughness tests* (parts 1–4
  covering K, CTOD, J on parent metal and weldments). Parallel
  national standard; BS 7448 Part 1 is the UK analogue of E399 for
  K-based testing.
- **ISO 12135** — *Metallic materials — Unified method of test for
  the determination of quasistatic fracture toughness*. International
  parallel; intentionally aligned in scope with the E1820 unified
  method but preserves an E399-style K_Ic qualification path.
- **API 579-1 / ASME FFS-1** — *Fitness-for-Service*. Consumes E399
  `K_Ic` (LEFM Option 1 / 2) and E1820 J-based toughness inputs in
  Part 9 flaw-assessment procedures; see [api-std-579](api-std-579.md) when its
  page lands.
- **BS 7910** — *Guide to methods for assessing the acceptability of
  flaws in metallic structures* (BSI). UK FFS standard; cites E399
  alongside BS 7448 / ISO 12135 / E1820 for toughness inputs to FAD
  Level 1 / 2 / 3 assessments.

## Sources

- Concept-page consumer: [fracture-toughness-measurement](../concepts/fracture-toughness-measurement.md)
  — cross-references E399 in its `K_Ic` row and in its small-scale-
  yielding ancestry note; this standards page is the bidirectional
  target.
- Source page: [og-standards-astm-e-series](../sources/og-standards-astm-e-series.md)[esrc] — catalog row
  `E399 | Plane-strain Fracture Toughness K_IC of Metallic Materials |
  1 edition (headline) / 2 editions (catalog rows)`.
- Catalog provenance: `/mnt/ace/O&G-Standards/_catalog.json` (2 entries
  matching `E399`; 1990 R97 reapproval and 2006 edition).
- Raw PDFs (read-only, vendor-derivative; do NOT copy into git per
  the spinout 2026-05-05 vendor-PDF firewall):
  - `/mnt/ace/O&G-Standards/ASTM/E-Series/E_399_-_90_R97_RTM5OQ_.pdf`
  - `/mnt/ace/O&G-Standards/ASTM/D-Series/ASTM_E399_(2006)_Std_Test_Method_for_Linear-Elastic_Plane-Strain_Fracture_Toughness_K_of_Metallic_Materials.pdf`
    (filesystem path reflects the catalog mis-bucket noted above)
- Publisher catalogue: <https://www.astm.org/e0399-23.html>

[esrc]: ../sources/og-standards-astm-e-series.md
