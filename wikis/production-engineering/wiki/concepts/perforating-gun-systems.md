---
title: "Perforating Gun Systems"
tags: [perforating, tcp, wireline-conveyed, coiled-tubing, gun-system, expendable, retrievable, packer]
sources:
  - api-rp-19b
added: 2026-05-15
last_updated: 2026-05-15
---

# Perforating Gun Systems

## Scope

The **gun system** is the assembly that carries shaped charges to depth, holds them in the correct spatial pattern, and detonates them on command. This page covers the conveyance and hardware framework — TCP vs wireline vs coiled-tubing, expendable vs retrievable, gun-system sizing relative to casing — and the operational decisions that flow from gun-system selection. Charge mechanics are in [Perforating — Shaped Charges](perforating-shaped-charges.md); strategy is in [Perforation Strategy](perforation-strategy.md); the system-level synthesis is in [Perforating](perforating.md).

## Conveyance family overview

| Conveyance | Carrier | Typical use case | Key constraint |
|---|---|---|---|
| Tubing-Conveyed Perforating (TCP) | Production tubing + packer | Long intervals, simultaneous perforate-and-test, high-rate completions | Permanent commitment (tubing tied to gun) |
| Wireline-conveyed | Slickline (mechanical wireline) or e-line (electrical wireline) | Short intervals, recompletion add-on perfs, cost-sensitive workover | Gravity conveyance — fails in highly-deviated and horizontal wells |
| Coiled-tubing-conveyed | Coiled tubing string with internal e-line | Highly-deviated and horizontal wells; pushed in, not gravity-fed | Higher day-rate than wireline |
| Through-tubing | E-line; gun OD small enough to pass through production tubing ID | Recomplete a producing well without pulling tubing | Limited gun OD → limited charge size → limited penetration |

Modern completions are dominated by TCP for first-completion perforating and by wireline / through-tubing for recompletion and add-on perfs.

## Tubing-Conveyed Perforating (TCP)

### Concept

A long string of perforating guns is attached to the bottom of the production tubing (or to a workstring run with packer). The gun string is run in the hole along with the tubing, the packer is set above the gun, the well is conditioned (often including a circulation displacement to underbalance), and the guns are fired from surface — typically via:

- **Drop-bar mechanical firing** — a steel bar dropped from surface impacts a firing head
- **Pressure-actuated firing** — pressure pulse from surface through the tubing or annulus triggers the firing head
- **Electric firing (less common in TCP)** — e-line wireline rigged through the gun string

### Strengths

- **Long intervals** — TCP gun strings can be hundreds of feet long; the limit is mechanical (string weight in casing) not conveyance.
- **High shot density** — TCP guns are typically large OD (matched to casing ID), supporting 8-18 spf with deep-penetrating charges.
- **Simultaneous perforate-and-flow** — the well can flow immediately after perforation through the tubing above the gun. This is the **standard** completion-and-test workflow in modern operations.
- **Underbalanced perforating** — TCP is the canonical UBP conveyance method because the tubing column can be displaced to underbalance before firing.

### Weaknesses

- **Cost** — gun string + packer + firing head + rig time. The most expensive perforating method per foot.
- **Commitment** — once the gun string is in the hole, recovery is non-trivial. Misfire risk → fishing job.
- **Specialised guns / mechanical considerations** — gun-string weight, casing-ID match, firing-head selection, packer-rating, all interact and require detailed completion-engineering review.

### When TCP wins

- First-completion perforating for any production well
- Long intervals (greater than ~ 50 feet)
- High-rate gas or oil completions where productivity justifies cost
- Simultaneous perforate-and-test programmes

## Wireline-conveyed perforating

### Concept

A shorter gun string (typically a few feet to a few tens of feet) is conveyed downhole on a slickline (mechanical wireline, no electrical conductor) or e-line (electrical wireline with armoured conductor for telemetry and gun firing). The gun is positioned by depth measurement (line tension and wheel calibration on slickline; CCL — casing-collar-locator — on e-line), fired, and recovered.

### Slickline vs e-line

- **Slickline** — single-strand mechanical line; cheaper rig-up; less precise depth control; gun firing typically via mechanical bar drop or pre-set hydraulic timer. Used for cost-sensitive short-interval jobs.
- **E-line** — multi-conductor electrical line; precise CCL depth control; electric gun firing; real-time downhole telemetry. The standard for any wireline perforating where depth accuracy or firing-confirmation matters.

### Strengths

- **Cost** — order-of-magnitude cheaper than TCP for short intervals.
- **Speed** — rig-up and rig-down are hours, not days.
- **Through-tubing capability** — small-OD guns can be run through completion tubing without pulling the well apart.

### Weaknesses

- **Gravity conveyance** — wireline only works where the well is steep enough for gun weight to drive the line downhole. The practical limit is typically 60-70° deviation; beyond that, **coiled-tubing conveyance** is required.
- **Short intervals only** — gun-string length limited by rig-up and surface lubricator capacity.
- **Lower shot density** — through-tubing guns are slim, supporting lower spf than TCP.
- **Reduced charge size** — slim through-tubing guns accommodate only small charges, reducing penetration depth.

### When wireline wins

- Recompletion add-on perforating in vertical wells
- Short add-on intervals on cased-hole frac stages
- Through-tubing recompletion when not pulling the existing tubing
- Cost-sensitive workover scopes

## Coiled-tubing-conveyed (CT-conveyed)

### Concept

The gun string is conveyed downhole on a coiled-tubing string with an internal e-line. The CT provides **push** capability — it can drive the gun string through highly-deviated and horizontal sections where wireline gravity-conveyance fails. The e-line inside the CT carries firing commands and telemetry.

### Strengths

- **Horizontal and high-angle wells** — the dominant perforating conveyance in horizontal-well completions when full TCP is not justified.
- **Recompletion in horizontal wells** — add-on perfs in horizontal producers, where wireline cannot reach.
- **Real-time depth control + firing confirmation** — same as e-line.

### Weaknesses

- **Cost** — CT day-rate is substantially higher than wireline; coiled tubing requires its own surface spread.
- **CT length** — limited by reel capacity; very-long horizontal sections may exceed reel limits, requiring multiple stages or alternative conveyance.

### When CT-conveyed wins

- Recompletion in horizontal or highly-deviated producers
- Re-perforating sections of a horizontal well after initial frac stages
- Multi-stage perforate-frac-plug-perforate sequences in some unconventional completions (though most use wireline-deployed perforating guns dropped into horizontal sections via pumpdown rather than CT-conveyance, which is a separate workflow)

## Through-tubing perforating

### Concept

A subset of wireline-conveyed perforating: the gun OD is small enough to pass through the completion tubing ID. Used for recompletion of an existing well without pulling tubing.

### Trade-offs

- Gun OD is bounded by tubing ID — typically 1¹¹⁄₁₆", 2⅛", or 2½" guns
- Charge size is bounded by gun OD — typically smaller deep-penetrating or specialised through-tubing charges
- Shot density is bounded by gun geometry — typically 4-6 spf
- Penetration is shorter than full-bore TCP because of charge-size constraint

Used heavily for recompletion of producing wells, especially in mature fields where the cost of pulling tubing exceeds the production gain from full-bore re-perforation.

## Expendable vs retrievable

### Expendable guns

- After firing, the gun-body steel breaks up; debris falls into the wellbore
- Cheaper per shot
- Tolerated downstream operations must accommodate the debris
- Common in cased-hole frac perforating where debris is irrelevant (the stage will be plugged and abandoned anyway)

### Retrievable guns

- The gun body remains intact and is recovered to surface
- More expensive per shot
- Clean wellbore — no debris cleanup required
- Common in completions where downhole intervention is anticipated (e.g. recompletion-prone reservoirs, sand-control completions)

### Hollow-carrier vs port-plug

- **Hollow-carrier** — gun has a steel outer carrier with closed ports at each charge location; charges fire through the ports, jet exits the gun, carrier remains intact (retrievable). Higher per-shot cost.
- **Strip / port-plug** — charges are exposed (not enclosed in a hollow carrier) or enclosed in expendable port plugs; cheaper per shot; debris is left in the wellbore.

The hollow-carrier / port-plug split is largely orthogonal to the conveyance dimension — TCP guns can be either hollow-carrier or strip; wireline guns can be either; etc.

## Gun OD and casing ID — the stand-off match

The **gun-to-casing-wall stand-off** is the operator-controllable lever for charge performance (see [Perforating — Shaped Charges](perforating-shaped-charges.md)). Charges are designed for an optimum stand-off, typically 0.2-0.7 inches.

| Casing OD | Casing ID (typical, 32 lb/ft P-110) | Recommended gun OD range |
|---|---|---|
| 4½" | ~ 3.8" | 3⅜" |
| 5½" | ~ 4.9" | 4¼" or 4½" |
| 7" | ~ 6.0" | 5" or 5⅛" |
| 9⅝" | ~ 8.5" | 7" or 7½" |

A slim gun in a big-bore casing creates excessive stand-off, derating penetration. A maximum-OD gun in the matched casing gives best penetration but reduces clearance for other tools (CT shifting tools, future intervention BHAs). Completion engineering trades stand-off vs intervention-clearance.

## Casing-burst interaction

Detonation of a shaped-charge gun creates a transient pressure pulse in the wellbore — the **detonation overpressure**. For a typical large-OD TCP gun firing a high shot density, this pulse can be in the thousands of psi range above the static wellbore pressure for milliseconds.

The pulse, combined with the static wellbore pressure, defines a **transient burst load** on the production casing at the perforating depth. For high-rated casing this is a non-issue; for thin-wall or de-rated casing strings, the burst-design margin can be eroded by gun detonation.

Practical consequences:

- Heavy / large-OD gun strings are subjected to a burst-check against the casing they will fire into.
- Gun-string design for HPHT wells often uses **lower-energy charges** and **reduced shot density** to bound the detonation pulse.
- Gun-detonation-pulse modelling is standard pre-job analysis for completion-engineering teams.

See drilling-engineering [Casing Program Design](../../../drilling-engineering/wiki/concepts/casing-program-design.md) for the burst-design framework that perforation policy interacts with.

## Firing-head systems

Beyond the gun string itself, the **firing head** governs how detonation is initiated:

- **Mechanical (drop-bar)** — surface-released steel bar falls through the tubing, impacts the firing head, triggers a percussion primer. Single-attempt; if the bar gets stuck, the job is over.
- **Pressure-actuated** — tubing or annulus pressure pulse from surface triggers the firing head. Allows multiple firing attempts at different pressures; supports complex multi-stage firing sequences.
- **Electric (e-line)** — direct electrical command from surface, used in wireline and CT-conveyed gun systems. Most precise; lowest failure rate.
- **Hydraulic timer** — preset downhole timer fires after a planned interval; used in some wireline / TCP applications where surface control is limited.
- **Acoustic / RF** (rare, specialised) — proprietary firing heads using non-traditional command paths.

Firing-head selection interacts with well-control posture, expected job duration, and the differential-pressure strategy (UBP / OBP / EOB).

## Vendor archetype framing

The four conveyance families are served by the same vendor archetypes named in [Perforating](perforating.md) — Halliburton, Schlumberger, Baker Hughes, Owen Oil Tools, GEODynamics, DynaEnergetics, Hunting Titan. Each vendor maintains a portfolio across all four conveyance families; the operator's vendor selection typically goes by overall completion-services contract, not by gun-conveyance specialty.

No vendor-proprietary firing-head designs or gun-mechanical-engineering details are reproduced in this wiki — concept-level only. Operators specifying gun systems should consult vendor catalogues and the [API RP 19B](../standards/api-rp-19b.md) test data for the specific gun-and-charge combination under consideration.

## Cross-references

- [Perforating](perforating.md) — system-level synthesis
- [Perforating — Shaped Charges](perforating-shaped-charges.md) — charge physics
- [Perforation Strategy](perforation-strategy.md) — shot-density / phasing / differential strategy
- [API RP 19B](../standards/api-rp-19b.md) — charge-evaluation methodology
- Drilling-engineering: [Casing Program Design](../../../drilling-engineering/wiki/concepts/casing-program-design.md) — casing-burst interaction
- [Electric Submersible Pumps](electric-submersible-pumps.md), [Gas Lift Overview](gas-lift-overview.md) — IPR / artificial-lift coupling

## Public references

- **Bell, W. T. & Behrmann, L. A.** — *Perforating Applications in the Petroleum Industry* (SPE Reprint Series). Covers gun-system design context.
- **King, G. E.** — multiple SPE papers on completion-engineering practice including perforating-gun-system selection (1990s-2010s).
- **Cosad, C.** — "Choosing a Perforation Strategy," *Oilfield Review*, October 1992. Older but practitioner-canonical on conveyance / charge / strategy framework.
- **SPE OnePetro perforating literature** — extensive on TCP / wireline / CT-conveyed operations and lessons-learned.
- **Lyons, W. C. (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, Elsevier (ISBN 978-0-7506-7785-1).
