---
title: "Asphaltene Precipitation"
tags: [asphaltene, sara, onset-pressure, de-boer-plot, hirschberg, dispersant, aromatic-solvent, deposition]
added: 2026-05-16
last_updated: 2026-05-16
---

# Asphaltene Precipitation

## Scope

Asphaltene precipitation is the destabilisation and aggregation of high-molecular-weight, polar, polyaromatic crude-oil components into a solid phase that can deposit on tubular and surface-equipment walls, on artificial-lift internals, and at near-wellbore-rock pore throats. Unlike wax deposition (which is temperature-driven), asphaltene destabilisation is principally **pressure-driven** — the asphaltene phase is most stable at high pressure and tends to destabilise as the produced fluid is drawn down through the saturation pressure region. Asphaltene-prone crudes can present chronic deposition problems through tubing, surface equipment, and downhole completion components.

This page covers asphaltene characterisation (SARA framework), onset-pressure prediction, the inhibition family taxonomy (cite-by-class), monitoring practice, and remediation (aromatic-solvent treatment, mechanical removal).

## What asphaltenes are

Asphaltenes are operationally defined by their solubility behaviour: the asphaltene fraction of a crude is the portion that is insoluble in light n-paraffins (n-pentane or n-heptane are standard precipitating solvents) but soluble in aromatic solvents (toluene, xylene). The definition is a chemistry-by-solubility classification rather than a single chemical-structure definition.

Structurally, asphaltenes are large polyaromatic molecules with attached alkyl side chains and heteroatom (nitrogen, oxygen, sulphur) functional groups. Their molecular weight, aromatic core size, and degree of association are subjects of ongoing research; for the production-engineering audience the operationally-relevant characterisation is the SARA framework.

## SARA characterisation

The SARA framework separates crude oil into four solubility classes:

- **Saturates** — n-paraffins, iso-paraffins, naphthenes; the non-polar non-aromatic fraction
- **Aromatics** — single- and multi-ring aromatic hydrocarbons; non-polar but aromatic
- **Resins** — polar, partly aromatic molecules that have stabilising interactions with asphaltenes; their presence in the crude affects asphaltene stability
- **Asphaltenes** — the heavy polar polyaromatic fraction defined above

The asphaltene stability of a crude is partly determined by the ratio of resins to asphaltenes. Crudes with high resin-to-asphaltene ratios tend to be asphaltene-stable; crudes with low ratios are more prone to destabilisation. The asphaltene stability index (ASI) and related indices express this in summary form.

SARA analysis is a routine PVT-laboratory exercise on representative crude samples. The results feed asphaltene-stability screening and inhibition-program design.

## Onset-pressure prediction

The pressure at which asphaltene precipitation first occurs during pressure depletion is the **asphaltene onset pressure**. Above this pressure asphaltenes remain in solution; below this pressure asphaltene aggregates begin to form, ultimately depositing on walls if the destabilisation is sustained.

Onset-pressure prediction is approached through a combination of experimental measurement and thermodynamic modelling:

- **Direct laboratory measurement** — live-fluid samples are depressurised under controlled conditions in a high-pressure visual cell or near-infrared (NIR) light-scattering cell; the pressure at which scattering first appears is the measured onset.
- **De Boer plot** — an empirical screening framework introduced by de Boer et al, plotting bubble-point pressure against in-situ asphaltene content, that identifies a "severe asphaltene problem" zone where most asphaltene-problem field cases fall. Useful as a first-cut screening tool.
- **Asphaltene stability index (ASI)** and related indices — computed from SARA composition, used as a stability screen
- **Thermodynamic models** — equation-of-state-based approaches (modified Hirschberg framework, PC-SAFT with asphaltene parameters, and similar) used to predict onset pressure across the operating envelope. Consult the simulator documentation for the model implementation.

The onset-pressure envelope is one of the inputs to flow-assurance modelling of an asphaltene-prone field; the operating-pressure trajectory through the production system can then be examined for points where it crosses the onset boundary.

## Deposition behaviour

Once asphaltenes destabilise they tend to:

1. Aggregate into colloidal-scale particles
2. Continue to grow into larger aggregates as further destabilisation proceeds
3. Deposit on surfaces (tubular walls, pump internals, surface equipment) by a combination of adhesion and gravitational settling in low-velocity zones
4. Mature into a denser deposit over time as aged asphaltene deposits cure

Deposition is more severe in zones of high pressure-gradient (near-wellbore rock pore-throats, choke restrictions, ESP intakes) and in zones of mechanical disturbance (mixers, pump impellers). Asphaltene damage to near-wellbore rock can produce a productivity-impact analogous to the drilling-fluid-invasion damage that matrix acid is the standard remediation for.

## Inhibition — chemistry families (cite-by-class)

Asphaltene inhibition divides into stabilisers and dispersants:

### Asphaltene stabilisers

Stabiliser chemistries are surfactant-based molecules that adsorb at the asphaltene-aggregate surface and prevent further aggregation. Common chemistry classes include alkyl-aryl-sulphonate surfactants, alkyl-phenol-resin polymers, and amide-based surfactants. Stabilisers act at the onset of destabilisation; injection upstream of the destabilisation zone is the typical deployment strategy.

### Asphaltene dispersants

Dispersants are functionally similar to stabilisers but optimised for breaking up existing aggregates rather than preventing aggregation. The chemistry classes overlap with stabilisers; the operational distinction is in the deployment timing and dosing strategy.

### Mutual-solvent washes

For wells where chemical inhibition is not maintaining acceptable deposition rates, periodic mutual-solvent washes can dissolve asphaltene deposits in the tubing and near-wellbore region. Mutual solvents (ethylene glycol monobutyl ether and similar) have the property of being soluble in both aqueous and hydrocarbon phases and can carry surfactant chemistry into oil-wet deposits where pure-water treatments would not reach.

### Selection workflow

Inhibitor selection follows the standard production-chemistry workflow — laboratory screening of candidate chemistries against representative crude samples, field trial with full-scale injection, ongoing surveillance and adjustment. Vendor laboratory screening data and field performance curves are typically proprietary; this wiki does not reproduce performance curves, dosage tables, or product-specific lab-screening data.

## Monitoring

Asphaltene-deposition surveillance combines instrumentation with operational-performance signals:

- **Tubing-pressure trend** — gradual rise in tubing pressure at constant rate signals build-up; the rate of pressure rise is a rough proxy for deposition rate. (Same signal as wax deposition; distinguishing the two requires correlation with operating-pressure trajectory and sampled deposit composition.)
- **ESP head-degradation trend** — for ESP-lifted wells, asphaltene fouling of pump internals produces a characteristic head-degradation pattern; sustained acceleration of the head-degradation rate is an asphaltene-or-scale signal.
- **Choke-pressure-drop trend** — increasing pressure drop across a fixed-position choke at constant flow is a choke-fouling signal that can be asphaltene-driven.
- **Sample collection during interventions** — wax-and-asphaltene deposit samples recovered during workovers or tubing pulls allow composition analysis (SARA-style) to confirm whether the dominant deposit phase is asphaltene, wax, or scale; this directly informs the appropriate inhibition and remediation response.
- **NIR or visual onset-pressure monitoring** — high-end instrumentation (where deployed) can directly observe the destabilisation envelope shifting with reservoir-pressure depletion.
- **Pressure-test interpretation** — increases in well-test-derived skin can indicate near-wellbore asphaltene damage; matrix-acid screening (see [Matrix Acid Stimulation](matrix-acid-stimulation.md)) covers asphaltene damage as one diagnosable damage mechanism.

Surveillance program intensity tracks the asphaltene severity of the crude and the operational consequences of unmitigated deposition (low for benign crudes, intensive for chronic-asphaltene wells where untreated deposition would cause unacceptable production loss).

## Remediation

When inhibition is insufficient and deposition has accumulated:

- **Aromatic-solvent treatment** — xylene or toluene batch treatment circulated through the affected zone dissolves asphaltene deposits. The deepest-penetrating solvent treatment uses coiled-tubing conveyance for downhole deposits. Aromatic solvents carry handling, environmental, and safety constraints that operators must address per facility-specific procedure.
- **Mutual-solvent flushes** — for less-severe build-up or for areas where pure-aromatic treatment is impractical, mutual-solvent + dispersant blends carry asphaltene-removing chemistry into the deposit.
- **Mechanical removal** — for severe build-up in tubing, mechanical-milling or tubing-pulling interventions remove the deposit physically.
- **Matrix-acid coupling** — when near-wellbore asphaltene damage is suspected, the matrix-acid program can be supplemented with asphaltene-dispersant or aromatic-solvent preflush to address the asphaltene component of the damage before the acid attacks the inorganic component. See [Matrix Acid Stimulation](matrix-acid-stimulation.md).

## Cross-references

- [Flow Assurance](flow-assurance.md) — integrated thermal-hydraulic-chemical envelope
- [Multiphase Flow in Wells](multiphase-flow-in-wells.md) — multiphase-flow context
- [Paraffin Deposition](paraffin-deposition.md), [Mineral Scale](mineral-scale.md), [Hydrate Management](hydrate-management.md) — sister deposition mechanisms
- [Matrix Acid Stimulation](matrix-acid-stimulation.md) — asphaltene damage handling in matrix-acid programs
- [Electric Submersible Pumps](electric-submersible-pumps.md), [Gas Lift Overview](gas-lift-overview.md) — artificial-lift performance affected by asphaltene deposition

## Public references

- **Hammami, A. & Ratulowski, J. (eds.)** — *Asphaltenes, Heavy Oils, and Petroleomics*, Springer 2007, ISBN 978-0-387-31734-2. Comprehensive reference covering asphaltene chemistry, characterisation, thermodynamics, and field-application context.
- **Kelland, M. A.** — *Production Chemicals for the Oil and Gas Industry*, 2nd ed., CRC Press 2014, ISBN 978-1-4398-7280-3. Asphaltene-inhibitor chemistry chapter.
- **de Boer, R. B., Leerlooyer, K., Eigner, M. R. P. & van Bergen, A. R. D.** — "Screening of Crude Oils for Asphalt Precipitation: Theory, Practice, and the Selection of Inhibitors," SPE 24987, 1995. Foundational onset-pressure-screening paper introducing the de Boer plot.
- **Hirschberg, A., deJong, L. N. J., Schipper, B. A. & Meijer, J. G.** — "Influence of Temperature and Pressure on Asphaltene Flocculation," *SPE Journal* 24(3), 1984. Foundational thermodynamic-modelling paper for asphaltene flocculation.
- **Bai, Y. & Bai, Q.** — *Subsea Engineering Handbook*, Elsevier 2010, ISBN 978-1-85617-689-7. Subsea asphaltene-deposition application context.
- **Lyons, W. C. (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, Elsevier (ISBN 978-0-7506-7785-1). Asphaltene-management chapter.
- **SPE OnePetro asphaltene literature** — extensive corpus on onset-pressure measurement, thermodynamic modelling, inhibitor screening, and field-case experience.
