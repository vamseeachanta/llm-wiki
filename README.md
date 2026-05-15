# llm-wiki

Engineering knowledge wikis spun out from [`vamseeachanta/workspace-hub`](https://github.com/vamseeachanta/workspace-hub) on 2026-05-05.

This repository is the **content storehouse** for the llm-wiki program — a multi-domain corpus extracted from publicly referenceable engineering sources, industry reports, and methodology references. The corpus extraction pipeline that feeds this repository remains in `workspace-hub` (orchestration tooling stays there; this repo holds the artifacts the pipeline produces).

## Layout

```
wikis/
  acma-projects/         project portfolio wikis
  asset-management/      asset-lifecycle methodology
  engineering/           multi-discipline engineering pages
  engineering-standards/ standards-by-publisher pages (ABS, API, AWS, ASME, BSI, DNV, ISO, NACE, NORSOK, ...)
  lng-projects/          LNG-domain expansion content
  marine-engineering/    marine/offshore corpus (largest domain)
  maritime-law/          maritime-law cases and liabilities
  naval-architecture/    naval-architecture references
  cross-links.md         cross-domain link manifest

seeds/                   seed YAMLs for downstream extraction (mooring failures, maritime cases, ...)

tests/fixtures/          data fixtures for the workspace-hub pipeline's wiki-conformance tests
```

## How to consume

- **AI-agent entrypoint:** start with [`llms.txt`](llms.txt), then route through the domain-level `llms.txt` files instead of recursively scanning `wikis/`.
- **Read directly:** browse `wikis/` on GitHub; pages use frontmatter per the workspace-hub schema (e.g., `code_id`, `publisher`, `revision` for standards pages — see `docs/schemas/`).
- **Programmatic access:** clone or `git submodule add https://github.com/vamseeachanta/llm-wiki` adjacent to your tooling; the workspace-hub pipeline expects `wikis/<domain>/...` paths.
- **Weekly freshness cadence:** update the root and domain `llms.txt` manifests when new domains, high-value concepts, governance routes, or code/result bridges change; keep them bounded to curated entrypoints rather than source-summary inventories.

## Licenses

This repository uses **dual licensing**:

| What | License | File |
|------|---------|------|
| Repo-local scripts/tests/validators (supporting tooling; primary extraction pipeline remains in workspace-hub) | MIT | [`LICENSE`](LICENSE) |
| Wiki content under `wikis/**/*.md` | CC-BY-4.0 | [`LICENSE-CONTENT`](LICENSE-CONTENT) |

Wiki pages contain citation-safe metadata, brief summaries, and authored synthesis of publicly referenceable engineering standards and methodology sources. Vendor-derivative PDFs, copied clauses, copied tables, copied figures, and other standards text (DNV, API, ABS, etc.) are explicitly **not** in this repository — restricted source material lives in private `/mnt/ace` archives per the workspace-hub vendor-derivative deny-list (see `.claude/rules/calc-citation-contract.md` upstream).

## Provenance

- Source: `vamseeachanta/workspace-hub@258e2bb8478e8301e68e46193a811064124e0f29`
- Spinout decision history: [vamseeachanta/workspace-hub#2398](https://github.com/vamseeachanta/workspace-hub/issues/2398)
- Migration plan: [vamseeachanta/worldenergydata `docs/plans/2026-05-05-llm-wiki-spinout-migration-plan.md`](https://github.com/vamseeachanta/worldenergydata/blob/main/docs/plans/2026-05-05-llm-wiki-spinout-migration-plan.md)
- Pre-flight scrub: workspace-hub PR [#2648](https://github.com/vamseeachanta/workspace-hub/pull/2648) removed vendor PDFs to `/mnt/ace` before this repo was initialized.

## Contributing

Wiki content additions follow the workspace-hub promotion contract (see `docs/governance/` once populated). Standards-derived constants must carry `code_id` frontmatter per the `#2471` schema.

The canonical high-volume authoring and extraction surface remains workspace-hub. This repo now also contains public-safe supporting scripts, tests, scorecards, and governance validators for repo-local verification and completion tracking.
