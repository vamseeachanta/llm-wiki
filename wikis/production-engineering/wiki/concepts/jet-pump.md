---
title: "Jet Pump"
tags: [jet-pump, artificial-lift, hydraulic-lift, venturi, throat-nozzle-ratio, cavitation]
added: 2026-05-14
last_updated: 2026-05-14
---

# Jet Pump

## Scope

The jet pump is a downhole Venturi-style mixer with **no moving parts**. High-pressure power fluid (clean produced fluid or supplied liquid) is pumped down a parallel string to the pump, where it accelerates through a nozzle, creating a low-pressure region that draws in produced fluid through the throat. The combined mixed stream then decelerates through a diffuser, regaining pressure, and returns to surface through the production tubing.

## Components (downhole, all stationary)

- **Power-fluid inlet** — power fluid arrives from surface via a parallel string
- **Nozzle** — fixed-geometry orifice; power fluid accelerates to high velocity here
- **Throat** — mixing region; produced fluid enters by suction; mixes with power fluid
- **Diffuser** — gradually expanding section converting velocity back to pressure
- **Mixed-stream outlet** — combined power + produced fluid returns to surface

## Throat-to-nozzle ratio

The **throat-area / nozzle-area ratio** is the single most important design parameter:

- **Low ratio (close to 1)** — high pressure rise, low rate
- **High ratio (3-5)** — lower pressure rise, higher rate
- Selection driven by well's pressure-rate operating point

## Cavitation envelope

If the produced-fluid pressure at the throat inlet drops below the fluid's vapor pressure, vapor bubbles form (cavitation) — they collapse violently in the diffuser, causing erosion and noise + flow disruption. The cavitation-free operating envelope is the load-bearing design constraint.

## Operating envelope

- **Rate**: 200-15,000 bbl/d
- **Depth**: works in deep wells (> 15,000 ft); favored where ESP would be at depth-limit
- **Free-gas tolerance**: moderate (better than ESP, worse than gas lift)
- **Solids tolerance**: moderate (no moving parts is the advantage, but throat erosion happens)

## Strengths and weaknesses

| Strength | Weakness |
|---|---|
| No moving downhole parts (long MTBF) | Surface power-fluid system adds complexity |
| Works at very-deep wells where ESP fails | Lower overall efficiency than ESP at design point |
| Tolerant of moderate solids and gas | Cavitation is a real operational hazard |
| Stationary downhole — easy to retrieve/replace | Power-fluid contamination (sand, scale) damages nozzle |

## Cross-references

- [Hydraulic Piston Pump](hydraulic-piston-pump.md), [Power Fluid Systems](power-fluid-systems.md)
- [Artificial Lift Overview](artificial-lift-overview.md)
- Drilling-engineering cross-link: [Coiled Tubing Overview](../../../drilling-engineering/wiki/concepts/coiled-tubing-overview.md) — jet pumps are sometimes deployed via CT for short-duration intervention

## Public references

- **Brown, Kermit E.** *The Technology of Artificial Lift Methods*, Vol 2b, PennWell 1980 — jet-pump chapter
- **Lyons handbook** — artificial-lift section
- **SPE OnePetro jet-pump literature** — efficiency optimization, deep-well case studies
