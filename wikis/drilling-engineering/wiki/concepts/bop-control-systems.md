---
title: "BOP Control Systems"
tags: [bop-control, accumulator, koomey, mux, hpu, response-time]
sources:
  - api-spec-16d
added: 2026-05-13
last_updated: 2026-05-13
---

# BOP Control Systems

## Scope

The hydraulic and electrohydraulic systems that operate the BOP stack — accumulator, hydraulic power unit (HPU), control manifold, and the multiplexed-electrohydraulic (MUX) modern subsea control. API Spec 16D anchors the spec; this concept page describes the architectures used in practice.

## Surface BOP control (land rig / jackup)

- **Koomey-style hydraulic unit** — accumulator bottle bank + HPU pump + manifold + control valves on the rig floor
- Short hydraulic hose runs (< 100 ft) to the BOP stack on the wellhead
- Sub-second response time for ram closure
- Accumulator sized to operate full function set without HPU pump support

## Subsea BOP control — pilot hydraulic (legacy)

- Hydraulic pilot lines down the marine riser umbilical
- Hydraulic accumulator banks on the BOP stack itself (high-pressure water-glycol fluid)
- Slow response (multi-second) due to hydraulic-fluid travel time down 1,000-10,000 ft of pilot line
- Large umbilical-hose bundle
- Modern rigs may use pilot hydraulic as backup to MUX

## Subsea BOP control — MUX (multiplexed electrohydraulic)

- Electric control signals over electrical multiplexed umbilical down the riser
- Hydraulic accumulators on the BOP stack itself
- Solenoid valves on the BOP open and close in response to electric signals
- Fast response (sub-second)
- Smaller umbilical, allowing larger marine riser ID
- Dual-redundant pods on the BOP for fault-tolerance

## Accumulator sizing per API Spec 16D

The accumulator must be sized to operate the full BOP function set (close all rams + close annular + open + flush) **without HPU pumping** — protects against electrical / hydraulic power failure. Specific volume formula in 16D depends on BOP type counts and stack hydraulic-volume requirements.

## Response-time requirements

API Spec 16D mandates closure-time targets — typically 30 seconds for annular preventers (10 sec for ram preventers in some specifications) at full stack pressure. Function-test logs verify response time meets spec.

## Public references

- **API Spec 16D** — [api-spec-16d.md](../standards/api-spec-16d.md). Primary authority.
- **API RP 53** — [api-rp-53.md](../standards/api-rp-53.md). Operational integration.

## Cross-references

- [BOP Stack Overview](bop-stack-overview.md), [BOP Pressure Classes](bop-pressure-classes.md), [Shut-In Procedures](shut-in-procedures.md), [Well-Control Methods](well-control-methods.md)
