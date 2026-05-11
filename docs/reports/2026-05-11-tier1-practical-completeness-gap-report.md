---
title: "Tier-1 Practical Completeness Gap Report"
created: 2026-05-11
last_updated: 2026-05-11
related_issue: 13
public_safety: public links and repository-relative targets only; no raw/vendor/client content
---

# Tier-1 Practical Completeness Gap Report

This report records the completed Codex read-only tier-1/data/results mapping lane and the safe artifacts added from it. It complements the control plane, tier-1 ecosystem map, and aggregate source-family scan.

## 1. Repo-by-repo authoritative targets

| Repo | Practical role | High-value targets for wiki linkage | Boundary |
|---|---|---|---|
| [workspace-hub](https://github.com/vamseeachanta/workspace-hub) | Orchestration and governance | `AGENTS.md`, `docs/document-intelligence/`, `docs/governance/`, audit reports, plan templates | Do not publish private memory, prompt packs, or raw archive details. |
| [digitalmodel](https://github.com/vamseeachanta/digitalmodel) | Engineering implementation and validated outputs | `docs/maps/digitalmodel-operator-map.md`, `docs/domains/`, `examples/demos/gtm/`, benchmark reports | Do not publish client solver models or private simulation outputs. |
| [assetutilities](https://github.com/vamseeachanta/assetutilities) | Shared extraction/reporting/YAML/unit utilities | `docs/maps/assetutilities-operator-map.md`, `src/assetutilities/common/`, `src/assetutilities/units/` | Link code/docs; do not vendor implementation into wiki pages. |
| [worldenergydata](https://github.com/vamseeachanta/worldenergydata) | Public energy data pipelines | `MODULE_INDEX.md`, `docs/data/`, `docs/data-sources/`, BSEE/SODIR/FDAS docs | Public provenance and dictionaries only; no private row-level dumps. |
| [llm-wiki](https://github.com/vamseeachanta/llm-wiki) | Public knowledge and control artifacts | `wikis/`, `docs/reports/`, `docs/governance/` | Store public-safe synthesis only. |
| [assethold](https://github.com/vamseeachanta/assethold) | Generic asset lifecycle/risk methods | `docs/api/`, `docs/architecture.md`, `docs/backtesting.md` | Exclude private holdings/account/personal finance data. |
| [aceengineer-website](https://github.com/vamseeachanta/aceengineer-website) | Public demos/results/calculators | `content/demos/`, `content/case-studies/`, `content/calculators/`, `assets/data/` | Prefer deployed public URLs once confirmed. |
| [aceengineer-strategy](https://github.com/vamseeachanta/aceengineer-strategy) | Private GTM boundary | Boundary note only | No prospects, contacts, pricing, proposals, or confidential strategy. |

## 2. Data/software/results layer map

| Layer | Authoritative repos | Safe `llm-wiki` exposure |
|---|---|---|
| Data | `worldenergydata`, selected public website data, aggregate `llm-wiki` source-family scans | Public-source provenance, source-family status, data dictionaries, no raw private dumps. |
| Software | `digitalmodel`, `assetutilities`, `worldenergydata`, `assethold` | Concept/source pages link modules, examples, tests, and docs. |
| Results | `digitalmodel` demo outputs and benchmarks, `aceengineer-website` demos/case studies/calculators, `llm-wiki` reports | Public-safe HTML/JSON/Markdown reports with validation references. |
| Governance | `workspace-hub`, `llm-wiki`, GitHub issue portfolio | Promotion rules, clearance state, approval gates, roadmap issue links. |

## 3. Wiki cross-link gaps addressed now

The following safe artifacts were added to make the wiki more practical without raw extraction:

1. `wikis/cross-links-tier1.md` — tier-1 code/data/results index across all domains.
2. `wikis/marine-engineering/wiki/code-results-links.md` — implementation and public-result pointers for marine/offshore workflows.
3. `wikis/engineering/wiki/public-data-software-links.md` — public data-source and utility-code anchors.
4. `wikis/asset-management/wiki/software-and-method-links.md` — public-safe asset lifecycle/method links.
5. This gap report — durable Codex lane synthesis.

Remaining high-value gaps should be handled under existing issues rather than a new umbrella: navigation/provenance issues #20/#21/#27/#28/#29/#30/#38/#39 are the safest next implementation lane; raw-family and domain-expansion issues remain clearance/approval gated.

## 4. Public/private/GTM boundary

Public-safe:

- Public GitHub repository URLs.
- Repository-relative docs/code/example paths.
- Public dataset provenance and data dictionaries.
- Aggregate source-family counts and stable family IDs.
- Generic engineering methodology and checked public demo results.

Blocked unless separately cleared:

- Vendor standards text, tables, figures, formulas, scans, or clause-level copying.
- Client/project archives, private solver models, private result folders, and row-level private datasets.
- Named prospects, contacts, pricing, proposals, outbound strategy, and private GTM notes.
- Personal finance, tax, account, admin, credential, or private memory material.

## 5. Safe next artifacts and validation checklist

Safe next artifacts:

1. Source-family disposition table keyed by stable family ID, not raw family label.
2. Domain completion matrix that ties page counts and link-density gaps to existing issues.
3. OSS tooling seed pages for MoorDyn, MoorPy, Gmsh, OpenFAST, HAMS, WEC-Sim, Capytaine, and OPM using upstream public links only.
4. Standards metadata index templates containing code ID, publisher, revision, and source URL only.
5. Plan-review packet hardening for #40/#41/#42 without implementation until approval.

Validation checklist for this packet:

- Link targets are repo-relative or public GitHub/site URLs.
- No raw archive subpaths or full local source paths are published.
- No vendor standards clauses/tables/formulas are copied.
- No client/prospect names or personal/account details are included.
- No row-level private data is included.
- Branch-sensitive `digitalmodel` targets remain repo-relative until public default-branch existence is confirmed.
