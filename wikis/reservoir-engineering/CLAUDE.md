# Wiki Schema: reservoir-engineering

> Founded 2026-05-16 under explicit user signal (approved plan [#40](https://github.com/vamseeachanta/llm-wiki/issues/40), marker `.planning/plan-approved/40.md`). **Formation-evaluation foundation scope** — NOT a full reservoir-engineering domain founding. Core reservoir-engineering topics (relative permeability, capillary pressure, recovery factor, material balance, decline-curve analysis, well-test interpretation, PVT) are explicitly DEFERRED to a future plan and may be covered under the parallel [workspace-hub #2667 Domain Knowledge Sweep](https://github.com/vamseeachanta/workspace-hub/issues/2667) when it reaches reservoir engineering.

## Scope boundary

This wiki covers — in its **founding (formation-evaluation) scope** — the rock-property and log-interpretation surface that the [Kaggle ROGII 2026 competition](https://github.com/vamseeachanta/kaggle-rogii-2026/issues/5) modeling work needs as a foundation:

- **Foundational rock properties** — porosity (definitions, types, measurement), permeability (Darcy framework, units, measurement; the absolute-vs-effective-vs-relative scope-distinction is named here, but **relative-perm deep coverage is deferred**)
- **Open-hole log interpretation** — gamma-ray log basics, density / neutron / sonic / NMR for porosity, resistivity for saturation (named at concept level; deep coverage staged for follow-up plans)
- **Dip and azimuth** — structural-geology surface needed for horizontal-well placement
- **Formation tops** — stratigraphic correlation surface
- **Geosteering workflow** — methodology overlay on the above; the Kaggle ROGII competition driver
- **Log correlation** — methodology overlay; well-to-well stratigraphic alignment

This wiki does **NOT** cover (deferred — not in this founding scope):

- **Core reservoir-engineering substrate** — relative permeability, capillary pressure, recovery factor, material balance, decline-curve analysis (DCA), well-test interpretation, PVT analysis — deferred to a future plan; may land under [#2667 Domain Knowledge Sweep](https://github.com/vamseeachanta/workspace-hub/issues/2667) when it reaches reservoir engineering
- **Reservoir simulation** — finite-difference / streamline / unstructured-grid simulators; EOR design
- **Well construction** (drilling, casing, cementing, BOP, drill-stem design) — `drilling-engineering/`
- **Production operations** (artificial lift, completions, stimulation, flow assurance) — `production-engineering/`
- **Reservoir geophysics** at the seismic-acquisition level — `seismic-interpretation/` (not yet founded)
- **Vendor-confidential log-interpretation manuals or formation-evaluation software docs** — vendor PDFs stay off-repo per the 2026-05-05 governance rule

Coordination boundary: this wiki's formation-evaluation scope SHOULD NOT overlap with what `#2667 Domain Knowledge Sweep` may eventually cover for the reservoir-engineering substrate. If/when `#2667` reaches reservoir-eng, the two scopes form a clean partition: this wiki carries the formation-evaluation surface, `#2667` carries the recovery / material-balance / EOR substrate.

## Directory Structure

```
raw/          # Immutable source documents (LLM reads, never modifies)
  papers/     # Academic papers, SPE / SPWLA / AAPG papers
  standards/  # Standards documents (API RP 40, SPWLA references, LAS / SEG-Y format specs)
  articles/   # Web articles, blog posts, practitioner essays
  assets/     # Images and figures extracted from sources
wiki/         # LLM-maintained markdown pages
  index.md       # Content catalog
  log.md         # Chronological timeline
  overview.md    # High-level domain synthesis
  concepts/      # Concept pages (porosity, permeability, GR log, dip-azimuth, formation tops)
  methodology/   # Methodology pages (geosteering workflow, log correlation)
  standards/     # Standards pages (publisher-agnostic; code_id, publisher, revision required)
  sources/       # Source summary pages (none yet — first real ingest will produce the first)
```

## Conventions

### Frontmatter Schema

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `title` | **required** | string | Page title |
| `tags` | **required** | list | Classification tags |
| `added` | **required** | date | ISO date when page was created |
| `last_updated` | **required** | date | ISO date of last modification |
| `sources` | recommended | list | Source documents referenced |
| `domain` | optional | string | Explicit domain classification |
| `cross_links` | optional | list | Cross-wiki references |

### Standards page extra fields (`wiki/standards/*.md`)

| Field | Required | Description |
|-------|----------|-------------|
| `code_id` | required (L0 prose) | Canonical code identifier (e.g. `api-rp-40`, `spwla-formation-evaluation`, `cwls-las-2.0`, `seg-y-rev2`) |
| `publisher` | required (L0 prose) | Publishing body (API, SPWLA, CWLS, SEG, …) |
| `revision` | required (L0 prose) | Revision / edition / year (use `verify-at-publish-time` when unknown — see Notes) |
| `jurisdiction` | optional | Geographic or regulatory scope |
| `supersedes` | optional | Prior revisions or codes replaced |

> L0-prose enforcement only.

## Ingest Workflow

1. Read source document.
2. Pre-flight license triage against `docs/research/reservoir-engineering-corpus.md` (license-fail-closed: when in doubt, deny-list — Codex r2 advisory on plan #40).
3. Extract entities, concepts, facts.
4. Create / update source summary in `wiki/sources/`.
5. Create / update concept pages in `wiki/concepts/`.
6. Create / update methodology pages in `wiki/methodology/`.
7. Create / update standards pages in `wiki/standards/` (require `code_id`, `publisher`, `revision`).
8. Update `wiki/index.md`.
9. Append entry to `wiki/log.md`.

## Lint Workflow

Check for:

1. Contradictions between pages.
2. Stale claims superseded by newer sources.
3. Orphan pages (no inbound links).
4. Missing cross-references to `drilling-engineering/` (well-trajectory / horizontal placement / formation-evaluation-basics handover), `production-engineering/` (perforation-strategy depends on formation tops + zone selection), `engineering-standards/` (API / SPWLA / SEG specs).
5. Concepts mentioned but lacking their own page (forward-references to deferred pages are OK during founding — flag for future plans).
6. Data gaps fillable by external sources.
7. **Verbatim-paraphrase audit**: no chunks > 30 words from any cited source regardless of license.
8. **Vendor-content audit**: vendor names (Schlumberger / Halliburton / Baker Hughes / CGG / etc.) cited by NAME + general capability only; no SKUs, no software product names with version, no proprietary log-curve internal nomenclature.

## Cross-domain anchor map

- **drilling-engineering** — `concepts/formation-evaluation-basics.md` already exists in drilling-engineering covering the well-construction-time framing of formation evaluation. This wiki is the reservoir-side complement: drilling-engineering's view is "what does the LWD tool tell me about the formation while I'm still drilling and steering?", reservoir-engineering's view is "what does the openhole / LWD log tell me about the rock as a reservoir-property substrate?". Bidirectional cross-link.
- **production-engineering** — perforation strategy (selecting which intervals to perforate) consumes formation-tops + porosity + permeability outputs from this wiki.
- **engineering-standards** — API RP 40 (core analysis), SPWLA formation-evaluation references (paywalled), CWLS LAS file format (open), SEG-Y format spec (open).
- **kaggle-rogii-2026** — the founding-driver companion repo; geosteering-workflow and dip-azimuth pages in this wiki are the educational substrate for that competition's modeling work.

## Founding-event rollback awareness

Per Codex r2 advisory on plan #40 (carried forward as implementation-time mitigation): if a license-tainted page lands post-publication, response order is:

1. **First**: content-scrub the offending text in place (commit + push the scrubbed version).
2. **Last resort**: `git revert` + force-push, and notify downstream archives (forks, mirrors) so they don't preserve the tainted content. Force-push is destructive to forks' history alignment; reserve for cases where scrubbing in place is insufficient.

## 5-wave PR landing strategy (Codex r2 carried forward)

Founding files (this session) are **Wave 1**. Subsequent waves cover:
- **Wave 2** — corpus manifest (`docs/research/reservoir-engineering-corpus.md`) — license-triaged ingest candidate list.
- **Wave 3** — remaining founding concept pages (gamma-ray-log-interpretation, dip-azimuth, formation-tops).
- **Wave 4** — methodology pages (geosteering-workflow, log-correlation).
- **Wave 5** — standards pages (API RP 40 + LAS + SEG-Y as the open-format anchors; SPWLA references at structural level only).

Each wave warrants its own GH-issue sub-task and adversarial review pass.

## Notes

This wiki was founded 2026-05-16 by user-approved plan [#40](https://github.com/vamseeachanta/llm-wiki/issues/40) as the **11th llm-wiki domain**. Founding driver: Kaggle ROGII 2026 competition modeling foundation. Founding event is documented in `wiki/overview.md` and `wiki/log.md`. The founding files are the structural scaffold (CLAUDE.md / overview.md / index.md / log.md) plus the two foundational rock-property concept pages (`porosity.md`, `permeability.md`); the remaining founding-scope pages (gamma-ray-log-interpretation, dip-azimuth, formation-tops, geosteering-workflow, log-correlation) land in Wave 3 and Wave 4 per the strategy above.

Standards-revision verification: any standards page authored during this founding session that lists `revision: "verify-at-publish-time"` MUST be fact-verified by the main session (or a follow-up sub-issue) before the wave 5 standards-pages PR lands. Founding sessions are draft sessions; the verification gate sits at PR-merge time, not at file-write time.
