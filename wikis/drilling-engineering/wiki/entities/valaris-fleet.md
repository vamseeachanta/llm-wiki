---
title: "Valaris Fleet"
tags: [drilling-contractor, valaris, jackup, semi-submersible, drillship]
sources:
  - iadc-drilling-manual
added: 2026-05-13
last_updated: 2026-05-13
---

# Valaris Fleet

## Scope

Public fleet stub for Valaris Limited (formed 2019 by merger of Ensco and Rowan; emerged from Chapter 11 reorganization in 2021). Headquartered in Hamilton, Bermuda. Diversified fleet across jackups, semi-submersibles, and drillships — one of the larger globally diversified contractors.

## Fleet character

- Sizable jackup fleet across all major regions (US Gulf, North Sea, Middle East, West Africa, Asia-Pacific)
- DS-7 / DS-8 / DS-9 / DS-12 / DS-15 / DS-16 ultra-deepwater drillship class
- Harsh-environment jackups for North Sea operations

## Public fleet reference

Valaris publishes a fleet status report listing each rig with rated water depth, drilling-depth, contract status. Cite the operator's public report when referencing specific rigs.

## Cross-references

- [Jackup Rig](../concepts/jackup-rig.md), [Semi-Submersible Rig](../concepts/semi-submersible-rig.md), [Drillship](../concepts/drillship.md)

## Data

Structured fleet data lives in [vamseeachanta/worldenergydata](https://github.com/vamseeachanta/worldenergydata):

- **Curated CSV** — [`data/modules/vessel_fleet/curated/drilling_rigs.csv`](https://github.com/vamseeachanta/worldenergydata/blob/main/data/modules/vessel_fleet/curated/drilling_rigs.csv). **48 rig rows, vendor-only, fully populated** (31 Noble + 17 Seadrill); refreshed 2026-05-14 via [worldenergydata#409](https://github.com/vamseeachanta/worldenergydata/pull/409), replacing the prior 2,211-row BSEE-WAR baseline. **Valaris rigs not yet in this CSV** — sub-page scrape pending per validation doc; FSR PDF parse is the alternative path.
- **Validation provenance** — [`docs/data/rig-fleet-website-validation.md`](https://github.com/vamseeachanta/worldenergydata/blob/main/docs/data/rig-fleet-website-validation.md). Valaris validated 2026-02-13: `valaris.com/our-fleet` is a category landing page only; sub-pages at `our-fleet/drillships`, `our-fleet/semisubmersibles`, `our-fleet/jackups` need separate scrape. FSR PDF at `s23.q4cdn.com/956522167/files/doc_downloads/2025/10/10232025-Fleet-Status-Report_FINAL.pdf` is the canonical bulk source.
- **Vendor scrape** — Valaris sub-page scrape pending; FSR PDF parse is the alternative path.
- **Filter for Valaris rigs** — `OWNER LIKE '%Valaris%' OR OWNER LIKE '%Ensco%' OR OWNER LIKE '%Rowan%'` (legacy pre-2019-merger names also appear in BSEE WARs); vendor→curated merge tracked at [worldenergydata#127](https://github.com/vamseeachanta/worldenergydata/issues/127).

This stub is the knowledge-layer anchor for Valaris; structured data lives in worldenergydata per the off-repo intel routing convention.

## Note

Specific named rigs filed as separate entity pages when ingested with citation to operator's public report.
