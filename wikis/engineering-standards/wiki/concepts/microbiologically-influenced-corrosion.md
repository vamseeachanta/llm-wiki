---
title: "Microbiologically Influenced Corrosion (MIC)"
slug: microbiologically-influenced-corrosion
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
tags:
  - mic
  - microbial-corrosion
  - srb
  - iob
  - biofilm
  - oilfield
  - hydrocarbon-storage
sources:
  - standards/api-rp-571.md
  - standards/ampp-sp0775.md
---

# Microbiologically Influenced Corrosion (MIC)

> Concept anchor for the bioactivity-driven corrosion family flagged in [api-rp-571](../standards/api-rp-571.md) §4 (loss-of-thickness mechanisms) and monitored under [ampp-sp0775](../standards/ampp-sp0775.md) coupon practice. Bidirectional with [damage-mechanism-screening](damage-mechanism-screening.md) (credible-mechanism shortlist input), [corrosion-rate-measurement](corrosion-rate-measurement.md) (rate-versus-localised-attack interpretation), and [pitting-and-crevice-corrosion](pitting-and-crevice-corrosion.md) (morphology distinction).

## What is MIC?

**Microbiologically Influenced Corrosion (MIC)** is corrosion **driven or accelerated** by the metabolic activity of microorganisms — bacteria, archaea, and fungi — operating at the metal–fluid interface, typically beneath an established biofilm. MIC is not a unique electrochemical mechanism in its own right; rather, microbial metabolism modifies the local environment (oxygen activity, pH, sulfide and organic-acid concentration, deposit chemistry) such that an otherwise-tolerable abiotic condition becomes aggressive enough to drive measurable metal loss.

MIC is distinguished from purely abiotic corrosion by a recurring set of signatures:

- **Localisation** — attack is concentrated at discrete sites under the biofilm rather than distributed over the wetted surface; macroscopically the damage looks like pitting or under-deposit corrosion.
- **Biofilm presence** — a viable extracellular-polymeric-substance (EPS) layer covers the attack site and harbours the responsible microbial community.
- **Sulfide-rich corrosion-product layer** — for sulfate-reducing-bacteria-driven MIC the deposit is iron sulfide (mackinawite, pyrrhotite, pyrite) in characteristic black-to-grey friable layers.
- **Characteristic morphology** — hemispherical pits, often with internal tunnelling or "cup-and-cone" sub-pit structure, distinct from the conical or undercut profile typical of chloride pitting on CRAs.
- **Detection sensitivity to biocide treatment** — corrosion rate or pit-growth rate responds to biocide injection in a way that purely abiotic mechanisms do not, making biocide bleed-down a diagnostic as well as a mitigation step.

## Microbial communities

MIC is driven by several metabolically distinct microbial groups; the relevant community for any given asset depends on oxygen availability, fluid chemistry, temperature, and the presence of fermentable organics.

| Group | Mechanism | Typical service |
|-------|-----------|-----------------|
| SRB (Sulfate-Reducing Bacteria) | Sulfate → sulfide; iron-sulfide deposit; cathodic-depolarisation hypothesis | Oxygen-deprived sour service, dead legs, downhole |
| IOB (Iron-Oxidizing Bacteria) | Fe²⁺ → Fe³⁺; tubercle / iron-oxide deposit creating differential aeration cell | Aerated waters, splash zones, fire-water systems |
| APB (Acid-Producing Bacteria) | Organic-acid metabolism; local pH depression | Cooling water, dead legs, fuel storage |
| Methanogens | CO₂ → CH₄; couple electron uptake from steel | Sour gas, anaerobic deep water, oilfield brines |
| Sulfur-Oxidizing Bacteria | H₂S → S° / H₂SO₄; sulfuric-acid generation | Oil-water interfaces, sewer crowns, biotrickling filters |

Real-world MIC settings host **community consortia**, not single populations — SRB and APB co-occur in many oilfield dead legs, and IOB tubercles routinely shelter SRB in their oxygen-depleted core. Diagnostic and mitigation programmes therefore target the consortium, not a single named species.

## Where MIC occurs

MIC reliably appears in services that combine water, low or intermittent flow, and a nutrient source (sulfate, organics, or atmospheric oxygen):

- **Atmospheric storage tanks** — water-bottom corrosion at the floor plate, governed by [api-653](../standards/api-653.md) §6 in-service inspection and bottom-plate magnetic-flux-leakage (MFL) screening.
- **Produced-water injection systems** — re-injected water carries indigenous SRB/APB communities; injection-well tubulars and water-handling piping are recurrent MIC sites.
- **Fire-water and utility-water systems** — stagnant or intermittent service, often in low-alloy carbon steel, with no continuous chemical treatment.
- **Dead legs** — branch lines, instrument tappings, vent and drain stubs, and pump-spare suction headers where flow is absent or intermittent and fluid chemistry diverges from the bulk.
- **Top-of-line condensation (TLC)** — wet-gas piping with stratified flow develops thin condensate films at the 12-o'clock position that host MIC consortia.
- **BOP rams and well-control equipment** — intermittent-service hydraulic chambers and ram cavities with brackish or seawater hydraulic fluid.
- **Idle pipelines and laid-up vessels** — extended shut-in periods without inhibitor turnover or biocide bleed-down let MIC consortia establish under residual water and sludge.

## Detection

MIC detection is multi-modal because no single technique simultaneously confirms biofilm presence, identifies the responsible community, and quantifies metal-loss damage:

- **ATP bioluminescence** — total-microbial-load screening; rapid (minutes) but does not distinguish community composition.
- **qPCR DNA quantification** — oilfield-specific kit panels (often called *molecular microbial monitoring*, MMM) targeting SRB, APB, IOB, and methanogen marker genes; quantitative and species-resolved.
- **MMM probes / online bioactivity sensors** — continuous monitoring of bioactivity at fixed points in a system.
- **Sessile-versus-planktonic sampling distinction** — planktonic (bulk-fluid) microbial counts can be orders of magnitude lower than sessile (biofilm-associated) counts; a defensible MIC programme samples both.
- **FeS deposit characterisation** — XRD and SEM-EDS confirm iron-sulfide phases (mackinawite, pyrrhotite, pyrite) at suspect attack sites, supporting an SRB attribution.
- **Hemispherical-pit morphology** — visual / replica / borescope evidence of cup-and-cone or tunnelled hemispherical pitting under an EPS-bearing deposit, distinct from chloride-driven CRA pitting (see [pitting-and-crevice-corrosion](pitting-and-crevice-corrosion.md)).

A defensible MIC attribution combines a positive community-detection result (qPCR or sessile culture) with a metal-loss observation (UT, MFL, or coupon mass-loss) at the same location.

## Mitigation hierarchy

MIC mitigation follows a tiered hierarchy, applied in combination rather than singly:

- **Design** — eliminate dead legs, slope drainable lines, avoid horizontal runs that pool water, specify bottom-drain fittings on storage tanks, minimise gasket-face crevices.
- **Water-chemistry control** — oxygen scavenger addition, pH control, salinity / ionic-strength management, removal of fermentable organics where economically tractable.
- **Pigging schedules** — regular mechanical cleaning of pipelines to disrupt biofilm and remove sludge that shelters anaerobic consortia.
- **Biocide rotation** — alternation between mechanism-distinct biocides (commonly THPS, glutaraldehyde, and quaternary-ammonium chemistries) to suppress development of biocide-tolerant communities; treatment frequency and dose are tuned against bioactivity-monitoring trends.
- **Cathodic protection** — effective on soil-side and immersed surfaces; CP-on potentials drive the structure into the immune region and collapse the corrosion rate, including the MIC contribution.
- **Coatings and linings** — barrier protection on tank floors, internal pipe linings, and FBE-coated buried piping reduces the wetted surface available for biofilm establishment.
- **MIC-resistant materials** — CRA upgrade (e.g., 22Cr / 25Cr duplex, 6Mo super-austenitic) where the economic case supports the metallurgy lift; note that MIC has been observed on stainless steels under heavy biofilm despite their nominal CPT, so material selection is a partial — not a complete — mitigation.

## Inspection and monitoring

In-service MIC monitoring layers three evidence streams at known MIC-risk Condition Monitoring Locations (CMLs):

- **Coupons per [ampp-sp0775](../standards/ampp-sp0775.md)** — *Preparation, Installation, Analysis, and Interpretation of Corrosion Coupons in Oilfield Operations.* Coupon mass-loss and pit-depth are the field calibration ground truth and drive the *short-term* corrosion-rate input that pairs with UT-survey LTCR per [corrosion-rate-measurement](corrosion-rate-measurement.md).
- **Biocide-bleed monitoring** — residual biocide concentration trending against bioactivity (ATP / qPCR) confirms the treatment programme is reaching the susceptible CMLs.
- **qPCR community profiling** — periodic sessile-and-planktonic sampling at MIC-risk CMLs (dead legs, water-bottoms, low-flow branches) to detect community shifts that precede measurable metal loss.

The monitoring loop closes through [damage-mechanism-screening](damage-mechanism-screening.md): a positive qPCR or coupon excursion re-classifies the CML's MIC credibility from *possible* to *probable* or *definite*, which propagates back into the asset's RBI POF score and its inspection-interval setting.

## Standards

Bidirectional cross-references — each standards page below should cross-link back to this concept page once the convention propagates.

- [api-rp-571](../standards/api-rp-571.md) — *Damage Mechanisms Affecting Fixed Equipment in the Refining Industry.* MIC is catalogued in §4 as a loss-of-thickness mechanism; the trigger criteria (water + low-flow + sulfate or organic-acid source) are the screening reference for MIC credibility.
- [api-510](../standards/api-510.md) — *Pressure Vessel Inspection Code.* In-service inspection consumer; vessels with stagnant water-bottoms or low-flow internals carry MIC-driven CML programmes.
- [api-570](../standards/api-570.md) — *Piping Inspection Code.* In-service inspection consumer; piping-circuit screening flags dead legs, drains, and intermittent-service stubs as MIC-credible CMLs.
- [api-653](../standards/api-653.md) — *Atmospheric Storage Tank Inspection Code.* In-service inspection consumer; §6 internal inspection drives the bottom-MFL + coupon programme that detects soil-side and water-bottom MIC on tank floors.
- [api-rp-574](../standards/api-rp-574.md) — *Inspection Practices for Piping System Components.* CML-practice reference for piping; identifies dead-leg geometries and the UT-thickness conventions that capture MIC under-deposit attack.
- [ampp-sp0775](../standards/ampp-sp0775.md) — *Preparation, Installation, Analysis, and Interpretation of Corrosion Coupons in Oilfield Operations.* Coupon-station practice underpinning MIC-prone-service monitoring; pairs with biocide-bleed and qPCR streams in the integrated monitoring programme.
- **NACE TM-0212** — *Detection, Testing, and Evaluation of Microbiologically Influenced Corrosion on Internal Surfaces of Pipelines.* Microbial surveillance and sampling-practice reference; future first-class standards page candidate.
- **NACE TM-0194** — *Field Monitoring of Bacterial Growth in Oil and Gas Systems.* Sibling field-monitoring practice; future first-class standards page candidate.

## Related concepts

- [damage-mechanism-screening](damage-mechanism-screening.md) — upstream credible-mechanism gate; MIC enters the per-asset shortlist when service conditions match the §4 trigger criteria (water + low-flow + nutrient source).
- [corrosion-rate-measurement](corrosion-rate-measurement.md) — paired metric; MIC is "highly variable; often manifests as locally accelerated pitting under biofilm rather than as a uniform rate" (cross-ref: rate table in that page), which means a single rate-of-loss number under-represents the MIC threat.
- [pitting-and-crevice-corrosion](pitting-and-crevice-corrosion.md) — morphology overlap; MIC pits superficially resemble chloride pitting on stainless and carbon steel but carry a biofilm signature, an iron-sulfide deposit (for SRB-driven cases), and a hemispherical-with-tunnelling sub-pit structure that distinguishes them on cross-section.

## Source materials

- [og-standards-api](../sources/og-standards-api.md) — parent source page for the [api-rp-571](../standards/api-rp-571.md) / [api-510](../standards/api-510.md) / [api-570](../standards/api-570.md) / [api-rp-574](../standards/api-rp-574.md) / [api-653](../standards/api-653.md) catalogue references underpinning the screening, inspection, and CML-practice framework above.

## Notes

- This is a concept page, not a standards page. No clause text, biocide-dose ladders, qPCR threshold values, or community-attribution criteria are reproduced here. For normative use, cite the publisher edition of API RP 571, AMPP SP0775, NACE TM-0212, or NACE TM-0194 directly.
- The community-and-mechanism table is a navigation aid; real MIC settings host consortia, and a defensible attribution requires both community-detection evidence and a co-located metal-loss observation.
- MIC mitigation is multi-barrier by design — single-mode treatment (e.g., biocide-only without dead-leg elimination) routinely fails as the surviving community adapts and re-establishes under deposits the chemistry cannot reach.
