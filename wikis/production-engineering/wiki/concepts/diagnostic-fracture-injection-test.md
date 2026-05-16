---
title: "Diagnostic Fracture Injection Test (DFIT)"
tags: [dfit, diagnostic-fracture-injection-test, mini-frac, pre-frac-test, closure-pressure, isip, leak-off, pressure-derivative, in-situ-stress, refrac, hydraulic-fracturing]
added: 2026-05-16
last_updated: 2026-05-16
---

# Diagnostic Fracture Injection Test (DFIT)

## Scope

A Diagnostic Fracture Injection Test (DFIT), also known as a pre-frac mini-frac or fracture-calibration test, is a small-volume low-rate injection test pumped before the main hydraulic-fracturing treatment (or before a refrac treatment) with the explicit goal of measuring the in-situ properties needed to design that treatment. The DFIT delivers four primary measurements:

1. **Closure pressure** — the in-situ minimum-horizontal-stress, which controls fracture initiation pressure and proppant-pack stress
2. **ISIP (Instantaneous Shut-In Pressure)** — the pressure at the instant pumping stops, used to bound the closure-pressure estimate from above
3. **Leak-off coefficient** — fluid loss per unit fracture-face area per unit square-root of time, which controls pad-volume sizing
4. **Reservoir pressure and permeability** — extracted from the long-time portion of the pressure-decline transient when the test is run long enough

DFIT is the dominant pre-frac diagnostic in modern hydraulic-fracturing practice. It supersedes the older step-rate test in most operator workflows because it delivers more measurements per dollar spent and because its pressure-decline transient — once correctly interpreted — characterises the formation more completely.

## Why DFIT is the dominant pre-frac diagnostic

DFIT is the dominant pre-frac diagnostic because the four measurements it delivers are the four parameters that dominate hydraulic-fracturing design uncertainty. Without DFIT measurements, the operator must rely on:

- **Regional analog data** for closure pressure, which can be off by 1,000-2,000 psi in some basins and produces correspondingly large frac-design errors
- **Generic leak-off coefficients** for the formation, which can be off by orders of magnitude in heterogeneous reservoirs and produces correspondingly large pad-volume errors
- **Indirect estimates** of present-day reservoir pressure, which can be far off in depleted reservoirs and which is critical for refrac candidate-selection

With DFIT measurements, the operator has formation-specific values for all four parameters, and the resulting frac-design uncertainty is reduced to the irreducible variability of rock and fluid properties.

DFIT is particularly important for refrac candidate selection (see [Refrac](refrac.md)) because depletion of the original stimulated rock volume can shift the closure pressure, re-orient the stress field, and change the leak-off behaviour from the original-completion values. A refrac DFIT is treated as mandatory in modern practice because the present-day in-situ state cannot be inferred from the original-completion data.

## DFIT procedure

A DFIT is pumped through the same surface and downhole equipment as the planned frac job, but with a much smaller fluid volume and a much lower pump rate. The procedure follows a fixed sequence:

### Stage 1: Injection

Clean fluid (typically low-viscosity water or 2% KCl brine to avoid clay-swelling complications) is pumped at low rate (typically 1-5 bbl/min) until a small fracture has been initiated and grown. Total injection volume is typically 50-500 bbl. The injection is held until the injected fluid has formed a fracture detectable by the pressure-rate response (a clear inflection in the pressure-vs-rate slope, indicating that the formation is now accepting fluid at fracture rather than matrix rate).

### Stage 2: Shut-in and pressure-decline monitoring

Pumping stops abruptly. The wellhead pressure is recorded at high time-resolution (typically 1-second or finer) for the entire pressure-decline transient, which can extend from hours (for high-permeability formations where pressure equilibrates quickly) to weeks (for low-permeability shale formations where pressure equilibration takes that long).

The pressure-decline transient is the data record from which all four DFIT measurements are extracted. The interpretation framework — pressure-derivative diagnostic plots, before-closure and after-closure analysis windows, and the specific pressure-vs-time-function plots that diagnose each flow regime — is the subject of an extensive industry literature (the Barree, Nolte, and Mayerhofer corpus in particular).

### Stage 3: Data extraction and interpretation

The shut-in pressure-decline data are processed through a sequence of diagnostic plots that identify the dominant flow regime at each stage of the decline:

- **Pressure vs square-root-of-time (Nolte G-function)** — characterises the before-closure flow regime when the fracture is still open and the dominant pressure drop is leak-off into the formation
- **G-function derivative** — diagnoses the leak-off mechanism (normal leak-off, pressure-dependent leak-off, tip-extension after shut-in, fissure-opening behaviour, transverse-storage)
- **Pressure vs time** — identifies the closure event as a clear inflection where the fracture closes and the dominant pressure drop transitions from leak-off-controlled to reservoir-controlled
- **After-closure analysis** — pseudo-radial-flow analysis of the long-time decline extracts reservoir pressure and permeability

The Barree et al. SPE 167165 and SPE 124292 papers establish the pressure-derivative-based interpretation framework that is now industry-standard. The Mayerhofer-Economides SPE OnePetro corpus extends the after-closure-analysis methodology.

## Closure pressure

Closure pressure is the pressure at which a fluid-filled fracture would close in the absence of proppant. It equals the in-situ minimum-horizontal-stress (σ_hmin) in most formations, modified by any tensile-strength contribution from the rock around the fracture tip. Closure pressure controls:

- **Fracture initiation pressure during the frac job** — initiation requires exceeding closure pressure plus the rock tensile strength plus the perforation friction, so closure-pressure miscalibration shifts the operator's expected initiation pressure
- **Propped-pack stress during production** — the proppant must withstand closure stress without crushing; closure-pressure miscalibration changes the proppant-selection envelope
- **Net-pressure interpretation during the frac job** — net pressure (treating pressure minus closure pressure) drives frac propagation; the operator's real-time decision-making during the frac depends on accurate closure-pressure baseline
- **Refrac candidate evaluation** — depletion shifts closure pressure, and a refrac DFIT often shows a closure pressure 500-2,000 psi different from the original-completion value, signalling that the present-day stress state differs from the design baseline (see [Refrac](refrac.md))

Closure pressure is identified on the pressure-decline transient as the inflection point where the pressure-vs-square-root-of-time slope changes from leak-off-dominated to reservoir-dominated. In some formations the closure event is sharp and the closure pressure can be read to within ±50 psi; in others the closure event is gradual and the closure-pressure estimate carries hundreds of psi uncertainty. The G-function derivative is the most reliable diagnostic plot for distinguishing the closure event from competing pressure-decline mechanisms.

## ISIP — Instantaneous Shut-In Pressure

ISIP is the pressure at the instant pumping stops. It is recorded as the first pressure data point of the shut-in transient (corrected for any wellbore-friction artefact in the instant before shut-in). ISIP exceeds closure pressure by an amount equal to the net pressure at the end of pumping plus a friction-pressure recovery term; ISIP minus closure pressure is therefore a measure of the net pressure the operator was running during the injection.

ISIP is used as:

- **An upper bound on closure pressure** — closure pressure cannot exceed ISIP, so ISIP narrows the search range for the closure-pressure inflection on the pressure-decline transient
- **A field check on perforation-friction estimates** — if the difference between treating pressure (just before shut-in) and ISIP exceeds the expected perforation-friction value, the operator has a quality-control flag that perforation friction or near-wellbore tortuosity is higher than expected
- **A diagnostic of multiple-fracture geometry** — in some completions ISIP shows a complex multi-step decay rather than a clean single-fracture response, signalling that multiple fractures or fracture branches are active

## Leak-off coefficient

The leak-off coefficient (typically denoted C_L) is the fluid loss per unit fracture-face area per unit square-root of time. Its dimensional form is ft/√min in field units. Leak-off coefficient controls the pad-volume sizing during the main frac job:

- **High leak-off** (large C_L) → the fluid leaks off into the formation faster than the fracture can grow, so a large pad volume is required to maintain the fracture geometry against the leak-off
- **Low leak-off** (small C_L) → the fluid is contained in the fracture and the fracture grows efficiently, so the pad volume can be smaller
- **Pressure-dependent leak-off** — in fissured or naturally-fractured formations, leak-off can rise sharply once the net pressure exceeds a threshold that opens secondary fissures; the G-function derivative diagnoses this behaviour
- **Tip extension after shut-in** — in some formations the fracture continues to grow after pumping stops, which appears as a characteristic concave-down G-function derivative; this signals that the planned frac geometry must account for post-shut-in tip extension

The Nolte G-function framework provides the analytical machinery to convert the pressure-decline transient into a leak-off-coefficient estimate. The Barree pressure-derivative methodology is the dominant practitioner-facing implementation.

## After-closure analysis — reservoir pressure and permeability

When the DFIT shut-in is held long enough for the formation to enter pseudo-radial flow after fracture closure, the long-time pressure-decline transient yields a reservoir-pressure and effective-permeability estimate via standard pressure-transient analysis. In high-permeability formations the pseudo-radial-flow window opens within hours of closure; in tight shale formations it may take days or weeks.

After-closure analysis is particularly important for refrac candidate selection because:

- **Present-day reservoir pressure** directly indicates how much pressure depletion the original stimulated rock volume has experienced; this constrains the remaining-recoverable estimate that drives the refrac-vs-new-well economic decision
- **Present-day effective permeability** characterises the post-original-stimulation in-situ flow capacity; a refrac that targets a region where the post-original-frac permeability is already high produces less uplift than a refrac that targets a region with low effective permeability

The Mayerhofer-Economides framework is the canonical after-closure-analysis methodology for low-permeability formations.

## Common pitfalls and lessons learned

The industry literature on DFIT interpretation catalogues several recurring pitfalls:

- **Premature shut-in interpretation** — declaring the closure event from the early shut-in data before the pressure-decline transient has actually closed; the G-function derivative is the safeguard
- **Confusing wellbore-storage effects with formation response** — early-time shut-in pressure is dominated by wellbore-fluid expansion and tubular-storage compressibility; a true formation-leak-off signal only emerges after the wellbore-storage period
- **Misidentifying multi-stage pressure decay as single closure** — fissured formations or formations with multiple fracture branches show multi-step pressure decay; treating this as single closure misestimates closure pressure
- **Insufficient shut-in duration** — after-closure-analysis requires the test to be held long enough for pseudo-radial flow to develop; truncating the shut-in prematurely sacrifices the reservoir-pressure and permeability measurements
- **Treating-pressure artefact at shut-in** — the very last data point before shut-in can be corrupted by friction-pressure recovery artefacts; ISIP should be extracted from the corrected pressure transient, not from the raw rate-decay artefact

## Decision framework — when to run a DFIT

A simplified operator decision tree:

1. **For every refrac candidate** — DFIT is mandatory. The present-day in-situ stress state cannot be inferred from original-completion data, and the candidate-selection economics depend on present-day reservoir-pressure and permeability values.
2. **For every new-well first frac in a play with limited regional data** — DFIT reduces frac-design uncertainty enough to justify the cost on a single-well basis.
3. **For pad-development infill wells in well-characterised plays** — DFIT may be selective; one DFIT per pad on the first well, with the remaining wells designed against the characterised values, is a common workflow.
4. **For frac-trial or new-completion-design wells** — DFIT is part of the experimental-design protocol; the comparison of pre-trial-design to post-trial-actual frac response is what makes the trial interpretable.

## Cross-domain interactions

- **Hydraulic fracturing** — DFIT measurements are direct inputs to frac design (pad volume, slurry-stage ramp, treating-pressure budget). See [Hydraulic Fracturing](hydraulic-fracturing.md), [Frac Design](frac-design.md).
- **Refrac** — DFIT is the mandatory diagnostic for refrac candidate selection. See [Refrac](refrac.md).
- **Reservoir engineering** — DFIT after-closure analysis yields reservoir-pressure and permeability estimates that feed reservoir-engineering models.
- **Casing-program coupling** — DFIT pressure transient validates the wellbore-integrity status of the casing and cement-sheath, which informs the recompletion-architecture choice for refrac candidates. See [Casing Program Design](../../../drilling-engineering/wiki/concepts/casing-program-design.md).

## Cross-references

- [Refrac](refrac.md) — refrac candidate selection workflow
- [Hydraulic Fracturing](hydraulic-fracturing.md) — frac-mechanics framework
- [Frac Design](frac-design.md) — pad-volume sizing and pump-schedule architecture
- [Production History Decline Analysis](production-history-decline-analysis.md) — companion candidate-selection methodology
- [API RP 39](../standards/api-rp-39.md) — frac-fluid viscosity testing methodology

## Public references

- **Economides, M. J. & Nolte, K. G. (eds.)** — *Reservoir Stimulation*, 3rd Edition (SPE Monograph 17), Wiley 2000, ISBN 978-0-471-49192-7. The canonical industry reference; DFIT methodology chapter is practitioner-standard.
- **Barree, R. D., Barree, V. L. & Craig, D. P.** — SPE 107877 (2007), "Holistic Fracture Diagnostics: Consistent Interpretation of Prefrac Injection Tests Using Multiple Analysis Methods," and the broader Barree SPE OnePetro DFIT-methodology corpus (including SPE 167165 and SPE 124292) that established the pressure-derivative-based DFIT interpretation framework now in industry use.
- **Nolte, K. G.** — foundational SPE papers on the G-function framework and the before-closure / after-closure pressure-decline analysis methodology that underpins all modern DFIT interpretation.
- **Mayerhofer, M. J. & Economides, M. J.** — SPE OnePetro corpus on after-closure-analysis methodology for low-permeability formations, particularly for unconventional-play DFIT interpretation.
- **Lyons, W. C. (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, Elsevier (ISBN 978-0-7506-7785-1). Pre-frac diagnostics chapter.
- **SPE OnePetro DFIT literature** — extensive corpus on field-case DFIT interpretations across major unconventional plays, including documentation of formations where standard interpretation methods fail and alternative interpretation frameworks must be applied.
