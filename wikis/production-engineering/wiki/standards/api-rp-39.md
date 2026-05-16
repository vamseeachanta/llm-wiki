---
title: "API RP 39 — Measuring the Viscous Properties of a Cross-linked Water-Based Fracturing Fluid"
code_id: api-rp-39
publisher: American Petroleum Institute
revision: "4th Edition (most recent edition tracked on api.org; first published 1998)"
jurisdiction: international
tags: [recommended-practice, api, hydraulic-fracturing, frac-fluid, rheology, viscosity-testing, crosslinked-gel]
sources:
  - api-rp-39
added: 2026-05-16
last_updated: 2026-05-16
---

# API RP 39 — Measuring the Viscous Properties of a Cross-linked Water-Based Fracturing Fluid

## Scope

API RP 39 is the practitioner-canonical recommended practice for the **laboratory measurement of viscosity** of crosslinked water-based hydraulic-fracturing fluids. It defines the rotational-viscometer methodology, the shear-rate / temperature / time test envelope, and the data-reporting format used to qualify a frac-fluid system for service. The standard does **not** prescribe which fluid system an operator should use for any given treatment; its scope is bounded to the methodology that produces apples-to-apples viscosity-vs-time curves for vendor-quoted frac-fluid systems under defined laboratory conditions.

Operators then apply judgement (and proprietary frac-fluid-selection workflows) to translate RP 39 test data into field expectations for proppant transport, fluid-loss control, and post-treatment cleanup.

## Why operators read it

- **Vendor-comparison framework** — without a common test methodology, vendor-quoted frac-fluid viscosity curves cannot be compared meaningfully. RP 39 is the widely-adopted standardised methodology for crosslinked water-based systems.
- **Acceptance-test reference** — operators specifying frac-fluid systems often write acceptance tests against RP 39 viscosity-vs-time thresholds at specified bottomhole-static-temperature (BHST) conditions.
- **Frac-design model inputs** — frac-design models (PKN, KGD, pseudo-3D, 3D — see [Frac Design](../concepts/frac-design.md)) require fluid-viscosity inputs as a function of time and temperature. The viscosity-vs-time curves produced under RP 39 conditions are the standard input source.
- **Post-treatment cleanup framing** — viscosity must be high enough during pumping and proppant transport, then low enough for flowback and cleanup. The RP 39 viscosity-decay curve is the operator's primary handle on cleanup-time expectations.

## Test methodology (structural overview)

The standard defines a rotational-viscometer test conducted at controlled bottomhole-static temperature with the fluid sample sheared for a defined duration. The exact viscometer geometry, shear-rate sequence, and temperature ramp have evolved across editions and are not transcribed here (paywalled standard); the structural intent is stable:

- **Constant-temperature isothermal test** — the fluid sample is heated to the planned BHST, then sheared at a controlled shear rate for a defined duration (typically 1-2 hours). Viscosity is recorded as a function of time. The operator reads the curve to estimate how long the fluid will retain transport-quality viscosity at downhole temperature.
- **Shear-rate sweep** — at fixed time and temperature, shear rate is varied across a defined range. The resulting viscosity-vs-shear-rate curve characterises the fluid's non-Newtonian behaviour (power-law, Herschel-Bulkley, or similar rheological model).
- **Temperature-ramp test** — the fluid sample is sheared while temperature is raised from surface to BHST on a defined ramp. This characterises the crosslinker-activation kinetics and the time-window between mixing and full crosslink.
- **Breaker-response test** — after the main viscosity sequence, an enzymatic or oxidative breaker is added (or the temperature held long enough for breaker self-activation) and viscosity decay is recorded. This characterises the post-treatment cleanup time.

The standard specifies viscometer geometry (typically Bob-cup, Couette geometry) and data-reduction formulas (apparent viscosity at the reference shear rate). Operators reading vendor frac-fluid data sheets should always check that the quoted viscosity-vs-time data was produced under RP 39 conditions; ad-hoc or simplified viscometer protocols can overstate downhole performance.

## What the data is used for downstream

Frac-design simulators (see [Frac Design](../concepts/frac-design.md)) consume RP 39 viscosity-vs-time data in three ways:

1. **Proppant-settling models** — the carrier fluid's viscosity at downhole shear rate determines proppant settling velocity per Stokes' law (or its Newtonian-correction descendants). Insufficient viscosity at BHST allows proppant to settle out of the frac near the wellbore, choking width and conductivity.
2. **Fluid-loss models** — viscous fluid leaks off into the formation more slowly than thin fluid. Viscosity-vs-time data feeds the leak-off coefficient calculation that sets the pad-volume requirement.
3. **Net-pressure / closure-tracking models** — frac propagation is driven by net pressure (treating pressure minus closure pressure), and net pressure is set by the fluid's effective viscosity in the frac at downhole shear rate. Viscosity data is the input that lets the simulator predict frac width vs length over treatment time.

When the RP 39 test data shows viscosity decay faster than the simulator's design assumption, the operator must either pump a higher-loaded carrier fluid (more guar or other thickener), switch to a higher-temperature crosslinker chemistry, or shorten the planned treatment time.

## Adjacent standards

- **API RP 42** — *Recommended Practices for Laboratory Testing of Surface Active Agents for Well Stimulation* — sister standard, surfactant-additive testing methodology used alongside RP 39 in many frac-fluid qualification programmes.
- **ISO 13503** series — *Petroleum and natural gas industries — Completion fluids and materials* — covers proppant qualification (pack permeability, conductivity, embedment), which is the proppant-side counterpart to RP 39's fluid-side methodology.
- **NACE MR0175 / ISO 15156** — sour-service material requirements applicable to frac-equipment metallurgy (frac-iron, treating-line connections, wellhead components).

## Concept-page references

- [Hydraulic Fracturing](../concepts/hydraulic-fracturing.md) — the production-engineering router page for hydraulic-fracturing coverage
- [Frac Fluids](../concepts/frac-fluids.md) — five frac-fluid families (slickwater, linear gel, crosslinked, energized, foamed) with rheology + cleanup characteristics
- [Frac Design](../concepts/frac-design.md) — PKN / KGD / pseudo-3D / 3D width formulas + pump-schedule design
- [Proppants](../concepts/proppants.md) — sand / resin-coated sand / ceramic / ultra-light proppant families with ISO 13503 qualification framework

## Cross-references

- **Sand-control coupling** — frac-pack treatments (see [Frac Packing](../concepts/frac-packing.md)) consume crosslinked frac-fluid systems characterised under RP 39, with tip-screenout (TSO) design requiring tighter control of viscosity-decay than conventional frac treatments.
- **Drilling-engineering coupling** — production-casing burst margin (see [Casing Program Design](../../../drilling-engineering/wiki/concepts/casing-program-design.md)) accommodates the surface treating pressure that depends on fluid viscosity (higher fluid viscosity → higher friction-pressure → higher treating pressure).
- **Vendor-archetype framing** — frac-service vendors (Halliburton, Schlumberger, Baker Hughes, Liberty, ProFrac, and many independents) publish frac-fluid system data sheets citing RP 39 test conditions; concept-level only, no proprietary chemistry or recipe content reproduced here.

## Public references

- **API** — official publication page for API RP 39 (current edition retrievable from api.org). First published 1998 (1st edition); subsequent editions have refined viscometer geometry and shear-rate ranges.
- **Economides, M. J. & Nolte, K. G. (eds.)** — *Reservoir Stimulation*, 3rd ed., Wiley, 2000 (ISBN 978-0-471-49192-7). Industry-canonical reference; chapters on frac-fluid rheology contextualise the methodology that RP 39 formalises.
- **Howard, G. C. & Fast, C. R.** — *Hydraulic Fracturing*, SPE Monograph Series Vol. 2, 1970. Foundational hydraulic-fracturing reference; pre-RP 39 era frac-fluid rheology testing methodology.
- **SPE OnePetro frac-fluid literature** — extensive corpus on viscometer-test-vs-field-performance correlation, especially for high-temperature (>275°F BHST) frac systems where the RP 39 methodology evolved most rapidly.
- **Lyons, W. C. (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, Elsevier (ISBN 978-0-7506-7785-1) — hydraulic-fracturing chapter covering frac-fluid rheology testing.

## Notes

- API RP 39 revisions have been issued multiple times since the 1st edition (1998). Operators specifying frac-fluid-system acceptance tests should always pin to a specific edition in their AFE / scope-of-work documents.
- The standard's scope is intentionally narrow — crosslinked water-based systems only. Non-crosslinked (linear-gel, slickwater) and non-water-based (foam, energized, oil-based) frac fluids fall outside its direct scope, though the rotational-viscometer methodology is widely adapted to those systems by reference.
- API RP 39 is paywalled. This wiki paraphrases the structural intent and references the standard for operators who already have a licensed copy. No verbatim text reproduced.
