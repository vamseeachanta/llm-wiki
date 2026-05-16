---
title: "Matrix Acid Diversion"
tags: [matrix-acid, diversion, foam-diversion, ball-sealer, fiber-diversion, ves, mechanical-isolation, completion]
added: 2026-05-16
last_updated: 2026-05-16
---

# Matrix Acid Diversion

## Scope

Acid diversion is the operational discipline of **forcing matrix acid into the parts of the treated interval that need stimulation**, when un-diverted acid would preferentially flow into already-high-permeability zones (high-permeability streaks, already-stimulated perforation clusters, already-wormholed carbonate zones). Without diversion, the natural flow distribution in a heterogeneous interval is dominated by the high-permeability zones, and those zones receive most or all of the acid budget while low-permeability damaged zones — the actual stimulation targets — remain untreated.

Diversion is therefore not an *optional* refinement to matrix-acid design. For any treated interval over approximately 30 ft, or for any treated interval with measurable permeability heterogeneity, or for any treated interval where the operator-target uplift requires uniform stimulation across the entire perforated zone, **some form of diversion is mandatory**. The question is not *whether* to divert; the question is *which* diversion family fits the chemistry, the completion architecture, and the operational envelope.

This page covers the four dominant diversion families (chemical / particulate / fiber / mechanical), the selection logic that maps diversion family to job context, and the failure modes that diversion is intended to prevent and that poorly-executed diversion can produce. The matrix-acid overview is at [Matrix Acid Stimulation](matrix-acid-stimulation.md); diversion-specific notes for sandstone and carbonate jobs respectively are at [Sandstone Acidizing](sandstone-acidizing.md) and [Carbonate Acidizing](carbonate-acidizing.md).

## Why diversion is harder than it looks

The naive operator picture — pump acid, it goes everywhere uniformly — is wrong for two reinforcing reasons:

**Reason 1: Darcy-flow heterogeneity bias.** Even before any acid is pumped, the natural flow distribution into a heterogeneous interval at constant injection pressure is biased toward the high-permeability zones. A 10× permeability contrast produces an order-of-magnitude flow-rate contrast between zones. Pumping acid uniformly at the wellhead does not produce uniform acid placement in the formation.

**Reason 2: Stimulation feedback.** As acid enters a zone and dissolves damage minerals (sandstone) or carves wormholes (carbonate), the permeability of that zone *increases*. The already-high-flow zone gets even more flow. This positive-feedback loop means that small initial flow-distribution biases amplify rapidly during the job, and by the time the operator notices the surface-pressure-rate signature, most of the acid is already in the wrong zone.

Diversion is the operational counter-loop: introduce something that **selectively blocks** the high-permeability or already-stimulated zones, so subsequent acid is forced into the under-treated zones. The mechanisms differ across diversion families but the principle is the same.

A field rule of thumb: **the signature of inadequate diversion is a falling surface treating pressure during the job.** A well-diverted job shows a step-up in surface pressure each time diversion engages, then a slow decline as the newly-treated zone responds. A poorly-diverted job shows continuously declining pressure as the dominant-flow zone is over-stimulated and the rest of the interval is untouched.

## Family 1 — Foam diversion (chemical, viscosity-based)

**Mechanism**: Nitrogen-foamed acid (typically 60-80% N₂ quality at downhole conditions) has 10-100× higher apparent viscosity than non-foamed acid. The foamed acid preferentially enters lower-permeability or already-treated zones because the viscous flow imposes a larger pressure penalty on flowing into high-permeability paths. Once the foam is placed in the high-permeability zones, subsequent non-foamed acid is forced into other parts of the interval.

**Best for**:
- Carbonate matrix-acid jobs where wormhole-instability bias is severe
- Open-hole completions where mechanical diversion is infeasible
- Long intervals (> 50 ft) where ball-sealer count would be impractical
- Wells with no completion hardware available for staged treatment

**Operational characteristics**:
- Foam quality control during pumping requires nitrogen-pumping equipment and surfactant-foamer chemistry sized to the acid volume
- Foam half-life sets the diversion duration — typically 30 minutes to several hours; foam breaks down naturally as the surfactant degrades or as the foam contacts formation hydrocarbons
- Co-injection of foam with acid ("foamed acid") vs alternating-stage placement ("foam pill" between acid stages) — both common; alternating-stage gives sharper diversion engagement

**Failure modes**:
- Wrong surfactant chemistry → foam de-stabilises during pumping and provides no diversion
- Wrong foam quality (too dry: insufficient viscosity contrast; too wet: foam liquefies under shear) → suboptimal diversion
- Foam half-life too short for the remaining acid budget → diversion engages but breaks down before the un-treated zones are reached

## Family 2 — Ball-sealer diversion (particulate, perforation-blocking)

**Mechanism**: Small spheres ("ball sealers," typically 7/8-inch or 1-inch diameter, sometimes specialty sizes) are pumped into the wellbore during the acid job. The balls are carried by the acid stream to the perforations, where they **seat** on already-stimulated (high-flow) perforations because those perforations have the highest fluid velocity around their entrance. With high-flow perforations sealed off by balls, subsequent acid is diverted to un-sealed perforations.

Ball density is chosen so that the balls float at the surface in flowback fluid (allowing easy recovery) or sink to the bottom of the wellbore for later cleanout, depending on operator preference. Standard practice uses an over-population of balls (more balls than perforations) to ensure that every high-flow perforation is sealed.

**Best for**:
- Cased-and-perforated wells with discrete perforation clusters
- Carbonate jobs where the wormhole-capture failure mode is the dominant concern
- Sandstone jobs in unevenly-perforated multi-zone intervals
- Workover treatments where the operator wants explicit diversion control

**Operational characteristics**:
- Balls are typically dropped from the surface via a ball-drop tool integrated with the surface manifold
- The number of balls is sized to the perforation count (typically 1.5-2× perforation count to ensure full coverage)
- Ball seating is observed as a surface-pressure spike at the time each ball seats

**Failure modes**:
- Wrong ball size for the perforation diameter → balls do not seat (too small) or block too aggressively (too large)
- Ball density wrong → balls settle to the bottom of the wellbore (sinkers) or float at the top (floaters) without reaching the perforations
- Premature ball seating (balls reach perforations before all high-flow zones are wormholed) → diversion engages too early and leaves the natural-flow distribution un-treated

## Family 3 — Fiber diversion (particulate, bridging-based)

**Mechanism**: Engineered fibers (typically 3-6 mm length, polymer or specialty material, sometimes degradable) are co-pumped with the acid. The fibers **bridge** at perforation entrances or in fracture-face microstructures, creating a temporary plug that diverts subsequent acid. After the job, the fibers either flow back with produced fluids (non-degradable fibers in clean produced streams) or **dissolve or hydrolyse** away (degradable fibers — increasingly the field standard, because non-degradable fibers can persist and cause flow restrictions long after the job).

**Best for**:
- Jobs where ball-sealer count is impractical (very high perforation density) or unavailable
- Acid-frac jobs where fracture-tip diversion is the design intent
- Hybrid matrix-acid / mini-frac jobs where the fiber acts both as diversion and as proppant transport aid
- Replacing rock-flour or salt-particulate diverters (older diversion technologies) in modern field practice

**Operational characteristics**:
- Fiber concentration is typically 5-20 lb per 1,000 gallons of acid, sized to the perforation count and the target diversion duration
- Degradable fibers have a service-life-vs-temperature curve that must be matched to the job duration
- Fiber-laden acid has different rheology than plain acid — friction-loss modelling must account for the fiber loading

**Failure modes**:
- Wrong fiber length for the perforation diameter → fibers pass through (too short) or pre-plug the wellbore (too long)
- Wrong fiber concentration → inadequate diversion (too low) or wellbore-plugging during pumping (too high)
- Fiber degradation too slow → post-job flow restriction; fiber degradation too fast → diversion breaks before un-treated zones are reached

## Family 4 — Viscoelastic surfactant (VES) diversion

**Mechanism**: Viscoelastic surfactants are a class of chemistries that produce **high apparent viscosity** in salty water at low concentrations but **break back to low viscosity on contact with hydrocarbons or with shear above a threshold**. As a diversion fluid, a VES-thickened acid (or a VES pill between acid stages) preferentially enters lower-permeability zones (high apparent viscosity at low flow rate) and creates a viscous block in the high-permeability zones. When the well returns to production, formation hydrocarbons contact the VES and reduce the viscosity to near-water, allowing automatic clean-up without a separate flowback or break stage.

**Best for**:
- HPHT carbonate matrix-acid jobs where conventional diversion (foam, fiber) struggles with temperature
- Multi-zone jobs where post-job clean-up cost is a constraint
- Wells where formation hydrocarbons provide reliable VES-break contact

**Operational characteristics**:
- VES chemistry is more expensive per gallon than foamer or fiber chemistry
- Viscosity-break behaviour depends on the produced-hydrocarbon composition; gas wells may not provide reliable VES-break contact
- VES-laden acid has different rheology than plain acid; friction-loss modelling must account for VES viscosity

**Failure modes**:
- Wrong VES chemistry for the produced-hydrocarbon composition → VES does not break and remains as a flow restriction
- Excessive shear during pumping breaks the VES prematurely → no diversion
- Wrong VES concentration → insufficient viscosity contrast (too low) or pump-trip / surface-pressure overshoot (too high)

## Family 5 — Mechanical isolation (positive-engagement, stage-by-stage treatment)

**Mechanism**: Physical isolation hardware (straddle packers, ball-activated sleeves, coiled-tubing-conveyed isolation tools, frac-string isolation tools) **physically isolates** a sub-interval of the treated zone, so that all acid pumped during the isolation period enters only that sub-interval. After each stage, the isolation is shifted to the next sub-interval and the next stage of acid is pumped.

This is the gold-standard diversion family because every other family relies on chemical or fluid-mechanical effects that have failure modes; mechanical isolation has only the failure mode of "isolation hardware does not engage" — which is observable in real time.

**Best for**:
- High-value HPHT carbonate matrix-acid jobs where any other diversion failure mode is unacceptable
- Multi-zone selective-completion wells where the completion architecture already provides isolation hardware
- Acid-frac jobs in cased-hole completions where stage isolation is required regardless of diversion
- Workover treatments via coiled tubing where the isolation tool is included in the CT-conveyance package

**Operational characteristics**:
- Mechanical isolation requires sufficient wellbore size for the isolation tool
- The treatment must be designed as a sequence of stages with each stage sized for its own sub-interval
- Job duration is longer than non-isolation diversion (one stage at a time) — surface-equipment availability and operator-personnel cost are higher
- Mechanical-isolation diversion is fully observable in real time (surface pressure response to each stage is unambiguous), making it the easiest diversion family to diagnose during the job

**Failure modes**:
- Isolation hardware fails to engage (packer seats wrong, sleeve does not actuate) → entire sub-interval is treated as commingled
- Hardware damage during repeated stage shifting → mechanical-failure-driven job termination
- Sub-interval sizing wrong → stages are too long (high-permeability bias re-emerges within a sub-interval) or too short (operational cost dominates)

## Selection logic — which family fits the job

The choice of diversion family is set by the intersection of chemistry constraints, completion-architecture constraints, and operational cost-benefit. A simplified decision framework:

| Job context | Default diversion family |
|---|---|
| Cased-and-perforated carbonate matrix acid, single zone | Ball sealers (workhorse) |
| Cased-and-perforated sandstone matrix acid, single zone | Ball sealers (workhorse) |
| Open-hole carbonate matrix acid | Foam diversion |
| Open-hole sandstone matrix acid | Foam diversion |
| Long-interval (> 100 ft) any-lithology matrix acid | Mechanical isolation (CT-conveyed straddle packer) |
| HPHT carbonate matrix acid | Mechanical isolation OR VES diversion |
| Acid-frac job (above parting pressure — not strictly matrix) | Fiber diversion (in-stage) + mechanical isolation (stage-to-stage) |
| Multi-zone selective-completion well | Use the completion's existing isolation hardware (sliding sleeves, ICVs) |
| Workover treatment via CT | CT-conveyed mechanical isolation + chemical diversion as belt-and-braces |
| Cost-constrained shallow water well | Foam diversion (lowest hardware footprint) |

These are defaults — operator practice often blends two families for redundancy (foam + ball sealers in long carbonate jobs; fiber + mechanical isolation in acid-frac jobs). The cost of inadequate diversion is the entire stimulation budget mis-placed; the cost of redundant diversion is the incremental chemistry or hardware spend, which is typically a small fraction of the total job cost.

## Diversion-failure diagnostic — reading the surface-pressure trace

A real-time surface-pressure trace is the operator's primary diagnostic for diversion effectiveness during the job. Pattern recognition:

- **Continuously declining pressure throughout the job** → no effective diversion; acid is following the natural flow distribution into the dominant-permeability zone; remaining stages are likely wasted on the same zone unless mid-job diversion is triggered
- **Step-up at each diversion event followed by slow decline** → effective diversion; each step represents the moment when the diverter engages and the next sub-zone begins to be treated; this is the target pattern
- **Step-up too early in the job** → diversion engaged before the high-flow zone was adequately treated; subsequent stages may over-treat the wrong zone
- **No step-up at expected diversion event time** → diverter did not engage (wrong chemistry, wrong size, wrong placement timing); the job is effectively un-diverted from that point
- **Step-up followed by rapid pressure rise to surface-pressure limit** → diversion was too aggressive (full-wellbore plug); the job must be paused while the plug is broken

Operator real-time decision-making during the job rests on this pressure-trace pattern recognition combined with **rate-vs-pressure plot analysis** (Hall plots, McLeod plots, real-time skin calculation). The decision to halt-and-reconfigure or to push-through-as-planned is made based on the live diagnostic, not on the pre-job plan alone.

## Common operator mistakes

### 1. Selecting diversion based on chemistry cost rather than failure-mode risk

Foam and ball sealers are cheap; mechanical isolation is expensive. Operators frequently default to the cheap family without quantifying the cost of inadequate diversion (entire acid budget mis-placed = total job cost wasted). For high-value wells, the expected-loss-from-diversion-failure usually exceeds the cost of mechanical isolation by an order of magnitude or more.

### 2. Designing the diversion before designing the rate envelope

Diversion engagement depends on rate-driven pressure transients. If the rate envelope is set without considering how the diversion will engage at that rate, the diversion may not function as designed. Diversion and rate envelope must be designed together.

### 3. Not monitoring the diversion in real time

Diversion is a real-time-observable phenomenon. Operators who pump the job without active surface-pressure monitoring miss the diagnostic and discover diversion failure only after the post-job production test shows poor uplift. Real-time pressure-rate monitoring with a stimulation engineer present at the wellsite is operational discipline that pays back in observed-and-corrected diversion failures.

### 4. Re-using ball-sealer or foam designs from a different well

Ball-sealer and foam-diversion design parameters (ball size, foam quality, surfactant concentration) are tied to the perforation density, the completion architecture, and the chemistry of the acid. A design that worked on one well may fail on a nominally-similar offset well if any of these parameters differ. Each well's diversion design must be re-validated against the specific well's parameters.

### 5. Trusting non-degradable fibers in long-life producing wells

Non-degradable fibers can persist for years and cause progressive flow restriction. For any long-life producing well, **degradable fibers** matched to the well's temperature profile are mandatory. Non-degradable fibers are only acceptable in short-life or intervention wells where the produced-fiber stream will be managed as part of normal flowback.

## Cross-domain interactions

- **Sand control** — diversion design on sand-control completions (gravel pack, frac pack, screens) must account for the screen and gravel as additional flow restrictions; ball sealers may not seat on screen-protected perforations; foam viscosity may not propagate through the gravel pack. See [Sand Control](sand-control.md), [Gravel Packing](gravel-packing.md).
- **Perforating** — perforation cluster geometry directly affects ball-sealer count and seating dynamics; perforation cluster spacing affects the effectiveness of foam and fiber diversion. See [Perforating](perforating.md), [Perforation Strategy](perforation-strategy.md).
- **Multi-zone selective completions** — the selective-completion hardware (sliding sleeves, ICVs, polished-bore receptacles) provides built-in mechanical isolation that can be used in place of, or in addition to, chemical diversion. See [Multi-Zone Completions](multi-zone-completions.md), [Selective Production](selective-production.md), [Intelligent-Well Completions](intelligent-well-completions.md).
- **Acid-frac** — diversion in acid-frac jobs differs in target (fracture-tip diversion to extend etched length rather than radial-flow distribution); fiber diversion dominates this application.

## Cross-references

- [Matrix Acid Stimulation](matrix-acid-stimulation.md) — chemistry-family overview
- [Sandstone Acidizing](sandstone-acidizing.md) — sandstone-specific diversion notes
- [Carbonate Acidizing](carbonate-acidizing.md) — carbonate-specific diversion notes (especially foam and ball sealers for wormhole-instability mitigation)
- [Perforating](perforating.md), [Perforation Strategy](perforation-strategy.md) — perforation-cluster coupling
- [Sand Control](sand-control.md), [Gravel Packing](gravel-packing.md) — sand-control completion constraints
- [Multi-Zone Completions](multi-zone-completions.md), [Selective Production](selective-production.md) — built-in mechanical-isolation diversion

## Public references

- **Economides, M. J. & Nolte, K. G. (eds.)** — *Reservoir Stimulation*, 3rd Edition (SPE Monograph 17), Wiley 2000, ISBN 978-0-471-49192-7. Diversion chapter (Chapter 19 in the 3rd edition) covers ball-sealer, foam, particulate, and mechanical-isolation families.
- **Williams, B. B., Gidley, J. L. & Schechter, R. S.** — *Acidizing Fundamentals* (SPE Monograph 6), Society of Petroleum Engineers, 1979. Foundational discussion of ball-sealer and particulate diversion.
- **Schechter, R. S.** — *Oil Well Stimulation*, Prentice Hall 1992, ISBN 0-13-949786-2. Diversion-design chapter.
- **Erbstoesser, S. R.** — "Improved Ball Sealer Diversion," JPT 32(11), November 1980. Practitioner-classic ball-sealer design framework.
- **Kennedy, D. K., Kitziger, F. W. & Hall, B. E.** — "Case Study on the Effectiveness of Nitrogen Foams and Water-Zone Diverting Agents," SPE Production Engineering 7(2), May 1992. Foam-diversion field-case framework.
- **Templeton, C. C., Richardson, E. A., Karnes, G. T. & Lybarger, J. H.** — "Selfgenerating Mud Acid: A New Concept for Diverting in Sandstone Acidizing," JPT 27(10), 1975. Foundational sandstone-acid diversion paper.
- **Powell, R. J., McCabe, M. A., Slabaugh, B. F., Terracina, J. M., Yaritz, J. G. & Ferrer, D.** — "Applications of a New, Efficient Hydraulic Fracturing Fluid System," SPE 56204, 1999. VES chemistry foundation paper.
- **Crowe, C. W.** — "Evaluation of Oil Soluble Resin Mixtures as Diverting Agents for Matrix Acidizing," SPE 5860, 1976. Particulate-diverter framework predating modern fiber diversion.
- **Lyons, W. C. (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, Elsevier (ISBN 978-0-7506-7785-1). Diversion section in the acidizing chapter.
- **SPE OnePetro acid-diversion literature** — extensive corpus on foam-quality optimisation, ball-sealer seating dynamics, VES chemistry, fiber-degradation modelling.
