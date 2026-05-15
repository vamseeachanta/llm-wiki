---
title: "Noble Lloyd Noble"
tags: [noble-corporation, jackup, harsh-environment, north-sea, he-class]
sources:
  - iadc-drilling-manual
added: 2026-05-14
last_updated: 2026-05-14
---

# Noble Lloyd Noble

## Scope

Specific named rig entity for **Noble Lloyd Noble** — a flagship harsh-environment jackup from Noble Corporation's fleet, designed for North Sea HE service. Part of the Noble HE jackup line.

## Public spec summary

(Paraphrased from Noble Corp's public fleet status at noblecorp.com/our-fleet)

- **Contractor**: Noble Corporation
- **Rig class**: Jackup (harsh-environment)
- **Operating area**: North Sea typical
- **HE classification**: heavy-leg, deeper-water-rating, winterized
- **Year**: built mid-2010s (verify)

## worldenergydata cross-link

- Should appear in current curated CSV from Noble vendor scrape ([noble.json](https://github.com/vamseeachanta/worldenergydata/blob/main/data/modules/vessel_fleet/raw/contractor_scrape/noble.json) → spec_details parquet → curated CSV via PR #409)
- Filter: `RIG_NAME LIKE '%Lloyd Noble%' OR RIG_NAME LIKE '%Noble Lloyd%'` AND `OWNER LIKE '%Noble%'`

## Cross-references

- Parent: [Noble Corporation Fleet](noble-corporation-fleet.md)
- Concept: [Jackup Rig](../concepts/jackup-rig.md), [Rig Classes Overview](../concepts/rig-classes-overview.md)
