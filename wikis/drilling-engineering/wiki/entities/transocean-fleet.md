---
title: "Transocean Fleet"
tags: [drilling-contractor, transocean, semi-submersible, drillship, ultra-deepwater]
sources:
  - iadc-drilling-manual
added: 2026-05-13
last_updated: 2026-05-13
---

# Transocean Fleet

## Scope

Public fleet stub for Transocean Ltd. — historically the largest offshore drilling contractor by combined fleet capability. Headquartered in Steinhausen, Switzerland; rigs operate worldwide under flags of Liberia, Marshall Islands, and Vanuatu.

## Fleet character

- Concentrated in ultra-deepwater drillships and harsh-environment semi-submersibles
- Multiple Gen 6+ drillships rated for 12,000 ft water depth
- Harsh-environment Gen 7+ semis for North Sea, Norwegian Sea, Arctic operations

## Public fleet reference

Transocean publishes a fleet status page listing each rig with rated water depth, drilling-depth, contract status, and rig generation. Cite the operator's public fleet page when referencing specific rigs from this contractor.

## Cross-references

- [Semi-Submersible Rig](../concepts/semi-submersible-rig.md), [Drillship](../concepts/drillship.md)
- [MODU](../concepts/modu.md)

## Data

Structured fleet data lives in [vamseeachanta/worldenergydata](https://github.com/vamseeachanta/worldenergydata), the workspace-hub ecosystem's data corpus:

- **Curated CSV** — [`data/modules/vessel_fleet/curated/drilling_rigs.csv`](https://github.com/vamseeachanta/worldenergydata/blob/main/data/modules/vessel_fleet/curated/drilling_rigs.csv). 2,211 rig rows; schema: RIG_NAME, RIG_TYPE, OWNER, OPERATOR, IMO_NUMBER, FLAG_STATE, WATER_DEPTH_RATING_FT, DRILLING_DEPTH_RATING_FT, YEAR_BUILT, DP_CLASS, plus BSEE-WAR-linked activity columns. Base source: BSEE Well Activity Reports (US OCS). Last refresh 2026-05-05.
- **Validation provenance** — [`docs/data/rig-fleet-website-validation.md`](https://github.com/vamseeachanta/worldenergydata/blob/main/docs/data/rig-fleet-website-validation.md). 2026-02-13 site-by-site accessibility audit. Transocean validated at `deepwater.com/our-fleet/our-rigs` as Pass-1-scrapable (static HTML table, 26 rigs named, 26 image-based PDF spec sheets at `/documents/RigSpecs/{name}.pdf`).
- **Vendor scrape** — Transocean raw-scrape JSON pending capture; the scrape-target structure is documented in the validation doc.
- **Filter for Transocean rigs** — `OWNER LIKE '%Transocean%' OR OPERATOR LIKE '%Transocean%'` once vendor→curated merge lands (tracked at [worldenergydata#127](https://github.com/vamseeachanta/worldenergydata/issues/127)).

This stub is the **knowledge-layer anchor** for Transocean in llm-wiki — concept context (rig classes, MODU framework, harsh-environment scope) sits here. The **structured-data corpus is in worldenergydata** per the off-repo intel routing convention. Do not duplicate operator-fleet data into this CC-BY-4.0 wiki.

## Note

This entity stub deliberately does not list specific named rigs. Named-rig entity pages with citation to the operator's public fleet status are written as separate pages when ingested; do not reproduce vendor brochures, technical fact-sheets, or specifications verbatim into the wiki.
