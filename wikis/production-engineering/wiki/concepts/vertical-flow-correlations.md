---
title: "Vertical Flow Correlations"
tags: [vertical-flow, hagedorn-brown, duns-ros, gray, correlation, holdup, pressure-gradient, wet-gas]
added: 2026-05-16
last_updated: 2026-05-16
---

# Vertical Flow Correlations

## Scope

Vertical-flow correlations are the empirical models that predict the in-situ pressure gradient and the in-situ liquid holdup of two-phase or three-phase production flow in vertical and near-vertical tubing strings. They are the working tool for hand-calculation and quick-look modelling of producing-tubing hydraulics, and they remain the physics layer that many industry-standard multiphase-flow simulators consume for vertical-segment calculation.

This page covers the three correlation lineages that dominate practitioner use for vertical wells: **Hagedorn-Brown** (broad-applicability vertical oil well default), **Duns-Ros** (regime-aware vertical-flow framework), and **Gray** (wet-gas / gas-condensate specific). For the system-level synthesis and the inclined / horizontal segment correlations see [Multiphase Flow in Wells](multiphase-flow-in-wells.md) and [Horizontal and Inclined Flow](horizontal-inclined-flow.md).

## Hagedorn-Brown (1965)

The Hagedorn-Brown correlation is the durable vertical-flow default for production-engineering practice. It was derived from an extensive set of field measurements covering vertical tubing strings of varied diameter, fluid composition, and operating rate, regressed into a holdup-and-friction-factor framework that is straightforward to apply by hand or to embed in a simulator.

### Applicability envelope

- Vertical and near-vertical (deviation typically up to about 10 degrees from vertical before the inclination effects degrade the correlation's accuracy)
- Two-phase oil-gas flow; three-phase oil-gas-water flow handled by treating the liquid phase as a mixture and correcting fluid properties accordingly
- Tubing diameters spanning typical production tubing (the original data set covered approximately 1 to 1.5 inch internal diameter; broader applicability has been demonstrated in subsequent decades of operator use)
- Pressure-gradient calculation across the slug-flow regime where most vertical oil wells operate

### Practitioner use

The correlation is the default for vertical oil wells in many nodal-analysis tools. Practitioners should consult the industry-standard simulator implementations (PIPESIM, OLGA, K-Spice, and similar) for calculation; the simulator handles the iterative coupling with PVT properties and the segment-by-segment integration along the tubing string.

### Known limitations

- Underpredicts holdup in low-rate wells where the correlation slips outside its regression-data envelope; manual cross-checks against measured tubing pressure are advised for low-rate applications.
- Limited applicability to high-GOR or wet-gas wells where Gray or simulator-resident correlations are preferred.
- Empirical structure means extrapolation outside the original regression envelope (very high temperature, very high pressure, atypical fluid compositions) carries elevated uncertainty.

## Duns-Ros (1963)

The Duns-Ros correlation was one of the first published vertical-flow models with explicit regime treatment. The framework distinguishes bubble, slug, and mist regimes and applies regime-specific calculation procedures, with regime selection driven by dimensionless-group screening.

### Applicability envelope

- Vertical and near-vertical flow with broad applicability across the bubble / slug / mist regime spectrum
- Originally derived from a controlled laboratory data set; subsequent field validation across operator use
- Particularly applied where regime identification is critical to the engineering question (e.g. distinguishing slug-flow from annular-mist behaviour in high-GOR wells)

### Practitioner use

Duns-Ros is less commonly the default selection than Hagedorn-Brown in modern practice but retains a niche in regime-sensitive applications. Industry-standard simulators include Duns-Ros among their correlation library; practitioners should consult the simulator documentation for the recommended application envelope and any modifications applied to the original 1963 formulation.

### Known limitations

- The 1963 framework predates much of the modern flow-regime-map literature; subsequent work (Taitel-Dukler, Taitel-Bornea-Dukler) has refined regime-transition prediction. Practitioners using Duns-Ros for regime identification should cross-check against the modern regime-map literature.
- Some derivative implementations modify the original transition criteria; results can vary between simulator implementations.

## Gray (1974)

The Gray correlation was developed specifically for wet-gas and gas-condensate wells where the dominant flow regime is annular or annular-mist and the liquid phase is sufficiently dispersed that oil-well-derived correlations fit poorly. It was published in the *API Manual of Back Pressure Testing of Gas Wells* and remains a workhorse for vertical gas-well modelling.

### Applicability envelope

- Vertical wet-gas and gas-condensate wells operating in annular / annular-mist regime
- High gas-liquid ratios where the liquid phase is mostly entrained in the gas core
- Use cases including gas-well backpressure analysis, gas-well deliverability prediction, and high-GOR oil-well tubing modelling at the upper end of the GOR range

### Practitioner use

Gray is widely embedded in industry-standard simulators for the wet-gas-well segment. Practitioners selecting Gray over a generic oil-well correlation should verify that the well's operating regime is genuinely annular or annular-mist; for wet-gas wells transitioning through churn or slug regimes during turn-down or kickoff, a regime-aware correlation or a mechanistic model is the appropriate selection.

### Known limitations

- Outside the wet-gas / gas-condensate envelope the correlation underpredicts holdup and can produce non-physical results for slug-dominated flow.
- Like the other empirical correlations, extrapolation outside the original applicability envelope carries elevated uncertainty.

## Selecting between the three

Practitioner heuristics for vertical-correlation selection:

- **Vertical oil well, moderate GOR, default selection** → Hagedorn-Brown
- **High-GOR well or gas-condensate well in annular regime** → Gray
- **Regime-sensitive analysis requiring explicit bubble / slug / mist treatment** → Duns-Ros (with cross-check against modern regime-map literature)
- **System-design / flow-assurance modelling** → industry-standard simulator with multiple correlations available and PVT package handling the property variation along the wellbore
- **Research or atypical fluid / condition** → mechanistic model from the academic literature

All three correlations have been studied extensively in subsequent decades of operator use and SPE-paper validation; practitioners can find published guidance for many specific basins, fluid types, and operating conditions.

## Comparing predicted holdup and pressure gradient

In practice production engineers often run multiple correlations against the same well data and bracket the result. Two heuristics from operator practice:

- For vertical oil wells in slug-flow regime, Hagedorn-Brown and Beggs-Brill (applied to the vertical limit) typically bracket the field result; an averaged prediction is often a reasonable estimate when neither correlation can be definitively recommended.
- For wet-gas wells, Gray is typically the default and Duns-Ros provides a regime-sensitive cross-check; large divergence between the two suggests the well is operating in a transition regime where modelling uncertainty is elevated.

## Cross-references

- [Multiphase Flow in Wells](multiphase-flow-in-wells.md) — system-level synthesis and model-choice framework
- [Horizontal and Inclined Flow](horizontal-inclined-flow.md) — Beggs-Brill correlation for inclined segments
- [Flow Regime Maps](flow-regime-maps.md) — modern regime-transition framework
- [Flow Assurance](flow-assurance.md) — flow-assurance integration of multiphase-flow modelling
- [Electric Submersible Pumps](electric-submersible-pumps.md), [Gas Lift Overview](gas-lift-overview.md) — artificial-lift design consumes tubing-pressure-drop predictions from these correlations

## Public references

- **Hagedorn, A. R. & Brown, K. E.** — "Experimental Study of Pressure Gradients Occurring During Continuous Two-Phase Flow in Small-Diameter Vertical Conduits," *Journal of Petroleum Technology* 17(4), April 1965. The foundational Hagedorn-Brown paper.
- **Duns, H. & Ros, N. C. J.** — "Vertical Flow of Gas and Liquid Mixtures in Wells," *Proceedings of the 6th World Petroleum Congress*, Frankfurt, 1963. The foundational Duns-Ros paper.
- **Gray, H. E.** — "Vertical Flow Correlation in Gas Wells," *API Manual of Back Pressure Testing of Gas Wells*, American Petroleum Institute, 1974. The foundational Gray wet-gas correlation.
- **Brill, J. P. & Mukherjee, H.** — *Multiphase Flow in Wells*, SPE Monograph Series Vol. 17, SPE, 1999. Synthesises the vertical-correlation lineage with practitioner application guidance.
- **Orkiszewski, J.** — "Predicting Two-Phase Pressure Drops in Vertical Pipe," *JPT* 19(6), June 1967. Companion vertical correlation with regime-specific treatment.
- **Brown, K. E.** — *The Technology of Artificial Lift Methods*, Vol 1 PennWell 1977. Practitioner reference with extensive vertical-flow correlation application examples.
- **Lyons, W. C. (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, Elsevier (ISBN 978-0-7506-7785-1). Vertical-flow correlation reference chapter.
- **SPE OnePetro vertical-flow literature** — extensive corpus on correlation validation, application envelopes, and field-case experience.
