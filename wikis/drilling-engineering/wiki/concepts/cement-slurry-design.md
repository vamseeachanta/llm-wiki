---
title: "Cement Slurry Design"
tags: [cement, slurry-design, thickening-time, fluid-loss, compressive-strength, additives, retarder, accelerator]
sources:
  - api-rp-10b-2
added: 2026-05-13
last_updated: 2026-05-13
---

# Cement Slurry Design

## Scope

Engineering design of a cement slurry for a specific well section — base cement class, water ratio, weighting agents, additives (retarders, accelerators, fluid-loss control, dispersants, fluid-loss additives, gas-migration additives), and the resulting predicted thickening time, compressive strength, rheology, and fluid loss.

## Design dimensions

### Density

Target slurry density set by:
- Hydrostatic pressure requirement (kick prevention)
- Formation fracture-gradient limit (lost-circulation prevention)
- Typical range: 12 ppg (lightweight pozzolan) to 18 ppg (hematite-weighted)

### Thickening time

Time for slurry to remain pumpable (consistency < 70-100 Bc). Drives:
- **Lower bound** — must exceed total pumping + displacement time + safety margin (typically 1-2 hr)
- **Upper bound** — must not delay WOC (wait-on-cement) more than necessary

### Compressive strength development

Critical-strength threshold for casing-support typically ~500 psi. Operator's WOC time is set when slurry reaches this threshold (per UCA measurement during the cement job).

### Fluid loss

HTHP API RP 10B-2 fluid loss should be < 50 mL / 30 min for primary cementing of producing intervals; tighter limits for HPHT.

### Free water

Should be ≈ 0% for vertical and intermediate sections; non-zero free water risks channels and gas-migration paths.

## Additive families

- **Retarders** — lignosulfonates, organic acids; extend thickening time at high T
- **Accelerators** — calcium chloride, sodium silicate; shorten thickening time for shallow / cold wells
- **Fluid-loss additives** — synthetic polymers controlling filtrate volume
- **Dispersants** — reduce slurry rheology for low-pressure-loss displacement
- **Gas-migration additives** — reduce permeability development during setting
- **Lost-circulation materials (LCM)** — granular / fibrous; bridge formation fissures
- **Weighting agents** — barite, hematite (heavy); pozzolan, microspheres (light)

## Public references

- **API RP 10B-2** — [api-rp-10b-2.md](../standards/api-rp-10b-2.md)
- **Nelson & Guillot** 2006 — practitioner-canonical reference
- **Bourgoyne et al.** Ch. 3

## Cross-references

- [Cement Classes](cement-classes.md), [Primary Cementing](primary-cementing.md), [Cement Job Execution](cement-job-execution.md), [Cement Evaluation](cement-evaluation.md)
