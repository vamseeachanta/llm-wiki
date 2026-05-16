---
title: "Flow Regime Maps"
tags: [flow-regime-map, taitel-dukler, mandhane, regime-transition, bubble-slug-annular-mist, instrumentation]
added: 2026-05-16
last_updated: 2026-05-16
---

# Flow Regime Maps

## Scope

A flow regime map is a graphical or analytical framework that predicts which multiphase flow regime occurs at a given combination of operating conditions (gas superficial velocity, liquid superficial velocity, fluid properties, pipe geometry, inclination). Regime maps sit at the foundation of mechanistic-model construction because regime identification is the first step of any regime-specific calculation; they also feed the practitioner-level interpretation of correlation predictions and the design-time selection of operating envelopes that avoid problematic regimes (slug-flow with large slugs, churn-flow with chaotic behaviour).

This page covers the dominant regime-map literature — **Mandhane** (empirical, horizontal flow), **Taitel-Dukler** (semi-mechanistic, horizontal and near-horizontal flow), and **Taitel-Bornea-Dukler** (vertical flow) — together with the operational-instrumentation framework that supports regime identification in producing wells. For the system-level multiphase-flow synthesis see [Multiphase Flow in Wells](multiphase-flow-in-wells.md).

## Why regime identification matters

Multiphase flow regimes are not all hydraulically equivalent. The pressure-drop calculation, the in-situ holdup distribution, and the heat-transfer behaviour differ by regime; many flow-assurance pathologies are regime-specific. Examples:

- **Slug-flow induced loading** — slug flow produces large transient liquid-rate excursions at the surface separator, with consequences for separator sizing and downstream-equipment dynamic loading. Severe slugging in subsea risers can produce slugs of significant pipe-volume scale that the surface facility must accommodate.
- **Liquid loading in gas wells** — once a gas well's rate falls below the lift-off threshold, the regime transitions from annular / annular-mist to churn or slug, and free liquid accumulates at the bottom of the tubing. This regime transition is the operational definition of liquid loading.
- **Annular-flow droplet entrainment** — surface-facility separator design depends on the mist-flow droplet-loading prediction at the wellhead, which is a regime-specific calculation.
- **Erosion-corrosion regime sensitivity** — mechanical erosion in elbows and bends is most severe in slug and churn regimes where periodic impact loading occurs; annular and bubble regimes typically have more benign erosion behaviour at comparable superficial velocities. See [Erosional Velocity](erosional-velocity.md).
- **Wax-deposition gradient sensitivity** — radial temperature gradient and turbulent intensity differ by regime; the molecular-diffusion wax-deposition flux depends on both. See [Paraffin Deposition](paraffin-deposition.md).

Flow regime maps therefore enter both design-time engineering (selecting operating conditions and equipment for benign regimes) and run-time surveillance (interpreting field measurements to identify the operating regime).

## Mandhane et al (1974) — empirical horizontal map

The Mandhane et al regime map is an empirical horizontal-flow regime map built from a large compilation of laboratory data. The map plots superficial gas velocity against superficial liquid velocity (logarithmic axes) and partitions the plane into regime zones (stratified, slug, plug, annular, annular-mist, dispersed-bubble). Regime selection is read directly from the position of an operating point in the map.

### Applicability and limitations

- Empirical map calibrated to air-water laboratory data; application to oil-gas systems requires either property correction or use of property-aware alternatives
- Horizontal-flow only; inclined-flow extension requires switching to Taitel-Dukler or an inclination-correction methodology
- Continues to be cited as a benchmark for horizontal-flow regime identification, often alongside Taitel-Dukler for cross-check

## Taitel-Dukler (1976) — semi-mechanistic horizontal map

The Taitel-Dukler framework derives regime-transition criteria from semi-mechanistic momentum and instability analysis rather than from purely empirical correlation. The framework produces analytical transition criteria between the dominant horizontal-flow regimes (stratified, intermittent / slug, annular, dispersed-bubble) and allows the regime-map to be regenerated for arbitrary fluid properties and pipe geometry.

### Why it became dominant

The framework's mechanistic basis makes it extrapolate better than purely empirical maps, particularly for fluid systems and pipe geometries outside the air-water laboratory envelope that the Mandhane map was calibrated to. It became the practitioner-standard horizontal-flow regime-map basis through the 1980s and remains widely cited in industry-standard simulators.

### Subsequent refinements

The Taitel-Dukler framework has been refined and extended by subsequent work, with Barnea's regime-map extensions across the inclination angle range being among the most-cited extensions. Industry-standard simulators routinely build on the Taitel-Dukler / Barnea lineage with vendor-specific transition-criterion modifications; consult the simulator documentation for the implementation specifics.

## Taitel-Bornea-Dukler (1980) — vertical flow

The 1980 Taitel-Bornea-Dukler paper extended the mechanistic regime-transition framework to vertical upward flow, producing analytical criteria for the bubble / slug / churn / annular regime transitions. The framework completes the mechanistic regime-map literature for the dominant inclination cases (vertical up, vertical down, horizontal, intermediate inclination handled via interpolation or via separate inclined-flow extensions).

### Practitioner significance

For vertical-well modelling the Taitel-Bornea-Dukler framework is the modern alternative to the regime classifications embedded in vertical-flow correlations like Duns-Ros (1963) or Orkiszewski (1967). Practitioners using mechanistic multiphase-flow models or regime-aware simulators will encounter the Taitel-Bornea-Dukler framework as the regime-identification layer.

## Regime-identification instrumentation in producing wells

Field regime identification is non-trivial because direct flow visualisation is not available in production tubing. Practitioners infer the operating regime from a combination of surface and downhole measurements:

### Surface instrumentation

- **Wellhead pressure trace** — a stable wellhead pressure with low variance suggests steady regimes (annular-mist, dispersed-bubble); a wellhead pressure trace with periodic excursions suggests slug or churn behaviour.
- **Wellhead temperature trace** — slug arrivals produce characteristic transient cooling at the surface as the cooler liquid slug arrives ahead of the warmer gas behind it.
- **Test-separator rate trace** — measured liquid and gas rates at the test separator show periodic spikes during slug arrivals; the temporal structure of the spike pattern is diagnostic of slug-flow vs steady-flow regimes.
- **Acoustic monitoring** — downhole and surface acoustic instruments can identify slug arrivals and churn-flow turbulence through their acoustic signatures.

### Downhole instrumentation

- **Permanent downhole gauges (PDGs)** — bottomhole pressure and temperature trends provide regime-diagnostic data; the gauge trace texture (smooth vs noisy, periodic vs random) reflects the local regime.
- **Production-logging tools (PLTs)** — array PLTs with spinner, density, and capacitance sensors directly identify the local phase distribution and flow regime at specific depths during conveyance runs. Multi-arm PLTs handle the horizontal-flow case where single-arm tools are degraded by stratified-regime non-uniform phase distribution.
- **Distributed temperature sensing (DTS)** — fibre-optic DTS along the tubing string identifies cooling fronts and slug-arrival events; the spatial structure of the temperature anomaly is diagnostic of the regime.

### Regime-inference from production performance

Even without specialised instrumentation, the production-engineer can infer regime from operational behaviour. Gas wells operating with stable rate and pressure are typically in annular or annular-mist; gas wells showing periodic loading-unloading cycling are in slug or churn; oil wells with stable wellhead pressure are typically in bubble or smooth-slug regimes; oil wells with persistent slugging at surface are in slug or churn.

## Integration with industry-standard simulators

Industry-standard multiphase-flow simulators (OLGA, LedaFlow, PIPESIM, K-Spice) consume the regime-map literature as the foundation for their regime-identification layer. Each simulator augments the public-literature transition criteria with proprietary tuning parameters and regime-handling logic; results can vary between simulators for cases where the operating point sits close to a regime transition. Practitioners should consult the simulator documentation for the regime-handling approach and should cross-check borderline cases against alternative simulators or against the public regime-map literature.

## Cross-references

- [Multiphase Flow in Wells](multiphase-flow-in-wells.md) — system-level synthesis of correlation and regime-map literature
- [Vertical Flow Correlations](vertical-flow-correlations.md), [Horizontal and Inclined Flow](horizontal-inclined-flow.md) — correlation lineages that consume regime identification
- [Flow Assurance](flow-assurance.md) — flow-assurance integration
- [Erosional Velocity](erosional-velocity.md) — regime sensitivity of erosion-corrosion
- [Paraffin Deposition](paraffin-deposition.md) — regime sensitivity of wax-deposition flux

## Public references

- **Mandhane, J. M., Gregory, G. A. & Aziz, K.** — "A Flow Pattern Map for Gas-Liquid Flow in Horizontal Pipes," *International Journal of Multiphase Flow* 1(4), 1974. The foundational empirical horizontal-flow regime map.
- **Taitel, Y. & Dukler, A. E.** — "A Model for Predicting Flow Regime Transitions in Horizontal and Near Horizontal Gas-Liquid Flow," *AIChE Journal* 22(1), 1976. The foundational mechanistic horizontal-flow regime-transition framework.
- **Taitel, Y., Bornea, D. & Dukler, A. E.** — "Modelling Flow Pattern Transitions for Steady Upward Gas-Liquid Flow in Vertical Tubes," *AIChE Journal* 26(3), 1980. The foundational mechanistic vertical-flow regime-transition framework.
- **Barnea, D.** — "A Unified Model for Predicting Flow Pattern Transitions for the Whole Range of Pipe Inclinations," *International Journal of Multiphase Flow* 13(1), 1987. Inclination-independent regime-transition framework.
- **Brill, J. P. & Mukherjee, H.** — *Multiphase Flow in Wells*, SPE Monograph Series Vol. 17, SPE, 1999. Synthesises the regime-map literature with practitioner application guidance.
- **Bai, Y. & Bai, Q.** — *Subsea Engineering Handbook*, Elsevier 2010, ISBN 978-1-85617-689-7. Subsea regime-map application context.
- **SPE OnePetro flow-regime literature** — extensive corpus on regime-map validation, field-case regime identification, and instrumentation strategies for regime inference.
