---
title: "Tier-1 Code/Data/Results Cross-Links"
created: 2026-05-11
last_updated: 2026-05-11
type: cross-link-index
tags: [tier-1, provenance, results, public-safe]
public_safety: public links and repository-relative targets only
sources:
  - docs/reports/2026-05-11-tier1-ecosystem-link-map.md
  - docs/reports/2026-05-11-tier1-practical-completeness-gap-report.md
---

# Tier-1 Code/Data/Results Cross-Links

This index adds the practical code/data/results layer beside the existing domain-to-domain wiki links. It is link-only: it points to public repositories, repository-relative files, checked-in reports, and public issue anchors without copying raw data, vendor standards text, client deliverables, or private GTM material.

## Engineering Methods → digitalmodel

| Wiki domain | Wiki topic | Repo | Target | Layer | Public-safety note |
|---|---|---|---|---|---|
| marine-engineering | OrcaFlex, OrcaWave, hydrodynamics, mooring, subsea workflows | [digitalmodel](https://github.com/vamseeachanta/digitalmodel) | `docs/maps/digitalmodel-operator-map.md` | Software | Link implementation docs only; no client models. |
| marine-engineering | GTM demo reports and engineering proof artifacts | [digitalmodel](https://github.com/vamseeachanta/digitalmodel) | `examples/demos/gtm/README.md` and `examples/demos/gtm/output/` | Results | Link only public-safe demo outputs. |
| engineering-standards | Fatigue, cathodic protection, wall thickness, on-bottom stability, FFS/API 579 | [digitalmodel](https://github.com/vamseeachanta/digitalmodel) | `docs/domains/` and standards-backed examples | Software/Results | Link implementation and validation artifacts; do not quote standards clauses. |

## Data Sources → worldenergydata

| Wiki domain | Wiki topic | Repo | Target | Layer | Public-safety note |
|---|---|---|---|---|---|
| engineering | BSEE, SODIR, USCG, marine safety, FDAS/economics | [worldenergydata](https://github.com/vamseeachanta/worldenergydata) | `docs/data-sources/AVAILABLE_DATA_SOURCES.md` | Data | Prefer public-source provenance and data dictionaries. |
| engineering | Two-tier data governance and local data pattern | [worldenergydata](https://github.com/vamseeachanta/worldenergydata) | `docs/data/TWO_TIER_DATA.md` | Governance/Data | Do not publish raw private dumps or row-level sensitive records. |

## Utility/Extraction Stack → assetutilities

| Wiki domain | Wiki topic | Repo | Target | Layer | Public-safety note |
|---|---|---|---|---|---|
| engineering | YAML utilities, file management, report generation, visualization, units | [assetutilities](https://github.com/vamseeachanta/assetutilities) | `docs/maps/assetutilities-operator-map.md` and `src/assetutilities/common/` | Software | Link reusable utilities; do not vendor source into wiki pages. |
| engineering-standards | Metadata-only scanners and report builders | [assetutilities](https://github.com/vamseeachanta/assetutilities) | `docs/HTML_REPORTING_STANDARDS.md` | Results/Governance | Use for report conventions and validation, not raw-source publication. |

## Asset Lifecycle → assethold

| Wiki domain | Wiki topic | Repo | Target | Layer | Public-safety note |
|---|---|---|---|---|---|
| asset-management | Portfolio, lifecycle, risk metrics, daily strategy methods | [assethold](https://github.com/vamseeachanta/assethold) | `docs/api/index.md` | Software | Keep private holdings/account details out. |
| asset-management | Backtesting and generic asset-lifecycle methodology | [assethold](https://github.com/vamseeachanta/assethold) | `docs/backtesting.md` | Results/Software | Treat as generic method context, not investment advice. |

## Public Results/Demos → aceengineer-website

| Wiki domain | Wiki topic | Repo | Target | Layer | Public-safety note |
|---|---|---|---|---|---|
| marine-engineering | Freespan, wall thickness, mudmat, pipelay, jumper, mooring demos | [aceengineer-website](https://github.com/vamseeachanta/aceengineer-website) | `content/demos/` and `content/case-studies/` | Results | Prefer deployed public URLs when confirmed. |
| engineering | Calculators and public engineering explainers | [aceengineer-website](https://github.com/vamseeachanta/aceengineer-website) | `content/calculators/` and `content/blog/` | Results | Link public-facing artifacts only. |

## Governance → workspace-hub and llm-wiki

| Wiki domain | Wiki topic | Repo | Target | Layer | Public-safety note |
|---|---|---|---|---|---|
| all | Promotion, public/private boundary, completion scorecards | [workspace-hub](https://github.com/vamseeachanta/workspace-hub) | `docs/document-intelligence/` and `docs/governance/` | Governance | Link policies and control-plane docs. |
| all | Wiki pages, scorecards, source-family aggregate scans, cross-link reports | [llm-wiki](https://github.com/vamseeachanta/llm-wiki) | `docs/reports/` and `wikis/` | Knowledge/Results | Store only public-safe synthesis. |
| all | Private GTM/prospect boundary | [aceengineer-strategy](https://github.com/vamseeachanta/aceengineer-strategy) | boundary note only | Governance | No named prospects, contacts, pricing, or private strategy. |

## Operational rule

A wiki page is practical-complete only when it can answer: what is this, where did it come from, where is it implemented or validated, and what remains blocked by clearance or approval.
