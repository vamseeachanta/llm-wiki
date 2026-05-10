---
title: "LLM-Wiki Practical Completion Roadmap"
created: 2026-05-10
last_updated: 2026-05-10
source_inventory: sanitized /mnt/ace source-family audit
related_issue: 13
---

# LLM-Wiki Practical Completion Roadmap

This report turns the current `llm-wiki` repo, historic GitHub issue portfolio, tier-1 repo ecosystem, and local `/mnt/ace` source-family inventory into a practical completion queue. It is intentionally **public-safe**: it records source-family labels and aggregate file/extension counts, but it does not copy raw files, vendor standards text, client material, personal/admin data, credentials, or private workspace memory into the repo.

## Current Completeness Baseline

Generated on 2026-05-10 with `uv run python scripts/llm_wiki_strengthening_scorecard.py`:

| Domain | Practical status |
|---|---|
| `marine-engineering` | Largest and source-heavy domain; needs index/cross-link/navigation hardening more than more volume. |
| `engineering-standards` | Strong standards coverage; keep expansions metadata-only and clear Batch Pack 4 inputs first. |
| `engineering` | Good hub; needs reverse-link/cross-domain routing against standards and marine pages. |
| `lng-projects` | Expanded but still gated for SESA/source-family work; prioritize standards routing and clearance. |
| `maritime-law` | Domain exists with cases/liabilities; implement convention routing only after approval. |
| `naval-architecture` | Useful but smaller; safe growth via public/open educational and repo-backed references. |
| `asset-management` | Structurally complete small domain; link more explicitly to asset lifecycle and standards pages. |
| `acma-projects` | Structurally complete but thin; only public-safe project synthesis should be promoted. |
| `reservoir-engineering` | Not yet a first-class wiki domain; #40 is the correct plan-review lane. |

See the refreshed scorecard: [`docs/reports/llm-wiki-strengthening-scorecard.md`](llm-wiki-strengthening-scorecard.md).

## Tier-1 Ecosystem Links

| Repo | llm-wiki relationship |
|---|---|
| [workspace-hub](https://github.com/vamseeachanta/workspace-hub) | orchestration, extraction pipelines, governance docs |
| [digitalmodel](https://github.com/vamseeachanta/digitalmodel) | marine/offshore computation, OrcaFlex/OrcaWave workflows, engineering reports |
| [assetutilities](https://github.com/vamseeachanta/assetutilities) | shared Python utilities used by pipelines |
| [worldenergydata](https://github.com/vamseeachanta/worldenergydata) | energy data acquisition and public datasets |
| [llm-wiki](https://github.com/vamseeachanta/llm-wiki) | public wiki artifacts and scorecards |
| [assethold](https://github.com/vamseeachanta/assethold) | asset lifecycle / asset-management context |
| [aceengineer-website](https://github.com/vamseeachanta/aceengineer-website) | public-facing demos and published outcomes |
| [aceengineer-strategy](https://github.com/vamseeachanta/aceengineer-strategy) | private GTM/prospect strategy; link only generic public-safe outputs |

## Sanitized `/mnt/ace` Source-Family Map

| Source family | Files seen | Top observed extensions | Candidate wiki domains/results | Public-safety class | Completion action |
|---|---:|---|---|---|---|
| `O&G-Standards` | 57,463 | .pdf 54,899, .txt 664, .doc 560, .jpg 289, .docx 278 | engineering-standards, engineering, future reservoir/petroleum pages | High: vendor/standards-derived | Use metadata-only standards/source-family manifests; no copied standards text. Tie to #7/#12/#48. |
| `digitalmodel` | 138,738 | .sldprt 26,733, .pdf 20,083, .doc 11,327, .lod 7,768, .dat 5,838 | marine-engineering, naval-architecture, engineering workflows | Medium | Link repo modules/results to wiki concepts and examples through public repo URLs; avoid private project files. |
| `docs` | 250,101+ | .key 52,836, .dat 16,990, .bat 16,788, .pdf 14,952, .sldprt 14,852 | engineering-standards, marine-engineering | High/mixed | Treat as private/archive source family; only promote cleared public metadata and issue-derived summaries. |
| `data` | 760,615+ | .json 717,139, .jpg 17,858, .mp3 3,375, .pdf 3,181, .aif 1,924 | future datasets/source inventory, not direct wiki pages | High/mixed | Do not bulk ingest; build aggregate manifests only after clearance. |
| `acma-codes` | 4,897 | .pdf 2,559, .tif 1,634, .gif 61, .dll 60, .fnt 50 | engineering-standards, acma-projects | High | Candidate metadata lane after license review; avoid code text/images. |
| `acma-projects` | 10,729 | .yml 5,498, .sim 2,766, .pdf 642, .csv 288, .dat 274 | acma-projects, marine/offshore project method pages | High/client-sensitive | Only public-safe project summaries and synthetic methodology pages; no client deliverables. |
| `frontierdeepwater` | 6,277 | [no_ext] 5,488, .md 186, .csv 125, .pdf 89, .py 75 | marine-engineering/offshore operations candidates | High | Keep blocked pending #46 clearance checklist. |
| `doris` | 72,903 | .pdf 29,017, .jpg 24,578, .png 6,590, [no_ext] 1,750, .docx 1,215 | lng-projects / SESA candidates | High/client/vendor | Keep blocked pending #43; no direct extraction. |
| `rock-oil-field` | 918 | .pdf 296, .dat 235, .sim 189, .xlsx 70, .docx 68 | future reservoir-engineering domain | Mixed | Best expansion candidate after #40 approval/license triage; cite public literature only. |
| `openfast` | 1,288 | .f90 326, .rst 159, .txt 116, [no_ext] 88, .png 78 | engineering, marine-engineering, wind/offshore workflows | Low/OSS | Safe open-source documentation/code-derived page candidates with repo/source attribution. |
| `gmsh` | 3,984 | .h 1,096, .cpp 764, .geo 579, .c 236, .hpp 223 | engineering workflows, mesh generation | Low/OSS | Safe open-source tooling pages; cross-link to digitalmodel workflows. |
| `MoorDyn` | 1,193 | .h 354, .cpp 252, .hpp 190, .txt 106, [no_ext] 61 | marine-engineering/mooring dynamics | Low/OSS | Safe open-source tooling pages; link to mooring concepts. |
| `MoorPy` | 93 | .py 23, [no_ext] 14, .sample 14, .dat 12, .rst 6 | marine-engineering/mooring design | Low/OSS | Safe open-source tooling pages; link to mooring concepts. |
| `HAMS` | 1,086 | .rao 756, .txt 174, .f90 22, [no_ext] 16, .sample 14 | hydrodynamics/BEM tooling | Low/OSS-academic | Safe open-source/academic tooling lane after provenance check. |
| `WEC-Sim` | 1,085 | .dat 242, .m 171, .png 152, .tec 73, .rst 43 | marine/offshore wave energy tooling | Low/OSS | Safe open-source tooling lane after provenance check. |
| `opm-common` | 3,278 | [no_ext] 1,276, .hpp 718, .cpp 684, .data 117, .cmake 79 | future petroleum/reservoir computation | Low/OSS | Safe open-source tooling lane for reservoir engineering after #40. |
| `worldenergydata` | 345 | .bin 145, .csv 67, .pdf 59, [no_ext] 32, .zip 17 | worldenergydata repo links, energy data pipelines | Medium | Link repo outputs and documented public datasets; no raw private dumps. |
| `assethold` | 507 | .md 500, .xlsx 4, .pdf 3 | asset-management | Medium | Link public repo/docs and asset lifecycle pages. |
| `aceengineercode` | 4,178 | .yml 1,162, .png 901, .py 558, .csv 409, .md 274 | engineering implementation examples | Medium | Use public/reusable examples only; no confidential project artifacts. |

Excluded from public completion work: admin/tax/personal/recruiting/credential folders, client-sensitive project deliverables, raw HSE rows, private vendor PDFs, path-rich manifests, copied standards clauses/tables/formulas, and any workspace-hub private memory or strategy notes.

## Historic Issue Portfolio Synthesis

| Issue set | Link | Completion interpretation |
|---|---|---|
| #13 | [roadmap umbrella](https://github.com/vamseeachanta/llm-wiki/issues/13) | Update/cross-link; do not create duplicate roadmap. |
| #1-#5, #7-#11 | [raw corpus / deep extraction portfolio](https://github.com/vamseeachanta/llm-wiki/issues/1) | Upstream extraction portfolio; public repo receives only cleared synthesized artifacts. |
| #19 | [offshore raw-source family backfill](https://github.com/vamseeachanta/llm-wiki/issues/19) | Remains blocked; split into #44-#46 clearance tasks. |
| #40 | [reservoir engineering literature](https://github.com/vamseeachanta/llm-wiki/issues/40) | Best next domain expansion after plan approval/license triage. |
| #43-#46 | [clearance checklists](https://github.com/vamseeachanta/llm-wiki/issues/43) | First aggressive Codex lane: public-safe governance checklists. |
| #47-#48 | [restore approved batch inputs](https://github.com/vamseeachanta/llm-wiki/issues/47) | First aggressive Codex lane: unblock Batch Pack 1/4. |
| #20/#21/#27/#28/#29 | [navigation/cross-links/indexing](https://github.com/vamseeachanta/llm-wiki/issues/20) | Parallel low-risk repo-local markdown/script work. |
| #23/#30/#38 | [frontmatter/provenance/WRK normalization](https://github.com/vamseeachanta/llm-wiki/issues/23) | Foundation lane after blocker prep. |
| #41/#42 | [standards routing implementation](https://github.com/vamseeachanta/llm-wiki/issues/41) | Implement only after plan approval/state sync. |

## Aggressive Codex Usage Plan

Use the remaining Codex budget on read/write work that is narrow, public-safe, and independently verifiable:

1. **Blocker-prep wave (6 parallel lanes):** #43, #44, #45, #46, #47, #48. Deliver governance/checklist/input-restore markdown only; no raw extraction.
2. **Navigation wave (5 parallel lanes):** #20, #21, #27, #28, #29. Regenerate cross-links, add uplinks, chunk large indexes, and add source-title aliases.
3. **Foundation wave (3 parallel lanes):** #23, #30, #38. Normalize required frontmatter/provenance and WRK completion seeds.
4. **Approved-domain wave:** #41/#42 only after plan-review approval; #40 only after user approval/license triage.
5. **Corpus extraction wave:** #1-#5/#7-#11 stay upstream/pipeline work; public `llm-wiki` should receive only synthesized, license-cleared pages and manifests.

## Practical Definition of “Complete Enough”

`llm-wiki` is complete enough for practical use when:

- Every existing domain has index/log/overview/portal navigation and no unindexed content pages.
- Cross-links include tier-1 repo targets, source-family summaries, and domain-to-domain backlinks.
- Every promoted page has minimal provenance frontmatter and a public-safe source classification.
- Raw `/mnt/ace` material is represented only as clearance-gated source-family manifests or synthesized public pages.
- All broad historic issues are either closed with evidence, narrowed into executable children, or marked blocked with explicit clearance requirements.

## Immediate Next Commit Candidates

- Keep this roadmap and the refreshed scorecard in `docs/reports/`.
- Post a concise update to #13 linking this report and stating that no new umbrella issue is needed.
- Then run issue-specific worktrees/Codex lanes for #43-#48 and #20/#21/#27/#28/#29.
