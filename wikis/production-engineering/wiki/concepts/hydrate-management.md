---
title: "Hydrate Management"
tags: [natural-gas-hydrate, clathrate, vdw-platteeuw, thi, mehg, methanol, ldhi, kinetic-hydrate-inhibitor, anti-agglomerant, depressurisation]
added: 2026-05-16
last_updated: 2026-05-16
---

# Hydrate Management

## Scope

Natural-gas hydrates are crystalline ice-like solids in which water molecules form cage-like clathrate structures that enclose individual gas molecules. Under conditions of low temperature and high pressure, in the presence of free water, hydrocarbon gases (methane, ethane, propane, isobutane, plus CO2 and H2S as supporting hydrate-formers) crystallise into hydrate that can plug tubing, flowlines, risers, and topsides piping. Hydrate-plug formation is among the most-severe flow-assurance pathologies — a fully-formed hydrate plug can completely stop production in minutes, and removing a hydrate plug is operationally hazardous and time-consuming.

This page covers the hydrate-stability framework (van der Waals-Platteeuw thermodynamic basis), the operating-envelope mapping, the prevention strategies (THI thermodynamic inhibition, LDHI kinetic + anti-agglomerant inhibition), and the remediation toolkit (depressurisation, hot-fluid circulation, methanol treatment) plus monitoring practice.

## Hydrate structures and thermodynamics

Natural-gas hydrates form three principal crystalline structures depending on the size distribution of the guest gas molecules:

- **Structure I (sI)** — primarily methane and ethane hydrates; the simpler clathrate structure with small and medium cages.
- **Structure II (sII)** — natural-gas hydrates with propane and isobutane as supporting hydrate-formers; the larger cages of sII can host the larger hydrocarbon molecules that do not fit in sI cages.
- **Structure H (sH)** — requires both small and large guest molecules; appears in some hydrocarbon systems with branched-isomer content.

For typical natural-gas production systems sII is the dominant operating structure (the presence of propane and isobutane in most natural gases drives sII formation). Structure determination is informative for thermodynamic modelling but the operational consequences (plug formation, plugging severity) are broadly similar across the structures.

The thermodynamic stability of hydrate is described by the **van der Waals-Platteeuw (1959) statistical-thermodynamic framework**, which computes the chemical-potential balance between the hydrate phase, the liquid water phase, and the hydrocarbon gas phase. The framework produces the hydrate stability boundary — the temperature-pressure-composition envelope inside which hydrate is the thermodynamically-stable phase.

Practical hydrate-stability prediction uses public academic codes (CSMHYD from the Colorado School of Mines hydrate group is widely cited) and commercial PVT / process simulators that consume the van der Waals-Platteeuw lineage as their physics layer. Practitioners should consult the simulator documentation for the calculation methodology and the gas-composition input data requirements.

## Hydrate-formation envelope

For a given gas composition the hydrate stability boundary is a curve in pressure-temperature space — at any given pressure there is a hydrate-equilibrium temperature above which hydrate does not form and below which it does. Typical natural-gas hydrate equilibrium temperatures for production-engineering operating pressures fall in a range that overlaps with subsea ambient temperatures, with deep-water tieback temperatures, and with topsides ambient temperatures in winter operating conditions. Hydrate formation is therefore a routine flow-assurance concern across most field-development configurations involving gas in cool environments.

Free water is **required** for hydrate formation; bone-dry gas streams do not form hydrate. The water content target for dehydration of gas-export systems is set to keep the gas inside the no-hydrate-formation envelope across the full operating temperature range.

For subsea tiebacks the dominant hydrate-formation events are:

- **Cooldown during shutdown** — the tieback fluid loses heat to the seabed environment after a shutdown; once temperature falls below the hydrate-formation temperature at the prevailing pressure, hydrate can form if free water is present
- **Cold restart** — restarting cold fluid into a tieback brings cold fluid into contact with hydrate-prone conditions before the fluid temperature recovers
- **Choke or restriction pressure-drop cooling** — Joule-Thomson cooling across a restriction (wellhead choke, manifold valve) can cool the gas into the hydrate-formation envelope at high pressure even when the upstream temperature is well above the equilibrium hydrate temperature
- **Low-rate operation** — at low rate, the tieback fluid resides longer in the cool section and approaches the seabed temperature more closely; the operating-rate floor for some tiebacks is set above the hydrate-limited minimum

## Prevention — chemistry families (cite-by-class)

Hydrate-prevention chemistries divide into two functional categories:

### Thermodynamic hydrate inhibitors (THI)

THIs are chemicals that shift the hydrate-stability boundary to lower temperature at a given pressure, allowing the operating system to stay above the (now-shifted) hydrate-formation temperature without modifying its operating conditions. The dominant THIs:

- **Methanol** — historically the most-widely-used THI. Effective across the operating-temperature range, established handling and safety protocols, mature operator experience. The principal operational drawback is recovery: methanol must be present in significant proportion to provide sufficient hydrate-stability shift, and the downstream methanol-recovery system (typically a distillation column at the host facility) is an operating-cost burden.
- **Monoethylene glycol (MEG)** — an alternative to methanol that has become standard in many modern subsea developments. MEG is recoverable in a closed-loop dehydration system at the host facility and recycled back through the subsea injection line, reducing the operating-cost burden of make-up chemistry. MEG injection rates are typically high (multiple percent of the produced-water rate) to provide adequate hydrate-stability shift.
- **Diethylene glycol (DEG) and triethylene glycol (TEG)** — used in some applications; DEG offers different recovery and handling characteristics than MEG.

The required THI injection rate depends on operating conditions and gas composition; consult a flow-assurance simulator and gas-composition-aware thermodynamic prediction for the design calculation. THIs are typically the only viable approach when significant amounts of free water cannot be excluded and a substantial hydrate-stability shift is required.

### Low-dosage hydrate inhibitors (LDHI)

LDHIs work at much lower concentration than THIs by acting kinetically rather than thermodynamically. They do not shift the hydrate-stability boundary; rather they interfere with hydrate-crystal nucleation, growth, or aggregation at concentrations well below the stoichiometric requirement of a THI. Two LDHI families:

- **Kinetic hydrate inhibitors (KHIs)** — polymer chemistries that adsorb at incipient hydrate-crystal surfaces and slow further crystal growth. Common chemistry classes include vinyl-pyrrolidone-based polymers (poly-vinyl-pyrrolidone PVP, poly-vinyl-caprolactam PVCap, and related vinyl-lactam-copolymer chemistries) and other polymer families with the structural feature of an amide-or-lactam ring on the polymer backbone. KHIs provide a "delay window" during which hydrate formation is suppressed; they are most effective in operating systems where the residence time in the hydrate-formation envelope is short enough for the delay to keep formation from happening (e.g. flow operations where the fluid passes through the hydrate envelope quickly; less effective in shut-in situations with extended residence in the envelope).
- **Anti-agglomerants (AAs)** — surfactant chemistries that allow hydrate crystals to form but prevent them from agglomerating into transportable plugs. Common chemistry classes include quaternary-ammonium-salt surfactants and related cationic-surfactant chemistries. AAs require free water to function (the AA partitions at the water-hydrocarbon interface); their applicability envelope is bounded by the maximum-water-cut where the AA-mediated dispersion can be sustained.

LDHIs offer substantial operating-cost reductions relative to THIs because their injection rates are much lower; their adoption has grown substantially in modern subsea developments where the lifecycle cost of THI injection is a significant constraint. The applicability envelope and limitations of each LDHI family must be assessed against the specific field operating conditions.

### Dehydration

For gas-export systems and for systems where water can be excluded entirely, **dehydration** of the gas stream below the water-content threshold corresponding to no-hydrate-formation across the operating temperature envelope is the principal alternative to chemical inhibition. Dehydration is typically achieved by glycol contactor systems (TEG dehydration as the dominant production-facility technology) or molecular-sieve dehydration. The dehydration design target is gas-water-content set well below the saturation water content at the lowest operating temperature in the downstream system.

For gas-lift operations where injection-gas dehydration is marginal, residual water in the injection gas can drive hydrate formation in the gas-lift valves and in the tubing above the gas-lift mandrel. See [Gas Lift Overview](gas-lift-overview.md) for the gas-lift-coupling context.

## Operational design

A well-designed hydrate-management program addresses both steady-state operation and transient events:

- **Steady-state operation** — operating system designed to stay outside the hydrate-formation envelope under nominal conditions, with continuous low-rate THI or LDHI injection as required
- **Cooldown management** — for systems where cooldown after shutdown crosses the hydrate envelope, options include scheduled depressurisation to take the system below hydrate-formation pressure before cooling has time to drop the temperature into the envelope, or continuous warming via electrical-heat-tracing or hot-fluid circulation
- **Restart management** — restart procedures define the warm-fluid displacement sequence and the chemical-injection strategy to clear the cold tieback before flowing live gas-water through it
- **No-flow shutdowns** — extended no-flow periods require explicit hydrate-risk management; the procedure may include methanol displacement of vulnerable segments, gas-blanket placement, or planned depressurisation
- **Inhibitor injection-system design** — injection points, injection rate envelope, recovery infrastructure (for MEG systems), make-up infrastructure (for methanol), and surveillance instrumentation are designed at the field-development stage

Industry-standard flow-assurance simulators model the full transient operating cycle (steady-state, shutdown cooldown, restart) with hydrate-formation prediction integrated into the transient calculation.

## Monitoring

Hydrate-management surveillance focuses on:

- **Inhibitor-residual measurement** — methanol or MEG residual in produced water is sampled to confirm adequate inhibition; LDHI residual measurement is challenging at the low concentrations these inhibitors operate at, and inferential methods (downstream pressure-drop trending) are often used instead
- **Pressure-and-temperature surveillance** — operating-pressure and operating-temperature trends compared against the hydrate-stability boundary identify when the operating point is approaching the envelope
- **Pressure-drop trending across choke and restriction points** — sudden pressure-drop increase across a wellhead choke or subsea manifold restriction can signal incipient hydrate formation before a fully-formed plug develops
- **Downhole and tieback temperature monitoring** — DTS or PDG temperature data identify when temperature is approaching the hydrate boundary
- **Shutdown-cooldown surveillance** — the temperature trajectory during shutdown is monitored against the hydrate-formation timeline; the operator may pre-position remediation chemistry or initiate planned depressurisation if the trajectory indicates impending hydrate formation

## Remediation — once a plug forms

Hydrate-plug remediation is operationally serious because the plug can be at high differential pressure (with one side at operating pressure and the other side depressurised); rapid plug ejection from high differential pressure can produce projectile hazards. Standard procedures:

- **Single-sided depressurisation** — reducing pressure on one side of the plug at controlled rate. Plug dissociation occurs as the pressure drops below the hydrate equilibrium pressure at the prevailing temperature. The slow-and-controlled approach minimises projectile risk.
- **Two-sided depressurisation** — equalising pressure on both sides of the plug, then depressurising both sides simultaneously. Eliminates projectile risk but requires access to both sides of the plug.
- **Methanol or MEG injection** — chemical injection at the plug interface accelerates dissociation by shifting the local hydrate-stability boundary
- **Hot-fluid circulation** — circulating warm hydrocarbon or water through the system warms the plug above its equilibrium temperature; effective for accessible plugs
- **Plug location identification** — pressure-pulse testing, acoustic-monitoring, or temperature-monitoring techniques can localise the plug to inform the remediation approach

Hydrate-plug remediation procedures are typically documented in field-specific procedures and follow operator safety-management-system practice for high-energy intervention work.

## Cross-references

- [Flow Assurance](flow-assurance.md) — integrated thermal-hydraulic-chemical envelope
- [Multiphase Flow in Wells](multiphase-flow-in-wells.md), [Horizontal and Inclined Flow](horizontal-inclined-flow.md) — multiphase-flow and cooldown context
- [Paraffin Deposition](paraffin-deposition.md), [Asphaltene Precipitation](asphaltene-precipitation.md), [Mineral Scale](mineral-scale.md) — sister deposition mechanisms
- [Gas Lift Overview](gas-lift-overview.md) — injection-gas dehydration and gas-lift hydrate risk

## Public references

- **Sloan, E. D. & Koh, C. A.** — *Clathrate Hydrates of Natural Gases*, 3rd ed., CRC Press / Taylor & Francis 2007, ISBN 978-0-8493-9078-4. The canonical hydrate-thermodynamics reference covering stability, structures, kinetics, and the LDHI literature.
- **van der Waals, J. H. & Platteeuw, J. C.** — "Clathrate Solutions," *Advances in Chemical Physics* Vol. 2, 1959. The foundational statistical-thermodynamic clathrate framework.
- **Kelland, M. A.** — *Production Chemicals for the Oil and Gas Industry*, 2nd ed., CRC Press 2014, ISBN 978-1-4398-7280-3. Comprehensive LDHI chemistry chapter (KHI and AA chemistry families).
- **Bai, Y. & Bai, Q.** — *Subsea Engineering Handbook*, Elsevier 2010, ISBN 978-1-85617-689-7. Subsea hydrate-management application context.
- **Carroll, J.** — *Natural Gas Hydrates: A Guide for Engineers*, 3rd ed., Gulf Professional Publishing / Elsevier 2014, ISBN 978-0-12-800074-8. Industry reference for hydrate-formation prediction and inhibition design.
- **Lyons, W. C. (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, Elsevier (ISBN 978-0-7506-7785-1). Hydrate-management chapter.
- **SPE OnePetro hydrate literature** — extensive corpus on hydrate-formation prediction, inhibitor development and field deployment, plug-remediation case studies, and cooldown management in subsea developments.
- **CSMHYD** academic reference code (Colorado School of Mines hydrate research group) — widely-cited public academic hydrate-prediction implementation.
