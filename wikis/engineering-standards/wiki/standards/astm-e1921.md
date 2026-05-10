---
title: "ASTM E1921 — Master Curve and Reference Temperature T0"
slug: astm-e1921
code_id: astm-e1921
publisher: ASTM
revision: "latest (catalog: 1997, 2002, 2003, 2005); current published edition E1921-23a (ASTM)"
tags:
  - astm
  - e-series
  - master-curve
  - brittle-fracture
  - weibull
  - transition-region
  - t0
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
sources:
  - /mnt/ace/O&G-Standards/ASTM/E-Series
  - ../sources/og-standards-astm-e-series.md
extraction_policy: metadata-only
raw_copy_allowed: false
---

# ASTM E1921 — Master Curve and Reference Temperature T0

> **code_id:** `astm-e1921` &nbsp;·&nbsp; **publisher:** ASTM International (Committee E08 — Fatigue & Fracture) &nbsp;·&nbsp; **revision:** latest published edition is E1921-23a; catalog holds four earlier editions (1997, 2002, 2003, 2005)

## Scope

ASTM E1921 specifies a **statistical** test method for determining the
**reference temperature `T₀`** of ferritic structural steels in the
**brittle-to-ductile transition region**, where cleavage fracture
toughness exhibits large specimen-to-specimen scatter and a strong
temperature dependence. `T₀` is defined as the temperature at which the
**median elastic-plastic cleavage toughness** `K_Jc(med)` of a
**1T (one-inch-thick) compact-tension-equivalent** specimen equals
**100 MPa·m^0.5**. From a small set of valid `K_Jc` data points
(typically 6–10 specimens) tested at one temperature — or distributed
across a narrow band of temperatures via the multi-temperature option —
the method fits a **three-parameter Weibull distribution** with fixed
shape modulus and lower-bound `K_min`, applies a **size adjustment** to
1T-equivalent thickness, and reports `T₀` together with **lower-bound
tolerance curves** at 5% and 1% cumulative-failure probability for
direct use in design and fitness-for-service assessment. The method
**replaces drop-weight (NDT) and Charpy-shift correlations** as the
primary reference-temperature measurement for irradiated and unirradiated
ferritic pressure-vessel steels and is the laboratory underpinning of
**ASME Code Case N-629 / N-631** and the analogous routes in API 579-1
Part 9 and BS 7910 Annex J.

## Edition history

Catalog entries observed under `/mnt/ace/O&G-Standards/ASTM/E-Series/`
plus a 2005-edition copy filed (mistakenly) under the D-Series subtree:

| Edition | Year | Catalog filename | Size (B) |
|---------|------|------------------|----------|
| E1921-97 | 1997 | `E 1921 - 97  _RTE5MJETOTC_.pdf` | 195,471 |
| E1921-02 | 2002 | `E 1921 - 02  _RTE5MJETMDI_.pdf` | 290,529 |
| E1921-02 (alt scan) | 2002 | `E 1921 - 02  _RTE5MJETUKVE.pdf` | 205,870 |
| E1921-03 | 2003 | `E 1921 - 03  _RTE5MJE_.pdf` | 267,870 |
| E1921 (2005) | 2005 | `ASTM E1921 (2005) Standard Test Method for Determination of Reference Temperature , T, for Ferritic Steels in the.pdf` | 309,437 |

Source-page summary records **4 editions** for E1921 (the two 2002 scans
are duplicate captures of the same edition; the 2005 PDF is filed under
the D-Series subtree but is genuinely an E-Series document). Current
published edition is **E1921-23a** (not in catalog); intermediate
editions E1921-08, -09, -10, -11, -12, -13, -13a, -14, -15, -16, -17,
-19, -20, -21, -22 and -23 have been issued by ASTM between the 2005
catalog snapshot and the current edition. The 1997 first edition
codified the **Wallin master-curve** concept (see Cross-references); the
2002–2005 cycle added the multi-temperature option and tightened
size-adjustment language; later editions refined the censoring rules for
specimens that exceed the validity ceiling.

## Key concepts

- **Three-parameter Weibull distribution.** Cumulative failure
  probability for cleavage initiation at temperature `T` is modelled as
  `P_f = 1 − exp[ −((K_Jc − K_min)/(K_0 − K_min))^b ]`, with the
  **shape (modulus) fixed at `b = 4`** (theoretically derived from
  weakest-link statistics), a **fixed lower-bound `K_min = 20 MPa·m^0.5`**
  (the minimum cleavage-driving toughness), and the **scale parameter
  `K_0`** estimated from the data. The fixed shape is what allows `T₀`
  to be fitted from a small specimen set.
- **Size adjustment via weakest-link.** Cleavage is governed by the
  probability of a critical particle sampling the high-stress volume
  ahead of the crack front. For thickness `B`, toughness scales as
  `K_Jc(1T) = K_min + (K_Jc(B) − K_min)·(B/25.4 mm)^(1/4)`, so all data
  are normalised to a **1T (25.4-mm) reference thickness** before the
  master curve is fitted. This is the operational "small-specimen-to-
  large-component" bridge.
- **Censored-data treatment.** Specimens that **exceed validity** —
  either because ductile tearing initiates before cleavage, or because
  the measuring capacity ceiling `K_Jc(limit) = √(E·b₀·σ_Y / (30·(1−ν²)))`
  is reached — are **right-censored** rather than discarded; their
  contribution enters the maximum-likelihood estimator for `K_0` as a
  bound rather than a value. This is the key statistical move that lets
  the method survive small specimens.
- **Master Curve and `T₀`.** Once `K_0` (and hence `K_Jc(med)`) is
  estimated, the temperature-dependence of the median is **fixed** by
  the universal relation
  `K_Jc(med) = 30 + 70·exp[ 0.019·(T − T₀) ]` (MPa·m^0.5),
  so a single-temperature dataset locates `T₀` by inverting the
  expression. The full curve and its 5% / 1% tolerance bounds then
  follow without further fitting.
- **Multi-temperature analysis.** When data are scattered across a band
  (typically `T₀ ± 50 °C`), a **maximum-likelihood** estimator combines
  all temperatures simultaneously using the universal exponential
  shape, yielding a single `T₀` with a tighter confidence interval than
  any single-temperature fit.
- **Lower-bound 5% / 1% probability curves for design.** The Weibull
  parameters and the universal temperature shape are inverted to give
  closed-form **lower-tolerance** curves
  `K_Jc(0.05) = 25.4 + 37.8·exp[0.019·(T − T₀)]` and
  `K_Jc(0.01) ≈ 23.5 + 24.4·exp[0.019·(T − T₀)]` (MPa·m^0.5),
  which are the curves consumed downstream by ASME, API 579, and BS 7910
  for setting allowable flaw sizes.

## Application

- **Life-extension assessment of irradiated reactor pressure vessels
  (RPV).** The dominant industrial application: surveillance-capsule
  Charpy data are supplemented or replaced by `T₀` measurements on
  small precracked Charpy `PCVN` specimens to track the
  irradiation-induced shift `ΔT₀` and hence the projected
  pressurised-thermal-shock (PTS) margin. ASME Code Cases **N-629**
  (now incorporated into Section XI App. G) and **N-631** sanction
  `RT_T0 = T₀ + 19.4 °C` as a direct replacement for `RT_NDT` derived
  from the older drop-weight + Charpy procedure.
- **Offshore structural integrity in cold conditions.** Arctic-service
  jacket steels, FPSO topsides, and pipeline-end-manifold welds operate
  in the transition region during low-temperature excursions. E1921
  delivers the lower-bound design toughness used in DNV-OS-F101,
  DNV-RP-C203, and ABS Arctic Class assessments where direct upper-shelf
  J-integral data are unconservative.
- **Weldment-toughness qualification with limited test material.** Heat-
  affected-zone (HAZ) and weld-metal regions in pressure-vessel and
  pipeline welds are typically only millimetres wide, which forces the
  use of small `PCVN` (`SE(B)` 10×10×55 mm) or shallow-notch C(T)
  specimens. The Weibull-with-fixed-shape statistical model is the only
  sanctioned route to a defensible toughness number from such small
  populations, making E1921 the de-facto standard for narrow-zone
  weldment qualification.

## Cross-references

- **ASTM E1820** — *Measurement of Fracture Toughness*. Upstream test
  method that **produces the `K_Jc` inputs** consumed by E1921. The
  load-CMOD records, J-integral conversion, and validity-ceiling
  formulae used inside E1921 are inherited from E1820. See
  [astm-e1820](astm-e1820.md).
- **ASTM E399** — *Linear-Elastic Plane-Strain Fracture Toughness K_Ic
  of Metallic Materials*. Used for the **upper-toughness end of the
  transition** where small-scale yielding still holds and a valid
  `K_Ic` can be measured directly; E1921 takes over once cleavage
  scatter dominates and the LEFM size criterion fails.
- **ASTM E208** — *Drop-Weight Test for Nil-Ductility Transition
  Temperature `T_NDT`*. Predecessor reference-temperature method;
  retained for legacy `RT_NDT` calculations but superseded by E1921 for
  small-specimen and irradiated-steel applications.
- **API 579-1 / ASME FFS-1** — *Fitness-for-Service*. Part 9 brittle-
  fracture screening consumes `T₀` (or `RT_T0`) and the master-curve
  lower bounds via Charpy-correlation lookup tables (Annex 9F) and
  through direct master-curve substitution; see [api-std-579](api-std-579.md).
- **BS 7910** — *Guide to methods for assessing the acceptability of
  flaws in metallic structures* (BSI). Annex J brittle-fracture
  assessment consumes `T₀` data through Charpy-shift correlations and,
  in recent revisions, accepts master-curve lower-bound input directly.
- **ASME BPVC Section XI Appendix G + Code Cases N-629 / N-631** —
  pressure-vessel brittle-fracture rules; sanction `RT_T0 = T₀ + 19.4 °C`
  as a direct substitute for `RT_NDT` in P-T-limit and PTS calculations.
- **K. Wallin (1984, 1989, 1991, 1993)** — VTT papers establishing the
  weakest-link / fixed-modulus / universal-shape master curve that
  underlies the entire E1921 procedure. Background literature; cited
  but not normative.

## Sources

- Source page: [og-standards-astm-e-series](../sources/og-standards-astm-e-series.md)[esrc] — catalog row
  `E1921 | Reference Temperature T₀ for Ferritic Steels (Master Curve) | 4 editions in catalog`.
- Catalog provenance: `/mnt/ace/O&G-Standards/_catalog.json`
  (5 entries matching `E1921`; four editions: 1997, 2002, 2003, 2005;
  one 2005 copy is filed under the D-Series subtree but is genuinely
  an E-Series document).
- Raw PDFs (read-only, vendor-derivative; do NOT copy into git per
  the spinout 2026-05-05 vendor-PDF firewall):
  - `/mnt/ace/O&G-Standards/ASTM/E-Series/E 1921 - 97  _RTE5MJETOTC_.pdf`
  - `/mnt/ace/O&G-Standards/ASTM/E-Series/E 1921 - 02  _RTE5MJETMDI_.pdf`
  - `/mnt/ace/O&G-Standards/ASTM/E-Series/E 1921 - 03  _RTE5MJE_.pdf`
  - `/mnt/ace/O&G-Standards/ASTM/D-Series/ASTM E1921 (2005) Standard Test Method for Determination of Reference Temperature , T, for Ferritic Steels in the.pdf`
- Publisher catalogue: <https://www.astm.org/e1921>

[esrc]: ../sources/og-standards-astm-e-series.md
