---
title: "Risk-Based Inspection (RBI)"
slug: risk-based-inspection
tags:
  - rbi
  - inspection
  - risk-assessment
  - integrity-management
  - api-580
  - api-581
added: 2026-05-09
last_updated: 2026-05-10
domain: engineering-standards
sources:
  - standards/api-510.md
  - standards/api-570.md
  - standards/api-653.md
---

# Risk-Based Inspection (RBI)

> Concept page. RBI is methodology, not a single standard; load-bearing normative content lives on the standards pages this concept routes into ([api-510](../standards/api-510.md), [api-570](../standards/api-570.md), [api-653](../standards/api-653.md), [api-std-579](../standards/api-std-579.md)) and on API RP 580 / RP 581 (future first-class pages).

## What is RBI?

**Risk-Based Inspection (RBI)** is a methodology that prioritises inspection effort by combining the **probability of failure (POF)** of an asset with its **consequence of failure (COF)** to give a **risk** ranking (risk = POF × COF). The risk ranking — typically rendered on a 5×5 matrix or as a quantitative $/year exposure — drives the inspection plan: high-risk items receive more frequent inspections, more sensitive techniques (PAUT, EMAT, ILI rather than spot UT), and tighter coverage; low-risk items receive longer intervals or less-invasive methods. The output is an inspection programme whose marginal inspection-hour buys the most marginal risk reduction.

## Why RBI replaces table-based intervals

Code-defined fixed-interval inspection — half-life or 10-year tank externals, 5-year piping circuits — applies one schedule across an asset population whose individual risk varies by orders of magnitude. The result is over-inspection of low-risk equipment (low-pressure utility piping, clean-service tanks) and under-inspection of high-risk equipment (sour-service vessels, hot hydrogen circuits, cyclic-service piping). RBI lets the inspection programme allocate inspection-hours where they reduce the most risk per dollar, rather than where the table happens to fall. RBI is **explicitly permitted** by [api-510](../standards/api-510.md) (§6, vessels), [api-570](../standards/api-570.md) (§6, piping), and [api-653](../standards/api-653.md) (§6, tanks) as an alternative to the half-life and table-based intervals, provided the programme conforms to API RP 580. RBI is **required by reference** for some tier-1 facilities under US OSHA Process Safety Management (29 CFR 1910.119) mechanical-integrity programmes, and for offshore topsides under several flag-state regimes that adopt DNV-RP-G101.

## POF inputs

POF is built bottom-up from asset-specific data:

- **Damage-mechanism susceptibility** — corrosion (general thinning, localised, MIC, CUI), cracking (SCC, sulfide-stress, hydrogen-induced, chloride, caustic, polythionic), fatigue (mechanical, thermal, vibration), creep (high-temperature time-dependent), erosion, and metallurgical degradation (sigma-phase, temper embrittlement, graphitisation, HTHA). Damage-mechanism screening is the first analytical step.
- **Inspection effectiveness history** — how thoroughly the asset has been inspected previously, with which techniques, and what they detected (or failed to detect). API RP 581 categorises inspection effectiveness from "highly effective" down to "ineffective", and the POF curve relaxes as effective inspections accumulate evidence of low damage.
- **Inspection-finding extrapolations** — corrosion-rate trends derived from sequential UT thickness surveys, ILI run-comparison, or coupon data. Trend slope feeds the time-to-failure prior.
- **Age, condition, and design margin** — original construction code, corrosion allowance consumed, fabrication-flaw history, and as-built quality records.

## COF inputs

COF translates a postulated failure event into a multi-axis impact:

- **Flammable and toxic release scenarios** — release-rate modelling for vapour cloud, BLEVE, jet fire, pool fire, toxic dispersion. API RP 581 provides a consequence model that ingests fluid composition, inventory, and release-hole-size distribution.
- **Production loss and business interruption** — outage duration × throughput × margin, including downstream-unit dependency.
- **Environmental release** — soil and groundwater contamination, surface-water release, regulatory fines, remediation cost.
- **Personnel exposure** — workforce density in the affected zone, evacuation path, secondary-event escalation.
- **Asset-replacement cost** — repair vs. full-replacement cost of the failed component plus collateral damage to surrounding equipment.

COF can be expressed quantitatively ($/event) or as a category band (A–E or 1–5) for use in a risk matrix.

## Methodologies

RBI is implemented along a rigour spectrum. Choice of method is driven by data availability, regulator expectation, fleet size, and the operator's risk-acceptance posture. The three principal tiers are summarised below; in practice most fleet-scale programmes blend tiers across asset classes.

| Method | Reference | POF basis | COF basis | Output | Typical use |
|---|---|---|---|---|---|
| **Qualitative** | [api-rp-580](../standards/api-rp-580.md) + plant subject-matter expertise | Category-banded (1–5 / A–E) by SME judgement | Category-banded by SME judgement | Risk matrix (5×5 typical), risk category | Initial fleet screening; small populations; data-poor sites |
| **Semi-quantitative** | Hybrid of API RP 580 governance + simplified RP 581 model | Numeric POF (e.g. failure events per year) using simplified damage-factor look-up | Matrixed COF using release-rate banding | Numeric POF × matrixed COF, OR matrixed POF × monetised COF | Mid-rigour programmes; refining circuit-by-circuit; data-rich subset of a larger fleet |
| **Quantitative** | [api-rp-581](../standards/api-rp-581.md) (formerly the *RBI Base Resource Document*) | Calibrated damage-factor model with inspection-effectiveness Bayesian update | Level-1 (look-up) or Level-2 (CFD-grade dispersion) consequence model — $/event | Calibrated $/year risk per asset; sortable by absolute risk and risk-driver | Refinery / petrochem fleet RBI; insurance-grade risk reporting; PSM regulatory submissions |
| **ASME PCC-3** | *Inspection Planning Using Risk-Based Methods* (ASME parallel methodology) | Equivalent to API RP 580 + 581 with broader equipment scope | Same | Risk matrix or quantitative $/year | Cross-sector (power, chemicals, infrastructure); covers equipment classes outside API scope (heat-recovery boilers, BOP) |
| **DNV ORM / RIMAP** | DNV Offshore Risk Management; RIMAP CEN workshop agreement | Offshore-topsides damage-factor model (RP-G101 derivative) | Offshore COF model with personnel-on-board weighting | $/year risk + manning-weighted personnel risk | North Sea topsides; FPSO inspection planning; cross-sector European programmes |

[api-rp-580](../standards/api-rp-580.md) sets the *programme requirements* — governance, team competence, documentation, sign-off authority, re-evaluation triggers, management of change — that any RBI study must satisfy regardless of which numeric methodology is used. [api-rp-581](../standards/api-rp-581.md) provides the *quantitative damage-factor and consequence model* most widely deployed in refining and petrochemical service. Most production RBI software packages (Meridium, Visions/Bentley, Antea, Credo) implement an API RP 581-derived engine and overlay operator-specific calibration on damage-mechanism susceptibility scores. ASME PCC-3 covers a broader equipment universe — including waste-heat boilers, fired heaters, and HRSGs — that sits outside the API inspection-trilogy scope. [dnv-rp-g101](../standards/dnv-rp-g101.md) codifies the offshore-topsides application and is the de-facto reference for North Sea and tropical-FPSO topsides RBI; [dnv-rp-c210](../standards/dnv-rp-c210.md) provides probabilistic-fatigue methods that feed into RBI of cyclic offshore equipment.

### POF tier definitions (5×5 matrix)

A common 5×5 POF banding — used by API RP 580 examples and most operator standards — quantises annual failure-likelihood into ordinal categories:

| POF tier | Annual failure frequency | Description |
|---|---|---|
| 1 — Very Low | < 1×10⁻⁵ /yr | New equipment, conservative design margin, known-benign service, recent highly-effective inspection clearing all credible damage mechanisms |
| 2 — Low | 1×10⁻⁵ to 1×10⁻⁴ /yr | Mature equipment in mild service, regular inspection, no active damage indicators |
| 3 — Medium | 1×10⁻⁴ to 1×10⁻³ /yr | Active but bounded damage mechanism (general thinning at known rate, low SCC susceptibility) with ongoing monitoring |
| 4 — High | 1×10⁻³ to 1×10⁻² /yr | Aggressive damage mechanism (sour service, HTHA-susceptible, sulfidation, CUI-susceptible insulated lines), inspection effectiveness fair to poor |
| 5 — Very High | > 1×10⁻² /yr | Active damage with degraded margin, prior inspection finding above acceptance, near end of service life, inspection effectiveness ineffective |

The numeric anchors above are illustrative; operator-calibrated programmes adjust the band breaks using their own historical leak/failure data. Per [api-rp-581](../standards/api-rp-581.md), the POF for a given asset is the product of a *generic failure frequency* (industry-pooled by equipment class), a *damage-factor* (asset-specific for active mechanisms), and a *management-systems factor* (operator's PSM maturity).

### COF tier definitions

COF is multi-dimensional — safety, environmental, financial, reputational. A common collapsing scheme bands the worst-case axis into the same 1–5 ordinal:

| COF tier | Safety (fatalities) | Environmental | Financial | Reputational |
|---|---|---|---|---|
| A — Very Low | None credible | Containable on-site | < $100k | Internal only |
| B — Low | Single first-aid case | On-site spill, no off-site impact | $100k–$1M | Local |
| C — Medium | Lost-time injury | Off-site reportable spill | $1M–$10M | Regional press |
| D — High | Single fatality | Major off-site environmental impact | $10M–$100M | National press, regulatory enforcement |
| E — Very High | Multiple fatalities | Catastrophic environmental damage | > $100M | International press, license-to-operate threat |

The asset's COF tier is the **highest-axis** category, not an average — a tank rupture that destroys $5M of inventory but kills nobody is rated C on financial and A on safety, COF = C overall. Quantitative RBI under [api-rp-581](../standards/api-rp-581.md) replaces the band with a calibrated $/event consequence (jet-fire footprint, vapour-cloud LFL contour, pool-fire flame area, toxic-dispersion AEGL contour) and produces a numeric risk in $/year.

### 5×5 vs 4×4 matrix variations

The 5×5 risk matrix (25 cells) is the most common in API RP 580 example material and operator standards, but 4×4 (16 cells), 6×6 (36 cells), and 3×3 (9 cells) variants exist:

- **3×3** — used in initial-screening exercises and small-fleet programmes (< 100 assets); coarse banding accepts more false-positives in the High band in exchange for analytical simplicity.
- **4×4** — common in offshore-topsides programmes and some refining operators; deliberately removes the "middle" category that 5×5 produces, forcing a binary acceptable / not-acceptable disposition above the diagonal.
- **5×5** — the API RP 580 reference. Cell colouring (green / yellow / orange / red) typically follows the diagonal-band convention: cells along and below the anti-diagonal are acceptable; cells above are unacceptable and require risk-reduction action.
- **6×6** — used by some quantitative RBI implementations to provide finer resolution at the high-COF end (E1-E2 catastrophic-but-rare distinction matters for insurance loss-modelling).

The matrix is a presentation layer over an underlying numeric risk; the matrix shape does not change the numerator (risk = POF × COF) or the action thresholds, only the granularity at which they are reported.

### Inspection-effectiveness categories

[api-rp-581](../standards/api-rp-581.md) Annex 2.C introduced the inspection-effectiveness categorisation that updates the POF when an inspection result is fed back into the model. Categories quantify both *detection probability* (how likely the inspection technique would have found the damage if present) and *coverage confidence* (how representative the inspected sample is of the asset population):

| Category | Label | Detection probability | Coverage | POF Bayesian-update effect |
|---|---|---|---|---|
| **A** | Highly Effective | > 80% for the credible damage mechanism | Full or representative | Strong reduction; damage-factor halved or quartered after a clear A inspection |
| **B** | Usually Effective | 60–80% | Partial but representative | Moderate reduction |
| **C** | Fairly Effective | 40–60% | Partial | Modest reduction |
| **D** | Poorly Effective | 20–40% | Limited | Minimal reduction |
| **E** | Ineffective | < 20% | Insufficient | No POF credit; model treats asset as un-inspected |

Effectiveness is **mechanism-specific** — a UT thickness scan is highly effective (A) for general thinning but ineffective (E) for SCC. A radiographic survey is highly effective for through-thickness cracking but only fairly effective for shallow surface SCC. Inspection-technique selection in the RBI plan must match the credible damage mechanism identified in [damage-mechanism-screening](./damage-mechanism-screening.md), or the inspection burns hours without buying POF credit. This is the analytical core of why an RBI programme directs *which* technique, not just *when*.

## Workflow

1. **Asset register** — define the equipment population in scope (vessels, piping circuits, tanks, exchangers, relief devices), with as-built and current-state data.
2. **Damage-mechanism screening** — for each asset, identify credible damage mechanisms based on materials, fluid, temperature, pressure, and operating history (e.g. corrosion-under-insulation on cold-service piping, MIC on stagnant water draws, sulfidation on hot crude circuits, polythionic SCC on austenitic stainless during shutdowns).
3. **POF model** — combine damage-mechanism susceptibility, inspection effectiveness, and rate trends into a numeric or category-banded POF.
4. **COF model** — apply consequence model to the asset's fluid, inventory, location, and surroundings.
5. **Risk ranking** — plot POF × COF on a matrix or compute $/year; rank the asset population.
6. **Inspection plan optimisation** — set per-asset inspection interval, technique, and coverage so that residual risk lies below the operator's risk-acceptance threshold; document deferrals and any overrides.
7. **Re-evaluation cycle** — typically every 5–10 years, OR after material change (fluid, throughput, metallurgy, configuration), OR after an FFS finding that materially shifts a POF input.

## RBI + FFS integration

RBI and [fitness-for-service](./fitness-for-service.md) (FFS, codified in [api-579-1-asme-ffs-1](../standards/api-579-1-asme-ffs-1.md) / [api-std-579](../standards/api-std-579.md)) are coupled, not parallel. When inspection finds a flaw exceeding the inspection-code acceptance threshold, two things happen in the same cycle:

1. **POF input shifts.** The asset's damage state is no longer probabilistic — a specific flaw has been characterised. The next RBI cycle's POF must incorporate the now-known damage, including any growth model (corrosion rate, fatigue-cycle accumulation, SCC growth law) calibrated against the inspection finding. For corrosion, the [corrosion-rate-measurement](./corrosion-rate-measurement.md) trend at the inspection site replaces the prior corrosion-allowance-consumed estimate. For cracking, the [fatigue-crack-growth](./fatigue-crack-growth.md) Paris-law parameters or the [stress-corrosion-cracking](./stress-corrosion-cracking.md) growth law are calibrated to the observed flaw geometry.
2. **FFS is invoked.** The flaw is assessed under [api-std-579](../standards/api-std-579.md) (or, for crack-like flaws, [bs-7910-flaw-assessment](../standards/bs-7910-flaw-assessment.md) and [engineering-critical-assessment](./engineering-critical-assessment.md)) to produce a run / repair / replace / re-rate / re-inspect verdict. The FFS outcome — remaining-strength factor (RSF), remaining life, monitoring requirement, allowable operating envelope — feeds back into the next RBI cycle's POF and into the inspection-plan re-optimisation.

This loop — inspection → finding → FFS → updated POF → revised inspection plan → next inspection — is the *integrity-management cycle* that ties [api-510](../standards/api-510.md) / [api-570](../standards/api-570.md) / [api-653](../standards/api-653.md) together with [api-std-579](../standards/api-std-579.md) and RBI under one programme. In mature operators, the cycle is instrumented in software with a single asset-master record so that an FFS Level-2 assessment automatically updates the next RBI re-evaluation's damage factor without manual transcription.

## Worked-example case studies

The following sketches show how RBI scoping differs across industry segments. Numbers are illustrative — they show *which inputs dominate*, not specific operator practice.

### Refinery — sour-service hydrotreater circuit

A hydrotreater feed-effluent exchanger train carries hot crude with H₂S concentration ~5,000 ppm at 320 °C and 80 bar. Damage mechanisms identified in [damage-mechanism-screening](./damage-mechanism-screening.md): [sulfidation-and-naphthenic-acid](./sulfidation-and-naphthenic-acid.md) (modified McConomy curve), [hydrogen-embrittlement](./hydrogen-embrittlement.md) (HIC / SOHIC on the carbon-steel shell), and high-temperature cracking risk from temper embrittlement on 2¼Cr-1Mo internals. POF tier sits at 4 (High) because all three mechanisms are credibly active. COF is D (High) — large hydrocarbon inventory, jet-fire footprint reaches the operator control room. Risk = 4×D, sitting in the red zone of a 5×5 matrix. Inspection plan: AUT thickness mapping at 100% coverage every 4 years (Category A for thinning), wet-fluorescent-MT on weld toes for HIC every 4 years (Category B for cracking), and Charpy V-notch testing on a sentinel coupon at each turnaround. The RBI cycle drives both *frequency* (4 years vs the [api-510](../standards/api-510.md) half-life default of 5–10) and *technique selection*.

### Offshore platform — North Sea topsides

An FPSO process-deck riser-pipework circuit operates at 60 bar, 80 °C, with chloride-bearing produced water. Damage mechanisms: [pitting-and-crevice-corrosion](./pitting-and-crevice-corrosion.md) on austenitic-stainless flanges, [microbiologically-influenced-corrosion](./microbiologically-influenced-corrosion.md) at low-flow dead-legs, and external [corrosion-under-insulation](./corrosion-under-insulation.md) at insulation breaches. The programme follows [dnv-rp-g101](../standards/dnv-rp-g101.md) rather than [api-rp-580](../standards/api-rp-580.md)/[api-rp-581](../standards/api-rp-581.md) because the regulator (UK HSE under SCR 2015 or NPD on the Norwegian shelf) recognises the DNV methodology. COF weighting is dominated by personnel-on-board — POB count of 80 with limited muster-and-evacuate options pushes a credible jet-fire scenario to E (Very High). Inspection plan: ROV-deployed UT crawler for splash-zone external corrosion, RFT (Remote-Field Testing) for under-insulation thinning, biocide-residual sampling at dead-legs.

### Petrochem — ethylene cracker furnace tubes

Ethylene-cracker radiant-coil HK-40 cast tubes operate at 1,050 °C metal temperature with 350 ppm steam dilution. Damage mechanism: [creep-and-stress-rupture](./creep-and-stress-rupture.md) (Larson-Miller parameter against published rupture curves), supplemented by carburisation from coke deposition. POF model is bottom-up creep-life consumption; an inspection cycle (Eddy-current dimensional check + radiographic carburisation depth measurement) feeds straight into a remaining-life calc per [api-std-579](../standards/api-std-579.md) Part 10 (Creep). RBI here is essentially a creep-life programme; the POF curve is a deterministic time-to-rupture with a probabilistic envelope from cast-to-cast metallurgical variation.

### LNG terminal — marine loading-arm flexible

An LNG-terminal liquid loading-arm presented under [csa-z276](../../../lng-projects/wiki/standards/csa-z276.md) and an FSRU pipework circuit per the FSRU marine-terminal interface present a low-temperature ([brittle-fracture](./brittle-fracture.md)) damage mode rather than a thinning mode. POF inputs are dominated by [thermal-fatigue](./thermal-fatigue.md) cycle accumulation per shipment and by [fracture-toughness-measurement](./fracture-toughness-measurement.md) of the 9% Ni or austenitic-stainless base metal. COF is dominated by cryogenic vapour-cloud dispersion modelling — the cold dense vapour cloud expands at near-ground level and reaches LFL distances much greater than equivalent-mass hydrocarbon releases. Inspection plan: helium leak-test on bellows expansion joints every 12 months, dye-penetrant on weld toes every 24 months, fracture-toughness re-qualification of replacement spools per [astm-e1921](../standards/astm-e1921.md) master-curve methodology.

## Standards landscape

The standards governing RBI fall into three groups: the *programme-requirements* layer (governance, team competence, re-evaluation), the *methodology* layer (POF and COF models), and the *enabling inspection codes* layer (which permit RBI as an alternative to fixed intervals). Bidirectional cross-references — each standards page below should cross-link back to this concept page.

### Programme requirements
- [api-rp-580](../standards/api-rp-580.md) — *Risk-Based Inspection* — programme-requirements recommended practice (governance, team competence, documentation, re-evaluation triggers, MoC). Sets the qualitative-tier baseline.
- **ASME PCC-3** — *Inspection Planning Using Risk-Based Methods* — ASME's parallel RBI programme document; covers equipment classes outside the API inspection-trilogy (HRSGs, fired heaters, BOP). First-class standards page candidate.

### Methodology
- [api-rp-581](../standards/api-rp-581.md) — *Risk-Based Inspection Methodology* — the quantitative POF + COF model with calibrated damage factors and Level-1/Level-2 consequence model.
- [dnv-rp-c210](../standards/dnv-rp-c210.md) — Probabilistic Methods for Planning of Inspection for Fatigue Cracks in Offshore Structures — supplies the probabilistic-fatigue input to RBI of cyclic offshore equipment.

### Enabling inspection codes
- [api-510](../standards/api-510.md) — Pressure Vessel Inspection Code; RBI is an explicit option for setting inspection intervals (§6 / §6.5), in lieu of half-life table-based intervals.
- [api-570](../standards/api-570.md) — Piping Inspection Code; RBI is an explicit option for piping-circuit inspection-interval setting.
- [api-653](../standards/api-653.md) — Atmospheric Storage Tank Inspection Code; RBI is an explicit option for tank external-, internal-, and bottom-inspection-interval setting.
- [api-std-579](../standards/api-std-579.md) / [api-579-1-asme-ffs-1](../standards/api-579-1-asme-ffs-1.md) — Fitness-for-Service; called when RBI surfaces a flaw exceeding code acceptance thresholds, and feeds back into the next RBI cycle's POF.
- [api-rp-571](../standards/api-rp-571.md) — Damage Mechanisms Affecting Fixed Equipment in the Refining Industry — the canonical taxonomy underlying refinery damage-mechanism screening.
- [api-rp-583](../standards/api-rp-583.md) — Corrosion Under Insulation and Fireproofing — a damage-specific recommended practice that supplies CUI POF inputs.
- [api-rp-577](../standards/api-rp-577.md) — Welding Inspection and Metallurgy — feeds inspection-effectiveness categorisation for weld-toe inspection.

### Sector-specific
- [dnv-rp-g101](../standards/dnv-rp-g101.md) — Risk-Based Inspection of Offshore Topsides Static Mechanical Equipment — the offshore-topsides RBI recommended practice; widely adopted on UK/Norwegian Continental Shelf and tropical-FPSO programmes.
- **ISO 17776** — *Petroleum and natural gas industries — Offshore production installations — Major accident hazard management during the design of new installations* — provides the offshore-lifecycle major-accident integration that RBI plugs into; first-class standards page candidate.
- **RIMAP CWA 15740** — CEN Workshop Agreement on Risk-Based Inspection and Maintenance Procedures — pan-European cross-sector RBI methodology; complementary to API RP 580/581 and ASME PCC-3.

## Industry adoption

RBI uptake varies sharply by sector and by regulator:

- **Refining and petrochem (USA / EU / Asia)** — RBI is the dominant inspection-planning paradigm. US OSHA Process Safety Management (29 CFR 1910.119) mechanical-integrity requirements and EPA Risk Management Plan rules are typically met through an [api-rp-580](../standards/api-rp-580.md) / [api-rp-581](../standards/api-rp-581.md) programme. Insurers (FM Global, Chubb-Allianz industrial, Lloyd's energy syndicates) require RBI evidence at renewal.
- **Offshore upstream** — Topsides static equipment under [dnv-rp-g101](../standards/dnv-rp-g101.md); subsea pipelines under [dnv-rp-f101](../standards/dnv-rp-f101.md) RBI overlay; floating-system structural integrity overlaps the [mooring-integrity-management](./mooring-integrity-management.md) programme. UK HSE Safety Case Regulations 2015 and Norwegian PSA expect demonstrable RBI. ABS, DNV, BV, and LR all publish offshore-RBI class notations.
- **LNG terminals and FSRUs** — RBI is overlaid on the standards in [csa-z276](../../../lng-projects/wiki/standards/csa-z276.md) and IGC-Code regimes; emphasis shifts from thinning to brittle-fracture and cryogenic vapour-cloud COF.
- **Power generation** — RBI is well-established for HRSGs and conventional-power steam-cycle equipment under ASME PCC-3, less so for nuclear (which has a parallel ASME Section XI inservice-inspection programme).
- **Pipelines (onshore)** — Integrity Management Programs under 49 CFR 192/195 are conceptually RBI but are codified separately under [asme-b31-8](../standards/asme-b31-8.md), [asme-b31-4](../standards/asme-b31-4.md), and [api-rp-1111](../standards/api-rp-1111.md) for offshore pipelines; the [opa-90](../../../maritime-law/wiki/concepts/opa-90.md) regulatory framework drives spill-response COF inputs for marine-impact-zone segments.
- **Maritime and offshore safety integration** — RBI of mechanical equipment connects to vessel-level safety management under the [ism-code](../../../maritime-law/wiki/concepts/ism-code.md). The 2021 IMO Resolution MSC.428(98) cybersecurity amendment to the ISM Code extends safety-management-system scope to OT/ICS networks, opening a *cybersecurity-RBI* extension where consequence-of-cyber-failure becomes a COF axis alongside safety, environment, financial, and reputational axes. This extension is most active on FPSO, MODU, and LNG-carrier programmes where integrated-control-system compromise can drive a release scenario as severely as a mechanical failure.

## Source materials

- [og-standards-api](../sources/og-standards-api.md) — catalog reference for [api-rp-580](../standards/api-rp-580.md), [api-rp-581](../standards/api-rp-581.md), [api-rp-571](../standards/api-rp-571.md), and the inspection-trilogy ([api-510](../standards/api-510.md), [api-570](../standards/api-570.md), [api-653](../standards/api-653.md)) plus [api-std-579](../standards/api-std-579.md).
- [og-standards-asme](../sources/og-standards-asme.md) — catalog reference for ASME PCC-3 and the BPVC inspection-code linkages.
- [og-standards-dnv](../sources/og-standards-dnv.md) — catalog reference for [dnv-rp-g101](../standards/dnv-rp-g101.md) and [dnv-rp-c210](../standards/dnv-rp-c210.md).

## Related concepts

- [fitness-for-service](./fitness-for-service.md) — downstream consumer of RBI inspection findings; the FFS verdict on a found flaw feeds back into the next RBI cycle's POF (see also [api-std-579](../standards/api-std-579.md)).
- [corrosion-rate-measurement](./corrosion-rate-measurement.md) — UT thickness surveys, ILI runs, and coupon data that produce the corrosion-rate trends feeding RBI's POF.
- [damage-mechanism-screening](./damage-mechanism-screening.md) — the upstream analytical step (step 2 of the workflow) that identifies which damage mechanisms a given asset is credibly susceptible to; drives both POF construction and inspection-technique selection.
- [fatigue-design-and-assessment](./fatigue-design-and-assessment.md) — fatigue-cycle accumulation as a POF input for cyclic-service equipment.
- [fatigue-crack-growth](./fatigue-crack-growth.md) — Paris-law growth model used to set POF and re-inspection intervals for cyclic equipment with characterised flaws.
- [pitting-and-crevice-corrosion](./pitting-and-crevice-corrosion.md) — localised damage mechanisms whose progression rate and detectability shape POF for stainless and CRA-clad equipment.
- [htha-nelson-curves](./htha-nelson-curves.md) — high-temperature hydrogen-attack damage factor is a first-class POF input under [api-rp-581](../standards/api-rp-581.md) Part 2 for hydroprocessing fleet RBI prioritisation.
- [stress-corrosion-cracking](./stress-corrosion-cracking.md) — SCC family (Cl-SCC, polythionic, caustic, carbonate, amine, sour-service) is a major POF input for the cracking damage class in API RP 581.
- [hydrogen-embrittlement](./hydrogen-embrittlement.md) — HIC / SOHIC / SSC mechanisms drive POF for sour-service carbon-steel equipment.
- [sulfidation-and-naphthenic-acid](./sulfidation-and-naphthenic-acid.md) — high-temperature sulfidic and naphthenic-acid corrosion driving POF for hot-crude refinery service.
- [corrosion-under-insulation](./corrosion-under-insulation.md) — CUI is a dominant offshore-topsides POF input and the principal subject of [api-rp-583](../standards/api-rp-583.md).
- [microbiologically-influenced-corrosion](./microbiologically-influenced-corrosion.md) — MIC is a damage mode for stagnant water-leg POF inputs.
- [creep-and-stress-rupture](./creep-and-stress-rupture.md) — creep-life-fraction consumed is a POF input for high-temperature equipment.
- [thermal-fatigue](./thermal-fatigue.md) — thermal-cycle damage in cryogenic and high-temperature service.
- [brittle-fracture](./brittle-fracture.md) — low-temperature failure mode driving COF severity for cryogenic and arctic-service equipment.
- [engineering-critical-assessment](./engineering-critical-assessment.md) — ECA closes the FFS loop for crack-like flaws and feeds back into POF.
- [erosion-and-fac](./erosion-and-fac.md) — flow-accelerated corrosion as a POF input for high-velocity wet steam and produced-fluids equipment.
- [sour-service-materials](./sour-service-materials.md) — sour-service material qualification under [iso-15156](../standards/iso-15156.md) bounds the credible cracking-damage POF.
- [mooring-integrity-management](./mooring-integrity-management.md) — sister integrity-management programme for floating-system mooring equipment.

## Notes

- This is a concept page, not a standards page. No clause text, formulas, risk-matrix calibration tables, or consequence-model coefficients are reproduced here. For normative use, cite the publisher edition of API RP 580 and API RP 581 (or ASME PCC-3, or DNV-RP-G101) directly.
- RBI is a programme, not a single calculation. A spreadsheet POF × COF without the API RP 580 governance elements (team competence, documentation, re-evaluation triggers, management of change) is **not** a sanctioned RBI programme and will not satisfy regulator or insurer expectations.
- The §-references to API 510 / 570 / 653 above are directional pointers ("RBI is permitted in §6"); for clause-level citation, consult the publisher edition of the inspection code in question.
