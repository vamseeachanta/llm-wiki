---
title: "Cement Job Execution"
tags: [cementing, cementing-unit, batch-mixer, displacement-pump, halliburton, schlumberger]
sources:
  - api-spec-10a
added: 2026-05-13
last_updated: 2026-05-13
---

# Cement Job Execution

## Scope

The surface equipment and procedural execution of a primary cement job — cementing-unit configuration, batch mixing, pumping schedule, plug release and displacement. The operational counterpart to [primary-cementing.md](primary-cementing.md).

## Surface equipment

### Cementing unit

A self-contained skid (truck-mounted on land, modular skid on offshore rigs) carrying:
- Triplex positive-displacement pumps (typically 2 in redundant configuration)
- Centrifugal mixing pump
- Recirculating mixer (jet mixer or batch mixer)
- Density / rate / pressure instrumentation
- Computerized control system

### Batch mixer

For pre-blending cement and additives in a known volume before main job:
- Reduces variability in density and consistency
- Useful for HPHT, long jobs, critical applications
- Slower than continuous mixing

### Continuous mixing

Cement and water blended at the jet mixer in real time; faster but more variable

## Pumping schedule

A pumping schedule pre-computed by cementing engineer:

1. Spacer volume + flow rate
2. Lead cement volume + flow rate
3. Tail cement volume + flow rate
4. Plug release timing
5. Displacement fluid (usually mud) volume

Operator watches density and pressure traces in real time against the planned schedule. Deviations trigger immediate decision: continue, slow down, abort.

## Bottom and top plugs

- **Bottom plug** released before cement; wipes mud off casing ID ahead of cement column
- **Top plug** released after cement; wipes cement off casing ID behind cement column; lands on landing collar to signal end-of-displacement

## Public references

- **API Spec 10A** — [api-spec-10a.md](../standards/api-spec-10a.md)
- **Nelson & Guillot** 2006 — cementing-unit and job-execution chapters
- **Bourgoyne et al.** Ch. 3

## Cross-references

- [Primary Cementing](primary-cementing.md), [Cement Slurry Design](cement-slurry-design.md), [Cement Evaluation](cement-evaluation.md), [Cement Classes](cement-classes.md)
