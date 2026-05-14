---
title: "Cement Classes"
tags: [cement, class-a, class-b, class-c, class-g, class-h, pozzolan, hpht-cement]
sources:
  - api-spec-10a
added: 2026-05-13
last_updated: 2026-05-13
---

# Cement Classes

## Scope

The API Spec 10A cement-class system — eight base classes (A through H) plus special-purpose families — and the selection drivers that map a well to a class. Class G is the workhorse worldwide; Class H is common in US Gulf Coast; the others have specific applications.

## Class summary

| Class | Chemistry | Application |
|---|---|---|
| A | Portland-type | Shallow / low-temperature; rare today |
| B | Portland + sulfate resistance | Moderate / high sulfate environments |
| C | Higher fineness | High-early-strength applications |
| D, E, F | Retarded-set Portland | Moderate / high P-T; setting controlled by chemistry |
| G | Basic Portland, no accelerator / retarder built in | Workhorse — used with additives for full P-T envelope |
| H | Coarser-ground Class G equivalent | US Gulf Coast common; same flexibility as G |
| Pozzolan / fly-ash blended | Portland + reactive supplementary | HPHT, deep wells, salt-resistant |
| Silica-flour blended | Class G + silica flour | Above 230 °F to prevent compressive-strength retrogression |

## Selection drivers

- **Temperature** — drives retardation requirement and silica-flour need (> 230 °F downhole = silica flour mandatory)
- **Pressure** — drives required compressive strength and rheology
- **Formation type** — sulfate-bearing → Class B; lost-circulation zone → foamed cement
- **Operator-policy / regional convention** — Gulf Coast prefers H, North Sea prefers G, etc.

## Compressive-strength retrogression

Above ~230 °F, basic Class G/H cements undergo a chemical transformation that **reduces** compressive strength over time. Silica flour addition (~35% by weight of cement) prevents this. This is a critical HPHT design constraint.

## Public references

- **API Spec 10A** — [api-spec-10a.md](../standards/api-spec-10a.md)
- **Nelson & Guillot** (Schlumberger) — *Well Cementing* 2e 2006 (ISBN 978-0-9788930-0-9)
- **Bourgoyne et al.** Ch. 3 — cement chemistry overview

## Cross-references

- [Cement Slurry Design](cement-slurry-design.md), [Primary Cementing](primary-cementing.md), [Cement Job Execution](cement-job-execution.md), [Cement Evaluation](cement-evaluation.md)
