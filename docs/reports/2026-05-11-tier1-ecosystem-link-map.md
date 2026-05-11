---
title: "Tier-1 Ecosystem Link Map for LLM-Wiki Completion"
created: 2026-05-11
last_updated: 2026-05-11
related_issue: 13
public_safety: public links and aggregate source-family references only
---

# Tier-1 Ecosystem Link Map for LLM-Wiki Completion

This map defines how `llm-wiki` should link all tier-1 repositories, the data, and the results while keeping the public wiki safe. It is a control-plane artifact: it links authoritative public repos and GitHub issues, but it does **not** copy raw/vendor/client content.

## Completion Architecture

| Layer | Authoritative surface | LLM-wiki exposure rule | Practical completion target |
|---|---|---|---|
| Data layer | Private raw archives under the safe root label `/mnt/ace`, public datasets in repos, and cleared fixtures | Aggregate manifests, source-family IDs, public dataset URLs, issue links | Every high-value source family has a public-safe status: cleared, blocked, or candidate. |
| Software layer | Tier-1 repos and selected OSS tools | Wiki pages link public repo modules, docs, examples, and tests | Concepts/entities/standards point back to code that implements or validates them. |
| Results layer | Validated reports, scorecards, dashboards, demo artifacts, and reproducible outputs | Link public-safe generated outputs; summarize only non-client, license-safe results | Important wiki pages identify where results live and what validator produced them. |
| Governance layer | GitHub issue portfolio and plan/approval state | Issue links are the execution control plane | Historic work is reused; duplicate umbrella issues are avoided. |

## Public-safe link targets

| Repo | Role in practical completion | What llm-wiki should link | Boundary |
|---|---|---|---|
| [workspace-hub](https://github.com/vamseeachanta/workspace-hub) | Orchestration, extraction pipelines, governance, multi-repo closeout | Plans, policies, pipeline docs, public issue evidence | Do not copy private workspace memory, local prompts, or raw archive details. |
| [digitalmodel](https://github.com/vamseeachanta/digitalmodel) | Marine/offshore computation and report generation | OrcaFlex/OrcaWave workflows, solver-proof reports, public examples, module docs | Do not copy client model files or private project simulations. |
| [assetutilities](https://github.com/vamseeachanta/assetutilities) | Shared utility package for extraction/reporting pipelines | Utility modules used by scanners, report builders, and validators | Link implementation; avoid vendoring utility code into wiki pages. |
| [worldenergydata](https://github.com/vamseeachanta/worldenergydata) | Energy data acquisition and dataset workflows | Public dataset pipelines, source registries, field/energy examples | Avoid raw private dumps; prefer reproducible public-data provenance. |
| [llm-wiki](https://github.com/vamseeachanta/llm-wiki) | Public knowledge artifact store | Wiki pages, scorecards, portals, source-family manifests, governance docs | This repo stores public-safe synthesis only. |
| [assethold](https://github.com/vamseeachanta/assethold) | Asset lifecycle and holding-structure context | Asset-management concepts, lifecycle methodology, cleared public docs | Keep private financial/admin details out. |
| [aceengineer-website](https://github.com/vamseeachanta/aceengineer-website) | Public-facing demos and published outcomes | Demo/result pages that can point users from knowledge to rendered proof | Link only public site artifacts and generic demos. |
| [aceengineer-strategy](https://github.com/vamseeachanta/aceengineer-strategy) | GTM/private strategy repository | Generic GTM learnings only when already public-safe | GTM/private boundary: no named prospects, private contacts, or confidential strategy in llm-wiki. |

## Data layer

The safe root label `/mnt/ace` represents heterogeneous raw material: standards, engineering documents, private project files, software repos, datasets, result folders, and personal/admin material. Practical completion does not mean bulk ingest. It means each source family has a public-safe disposition:

1. **Low-risk OSS/public software** — link to public upstream repos or public tier-1 modules; create concept/entity pages with attribution.
2. **Public datasets** — link to public dataset sources and reproducible extraction scripts; avoid row-level sensitive data.
3. **Vendor standards and copyrighted standards-derived documents** — use metadata-only references, code IDs, publisher/revision facts, and cleared public summaries; do not copy clauses, tables, figures, or formulas.
4. **Client/project archives** — use only synthetic/generic methodology pages or public-safe result summaries after clearance.
5. **Personal/admin/credential material** — excluded from wiki completion.

## Software layer

Wiki pages should include repo links when a tier-1 repo implements, validates, visualizes, or operationalizes the topic. Preferred link directions:

- Standards and engineering-method pages -> `digitalmodel` implementation/report examples when public-safe.
- Data-source pages -> `worldenergydata` public pipelines and `assetutilities` helper modules.
- Asset lifecycle pages -> `assethold` public methods and `assetutilities` common utilities.
- Knowledge governance pages -> `workspace-hub` plans and `llm-wiki` scorecards.
- Demo/result pages -> `aceengineer-website` published artifacts.

## Results layer

Result linkage should be evidence-first:

| Result type | Wiki representation | Required proof before linking |
|---|---|---|
| Scorecard/report | Link checked-in Markdown/JSON report | Generator command and validation command. |
| Solver/demo output | Link public HTML/PDF/image/demo page | Public-safe artifact, no client identifiers, and validator evidence. |
| Dataset summary | Link public dataset source and generated summary | Source URL, extraction script, and row/field safety review. |
| Issue closeout evidence | Link GitHub issue comment or plan artifact | Issue state, validation, and push/commit proof. |

## Governance layer

Do not create a replacement roadmap. The active control plane is:

- [#13 roadmap umbrella](https://github.com/vamseeachanta/llm-wiki/issues/13) — primary practical-completion anchor.
- [#19 raw-source family backfill](https://github.com/vamseeachanta/llm-wiki/issues/19) — blocked raw-family lane until clearance artifacts are complete.
- [#40 reservoir engineering research](https://github.com/vamseeachanta/llm-wiki/issues/40) — plan-review lane for a new reservoir/petroleum domain.
- [#43 SESA clearance](https://github.com/vamseeachanta/llm-wiki/issues/43) and related clearance/input-restoration issues — unblock safe future extraction.

## Wiki exposure rule

A wiki page is complete enough only when it answers all four questions:

1. **What is this?** A concept/entity/standard/source/result with frontmatter.
2. **Where did it come from?** Public-safe provenance or a clearance-blocked source-family link.
3. **Where is it used?** Links to tier-1 repos, code, data, or generated results where applicable.
4. **What remains blocked?** Issue link or explicit clearance note if raw data cannot be promoted yet.

## Do not copy raw/vendor/client content

This map is safe because it uses public GitHub URLs, issue URLs, and aggregate source-family categories only. It must not be expanded with raw file paths, raw text, standards clauses, screenshots from private documents, private result files, credentials, or client/project identifiers unless a separate clearance issue explicitly authorizes the exact public-safe artifact.
