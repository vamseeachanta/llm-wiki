---
title: "LNG Process Safety"
tags: [lng-projects, safety, vce, pool-fire, rollover]
added: 2026-05-03
last_updated: 2026-05-09
sources: []
see_also:
  - ../concepts/lng-storage-tanks.md
  - ../concepts/lng-regulatory-framework.md
---

# LNG Process Safety

## Scope

This page summarizes canonical LNG release and consequence categories used in process-safety hazard identification. It does **not** restate exclusion-zone formulas, dispersion model coefficients, or consequence-distance tables — those are jurisdiction-specific (NFPA 59A vs. EN 1473 use distinct deterministic vs. probabilistic methodologies) and are reserved for standards-page authoring.

## Key Concepts

- **Vapor cloud dispersion** — LNG vapor is initially denser than air at cryogenic temperature; warms to neutral or buoyant
- **Vapor cloud explosion (VCE)** — flammable cloud confined or congested ignition; magnitude depends on confinement and reactivity
- **Pool fire** — sustained combustion above a contained or unconfined LNG pool; thermal radiation governs separation distances
- **Rapid Phase Transition (RPT)** — physical (non-combustion) explosion when LNG contacts water and flashes
- **Rollover** — stratified-tank density inversion that releases boil-off vapor in excess of relief capacity
- **BLEVE** — boiling-liquid expanding-vapor explosion; less commonly cited for LNG than for LPG but referenced in some hazard surveys
- **LOPA / HAZOP / QRA** — canonical hazard-evaluation techniques applied across the project lifecycle

## Standards / References

- [NFPA 59A](../standards/nfpa-59a.md) — US-jurisdiction LNG process-safety primary standard (exclusion zones, deterministic methodology)
- [PHMSA 49 CFR 193](../standards/phmsa-49-cfr-193.md) — US LNG facility safety operations including incident reporting and operator-qualification rules
- [FERC 18 CFR 153](../standards/ferc-18-cfr-153.md) — US siting framework whose Resource Reports include cryogenic-design and safety review for export terminals
- EN 1473 — European LNG process-safety primary standard: <https://www.cencenelec.eu/>
- SIGTTO — industry guidance on liquefied-gas terminal safety: <https://www.sigtto.org/publications>

## Cross-References

- [LNG Storage Tanks](./lng-storage-tanks.md) — containment systems whose design is driven by these consequence categories
- [LNG Regulatory Framework](./lng-regulatory-framework.md) — standards bodies that codify safety distances
- **Cross-wiki (marine-engineering)**: [Process Safety](../../../marine-engineering/wiki/concepts/process-safety.md) -- similar slugs (88%); similar titles (88%); shared tags: safety; shared keywords: cross-references, explosion, fire, key, process
- **Cross-wiki (engineering-standards)**: [Brittle Fracture and the Brittle-Ductile Transition](../../../engineering-standards/wiki/concepts/brittle-fracture.md) — **bidirectional bridge**: cryogenic-failure-mode coverage on this page (cold-spill, RPT, rollover-driven thermal transients) defines the minimum design temperature (MDT) that the brittle-fracture / Charpy / `T₀` screening must clear for LNG inner tanks (9% Ni / ASTM A553), membrane systems (Invar), and process piping under EN 1473 and NFPA 59A.
- **Cross-wiki (engineering-standards)**: [ISO 15156 / NACE MR0175 — H2S Sour Service Materials](../../../engineering-standards/wiki/standards/iso-15156.md) — **bidirectional bridge**: LNG cargoes carry trace H2S below pipeline-specification thresholds, but ISO 15156 / NACE MR0175 still binds materials qualification for cargo-handling, reliquefaction, and BOG-treatment equipment because **H2S partial pressure** (not concentration) sets the sulfide-stress-cracking (SSC) and hydrogen-induced-cracking (HIC) regime. Most consequential for **9% Ni inner-tank welds (ASTM A553), Invar membrane attachments, and 22Cr/25Cr duplex / super-duplex cargo-handling components**: cryogenic-MDT material selection interacts with Pt 2 weld-zone hardness caps and Pt 3 CRA compositional / cold-work envelopes. BOG-amine sweetening and any sour-pocket cargo loading drive parallel sour-service exposure that must be cleared alongside the cryogenic envelope.
