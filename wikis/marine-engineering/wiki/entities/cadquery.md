---
title: "CadQuery"
tags: [cadquery, parametric-cad, python, geometry-generation, step-export, brep]
sources:
  - https://news.ycombinator.com/item?id=47772725
  - https://cadquery.github.io/
added: 2026-04-17
last_updated: 2026-04-17
domain: marine-engineering
cross_links:
  - engineering/entities/cadquery
  - engineering/sources/2026-04-17-hn-cadquery
---

# CadQuery (marine-engineering context)

**CadQuery** is a Python library for programmatic 3D CAD on the OpenCASCADE B-rep kernel. In marine and offshore engineering, its value is generating **parametric families of hardware** — fasteners, connectors, clumps, fairleads, mooring components, instrument housings — as STEP files, ready for meshing and downstream solver ingestion (AQWA, OrcaFlex, Abaqus, OpenFOAM).

## Why B-rep (not mesh) for offshore geometry

Panel methods (AQWA, WAMIT, OrcaWave) and high-fidelity CFD preprocessors want **exact curved surfaces**, not pre-discretized triangles. CadQuery emits STEP files containing trimmed NURBS/analytic surfaces, so:

- The meshing step is controlled separately (gmsh, Salome, commercial meshers) — you pick density by region without being trapped by authoring-time facets
- Watertightness properties of the solid propagate to the mesh
- Remesh-for-fatigue or remesh-for-ULS stays cheap, because the master geometry is parametric

## Candidate Offshore Applications

| Asset class | Parametric family | Why code-first wins |
|---|---|---|
| Mooring hardware | H-links, shackles, connectors, swivels | MBL-driven dimensioning, repeated across projects |
| Riser components | Buoyancy modules, bend stiffeners, end fittings | Geometry scales with ID/OD and VIV suppression design |
| Subsea structures | PLET, PLEM, manifold saddles | Batch generation across field layouts |
| Topside | Pipe supports, brackets, platform cleats | Swept families with minor variations |
| Instrumentation | Sensor pods, ROV-friendly housings | Ergonomic parametrics (hot-stab clearance, etc.) |

## Integration with Marine Solvers

```
CadQuery (Python, parametric)
    │
    ▼ STEP export
[gmsh / Salome / commercial mesher]
    │
    ▼ panel mesh / volume mesh
┌──────────────┬─────────────────┬──────────────────┐
│ AQWA QPPL DIFF│ OrcaWave        │ OpenFOAM / CFD   │
│ (RAOs, QTFs) │ (BEM diffraction)│ (wave, Morison)  │
└──────────────┴─────────────────┴──────────────────┘
```

For AQWA: remember the `QPPL DIFF` requirement (see [[AQWA Solver]] in engineering wiki) — the mesh density and element topology still matters; CadQuery doesn't remove the meshing craft, it just decouples it from the authoring step.

## Open Questions (tracked as GH issues)

- Does CadQuery output mesh quality acceptable for `QPPL DIFF` after a gmsh pass, or does panel topology need hand-tuning?
- Is build123d (sister library, same kernel) a better idiomatic fit for marine parametric families?
- Can the library approach replace any of the existing CAD-DEVELOPMENTS tooling for standardized marine hardware?

## Cross-References

- **Cross-wiki (engineering)**: [CadQuery entity](../../../engineering/wiki/entities/cadquery.md) — full entity page with API example, kernel discussion, LLM codegen notes
- **Cross-wiki (engineering source)**: [HN CadQuery thread](../../../engineering/wiki/sources/2026-04-17-hn-cadquery.md)
- **Related entity**: [[OrcaFlex VIV Analysis]](./orcaflex-viv-analysis.md)
- **Related concept**: [[Mooring Line Failure]](../concepts/mooring-line-failure.md) — parametric mooring hardware families motivate the tooling
