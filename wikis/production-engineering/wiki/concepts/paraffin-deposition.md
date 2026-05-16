---
title: "Paraffin Deposition"
tags: [paraffin, wax, n-alkane, wat, wax-appearance-temperature, deposition, pour-point-depressant, dispersant, hot-oiling, pigging]
added: 2026-05-16
last_updated: 2026-05-16
---

# Paraffin Deposition

## Scope

Paraffin deposition is the precipitation and accumulation of solid wax (high-molecular-weight n-alkanes and structurally-related hydrocarbons) on tubing and flowline walls when the produced fluid cools below the wax appearance temperature (WAT). It is the most-common organic-deposition flow-assurance problem in conventional oil-well production, and depending on crude composition can range from a manageable inhibition-and-pigging routine to a chronic operating constraint that drives field-development design decisions.

This page covers the wax-deposition physics, the WAT measurement methodology, the deposition-flux framework, the chemical inhibition family taxonomy (cite-by-class), the operational monitoring practice, and the remediation toolkit (hot oiling, mechanical pigging, solvent treatments).

## Wax chemistry — what precipitates

Crude oils contain a continuum of n-alkanes from very light (C1-C5 gases) through middle distillates (C10-C20 liquids) into heavy paraffins (C20-C60+) that are solid at ambient temperature but soluble in the lighter fractions at elevated temperature. The high-molecular-weight n-alkanes are the dominant wax-deposition precursors. Their solubility in the bulk oil is temperature-dependent: as the fluid cools, the heaviest alkanes lose solubility first and crystallise into the wax phase. The temperature at which the first detectable wax crystals form is the **wax appearance temperature (WAT)**.

The wax phase that ultimately deposits on a pipe wall typically also contains:

- **Naphthenes** with long alkyl chains that co-crystallise with n-alkanes
- **Asphaltenes** entrained or co-precipitated under some operating conditions (this overlaps with the asphaltene-precipitation pathology — see [Asphaltene Precipitation](asphaltene-precipitation.md))
- **Resin** fractions that can stabilise or destabilise the wax phase depending on composition
- Trapped liquid oil inside the wax matrix (deposited wax is typically a wax-oil mixture, not pure wax)

The wax phase's mechanical properties — hardness, ductility, adhesion to the tubular wall — depend on composition and aging time. Fresh-deposited wax is typically softer and more amenable to mechanical removal; aged wax can densify and require more-aggressive remediation.

## Wax appearance temperature (WAT) — measurement

WAT measurement is a laboratory PVT exercise performed on representative live or stock-tank fluid samples. Common methods:

- **Cross-polarised microscopy (CPM)** — sample is cooled in a temperature-controlled stage on a polarising microscope; the first appearance of birefringent wax crystals is recorded as WAT. CPM is the practitioner-standard reference method.
- **Differential scanning calorimetry (DSC)** — measures the enthalpy release as wax crystallises during a controlled cooling ramp; the onset of the exothermic peak is taken as WAT.
- **Viscometry** — measures the apparent viscosity during a cooling ramp; the temperature at which viscosity begins to increase non-linearly is approximately WAT (less precise than CPM or DSC; useful for screening).
- **Filter-plugging methods** — fluid is pushed through a fine-mesh filter during cooling; the temperature at which the filter begins to plug correlates with WAT.

WAT measured on stock-tank oil typically overestimates WAT measured on live oil (the dissolved-gas content of live oil depresses WAT). For flow-assurance design WAT measured on representative live-fluid samples is the appropriate reference.

## Deposition physics

The dominant deposition mechanism in producing systems is **molecular diffusion** of wax-precursor species from the bulk fluid to the cooler pipe wall, where they encounter conditions below WAT and crystallise. The deposition flux depends on:

- **Radial temperature gradient** at the wall — the steeper the gradient, the higher the diffusive driving force. Heat-transfer coefficients and ambient-temperature boundary conditions therefore directly enter the deposition prediction.
- **Bulk-fluid temperature** relative to WAT — deposition flux is highest when the bulk-fluid temperature is just above WAT (high gradient, large solubility-difference driver).
- **In-situ wax-precursor concentration** in the bulk fluid — heavier-paraffin crudes deposit more rapidly.
- **Flow regime and shear rate** at the wall — high shear can strip soft deposited wax via mechanical action (the "shear stripping" limit on net deposition); annular and slug regimes have different wall-shear behaviour.

The two competing limits on net deposition rate — diffusive deposition versus shear stripping — produce the empirical observation that wax deposition is often highest in moderate-rate operating conditions, with very low rates (cooling dominates, low shear) and very high rates (shear stripping dominates) producing benign behaviour.

Industry-standard flow-assurance simulators model wax-deposition flux as part of the integrated multiphase-flow + thermal calculation; practitioners should consult the simulator documentation for the specific deposition-flux model and the model-calibration data requirements.

## Operating-envelope framing

Wax-deposition risk enters flow-assurance design as a temperature constraint:

- **Insulation design** — for subsea tiebacks and long-flowline scope, pipe insulation (wet, dry, pipe-in-pipe, electrically-heated) is sized to keep the tieback temperature above WAT under steady-state operation
- **Operating-rate floor** — at low rate the residence time in the cool section of the system increases and wax deposition accelerates; the operating-rate floor may need to be set above the wax-limited minimum even when the artificial-lift system could deliver lower rates
- **Shutdown management** — cooldown during shutdown crosses WAT; restart procedures must address wax that has deposited during cooldown, and a sufficiently-long shutdown may require chemical or mechanical wax remediation before restart can succeed
- **Topsides cooling** — wax deposition at the topsides choke or in the production manifold is a different operational location than tubing wax deposition; both require attention.

## Inhibition — chemistry families (cite-by-class)

Wax-inhibition chemistry is organised into broad families, each with a different mechanism of action. Production-chemistry vendors (Champion-X, Halliburton MultiChem, Nalco Champion / Ecolab, Baker Hughes) market chemistries within each family. Proprietary product formulations, dosage rates, and lab-screening performance curves are not reproduced in this wiki.

### Pour-point depressants (PPDs) and wax-crystal modifiers

PPDs are polymer or oligomer chemistries that co-crystallise with the wax phase at the molecular level. They modify the wax crystal habit, producing smaller and more-dispersed crystals that have lower tendency to adhere to the wall and lower yield strength when subjected to shear. Common chemistry classes include ethylene-vinyl-acetate (EVA) copolymers, comb-type polymers with alkyl side chains, and polymethacrylate-based copolymers. PPDs typically act below WAT; they do not depress WAT itself but they reduce the depositional consequences of wax appearance.

### Dispersants and dispersant-PPD blends

Wax dispersants are surfactant-based chemistries that disperse precipitated wax crystals into the bulk-fluid suspension, preventing aggregation and adhesion to the wall. Dispersant chemistries include alkyl-amine and alkyl-amide families, and can be blended with PPDs to produce dual-action inhibitors.

### Solvent injection

For severe cases or as a remedial alternative to inhibition, aromatic-solvent or kerosene-distillate injection can dissolve wax in the bulk fluid and suppress deposition by holding the wax precursors below saturation. Solvent injection is typically more expensive than PPD inhibition and is reserved for cases where PPDs are not effective or for periodic remediation.

### Inhibitor selection workflow

The standard practitioner workflow:

1. Laboratory screening of candidate chemistries against representative crude samples (cold finger or flow loop)
2. Selection of the best-performing chemistry family per the screening matrix
3. Field trial with full-scale injection and surveillance
4. Adjustment of chemistry and operational protocol based on field performance

Vendor screening matrices and field-trial data are typically proprietary; this wiki does not reproduce performance curves, dosage tables, or product-specific lab-screening data.

## Monitoring

Wax-deposition monitoring during operation combines surveillance instruments with operational-performance signals:

- **Tubing-pressure trend** — gradual rise in tubing pressure at constant rate is the classic deposition signal; the pressure rise rate is a rough proxy for the deposition rate.
- **Flowline pressure-drop trend** — for subsea tiebacks the flowline pressure-drop tracks the wax-build-up; declining throughput at constant inlet pressure tracks the same effect.
- **Temperature trends** — declining tubing or flowline outlet temperature can indicate insulation-effective wax build-up (the wax layer acts as additional insulation).
- **Pigging-debris recovery** — wax recovered during routine pigging operations is the most-direct measurement; volume, mass, and texture of recovered wax inform the inhibition and pigging program.
- **Mass-loss coupons or polished-rod paraffin sampling** for some surface-equipment locations — direct sample collection from controlled sample points.
- **PDG and DTS instrumentation** — where installed, downhole temperature and pressure trends and distributed-temperature traces across the tubing string provide localised deposition-zone identification.

Monitoring program design typically links the surveillance frequency to the expected deposition severity (more-aggressive monitoring on chronic-wax wells, baseline-only on benign-wax wells) and to the field-development geometry (subsea tiebacks need flowline-integrity monitoring that surface wells do not).

## Remediation

Once wax has deposited beyond the acceptable build-up, remediation options:

- **Hot oiling / hot watering** — circulate heated oil or water through the tubing or flowline to melt the wax phase and carry it out of the system. Requires a heating capacity match to the wax-deposit volume; over-hot circulation can damage downhole completion equipment.
- **Mechanical pigging** — for flowlines and large-diameter tubing, run a pig that scrapes the wax off the wall. Pig design (foam, brush, scraper, intelligent pig) is selected to the wax-deposit hardness and the pipe geometry.
- **Solvent treatment** — circulate an aromatic solvent or kerosene-distillate batch through the tubing or flowline to dissolve wax; usually combined with a soak time.
- **Mechanical milling** — for severe wax build-up in tubing where pigging is not feasible, a tubing-conveyed milling tool can remove the deposit; this is typically a last-resort intervention.
- **Coiled-tubing intervention** — CT-conveyed solvent treatment or mechanical-removal tool for downhole wax remediation.

The remediation method is selected based on deposit location, deposit hardness, deposit volume, and the cost-benefit of intervention versus continuing operation with the deposit.

## Cross-references

- [Flow Assurance](flow-assurance.md) — the integrated thermal-hydraulic-chemical envelope
- [Multiphase Flow in Wells](multiphase-flow-in-wells.md), [Horizontal and Inclined Flow](horizontal-inclined-flow.md) — flow-regime sensitivity of deposition flux
- [Asphaltene Precipitation](asphaltene-precipitation.md), [Mineral Scale](mineral-scale.md), [Hydrate Management](hydrate-management.md) — sister deposition mechanisms
- [Electric Submersible Pumps](electric-submersible-pumps.md), [Gas Lift Overview](gas-lift-overview.md) — artificial-lift performance affected by wax deposition

## Public references

- **Kelland, M. A.** — *Production Chemicals for the Oil and Gas Industry*, 2nd ed., CRC Press 2014, ISBN 978-1-4398-7280-3. Comprehensive coverage of wax-inhibitor chemistry families.
- **Hammami, A. & Raines, M. A.** — "Paraffin Deposition from Crude Oils: Comparison of Laboratory Results to Field Data," SPE 38776, 1999. Foundational laboratory-to-field comparison paper.
- **Bai, Y. & Bai, Q.** — *Subsea Engineering Handbook*, Elsevier 2010, ISBN 978-1-85617-689-7. Subsea wax-deposition application context.
- **Brill, J. P. & Mukherjee, H.** — *Multiphase Flow in Wells*, SPE Monograph Series Vol. 17, SPE, 1999. Multiphase-flow context for wax-deposition modelling.
- **Lyons, W. C. (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, Elsevier (ISBN 978-0-7506-7785-1). Production-chemistry chapter.
- **SPE OnePetro wax-deposition literature** — extensive corpus on WAT measurement, deposition-flux modelling, inhibitor laboratory screening, and field-case experience.
- **NACE / AMPP corrosion-handbook chapters** on organic-deposition interaction with corrosion management.
