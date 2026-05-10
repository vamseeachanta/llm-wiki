---
title: "Fatigue Design and Assessment"
slug: fatigue-design-and-assessment
tags:
  - fatigue
  - sn-curve
  - hot-spot-stress
  - fcg
  - palmgren-miner
  - offshore
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
sources:
  - standards/dnv-rp-c203.md
  - standards/api-rp-2a-wsd.md
---

# Fatigue Design and Assessment

> Concept page. Synthesises engineering practice for fatigue design and assessment of welded and machined metallic structures, with bidirectional links to the standards pages that govern each method. No clause text or table content reproduced from vendor PDFs.

## Fatigue in a sentence

Fatigue is the cumulative degradation of a metallic component under cyclic loading at stress amplitudes well below the static yield strength, comprising three sequential stages — **crack initiation** at a stress raiser (notch, weld toe, surface flaw), **stable crack propagation** under repeated cycling, and **final failure** by net-section yielding, fast fracture, or plastic collapse once the remaining ligament can no longer carry the peak load.

## Two paradigms

Fatigue assessment is performed under one of two methodological paradigms; the choice depends on whether a flaw has been postulated or detected, and on whether the design surface is a welded detail catalogue or a known crack geometry.

| Paradigm | Surface | Inputs | Damage measure | When to use |
|---|---|---|---|---|
| **S-N (stress-life)** | Cyclic stress range vs. number of cycles | Hot-spot or nominal stress range, cycle count, S-N class | Palmgren-Miner sum `D = Σ n_i / N_i` | Default for design and re-assessment of welded details with classifiable geometry; no flaw assumed |
| **Fracture mechanics (FCG)** | Crack-driving force vs. crack growth rate | Initial flaw size, K-solution, da/dN-vs-ΔK law (Paris regime), threshold ΔK<sub>th</sub> | Cycles to grow from `a₀` to `a_crit` | Postulated or NDE-detected crack-like flaw; remaining-life calculation; fitness-for-service; ECA of welded joints with sub-detection flaws |

In practice, design uses S-N (Palmgren-Miner damage summation against a tabulated detail class), while in-service assessment of detected flaws or sub-detection postulated flaws uses FCG (Paris-law integration of `da/dN = C(ΔK)^m`, with `da/dN`-vs-`ΔK` constants determined per ASTM E647). Re-assessment of an aged welded structure can use both: S-N for un-flawed details and FCG for any detected indication.

## Hot-spot stress concept

Welded joints are the dominant fatigue site in offshore steel structures. The stress state at a weld toe is geometry-dependent and singular at the notch root, so fatigue assessment uses one of three stress definitions, each paired with its own S-N family:

- **Nominal stress** — far-field stress in the parent member, ignoring all local geometry. Paired with detail-classified S-N curves (DNV-RP-C203 classes B–W; BS 7608 classes B–W). Cheapest; valid only for catalogued joint geometries.
- **Structural hot-spot stress (HSS)** — linearised structural stress at the weld toe, excluding the local notch singularity but including the geometric stress concentration of the joint. Determined by FE extrapolation from reference points (typically at 0.4·t and 1.0·t from the weld toe for shell/solid models, with linear or quadratic extrapolation per IIW recommendations). Paired with a single hot-spot S-N curve (DNV-RP-C203 D-curve in air, with environmental modifiers). Standard for non-classifiable geometries.
- **Notch stress** (effective notch / 1 mm fictitious radius) — full local stress at a fictitious notch radius (r<sub>f</sub> = 1 mm for steel, IIW). Paired with a master notch-stress S-N. Used for fine-mesh FE assessments of complex weld details.

The **stress concentration factor (SCF)** is the ratio of hot-spot stress to nominal stress for a given joint geometry; for tubular joints DNV-RP-C203 / API RP 2A provide parametric SCF formulae (Efthymiou, Lloyd's Register / Smedley-Fisher) keyed on joint dimensionless ratios (β, γ, τ, α, ζ).

## S-N curve families

S-N curves are detail-class catalogues — each curve is a regression-fit lower-bound (typically mean-minus-two-standard-deviations) through cycles-to-failure test data for a specific weld geometry, loading mode, and environment. Bilinear formulations (two slopes) are standard, with the slope-change "knee" representing the variable-amplitude endurance threshold.

| Family | Curves / classes | Basis |
|---|---|---|
| **DNV-RP-C203** (offshore steel) | B1, B2, C, C1, C2, D, E, F, F1, F3, G, T (tubular), W (weld throat) | Test-data fit, mean-minus-2σ; in-air, seawater-with-CP, and seawater-free-corrosion variants per curve; bilinear with slope change at 10⁷ cycles |
| **AWS D1.1** (US bridge / building steel) | A through F detail categories | Test-data fit on welded steel detail families; nominal-stress only |
| **BS 7608** (UK steel structures) | B, C, D, E, F, F2, G, W | Test-data fit, mean-minus-2σ; nominal-stress; cross-cited from BS 7910 Annex M as the S-N companion to FCG |
| **API RP 2A-WSD** (fixed offshore platforms) | X, X' tubular curves | Tubular-joint test-data fit; hot-spot stress paired |
| **ABS GUI-115** (offshore / FPSO fatigue) | DNV-aligned with ABS-specific environmental modifiers | Test-data fit; FPSO-specific load combinations |

Curves differ on slope (typically m = 3 in the high-cycle regime, m = 5 beyond the knee), constant `a` (intercept), thickness-correction exponents, and environmental factors. **Mixing curves across publishers is unsafe** — each catalogue is internally calibrated against a specific stress definition and detail-classification convention.

## Mean-stress effects

S-N test data are typically generated under fully-reversed loading (R = -1, mean stress = 0). In service, mean stress shifts the fatigue strength: tensile mean stress reduces life, compressive mean stress extends it. Three classical correction surfaces map a stress range with non-zero mean to an equivalent fully-reversed range:

- **Goodman** — linear: `σ_a / σ_e + σ_m / σ_u = 1` (σ_e = endurance limit, σ_u = ultimate). Conservative; default for ductile metals.
- **Gerber** — parabolic: `σ_a / σ_e + (σ_m / σ_u)² = 1`. Less conservative; better fit for ductile steels.
- **Soderberg** — linear vs. yield: `σ_a / σ_e + σ_m / σ_y = 1` (σ_y = yield). Most conservative; used when plastic shakedown is unacceptable.

For welded details, **mean stress is implicitly absorbed** into the S-N curve's residual-stress assumption — as-welded curves assume tensile residual stresses at yield, which dominate any applied mean stress, so explicit mean-stress correction is typically suppressed. For PWHT or stress-relieved welds, mean-stress corrections may be applied per the governing code (e.g., DNV-RP-C203 partial mean-stress benefit for PWHT details).

In offshore service, **tide-wind cycling** generates a slowly-varying mean stress (tide period) superposed on a wave-frequency stress range; the mean component is captured by full rainflow counting on the unfiltered stress history rather than by post-hoc Goodman correction.

## Variable-amplitude loading

Service stress histories are irregular (random or quasi-random), not constant-amplitude. Two devices convert irregular history to a damage equivalent:

- **Rainflow counting** (ASTM E1049) — extracts closed hysteresis loops from a stress-vs-time signal; each loop is a (range, mean) pair. Modern implementations use the four-point algorithm. Output is a histogram (range, mean, count) consumed by either S-N damage summation or FCG cycle integration.
- **Palmgren-Miner linear damage hypothesis** — `D = Σ n_i / N_i`, where `n_i` is the cycle count at stress range `S_i` from rainflow output and `N_i` is the allowable cycles at `S_i` from the chosen S-N curve. Failure at `D ≥ 1.0`; design acceptance at `D ≤ 1/DFF`, where DFF is the design fatigue factor (e.g., 1, 2, 3, or 10 depending on inspectability and consequence per DNV-RP-C203).

**Block loading** is the discretised form: the service spectrum is binned into stress-range blocks (often 10–20 bins) with associated cycle counts, and Miner's rule is applied block-by-block. This is the standard for sea-state-binned spectral fatigue under a Pierson-Moskowitz or JONSWAP wave scatter.

Linearity is the key approximation: Miner's rule ignores load-sequence effects (over-load retardation, under-load acceleration) and threshold effects below ΔK<sub>th</sub>. For high-stress, low-cycle, or sequence-sensitive cases, FCG with explicit retardation modelling supersedes Miner.

## Fatigue + corrosion

Seawater exposure aggressively reduces fatigue life through corrosion-fatigue interaction — surface pitting accelerates initiation, hydrogen ingress (under cathodic protection) embrittles the crack tip, and the protective oxide cannot reform between cycles fast enough at typical wave frequencies (~0.1 Hz). S-N catalogues respond with three environmental tiers:

- **In air** — baseline curves; applicable to topsides, dry hull, and protected interior surfaces.
- **In seawater with cathodic protection (CP)** — modest knock-down (slope unchanged, intercept reduced; bilinear knee may shift) reflecting hydrogen-assisted growth at adequate -800 to -1100 mV<sub>Ag/AgCl</sub> potential.
- **In seawater, free corrosion (no CP)** — severe knock-down; the bilinear knee is often suppressed (single-slope curve continues indefinitely), reflecting the absence of a true endurance limit under corrosion. Applies to splash-zone details where CP is intermittent.

Other environmental cracking mechanisms (sulphide stress cracking per NACE MR0175 / ISO 15156, hydrogen-induced cracking, stress-corrosion cracking in chloride media) interact with fatigue and can drive crack-like flaws into FCG-regime growth at ΔK below the in-air threshold. Sour-service designs require concurrent corrosion-fatigue and SSC compliance.

## Standards

Bidirectional links to the governing publisher pages in this wiki:

- [dnv-rp-c203](../standards/dnv-rp-c203.md) — *Fatigue Design of Offshore Steel Structures* (DNV recommended practice). Primary multi-edition standard for offshore S-N catalogues, hot-spot extrapolation, environmental modifiers, and design fatigue factors. The single most-cited code in `digitalmodel` calc paths.
- [api-rp-2a-wsd](../standards/api-rp-2a-wsd.md) — *Planning, Designing, and Constructing Fixed Offshore Platforms — Working Stress Design* (API RP). Tubular-joint fatigue for fixed offshore platforms; X / X' S-N curves and parametric SCF formulae.
- [abs-gui-115-fatigue-offshore](../standards/abs-gui-115-fatigue-offshore.md) — *Fatigue Assessment of Offshore Structures* (ABS guide). FPSO-oriented fatigue methodology; DNV-aligned curves with ABS-specific environmental and load-combination conventions.
- [api-579-1-asme-ffs-1](../standards/api-579-1-asme-ffs-1.md) — *Fitness-for-Service*. Part 14 covers fatigue assessment of pressurised equipment; Part 9 covers crack-like flaw FCG. Joint API/ASME standard for in-service damage assessment.
- [bs-7910-flaw-assessment](../standards/bs-7910-flaw-assessment.md) — *Guide to Methods for Assessing the Acceptability of Flaws in Metallic Structures* (BSI). Annex M covers FCG-based fatigue (Paris-law constants for ferritic/austenitic steels and aluminium, threshold ΔK<sub>th</sub>, environmental modifiers, R-ratio handling). Cross-cited with [bs-7608](../standards/bs-7608.md) for the S-N companion.

## Related concepts

- [fitness-for-service](fitness-for-service.md) — quantitative damage-tolerance assessment of in-service equipment; consumes FCG outputs from this concept.
- [fracture-toughness-measurement](fracture-toughness-measurement.md) — K<sub>Ic</sub>, J-integral, CTOD test methods (ASTM E399 / E1820 / E1921 / BS 7448) supplying the toughness inputs that bound the FCG integration at `a_crit`.
- [weld-toughness](weld-toughness.md) — Charpy and CTOD acceptance for weld procedure qualification; sets the floor on fracture toughness for fatigue-cracked welds.
- [[riser-fatigue]] — domain-specific application: VIV-driven and wave-frequency fatigue of dynamic risers per [dnv-os-f201](../standards/dnv-os-f201.md).

## Source materials

- [og-standards-api](../sources/og-standards-api.md) — API publisher catalog row (RP 2A-WSD, Std 579, RP 2SK).
- [og-standards-bsi](../sources/og-standards-bsi.md) — BSI publisher catalog (BS 7910, BS 7608, BS 7448).
- [og-standards-dnv](../sources/og-standards-dnv.md) — DNV publisher catalog (RP-C203, OS-E301, OS-F201, RP-C210).

## Notes

- Page is **methodology-level**; no S-N curve constants, FAD curve coordinates, Paris-law `C` and `m` values, or DFF tables are reproduced here. Cite the publisher edition for normative work.
- General engineering knowledge described above is paraphrased from public textbook sources (Schijve, *Fatigue of Structures and Materials*, 2nd ed., Springer 2009; Suresh, *Fatigue of Materials*, 2nd ed., CUP 1998; Almar-Næss, *Fatigue Handbook — Offshore Steel Structures*, Tapir 1985) and is independent of any vendor PDF in the deny-list catalogue.
