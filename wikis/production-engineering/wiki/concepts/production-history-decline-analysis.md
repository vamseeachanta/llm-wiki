---
title: "Production History Decline Analysis"
tags: [decline-analysis, arps, fetkovich, type-curve, b-factor, exponential-decline, hyperbolic-decline, harmonic-decline, refrac, candidate-selection, remaining-recoverable, production-forecasting]
added: 2026-05-16
last_updated: 2026-05-16
---

# Production History Decline Analysis

## Scope

Production history decline analysis is the family of empirical and semi-analytical methods that extract remaining-recoverable estimates and diagnostic insights from a well's measured production-rate-vs-time history. The dominant framework — Arps' three-form decline-curve model (exponential, hyperbolic, harmonic) augmented by Fetkovich's type-curve matching — converts a noisy field measurement (monthly oil rate, gas rate, or water-cut) into a forward-looking remaining-reserves estimate and a present-day characterisation of the flow regime the well is operating in.

Decline analysis serves three primary use-cases:

1. **Reserves booking and forecasting** — the dominant volumetric basis for proved-developed-producing reserves under SEC and equivalent international frameworks
2. **Operating-decision support** — identifying wells whose production trajectory deviates from expected, signalling damage, equipment failure, or reservoir-management opportunities
3. **Refrac candidate selection** — discriminating wells whose decline pattern indicates conductivity loss (refrac-treatable) from wells whose decline pattern indicates rock-volume depletion (refrac will produce minimal uplift)

This page covers the foundational Arps framework, the Fetkovich type-curve extension, the b-factor diagnostic, and the refrac-candidate-selection application. The decline-analysis methodology is broader than refrac use, but the refrac connection is the load-bearing application this page anchors for the Phase 3 stimulation cluster.

## The Arps framework — three decline forms

J. J. Arps' 1945 Trans. AIME paper established the empirical framework that still dominates decline analysis. Arps observed that production-decline behaviour across a wide range of wells could be fit by one of three mathematical forms, distinguished by a single shape parameter b:

### Exponential decline (b = 0)

Rate falls at a constant fractional rate per unit time:

q(t) = q_i × exp(-D_i × t)

where q_i is the initial rate, D_i is the initial decline rate (fraction per time), and t is time. The cumulative production is bounded by q_i / D_i; the well produces a finite ultimate volume.

Exponential decline is the boundary-dominated-flow behaviour for a single-phase fluid in a closed reservoir at constant flowing-bottomhole-pressure. It is the simplest and most pessimistic of the three forms in terms of the implied ultimate recovery. Conventional moderate-permeability oil wells often decline approximately exponentially after the early transient-flow period ends.

### Hyperbolic decline (0 < b < 1)

Rate falls at a fractional rate that itself declines with time:

q(t) = q_i / (1 + b × D_i × t)^(1/b)

The cumulative production is still bounded, but by a larger volume than the exponential case at the same q_i and D_i. Hyperbolic decline is the boundary-dominated-flow behaviour for a multi-phase fluid (oil + gas + water with changing relative permeabilities) and for compressible-fluid flow where the in-situ compressibility changes as pressure depletes. Most conventional oil wells decline hyperbolically with b typically in the range 0.2-0.6.

### Harmonic decline (b = 1)

Rate falls slowly and the cumulative production is unbounded in the analytical limit:

q(t) = q_i / (1 + D_i × t)

The unbounded cumulative is an artefact of the mathematics; physical wells always produce a finite volume. Harmonic decline is the boundary-dominated-flow behaviour for some gravity-drainage gas-cap-expansion mechanisms and for water-drive reservoirs with very weak depletion. In practice, harmonic decline is rare for the entire production history but common as a curve-fit over short time windows in wells that are approaching abandonment-pressure limits.

## The b-factor diagnostic

The b-factor (the shape parameter that distinguishes the three Arps forms) is more than a curve-fitting convenience — it carries diagnostic information about the flow regime the well is operating in. The b-factor diagnostic spectrum:

| b-factor range | Typical interpretation | Implication for refrac |
|---|---|---|
| **b = 0** (exponential) | Boundary-dominated single-phase flow in a closed system; rock-volume depletion dominates | Refrac uplift will be limited; the well has produced most of its accessible rock volume |
| **0 < b < 0.5** | Boundary-dominated multi-phase or compressible-flow behaviour in a conventional reservoir | Refrac uplift modest; rock-volume depletion is significant but not complete |
| **0.5 < b < 1** | Hyperbolic decline with significant residual flow capacity; can indicate conductivity-loss-dominated decline | Refrac uplift can be substantial if the decline is conductivity-loss-driven; DFIT and core-and-log diagnostics distinguish conductivity-loss from depletion |
| **b > 1** ("super-hyperbolic") | Transient-flow behaviour in tight or naturally-fractured rock; observed routinely in early shale-well decline | Refrac uplift can be very large; the well has not yet reached boundary-dominated flow and substantial rock volume remains accessible |

The b > 1 range is the diagnostic that motivates much of the modern refrac field-experience. Shale wells routinely show b-factors of 1.2-2.5 over their early production history, signalling that the well is still in transient flow and that significant un-contacted rock remains. A refrac that contacts new rock in such a well can produce a step-change in IP rate and a new declining curve from the refrac date forward.

Caveat: b > 1 produces unbounded ultimate recovery in the analytical Arps framework, which is non-physical. Industry practice imposes a **b-factor switch** — fit b > 1 hyperbolic decline during the transient-flow period, then switch to a capped b ≤ 1 (often a terminal exponential decline) once boundary-dominated flow is judged to have started. The switch point and the terminal-decline rate are themselves engineering judgments calibrated to offset-well data and to physical limits.

## Fetkovich type-curve matching

M. J. Fetkovich's 1980 JPT paper extended Arps in two directions: (1) explicit treatment of the transient-flow period that Arps had treated only implicitly, and (2) a type-curve framework that allows the engineer to match a measured production history to a family of dimensionless solutions parameterised by reservoir and well properties.

Fetkovich type-curves cover both the transient-flow period (where the well drains an expanding region of investigation around the wellbore) and the boundary-dominated-flow period (where the well drains a fixed region defined by drainage-area boundaries). The transition between the two is the **end-of-transient** inflection that the Fetkovich framework characterises directly.

Type-curve matching delivers:

- **Reservoir permeability** — from the position of the matched type-curve on the dimensionless-time axis
- **Drainage radius and effective reservoir size** — from the position of the matched type-curve on the dimensionless-rate axis
- **End-of-transient time** — directly readable from the matched type-curve
- **Forecast** — the remainder of the matched type-curve becomes the forward-projection

Fetkovich type-curves are particularly useful for refrac candidate selection because they discriminate cleanly between wells still in transient flow (refrac candidates with high uplift potential) and wells in boundary-dominated flow (limited uplift potential).

## Modern extensions — power-law and stretched-exponential decline

Modern unconventional-play production-history analysis frequently uses decline-curve extensions beyond pure Arps, motivated by the observation that ultra-low-permeability shale wells decline in patterns that do not fit the classic three Arps forms cleanly. Two extensions in widespread industry use:

- **Duong's power-law decline** (Duong 2011, SPE 137748) — designed specifically for transient linear-flow behaviour in fractured tight wells; uses a t^(-m) rate decay rather than the Arps hyperbolic form
- **Stretched-exponential decline** (Valkó 2009, SPE 119369) — uses a stretched-exponential time-decay function; well-suited to the early-time-to-boundary-dominated-flow transition in some unconventional plays

The choice among Arps, Duong, stretched-exponential, and other extensions is a curve-fitting decision driven by the residual structure of the fit and by the operator's preferred conservatism on terminal-decline assumptions. The b-factor diagnostic interpretation transfers approximately to the modern extensions but the specific numerical thresholds differ.

## Refrac candidate-selection workflow

Production-history decline analysis enters refrac candidate selection through a structured workflow:

### Step 1: Fit the historical production curve

Fit Arps (or a modern extension where appropriate) to the measured monthly production rate. Extract the implied b-factor, the initial decline rate D_i, and the implied end-of-transient time (if a Fetkovich type-curve match has been done).

### Step 2: Classify the decline regime

- **High b (b > 1)** with steep transient decline → refrac candidate with high uplift potential (transient flow, un-contacted rock remains)
- **Moderate b (0.5 < b < 1)** with intermediate decline → potential candidate; supplementary diagnostics (DFIT, core-and-log, offset-well behaviour) needed to distinguish conductivity-loss decline from rock-depletion decline
- **Low b (b < 0.5)** with exponential or near-exponential decline → poor candidate; the well is in boundary-dominated flow against a small drainage volume
- **b = 0** exponential decline well past the end-of-transient → not a refrac candidate

### Step 3: Compare to offset-well decline

A candidate well declining steeper than its offset-well cohort of the same vintage and completion design is more likely to benefit from refrac than a candidate declining in line with the cohort. The offset-well comparison adds context that single-well decline-analysis cannot provide.

### Step 4: Cross-check against DFIT

DFIT closure-pressure and after-closure-analysis results (see [Diagnostic Fracture Injection Test](diagnostic-fracture-injection-test.md)) provide an independent measurement of present-day reservoir pressure and stress state. A refrac candidate whose decline-analysis says "transient flow, refrac-treatable" should also show DFIT after-closure-analysis results consistent with substantial remaining pressure and substantial remaining rock volume. Inconsistency between the two diagnostics is a red flag that something in the candidate-selection logic is wrong.

### Step 5: Project post-refrac production

Project the post-refrac production curve using an analog-well distribution or a physics-based simulation. The refrac economic decision compares the projected post-refrac cumulative-uplift-discounted-at-cost-of-capital against the all-in refrac cost; see [Refrac](refrac.md) for the refrac-vs-new-well economic frame that consumes this projection.

## Common pitfalls

- **Fitting too short a history** — the b-factor estimate is highly unstable when the fit window is shorter than the relevant flow-regime characteristic time; a Fetkovich type-curve match or a longer-history fit is needed before the b-factor can be trusted
- **Confusing rate-restricted operation with depletion** — wells operating under a deliberate rate restriction (production-allocation cap, surface-equipment limit, gas-handling constraint) decline pathologically in ways that look like depletion but reflect surface-side throttling; production-history analysis must screen for this
- **Ignoring water-cut and GOR trends** — a well whose oil rate is declining while water cut or GOR is rising is operating under different physics than a constant-cut declining well; the b-factor diagnostic interpretation shifts accordingly
- **Treating refrac uplift as a permanent step** — refrac uplift typically declines steeply (re-fracced wells show their own initial decline) and the projected ultimate-recovery contribution of refrac is the integrated uplift over the post-refrac decline, not the IP-rate step
- **Mixing transient and boundary-dominated flow in a single Arps fit** — fitting a single hyperbolic curve to a well that has crossed the end-of-transient produces a b-factor estimate that averages the two regimes and over-projects the future; the modern practice is to fit the two regimes separately or to use a Fetkovich type-curve that handles the transition explicitly

## Decision framework — when decline analysis drives the decision

A simplified operator decision tree:

1. **For every refrac candidate evaluation** — decline analysis is the first diagnostic. The b-factor and the offset-well comparison filter the candidate list before any DFIT or wellbore-integrity work is commissioned.
2. **For SEC reserves booking** — decline analysis on proved-developed-producing wells underpins the reserves estimate; the operator's decline-analysis methodology is auditable and is reviewed by the third-party reserves auditor.
3. **For operating-decision support** — decline analysis on a per-well basis flags wells whose actual rate deviates from the projected curve; the deviation is the trigger for investigation (failure, damage, surface-throttling, or reservoir-management opportunity).
4. **For new-completion-trial evaluation** — decline analysis on the trial wells versus the offset-well cohort is the empirical evidence the operator uses to decide whether to roll the trial design to the broader development program.

## Cross-domain interactions

- **Refrac** — decline-analysis b-factor and offset-well comparison are first-cut diagnostics in refrac candidate selection. See [Refrac](refrac.md).
- **DFIT** — DFIT after-closure-analysis provides an independent reservoir-pressure measurement that cross-checks decline-analysis interpretation. See [Diagnostic Fracture Injection Test](diagnostic-fracture-injection-test.md).
- **Hydraulic fracturing** — post-frac decline-analysis on offset wells calibrates the expected post-refrac decline curve. See [Hydraulic Fracturing](hydraulic-fracturing.md), [Frac Design](frac-design.md).
- **Reservoir engineering** — decline analysis is at the production-engineering / reservoir-engineering interface; reservoir simulation provides the physics framework against which decline-analysis empiricism can be calibrated.
- **Artificial lift** — declining wells trigger artificial-lift redesign or replacement when the lift-method's operating envelope no longer matches the well's reduced flowrate. See [ESP](electric-submersible-pumps.md), [Gas Lift Overview](gas-lift-overview.md), [Plunger Lift](plunger-lift.md).

## Cross-references

- [Refrac](refrac.md) — refrac candidate selection workflow
- [Diagnostic Fracture Injection Test](diagnostic-fracture-injection-test.md) — companion candidate-selection methodology
- [Hydraulic Fracturing](hydraulic-fracturing.md) — frac-mechanics framework
- [Frac Design](frac-design.md) — design framework for new and refrac fracs
- [Electric Submersible Pumps](electric-submersible-pumps.md), [Gas Lift Overview](gas-lift-overview.md), [Plunger Lift](plunger-lift.md) — artificial-lift redesign triggers from declining-well analysis

## Public references

- **Arps, J. J.** — "Analysis of Decline Curves," Trans. AIME 160(1), 1945. The foundational decline-curve paper; exponential / hyperbolic / harmonic framework originates here and remains the practitioner-standard reference.
- **Fetkovich, M. J.** — "Decline Curve Analysis Using Type Curves," JPT 32(6), 1980. The modern decline-analysis methodology; introduces the type-curve matching framework that handles transient-vs-boundary-dominated-flow transition explicitly.
- **Duong, A. N.** — SPE 137748 (2011), "Rate-Decline Analysis for Fracture-Dominated Shale Reservoirs." Power-law decline framework for tight unconventional wells.
- **Valkó, P. P.** — SPE 119369 (2009), "Assigning Value to Stimulation in the Barnett Shale: A Simultaneous Analysis of 7000 Plus Production Histories and Well Completion Records." Stretched-exponential decline framework.
- **Economides, M. J. & Nolte, K. G. (eds.)** — *Reservoir Stimulation*, 3rd Edition (SPE Monograph 17), Wiley 2000, ISBN 978-0-471-49192-7. Decline-analysis material in the context of stimulation evaluation.
- **Lyons, W. C. (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, Elsevier (ISBN 978-0-7506-7785-1). Decline-analysis chapter.
- **SPE OnePetro decline-analysis literature** — extensive corpus on decline-curve methodology, type-curve extensions, refrac-candidate-selection applications, and field-case validation across conventional and unconventional plays.
