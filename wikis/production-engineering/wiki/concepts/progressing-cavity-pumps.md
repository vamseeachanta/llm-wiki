---
title: "Progressing-Cavity Pumps (PCP)"
tags: [pcp, progressing-cavity, artificial-lift, helical-rotor, elastomer-stator]
sources:
  - api-spec-11w
added: 2026-05-14
last_updated: 2026-05-14
---

# Progressing-Cavity Pumps (PCP)

## Scope

The PCP is a downhole helical-screw positive-displacement pump. A metal helical rotor (typically single-helix) turns inside a double-helix elastomeric stator with a fixed interference fit; the two surfaces create a chain of sealed cavities that progress from intake to discharge as the rotor rotates. PCP is the **niche method for high-viscosity and high-solids service** — neither ESP nor rod pump handles those well, but PCP excels.

## Two surface configurations

### Surface-driven PCP (most common)

- Drive motor at surface; long rotating rod string transmits torque downhole
- Rod string spins at 100-500 RPM
- Surface unit: motor + drive head + sheave (or direct-drive); polished-rod equivalent for stuffing-box seal at wellhead
- Most installations are this type

### Electric submersible PCP (ESPCP)

- Downhole electric motor (similar to ESP) turns rotor directly
- No rotating rod string → no rod-wear; works in highly deviated and horizontal wells
- Higher CAPEX than surface-driven; specialty application

## Operating envelope

- **Rate**: < 4,000 bbl/d typical
- **Depth**: < 8,000 ft (deeper for ESPCP)
- **Fluid viscosity**: tolerates very high viscosity (advantage over ESP)
- **Solids**: tolerates sand-bearing production (advantage over ESP and rod pump)
- **Free gas**: moderate tolerance (better than ESP, worse than gas lift)

## Strengths and weaknesses

| Strength | Weakness |
|---|---|
| Excellent for heavy oil | Elastomer chemistry limits service envelope (see [PCP Elastomer Chemistry](pcp-elastomer-chemistry.md)) |
| Excellent for sand-producing wells | Depth-limited (rod-string fatigue for surface-driven) |
| Lower CAPEX than ESP | Slower rate ramp than ESP (limited RPM range) |
| Continuous low-shear operation (gentle on viscous fluid) | Sensitivity to dry-running (no fluid → elastomer overheats) |

## Cross-references

- [PCP Elastomer Chemistry](pcp-elastomer-chemistry.md), [PCP Heavy-Oil Application](pcp-heavy-oil-application.md)
- [API Spec 11W](../standards/api-spec-11w.md)
- [Artificial Lift Overview](artificial-lift-overview.md)

## Public references

- **Brown, Kermit E.** *Technology of Artificial Lift Methods* Vol 2b, PennWell 1980 (ISBN 0-87814-031-X) — PCP chapter
- **Lyons handbook** PCP section
- **SPE OnePetro PCP literature** — heavy-oil case studies, elastomer-failure patterns
- **API Spec 11W**
