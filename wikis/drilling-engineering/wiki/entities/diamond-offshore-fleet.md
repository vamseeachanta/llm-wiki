---
title: "Diamond Offshore Fleet"
tags: [drilling-contractor, diamond-offshore, semi-submersible, drillship]
sources:
  - iadc-drilling-manual
added: 2026-05-13
last_updated: 2026-05-13
---

# Diamond Offshore Fleet

## Scope

Public fleet stub for Diamond Offshore Drilling, Inc. Houston-headquartered offshore drilling contractor; historical fleet emphasis on harsh-environment semi-submersibles. Merged with Noble Corporation in 2024 (closed September 2024); operations continued under the combined entity post-merger.

## Fleet character

- Pre-merger: concentrated semi-submersible fleet covering ultra-deepwater (e.g., Ocean BlackHornet, Ocean BlackLion, Ocean GreatWhite class)
- Post-merger (2024+): fleet integrated into Noble Corporation's combined operations

## Public fleet reference

Pre-merger Diamond fleet reports archived on the corporate site; current rig dispositions reported via Noble Corporation public filings post-merger.

## Cross-references

- [Semi-Submersible Rig](../concepts/semi-submersible-rig.md), [Drillship](../concepts/drillship.md)
- [Noble Corporation Fleet](noble-corporation-fleet.md) — merger acquirer

## Data

Structured fleet data lives in [vamseeachanta/worldenergydata](https://github.com/vamseeachanta/worldenergydata):

- **Curated CSV** — [`data/modules/vessel_fleet/curated/drilling_rigs.csv`](https://github.com/vamseeachanta/worldenergydata/blob/main/data/modules/vessel_fleet/curated/drilling_rigs.csv). 2,211 rig rows; includes pre-2024-Q3 Diamond Offshore fleet under the OWNER='Diamond' label and post-merger entries that may carry OWNER='Noble' or compound labels reflecting the integrated entity.
- **Validation provenance** — [`docs/data/rig-fleet-website-validation.md`](https://github.com/vamseeachanta/worldenergydata/blob/main/docs/data/rig-fleet-website-validation.md). Diamond not separately validated 2026-02-13 (merger predated the WRK-104 sweep); post-merger fleet captured under [Noble Corporation](noble-corporation-fleet.md) scrape.
- **Filter for Diamond rigs** — `OWNER LIKE '%Diamond%'` for pre-2024-Q3 records; cross-check `(LAST_WAR_DATE < '2024-09-01' AND OWNER LIKE '%Diamond%')` for the merger-boundary cut. Vendor→curated merge tracked at [worldenergydata#127](https://github.com/vamseeachanta/worldenergydata/issues/127).

This stub is the knowledge-layer anchor for the pre-merger Diamond Offshore historical record; structured data lives in worldenergydata.

## Note

Diamond's reputation for harsh-environment semis is reflected in the Ocean Black / Ocean Great series rig names; those classes are captured in the curated CSV with their historical OWNER attribution.
