---
title: "Helmerich & Payne FlexRig"
tags: [drilling-contractor, helmerich-payne, h-p, flexrig, land-rig, pad-drilling, ac-drive]
sources:
  - iadc-drilling-manual
added: 2026-05-13
last_updated: 2026-05-13
---

# Helmerich & Payne FlexRig

## Scope

Public entity stub for Helmerich & Payne, Inc.'s FlexRig product family — the canonical modern North American pad-drilling rig class. H&P is the dominant US land-rig contractor by AC-drive high-spec rig count; FlexRig has become the industry archetype for modern unconventional / shale pad drilling.

## FlexRig class characteristics

- **AC-drive** — variable-frequency-driven AC motors on drawworks and mud pumps (replaces older DC / mechanical drives)
- **Walking system** — hydraulic skid mechanism allowing the rig to walk 20-60 ft between wellheads on a multi-well pad without rig-down
- **Substructure** — fast-erect hydraulic raise; significantly faster rig-up than legacy box-on-box
- **Class subtypes** — multiple FlexRig generations (FlexRig 3, FlexRig 4, FlexRig 5) with progressively higher hookload, deeper-rated, larger top-drive
- **Hookload rating** — 750,000 to 1,500,000+ lbf depending on subtype

## Why this entity matters

FlexRig is the canonical example of how rig-spec drives downstream well-economics in unconventional plays: AC-drive precision enables higher ROP / steerable directional control; walking system reduces rig-move time from days to hours, compressing well-cost. The Papkov AI-tender-evaluation use case implicitly requires modeling these capability dimensions — see [Papkov founding source](../sources/papkov-2026-drilling-tender-ai-agent.md).

## Public reference

H&P fleet status and FlexRig family specifications published on the corporate site. Specific FlexRig units have rig numbers (HP-XXX); cite the operator's public listing when referencing specific units.

## Cross-references

- [Land Rig](../concepts/land-rig.md)
- [Rig Classes Overview](../concepts/rig-classes-overview.md)

## Data

Structured rig-fleet data lives in [vamseeachanta/worldenergydata](https://github.com/vamseeachanta/worldenergydata) — but with **scope-edge caveats** for H&P:

- **Curated CSV** — [`data/modules/vessel_fleet/curated/drilling_rigs.csv`](https://github.com/vamseeachanta/worldenergydata/blob/main/data/modules/vessel_fleet/curated/drilling_rigs.csv). **48 rig rows, vendor-only, fully populated** (31 Noble + 17 Seadrill; refreshed 2026-05-14 via [worldenergydata#409](https://github.com/vamseeachanta/worldenergydata/pull/409)). **H&P units NOT in the current CSV** — H&P is dominantly a US land-rig contractor (~203 US rigs, 131 international) and the validation doc found `hpinc.com/rig-fleet/flexrig-fleet` only publishes FlexRig **model**-specs (3 model classes), not per-unit listings. Land-rig coverage gap requires state-RRC ingest path ([worldenergydata#127 WRK-1204](https://github.com/vamseeachanta/worldenergydata/issues/127)).
- **Validation provenance** — [`docs/data/rig-fleet-website-validation.md`](https://github.com/vamseeachanta/worldenergydata/blob/main/docs/data/rig-fleet-website-validation.md). H&P validated 2026-02-13: `hpinc.com/rig-fleet/flexrig-fleet` is a tabbed FlexRig **model**-specification page (3 model classes) — individual unit-level rig names are **not** published online (typical for land-rig contractors with hundreds of near-identical units). 1 fact sheet PDF.
- **Filter for H&P rigs** — `OWNER LIKE '%Helmerich%'` or `OWNER LIKE '%H&P%'` in the curated CSV; expect sparse offshore coverage. Land-rig coverage needs a state-railroad-commission ingest path (Texas RRC, NDIC, COGCC) — exactly the scope of [worldenergydata#127 WRK-1204](https://github.com/vamseeachanta/worldenergydata/issues/127).

The FlexRig **class** content (the archetype description above) is the load-bearing content of this stub; per-unit detail for H&P specifically is data-gap-by-vendor-design and will be sparse until the state-RRC ingest lands.

## Note

This is a **class-archetype entity** rather than a contractor-fleet entity in the offshore sense — H&P's value to the corpus is the FlexRig product family as the canonical pad-drilling rig design, not per-unit specifications.
