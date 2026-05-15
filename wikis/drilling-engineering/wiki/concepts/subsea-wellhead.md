---
title: "Subsea Wellhead"
tags: [subsea-wellhead, casing-hanger, lockdown-ring, 18-3-4-wellhead, mudline-hanger]
sources:
  - api-spec-17d
added: 2026-05-14
last_updated: 2026-05-14
---

# Subsea Wellhead

## Scope

The subsea wellhead is the load-bearing connection between the well's casing strings, the BOP stack during drilling, and (post-completion) the production Christmas tree. It sits on the seabed (or just below in a temporarily-covered well) and provides the wellbore-pressure-containment + casing-support function. Drilling-engineering scope is the drilling-side perspective (casing hangers, lockdown, test plugs); the Christmas-tree side crosses into future production-engineering scope.

## The 18-3/4" wellhead family

The dominant subsea wellhead OD is **18-3/4 inches** — sized to fit inside a 26" or 30" structural conductor pipe. Casing strings of successively smaller OD (typically 36" → 20" → 13-3/8" → 9-5/8" → 7") hang from inside the wellhead, with each hanger landing on the shoulder below it.

## Casing hanger anatomy

1. Each casing string runs from depth to the wellhead
2. The casing hanger (a wedge-shaped collet or split-ring) lands on a shoulder in the wellhead housing
3. Lockdown ring or auto-lock dogs engage to prevent the hanger from lifting under differential pressure
4. The next outer-casing-string runs to its setting depth + cement + hangs from the same wellhead at a shoulder above

## Lockdown ring design

Differential pressure (high inside the well, lower outside) can lift the hanger if it's not locked. Lockdown rings are engaged via either:

- **Mechanical actuation** — hex-key turn applied via running tool
- **Hydraulic actuation** — pressurization via wellbore-internal line

Lockdown ratings typically 1.5-2× working pressure as safety factor.

## Drilling vs production wellhead

- **During drilling**: BOP stack lands on the wellhead; high-pressure during well-control
- **Post-completion**: BOP removed, Christmas tree installed on top of the same wellhead; production fluid flows through tree to the umbilical / flowline

The wellhead is a long-life component (20-40 years); the BOP and tree above it change with the well's lifecycle.

## Cross-references

- [API Spec 17D](../standards/api-spec-17d.md)
- [Subsea BOP Stack Architecture](subsea-bop-stack-architecture.md), [Lower Marine Riser Package](lower-marine-riser-package.md), [Marine Drilling Riser Overview](marine-drilling-riser-overview.md)
- Phase 1 + 2 cross-refs: [BOP Stack Overview](bop-stack-overview.md), [Casing Program Design](casing-program-design.md)

## Public references

- **API Spec 17D** — [api-spec-17d.md](../standards/api-spec-17d.md)
- **Bourgoyne et al.** Chapter 1 (rig overview includes subsea wellhead)
- **Vendor docs** (Cameron, FMC Technologies, GE Aker Solutions, NOV Drilquip) — consulted at design time; not transcribed
