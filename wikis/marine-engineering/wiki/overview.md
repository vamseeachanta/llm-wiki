---
title: "Marine Engineering - Domain Overview"
type: overview
domain: marine-engineering
created: 2026-04-07 02:15 UTC
last_updated: 2026-05-06
---

# Marine Engineering - Domain Overview

This wiki covers offshore and marine engineering knowledge compiled from committed public Markdown metadata, authored synthesis pages, standards resolver metadata, product/reference source summaries, and incident-oriented seed material. The raw private/vendor source layer remains outside this public repository.

## Domain Scope

| Area | Coverage | Entities | Concepts | Key Sources |
|------|----------|----------|----------|-------------|
| Cathodic Protection | Galvanic and ICCP design | anode | cp-system, corrosion-control, coating-breakdown | [DNV-RP-B401] |
| Process Systems | Topsides equipment, safety | separator, compressor | process-safety, sour-service | [DNVGL-OS-E201] |
| Well Equipment | Float equipment, cementing | float-collar, float-shoe | - | [RB122/Halliburton] |
| Process Piping | Flanges, gaskets, fittings | flange, gasket | - | [Piping Components] |
| Mooring Engineering | LNG terminal mooring, failures | lng-carrier-mooring | long-period-swell-resonance, mooring-line-failure | [Mooring Failures] |
| Station-Keeping and Motions | Floating-unit offsets, RAOs, mooring, DP, spread mooring | fpso, flng, semisubmersible, spar, tlp | station-keeping, motions-rao, dynamic-positioning, spread-mooring | [DNV-OS-E301] |
| Floating Platforms | Production, drilling, construction, and fixed-platform entity coverage | fpso, flng, semisubmersible, spar, jack-up, tlp, jacket | stability-in-waves | [DNV-RP-C205] |

## Current Statistics (committed repo snapshot, 2026-05-06)

| Metric | Value |
|--------|-------|
| Source-summary pages | 19,166 |
| Entity pages | 22 |
| Concept pages | 19 |
| Comparison pages | 1 |
| Standards template pages | 1 |
| Total markdown pages under `wiki/` | 19,213 |

## Key Standards Referenced

- **DNV-RP-B401**: Cathodic Protection Design
- **DNVGL-OS-E201**: Oil and Gas Processing Systems
- **NACE MR0175**: Materials for H2S environments
- **ASME B16.5**: Flange standards
- **DNV-OS-E301**: Position mooring and station-keeping design basis
- **DNV-RP-C205**: Environmental conditions and environmental loads

## Key Incident Data

- **NWS LNG 2014**: 3 lines parted in ~50mm swell (resonance)
- **18 mooring failure incidents** across LNG terminals and ports worldwide
- **Industry-wide HMPE failure pattern** (2007-2011)
- **2 fatalities** (Ansac Splendor, 2018)

## Current Expansion Priorities

- Continue converting source-heavy areas into curated concept/entity navigation pages.
- Add standards resolver pages only when public revision metadata is independently verified.
- Keep raw PDFs, vendor standards, private archives, and project-sensitive source material outside git.
- Use [Domain portal](portal.md) for faceted navigation through the large source-summary layer.

## Cross-Wiki Linking

- Links to: [engineering](../../engineering/wiki/index.md) for solvers, standards-routing pages, calculation methodology, and offshore engineering concepts.
- Links to: [engineering-standards](../../engineering-standards/wiki/index.md) for metadata-only standards resolver pages.
- Links to: [naval-architecture](../../naval-architecture/wiki/index.md) for hydrostatics, ship stability, and seakeeping concepts.
- Links to: [lng-projects](../../lng-projects/wiki/index.md) for LNG project/domain pages.

[DNV-RP-B401]: sources/dnv-rp-b401-cathodic-protection.md "DNV RP B401"
[DNVGL-OS-E201]: sources/dnvgl-os-e201-oil-gas-processing.md "DNVGL OS-E201"
[RB122/Halliburton]: sources/rb122-float-equipment.md "Halliburton RB122"
[Piping Components]: sources/piping-components-ebook.md "Piping Components Reference"
[Mooring Failures]: sources/mooring-failures-lng-terminals.md "Mooring Failures at LNG Terminals"
[DNV-OS-E301]: ../../../engineering-standards/wiki/standards/dnv-os-e301.md "DNV OS E301"
[DNV-RP-C205]: ../../../engineering-standards/wiki/standards/dnv-rp-c205.md "DNV RP C205"
