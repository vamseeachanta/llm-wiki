---
title: "Corrosion Management"
tags: [corrosion, co2-corrosion, h2s-corrosion, mic, oxygen-ingress, inhibition, de-waard-milliams, norsok-m-506, production-engineering, prose-only]
sources:
  - iso-21457
  - nace-sp0106
added: 2026-05-16
last_updated: 2026-05-16
---

# Corrosion Management

## Scope

Corrosion management is the operating-time discipline that keeps internal corrosion of producing-well tubulars and the associated production-system piping within tolerance across the producing life of the well. It sits inside the [Well Integrity During Production](well-integrity-during-production.md) operating-time scope and is the dominant integrity-management threat in most production service environments.

The discipline organises around four operating-time corrosion mechanisms (CO2 / H2S / microbiologically-influenced / oxygen-ingress) and the inhibition / mitigation strategy hierarchy that operators deploy against them. Modelling frameworks for corrosion-rate prediction are described qualitatively at the framework level. Specific inhibitor chemistries are described by chemistry class only, with no commercial product designations, no dosage-rate citations with engineering units, and no performance-curve transcriptions, per the production-engineering vendor-discipline rule.

This page is the **operating-time corrosion-mechanism reference** for the production-engineering wiki. It anchors to [ISO 21457](../standards/iso-21457.md) at the design-time system-level philosophy and to [NACE SP0106](../standards/nace-sp0106.md) at the operating-time line-item management methodology.

## Four operating-time corrosion mechanisms

### 1. CO2 corrosion (sweet corrosion)

CO2 dissolved in produced water forms carbonic acid, which lowers the pH of the water phase and drives accelerated corrosion of carbon and low-alloy steels. The mechanism is the dominant operating-time corrosion threat in most CO2-bearing production environments. Three regional forms are typically distinguished in practitioner literature:

- **Uniform-attack wall thinning** — the baseline mode in clean-flow service where the water phase contacts the metal surface continuously; rates vary widely with CO2 partial pressure, temperature, flow regime, water chemistry, and the presence (or absence) of protective iron-carbonate scale.
- **Mesa attack** — a localised mode where protective scale forms unevenly, exposing patches of the underlying steel to acidic water while adjacent scaled regions are protected; the rate at the unscaled patches is far higher than the average uniform rate and the failure mode is rapid localised wall loss rather than uniform thinning.
- **Top-of-line corrosion (TLC)** — a specific failure mode in stratified-flow gas-condensate lines where condensed water containing dissolved CO2 forms at the top of the line and drips back, attacking the line crown; this mode is well-documented in long subsea tiebacks and onshore gas-gathering systems.

CO2-corrosion-rate prediction is anchored historically by the **de Waard-Milliams framework**, developed and refined across multiple papers from the 1970s into the early 1990s. The framework expresses corrosion rate as a function of CO2 partial pressure, temperature, and pH, with subsequent modifications addressing the effect of scale formation, fluid velocity, oil-wetting versus water-wetting flow conditions, and other operating variables. The framework is qualitative-mechanistic in this wiki: operators consulting the framework for engineering calculations should refer to the original papers and to the **Norsok M-506** Norwegian sector standard, which provides one of the most widely-adopted operator-facing implementations of CO2-corrosion-rate prediction methodology and which references the de Waard-Milliams lineage explicitly. Both the de Waard-Milliams framework and Norsok M-506 are paywalled or restricted-access references; this wiki paraphrases their framework-level structure only and does not transcribe their numerical relationships.

### 2. H2S corrosion (sour corrosion)

H2S dissolved in produced water drives a distinct family of corrosion mechanisms on carbon and low-alloy steels:

- **Sulfide stress cracking (SSC)** — a hydrogen-embrittlement-driven cracking mechanism in which atomic hydrogen produced at the metal surface by H2S-water chemistry enters the steel and embrittles it, producing brittle cracks under tensile stress. The mechanism is severely service-limiting for high-strength steels; NACE MR0175 / ISO 15156 (see engineering-standards [ISO 15156](../../../engineering-standards/wiki/standards/iso-15156.md)) is the canonical material-qualification standard for sour-service steel selection that addresses SSC.
- **Hydrogen-induced cracking (HIC)** — a hydrogen-accumulation mechanism at internal microstructural discontinuities (manganese-sulfide inclusions, hard segregated bands) that produces blistering and stepwise cracking in the parent metal. The mechanism is more service-limiting for plate steel (line pipe, vessel walls) than for tubular steel; AMPP / NACE TM0284 (see engineering-standards [AMPP TM0284](../../../engineering-standards/wiki/standards/ampp-tm-0284.md)) is the canonical laboratory-test methodology.
- **General sour corrosion** — accelerated uniform-attack and pitting in H2S-bearing service, often in combination with CO2 corrosion mechanisms in mixed-gas environments. The protective scale chemistry shifts from iron carbonate (sweet-dominant) to iron sulfide (sour-dominant), with different stability and protective behaviour.

H2S corrosion-rate prediction is less mature than CO2-rate prediction in publicly-available methodology; operators typically combine NACE MR0175 / ISO 15156 material-qualification logic with operating-time monitoring (coupon analysis, UT surveying) and conservative material-selection at design time per [ISO 21457](../standards/iso-21457.md) methodology. The mechanism-level reference for sour-service degradation is API RP 571 (see engineering-standards [API RP 571](../../../engineering-standards/wiki/standards/api-rp-571.md)).

### 3. Microbiologically-influenced corrosion (MIC)

MIC is the family of corrosion mechanisms driven by microbial activity (sulfate-reducing bacteria, acid-producing bacteria, iron-oxidising bacteria, methanogens, and others) in the production system. The mechanism is typically localised, often manifesting as deep pitting under sessile biofilm colonies that establish on metal surfaces in water-bearing service. MIC is most common in:

- **Water-injection lines feeding back to producing zones** — biofilm establishes in the injection line and the bacteria are carried through the injection-and-production cycle into the producing well
- **Stagnant or low-flow regions** of the production system where biofilm has the opportunity to establish without being scoured by flow
- **Under-deposit regions** where solids accumulation creates anaerobic conditions favourable to sulfate-reducing bacteria

Operating-time management combines microbiological monitoring (sessile-vs-planktonic biofilm characterisation, microbial-count trending), biocide treatment (chemistry-class selection from oxidising biocides, non-oxidising biocides, and quaternary-ammonium families at concept level), pigging programs to remove deposits and disrupt biofilm, and water-treatment-program management. The [Integrity Monitoring](integrity-monitoring.md) page covers the monitoring discipline; the [NACE SP0106](../standards/nace-sp0106.md) framework provides the operating-time methodology that integrates MIC management with the other corrosion-threat management.

### 4. Oxygen-ingress corrosion

Production systems are typically designed as closed-loop oxygen-free systems; oxygen ingress through tankage venting, leaking pump seals, gas-lift gas with inadequate oxygen removal, or other infiltration paths produces accelerated corrosion that is often disproportionate to the relatively small oxygen mass loading. Oxygen acts as a strong cathodic depolariser, accelerating corrosion-cell kinetics that would otherwise be limited by oxygen availability. Oxygen-ingress diagnosis is performed by oxygen-content monitoring of representative production-system points, with mitigation by closing off ingress paths and by chemical oxygen scavenging where ingress cannot be eliminated by design.

## Predictive-modelling framework landscape

CO2-corrosion-rate prediction has the most mature publicly-available modelling landscape; H2S-corrosion-rate prediction and MIC-rate prediction are less mature in publicly-available methodology and operators typically combine modelling with heavier operating-time monitoring:

- **de Waard-Milliams framework family** — the historical anchor for CO2-corrosion-rate prediction, with successive refinements addressing scale-protection effects, fluid-velocity effects, oil-wetting effects, and pH chemistry. The framework is qualitative-mechanistic in this wiki; engineering-unit relationships are in the source papers and in the standards that operationalise them.
- **Norsok M-506** — Norwegian sector standard providing an operator-facing implementation of CO2-corrosion-rate prediction. The standard provides a calculation framework structured for engineering use in design and operating-time review; its outputs are typically used as one input among several (alongside operating-time monitoring data, water-chemistry data, and engineering judgement) rather than as a sole prediction basis. Like the underlying de Waard-Milliams framework, Norsok M-506 is paywalled and this wiki describes its framework intent only without transcribing its numerical relationships.
- **Vendor-developed proprietary models** — several integrated-corrosion-services vendors maintain proprietary CO2-corrosion-rate models. These are not described in this wiki per the production-engineering vendor-discipline rule; the operator-facing reference is the public-literature framework (de Waard-Milliams, Norsok M-506) plus operator-internal calibration against operating-time monitoring data.
- **Mechanistic models from academic and consortium research** — research-grade CO2-corrosion models (the OLI mechanistic-modelling framework family, electrochemical-mechanism-based research codes) provide more detailed mechanistic representation but require correspondingly more input data and engineering expertise to operate. Operators typically deploy these for specific high-value problems rather than as routine design-screening tools.

The discipline-wide practice is to **treat predictive modelling as one input among several** to the operating-time corrosion-management decision rather than as the primary basis. Operating-time monitoring (coupons, ER probes, UT surveys, inhibitor-residual analysis) provides the ground-truth corrosion-rate distribution; predictive modelling provides the framework for anticipating corrosion-rate response to operating-condition changes (water-cut increase, temperature shift, pressure depletion, inhibitor-program adjustment).

## Mitigation-strategy hierarchy

The mitigation-strategy hierarchy that operators deploy against the four corrosion mechanisms follows [ISO 21457](../standards/iso-21457.md) framework:

### Chemical inhibition

The dominant operating-time mitigation strategy for carbon-steel production systems. Corrosion inhibitors are surface-active chemistries that form protective films on the metal surface, reducing corrosion-cell kinetics. The major chemistry classes used in oil-and-gas service:

- **Imidazoline-class inhibitors** — nitrogen-containing surface-active compounds widely used in sweet and mildly-sour service; effective as continuous or batch treatment
- **Quaternary-ammonium-class inhibitors** — cationic surface-active compounds often used in combination with imidazolines or as standalone treatment in specific service environments
- **Amide-class and amine-class inhibitors** — additional surface-active families used in various service environments and chemistry blends
- **Phosphate-ester-class inhibitors** — used in specific service environments, particularly where water-phase chemistry favours phosphate-film formation
- **Inhibitor blends** — most operating-time inhibitor programs deploy proprietary blends rather than single-chemistry products; the chemistry-class designation here is the public framework, the specific blend formulations are vendor-proprietary and are not transcribed in this wiki

Inhibitor application logic is **continuous injection** (for high-severity continuous-flow service), **batch treatment** (for moderate-severity service or for tubular regions not reachable by continuous injection), **squeeze treatment** (for downhole tubular regions where continuous injection is impractical), and **gas-phase inhibitor injection** for top-of-line corrosion in stratified-flow gas lines. Application-rate decisioning is operator-program-specific and is calibrated against monitoring response per [NACE SP0106](../standards/nace-sp0106.md) operating-time methodology; specific application-rate values are not transcribed here.

### Biocide treatment for MIC

MIC mitigation deploys biocide treatments from the chemistry-class families noted above; application logic includes continuous low-level dosing, batch high-concentration treatments to break established biofilm, and pigging-coordinated treatments that combine deposit removal with biocide application.

### Oxygen scavenging

Where oxygen ingress cannot be eliminated by design, chemical oxygen scavengers consume the oxygen before it can drive corrosion. The most common chemistry classes are bisulfite-based and hydrazine-based oxygen scavengers, with class selection driven by service-temperature, application-rate, and downstream-compatibility considerations.

### Material upgrades

Where chemical inhibition is insufficient or impractical, material upgrades from carbon steel to corrosion-resistant alloys (chrome-content low-alloy steels, 13Cr stainless, duplex stainless, super-duplex stainless, nickel-based alloys) shift the operating-time integrity from inhibition-dependent to inherently-resistant. Selection of upgraded materials is governed by [ISO 21457](../standards/iso-21457.md) at the system level and by NACE MR0175 / ISO 15156 at the component-qualification level (see engineering-standards [ISO 15156](../../../engineering-standards/wiki/standards/iso-15156.md), [AMPP MR0175 Part 3](../../../engineering-standards/wiki/standards/ampp-mr-0175-pt3.md)).

### Internal coatings and linings

Internal coatings and linings provide barrier-protection for specific service environments. The discipline is well-developed for tankage and large-diameter piping; for production tubing and small-diameter piping the application is more constrained by deployment logistics and by coating-condition monitoring difficulty.

### Cathodic protection of internal surfaces

Internal cathodic protection is used in specific tankage and water-injection service. For production-tubing and pipeline internal surfaces, the technique is not generally applicable because of the absence of a continuous electrolyte path; the corrosion-control strategy relies on inhibition, material selection, and coatings rather than on internal cathodic protection.

## Coupling with adjacent operating-time disciplines

- **Flow-assurance scale-deposition coupling** — iron-carbonate scale (sweet service) and iron-sulfide scale (sour service) are corrosion reaction products; their deposition is both a [Mineral Scale](mineral-scale.md) management problem and a corrosion-rate diagnostic (deposition rate is one indicator of corrosion-rate trending). Chemical-inhibitor program design must account for scale-inhibitor co-management.
- **Erosion-corrosion coupling** — accelerated corrosion in regions of high fluid velocity or sand-laden flow can produce damage rates that exceed the linear superposition of pure-erosion and pure-corrosion contributions; the combined mode is addressed by combination of [Erosional Velocity](erosional-velocity.md) screening for rate ceilings and material selection per [ISO 21457](../standards/iso-21457.md) framework.
- **Sour-service material-qualification coupling** — NACE MR0175 / ISO 15156 component-qualification logic determines whether candidate materials are usable at all in the H2S partial-pressure and temperature envelope of the service; this is a hard constraint above and beyond corrosion-rate prediction.

## Standards anchors

- [ISO 21457](../standards/iso-21457.md) — system-level material-selection and corrosion-control philosophy; design-time anchor
- [NACE SP0106](../standards/nace-sp0106.md) — operating-time internal-corrosion management methodology
- AMPP / NACE MR0175 / ISO 15156 — sour-service material qualification (see engineering-standards [ISO 15156](../../../engineering-standards/wiki/standards/iso-15156.md), [AMPP MR0175 Part 1](../../../engineering-standards/wiki/standards/ampp-mr-0175-pt1.md), [AMPP MR0175 Part 2](../../../engineering-standards/wiki/standards/ampp-mr-0175-pt2.md), [AMPP MR0175 Part 3](../../../engineering-standards/wiki/standards/ampp-mr-0175-pt3.md))
- AMPP TM0177 / TM0284 — laboratory test methodology for SSC / HIC (see engineering-standards [AMPP TM0177](../../../engineering-standards/wiki/standards/ampp-tm-0177.md), [AMPP TM0284](../../../engineering-standards/wiki/standards/ampp-tm-0284.md))
- API RP 571 — damage mechanisms in fixed equipment (engineering-standards cross-link) [API RP 571](../../../engineering-standards/wiki/standards/api-rp-571.md)
- Norsok M-506 — Norwegian sector standard for CO2-corrosion-rate calculation (paywalled; described qualitatively above)

## Cross-references

- [Well Integrity During Production](well-integrity-during-production.md) — operating-time well-integrity router
- [Integrity Monitoring](integrity-monitoring.md) — monitoring discipline that provides operating-time corrosion-rate ground truth
- [Intervention Triggers](intervention-triggers.md) — workover decisioning based on accumulated corrosion-driven integrity degradation
- [Mineral Scale](mineral-scale.md) — iron-carbonate / iron-sulfide scale coupling
- [Erosional Velocity](erosional-velocity.md) — erosion-corrosion combined-mode coupling
- [Flow Assurance](flow-assurance.md) — broader chemical-management programmatic context
- Marine-engineering: [Corrosion Control](../../../marine-engineering/wiki/concepts/corrosion-control.md) — external structural corrosion (complementary scope)

## Public references

- **de Waard, C. & Milliams, D. E.** — "Carbonic Acid Corrosion of Steel," *Corrosion* 31(5), 1975. The foundational CO2-corrosion-rate framework paper.
- **de Waard, C., Lotz, U. & Milliams, D. E.** — "Predictive Model for CO2 Corrosion Engineering in Wet Natural Gas Pipelines," *Corrosion* 47(12), 1991. Refined framework addressing scale-protection effects.
- **de Waard, C., Lotz, U. & Dugstad, A.** — "Influence of Liquid Flow Velocity on CO2 Corrosion: A Semi-Empirical Model," NACE CORROSION/95 paper 128, 1995. Velocity-effect extension to the framework family.
- **Nesic, S.** — "Key issues related to modelling of internal corrosion of oil and gas pipelines — A review," *Corrosion Science* 49(12), 2007. Practitioner-and-academic review of CO2 and CO2/H2S corrosion-rate modelling state of the art; useful complement to the de Waard-Milliams lineage and to the Norsok M-506 framework.
- **Heidersbach, R.** — *Metallurgy and Corrosion Control in Oil and Gas Production*, 2nd ed., Wiley 2018 (ISBN 978-1-119-25925-6). Practitioner-oriented textbook covering CO2 / H2S / MIC / oxygen-ingress mechanisms and the inhibition / mitigation framework at engineering-implementation level.
- **Papavinasam, S.** — *Corrosion Control in the Oil and Gas Industry*, Elsevier 2014 (ISBN 978-0-12-397022-0). Comprehensive industry-practitioner reference; covers operating-time inhibitor-program management, MIC management, and integrity-monitoring integration with corrosion-rate prediction.
- **Schweitzer, P. A.** — *Corrosion of Linings and Coatings: Cathodic and Inhibitor Protection and Corrosion Monitoring*, CRC Press 2007 (ISBN 978-0-8493-8246-8). Adjacent coverage of inhibition, coatings, and corrosion-monitoring techniques.
- **ASM International** — *ASM Handbook Volume 13C: Corrosion: Environments and Industries*, 2006 (ISBN 978-0-87170-709-3). Industry-by-industry corrosion characterisation; the oil-and-gas chapters cover the operating-time discipline at handbook-level depth.
- **API RP 571** — *Damage Mechanisms Affecting Fixed Equipment in the Refining Industry*, 3rd ed., 2020. Mechanism-level catalogue widely applied to upstream production systems by analogy.
- **NACE / AMPP CORROSION conference corpus** — extensive practitioner literature on CO2 / H2S / MIC corrosion-management methodology, inhibitor-program design, and field-case operating-time experience. Accessible through ampp.org and through OnePetro.

## Notes

- Per the production-engineering wiki's vendor-discipline rule, no commercial corrosion-inhibitor product designations, no specific dosage-rate values with engineering units, and no vendor-specific performance curves are reproduced in this page. Operators reviewing inhibitor selection should consult vendor data sheets directly and validate against operating-time monitoring data per the [NACE SP0106](../standards/nace-sp0106.md) framework.
- The de Waard-Milliams CO2-corrosion-rate framework and the Norsok M-506 standard are described qualitatively at framework level only; specific numerical relationships are in the source papers (de Waard-Milliams lineage) and in the paywalled Norsok M-506 standard. Operators performing engineering-unit corrosion-rate calculations should consult those sources directly.
- The MIC literature includes microbiology-side terminology (sessile vs planktonic biofilm, sulfate-reducing-bacteria genera, biofilm-extracellular-polymeric-substance chemistry) that this concept-page summarises at framework level only; operators developing MIC-management programs should engage microbiology-specialist services and consult the dedicated MIC-management literature for diagnostic and treatment methodology depth beyond this overview.
