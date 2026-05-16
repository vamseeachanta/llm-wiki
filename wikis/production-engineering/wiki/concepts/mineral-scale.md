---
title: "Mineral Scale"
tags: [scale, calcium-carbonate, barite, sulphate-scale, halite, iron-sulphide, iron-carbonate, oddo-tomson, saturation-index, threshold-inhibitor]
added: 2026-05-16
last_updated: 2026-05-16
---

# Mineral Scale

## Scope

Mineral scale is the precipitation of inorganic salts from produced water onto tubular and equipment surfaces. Unlike paraffin and asphaltene deposition (organic phases), scale is **inorganic crystalline** and originates in the produced-water chemistry that mixes formation water, injection water, and condensate. Scale-deposition severity tracks the operating envelope (pressure, temperature, pH) and the composition of the mixed water stream, with scale-supersaturation indices providing the screening framework that operators consume for inhibition-program design.

This page covers the dominant scale-family taxonomy (calcium carbonate, sulphate scales, halite, iron sulphide / iron carbonate), the Oddo-Tomson and related saturation-index frameworks, the inhibitor chemistry families (cite-by-class), monitoring practice, and remediation (acid treatment, scale-dissolver squeezes, mechanical removal).

## Scale-family taxonomy

The dominant inorganic scales in production-engineering practice:

### Calcium carbonate (CaCO3 — calcite, aragonite)

Calcium carbonate is the most-common scale across conventional oil-and-gas production. It precipitates when calcium-rich water encounters conditions of elevated pH, elevated temperature, or reduced CO2 partial pressure — all of which decrease the calcium-carbonate solubility. The pressure-drop across a wellhead choke is a classic CaCO3-scaling trigger because the pressure drop drives CO2 out of solution and shifts the carbonate equilibrium.

CaCO3 is relatively soluble in acid — the same HCl chemistry that addresses near-wellbore carbonate-formation damage (see [Matrix Acid Stimulation](matrix-acid-stimulation.md)) addresses CaCO3 scale. This makes CaCO3 the most operationally-tractable of the scale families.

### Sulphate scales (BaSO4 barite, SrSO4 celestite, CaSO4 gypsum / anhydrite)

Sulphate scales precipitate when sulphate-rich water (seawater is the dominant source — seawater is high in sulphate) mixes with formation water that is rich in barium, strontium, or calcium. Barium-sulphate and strontium-sulphate scales are particularly challenging because they have very low solubility in conventional acids (HCl will not dissolve them), they precipitate as hard adherent layers, and they often co-precipitate with naturally-occurring radioactive material (NORM) which adds an environmental-and-occupational-safety dimension to the remediation problem.

Sulphate scaling is the dominant flow-assurance scale problem in waterflood operations where seawater is the injection-water source — the North Sea and similar offshore waterflood developments have driven much of the operator-side sulphate-scale management literature.

### Halite (NaCl)

Halite precipitation occurs in produced systems where water salinity is very high (e.g. gas-condensate wells producing high-salinity formation water) and where water-content changes (evaporation, cooling, mixing) push the system past halite saturation. Halite scaling is less common across conventional production but appears in HPHT gas-condensate fields and in some heavy-oil thermal operations.

Halite is highly soluble in fresh water — fresh-water washes are the standard remediation when halite scaling is identified.

### Iron sulphide (FeS) and iron carbonate (FeCO3) "corrosion-coupled" scales

These scales originate in **corrosion reactions** rather than purely in the produced-water chemistry. H2S corrosion of carbon-steel tubulars produces iron sulphide (mackinawite, troilite, pyrrhotite, pyrite depending on conditions) at the corrosion interface; CO2 sweet corrosion produces iron carbonate (siderite). Both scales are deposition products of the corrosion reaction; their formation rate is therefore a corrosion-rate diagnostic.

Iron sulphide is also a microbiologically-influenced-corrosion (MIC) signature — sulphate-reducing bacteria produce sulphide ion which then reacts with available iron. Iron-sulphide deposit composition and morphology can be informative about the corrosion regime that produced it.

### Less-common scales

- **Calcium fluoride (CaF2)** — can precipitate in sandstone-acidizing operations where HF acid encounters calcium-rich pore fluid; this is a sandstone-acidizing failure mode rather than a routine scale problem. See [Sandstone Acidizing](sandstone-acidizing.md).
- **Silica (SiO2) scales** — appear in geothermal operations and some HPHT applications; less common in conventional oil-and-gas.
- **Mixed scales** — many field-recovered scale samples are not pure single-mineral but mixtures (CaCO3 + BaSO4 + FeS, for example); composition analysis of recovered scale samples is part of standard surveillance.

## Saturation-index prediction

The Oddo-Tomson framework is the practitioner-standard saturation-index prediction for production-water scale potential. The framework computes a saturation index (SI) for each scale family as the logarithmic ratio of the current ion-activity product to the equilibrium solubility product:

- SI < 0 — undersaturated; scale will not precipitate
- SI = 0 — saturation; equilibrium
- SI > 0 — supersaturated; scale precipitation is thermodynamically favoured

Calculated SI values for the operating pressure-temperature trajectory through the producing system identify the depth and operating-condition zones where scaling is most likely. Industry-standard simulator implementations consume the framework as the scaling-prediction layer; practitioners should consult the simulator documentation for the specific equation set and the parameter-calibration data requirements.

Related saturation-index frameworks include the Stiff-Davis index (used historically for CaCO3 scaling prediction) and the Langelier saturation index (originating in water-treatment-industry practice, used for CaCO3 prediction in some operator applications). Each has known applicability envelopes and known limitations; consult the specific framework's calibration scope when applying.

## Mixed-water scaling

For waterflood operations and for wells producing mixed water streams, scaling prediction depends on the mixing fractions of the constituent water streams. Two practitioner approaches:

- **Sensitivity calculation** — Oddo-Tomson SI computed at a range of mixing fractions, identifying the mixing range where SI > 0 for any scale family
- **Brine-compatibility laboratory testing** — controlled mixing of representative water samples under operating temperature and pressure, with direct observation of precipitation onset (per NACE / AMPP TM0374 brine-compatibility test methodology)

The mixing range identified as scaling-prone is typically the operating window where waterflood breakthrough is expected; scale-inhibitor programs are designed around this prediction.

## Inhibition — chemistry families (cite-by-class)

Scale inhibition relies on **threshold inhibitors** — chemistries that prevent or retard scale-crystal nucleation and growth at concentrations well below the stoichiometric amount that would be required to chemically titrate the scaling ions. Threshold inhibitors work by adsorbing onto incipient scale crystals and disrupting growth at the crystal-face level.

### Phosphonate inhibitors

Phosphonate chemistries are the dominant calcium-carbonate and sulphate-scale inhibitor family. Common chemistry classes include amino-tris-methylene-phosphonate, hydroxy-ethylidene-diphosphonate, and diethylenetriaminepenta-(methylene-phosphonate) (DTPMP). Phosphonates have good thermal stability and broad compatibility across produced-water compositions; their main operational constraint is hard-water-compatibility (calcium-phosphonate precipitates can form in certain operating envelopes).

### Polymer / polyacrylate inhibitors

Polyacrylate-based and related polymer chemistries provide complementary inhibition action. Specific classes include polyacrylic-acid, polymaleic-acid, and acrylic-maleic copolymers. Polymer inhibitors are typically preferred for high-temperature and high-pH applications where phosphonate compatibility is degraded.

### Polyphosphate inhibitors

Polyphosphate chemistries (sodium hexametaphosphate and related) are used in some applications, particularly for CaCO3 scale at moderate temperature; they degrade at higher temperature and are less common in HPHT applications.

### Combination inhibitors

Many commercial inhibitors are blends of phosphonate, polymer, and biocide chemistries tuned to a specific application envelope. Production-chemistry vendors (Champion-X, Nalco Champion / Ecolab, Halliburton MultiChem, Baker Hughes) market inhibitors within each chemistry family; proprietary formulations and lab-screening performance data are not reproduced in this wiki.

### Inhibitor placement

Two principal placement strategies:

- **Continuous injection** — inhibitor injected at surface or downhole into the produced fluid stream; the standard approach for many surface and topsides scale-control applications
- **Scale-inhibitor squeeze** — inhibitor injected into the near-wellbore formation during a workover and allowed to soak; the inhibitor then bleeds back into produced fluid over weeks to months. The squeeze approach is the standard for downhole scaling problems where continuous injection at the right downhole location is impractical

The placement strategy is selected based on scaling location, well architecture, and operational logistics.

## Monitoring

Scale-deposition surveillance combines instrumentation, sampling, and operational-performance signals:

- **Tubing-pressure trend** — gradual rise in tubing pressure at constant rate is a deposition signal that can be scale-driven (alongside wax / asphaltene possibilities; sample analysis distinguishes).
- **Choke-pressure-drop trend** — scaling at the wellhead choke produces increasing pressure drop at constant flow.
- **ESP head-degradation trend** — scale fouling of ESP internals produces head-degradation; pump-pull tear-down sample composition confirms the deposit family.
- **Water analysis** — periodic analysis of produced water for scaling-ion content (calcium, barium, strontium, sulphate, carbonate, iron, sulphide) feeds the SI calculation and the inhibitor-program adjustment.
- **Inhibitor-residual monitoring** — continuous-injection programs are monitored by sampling produced water for inhibitor residual (against an established minimum-inhibitory-concentration target); squeeze programs are monitored by tracking inhibitor residual to identify when the squeeze has been exhausted and re-squeeze is needed.
- **Coupon and probe measurements** — direct mass-deposit measurement on test coupons exposed to the produced-fluid stream provides quantitative deposition-rate data. NACE / AMPP SP0775 covers coupon-program methodology.
- **Sample-jar recovery during interventions** — physical samples of recovered scale from interventions (workovers, tubing pulls) are analysed by X-ray diffraction (XRD) or X-ray fluorescence (XRF) to identify scale family and composition.

## Remediation

Once scale has deposited beyond inhibition-program management:

- **Acid treatment for CaCO3 scale** — HCl-based treatment dissolves CaCO3 scale, often combined with iron-control additives to handle iron carbonate and dissolved iron from tubing surfaces. The treatment overlaps operationally with carbonate matrix-acid (see [Matrix Acid Stimulation](matrix-acid-stimulation.md), [Carbonate Acidizing](carbonate-acidizing.md)).
- **Scale-dissolver squeezes for sulphate scale** — chelating-agent-based dissolvers (typically EDTA, DTPA, or related amino-poly-carboxylate chemistries) can dissolve barium-sulphate and strontium-sulphate at field-acceptable rates over a soak period. Sulphate-scale dissolution is intrinsically slow because of the very low equilibrium solubility; dissolver squeezes typically require multi-day soak intervals.
- **Fresh-water washes for halite** — circulation of fresh water dissolves halite quickly; the standard remediation.
- **Mechanical removal** — for hard adherent scale (BaSO4, FeS where well-adhered), tubing-conveyed milling tools can mechanically remove the deposit; this is typical for sulphate scale in severe scenarios.
- **Coiled-tubing intervention** — CT-conveyed solvent-and-acid treatments for downhole scale where rig-conveyed intervention is uneconomic.

Selection of remediation method depends on scale family, deposit location, deposit volume, and the cost-benefit of intervention vs continued operation.

## Cross-references

- [Flow Assurance](flow-assurance.md) — integrated thermal-hydraulic-chemical envelope
- [Multiphase Flow in Wells](multiphase-flow-in-wells.md) — multiphase-flow context
- [Paraffin Deposition](paraffin-deposition.md), [Asphaltene Precipitation](asphaltene-precipitation.md), [Hydrate Management](hydrate-management.md) — sister deposition mechanisms
- [Matrix Acid Stimulation](matrix-acid-stimulation.md), [Carbonate Acidizing](carbonate-acidizing.md) — CaCO3 scale removal overlap with matrix-acid programs
- [Sandstone Acidizing](sandstone-acidizing.md) — CaF2 precipitation as a sandstone-acidizing failure mode
- [Electric Submersible Pumps](electric-submersible-pumps.md) — ESP performance affected by scale fouling

## Public references

- **Oddo, J. E. & Tomson, M. B.** — "Why Scale Forms in the Oil Field and Methods to Predict It," *SPE Production & Facilities* 9(1), 1994. Foundational saturation-index paper.
- **Kelland, M. A.** — *Production Chemicals for the Oil and Gas Industry*, 2nd ed., CRC Press 2014, ISBN 978-1-4398-7280-3. Comprehensive scale-inhibitor chemistry chapter.
- **Frenier, W. W. & Ziauddin, M.** — *Formation, Removal, and Inhibition of Inorganic Scale in the Oilfield Environment*, Society of Petroleum Engineers, 2008. Industry reference for scale chemistry, prediction, and remediation across the deposition families.
- **Bai, Y. & Bai, Q.** — *Subsea Engineering Handbook*, Elsevier 2010, ISBN 978-1-85617-689-7. Subsea scale-management application context.
- **NACE / AMPP TM0374** — brine-compatibility testing methodology for produced-water scaling prediction.
- **NACE / AMPP SP0775** — corrosion-coupon program methodology applicable to scale-coupon work.
- **Lyons, W. C. (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, Elsevier (ISBN 978-0-7506-7785-1). Scale-management chapter.
- **SPE OnePetro scale literature** — extensive corpus on saturation-index prediction, threshold-inhibitor screening, squeeze-program design, and field-case experience.
