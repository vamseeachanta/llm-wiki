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
last_updated: 2026-05-09
domain: engineering-standards
sources:
  - standards/api-510.md
  - standards/api-570.md
  - standards/api-653.md
---

# Risk-Based Inspection (RBI)

> Concept page. RBI is methodology, not a single standard; load-bearing normative content lives on the standards pages this concept routes into ([[api-510]], [[api-570]], [[api-653]], [[api-std-579]]) and on API RP 580 / RP 581 (future first-class pages).

## What is RBI?

**Risk-Based Inspection (RBI)** is a methodology that prioritises inspection effort by combining the **probability of failure (POF)** of an asset with its **consequence of failure (COF)** to give a **risk** ranking (risk = POF × COF). The risk ranking — typically rendered on a 5×5 matrix or as a quantitative $/year exposure — drives the inspection plan: high-risk items receive more frequent inspections, more sensitive techniques (PAUT, EMAT, ILI rather than spot UT), and tighter coverage; low-risk items receive longer intervals or less-invasive methods. The output is an inspection programme whose marginal inspection-hour buys the most marginal risk reduction.

## Why RBI replaces table-based intervals

Code-defined fixed-interval inspection — half-life or 10-year tank externals, 5-year piping circuits — applies one schedule across an asset population whose individual risk varies by orders of magnitude. The result is over-inspection of low-risk equipment (low-pressure utility piping, clean-service tanks) and under-inspection of high-risk equipment (sour-service vessels, hot hydrogen circuits, cyclic-service piping). RBI lets the inspection programme allocate inspection-hours where they reduce the most risk per dollar, rather than where the table happens to fall. RBI is **explicitly permitted** by [[api-510]] (§6, vessels), [[api-570]] (§6, piping), and [[api-653]] (§6, tanks) as an alternative to the half-life and table-based intervals, provided the programme conforms to API RP 580. RBI is **required by reference** for some tier-1 facilities under US OSHA Process Safety Management (29 CFR 1910.119) mechanical-integrity programmes, and for offshore topsides under several flag-state regimes that adopt DNV-RP-G101.

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

| Method | Reference | Output |
|---|---|---|
| Qualitative | API RP 580 + plant subject-matter expertise | Risk matrix (5×5 typical), category-banded POF and COF |
| Quantitative | API RP 581 (formerly the *RBI Base Resource Document*) | Calibrated POF + COF, $/year risk per asset |
| Semi-quantitative | Hybrid | Numeric POF + matrixed COF, or matrixed POF + monetised COF |
| ASME PCC-3 | parallel ASME methodology | Variant with broader equipment-class scope |
| DNV ORM / RIMAP | parallel European methodologies | Offshore-topsides and cross-sector variants; DNV-RP-G101 codifies the offshore application |

API RP 580 sets the *programme requirements* (governance, team competence, documentation, re-evaluation) that any RBI study must satisfy regardless of methodology. API RP 581 provides the *quantitative model* most commonly used for refinery and petrochemical applications. Most production RBI software packages implement an API RP 581-derived engine with operator-specific calibration.

## Workflow

1. **Asset register** — define the equipment population in scope (vessels, piping circuits, tanks, exchangers, relief devices), with as-built and current-state data.
2. **Damage-mechanism screening** — for each asset, identify credible damage mechanisms based on materials, fluid, temperature, pressure, and operating history (e.g. corrosion-under-insulation on cold-service piping, MIC on stagnant water draws, sulfidation on hot crude circuits, polythionic SCC on austenitic stainless during shutdowns).
3. **POF model** — combine damage-mechanism susceptibility, inspection effectiveness, and rate trends into a numeric or category-banded POF.
4. **COF model** — apply consequence model to the asset's fluid, inventory, location, and surroundings.
5. **Risk ranking** — plot POF × COF on a matrix or compute $/year; rank the asset population.
6. **Inspection plan optimisation** — set per-asset inspection interval, technique, and coverage so that residual risk lies below the operator's risk-acceptance threshold; document deferrals and any overrides.
7. **Re-evaluation cycle** — typically every 5–10 years, OR after material change (fluid, throughput, metallurgy, configuration), OR after an FFS finding that materially shifts a POF input.

## RBI + FFS interplay

RBI and Fitness-for-Service ([[fitness-for-service]]) are coupled, not parallel. When inspection finds a flaw exceeding the inspection-code acceptance threshold, two things happen:

1. **POF input shifts.** The asset's damage state is no longer probabilistic — a specific flaw has been characterised. The next RBI cycle's POF must incorporate the now-known damage, including any growth model (corrosion rate, fatigue-cycle accumulation, SCC growth law) calibrated against the inspection finding.
2. **FFS is invoked.** The flaw is assessed under [[api-std-579]] (or, for crack-like flaws, [[bs-7910-flaw-assessment]]) to produce a run / repair / replace / re-rate / re-inspect verdict. The FFS outcome — remaining-strength factor, remaining life, monitoring requirement — feeds back into the next RBI cycle's POF and into the inspection-plan re-optimisation.

This loop — inspection → finding → FFS → updated POF → revised inspection plan → next inspection — is the integrity-management cycle that ties [[api-510]] / [[api-570]] / [[api-653]] together with [[api-std-579]] and RBI under one programme.

## Standards

Bidirectional cross-references — each standards page below should cross-link back to this concept page once the convention propagates.

- [[api-510]] — Pressure Vessel Inspection Code; RBI is an explicit option for setting inspection intervals (§6 / §6.5), in lieu of half-life table-based intervals.
- [[api-570]] — Piping Inspection Code; RBI is an explicit option for piping-circuit inspection-interval setting.
- [[api-653]] — Atmospheric Storage Tank Inspection Code; RBI is an explicit option for tank external-, internal-, and bottom-inspection-interval setting.
- [[api-std-579]] — Fitness-for-Service; called when RBI surfaces a flaw exceeding code acceptance thresholds, and feeds back into the next RBI cycle's POF.
- **API RP 580** — *Risk-Based Inspection* — the programme-requirements recommended practice. Future first-class standards page candidate.
- **API RP 581** — *Risk-Based Inspection Methodology* — the quantitative POF + COF model. Future first-class standards page candidate.
- **ASME PCC-3** — *Inspection Planning Using Risk-Based Methods* — ASME's parallel RBI guide. Future first-class standards page candidate.
- [[dnv-rp-g101]] — Risk-Based Inspection of Offshore Topsides Static Mechanical Equipment — the offshore-topsides RBI recommended practice.

## Related concepts

Wikilinks below point to concept pages that may not yet exist — leave as wikilinks for future creation per the spinout's link-and-fill convention.

- [[fitness-for-service]] — downstream consumer of RBI inspection findings; the FFS verdict on a found flaw feeds back into the next RBI cycle's POF.
- [[corrosion-rate-measurement]] — UT thickness surveys, ILI runs, and coupon data that produce the corrosion-rate trends feeding RBI's POF.
- [[damage-mechanism-screening]] — the upstream analytical step (step 2 of the workflow) that identifies which damage mechanisms a given asset is credibly susceptible to; drives both POF construction and inspection-technique selection.
- [[fatigue-design-and-assessment]] — fatigue-cycle accumulation as a POF input for cyclic-service equipment.
- [[pitting-and-crevice-corrosion]] — localised damage mechanisms whose progression rate and detectability shape POF for stainless and CRA-clad equipment.

## Source materials

- [[og-standards-api]](../sources/og-standards-api.md) — catalog reference for API RP 580 and API RP 581 alongside the inspection-trilogy (API 510, API 570, API 653) and FFS-1 (API 579).

## Notes

- This is a concept page, not a standards page. No clause text, formulas, risk-matrix calibration tables, or consequence-model coefficients are reproduced here. For normative use, cite the publisher edition of API RP 580 and API RP 581 (or ASME PCC-3, or DNV-RP-G101) directly.
- RBI is a programme, not a single calculation. A spreadsheet POF × COF without the API RP 580 governance elements (team competence, documentation, re-evaluation triggers, management of change) is **not** a sanctioned RBI programme and will not satisfy regulator or insurer expectations.
- The §-references to API 510 / 570 / 653 above are directional pointers ("RBI is permitted in §6"); for clause-level citation, consult the publisher edition of the inspection code in question.
