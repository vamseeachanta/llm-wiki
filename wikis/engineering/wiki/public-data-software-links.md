---
title: "Engineering Public Data and Software Links"
added: 2026-05-11
last_updated: 2026-05-11
type: reference-index
tags: [engineering, data, software, provenance, public-safe]
sources:
  - ../../cross-links-tier1.md
  - ../../../docs/reports/2026-05-11-tier1-ecosystem-link-map.md
---

# Engineering Public Data and Software Links

This page connects engineering wiki concepts to public data provenance and reusable software surfaces. It is not a data extract and contains no private row-level records.

## Data provenance anchors

| Topic | Authoritative target | Wiki use |
|---|---|---|
| Energy module inventory | [worldenergydata](https://github.com/vamseeachanta/worldenergydata) `MODULE_INDEX.md` | Discover public energy-data modules. |
| Local data pattern | [worldenergydata](https://github.com/vamseeachanta/worldenergydata) `docs/data/LOCAL_DATA_PATTERN.md` | Explain why raw/local stores are not copied into wiki. |
| Two-tier data governance | [worldenergydata](https://github.com/vamseeachanta/worldenergydata) `docs/data/TWO_TIER_DATA.md` | Distinguish reproducible public data from private/local caches. |
| Available data sources | [worldenergydata](https://github.com/vamseeachanta/worldenergydata) `docs/data-sources/AVAILABLE_DATA_SOURCES.md` | Link source registries rather than embedding datasets. |
| BSEE knowledge base | [worldenergydata](https://github.com/vamseeachanta/worldenergydata) `docs/knowledge-base/bsee/README.md` | Provenance for offshore energy data pages. |
| FDAS validation | [worldenergydata](https://github.com/vamseeachanta/worldenergydata) `docs/modules/fdas/VALIDATION-REPORT.md` | Link checked validation reports for economics workflows. |

## Software utility anchors

| Topic | Authoritative target | Wiki use |
|---|---|---|
| Utility routing | [assetutilities](https://github.com/vamseeachanta/assetutilities) `docs/maps/assetutilities-operator-map.md` | Route reusable extraction/reporting utilities. |
| Report generation | [assetutilities](https://github.com/vamseeachanta/assetutilities) `src/assetutilities/common/reportgen/` | Link report-generation backing code. |
| Units | [assetutilities](https://github.com/vamseeachanta/assetutilities) `src/assetutilities/units/` | Link unit-handling implementation. |
| YAML utilities | [assetutilities](https://github.com/vamseeachanta/assetutilities) `src/assetutilities/common/yml_utilities.py` | Link configuration parsing support. |

## Exposure contract

When promoting a data-heavy page, use a public source URL, a repo-relative script/doc path, an issue link, and a safety note. Do not include raw private dumps, full local archive paths, sensitive row-level records, or vendor/client content.
