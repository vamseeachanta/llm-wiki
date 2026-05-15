---
title: "Seadrill Fleet"
tags: [drilling-contractor, seadrill, jackup, semi-submersible, drillship]
sources:
  - iadc-drilling-manual
added: 2026-05-13
last_updated: 2026-05-13
---

# Seadrill Fleet

## Scope

Public fleet stub for Seadrill Limited. Hamilton, Bermuda-headquartered offshore drilling contractor; multiple Chapter 11 reorganizations (2017, 2021) reshaped the fleet substantially. Modern Seadrill operates a high-spec drillship and harsh-environment semi-submersible fleet.

## Fleet character

- West Polaris / West Tellus / West Capella class drillships
- Harsh-environment semis (West Hercules, West Aquarius)
- Jackup fleet (West-class, Sevan-class)

## Public fleet reference

Seadrill publishes a fleet status report covering current contracts, rated water depth, and rig generation. Cite the operator's public report when referencing specific rigs.

## Cross-references

- [Jackup Rig](../concepts/jackup-rig.md), [Semi-Submersible Rig](../concepts/semi-submersible-rig.md), [Drillship](../concepts/drillship.md)

## Data

Structured fleet data lives in [vamseeachanta/worldenergydata](https://github.com/vamseeachanta/worldenergydata):

- **Curated CSV** — [`data/modules/vessel_fleet/curated/drilling_rigs.csv`](https://github.com/vamseeachanta/worldenergydata/blob/main/data/modules/vessel_fleet/curated/drilling_rigs.csv). **48 rig rows, vendor-only, fully populated** (31 Noble + 17 Seadrill); refreshed 2026-05-14 via [worldenergydata#409](https://github.com/vamseeachanta/worldenergydata/pull/409). **All 17 Seadrill rigs from vendor scrape are now in this CSV** (West Polaris, West Capella, West Carina, West Gemini, West Jupiter, West Neptune, West Saturn, West Tellus, West Vela + Sonangol Libongos / Quenguela + Sevan Louisiana + West Aquarius / Eclipse / Phoenix + West Elara) with OWNER + RIG_TYPE classified by water depth.
- **Vendor scrape** — [`data/modules/vessel_fleet/raw/contractor_scrape/seadrill.json`](https://github.com/vamseeachanta/worldenergydata/blob/main/data/modules/vessel_fleet/raw/contractor_scrape/seadrill.json). 17 Seadrill rigs scraped 2026-02-13 via Puppeteer from `seadrill.com/fleet/` (Divi WordPress JS-rendered theme, requires headless Chrome). Card layout with explicit type labels (13 drillships including West Auriga / Capella / Carina / Gemini / Jupiter / Neptune / Polaris / Saturn / Tellus / Vela plus Sonangol Libongos and Quenguela JV; 3 semisubmersibles Sevan Louisiana + West Aquarius/Eclipse + West Phoenix; 1 jackup West Elara). 17 tech-sheet PDFs at `seadrill.com/wp-content/uploads/`. FSR PDF: `Seadrill-Fleet-Status-Report-August-6-2025-vF.pdf`.
- **Validation provenance** — [`docs/data/rig-fleet-website-validation.md`](https://github.com/vamseeachanta/worldenergydata/blob/main/docs/data/rig-fleet-website-validation.md).
- **Filter for Seadrill rigs** — `OWNER LIKE '%Seadrill%' OR OWNER LIKE '%Sonadrill%'` (the JV); vendor→curated merge tracked at [worldenergydata#127](https://github.com/vamseeachanta/worldenergydata/issues/127).

This stub is the knowledge-layer anchor for Seadrill; structured data lives in worldenergydata.

## Note

Specific named rigs filed as separate entity pages when ingested.
