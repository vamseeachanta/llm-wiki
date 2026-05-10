---
title: "Damage-Mechanism Screening"
slug: damage-mechanism-screening
tags:
  - damage-mechanisms
  - rbi
  - ffs
  - integrity-management
  - htha
  - sulfidation
  - scc
  - refinery-corrosion
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
sources:
  - standards/api-rp-571.md
---

# Damage-Mechanism Screening

> Concept anchor for the analytical step that identifies which damage mechanisms credibly apply to a piece of equipment. Sits upstream of [risk-based-inspection](risk-based-inspection.md) (POF input), [fitness-for-service](fitness-for-service.md) (which Part / Annex governs the assessment), and [corrosion-rate-measurement](corrosion-rate-measurement.md) (which rate model interprets a measured number). Routes into the API RP 571 catalogue page (forthcoming, iter-18 primary).

## What is damage-mechanism screening?

**Damage-mechanism screening** is the systematic identification of which damage mechanisms apply to a piece of equipment given its **process service** (fluid composition, temperature, pressure, flow regime, contaminant profile), **construction materials** (base metal grade, weld filler, clad / overlay layers, heat-treatment condition), **fabrication history** (weld procedures, post-weld heat treatment, cold-work, prior-repair record), and **operating envelope** (cycle counts, upset frequency, start-up / shutdown chemistry, idle and steam-out exposure). Screening is the first analytical step in any RBI or FFS workflow because POF construction, remaining-life calculation, inspection-technique selection, and CML placement all depend on which mechanisms are actually credible for the asset in question. A complete corrosion-rate number means little until the engineer knows which mechanism produced it; a quantitative POF score is undefined until the candidate-mechanism set is closed.

The output of screening is a **per-asset shortlist** of credible mechanisms, each tagged with an indicative rate or progression model, an inspection-effectiveness recommendation, and a damage-factor family for the downstream RBI engine.

## The mechanism-class taxonomy

API RP 571 — *Damage Mechanisms Affecting Fixed Equipment in the Refining Industry* — organises the universe of refining-and-petrochem damage mechanisms into five broad classes. The taxonomy below mirrors the RP 571 §3 / §4 / §5 partitioning that is the working reference for nearly every refining-integrity programme.

| Class | Examples | Reference |
|---|---|---|
| Mechanical / metallurgical | Brittle fracture, mechanical fatigue, thermal fatigue, creep, dissimilar-metal-weld (DMW) cracking, temper embrittlement, sigma-phase embrittlement, 885 °F embrittlement, graphitisation, spheroidisation | API RP 571 §3 |
| Loss-of-thickness | General corrosion, localised corrosion, erosion, erosion-corrosion, corrosion under insulation (CUI), microbiologically influenced corrosion (MIC), galvanic corrosion, soil-side corrosion | API RP 571 §4 |
| High-temperature | Sulfidation (Couper–Gorman / McConomy curves), high-temperature hydrogen attack (HTHA, Nelson curves), oxidation, naphthenic-acid corrosion (NAC), decarburisation, carburisation, metal dusting, fuel-ash corrosion | API RP 571 §5 |
| Environmentally-assisted cracking | Chloride-SCC, caustic SCC, amine SCC, polythionic-acid SCC (PASCC), carbonate SCC, ammonia SCC, sulfide-stress cracking (SSC), hydrogen-induced cracking (HIC), stress-oriented hydrogen-induced cracking (SOHIC), liquid-metal embrittlement | API RP 571 §5 |
| Low-temperature aqueous | Sweet (CO2) corrosion, sour (H2S) corrosion, dew-point corrosion, atmospheric corrosion, oxygenated-water corrosion, condensate corrosion | API RP 571 §4 |

The boundaries between classes are not bright lines — sulfidation in the presence of hydrogen ("sulfidation in H2/H2S service") combines the high-temperature and aqueous-cracking branches, and CUI is simultaneously a loss-of-thickness mechanism and an environmentally-driven one. The taxonomy is a navigation aid into the RP 571 catalogue, not a partition of the failure mode space.

## Screening triggers per process unit

Refinery and petrochemical units have characteristic damage-mechanism signatures driven by their fluid chemistry and operating temperature. The table below names the dominant mechanisms an RBI / FFS team should expect to see on a unit-by-unit screening pass; it does not replace asset-specific evaluation.

| Unit | Common mechanisms |
|---|---|
| Crude unit (atmospheric + vacuum) | Naphthenic-acid corrosion (high-TAN crudes), sulfidation on hot circuits, atmospheric corrosion on cold-end equipment, high-T H2 / H2S in stripping sections, dew-point corrosion in overhead condensers, ammonium-chloride and ammonium-bisulfide corrosion at salt-deposition locations |
| Hydroprocessing (HDS, HDT, hydrocracker) | High-temperature hydrogen attack (HTHA) per Nelson curves, polythionic-acid SCC of austenitic stainless during shutdowns and exposure to wet sulfur compounds, sour-service cracking (SSC, HIC, SOHIC), amine SCC, thermal and mechanical fatigue, hydrogen embrittlement |
| Fluid Catalytic Cracking (FCC) | Catalyst-driven erosion in slide valves, cyclones and slurry piping; sulfidation of hot-section internals; polythionic-acid SCC at shutdowns; high-temperature creep and thermal fatigue in regenerator-to-reactor lines; vibration fatigue |
| Catalytic reformer | HTHA in hydrogen-rich circuits, hydrogen damage, creep in furnace tubes, thermal fatigue from cycling, decarburisation, metallurgical degradation of furnace-tube alloys |
| Amine treating (MEA / DEA / MDEA) | Amine SCC of carbon steel non-PWHT'd welds, wet H2S cracking (SSC, HIC, SOHIC), MIC in stagnant draws, CO2 corrosion, erosion-corrosion at high-velocity locations, foaming-driven flow excursions |
| Sulfur recovery (Claus + tail gas) | Sulfidation on hot reaction-furnace circuits, condensate corrosion in cold-end equipment, sulfide cracking in wet streams, ammonium-salt corrosion at shutdown, refractory-deterioration-driven hot-spotting |
| Atmospheric storage tanks | External atmospheric corrosion on shell and roof, MIC on bottom soil-side, soil-side under-deposit corrosion, settlement-driven shell-to-bottom-weld fatigue, internal corrosion in water-bottoms zones, vapour-space corrosion at the wet-dry interface |

## Screening output

A defensible screening pass yields, per asset:

1. **Credible-mechanism shortlist** — each mechanism tagged with a justification (process-condition match against API RP 571 trigger criteria) and a confidence flag (definite / probable / possible / excluded).
2. **Initial rate or progression-model estimates** — corrosion-rate band from API RP 571 + plant-historical data + applicable model (Couper–Gorman, McConomy, de Waard–Milliams, Nelson curve threshold check, etc.). For cracking mechanisms, a susceptibility flag rather than a rate.
3. **Inspection-effectiveness recommendations** — which NDT techniques can detect each credible mechanism at the relevant damage scale (UT thickness for general thinning, AUT or PAUT for localised attack, WFMT or ACFM for surface-breaking SCC, automated UT for HIC/SOHIC, EMAT for CUI, advanced-UT or in-situ replication for HTHA).
4. **POF input** — the mechanism shortlist is mapped to API RP 581 **damage-factor families** (thinning, SCC, HTHA, mechanical fatigue, brittle fracture, external) so the downstream RBI engine can compute a numeric POF.
5. **CML placement guidance** — credible mechanisms drive monitoring-location selection (high-velocity elbows for erosion-corrosion, dead legs for MIC, weld HAZ for SCC, soil-air interface for atmospheric corrosion, vapour-liquid interface for dew-point corrosion).

The deliverable is the **per-asset corrosion-loop diagram** plus the screening write-up; both feed directly into the RBI study and the inspection-plan optimisation.

## Why this concept matters as a concept (not just embedded in API RP 571)

Damage-mechanism screening is the **central organising decision** in a refining-integrity programme. Multiple standards reference it and presuppose it without containing the full procedural definition:

- **API RP 580** §6.2 *Damage Mechanisms and Failure Modes* requires the RBI team to identify credible damage mechanisms as a programme-element step — but routes the catalogue itself out to API RP 571.
- **API RP 581** Part II *Probability of Failure Methodology* organises its damage-factor calculations (thinning, SCC, HTHA, external, brittle fracture, mechanical fatigue) by mechanism family — and presupposes that the screening step has already populated the per-asset mechanism list.
- [api-510](../standards/api-510.md) §6.5.x and [api-570](../standards/api-570.md) §5 require corrosion-loop / circuit definitions that group equipment by common service and metallurgy, which is in practice the screening exercise applied at the loop level.
- [api-std-579](../standards/api-std-579.md) FFS Parts 4 / 5 / 6 / 7 / 9 / 10 each apply to a specific damage-mechanism family, so the FFS practitioner must screen the mechanism before selecting which Part governs the assessment.

Because the screening step lives across the boundary between the catalogue (RP 571), the methodology (RP 580 / 581), the inspection codes (510 / 570 / 653), and the FFS code (579-1), no single standard is its natural home. A concept page is the right surface — it lets each standards page link in to a shared definition rather than duplicating screening guidance per standard.

## Standards

Bidirectional cross-references — each standards page below should cross-link back to this concept page once the convention propagates.

- **API RP 571** — *Damage Mechanisms Affecting Fixed Equipment in the Refining Industry.* Primary mechanism catalogue and trigger-criteria reference. Standards page forthcoming (iter-18 primary).
- [api-rp-580](../standards/api-rp-580.md) — *Risk-Based Inspection.* §6.2 names damage-mechanism identification as a required RBI programme element; this concept page is the qualitative-screening anchor that satisfies the requirement.
- [api-rp-581](../standards/api-rp-581.md) — *Risk-Based Inspection Methodology.* Quantitative consumer; Part II damage-factor families are populated from the screening output.
- [api-510](../standards/api-510.md) — *Pressure Vessel Inspection Code.* In-service inspection consumer; corrosion-loop / vessel-circuit screening drives CML placement and inspection-technique selection.
- [api-570](../standards/api-570.md) — *Piping Inspection Code.* In-service inspection consumer; piping-circuit screening drives CML density and the corrosion-rate-tracking workflow.
- [api-653](../standards/api-653.md) — *Atmospheric Storage Tank Inspection Code.* In-service inspection consumer; tank-specific screening (soil-side MIC, settlement fatigue, atmospheric corrosion, internal water-bottoms corrosion) drives the external / internal / bottom inspection-interval logic.
- [api-std-579](../standards/api-std-579.md) — *Fitness-for-Service.* FFS consumer; the screening output determines which Part / Annex (general thinning Pt 4, local thinning Pt 5, pitting Pt 6, blisters / HIC / SOHIC Pt 7, distortion Pt 8, crack-like Pt 9, creep Pt 10, fire Pt 11, dents Pt 12) governs the assessment of a found flaw.
- **API RP 941** — *Steels for Hydrogen Service at Elevated Temperatures and Pressures in Petroleum Refineries and Petrochemical Plants.* Holds the **Nelson curves** that govern HTHA screening across hydroprocessing and reformer units. Future first-class standards page candidate.

## Related concepts

Wikilinks below point to concept pages that may not yet exist — leave as wikilinks for future creation per the spinout's link-and-fill convention.

- [risk-based-inspection](risk-based-inspection.md) — downstream consumer; screening populates the credible-mechanism shortlist that becomes the RBI study's POF input.
- [fitness-for-service](fitness-for-service.md) — downstream consumer; screening selects which FFS Part / Annex governs the assessment of a found flaw.
- [corrosion-rate-measurement](corrosion-rate-measurement.md) — paired metric; rate inputs are interpreted **per mechanism** (a measured 500 μm/yr means very different things if it is sulfidation, naphthenic-acid corrosion, or MIC).
- [sour-service-materials](sour-service-materials.md) — subset of screening for H2S environments; ISO 15156 / NACE MR0175 material-selection rules apply once SSC / HIC / SOHIC are flagged credible.
- [pitting-and-crevice-corrosion](pitting-and-crevice-corrosion.md) — subset of localised-corrosion screening; depth-driven not rate-driven, with its own CPT / CCT screening framework.

## Source materials

- [og-standards-api](../sources/og-standards-api.md) — parent source page for the API RP 571 / RP 580 / RP 581 / 510 / 570 / 653 / 579 / RP 941 catalog references underpinning the screening framework above.

## Notes

- This is a concept page, not a standards page. No clause text, Nelson-curve coordinates, Couper–Gorman / McConomy / de Waard–Milliams coefficients, or RP 581 damage-factor formulas are reproduced here. For normative use, cite the publisher edition of API RP 571 / RP 580 / RP 581 / RP 941 directly.
- The unit-by-unit mechanism table is illustrative of typical refining experience; actual screening for any specific asset must consider the operator's feedstock slate, metallurgy choices, prior-incident history, and current-cycle operating envelope.
- Damage-mechanism screening is methodology, not a single standard. A standalone screening pass without the API RP 580 governance elements (team competence, documented justification, re-evaluation triggers) is **not** a sanctioned RBI input and will not satisfy regulator or insurer expectations under a tier-1 mechanical-integrity programme.
