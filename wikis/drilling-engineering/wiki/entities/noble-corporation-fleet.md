---
title: "Noble Corporation Fleet"
tags: [drilling-contractor, noble, jackup, drillship, harsh-environment]
sources:
  - iadc-drilling-manual
added: 2026-05-13
last_updated: 2026-05-13
---

# Noble Corporation Fleet

## Scope

Public fleet stub for Noble Corporation plc. Historically a leading harsh-environment jackup operator; expanded ultra-deepwater drillship fleet via the 2022 Maersk Drilling merger. Headquartered in Sugar Land, Texas.

## Fleet character

- Strong harsh-environment jackup presence (Noble Lloyd Noble and related HE class)
- Drillship fleet for ultra-deepwater work
- Post-Maersk-merger fleet covers North Sea, US Gulf, West Africa, South America, Asia

## Public fleet reference

Noble publishes a fleet specifications and contract status report. Cite the operator's public report when referencing specific rigs.

## Cross-references

- [Jackup Rig](../concepts/jackup-rig.md), [Drillship](../concepts/drillship.md)

## Data

Structured fleet data lives in [vamseeachanta/worldenergydata](https://github.com/vamseeachanta/worldenergydata):

- **Curated CSV** — [`data/modules/vessel_fleet/curated/drilling_rigs.csv`](https://github.com/vamseeachanta/worldenergydata/blob/main/data/modules/vessel_fleet/curated/drilling_rigs.csv). **48 rig rows, vendor-only, fully populated** (31 Noble + 17 Seadrill); refreshed 2026-05-14 via [worldenergydata#409](https://github.com/vamseeachanta/worldenergydata/pull/409). **All 31 Noble rigs from vendor scrape are now in this CSV** (Ocean Apex, BlackHawk, BlackHornet, BlackLion, Bob Douglas, Don Taylor, Sam Croft, Tom Madden, Faye Kozack, etc.) with full OWNER + RIG_DESIGN + WATER_DEPTH_RATING_FT + hull dimensions + PDF spec link.
- **Vendor scrape** — [`data/modules/vessel_fleet/raw/contractor_scrape/noble.json`](https://github.com/vamseeachanta/worldenergydata/blob/main/data/modules/vessel_fleet/raw/contractor_scrape/noble.json). 31 Noble rigs scraped 2026-02-13 via Puppeteer from `noblecorp.com/our-fleet` (Pass 1 HTTP 403, Pass 2 successful). Card-based grid with water depth, design, location, availability per rig; 28 individual spec PDFs at `s201.q4cdn.com`. Includes post-2022-Maersk-merger drillship fleet (BlackHawk, BlackHornet, BlackLion, BlackRhino, Bob Douglas, Don Taylor, Sam Croft, Tom Madden class) plus Faye Kozack, Stanley Lafosse (Samsung 96K), and the HE jackup line.
- **Validation provenance** — [`docs/data/rig-fleet-website-validation.md`](https://github.com/vamseeachanta/worldenergydata/blob/main/docs/data/rig-fleet-website-validation.md). Noble: 31 rigs named, 28 spec PDFs, per-rig detail pages at `noblecorp.com/our-fleet/fleet/fleet-details/2024/{name}/default.aspx`, FSR page at `noblecorp.com/investors/reports-and-filings/fleet-status-report/default.aspx`.
- **Filter for Noble rigs** — `OWNER LIKE '%Noble%'` plus post-merger former-Diamond fleet (`OWNER LIKE '%Diamond%'` pre-2024-Q3); vendor→curated merge tracked at [worldenergydata#127](https://github.com/vamseeachanta/worldenergydata/issues/127).

This stub is the knowledge-layer anchor for Noble; structured data lives in worldenergydata.

## Note

Specific named rigs filed as separate entity pages when ingested.
