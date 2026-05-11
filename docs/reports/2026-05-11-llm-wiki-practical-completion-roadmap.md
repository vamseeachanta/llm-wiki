---
title: "LLM-Wiki Practical Completion Roadmap"
created: 2026-05-11
last_updated: 2026-05-11
source_inventory: sanitized /mnt/ace source-family audit
related_issue: 13
public_safety: aggregate-only private-corpus references; no raw source content copied
---

# LLM-Wiki Practical Completion Roadmap

This roadmap defines how to make `llm-wiki` as complete as practical without violating the public/private boundary. It combines three fresh Codex audit lanes run on 2026-05-11:

1. repo completeness and structural scorecard;
2. `/mnt/ace` source-family and layer inventory; and
3. live GitHub issue portfolio/history.

The result is a **four-layer completion plan**: Data-bank, Software, Results, and GitHub issues, tied back to all tier-1 repos. It intentionally does **not** bulk ingest raw `/mnt/ace` content. Private/vendor/client/admin material stays behind clearance gates; public wiki content receives aggregate manifests, authored synthesis, links, scorecards, and cleared source pages only.

## Current Completeness Baseline

Generated on 2026-05-11 with:

```bash
uv run python scripts/llm_wiki_strengthening_scorecard.py --date 2026-05-11
uv run python scripts/validate_governance_artifacts.py
PYTHONDONTWRITEBYTECODE=1 uv run pytest -q -p no:cacheprovider
```

| Domain | Score | Pages | Curated | Sources | Practical status |
|---|---:|---:|---:|---:|---|
| `marine-engineering` | 84.4 | 19,216 | 45 | 19,171 | Deepest domain by volume, but source-heavy; needs curated portals, backlinks, and index chunking more than more raw pages. |
| `engineering` | 96.8 | 128 | 104 | 24 | Good hub; one unindexed template page and orphan curated pages need repair. |
| `naval-architecture` | 97.7 | 70 | 26 | 44 | Useful but smaller; grow through public/open educational and OSS tool references. |
| `lng-projects` | 98.4 | 30 | 22 | 8 | Structurally good; gated standards/SESA source-family work should remain clearance-first. |
| `maritime-law` | 99.0 | 82 | 80 | 2 | Strong case/convention skeleton; standards-routing is waiting in plan review. |
| `engineering-standards` | 99.8 | 216 | 197 | 19 | Strongest curated standards layer; backfill two index omissions and keep vendor text out. |
| `acma-projects` | 100.0 | 4 | 2 | 2 | Structurally complete but thin; only public-safe project synthesis should be promoted. |
| `asset-management` | 100.0 | 23 | 22 | 1 | Structurally complete; needs continued cross-domain asset lifecycle links. |

Fresh scorecard artifacts:

- [`llm-wiki-strengthening-scorecard.md`](llm-wiki-strengthening-scorecard.md)
- [`llm-wiki-strengthening-scorecard.json`](llm-wiki-strengthening-scorecard.json)

Important interpretation: high structural scores do **not** mean factual/domain completeness. They mean the repo is navigable enough to support targeted completion lanes.

## Tier-1 Ecosystem Links

| Repo | Public URL | llm-wiki completion role |
|---|---|---|
| `workspace-hub` | <https://github.com/vamseeachanta/workspace-hub> | Control plane for extraction pipelines, planning/governance, validation scripts, and source-family clearance. |
| `digitalmodel` | <https://github.com/vamseeachanta/digitalmodel> | Marine/offshore computation, OrcaFlex/OrcaWave workflows, engineering reports, and examples to link from marine/engineering pages. |
| `assetutilities` | <https://github.com/vamseeachanta/assetutilities> | Shared Python utilities and reusable implementation patterns referenced by workflows and source-processing pages. |
| `worldenergydata` | <https://github.com/vamseeachanta/worldenergydata> | Public energy-data acquisition and dataset pipeline references for Data-bank pages. |
| `llm-wiki` | <https://github.com/vamseeachanta/llm-wiki> | Public content storehouse: wikis, scorecards, governance artifacts, tests, and lightweight validators. |
| `assethold` | <https://github.com/vamseeachanta/assethold> | Asset lifecycle / asset-management references and reusable portfolio context. |
| `aceengineer-website` | <https://github.com/vamseeachanta/aceengineer-website> | Public-facing demos, published outcomes, and result-page destinations. |
| `aceengineer-strategy` | <https://github.com/vamseeachanta/aceengineer-strategy> | Private GTM/prospect strategy; only generic public-safe outputs should be linked, never named prospect details. |

## Sanitized `/mnt/ace` Source-Family Map

The 2026-05-11 source-family audit scanned aggregates only. The extension-profile scan counted 3,223,163 files under `/mnt/ace` while excluding `.git` internals and trash. The top-level source-family classifier uses a separate directory-family walk; its classification rows below are the authoritative inputs for public-safety routing and should not be arithmetically compared to the extension-profile total.

### Top-level classification

| Classification | Top-level dirs | Files | Subdirs | Public-safety decision |
|---|---:|---:|---:|---|
| Public-safe OSS candidates | 4 | 3,457 | 393 | Usable after license attribution and source citation checks. |
| Mixed standards/vendor reference | 2 | 62,406 | 1,201 | Metadata and authored synthesis only; no copied standards text/tables/figures. |
| Private/vendor/client engineering | 4 | 57,718 | 1,123 | Restricted; use only approved aggregate/source-family metadata. |
| Private software/results | 1 | 4,197 | 384 | Restricted; no raw code, config, results, or data promotion without clearance. |
| Private/admin/personal | 8 | 91,799 | 12,061 | Exclude from `llm-wiki` completion. |
| Unknown/mixed | 21 | 3,012,224 | 113,831 | Quarantine until source-family classification and clearance. |

### Dominant extension profile

| Extension/family | Count | Completion implication |
|---|---:|---|
| `.json` | 1,432,715 | Data-bank/index/export layer; classify before ingest. |
| `.pdf` | 290,828 | Standards, papers, reports; high copyright/vendor risk. |
| `.jpg` | 257,685 | Images/figures; do not promote unless public-cleared. |
| CAD/model files (`.dwg`, `.ipt`, `.sldprt`, `.iam`) | 471,041 combined | Treat as private/vendor/client model archive unless source family is explicitly OSS. |
| `.msg` | 38,573 | Email/message archive; exclude by default. |
| Office docs (`.doc`, `.docx`, `.xls`, `.xlsx`) | 77,741 combined | High private/client/vendor risk; only aggregate metadata unless cleared. |

### Low-risk first candidates

Public-safe OSS candidate families with local license indicators:

- `HAMS`
- `MoorDyn`
- `MoorPy`
- `WEC-Sim`

These should become the first aggressive content-expansion lane because they can improve `marine-engineering`, `naval-architecture`, and `engineering` with low public-safety risk if license attribution is verified.

## Data-bank, Software, Results, and GitHub-Issue Linkage

| Layer | `/mnt/ace` representation | Public `llm-wiki` representation | Completion rule |
|---|---|---|---|
| Data-bank | `data`, public energy datasets, dataset fixtures, JSON/CSV/archive exports | Dataset/source-family registries, public dataset links, reproducible summaries, scorecards | Aggregate and cite; never copy private row-level dumps or sensitive exports. |
| Software | Tier-1 repos plus OSS tool folders (`gmsh`, `MoorDyn`, `MoorPy`, `HAMS`, `WEC-Sim`, `openfast`, `opm-common`) | Tool/API/source pages, workflow pages, public repo links, install/build notes, benchmark indexes | Link implementation to concepts and results; avoid private project source drops. |
| Results | Engineering reports, dashboards, validation outputs, demos, result folders | Public-safe report links, generated dashboards, validation summaries, and scorecards | Promote only synthesized results that are reproducible, license-safe, and non-client-specific. |
| GitHub issues | Live issue history in `vamseeachanta/llm-wiki` plus upstream workspace issue history | Roadmap, execution lanes, blocker/approval state, evidence links | Historic issue work is the control plane; update existing umbrellas rather than creating duplicates. |
| Tier-1 repos | workspace-hub, digitalmodel, assetutilities, worldenergydata, llm-wiki, assethold, aceengineer-website, aceengineer-strategy | Cross-repo backlinks from wiki domains to authoritative code/data/result artifacts | Use public URLs where possible; keep private GTM/prospect material out. |

Upstream control-plane anchors already linked from this repo include the spinout decision [workspace-hub#2398](https://github.com/vamseeachanta/workspace-hub/issues/2398), pre-flight scrub [workspace-hub#2648](https://github.com/vamseeachanta/workspace-hub/pull/2648), and migration plan in [`worldenergydata/docs/plans/2026-05-05-llm-wiki-spinout-migration-plan.md`](https://github.com/vamseeachanta/worldenergydata/blob/main/docs/plans/2026-05-05-llm-wiki-spinout-migration-plan.md). Future completion issues should preserve this pattern: public repo URL, issue/PR URL, source-family safety class, and resulting wiki/report artifact URL.

## Historic GitHub Issue Portfolio Synthesis

Live `gh issue list/view` on 2026-05-11 found 48 issues: 36 open and 12 closed.

### Steering umbrellas and parent issues

| Issue | Status | Completion interpretation |
|---|---|---|
| [#13](https://github.com/vamseeachanta/llm-wiki/issues/13) | open | Main roadmap umbrella. Update this issue; do not create a duplicate umbrella. |
| [#1](https://github.com/vamseeachanta/llm-wiki/issues/1) | open, `status:plan-approved` | Large WRK-1245 corpus umbrella; public repo receives cleared synthesis only. |
| [#14](https://github.com/vamseeachanta/llm-wiki/issues/14) | open, blocked | SESA/LNG parent; prep issue [#43](https://github.com/vamseeachanta/llm-wiki/issues/43) is closed, so blocker state needs revalidation. |
| [#19](https://github.com/vamseeachanta/llm-wiki/issues/19) | open, blocked | Offshore raw-source family parent; prep issues [#44](https://github.com/vamseeachanta/llm-wiki/issues/44)-[#46](https://github.com/vamseeachanta/llm-wiki/issues/46) are closed, so blocker state needs revalidation. |
| [#25](https://github.com/vamseeachanta/llm-wiki/issues/25) | open, blocked | Batch Pack 1 execution parent; input-restore [#47](https://github.com/vamseeachanta/llm-wiki/issues/47) is closed. |
| [#26](https://github.com/vamseeachanta/llm-wiki/issues/26) | open, blocked | Batch Pack 4 execution parent; input-restore [#48](https://github.com/vamseeachanta/llm-wiki/issues/48) is closed. |

### Completed issue history that should not be repeated

Closed/completed lanes already include [#15](https://github.com/vamseeachanta/llm-wiki/issues/15), [#16](https://github.com/vamseeachanta/llm-wiki/issues/16), [#17](https://github.com/vamseeachanta/llm-wiki/issues/17), [#18](https://github.com/vamseeachanta/llm-wiki/issues/18), [#22](https://github.com/vamseeachanta/llm-wiki/issues/22), [#37](https://github.com/vamseeachanta/llm-wiki/issues/37), and the blocker-prep/input-restore set [#43](https://github.com/vamseeachanta/llm-wiki/issues/43)-[#48](https://github.com/vamseeachanta/llm-wiki/issues/48).

### Plan-review queue requiring user approval before implementation

- [#40 reservoir engineering literature](https://github.com/vamseeachanta/llm-wiki/issues/40)
- [#41 maritime-law standards routing](https://github.com/vamseeachanta/llm-wiki/issues/41)
- [#42 LNG-projects standards routing](https://github.com/vamseeachanta/llm-wiki/issues/42)

## Aggressive Codex Usage Plan

Given the 2026-05-11 operating assumption of 67% remaining weekly Codex budget, spend aggressively but safely on lanes that are narrow, parallelizable, public-safe, and independently verifiable.

1. **Unblock/revalidate parent issues (4 lanes):** [#14](https://github.com/vamseeachanta/llm-wiki/issues/14), [#19](https://github.com/vamseeachanta/llm-wiki/issues/19), [#25](https://github.com/vamseeachanta/llm-wiki/issues/25), [#26](https://github.com/vamseeachanta/llm-wiki/issues/26). Check whether completed prep issues satisfy blocker conditions, then update labels/comments through the issue workflow.
2. **Navigation/structural repair wave (5 lanes):** [#20](https://github.com/vamseeachanta/llm-wiki/issues/20), [#21](https://github.com/vamseeachanta/llm-wiki/issues/21), [#27](https://github.com/vamseeachanta/llm-wiki/issues/27), [#28](https://github.com/vamseeachanta/llm-wiki/issues/28), [#29](https://github.com/vamseeachanta/llm-wiki/issues/29). This is low-risk markdown/script work that directly improves practical usability.
3. **Provenance/frontmatter wave (4 lanes):** [#23](https://github.com/vamseeachanta/llm-wiki/issues/23), [#30](https://github.com/vamseeachanta/llm-wiki/issues/30), [#31](https://github.com/vamseeachanta/llm-wiki/issues/31), [#38](https://github.com/vamseeachanta/llm-wiki/issues/38). This makes pages machine-actionable and auditable.
4. **OSS-source expansion wave (4 lanes):** create or reuse issue lanes for HAMS, MoorDyn, MoorPy, and WEC-Sim public-safe tool pages after license checks. Target source pages, tool overviews, examples inventory, install/build notes, and benchmark index pages.
5. **Plan-review approvals:** move [#40](https://github.com/vamseeachanta/llm-wiki/issues/40), [#41](https://github.com/vamseeachanta/llm-wiki/issues/41), and [#42](https://github.com/vamseeachanta/llm-wiki/issues/42) only after user approval or plan revision.
6. **Keep raw-corpus extraction gated:** [#1](https://github.com/vamseeachanta/llm-wiki/issues/1)-[#12](https://github.com/vamseeachanta/llm-wiki/issues/12) remain upstream/deep-extraction work. The public repo should receive license-cleared summaries, manifests, and reproducible outputs only.

## Practical Definition of “Complete Enough”

`llm-wiki` is complete enough for practical use when:

- every existing domain has `index.md`, `log.md`, `overview.md`, and a portal/navigation path;
- all content pages are indexed or intentionally excluded with a reason;
- cross-links include tier-1 repos, source-family summaries, domain-to-domain backlinks, and result/report destinations;
- every promoted page has minimum provenance frontmatter and a public-safety/source classification;
- raw `/mnt/ace` material is represented only as clearance-gated source-family manifests or synthesized public pages;
- public OSS source-family pages cover HAMS, MoorDyn, MoorPy, WEC-Sim, gmsh/OpenFOAM-style workflows, and the digitalmodel bridge where license-safe;
- broad historic issues are either closed with evidence, narrowed into executable children, or marked blocked with explicit clearance requirements; and
- the scorecard can be regenerated without new structural regressions.

## Immediate Next Commit Candidates

1. Commit this roadmap plus the refreshed scorecard.
2. Update `README.md` to reflect that the repo now has scripts, tests, governance validators, and generated reports.
3. Post [#13](https://github.com/vamseeachanta/llm-wiki/issues/13) with this report and the three Codex audit outcomes.
4. Launch the next Codex wave against blocker revalidation, navigation, and provenance issues instead of bulk raw ingestion.

## Public-Safety Boundaries

Do not commit:

- raw `/mnt/ace` files;
- private path-rich manifests;
- vendor standards PDFs, clauses, tables, or figures;
- client deliverables, CAD/project archives, spreadsheets, or operational rows;
- admin/personal/finance/email material;
- workspace private memory, prospect/GTM notes, secrets, or credentials.

Do commit:

- aggregate source-family counts;
- public repo URLs;
- issue links and evidence comments;
- authored, citation-safe wiki pages;
- regenerated scorecards and validators;
- public-safe navigation/portal/index improvements.
