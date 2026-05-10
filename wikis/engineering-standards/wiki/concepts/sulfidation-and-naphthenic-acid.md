---
title: "Sulfidation and Naphthenic-Acid Corrosion"
slug: sulfidation-and-naphthenic-acid
tags:
  - sulfidation
  - nac
  - naphthenic-acid
  - refinery
  - crude-distillation
  - mod-mcconomy
  - couper-gorman
  - high-temperature
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
sources:
  - standards/api-rp-571.md
---

# Sulfidation and Naphthenic-Acid Corrosion

> Concept anchor for the two dominant high-temperature wall-loss mechanisms on refinery hot-circuit equipment — crude distillation, vacuum distillation, FCC slurry, and hydroprocessing inlet/outlet piping. Sits downstream of [[damage-mechanism-screening]] (which flags credible mechanisms) and feeds [[corrosion-rate-measurement]] (which interprets the measured wall-loss number per mechanism). Bidirectional with [[risk-based-inspection]] (POF input via API RP 581 thinning damage factor) and [[fitness-for-service]] (FFS Part 4 / Part 5 thinning assessment when wall loss exceeds T_min).

## What is sulfidation?

**Sulfidation** is the high-temperature reaction between hydrogen sulfide (H2S) and organic sulfur compounds in crude oil and the iron in steel, forming an iron-sulfide (FeS) scale. The reaction is thermally activated and operates over the range **~230 °C – 540 °C (450 – 1000 °F)**, with the rate accelerating sharply with both **temperature** and **total sulfur content** in the process stream. The protective character of the iron-sulfide scale depends strongly on the alloying chromium content of the substrate; chromium-bearing alloys form a more adherent, more protective Cr-rich sulfide layer than carbon steel does, which is why the alloy ladder for sulfidation tracks chromium content rather than nickel or molybdenum.

Sulfidation is the dominant wall-loss mechanism for hot-circuit refinery equipment that handles sulfur-bearing hydrocarbon streams without aqueous water present. It is the textbook high-temperature damage mechanism on:

- Crude distillation transfer lines (atmospheric-tower feed and overhead vapour outlets above the dew point)
- Atmospheric-tower internals (trays, reflux returns, strippers in the hot zone)
- Vacuum-tower transfer line and flash-zone internals
- FCC main fractionator slurry circuit
- Hydrotreater / hydrocracker reactor inlet and outlet piping (combined with H2 partial pressure → "sulfidation in H2/H2S service")
- Coker fractionator and visbreaker hot-product piping

Two regime distinctions matter for screening:

- **Sulfidation without H2** (crude unit, FCC slurry, coker) — governed by the original **McConomy** correlation and its alloy-specific curves.
- **Sulfidation in H2/H2S service** (hydroprocessing) — governed by the **modified Couper–Gorman** correlation, which captures the rate-accelerating effect of hydrogen partial pressure that the crude-unit-only McConomy curves do not model.

## Couper–Gorman / McConomy curves

The empirical correlation behind sulfidation rate prediction takes the general form:

```
log(corrosion rate) = f(T, S%, alloy)
```

with separate alloy-specific curve families parameterised by **temperature** (Arrhenius-style activation), **total stream sulfur content (wt%)**, and in the H2/H2S variant by **hydrogen partial pressure**. The historical lineage is:

- **McConomy (1963)** — original empirical correlation for sulfur-containing crude oil and crude-unit hot-circuit service. Derived from refinery field-data regression on a per-alloy basis.
- **Couper–Gorman (1971)** — extension to refinery streams generally, including FCC and coker streams, with broader sulfur-content range.
- **Modified Couper–Gorman** (as embedded in **API RP 571** and **API RP 581**) — current-generation model that captures hydrogen-rich service (hydrotreater / hydrocracker) where the H2 partial pressure measurably accelerates sulfidation rate beyond the H2-free McConomy prediction.

The curves are published per **alloy class** — the alloy ladder used across all three correlation families is essentially the same:

| Alloy class | Representative grades | Sulfidation behaviour |
|---|---|---|
| Carbon steel | A106-B, A53-B, A516-70 | Highest rate; baseline for the curve family |
| 5Cr–0.5Mo | P5, T5 | Modest improvement over CS; still rate-vulnerable |
| 9Cr–1Mo | P9, T9, P91/T91 (mod-9Cr) | Significant improvement; common workhorse alloy |
| 12Cr | 410 SS / P12 / P122 | Step-improvement at the 12% Cr threshold |
| 18Cr–8Ni austenitic | 304 SS, 316 SS | Substantially lower rate; also common for NAC |
| 18-13-3 / Ti or Nb stabilised | 321 SS, 347 SS | Equivalent sulfidation behaviour to 304/316 with PASCC mitigation |
| 25Cr–20Ni | 310 SS | Highest-Cr austenitic; strongest sulfidation resistance in the wrought-stainless ladder |

For normative rate prediction, cite the publisher edition of [[api-rp-571]] (mechanism description and alloy guidance) or [[api-rp-581]] (quantitative thinning damage factor with the modified Couper–Gorman embedding) directly. The curves themselves — coordinates, coefficients, and rate-band tables — are not reproduced here per the spinout's metadata-only policy on vendor-derivative content.

## What is naphthenic-acid corrosion (NAC)?

**Naphthenic-acid corrosion (NAC)** is the corrosion of refinery equipment by **carboxylic acids** present in crude oil distillates. The naphthenic-acid family is a heterogeneous mixture of cyclopentane-and-cyclohexane carboxylic acids (R-COOH) that distil out of crude oil over a characteristic boiling range of approximately **232 – 427 °C (450 – 800 °F)**. NAC is the second dominant high-temperature wall-loss mechanism on refinery hot-circuit equipment, often co-located with sulfidation but operating by a distinct chemical pathway (organic-acid attack rather than sulfide-scale formation).

The screening metric is the crude or distillate fraction's **Total Acid Number (TAN)**, expressed in mg KOH per g of oil and measured per ASTM D664. Operational thresholds:

- **TAN < 0.5** — generally not a concern; carbon steel is acceptable in most refinery hot circuits.
- **TAN 0.5 – 1.5** — NAC is credible; alloy upgrade often warranted, especially in high-velocity zones.
- **TAN > 1.5** — NAC is aggressive; molybdenum-bearing alloys are typically required.
- **TAN > 3.0** — high-Mo austenitic stainless (Type 316/317 or higher) is typically the minimum acceptable metallurgy.
- **TAN > 5.0** — exotic CRA territory; Alloy 904L or higher-Mo CRAs are credible candidates.

NAC is **velocity-dependent** — the corrosion rate scales with shear rate at the metal surface, because the protective oil film is shear-thinned and fresh acid is continuously delivered to the wall. This is the chemical reason NAC concentrates at vacuum-line elbows, downstream of injection points, in vacuum-gas-oil (VGO) side draws, in FCC slurry, and at the crude column flash zone. A given TAN value combined with low velocity may not produce significant NAC; the same TAN combined with high velocity can produce wall loss rates measured in mm/yr.

The **molybdenum content** of the alloy is the dominant materials-selection parameter for NAC, in contrast to sulfidation where chromium dominates. This is the reason the NAC alloy ladder and the sulfidation alloy ladder do not align cleanly — and the reason combined sulfidation + NAC service drives toward Mo-bearing **and** Cr-bearing alloys (e.g., Type 316/317 SS with both ≥ 18% Cr and ≥ 2% Mo).

## NAC alloy ladder

| TAN (mg KOH/g) | Velocity | Adequate alloy |
|---|---|---|
| < 0.5 | Any | Carbon steel |
| 0.5 – 1.5 | Low | 5Cr–0.5Mo with close inspection |
| 0.5 – 1.5 | Medium-High | 9Cr–1Mo |
| 1.5 – 3.0 | Any | 12Cr (Type 410 SS) or 9Cr–1Mo |
| 3.0 – 5.0 | Any | Type 316 / 317 SS (Mo content critical) |
| > 5.0 | Any | Alloy 904L or higher-Mo CRA |

The ladder is illustrative of typical refining experience. Asset-specific alloy selection must account for the operator's specific feedstock TAN distribution, blending strategy, hot-circuit velocity profile, sulfur-content overlay (which shifts the alloy choice toward higher-Cr grades to handle sulfidation simultaneously), and any inhibitor-injection programme (phosphate-ester or imidazoline-based NAC inhibitors are sometimes deployed as a complement to metallurgical upgrade rather than a replacement for it).

## Sulfidation + NAC interaction

Sulfidation and NAC occur in the **same refinery domain** — high-temperature hydrocarbon piping and column internals on the crude unit, vacuum unit, FCC main fractionator, and hot-side of the hydroprocessing complex — and frequently in **adjacent equipment** on the same circuit. The total mass-loss rate from both mechanisms can be the governing damage rate for an asset, and alloy-selection logic frequently must satisfy both simultaneously:

- NAC drives the requirement for **molybdenum content** (≥ 2% Mo for aggressive service).
- Sulfidation drives the requirement for **chromium content** (≥ 9% Cr for hot service, stepping up at the 12%-Cr austenitic threshold).

Type 316 / 317 SS and the 18-13-3 stabilised stainless steels (Type 321, 347) sit at the intersection — adequate Cr for sulfidation and adequate Mo for moderate NAC. Above TAN ≈ 3 with elevated velocity, the alloy choice is driven by NAC alone (Mo dominates) and the sulfidation margin comes for free with the higher Cr content of the candidate CRA. Below TAN ≈ 0.5, sulfidation dominates and the alloy ladder collapses to the McConomy / Couper–Gorman curves.

The corollary for inspection planning: a CML (Condition Monitoring Location) on a hot-circuit elbow may be tracking the **sum** of the two rate contributions, and a sudden acceleration in STCR (short-term corrosion rate per [[corrosion-rate-measurement]]) can indicate a TAN excursion in the crude slate even if the bulk sulfur content has not changed. Diagnostic separation typically requires a feed-stream TAN trend, a sulfur trend, and the metallurgy of the affected component.

## Inspection

The inspection programme for sulfidation + NAC service is built on three layers:

1. **UT thickness at high-velocity zones** — manual UT or AUT on elbows downstream of injection points, vacuum-tower transfer-line elbows, FCC slurry tees, and crude-column flash-zone internals. CML density per [[api-510]] / [[api-570]] is biased toward locations where shear rate is highest, since NAC rate scales with velocity.
2. **Velocity surveys** — computational (CFD) and ultrasonic-tracer surveys to map shear-rate distribution along high-risk circuits, particularly after a feedstock change or a debottlenecking project that increases throughput. NAC risk shifts with shear-rate distribution; CML placement based only on the original-design flow regime can miss damage that has migrated.
3. **Feed-stream and intermediate-stream chemistry monitoring** — sulfur content (wt%) and TAN (mg KOH/g) trended on every feed and key intermediate stream (atmospheric-residue, vacuum-residue, VGO side draws, FCC slurry). Step-changes in either trend prompt re-screening of the affected circuit, reassessment of the metallurgy adequacy, and adjustment of inspection-interval if STCR/LTCR (per [[corrosion-rate-measurement]]) has accelerated.

Damage-mechanism screening and CML placement for combined sulfidation + NAC service is a recurring theme in [[damage-mechanism-screening]]; consult that page for the broader unit-by-unit screening framework that situates this concept page in the integrity-management workflow.

## Standards

Bidirectional cross-references — each standards page below should cross-link back to this concept page once the convention propagates.

- [[api-rp-571]] — *Damage Mechanisms Affecting Fixed Equipment in the Refining Industry.* Mechanism catalogue; sulfidation and NAC are entries in the high-temperature corrosion family (RP 571 §5). Primary technical-content anchor.
- [[api-rp-581]] — *Risk-Based Inspection Methodology.* Quantitative RBI; embeds the modified Couper–Gorman correlation in the **thinning damage-factor** computation and provides the per-asset rate-prediction model for both sulfidation (with and without H2) and NAC.
- [[api-510]] — *Pressure Vessel Inspection Code.* In-service inspection consumer for vessel circuits subject to sulfidation + NAC; CML placement on hot-circuit pressure vessels (vacuum-tower, atmospheric-tower) follows the high-velocity-zone bias described above.
- [[api-570]] — *Piping Inspection Code.* In-service inspection consumer for hot-piping circuits subject to sulfidation + NAC; CML density on transfer lines, side draws, and slurry circuits is the principal piping-integrity surface for these two mechanisms.
- [[api-std-579]] — *Fitness-for-Service.* FFS consumer; Part 4 (general thinning) and Part 5 (local thinning) govern the assessment when measured wall loss exceeds the code-minimum thickness T_min for an asset subject to sulfidation, NAC, or both.
- **NACE Publication 34103** — *Refinery Crude Unit Practical Damage Mechanisms.* Companion field guide to API RP 571 with crude-unit-specific NAC + sulfidation case material; future first-class standards page candidate (promotion when the AMPP/NACE source slice lands in the catalog).

## Related concepts

- [damage-mechanism-screening](./damage-mechanism-screening.md) —
  upstream concept; screens which mechanisms are credible for a given
  hot-circuit asset, with sulfidation and NAC as primary entries on the
  crude-unit / FCC / hydroprocessing screening lists.
- [corrosion-rate-measurement](./corrosion-rate-measurement.md) — paired
  metric; both mechanisms produce wall-loss that is tracked via
  UT-thickness CML programmes, with mass-loss coupons used in lab
  qualification of candidate alloys against representative crude slates.
- [risk-based-inspection](./risk-based-inspection.md) — POF input; the
  modified-Couper–Gorman thinning damage factor in
  [api-rp-581](../standards/api-rp-581.md) Part II is one of the primary
  POF terms for hot-circuit refining assets, and the NAC alloy-adequacy
  assessment is a principal RBI re-evaluation trigger when the feedstock
  TAN distribution shifts.
- [fitness-for-service](./fitness-for-service.md) — downstream consumer;
  [api-std-579](../standards/api-std-579.md) Part 4 / Part 5 thinning
  assessment governs the run/repair/replace decision when sulfidation +
  NAC wall loss has consumed the corrosion allowance.
- [erosion-and-fac](./erosion-and-fac.md) — high-velocity wall-thinning
  sibling; FAC and NAC both intensify with velocity and can co-locate
  on the same elbows, complicating diagnostic separation.
- [htha-nelson-curves](./htha-nelson-curves.md) — co-resident
  high-temperature damage mechanism on the hydroprocessing complex; the
  alloy-ladder for sulfidation + NAC must also satisfy the Nelson-curve
  envelope where pH2 is non-trivial.
- [creep-and-stress-rupture](./creep-and-stress-rupture.md) —
  high-temperature time-dependent damage class; creep, sulfidation, and
  NAC all become active above ~370 degC and must be screened jointly on
  vacuum-unit and FCC main-fractionator components.

## Source materials

- [og-standards-api](../sources/og-standards-api.md) — parent source page for the API RP 571 / RP 581 / 510 / 570 / 579 references underpinning the mechanism description, rate-correlation lineage, alloy-ladder framework, and inspection-programme structure above.

## Notes

- This is a concept page, not a standards page. No clause text, McConomy / Couper–Gorman / modified-Couper–Gorman curve coordinates, alloy-specific rate-band tables, NAC-inhibitor formulation guidance, or RP 581 thinning damage-factor coefficients are reproduced here. For normative use, cite the publisher edition of [[api-rp-571]] / [[api-rp-581]] directly.
- The TAN thresholds and velocity-bin alloy-ladder above reflect typical refining experience and are illustrative, not normative. Asset-specific alloy selection must consider the operator's feedstock slate, blending strategy, hot-circuit velocity profile, simultaneous sulfidation overlay, prior-incident history, and any active inhibitor-injection programme.
- The boundary between the H2-free McConomy regime and the H2/H2S modified-Couper–Gorman regime is the key screening question for hydroprocessing-unit hot-circuit metallurgy. A unit that operates close to the H2-partial-pressure boundary may shift between regimes with feedstock changes; the screening is regime-dependent, not a single-correlation calculation.
