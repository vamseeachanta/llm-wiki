---
title: "Choke Management"
tags: [choke, production-choke, well-deliverability, bean-up, esd-interlock, surface-pressure-control, production-engineering]
sources:
  - api-rp-14c
  - api-rp-14e
added: 2026-05-16
last_updated: 2026-05-16
---

# Choke Management

## Scope

Choke management is the operator-tunable control surface that matches well deliverability to downstream-facility constraints. The production choke is the variable restriction in the flow path between the producing well and the first-stage separator; by adjusting the choke opening the operator controls flowing wellhead pressure, well rate, separator inlet pressure, and (indirectly) drawdown on the reservoir. Choke management is the day-to-day operational discipline of choosing the right choke size, the right opening trajectory, and the right ESD interlocking for each well over its producing life.

This page is the **router** for choke-management coverage in the production-engineering wiki. It synthesises the operational decisions, the hardware-family overview, the multiphase-flow physics, and the safety-system context, and links out to dedicated pages for choke types, multiphase choke modelling, sand-erosion considerations, and the API RP 14C safety-system standards anchor.

## Why choke management is the well-deliverability-matching surface

The production choke sits at the intersection of three independent constraint surfaces, and operating-point selection is an exercise in balancing them:

- **Reservoir inflow performance relationship (IPR)** — the well-side curve relating bottomhole flowing pressure to rate. See [Gas Lift Overview](gas-lift-overview.md) for the IPR / artificial-lift coupling. Excessive drawdown (overly-open choke) can trigger water or gas coning, sand production, or reservoir-pressure decline issues; insufficient drawdown leaves productivity on the table.
- **Tubing performance relationship (TPR)** — the vertical-flow correlation curve relating bottomhole flowing pressure to wellhead flowing pressure as a function of rate. The choke sets the wellhead boundary condition that fixes the operating intersection of IPR and TPR.
- **Surface-facility constraint envelope** — first-stage separator operating pressure, gas-handling capacity, water-handling capacity, flare-system capacity, sales-line backpressure. The choke must hold the wellhead pressure such that the well's flow into the facility stays within all these limits simultaneously.

Choke management is the daily reconciliation of these three surfaces. The choke is the only continuously-adjustable element between IPR and the separator; everything else (perforations, completion architecture, tubing geometry, separator size) is fixed at design time.

## The five choke-management questions

Any choke-management programme answers five operator questions:

1. **Which choke architecture?** (fixed-bore / adjustable / cage / multistage) — driven by service envelope (sand-laden vs clean, single-phase vs multiphase, surface vs subsea) — see [Choke Types](choke-types.md)
2. **Which trim material?** (tungsten-carbide / ceramic / stellite-class hardfacing) — driven by erosion / corrosion service — see [Choke Sand Erosion](choke-sand-erosion.md)
3. **What is the operating-point bean size?** — driven by the IPR/TPR/facility-constraint intersection per multiphase choke modelling — see [Multiphase Choke Modeling](multiphase-choke-modeling.md)
4. **What is the bean-up / bean-down trajectory?** — driven by well-startup procedure, reservoir-management strategy, and erosion-rate management
5. **What ESD interlocking applies?** — driven by [API RP 14C](../standards/api-rp-14c.md) safety-system architecture

These five decisions are interlocked: an adjustable cage choke with tungsten-carbide trim sized for the midlife operating-point bean, beaned up gradually over a 24-hour startup window, with PSHL ESD interlocks on the discharge line is a very different installation than a fixed-bore positive choke with stellite trim sized for the early-life high-rate envelope and bypassed on facility ESD. The choke-types and modelling pages give the framework; this overview gives the system-level synthesis.

## Choke-architecture families

Production chokes fall into a small number of architecture families, categorised first by **adjustability**:

| Family | Adjustability | When chosen |
|---|---|---|
| **Fixed-bore (positive)** | Bean changed manually by workover or by replacement insert | Stable wells with well-understood flow envelope; low-cost installations; subsea-tree backup chokes |
| **Adjustable** | Stem-and-seat assembly continuously variable from surface controller | Wells requiring active rate control or frequent bean changes; modern surface-tree default |
| **Cage** | Multi-orifice cage with rotating sleeve; flow area changes in discrete steps | High-pressure-drop service requiring noise / vibration / erosion control; subsea-tree default for high-rate wells |
| **Multistage** | Multiple staged pressure-drop elements (often a primary cage followed by a secondary trim) | Severe pressure-drop service (HP gas wells, deepwater HPHT) where single-stage drop would cause cavitation, erosion, or noise problems |

Secondary axes:

- **Service environment** — surface vs subsea (subsea chokes face control-line and replacement-access constraints); sweet vs sour (NACE MR0175 / ISO 15156 metallurgy); clean vs sand-laden (drives trim material and architecture choice).
- **Pressure-drop magnitude** — single-stage drops above approximately 1500-2000 psi differential in liquid-bearing service approach cavitation limits and drive selection toward cage or multistage architectures; the exact threshold depends on fluid properties and trim geometry.
- **Actuation type** — manual hand-wheel (legacy surface installations), pneumatic actuator (common surface), hydraulic actuator (subsea trees and high-rate surface), electric actuator (increasingly common for surface and emerging in subsea all-electric architectures).

See [Choke Types](choke-types.md) for the in-depth architecture-family framework.

## Bean-up and bean-down operations

The trajectory of choke opening (bean-up) and closing (bean-down) is an operationally-managed parameter, not just an instantaneous setpoint:

### Initial well startup (kickoff bean-up)

- **Flush-flow vs reservoir-deliverability-limited** — early flow during cleanup is sand-laden, sometimes contains completion-fluid debris, and may be dominated by wellbore-storage effects rather than reservoir inflow. Bean-up must be slow enough to flush the wellbore without overloading the surface separator, the flare system, or the erosion-rate budget of the choke trim.
- **Bean-up rate budget** — typical practice is to bean up in step increments with hold periods (e.g. 12/64-inch bean for 2 hours, then 16/64-inch for 2 hours, etc.) until target rate is reached. The exact schedule depends on completion type (a long horizontal frac well has different flush-flow characteristics than a vertical natural-completion well), reservoir fluid (sand-producing, gas-producing, GOR), and surface-facility readiness.
- **Coupling with perforation strategy** — [Perforation Strategy](perforation-strategy.md) decisions interact with bean-up rate. A well perforated underbalanced (UBP) has cleaner tunnels with less crushed-zone debris and tolerates faster bean-up; a well perforated overbalanced (OBP) without acid cleanup carries more debris and requires more conservative bean-up. See the perforating page's bean-up coupling section.

### Steady-state operating-point control

- **Reservoir-management constraints** — when reservoir engineering imposes drawdown limits (water-coning avoidance, gas-coning avoidance, compaction-management, voidage-replacement) the choke is the operational handle that enforces them.
- **Production-allowable enforcement** — some regulatory regimes impose well-rate allowables (Texas Railroad Commission allowables, OPEC quota enforcement). The choke is the enforcement device.
- **Facility load-balancing** — when a multi-well facility approaches separator or flare capacity, the operator beans down on the highest-rate or highest-GOR wells to free facility capacity for other wells or for upset-tolerance margin.

### Bean-down for shut-in or workover

- **Gradual bean-down avoids transient pressure spikes** — slamming the choke closed on a flowing well creates a pressure-wave (water-hammer) that propagates up the tubing and into the surface piping. Gradual bean-down allows the pressure transients to dissipate without exceeding the burst margins of upstream piping.
- **Inversion to artificial-lift operating envelope** — for wells on gas lift, ESP, or other artificial-lift systems, bean-down may inflect into a different operating regime (e.g. an ESP well beaned down too aggressively may shut in below the pump's minimum-rate envelope, risking pump damage).

## ESD interlock context

The production choke is a flow-control device, not a safety barrier per [API RP 14C](../standards/api-rp-14c.md) taxonomy. The choke participates in the facility ESD logic but does not provide the well-isolation barrier; that is provided by the surface safety valve (SSV) on the production wing of the tree, the wing/master valves further upstream, and the subsurface safety valve (SSSV) downhole per [API Spec 14A](../standards/api-spec-14a.md).

Typical ESD logic structure (per RP 14C SAFE-chart methodology):

- **High/low pressure shutdown (PSHL)** on the choke discharge line — initiates ESD on overpressure (downstream blockage indication) or underpressure (loss of well or flow-line rupture indication). PSHL setpoints are bracketed around the normal operating envelope of the choke.
- **Coordinated closure sequence on ESD** — choke biases toward closure first (reducing flow), SSV closes (topside well isolation), wing valve closes (additional tree isolation), master valve closes (final tree isolation), SSSV closes (downhole well isolation). The sequence is designed to avoid creating new hazards (e.g. trapping high-pressure fluid against closed valves, creating water-hammer pressure waves).
- **Choke as part of partial-shutdown logic** — some upset conditions (separator high-level, compressor trip) can be managed by beaning down the chokes on the affected wells without full ESD. RP 14C SAFE charts structure these intermediate shutdown paths.

See [API RP 14C](../standards/api-rp-14c.md) for the safety-system standards anchor and [API Spec 14A](../standards/api-spec-14a.md) for the SSSV envelope.

## Cross-domain interactions

- **Perforation strategy coupling** — bean-up rate is constrained by the cleanliness of the perforation tunnels left by the perforation programme. See the dedicated section in [Perforating](perforating.md). Flush-flow chokes (early-life cleanup) and reservoir-deliverability-limited chokes (mid- to late-life) have different sizing economics.
- **Gas-lift coordination** — for gas-lifted wells, the production choke and the gas-injection choke must be coordinated. See [Gas Lift Overview](gas-lift-overview.md) for the injection-side context.
- **Sand-control coupling** — sand-control completions and choke architecture are tightly coupled. A standalone-screen completion produces a well with measurable residual sand carryover; the choke must be erosion-rated for that duty. See [Sand Control](sand-control.md) and [Choke Sand Erosion](choke-sand-erosion.md).
- **Stimulation coupling** — wells brought on production after acid stimulation (see [Matrix Acid Stimulation](matrix-acid-stimulation.md)) or hydraulic fracturing (see [Hydraulic Fracturing](hydraulic-fracturing.md)) carry distinct early-life flowback profiles (acid spent-fluid, frac-flowback fluid + proppant flowback). Bean-up procedures are tuned accordingly.
- **Casing-burst rating** — the wellhead-and-choke section design pressure interacts with the burst-rating margin of the production casing. See drilling-engineering [Casing Program Design](../../../drilling-engineering/wiki/concepts/casing-program-design.md).

## Vendor archetype framing

The choke-services landscape includes integrated production-equipment majors plus specialty choke manufacturers:

- **Master Flo** — independent choke specialist; broad portfolio of fixed-bore, adjustable, and multistage chokes across surface and subsea service envelopes.
- **Mokveld** — independent severe-service control-valve and choke specialist; strong in cage-type chokes for high-pressure-drop service.
- **Cameron (a Schlumberger company)** — surface-tree, subsea-tree, and standalone-choke manufacturer; broad portfolio across surface and subsea.
- **Emerson (Fisher and Baker Hughes valve brands)** — integrated control-valve and severe-service-choke portfolio.

Other notable independents: **Weir Group (SPM)**, **Kent Introl**, **Severn Glocon**. Vendor proprietary algorithm details (CV-curve generation methods, erosion-rate models, trim-geometry optimisation) are not reproduced in this wiki — concept-level coverage only, with explicit "no proprietary content" framing per the production-engineering wiki's vendor-archetype discipline.

## Standards anchor

- [API RP 14C](../standards/api-rp-14c.md) — safety-system architecture; choke participates in coordinated-ESD logic, PSHL interlocks
- [API Spec 14A](../standards/api-spec-14a.md) — subsurface safety valve envelope (downhole well-isolation barrier complementary to the choke and SSV)
- **API RP 14E** (cross-link to engineering-standards wiki) — choke discharge piping erosional-velocity criterion (V_e); influences choke sizing economics
- **NACE MR0175 / ISO 15156** — sour-service material requirements for choke trim, body, and seal metallurgy

## Cross-references

- [Choke Types](choke-types.md), [Multiphase Choke Modeling](multiphase-choke-modeling.md), [Choke Sand Erosion](choke-sand-erosion.md)
- [API RP 14C](../standards/api-rp-14c.md), [API Spec 14A](../standards/api-spec-14a.md)
- [Perforating](perforating.md), [Perforation Strategy](perforation-strategy.md) — bean-up coupling
- [Gas Lift Overview](gas-lift-overview.md) — injection-side coordination
- [Sand Control](sand-control.md) — erosion-duty coupling
- [Matrix Acid Stimulation](matrix-acid-stimulation.md), [Hydraulic Fracturing](hydraulic-fracturing.md) — post-stimulation flowback bean-up
- Drilling-engineering: [Casing Program Design](../../../drilling-engineering/wiki/concepts/casing-program-design.md)

## Public references

- **Arnold, K. & Stewart, M.** — *Surface Production Operations*, Volume 1 (Design of Oil Handling Systems and Facilities), 3rd ed., Gulf Professional Publishing (Elsevier), ISBN 978-0-7506-7853-7. Surface-facility design chapters cover choke selection, sizing, and ESD interlocking.
- **Lyons, W. C. (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, Elsevier (ISBN 978-0-7506-7785-1). Production-operations chapter covers choke management and operating-point control.
- **Brill, J. P. & Mukherjee, H.** — *Multiphase Flow in Wells*, SPE Monograph Series Vol. 17, 1999 (ISBN 978-1-55563-080-5). Foundational multiphase-flow reference; chokes are covered in the multiphase-flow operating-context chapters.
- **SPE OnePetro choke literature** — extensive corpus on choke selection, multiphase choke performance, sand-erosion-rated choke design, and ESD interlocking practice.
- **API RP 14C** (8th edition 2017, Errata 1 2018) — safety-system methodology that structures choke ESD interlocking. See [API RP 14C](../standards/api-rp-14c.md).
- **Beggs, H. D.** — *Production Optimization Using Nodal Analysis*, 2nd ed., OGCI Publications, 2003 (ISBN 0-930972-14-7). Nodal-analysis framework for IPR/TPR/choke operating-point selection.
