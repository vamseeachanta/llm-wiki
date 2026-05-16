---
title: "Choke Types"
tags: [choke, fixed-bore, adjustable-choke, cage-choke, multistage-choke, trim-material, subsea-choke, production-engineering]
sources:
  - api-rp-14c
added: 2026-05-16
last_updated: 2026-05-16
---

# Choke Types

## Scope

Production chokes fall into a small number of distinct hardware-architecture families. Each family is characterised by its flow-control element (orifice geometry and adjustability), its pressure-drop staging, its erosion/cavitation tolerance, and its serviceability envelope. This page catalogues the four dominant architectures (fixed-bore, adjustable, cage, multistage), describes the trim-material families that underpin them, and frames the surface-vs-subsea service-envelope distinction.

For the operational discipline of choke management (bean-up, ESD interlocking, operating-point selection), see the router page [Choke Management](choke-management.md). For multiphase flow physics across the choke, see [Multiphase Choke Modeling](multiphase-choke-modeling.md). For erosion considerations under sand-laden duty, see [Choke Sand Erosion](choke-sand-erosion.md).

## Fixed-bore (positive) chokes

A fixed-bore choke uses a precision-machined cylindrical orifice (the "bean") of fixed inside diameter, mounted in a flanged choke body. Flow rate is set by the bean diameter; changing the operating point requires manually swapping the bean, typically during a workover or planned facility shutdown.

**Characteristics:**

- **Single fixed flow area** — the bean diameter (often expressed in 64ths of an inch, e.g. "24/64-inch bean") sets the orifice flow area.
- **Mechanically simple** — minimal moving parts, low complexity, low first cost.
- **Replacement-only adjustment** — re-sizing requires depressurising the line, opening the choke body, and replacing the bean insert.
- **Trim material** — typically tungsten-carbide or stellite-class hardfaced bean; ceramic beans appear in highly-abrasive service.

**When chosen:**

- Stable wells with well-understood flow envelope and infrequent operating-point changes.
- Backup or secondary chokes (e.g. subsea-tree chokes paired with topside adjustable chokes; the subsea choke holds a fixed conservative position while the topside choke does the active control).
- Low-cost installations where adjustability is not an operational requirement.
- Well-test facilities where flow rate is held constant during the test interval.

**Limitations:**

- Cannot accommodate well-aging deliverability changes without intervention.
- Cannot participate in dynamic ESD bean-down sequences; ESD logic at fixed-bore-choked wells relies on the SSV and tree valves for isolation.

## Adjustable chokes

An adjustable choke uses a stem-and-seat (or similar) variable-flow-area mechanism, continuously variable from a hand-wheel, pneumatic actuator, hydraulic actuator, or electric actuator. The flow area changes continuously with stem position, allowing the operator to track the well's deliverability changes over time and respond to facility-load-balancing requests in real time.

**Characteristics:**

- **Continuously variable flow area** — typically a needle-and-seat or stem-and-port geometry, with the stem driven by an actuator providing position-feedback to the surface controller.
- **Active control element** — supports nodal-analysis-driven operating-point control and integration with facility production-management systems.
- **Trim material** — tungsten-carbide stem and seat are the default for moderate-erosion service; stellite-class hardfacing is common; ceramic stems and seats appear in highly-abrasive service.
- **Actuation flexibility** — pneumatic actuators are the most common for surface installations; hydraulic actuators dominate subsea applications; electric actuators are increasingly common for both as control-system architectures shift toward all-electric.

**When chosen:**

- Wells requiring active rate control (deliverability changes over time, facility-balancing demands, regulatory-allowable enforcement).
- Modern surface-tree default for wells where the additional cost over a fixed-bore choke is justified by operational flexibility.
- Production-test installations where flow rate is varied through a test sequence.

**Limitations:**

- More complex actuator and seal arrangement than fixed-bore; higher first cost; more frequent maintenance.
- Stem-and-seat geometry is more vulnerable to localised erosion at high differential pressure than the long cylindrical bean of a fixed-bore choke.
- Cavitation at high single-stage pressure-drop service can damage the seat profile and cause erratic control response.

## Cage chokes

A cage choke uses a perforated cylindrical cage (the "cage") with multiple orifice openings; flow area is adjusted by rotating or translating a sleeve relative to the cage to expose or occlude the cage orifices in discrete steps. The cage geometry distributes the pressure drop across multiple parallel orifices, reducing peak velocity and shifting cavitation onset to higher differential pressure than a comparable single-orifice geometry.

**Characteristics:**

- **Multi-orifice flow area** — flow is divided among the open cage orifices, each carrying a fraction of the total flow; peak velocity at each orifice is much lower than the equivalent single-orifice choke.
- **Discrete step adjustability** — flow area changes in steps as cage orifices are progressively exposed; modern cage chokes use machined opening sequences to give smooth equal-percentage or linear effective characteristic.
- **Pressure-drop staging** — some cage designs incorporate sleeves with progressive multi-stage cage geometries that distribute pressure drop along the flow path rather than concentrating it at the orifice plane.
- **Trim material** — tungsten-carbide cage and sleeve are the default; ceramic cages appear in highly-abrasive HP gas service.

**When chosen:**

- High-pressure-drop service where single-stage adjustable choke geometry approaches cavitation or peak-velocity limits.
- Severe-erosion service where the multi-orifice geometry distributes erosion across multiple flow paths instead of concentrating it at a single stem-and-seat point.
- Noise- and vibration-sensitive service where the multi-orifice geometry reduces flow-induced vibration and acoustic noise.
- Subsea-tree default for high-rate wells where the long replacement cycle of subsea hardware penalises trim-erosion-driven failures.

**Limitations:**

- Higher complexity and first cost than adjustable chokes.
- Cage-orifice geometry is less tolerant of solids-laden flow than a long cylindrical bean; sand can pack into the cage-sleeve clearance and cause sticking.
- Cage clean-out during workover is more time-consuming than bean replacement.

## Multistage chokes

A multistage choke combines two or more pressure-drop elements in series (typically a primary cage followed by a secondary trim, or a sequence of staged orifices) to distribute the total pressure drop across multiple sequential stages. Each stage takes a fraction of the total pressure drop, reducing peak velocity and avoiding cavitation in service where a single-stage drop would be impossible.

**Characteristics:**

- **Sequential pressure-drop staging** — the upstream stage(s) take part of the pressure drop and discharge to an intermediate pressure; the downstream stage(s) take the remaining pressure drop. Total flow area at each stage is sized to achieve the target stage pressure drop.
- **Cavitation avoidance** — by keeping each stage's pressure drop below the cavitation threshold for the local fluid conditions, multistage geometry avoids the trim erosion, noise, and vibration damage that single-stage cavitation produces.
- **Geometry families** — common architectures include cage-and-plug multistage, drilled-disc-stack multistage, and labyrinth-path multistage. Specific geometry choice depends on the service envelope (gas vs liquid vs multiphase, sand-laden vs clean, sweet vs sour).
- **Trim material** — tungsten-carbide is the baseline; ceramic stages appear in the most severe abrasion service; specialty hardfacings (e.g. boron-carbide composites) appear in vendor-specific portfolios for extreme service.

**When chosen:**

- Severe pressure-drop service: HP gas wells where wellhead-to-separator differential exceeds the single-stage cavitation envelope; deepwater HPHT wells where reservoir pressure relative to topside separator pressure forces multi-thousand-psi differentials across the choke.
- Subsea HP gas tiebacks where the long subsea flowline and topside-host pressure budget force most of the pressure drop to occur at the tree-mounted choke.
- High-cavitation-risk service where single-stage drop would damage trim within an unacceptable replacement cycle.

**Limitations:**

- Highest complexity and first cost of the four families.
- Most difficult to retrofit into existing tree or surface-piping geometry (the staged-geometry length is longer than single-stage hardware).
- Solids-laden service requires careful trim selection — labyrinth and drilled-disc geometries are particularly vulnerable to sand packing.

## Trim materials

Choke trim (the surfaces in direct contact with the flow stream at the pressure-drop location) is the wear-critical component. Trim material selection drives both the erosion-life envelope and the cost of the choke installation.

| Material class | Typical hardness range | Strengths | Weaknesses |
|---|---|---|---|
| **Tungsten carbide (WC)** | Very high (e.g. ~1500-1800 HV) | Industry-default for erosion-critical service; broad service envelope; well-characterised | Brittle under impact loading; failure mode is sudden trim fracture rather than gradual wear |
| **Ceramic (typically zirconia or alumina-based)** | Higher than WC (e.g. ~1800-2200 HV) | Excellent erosion resistance in sand-laden HP gas service; extends replacement intervals significantly over WC | Even more brittle than WC; vulnerable to thermal shock; higher first cost; manufacturing constraints on geometry |
| **Stellite (cobalt-based hardfacing)** | Moderate-high (e.g. ~400-600 HV) | Tolerant of impact loading; good corrosion resistance in sour service; weld-overlay applicable | Lower erosion resistance than WC or ceramic; faster wear in sand-laden service |
| **Hardened alloy steel** | Lower (e.g. ~250-450 HV) | Lowest cost; good for clean-fluid service | Inadequate for sand-laden service; rapid erosion in abrasive duty |
| **Specialty composites (e.g. boron-carbide-filled or diamond-impregnated)** | Variable, often very high | Vendor-specific portfolios for extreme service | Limited availability; high cost; field-experience corpus less developed |

Trim material selection is closely coupled to choke architecture: a fixed-bore choke can use a more aggressive (and brittle) trim material because the bean is a single replaceable insert and replacement frequency drives the installed-cost calculation, while an adjustable or cage choke trim must balance erosion resistance against impact-tolerance because the trim is integral to the actuator assembly.

See [Choke Sand Erosion](choke-sand-erosion.md) for the erosion-rate framework that drives trim selection.

## Surface vs subsea service envelope

The surface-vs-subsea distinction is one of the largest drivers of choke architecture and trim selection:

| Aspect | Surface choke | Subsea choke |
|---|---|---|
| Replacement access | Easy (planned shutdown, manual or pneumatic actuator) | Requires intervention vessel (ROV-actuated, retrievable insert architecture, or full workover) |
| Replacement frequency budget | Tolerant of frequent trim changeouts | Must minimise trim-replacement frequency; drives toward higher-cost erosion-resistant trim |
| Actuation | Pneumatic / electric / manual | Hydraulic (via subsea control system) / electric (emerging all-electric) |
| Control-system integration | Direct facility-DCS integration | Via subsea production control system per API RP 17F |
| Service-envelope severity | Often moderate (downstream of subsea choke) | Often severe (full wellhead-to-separator differential) |
| Architecture default | Adjustable for active control; fixed-bore for backup | Cage or multistage for severe-service; retrievable architecture for trim replacement |

Subsea chokes are often paired with topside backup chokes: the subsea choke takes the bulk of the pressure drop and holds a relatively stable position, while the topside choke does the day-to-day active control. This split optimises the replacement-cost economics (the heavily-cycled topside choke trim is cheaper to replace than the lightly-cycled subsea choke trim).

## Cross-references

- [Choke Management](choke-management.md) — operational discipline router; bean-up, ESD interlocking, operating-point selection
- [Multiphase Choke Modeling](multiphase-choke-modeling.md) — critical/subcritical flow physics across the choke
- [Choke Sand Erosion](choke-sand-erosion.md) — erosion-rated choke selection and replacement-frequency tracking
- [API RP 14C](../standards/api-rp-14c.md) — safety-system architecture; choke participates in coordinated ESD logic
- [API Spec 14A](../standards/api-spec-14a.md) — subsurface safety valve envelope (the downhole counterpart to the topside choke)
- [Selective Production](selective-production.md) — multi-zone-completion tree architecture that hosts the choke

## Public references

- **Arnold, K. & Stewart, M.** — *Surface Production Operations*, Volume 1 (Design of Oil Handling Systems and Facilities), 3rd ed., Gulf Professional Publishing (Elsevier), ISBN 978-0-7506-7853-7. Choke selection and trim material chapters.
- **Lyons, W. C. (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, Elsevier (ISBN 978-0-7506-7785-1). Production-operations chapter covers choke families and trim material selection.
- **Bai, Y. & Bai, Q.** — *Subsea Engineering Handbook*, 2nd ed., Gulf Professional Publishing (Elsevier), 2018 (ISBN 978-0-12-812622-6). Subsea-tree and subsea-choke architecture chapters.
- **SPE OnePetro choke literature** — extensive corpus on choke architecture comparisons, trim-material erosion studies, and subsea-choke retrievable-insert architectures.
- **API RP 14C** (8th edition 2017, Errata 1 2018) — safety-system architecture that the choke installation must integrate with. See [API RP 14C](../standards/api-rp-14c.md).

## Notes

- The four-family taxonomy (fixed-bore / adjustable / cage / multistage) is the dominant industry framing but is not rigid: many modern installations are hybrids (e.g. adjustable choke with cage trim, or cage choke with multistage primary section). Architecture-family naming in vendor data sheets should be interpreted in context.
- Trim hardness values quoted above are illustrative ranges from published metallurgy references; specific values for any given vendor product should be taken from the vendor data sheet, not from this overview.
- The cavitation threshold for single-stage drop is highly fluid-dependent; the multistage transition decision must be made against the specific fluid properties of the well, not against a generic differential-pressure threshold.
