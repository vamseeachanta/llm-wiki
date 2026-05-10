---
title: "Fatigue Crack Growth (FCG)"
slug: fatigue-crack-growth
tags:
  - fatigue-crack-growth
  - paris-erdogan
  - da-dn
  - threshold
  - r-ratio
  - crack-closure
  - astm-e647
  - fcg
added: 2026-05-10
last_updated: 2026-05-10
domain: engineering-standards
sources:
  - standards/astm-e647.md
  - standards/bs-7910-flaw-assessment.md
  - standards/dnv-rp-c203.md
---

# Fatigue Crack Growth (FCG)

## Why fatigue-crack-growth matters

Fatigue crack growth (FCG) is the **sub-critical, cycle-by-cycle
extension of a sharp crack** under fluctuating stress, governed by the
range of the crack-tip stress-intensity factor `ΔK = K_max − K_min`
rather than by remote nominal stress. It is the **damage-tolerance**
half of fatigue-life accounting and stands as the operational
counterpart to S-N (total-life) analysis used elsewhere in
[fatigue-design-and-assessment](fatigue-design-and-assessment.md). Where
S-N curves treat the structure as crack-free until end of life, FCG
acknowledges that **manufactured flaws, weld defects, corrosion pits,
and in-service indications already exist** and asks the falsifiable
question: how many remaining cycles before this flaw reaches a
critical size?

The engineering significance of FCG is that it underwrites the
**inspection interval**, **leak-before-break licensing**, and
**ECA-based weld-acceptance** in offshore, pressure-vessel, pipeline,
nuclear, and aerospace service. Every modern fitness-for-service
calculation, [BS 7910 Annex L](../standards/bs-7910-flaw-assessment.md)
flaw-growth assessment, and [DNV-RP-C203](../standards/dnv-rp-c203.md)
ECA appendix consumes a `da/dN`-vs-`ΔK` law as the **integrand** for
predicted remaining life. Get the law wrong — wrong threshold, wrong
exponent, wrong R-ratio adjustment — and the licensed inspection
interval is wrong by the same multiplicative error.

## Doctrinal evolution

**1963 — Paris and Erdogan** publish the empirical observation that
fatigue-crack-growth rate `da/dN` correlates linearly with the stress-
intensity-factor range `ΔK` on a log-log plot, over a substantial
mid-range of growth rates, for a wide variety of metals. This
**Paris-Erdogan equation** `da/dN = C·(ΔK)^m` collapses the prior
nominal-stress-based ad-hoc fits and supplies a single material-pair-
of-constants `(C, m)` that travels across geometry, load, and
specimen size. The reformulation is the founding act of
**damage-tolerant design**.

**1970s — da/dN-vs-ΔK characterization broadens.** The Paris regime is
recognized as the central (Region II) part of a three-region curve:
**Region I** (near-threshold, sharp downturn at `ΔK_th`), **Region II**
(Paris-linear, the design-relevant window), and **Region III** (rapid
final-fracture acceleration as `K_max → K_c`). **Elber (1970)** then
identifies **plasticity-induced crack closure** as the mechanism
behind the observed R-ratio dependence — the idea that a crack
remains closed for part of its tensile cycle, so that the **effective**
range `ΔK_eff = K_max − K_open` drives growth, not the nominal `ΔK`.

**1978 — ASTM E647** publishes the first standardized test method for
measuring `da/dN`-vs-`ΔK`. Specimen geometries (CT, M(T), ESE(T)),
load-shedding for threshold determination, optical and compliance
crack-length monitoring, and validity criteria for K-dominance are all
codified. E647 becomes the upstream data-generator for every modern
FCG database (ESDU, NIMS, NRIM, MIL-HDBK-5).

**1980s-1990s — Newman crack-closure model and modern damage-tolerance
methodology.** **Newman (1981)** provides an analytical framework for
plasticity-induced closure that lets practitioners convert nominal-`ΔK`
data into `ΔK_eff` for arbitrary R-ratio service. The aerospace
community (ASIP, ENSIP, USAF damage-tolerance philosophy) and the
nuclear pressure-vessel community (ASME Section XI Appendix A flaw
evaluation) institutionalize FCG as the inspection-interval driver.

**2000s-present — environmentally-assisted FCG and variable-amplitude
loading.** [BS 7910](../standards/bs-7910-flaw-assessment.md) and
[DNV-RP-C203](../standards/dnv-rp-c203.md) codify **two-slope** FCG
laws, **seawater + cathodic-protection** environmental tiers, and
**marine free-corrosion** acceleration. ISO 12108 harmonizes the
European fatigue-crack-growth method with E647. Variable-amplitude
overload-retardation effects are still a research frontier; design
codes default to constant-amplitude `ΔK` integration with an
explicit conservatism factor.

## The Paris-Erdogan equation and the three regions

The canonical FCG law is:

```
da/dN = C · (ΔK)^m
```

with `da/dN` in m/cycle (or mm/cycle), `ΔK` in MPa·√m (or N·mm^-1.5),
and `(C, m)` a material- and environment-specific pair of constants.
For ferritic structural steels in air, typical values are
`m ≈ 3` and `C ≈ 6 × 10⁻¹²` (m/cycle, MPa·√m units), giving a `da/dN`
of order 10⁻⁹ m/cycle at `ΔK = 10` MPa·√m and 10⁻⁶ m/cycle at
`ΔK = 100` MPa·√m. The cube law is robust enough that BS 7910 Table
8 and DNV-RP-C203 Table 2-2 use it as the default for ferritic
in-air fatigue.

**Region I — near-threshold.** At low `ΔK` the curve **bends sharply
downward** to the **threshold stress-intensity range `ΔK_th`** below
which no crack growth occurs (operationally, growth slower than ~10⁻¹⁰
m/cycle). Threshold is strongly R-ratio dependent (high R reduces
closure, lowers `ΔK_th`) and microstructure-sensitive. Typical
ferritic-steel `ΔK_th` is 5-7 MPa·√m at R = 0.1, falling to 2-3
MPa·√m at R = 0.7. Threshold is the **design margin** behind
infinite-life claims for fatigue-rated welds and bolted connections.

**Region II — Paris-linear.** This is the working window of the law.
Linearity on log-log axes spans roughly two-and-a-half decades of
`da/dN` (10⁻⁸ to 10⁻⁵ m/cycle). All inspection-interval calculations
for crack-tolerant structures live in Region II. Material-environment
combinations are catalogued by their `(C, m)` pair: ferritic-in-air
(`m≈3`), ferritic-in-seawater-with-CP (`m≈3.42`, ~×2 acceleration),
ferritic-in-seawater-free-corrosion (`m≈5.1`, ~×3-5 acceleration),
austenitic-in-air (`m≈3`), aluminium-aerospace (`m≈3-4`).

**Region III — final fracture.** As `K_max` approaches the static
fracture toughness `K_c` (or `K_Jc`, or `K_mat`), `da/dN` accelerates
sharply and the curve sweeps upward asymptotically. The cycle count
in Region III is small (a few hundred to a few thousand cycles
typically) so it is omitted from inspection-interval integration but
**defines the critical crack size `a_c`** as the upper integration
limit. Region III meets the [brittle-fracture](brittle-fracture.md)
and [fracture-toughness-measurement](fracture-toughness-measurement.md)
domains: `K_c` is the same material toughness that governs unstable
fracture under monotonic load.

## R-ratio and crack-closure effects

The Paris equation in its simplest form ignores the **mean stress**
(or stress ratio `R = σ_min / σ_max = K_min / K_max`). Empirically
`da/dN` rises with R for fixed `ΔK` — high mean stress accelerates
crack growth. Two principal mechanisms explain this dependence:

**Plasticity-induced crack closure (Elber 1970).** A growing fatigue
crack leaves a wake of plastically-stretched material along the crack
flanks. On unloading, this stretched wake interferes with full crack-
face contact, so the crack physically **closes at a positive load
`K_open`**. Only the load excursion above `K_open` drives crack-tip
deformation. The effective stress-intensity range is
`ΔK_eff = K_max − K_open`, which is smaller than the nominal `ΔK`
when `R` is low (large compressive component, more closure). At high
`R` the minimum load already exceeds `K_open` and `ΔK_eff = ΔK`. The
**Newman closure model (1981)** parameterizes `K_open / K_max` as a
function of R, `K_max / σ_flow`, and constraint, and is the analytical
backbone of modern damage-tolerance software.

**Roughness-induced and oxide-induced closure.** At low `ΔK` (near
threshold) the crack-flank roughness and oxide debris contribute
additional contact mechanisms; the result is a **steeper R-ratio
sensitivity** of `ΔK_th` than of mid-Region-II growth. This is why
threshold values are quoted with their R-ratio and why `ΔK_th(R=0.7)`
is significantly lower than `ΔK_th(R=0.1)` for the same steel.

**Walker, Forman, and NASGRO formulations.** Several closed-form
generalizations of Paris-Erdogan absorb the R-dependence:

- **Walker:** `da/dN = C · ((1−R)^(γ−1) · ΔK)^m` with γ a fitted
  Walker exponent; collapses R-ratio data onto a single line.
- **Forman:** `da/dN = C · (ΔK)^m / ((1−R)·K_c − ΔK)`; embeds
  Region III rollover via `K_c` in the denominator.
- **NASGRO equation** (Forman-Mettu-Newman, 1990s): unifies Regions
  I, II, and III with explicit threshold and toughness asymptotes;
  default formulation in NASGRO® and the AFGROW life-prediction code.

For offshore, marine, and pressure-vessel ECA work, the simpler
two-segment **mean-fit + 95%-confidence** law of BS 7910 Table 8 is
the practical default; aerospace work uses NASGRO or its equivalents.

## Test methods and standards

The data underlying every FCG law come from **standardized
load-controlled fatigue tests on pre-cracked compact-tension or
middle-tension specimens** with continuous crack-length monitoring:

- **[ASTM E647](../standards/astm-e647.md)** — *Standard Test Method
  for Measurement of Fatigue Crack Growth Rates*. The dominant North
  American standard. Specimen geometries: C(T), M(T), ESE(T). Crack
  length tracked by **direct-current potential drop (DCPD)**,
  **compliance**, or visual measurement. Threshold determination by
  **load-shedding** at decreasing `ΔK`, with a normalized K-gradient
  `C = (1/K)·dK/da ≥ −0.08 mm⁻¹` to avoid history-dependent threshold
  artifacts. Validity gates check for **K-dominance** (uncracked
  ligament, specimen size), **constant R**, and **steady-state**
  growth over the reported `ΔK` range.

- **ISO 12108** — *Metallic materials — Fatigue testing — Fatigue
  crack growth method*. The European harmonized standard, broadly
  compatible with E647 specimen geometries and load-shedding
  protocols, with minor differences in validity-window definitions
  and reporting format. Cited by [BS 7910](../standards/bs-7910-flaw-assessment.md)
  Annex L as an acceptable data source.

- **[BS 7910](../standards/bs-7910-flaw-assessment.md) Annex L** —
  *Compendium of recommended fatigue-crack-growth-rate data for steels
  and aluminium alloys*. Codified two-segment laws for steels in
  air, in seawater with cathodic protection, and in seawater free-
  corrosion. Provides **mean** and **mean + 2σ** (97.5%) curves for
  use as best-estimate and conservative-design inputs respectively.

- **[DNV-RP-C203](../standards/dnv-rp-c203.md)** — *Fatigue design of
  offshore steel structures*. Section 2.3 supplies the recommended
  FCG laws for ECA-supplemented S-N analysis; values are aligned with
  BS 7910 Annex L. Typical recommended pair: `m = 3.0`, `C = 5.21 ×
  10⁻¹³` (mm/cycle, N·mm⁻¹·⁵ units) for ferritic steel in air.

- **[BS 7608](../standards/bs-7608.md)** — *Guide to fatigue design
  and assessment of steel products*. Predominantly an S-N standard
  but Annexes cite FCG data for ECA-supplemented life calculation
  consistent with BS 7910 Annex L.

- **[ASME BPVC Section VIII Division 2](../standards/asme-bpvc-viii-2.md)**
  — pressure-vessel design code; Appendix 5 historically and the
  current Annex 5-F provide FCG data and the integration framework
  for fatigue-flaw-evaluation in pressure-vessel ECA.

## Practitioner application

**Offshore — pipeline girth-weld ECA.** A typical sub-sea pipeline
girth-weld ECA per [DNV-OS-F101](../standards/dnv-st-f101.md) /
[DNV-RP-C203](../standards/dnv-rp-c203.md) accepts a flaw of size
`(a, c)` if integrating `da/dN = C·(ΔK)^m` from initial to critical
size yields a cycle count exceeding the design fatigue life with
appropriate safety factor. Inputs: stress histogram from installation
+ operation, weld-toughness `K_mat`, FCG law in the relevant
environment (air for installation; seawater + CP for in-service
flooded systems). Output: pass / fail flaw acceptance.

**Offshore — riser fatigue and SCR fatigue hot-spots.** Steel
catenary risers (SCRs) accumulate VIV and wave-fatigue cycles at the
touchdown zone. ECA on the welded girth-welds in this zone uses
FCG integration to license inspection intervals; the seawater-with-CP
acceleration factor (~×2 in `da/dN`) is the dominant cost driver.

**Pipeline — sour-service and HISC interaction.** When H₂S is present
the FCG law accelerates further (typically ×3-10 in `da/dN`,
material-and-pH dependent), and the [hydrogen-embrittlement](hydrogen-embrittlement.md)
mechanism couples to the FCG mechanism. ECA uses the highest
applicable acceleration factor as a conservative envelope.

**LNG cryogenic equipment.** Below the [brittle-fracture](brittle-fracture.md)
transition, FCG is suppressed but `K_c` is also suppressed, so
**critical crack size shrinks** and the inspection interval can be
short despite slow growth. The [master-curve-and-transition-temperature](master-curve-and-transition-temperature.md)
methodology supplies the temperature-dependent `K_mat` for the
upper integration limit.

**Pressure-vessel — ASME Section VIII Division 2 fatigue-flaw
evaluation.** A registered crack-like indication is integrated forward
in time using FCG laws and the operational stress histogram; if the
integrated remaining life exceeds the next inspection interval with
margin, the vessel returns to service under enhanced monitoring
rather than being repaired or retired.

**Aerospace — damage-tolerance philosophy.** Every primary structural
joint in a transport-category aircraft is designed under the
assumption that an undetectable initial flaw exists and grows under
service loads; inspection thresholds are set so that the flaw is
detected before it reaches critical size with a specified
probability of detection (POD) margin.

## Industry adoption — FFS, fitness-for-service, and damage-tolerance frameworks

FCG integration is the **engine** behind multiple consumer frameworks:

- **[Engineering Critical Assessment (ECA)](engineering-critical-assessment.md)**
  — alternative weld-acceptance approach; fatigue branch consumes FCG
  integration to demonstrate that a weld flaw will not grow to
  critical size in the design life.
- **[Fitness-for-Service (FFS)](fitness-for-service.md)** — in-service
  flaw evaluation per [API 579-1 / ASME FFS-1](../standards/api-std-579.md)
  Part 9; FCG integration drives the remaining-life calculation.
- **[Leak-before-break (LBB)](leak-before-break.md)** — stability +
  detectability margin; FCG sets the time available between leak
  detection and break.
- **ASME Section XI Appendix A** — flaw-evaluation procedures for
  in-service nuclear pressure vessels; FCG data are tabulated
  explicitly with environmental-tier multipliers.
- **MIL-HDBK-5 / MMPDS** — aerospace-alloy material properties
  handbook; tabulates `da/dN`-vs-`ΔK` curves for design.
- **NASGRO® / AFGROW** — life-prediction software using the unified
  Forman-Mettu-Newman equation; standard tooling for aerospace
  damage-tolerance compliance.

## Standards

- [astm-e647](../standards/astm-e647.md) — *Measurement of Fatigue
  Crack Growth Rates*; the upstream data-generator standard for FCG.
- [bs-7910-flaw-assessment](../standards/bs-7910-flaw-assessment.md)
  — *Guide to methods for assessing the acceptability of flaws in
  metallic structures*; Annex L FCG-data compendium and integration
  rules.
- [bs-7608](../standards/bs-7608.md) — *Guide to fatigue design and
  assessment of steel products*; S-N companion with FCG cross-
  references.
- [dnv-rp-c203](../standards/dnv-rp-c203.md) — *Fatigue design of
  offshore steel structures*; Section 2.3 FCG inputs for ECA branch.
- [dnv-rp-c210](../standards/dnv-rp-c210.md) — *Probabilistic methods
  for planning of inspection for fatigue cracks in offshore
  structures*; consumes FCG integration in the POD-coupled
  inspection-planning Bayesian update.
- [asme-bpvc-viii-1](../standards/asme-bpvc-viii-1.md) /
  [asme-bpvc-viii-2](../standards/asme-bpvc-viii-2.md) — pressure-
  vessel design codes; Section VIII Division 2 fatigue-flaw-evaluation
  Annex consumes FCG laws.
- [api-std-579](../standards/api-std-579.md) — *Fitness-for-Service*;
  Part 9 (Crack-Like Flaws) integrates FCG laws for remaining-life
  prediction.

## Related concepts

- [fatigue-design-and-assessment](fatigue-design-and-assessment.md)
  — total-life (S-N) sibling paradigm; FCG is the damage-tolerance
  half of the same fatigue-assessment whole.
- [mechanical-fatigue](mechanical-fatigue.md) — mechanism-of-damage
  parent concept covering HCF / LCF / VHCF regimes; FCG integration
  is mechanism-agnostic but consumes the same load histogram.
- [fracture-toughness-measurement](fracture-toughness-measurement.md)
  — supplies the upper-bound `K_mat` that defines `a_c` (critical
  crack size) at the top of the FCG integration.
- [brittle-fracture](brittle-fracture.md) — Region III final-fracture
  domain; the meeting place of fatigue and unstable fracture.
- [master-curve-and-transition-temperature](master-curve-and-transition-temperature.md)
  — companion concept; supplies temperature-dependent toughness for
  the FCG upper integration limit in transition-region service.
- [engineering-critical-assessment](engineering-critical-assessment.md)
  — primary downstream consumer of FCG integration in weld-
  acceptance and remaining-life workflows.
- [fitness-for-service](fitness-for-service.md) — in-service consumer;
  Part 9 crack-like-flaw evaluation.
- [thermal-fatigue](thermal-fatigue.md) — variant FCG driver where
  temperature cycles supply the `ΔK` amplitude.

## Source materials

- [`sources/og-standards-astm-e-series.md`](../sources/og-standards-astm-e-series.md)
  — catalog summary of the ASTM E-series fracture-mechanics test
  methods, including E647.
- [`sources/og-standards-bsi.md`](../sources/og-standards-bsi.md)
  — BSI publisher slice covering BS 7910 and BS 7608.
- [`sources/og-standards-dnv.md`](../sources/og-standards-dnv.md)
  — DNV publisher slice covering RP-C203 and RP-C210.
