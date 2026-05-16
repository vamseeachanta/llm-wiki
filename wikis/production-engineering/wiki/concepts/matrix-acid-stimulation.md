---
title: "Matrix Acid Stimulation"
tags: [matrix-acid, stimulation, sandstone-acidizing, carbonate-acidizing, near-wellbore-damage, hcl, hf, mud-acid, completion]
added: 2026-05-16
last_updated: 2026-05-16
---

# Matrix Acid Stimulation

## Scope

Matrix acid stimulation is the family of well-treatment operations that injects reactive acid into the producing formation **below the parting (fracture) pressure** with the explicit goal of dissolving near-wellbore damage and restoring or enhancing the inflow capacity of the well. The discriminating constraint — *below parting pressure* — is what distinguishes matrix acid from acid fracturing: matrix-acid jobs leave the rock fabric intact and act on near-wellbore (typically inches to a few feet) damage and dissolution surfaces, whereas acid frac jobs create or extend hydraulic fractures whose conductivity is established by acid-etched fracture walls.

Matrix acid is the lowest-cost, lowest-risk stimulation intervention in the production-engineering toolkit. It is the workhorse pre-production cleanup treatment after drilling-and-completion campaigns, the routine recompletion intervention after measured productivity decline, and the targeted near-wellbore-scale-and-paraffin remediation tool throughout field life. Properly designed and executed, it carries a high probability of recovering measurable productivity at a small fraction of frac-job cost; improperly designed, it can damage the formation, destabilise the completion, and produce post-job skin worse than the pre-job state.

This page is the **router** for matrix-acid coverage in the production-engineering wiki. It synthesises the chemistry families, the lithology-driven dispatch (sandstone vs carbonate), the candidate-selection framework, the diversion problem, the operator decision logic, and the cross-domain interactions, and links out to dedicated pages for sandstone acidizing, carbonate acidizing, and matrix-acid diversion.

## Why matrix acid is the highest-leverage Phase 3 entry

Matrix acid sits at the intersection of three operating-window questions:

- **Damage diagnostics** — Well-test analysis surfaces a positive skin attributable to near-wellbore damage. Matrix acid is the first-line intervention before any frac-or-recomplete escalation is considered.
- **Completion-quality recovery** — Drilling-fluid invasion, perforation crushed-zone debris, cementing-fluid intrusion, and gravel-pack placement debris all contribute to post-completion skin that matrix acid can address. See coupling to [Perforating](perforating.md) — overbalanced perforating produces a crushed zone that post-perforation matrix acid is the standard cleanup for.
- **Operating-phase remediation** — Inorganic scale (calcium carbonate, calcium sulphate, barium sulphate), paraffin and asphaltene precipitates, water-block damage from injected fluids, and emulsion blocks are all field-life damage modes that targeted matrix-acid (with appropriate chemistry — not always HCl/HF) can remove.

Matrix acid also interacts with **artificial-lift placement** decisions made in Phase 1: an ESP intake set above a damaged perforated interval will see the damaged-IPR loading until matrix acid restores the inflow performance. See [Electric Submersible Pumps](electric-submersible-pumps.md) and [Gas Lift Overview](gas-lift-overview.md) for the IPR / artificial-lift coupling that matrix-acid jobs are designed to relieve.

The most important conceptual frame for matrix acid: it is a **damage-bypass** technique, not a *productivity-creation* technique. Stimulation beyond the original undamaged IPR is the province of hydraulic fracturing and acid fracturing. Matrix-acid treatments that target post-completion skin values of +5 to +20 can plausibly recover the entire skin penalty (skin → 0 or slightly negative for carbonate wormholes). Matrix-acid treatments that promise multi-fold rate increases on un-damaged wells are usually mis-diagnosed candidates.

## Acid chemistry families

Matrix-acid treatments are designed around four chemistry families, each with characteristic reaction kinetics, formation-mineral targets, and operational constraints:

### 1. Hydrochloric acid (HCl)

The workhorse carbonate acid. HCl reacts strongly with calcium carbonate (CaCO₃ → CaCl₂ + CO₂ + H₂O) and dolomite (CaMg(CO₃)₂ → CaCl₂ + MgCl₂ + 2 CO₂ + 2 H₂O), producing soluble chloride salts and gaseous CO₂. Typical field concentrations: 15% HCl (the "regular" concentration), 20-28% HCl for HPHT carbonate treatments, sometimes 7.5% for sandstone preflush duty.

Operational constraints: corrosivity to tubular goods (mandatory corrosion inhibitor at all field concentrations), reactivity-driven spending profile that limits live-acid penetration distance, incompatibility with HF in the absence of preflush separation, asphaltene precipitation in some crude-asphaltene-class oils.

### 2. Hydrofluoric acid (HF) — almost always as HCl/HF mud acid

The only practical acid for sandstone-matrix dissolution. HF reacts with silicates (quartz, feldspars, clays) via complex multi-stage stoichiometry to produce fluorosilicate products. HF is never used standalone in field treatments — the dominant deployment is as a **mud-acid mixture** with HCl, the most common formulation being **12-3 mud acid** (12% HCl + 3% HF), with 9-1 (9% + 1%), 6-1.5 (6% + 1.5%), and other ratios used per formation mineralogy.

Operational constraints: severe acute toxicity (skin and inhalation hazards demand extensive PPE and emergency-response readiness), **mandatory HCl preflush** before HF contact with any formation containing carbonate cements (the Schechter-Gidley-Williams 3-stage framework — see [Sandstone Acidizing](sandstone-acidizing.md) — exists precisely to manage this incompatibility), retarded reaction at low temperature, complex secondary and tertiary precipitation reactions that can damage the formation if treatment design fails to manage spent-acid composition.

### 3. Retarded and organic acids

When standard HCl spends too rapidly (at HPHT carbonate matrix temperatures, on dolomite where reaction kinetics are anomalously slow but spent-acid handling is the issue, in chrome-tubular wells where Cl-corrosion is the constraint), the operator turns to **retarded acids** — chemistry families that slow the effective acid-rock reaction rate to extend live-acid penetration distance into the formation:

- **Gelled acids** — viscous-polymer-thickened HCl that reduces convective transport to the reaction surface and extends penetration; common in HPHT carbonate matrix and acid-frac applications.
- **Emulsified acids** — HCl-in-diesel emulsions where the acid is the internal phase and the hydrocarbon is the external phase; the hydrocarbon barrier slows acid-rock contact; HPHT carbonate workhorse.
- **Organic acids** — acetic acid (CH₃COOH) and formic acid (HCOOH); intrinsically weaker than HCl with smaller dissociation constants, giving slower reaction kinetics; also compatible with chrome tubulars where HCl corrosivity is a constraint, and lower asphaltene-destabilisation risk than HCl with some crudes.
- **Chelating-agent stimulation** — EDTA, HEDTA, and GLDA chelating agents that dissolve carbonates via complex-formation rather than acid attack; useful in HPHT carbonate where strong-acid corrosion control fails and where calcium-carbonate scale must be addressed in tubulars during placement.

### 4. Specialty matrix-acid systems

For specific damage modes outside the dominant scale-and-mineral envelope:

- **Solvent-acid systems** — mutual solvents (typically ethylene glycol monobutyl ether, EGMBE) added to acid blends to handle wettability-restoration alongside dissolution, used when oil-wet near-wellbore conditions block water-based acid contact with the formation matrix.
- **Foamed acid** — acid-foam systems (typically nitrogen foam) used both for treatment-placement (the foam provides apparent viscosity for diversion — see [Matrix Acid Diversion](matrix-acid-diversion.md)) and for spent-acid recovery (foam unloads spent acid faster than column flow).
- **Acid-system additives** — iron-control agents (citric acid, erythorbic acid, EDTA) to prevent iron-hydroxide precipitation from tubular rust dissolved by live acid; clay-stabilisers to prevent fines mobilisation; anti-sludge agents for asphaltene-class crudes; surfactants for wettability and emulsion control.

## Lithology-driven dispatch — the dominant first-cut

Matrix-acid design is split at the top by formation mineralogy, and the two branches use different chemistries, different stoichiometries, different reaction-rate mathematics, and different diversion logics:

| Lithology | Dominant chemistry | Reaction physics | Detailed page |
|---|---|---|---|
| **Sandstone matrix** | HCl preflush → HCl/HF mud-acid main → HCl/ammonium-chloride postflush | Reaction-rate-limited, surface-area-dominated; Schechter-Gidley-Williams 3-stage framework | [Sandstone Acidizing](sandstone-acidizing.md) |
| **Carbonate matrix** | HCl primary, with retarded variants for HPHT and chrome-tubular constraints | Transport-rate-limited at the reaction face; wormhole-regime physics (Daccord 1987) — uniform / conical / dominant / ramified | [Carbonate Acidizing](carbonate-acidizing.md) |

This split is not merely a chemistry preference — it reflects two fundamentally different stimulation mechanisms. Sandstone acidizing **enlarges existing flow paths** by dissolving damage minerals (drilling-fluid filtercake, clay swelling products, perforation crushed-zone fines) without significantly altering the rock fabric. Carbonate acidizing **creates entirely new flow paths** in the form of wormholes — focused, high-conductivity dissolution channels that propagate radially into the rock. The design objective for sandstone is to clean up; the design objective for carbonate is to create the longest, lowest-friction wormholes the available acid volume can support.

Mineralogy edge cases that complicate the dispatch:

- **Calcite-cemented sandstones** — the cement is dissolved by HCl but the framework is silicate; preflush sizing must dissolve enough calcite to expose the silicate without leaving spent-HCl in the formation when the HF main treatment arrives.
- **Dolomitic limestones** — slower HCl-dolomite kinetics than HCl-calcite; treatment volume and contact time must be sized for the slower reaction.
- **Chlorite- and zeolite-rich sandstones** — these clays are HF-reactive but their dissolution products can re-precipitate as gels (chlorite) or zeolite secondary products that block flow paths; mud-acid concentration must be reduced (6-1.5 or 3-1.5 ratios) and treatment design must include adequate postflush displacement.
- **Glauconite and chamosite (iron-bearing clays)** — HF dissolution releases iron, which precipitates as iron hydroxide if pH rises during spending; mandatory iron-control additive.

## Candidate selection — the gate before any acid job

The most important matrix-acid design decision is made before any acid is mixed: **is this well a candidate?** Operator literature is unambiguous that the majority of matrix-acid job underperformance traces to mis-diagnosed candidates rather than design errors in correctly-diagnosed jobs.

The candidate-selection framework rests on four diagnostic questions:

1. **Is there measurable damage?** Well-test (PBU/PFO) skin > +3 to +5, productivity below offset-well or analytical-IPR expectations by > 20%, or measured rate decline beyond a natural-decline projection. If skin is zero or negative and the well is delivering close to undamaged IPR, matrix acid will not produce a meaningful uplift.
2. **What is the dominant damage mechanism?** Drilling-mud filtercake, perforation crushed-zone, fines migration, inorganic scale, organic deposition (paraffin, asphaltene), water-block, emulsion-block — each has a chemistry signature and the wrong chemistry will fail or worsen the damage. Lab analysis of recovered fluids, geochemistry of produced water, and PVT-and-asphaltene screening data feed this answer.
3. **What is the lithology?** Determines sandstone vs carbonate dispatch and the mud-acid concentration envelope. Core descriptions, mud-log lithology, and wireline log mineralogy (where available — neutron-density-PEF, ECS, or dedicated spectroscopy logs) feed this answer.
4. **What is the completion architecture?** Open-hole vs cased-and-perforated determines diversion strategy; perforation shot density and phasing constrains acid placement; sand-control completion (gravel pack, frac pack, screen) may forbid some chemistries entirely (HF can degrade some screen alloys, gravel-pack disturbance is a job-killer for sand-control wells). See [Sand Control](sand-control.md).

The diagnostic that most often gets missed in candidate selection: **water-block damage** in gas wells (entrained water from invasion fluids that has not unloaded), which masquerades as a positive skin but does not respond to acid — it responds to surfactant-and-solvent treatment. A candidate-selection workflow that does not screen for water-block in gas-well candidates will see disappointing acid-job results.

## The matrix-acid design framework

For a confirmed candidate, the matrix-acid design proceeds through five operator decisions:

### Decision 1: Chemistry family

Lithology + damage mechanism + completion constraints set the chemistry family per the dispatch above. The default-cases are well-established:

- **Carbonate matrix, normal-temperature, conventional completion** → 15% HCl, standard corrosion inhibitor
- **Carbonate matrix, HPHT or chrome tubular** → retarded acid (gelled, emulsified, organic, or chelating)
- **Sandstone matrix, normal-temperature, conventional completion** → Schechter-Gidley-Williams 3-stage (HCl preflush → 12-3 or 9-1 mud acid → HCl/NH₄Cl postflush)
- **Sandstone matrix, chlorite-rich or HPHT** → reduced-HF mud acid (6-1.5 or 3-1.5) with extended preflush
- **Scale removal in any lithology** → scale-specific chemistry (HCl for CaCO₃, EDTA/chelant for sulphates, organic acid for paraffin precursors)

### Decision 2: Volume sizing

Two volume-sizing schools are in field use:

- **Empirical (volume-per-foot)** — typical recommendations are 50-200 gal/ft of treated interval for matrix HCl in carbonates, 50-100 gal/ft of HF mud-acid main treatment in sandstones (with comparable preflush and postflush volumes). Sourced from operator experience and Williams-Gidley-Schechter foundational ranges.
- **Analytical (wormhole-propagation or damage-radius-bypass)** — for carbonates, the analytical method targets a wormhole-penetration radius (often 3-10 ft) and back-calculates the volume from acid-mineral stoichiometry and wormhole-efficiency factors (see [Carbonate Acidizing](carbonate-acidizing.md) — Buijse-Glasbergen or PVBT framework). For sandstones, the analytical method targets a damage-radius bypass distance (e.g., the measured invasion depth) and back-calculates pore-volume HF consumption from mineralogy and damage-mineral fraction.

Empirical sizing remains the field default because the input data for analytical methods (damage-mineral fraction, anisotropic permeability, wormhole-regime efficiency) is rarely well-characterised at job-design time. Analytical methods are the right answer for high-value or repeatable-asset cases (large platforms with multiple offset wells, central-plant infill drilling, HPHT carbonates where a single mis-sized job represents seven-figure economic exposure).

### Decision 3: Injection rate and pressure envelope

Matrix-acid is *defined* as below parting pressure. The injection-rate target is the **maximum rate that holds bottomhole pressure below the fracture-initiation pressure**. The fracture-initiation pressure must be known from previous step-rate tests, instantaneous shut-in tests, or analytical estimates (Eaton's gradient, regional stress maps).

Three operational guardrails:

- **Surface treating pressure budget** — surface treating pressure plus hydrostatic head plus friction losses must equal target bottomhole pressure. The friction-loss calculation requires the actual acid rheology (viscosified acids have very different friction profiles than straight HCl); incorrect friction modelling can overshoot bottomhole pressure and unintentionally fracture the formation.
- **Live-acid breakthrough monitoring** — surface-pressure-and-rate transient analysis during the job indicates when live acid breaks through the damage zone; the operator can extend or shorten subsequent stages based on the observed response.
- **Diversion break-points** — if surface pressure rises persistently during the job, the acid is preferentially entering high-permeability streaks and the operator must trigger the diversion plan (see [Matrix Acid Diversion](matrix-acid-diversion.md)).

### Decision 4: Diversion strategy

For any treatment longer than 30-50 ft of perforated interval, or for any interval with measurable heterogeneity, the acid will preferentially enter high-permeability streaks and high-conductivity perforations. Without diversion, the high-permeability zones receive most of the acid and are over-stimulated while the low-permeability damaged zones receive little acid and remain damaged. Diversion is the operational discipline of forcing acid into the un-stimulated parts of the interval.

The diversion-family catalogue is the subject of a dedicated page: see [Matrix Acid Diversion](matrix-acid-diversion.md) for the foam / ball-sealer / fiber / VES / mechanical-isolation framework.

### Decision 5: Pre- and post-treatment workflows

A matrix-acid job is bracketed by a sequence of operational steps that have outsized impact on job success:

- **Pre-treatment wellbore cleanup** — circulate clean fluid through the wellbore to remove debris that would otherwise be injected with the acid (rust from tubulars, drilling-fluid residue, formation-debris drawdown into the wellbore). Iron from tubular rust is a particular concern; iron-control additives are commonly carried in the acid even after wellbore cleanup, on the assumption that some tubular iron will be dissolved during pumping.
- **Pad / displacement-fluid design** — a pad of treatment-compatible fluid (typically ammonium-chloride brine for sandstones, low-salinity-brine or KCl for carbonates) precedes the acid to displace wellbore fluids and condition the perforations.
- **Post-treatment flowback** — spent acid must be flowed back from the formation before secondary precipitation reactions complete; for HF mud-acid this is particularly important because spent-acid pH rise can trigger fluorosilicate gel precipitation. Flowback is typically begun within hours of acid placement.
- **Post-job evaluation** — well-test or production-test data within days to weeks of the job to confirm the productivity uplift. Underperformance triggers a re-evaluation of candidate diagnosis, chemistry selection, and diversion adequacy before repeating the treatment.

## Vendor archetype framing

The matrix-acid services landscape is dominated by the three integrated majors plus independent stimulation specialists. Vendor archetypes are named at concept level only; no proprietary acid chemistry, no proprietary additive formulations, no proprietary diversion algorithms, and no field-case treatment recipes are reproduced in this wiki.

- **Halliburton acidizing services** — integrated carbonate and sandstone matrix-acid portfolio across all lithology and temperature envelopes.
- **Schlumberger acidizing services** — comparable scope; historically strong in HPHT carbonate acidizing and chelating-agent systems.
- **Baker Hughes acidizing services** — comparable scope; portfolio includes specialty sandstone-acidizing chemistries.
- **Independent stimulation specialists** — operate at scale in regions where the integrated majors do not bundle (West Texas Permian, certain inland and shallow-water assets); typically serve a defined geographic or operator niche.

Vendor proprietary algorithm details (acid-spending models, wormhole-propagation simulators, real-time diversion-trigger logic, proprietary additive chemistries) are not reproduced in this wiki — see the **Hard constraints** note in the index for the vendor-confidentiality firewall. Operators evaluating matrix-acid vendors should consult vendor data sheets and Williams-Gidley-Schechter foundational ranges as their public anchor.

## Cross-domain interactions

- **Perforating** — overbalanced perforating produces a crushed-zone debris ring around each tunnel that contributes 5-30 elevated perforation-skin units; matrix acid is the standard cleanup. Deep-penetrating perforation charges (see [Perforation Strategy](perforation-strategy.md)) optimise for acid placement, since acid must travel through perforation tunnels into the formation. The interaction is bidirectional: perforation strategy affects acid-placement quality, and the expected matrix-acid post-job cleanup informs the choice of overbalanced-vs-underbalanced perforating.
- **Sand control** — matrix-acid treatments on gravel-pack and frac-pack completions must be designed not to chemically degrade the screen alloy (some HF-class chemistries attack screen materials) and not to destabilise the gravel pack (excessive injection rate can disturb the pack and produce sand). The completion engineer and stimulation engineer must align on what chemistry and rate envelope is allowable. See [Sand Control](sand-control.md), [Gravel Packing](gravel-packing.md).
- **IPR and artificial lift** — matrix-acid restores the IPR that artificial-lift sizing was originally built on. ESP sizing, gas-lift unloading-pressure design, and plunger-lift cycling all assume an IPR shape that damage degrades and acid restores. Post-acid-job rate change can change the artificial-lift operating point enough that the lift system needs re-tuning. See [Electric Submersible Pumps](electric-submersible-pumps.md), [Gas Lift Overview](gas-lift-overview.md).
- **Well integrity** — acid attacks tubular goods (mandatory corrosion inhibitor at all concentrations), and spent-acid composition can include precipitates that scale tubulars on flowback. Material selection for acid-service tubulars (chrome-bearing alloys for HCl service, specialty alloys for HF service) couples back to drilling-engineering completion-string design decisions.
- **Reservoir characterisation** — successful matrix-acid design depends on damage diagnosis and mineralogy characterisation that draw on reservoir-engineering data (well-test interpretation, core mineralogy, geochemistry of produced water). Without this upstream data, matrix-acid design defaults to empirical sizing with elevated failure-rate risk.

## Standards anchor

Matrix-acid stimulation does **not** have a clean API recommended-practice anchor of its own. The closest standards-derived references are:

- **API RP 39** — narrowly covers frac-fluid viscosity-testing methodology; not a matrix-acid design reference (see [Hydraulic Fracturing](hydraulic-fracturing.md) — when authored; per sub-issue #85, the API RP 39 page lands with frac coverage).
- **NACE MR0175 / ISO 15156** — sour-service material requirements applicable to acid-service tubulars in CO₂ / H₂S wells (adjacent — material selection for acid-compatible completion strings).
- **SPE Monograph 17** (*Reservoir Stimulation*, 3rd ed., Economides & Nolte 2000) functions as the de-facto practitioner-canonical reference; it has no API/ISO-equivalent.

Matrix-acid practice is therefore primarily anchored to **textbook and SPE-paper consensus** rather than to a standards-published procedure. This is a structural feature of stimulation engineering — vendor methodology and operator practice evolve faster than standards-body publication cycles. The Williams-Gidley-Schechter sandstone framework and the Daccord wormhole-regime framework are the closest things to "industry-canonical" methodologies.

## Cross-references

- [Sandstone Acidizing](sandstone-acidizing.md) — Schechter-Gidley-Williams 3-stage framework, HF/HCl mud-acid chemistry, reaction kinetics
- [Carbonate Acidizing](carbonate-acidizing.md) — HCl chemistry, wormhole regimes (Daccord 1987), retarded-acid systems, emulsified acid
- [Matrix Acid Diversion](matrix-acid-diversion.md) — foam / ball-sealer / fiber / VES / mechanical-isolation diversion families
- [Perforating](perforating.md), [Perforation Strategy](perforation-strategy.md) — perforation-strategy coupling
- [Sand Control](sand-control.md) — completion-architecture constraints on matrix-acid chemistry
- [Electric Submersible Pumps](electric-submersible-pumps.md), [Gas Lift Overview](gas-lift-overview.md) — IPR / artificial-lift coupling
- Drilling-engineering: [Casing Program Design](../../../drilling-engineering/wiki/concepts/casing-program-design.md) — acid-service tubular material selection

## Public references

- **Economides, M. J. & Nolte, K. G. (eds.)** — *Reservoir Stimulation*, 3rd Edition (SPE Monograph 17), Wiley 2000, ISBN 978-0-471-49192-7. The canonical industry reference covering both matrix acid and hydraulic fracturing; matrix-acid chapters synthesise sandstone and carbonate frameworks.
- **Williams, B. B., Gidley, J. L. & Schechter, R. S.** — *Acidizing Fundamentals* (SPE Monograph 6), Society of Petroleum Engineers, 1979. The foundational sandstone-acidizing reference; the 3-stage preflush/main/postflush framework originates here.
- **Schechter, R. S.** — *Oil Well Stimulation*, Prentice Hall 1992, ISBN 0-13-949786-2. Comprehensive matrix-acid and frac textbook; widely used as a graduate-level reference and operator-training source.
- **Daccord, G.** — "Chemical Dissolution of a Porous Medium by a Reactive Fluid," *Physical Review Letters* 58(5), 1987 — the foundational carbonate-wormholing physics paper.
- **Lyons, W. C. (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, Elsevier (ISBN 978-0-7506-7785-1). Acidizing chapter.
- **SPE OnePetro matrix-acid literature** — extensive corpus on candidate selection, diversion methodology, treatment-pressure interpretation, post-job evaluation.
- **McLeod, H. O.** — "Matrix Acidizing," JPT 36(13), December 1984. Practitioner-classic field-design framework for matrix acidizing.
- **Paccaloni, G. & Tambini, M.** — "Advances in Matrix Stimulation Technology," JPT 45(3), March 1993. Real-time monitoring framework (skin-vs-volume curves) still in operator use.
