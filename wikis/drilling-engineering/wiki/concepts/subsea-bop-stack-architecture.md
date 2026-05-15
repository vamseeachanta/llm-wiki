---
title: "Subsea BOP Stack Architecture"
tags: [subsea-bop, stack-architecture, lower-stack, lmrp, choke-kill-plumbing, rov-access]
sources:
  - api-spec-16a
  - api-spec-17d
added: 2026-05-14
last_updated: 2026-05-14
---

# Subsea BOP Stack Architecture

## Scope

The full architectural layout of the subsea BOP stack as it sits on the wellhead during deepwater drilling. The "stack" is actually TWO assemblies: a **lower stack** (latched to the wellhead, contains the load-bearing pressure-containment elements) and a **Lower Marine Riser Package (LMRP)** (latched to the lower stack via a disconnect plane, carries the riser-side interface and the hydraulic/MUX control pods). Together they're the deepwater BOP.

## Lower stack components (bottom-up)

1. **Wellhead connector** — bottom of stack; latches to the 18-3/4" subsea wellhead
2. **Pipe ram 1** (typically casing-sized, e.g., 5-1/2" or 5") — seals around drill collar / casing OD
3. **Pipe ram 2** (drill-pipe-sized, e.g., 5") — seals around drill pipe
4. **Variable-bore ram (VBR)** — seals around drill pipe of varying OD
5. **Blind-shear ram** — last-resort element; shears drill pipe + seals
6. **Pipe ram 3** (drill-pipe-sized, redundant)
7. **LMRP disconnect plane** — top of lower stack; mating face for LMRP

## LMRP components (bottom-up of LMRP)

1. **Wellhead connector (BOP-side)** — latches onto lower-stack disconnect plane
2. **Annular preventer** — top of LMRP; primary first-response seal
3. **Riser connector** — top of LMRP; latches onto the marine riser
4. **Hydraulic / MUX control pods** (dual redundant) — operates lower stack functions
5. **Choke / kill / booster auxiliary-line stubs** — interface with riser auxiliary lines

## Choke / kill plumbing

Choke and kill lines run from surface (rig choke manifold) down the marine riser as auxiliary lines, cross the LMRP disconnect plane via the connector interface, and tee into the lower stack at points between the pipe rams. This allows circulation and bleed-off through the lower stack with rams closed.

## ROV-intervention access points

Remotely-operated-vehicle (ROV) intervention is a load-bearing fail-safe capability:

- **Hot-stab panels** — accessible ports for hydraulic actuation if both MUX pods fail
- **Manual override** — wrench-actuated valves for specific functions
- **Acoustic emergency disconnect** — last-ditch wireless trigger if all umbilical control is lost

## Stack height and weight

- **Lower stack alone**: typically 15-30 ft tall, 200-400 short tons
- **Full subsea stack (lower + LMRP)**: 35-60 ft tall, 400-700 short tons
- **HPHT 20K stacks**: heavier, taller; modern Gen 7+ drillships designed to lift these
- Drillship + semi-sub crane handling: designed for subsea-stack deployment via cursor system

## Public references

- **API Spec 16A** — [api-spec-16a.md](../standards/api-spec-16a.md)
- **API Spec 16D** — [api-spec-16d.md](../standards/api-spec-16d.md)
- **API Spec 16F** — [api-spec-16f.md](../standards/api-spec-16f.md)
- **API Spec 17D** — [api-spec-17d.md](../standards/api-spec-17d.md)
- **API RP 53** — [api-rp-53.md](../standards/api-rp-53.md)
- **API RP 16Q** — [api-rp-16q.md](../standards/api-rp-16q.md)

## Cross-references

- [Marine Drilling Riser Overview](marine-drilling-riser-overview.md), [Riser Tensioning](riser-tensioning.md), [Lower Marine Riser Package](lower-marine-riser-package.md), [Subsea Wellhead](subsea-wellhead.md)
- Phase 1 + 2: [BOP Stack Overview](bop-stack-overview.md), [BOP Control Systems](bop-control-systems.md), [Drillship](drillship.md), [Semi-Submersible Rig](semi-submersible-rig.md)
