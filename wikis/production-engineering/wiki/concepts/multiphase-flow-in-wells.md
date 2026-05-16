---
title: "Multiphase Flow in Wells"
tags: [multiphase-flow, flow-regimes, holdup, pressure-gradient, correlation, mechanistic-model, brill-mukherjee]
added: 2026-05-16
last_updated: 2026-05-16
---

# Multiphase Flow in Wells

## Scope

Multiphase flow in producing wells is the simultaneous flow of two or more phases — oil + gas, gas + condensate + water, oil + gas + water — through tubing, casing annuli, flowlines, and risers. Unlike single-phase flow, the in-situ behaviour of multiphase flow is governed by interactions between phases that produce distinct **flow regimes** with their own pressure-gradient, in-situ holdup, and heat-transfer characteristics. Modelling the in-situ behaviour is the foundational hydraulic-physics layer that every flow-assurance prediction, every artificial-lift design, and every well-test interpretation depends on.

This page is the **router** for multiphase-flow coverage in the production-engineering wiki. It synthesises the regime taxonomy, the model-choice framework (mechanistic vs empirical), the historical correlation lineage, and the system-level synthesis, and links out to dedicated pages for the vertical-flow correlations, the horizontal/inclined-flow correlation family, and the flow-regime map literature.

## Why multiphase flow modelling matters

A producing well typically operates in multiphase flow across most of its life. Even single-phase oil wells in undersaturated reservoirs evolve toward two-phase flow as reservoir pressure drops below bubble point and free gas appears. Gas-condensate wells produce two phases continuously. Water breakthrough adds a third phase. Multiphase modelling enters production engineering at every scale:

- **Tubing pressure-drop calculation** — drives wellhead-pressure prediction, artificial-lift design (intake-pressure floor for ESP, operating-valve-depth gas-lift design), nodal-analysis productivity prediction.
- **In-situ holdup** — drives flow-assurance liquid-loading risk in gas wells, drives slug-volume prediction at the surface separator, drives downhole-gauge interpretation when the gauge sees a phase mixture.
- **In-situ velocity** — drives erosional-velocity calculation (see [Erosional Velocity](erosional-velocity.md)) since the V_e screen must be evaluated against the in-situ mixture velocity not against the volumetric flow rate.
- **Heat-transfer coefficient** — drives wax-deposition prediction (see [Paraffin Deposition](paraffin-deposition.md)) since the radial temperature gradient that drives molecular-diffusion wax flux depends on the multiphase heat-transfer film.
- **Free-water distribution** — drives hydrate-formation risk (see [Hydrate Management](hydrate-management.md)) since hydrate plugs nucleate at free-water interfaces.

The choice of multiphase-flow model is therefore one of the most consequential analytical decisions a production engineer makes.

## Flow-regime taxonomy

Multiphase flow regimes are catalogued primarily by the in-situ distribution of phases and the dynamic behaviour at the gas-liquid interface. The canonical taxonomy for **vertical upward flow** is:

| Regime | Description | When it occurs |
|---|---|---|
| **Bubble flow** | Discrete gas bubbles dispersed in a continuous liquid phase | Low gas rate relative to liquid; low-GOR oil wells near surface |
| **Slug flow** | Alternating large gas pockets (Taylor bubbles) and liquid slugs | Moderate gas-liquid rate ratio; the dominant regime in many oil wells across the producing tubing |
| **Churn flow** | Chaotic, oscillatory regime with periodic flooding and re-entrainment | Transition between slug and annular; unstable and difficult to model |
| **Annular flow** | Continuous gas core with a liquid film on the pipe wall and entrained droplets | High gas rate, characteristic of gas-condensate wells and high-GOR oil wells |
| **Mist flow** | Liquid almost entirely dispersed as droplets in continuous gas | Very high gas rate; the regime gas-well surveillance has to support |

For **horizontal and inclined flow** additional regimes appear because of gravity-driven phase segregation:

| Regime | Description |
|---|---|
| **Stratified smooth / stratified wavy** | Gas flows above liquid with a smooth or wavy interface; low rates only |
| **Slug flow (horizontal)** | Liquid slugs interspersed with gas pockets along the pipe |
| **Plug / elongated bubble** | Liquid-continuous flow with elongated gas pockets near the top of the pipe |
| **Annular / annular-mist (horizontal)** | Gas core with liquid film; the film is asymmetric (thicker at bottom) under gravity |
| **Dispersed bubble** | Liquid-continuous with dispersed gas bubbles, high liquid rate |

The horizontal / inclined regime catalogue is covered in detail on [Horizontal and Inclined Flow](horizontal-inclined-flow.md), and the map literature that predicts which regime occurs at given operating conditions is covered on [Flow Regime Maps](flow-regime-maps.md).

## Model-choice framework — mechanistic vs empirical

Multiphase flow models in production-engineering practice fall along a spectrum from purely empirical to purely mechanistic:

### Empirical correlations

Empirical correlations fit pressure-gradient and holdup data from laboratory and field experiments to functional forms. They are calibrated to the experimental envelope they were derived from and extrapolate poorly outside it, but they are computationally cheap and remain the working tool for many production-engineering quick-look calculations.

The dominant empirical lineage:

- **Vertical:** Hagedorn-Brown 1965, Duns-Ros 1963, Gray 1974 (wet-gas specific) — see [Vertical Flow Correlations](vertical-flow-correlations.md).
- **Horizontal / inclined:** Beggs-Brill 1973 (SPE 4007) — see [Horizontal and Inclined Flow](horizontal-inclined-flow.md).

### Mechanistic models

Mechanistic models build the pressure-gradient and holdup prediction from regime-specific momentum and mass balances, with regime selection driven by transition criteria from flow-regime-map literature. They typically extrapolate better than empirical correlations because their structure is grounded in the physics of the regime, but they require regime identification as a first step and therefore inherit the uncertainty of the regime map.

Major mechanistic frameworks include those derived from the Taitel-Dukler / Barnea regime-transition framework, Ansari et al (1990) and Petalas-Aziz (1998) for vertical and inclined flow, and the academic + commercial-simulator extensions that consume these as their physics layer.

### Industry-standard simulators

Modern flow-assurance practice consults industry-standard multiphase-flow simulators — OLGA, LedaFlow, PIPESIM, K-Spice — for steady-state and transient multiphase modelling. These simulators consume the public-literature correlation and mechanistic-model lineage as one input among many, augmented with proprietary regime-transition logic, PVT-handling layers, and numerical solvers that are not reproduced in this wiki. Practitioners should consult the simulator vendor documentation for the recommended application envelopes.

### Choosing a model

Three practitioner heuristics drive the model-choice decision:

1. **Quick-look hand calculations** → empirical correlation matched to the dominant operating regime (Hagedorn-Brown for slug-flow vertical wells, Beggs-Brill for inclined / horizontal segments).
2. **System-design and flow-assurance modelling** → industry-standard simulator with the full PVT package, transient capability, and inhibitor-injection modelling.
3. **Research and special-case analysis** → mechanistic models from the academic literature, often implemented in custom code or research-grade simulator extensions.

## Historical lineage — the public-literature correlation framework

The empirical-correlation literature for production-well multiphase flow developed through the 1960s and 1970s as field data accumulated and regression techniques became computationally tractable. The canonical sequence:

- **Poettmann-Carpenter 1952** — earliest published empirical method for vertical two-phase flow; foundational but limited applicability.
- **Duns-Ros 1963** — vertical-flow correlation with explicit regime treatment; one of the earliest models distinguishing bubble / slug / mist regimes in calculation.
- **Hagedorn-Brown 1965** — vertical-flow correlation derived from a comprehensive field-data set; broad applicability and durable as a default for vertical oil wells.
- **Orkiszewski 1967** — vertical-flow regime-by-regime correlation with explicit regime selection.
- **Beggs-Brill 1973** — the first widely-adopted horizontal / inclined / vertical correlation framework with inclination-angle correction; foundational for tubing-string segments with deviation. See SPE 4007.
- **Gray 1974** — wet-gas specific correlation widely used for gas-condensate well modelling.
- **Mukherjee-Brill 1985** — extended Beggs-Brill framework with refined inclination handling.

In parallel, the regime-mapping literature developed:

- **Mandhane et al 1974** — empirical regime map for horizontal flow.
- **Taitel-Dukler 1976** — semi-mechanistic regime-transition criteria for horizontal and near-horizontal flow.
- **Taitel-Bornea-Dukler 1980** — vertical-flow regime-transition framework.

See [Flow Regime Maps](flow-regime-maps.md) for the map framework, and [Vertical Flow Correlations](vertical-flow-correlations.md) / [Horizontal and Inclined Flow](horizontal-inclined-flow.md) for the correlation-application detail.

## System-level synthesis

Modelling a complete well system requires connecting the correlations into a coherent calculation chain:

1. **Tubing-string segmentation** — the well is divided into segments of approximately-uniform inclination, diameter, and ambient temperature. Each segment carries its own multiphase-flow calculation.
2. **PVT integration** — phase volumes (oil / gas / water) at each pressure-temperature point along the wellbore come from a PVT model (black-oil correlation or compositional EOS). The accuracy of the PVT package often dominates the accuracy of the multiphase-flow result.
3. **Heat-transfer integration** — the temperature profile is calculated alongside the pressure profile because the multiphase regime, the PVT property values, and the deposition risk all depend on temperature.
4. **Boundary-condition selection** — top-down (from a fixed wellhead pressure, calculating bottomhole pressure) vs bottom-up (from a fixed bottomhole pressure, calculating wellhead pressure). Choice depends on what is known and what is being predicted.
5. **Iterative coupling with IPR** — at the bottomhole boundary the tubing calculation must be coupled with the [inflow performance relationship](perforation-strategy.md). The operating point sits at the intersection of the tubing-performance curve and the IPR curve. This iterative coupling is the foundational "nodal analysis" framework.

## Cross-references

- [Vertical Flow Correlations](vertical-flow-correlations.md) — Hagedorn-Brown, Duns-Ros, Gray (wet-gas)
- [Horizontal and Inclined Flow](horizontal-inclined-flow.md) — Beggs-Brill correlation framework
- [Flow Regime Maps](flow-regime-maps.md) — Mandhane, Taitel-Dukler, Taitel-Bornea-Dukler
- [Flow Assurance](flow-assurance.md) — multiphase-flow is the foundational hydraulic layer
- [Erosional Velocity](erosional-velocity.md) — V_e calculation against in-situ mixture velocity
- [Paraffin Deposition](paraffin-deposition.md), [Hydrate Management](hydrate-management.md), [Asphaltene Precipitation](asphaltene-precipitation.md) — deposition mechanisms mediated by multiphase-flow regime
- [Electric Submersible Pumps](electric-submersible-pumps.md), [Gas Lift Overview](gas-lift-overview.md) — artificial-lift sizing depends on tubing-flow pressure-drop calculation
- [Perforation Strategy](perforation-strategy.md) — IPR coupling for nodal analysis

## Public references

- **Brill, J. P. & Mukherjee, H.** — *Multiphase Flow in Wells*, SPE Monograph Series Vol. 17, Society of Petroleum Engineers, 1999. The canonical industry reference for production-well multiphase flow.
- **Beggs, H. D. & Brill, J. P.** — "A Study of Two-Phase Flow in Inclined Pipes," SPE 4007 / *JPT* 25(5), May 1973. Foundational inclined/horizontal correlation paper.
- **Hagedorn, A. R. & Brown, K. E.** — "Experimental Study of Pressure Gradients Occurring During Continuous Two-Phase Flow in Small-Diameter Vertical Conduits," *JPT* 17(4), April 1965. Foundational vertical correlation paper.
- **Duns, H. & Ros, N. C. J.** — "Vertical Flow of Gas and Liquid Mixtures in Wells," *Proceedings of the 6th World Petroleum Congress*, Frankfurt, 1963. Early vertical-flow regime-aware correlation.
- **Gray, H. E.** — "Vertical Flow Correlation in Gas Wells," *API Manual of Back Pressure Testing of Gas Wells*, 1974. Wet-gas-specific correlation.
- **Taitel, Y. & Dukler, A. E.** — "A Model for Predicting Flow Regime Transitions in Horizontal and Near Horizontal Gas-Liquid Flow," *AIChE Journal* 22(1), 1976. Foundational regime-transition framework.
- **Lyons, W. C. (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, Elsevier (ISBN 978-0-7506-7785-1). Multiphase-flow chapters.
- **SPE OnePetro multiphase-flow literature** — extensive corpus on correlation derivation, mechanistic modelling, regime-map validation, and field-case applications.
