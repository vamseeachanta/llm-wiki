---
title: "Motion Compensation Systems"
tags: [motion-compensation, heave-compensation, drillstring, marine-riser, riser-tensioner, drawworks, active-heave, passive-heave, ahc, phc, offshore-drilling, offshore-crane]
sources:
  - nov-motion-compensation-product-family
added: 2026-05-12
last_updated: 2026-05-12
see_also:
  - concepts/dynamic-positioning.md
  - concepts/motions-rao.md
  - concepts/station-keeping.md
---

# Motion Compensation Systems

## Scope

This page synthesises the families of **motion compensation systems** used on offshore drilling and lifting vessels to decouple a suspended load — drillstring, marine riser, subsea package — from vessel heave. It treats the systems at a synthesis level: principle of operation, the principal architectural families, the passive-versus-active distinction, the control architecture for active systems, and the standards landscape. It does **not** restate vendor brochure content, capacity tables, stroke envelopes, or control-loop tuning detail — those depend on the specific product and revision and are deferred to vendor documentation and the standards-publisher documents named below.

## Purpose: decoupling the load from vessel heave

Floating drilling vessels and crane vessels experience vertical motion (heave) at wave frequency. Without compensation:

- The **drillstring** would see oscillatory weight-on-bit (WOB), risking bit damage, drilling-rate variability, and stress fatigue on tubular connections.
- The **marine drilling riser** would see oscillatory axial tension, varying about the top-tension setpoint and potentially excursioning into compression at the connector.
- A **crane-suspended load** would see corresponding vertical excursion at the seabed or landing target, defeating precision installation.

Motion compensation introduces a passive or active mechanism that absorbs vessel heave so that the load motion at the lower end of the system is much smaller than the motion at the deck. The system is sized by the expected heave amplitude and period at the operating sea state, the suspended weight, and the required residual motion at the bottom of the string.

## Passive versus active heave compensation

| Attribute | Passive heave compensation (PHC) | Active heave compensation (AHC) |
|---|---|---|
| Principle | Pre-charged gas-over-fluid accumulator acts as a soft spring; stroke is governed by load and gas-law behaviour. | Servo-controlled hydraulic or electric actuator driven by a heave reference, holding the load at a commanded position. |
| Sensing required | None for basic operation. | Motion reference unit (MRU/IMU) at the deck; sometimes load and position feedback. |
| Residual motion | Reduces but does not eliminate motion; behaviour depends on accumulator stiffness and damping. | Can reduce residual motion at the load to a small fraction of vessel heave (sub-decimetre is achievable at modest sea states). |
| Energy use | Effectively zero (passive). | Continuous hydraulic / electric power supply. |
| Failure mode | Degrades gracefully to a stiffer or softer spring. | Loses compensation if the control loop or actuator fails; usually backed by a passive fall-back. |
| Typical use | Riser tensioning baseline; drillstring compensation in benign sea states. | Crown-mounted drillstring compensation in deep water; AHC drawworks; AHC subsea-installation cranes. |

Many production systems are **hybrid**: a passive accumulator carries the static load while an active loop trims the residual motion. This combines the energy efficiency of PHC with the precision of AHC.

## Architectural families

### Drillstring compensation

The drillstring is suspended from the travelling block; the compensator's job is to keep the bit weight on bottom approximately constant as the vessel heaves.

- **Crown-mounted compensator (CMC).** A pair of cylinders mounted at the top of the derrick (the "crown"). The travelling block is suspended below the cylinder rods. As the vessel heaves, the rods stroke to decouple the block from the derrick motion. The cylinders are typically connected to a high-pressure gas-over-fluid accumulator (PHC) or to a servo-hydraulic supply (AHC) or both.
- **In-line / deadline compensator.** A compensator integrated at the deadline anchor end of the drilling line, or in line with the travelling-block suspension below the crown. Mechanically simpler than CMC but constrains line and sheave geometry.
- **Drawworks-integrated active heave compensation (AHC drawworks).** The drum motion of the drawworks itself is servo-controlled to spool line in and out at the heave rate, compensating heave at the hook. This is the architecture of NOV's AHD / AHDD product family ([source](../sources/nov-2026-motion-compensation-product-family.md)).

### Marine riser tensioning

The marine drilling riser is held in tension at the top so it does not buckle under its own submerged weight and so that the riser angle at the lower marine riser package (LMRP) stays within operating limits.

- **Wireline (deadline) tensioners.** Wire ropes run from each riser tensioner to the top of the riser tensioner ring around the riser; a hydraulic-pneumatic cylinder at the deck end maintains tension as the vessel heaves.
- **Direct-acting tensioners (DAT).** Hydraulic cylinders connect directly between the rig structure and the riser tensioner ring without intervening wire ropes; mechanically stiffer and reduces wire-rope failure modes.
- Tensioners are predominantly **passive** (gas-charged accumulator springs) with optional active trimming on modern systems. Capacity is set to maintain top tension within the API RP 16Q operating envelope across the design heave amplitude.

### Crane and winch heave compensation

- **Active heave compensation cranes.** Offshore subsea cranes installing equipment to the seabed use AHC to hold the load at a stable depth, decoupled from vessel heave. The control loop uses a vessel-mounted MRU and a position controller on the winch.
- **Passive heave compensation modules.** Pneumatic accumulators in series with the lift wire absorb heave for less stringent operations.
- **Constant-tension winches.** A related family that targets a tension setpoint rather than a position; used for mooring and towing rather than precision installation.

## Control architecture for active compensation

Active heave compensation closes a control loop on heave error:

1. **Heave measurement.** A motion reference unit (MRU) or inertial measurement unit (IMU) mounted on the vessel hull produces a heave signal (and roll/pitch) in real time.
2. **Reference frame and feed-forward.** The MRU signal is integrated and transformed to the actuator's coordinate system; a feed-forward command commands the actuator to track the heave directly.
3. **Closed-loop feedback.** Actuator position and load force are measured and fed back; the controller corrects feed-forward errors due to actuator dynamics and external disturbances.
4. **Limit and supervision logic.** Stroke limits, pressure limits, and rate limits guard the actuator; supervision logic detects MRU faults and reverts to passive operation.

System performance is characterised by **residual motion at the load** under specified heave conditions, **time response** of the actuator (bandwidth), and **maximum operating heave amplitude** before the actuator saturates.

## Standards and class-rules landscape (named only — clauses not reproduced)

- **API Spec 8C** — *Specification for Drilling and Production Hoisting Equipment*. The principal specification governing the design and rating of hoisting equipment including compensators. (Current edition.)
- **API Spec 16F** — *Specification for Marine Drilling Riser Equipment*. Covers riser tensioning equipment. (Current edition.)
- **API RP 16Q** — *Recommended Practice for Design, Selection, Operation, and Maintenance of Marine Drilling Riser Systems*. Sets operating-envelope methodology in which the riser tensioner is sized. (Current edition.)
- **DNV-OS-E101** — *Drilling Plant*. DNV offshore standard for drilling plant including hoisting and compensation systems. (Current edition.)
- **ABS Guide for the Classification of Drilling Systems**. American Bureau of Shipping classification reference for drilling equipment.
- **ISO 13628 series** — *Petroleum and natural gas industries — Design and operation of subsea production systems*; relevant parts address subsea riser systems that interface with surface tensioning equipment.

Each named document is the audit-trail anchor for any quantitative claim that this concept page does not make. Refer to the publisher's current revision and forward-adopt the citation in standards pages as those land in `wiki/standards/`.

## Vendors and product context

Motion compensation hardware is supplied by a small number of integrators with overlapping product lines:

- **NOV (National Oilwell Varco).** CMC, riser tensioners, AHD / AHDD drawworks ([source](../sources/nov-2026-motion-compensation-product-family.md)); the subject of the ingest that triggered this page.
- **Other major suppliers** include Cameron (part of SLB) and former heritage brands (Maritime Hydraulics, MHWirth) whose product lines have moved through the offshore-equipment consolidation cycle. The current owner of any specific historical product line should be checked against the supplier's current public catalogue; vendor identity is **not** a basis for any technical claim on this page.

## Cross-References

- [Dynamic Positioning](dynamic-positioning.md) — the lateral-station-keeping counterpart to vertical heave compensation; the two systems together hold the suspended-load position envelope.
- [Motions and Response Amplitude Operators](motions-rao.md) — the vessel-side motion characterisation that feeds the heave-amplitude design input for compensator sizing.
- [Station-Keeping](station-keeping.md) — the broader station-keeping framing for floating-system operations.

## Public references

The treatments below are the public-citable anchors for the material on this page. The NOV vendor brochures are on the [NOV (2026)](../sources/nov-2026-motion-compensation-product-family.md) source page and are **not** the anchor for any technical claim on this page.

- API Spec 8C (current edition). *Specification for Drilling and Production Hoisting Equipment*. American Petroleum Institute, Washington DC.
- API Spec 16F (current edition). *Specification for Marine Drilling Riser Equipment*. American Petroleum Institute, Washington DC.
- API RP 16Q (current edition). *Recommended Practice for Design, Selection, Operation, and Maintenance of Marine Drilling Riser Systems*. American Petroleum Institute, Washington DC.
- DNV-OS-E101 (current edition). *Drilling Plant*. DNV, Høvik. (Successor to legacy DNV-OS-E101 / DNVGL-OS-E101 designations.)
- ABS Guide for the Classification of Drilling Systems (current edition). American Bureau of Shipping, Houston.
- ISO 13628 series (current parts). *Petroleum and natural gas industries — Design and operation of subsea production systems*. International Organization for Standardization, Geneva.
- Hatleskog, J.T. and Dunnigan, M.W. (2007). "Passive Compensator Load Variation for Deep-Water Drilling". *IEEE Journal of Oceanic Engineering*, IEEE. — Public peer-reviewed treatment of PHC accumulator behaviour with load variation.
- Bai, Y. and Bai, Q. (2018). *Subsea Engineering Handbook*, 2nd edition. Gulf Professional Publishing / Elsevier. ISBN 978-0-12-812622-6. — General offshore-system reference covering heave compensation in the context of subsea installation.
- Offshore Technology Conference (OTC) proceedings — multiple papers across recent years on heave-compensation control, deep-water riser tensioning, and AHC crane performance. Public via OnePetro: https://onepetro.org/.
