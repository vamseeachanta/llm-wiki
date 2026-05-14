---
title: "Cement Evaluation"
tags: [cement-evaluation, cbl, vdl, segmented-bond, cement-bond-log, ultrasonic-cement]
sources:
  - api-spec-10a
added: 2026-05-13
last_updated: 2026-05-13
---

# Cement Evaluation

## Scope

Post-WOC techniques for evaluating cement-job quality — verifying that the cement reached planned top-of-cement (TOC), that it bonded to casing and formation, and that no channels or annular gas migration compromise zonal isolation. The diagnostic counterpart to the [primary cementing](primary-cementing.md) job and the bridge to FIT/LOT at the new shoe.

## Evaluation tool families

### Cement Bond Log (CBL)

- Acoustic tool measuring sonic-wave amplitude across the cemented annulus
- High amplitude = poor bond (or no cement, free pipe)
- Low amplitude = good bond
- Single-receiver tool; provides bulk indication but not azimuthal detail

### Variable Density Log (VDL)

- Companion display to CBL; full waveform amplitude vs time
- Visualizes the formation-arrival signal; helps distinguish casing-bond from formation-bond

### Segmented bond tools

- **Segmented bond tool (SBT)** — multiple pad-mounted sensors around casing circumference
- **Ultrasonic cement evaluation tool (USIT, CAST-V, Isolation Scanner)** — high-frequency ultrasound; azimuthal resolution; distinguishes solid cement / liquid / gas behind casing

### Cement integrity verification

- **Pressure test** after WOC; pressure-up casing to test cement seal
- **Inflow / negative pressure test** — reduce pressure inside casing, verify no flow from formation
- **FIT / LOT** at new shoe — formation-strength verification (also confirms cement seal)

## What good cement evaluation looks like

- TOC at or above planned depth
- Continuous bond signature (low CBL amplitude, ultrasonic indication of solid cement) across critical zones
- No channels in azimuthal segmented data
- Successful pressure test
- Successful FIT or LOT

## When evaluation fails

- TOC below planned — top-up cement job ("top job" / squeeze)
- Channels or free water — remedial cement squeeze through casing perforations
- Severely poor bond — abandon section, re-run smaller casing inside

## Public references

- **API Spec 10A** — [api-spec-10a.md](../standards/api-spec-10a.md)
- **Nelson & Guillot** 2006 — cement-evaluation chapter
- **Bourgoyne et al.** Ch. 3

## Cross-references

- [Primary Cementing](primary-cementing.md), [Cement Job Execution](cement-job-execution.md), [Cement Slurry Design](cement-slurry-design.md), [Cement Classes](cement-classes.md)
- [Casing Shoe Track](casing-shoe-track.md) — FIT/LOT pressure test confirms cement quality at new shoe
