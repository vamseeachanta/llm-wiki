# Wiki Schema: production-engineering

> Founded 2026-05-13 under explicit user signal to expand upstream value-chain coverage in llm-wiki. Receives the post-drilling production scope that is scope-edged in drilling-engineering's `artificial-lift-method-selection.md`.

## Scope boundary

This wiki covers **production engineering** — the post-completion well operations and surface-facility connection that turn a drilled well into a producing asset:

- **Artificial lift in depth** — electric submersible pumps (ESP), gas lift, progressing-cavity pumps (PCP), plunger lift, jet pumps, hydraulic lift, beam pumps (rod-pump deep coverage stays in drilling-engineering per API "drilling and well servicing" framing, with cross-link)
- **Completions** — perforating, sand control, gravel pack, frac packing, screen completions, multi-zone completions
- **Stimulation** — acid stimulation, hydraulic fracturing, well-stim design (matrix vs frac)
- **Production operations** — flow assurance, choke management, well testing during production, surface-handover procedures
- **Well integrity during production** — corrosion / scale / paraffin / asphaltene management, integrity monitoring, intervention triggers
- **Production-side regulatory** — production accounting, allowable rates, gas-oil ratio (GOR) reporting, water cut tracking

This wiki does **NOT** cover:

- **Well construction** (drilling, casing, cementing, BOP) — that's `drilling-engineering/`
- **Reservoir engineering** — characterization, simulation, recovery factor analysis, EOR design — separate domain (not yet founded)
- **Downstream** — refining, petrochemicals (LNG terminals are in `lng-projects/`)
- **Vessel-side floater design** — FPSO hulls in `naval-architecture/`; FPSO topsides processing in scope here only at the well-tubing-to-manifold boundary
- **Subsea production hardware** — Christmas trees, jumpers, flowlines — straddles marine-engineering and production-engineering; cross-link rather than duplicate

## Directory Structure

```
raw/          # Immutable source documents (LLM reads, never modifies)
  papers/     # Academic papers, SPE production papers
  standards/  # Standards documents (API 11/14/17 series)
  articles/   # Web articles, blog posts, practitioner essays
  assets/     # Images and figures extracted from sources
wiki/         # LLM-maintained markdown pages
  index.md    # Content catalog
  log.md      # Chronological timeline
  overview.md # High-level domain synthesis
  entities/   # Entity pages (specific producing fields, artificial-lift vendor archetypes)
  concepts/   # Concept pages
  sources/    # Source summary pages
  standards/  # Standards pages (publisher-agnostic; code_id, publisher, revision required)
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
| `code_id` | required (L0 prose) | Canonical code identifier (e.g. `api-rp-14e`, `api-spec-19c`) |
| `publisher` | required (L0 prose) | Publishing body |
| `revision` | required (L0 prose) | Revision / edition / year |
| `jurisdiction` | optional | Geographic or regulatory scope |
| `supersedes` | optional | Prior revisions or codes replaced |

## Ingest Workflow

1. Read source document
2. Extract entities, concepts, facts
3. Create / update source summary in `wiki/sources/`
4. Update / create entity pages in `wiki/entities/`
5. Update / create concept pages in `wiki/concepts/`
6. Update `wiki/index.md`
7. Append entry to `wiki/log.md`

## Lint Workflow

Check for:

1. Contradictions between pages
2. Stale claims superseded by newer sources
3. Orphan pages (no inbound links)
4. Missing cross-references to `drilling-engineering/` (well-construction handover), `naval-architecture/` (FPSO host platforms), `marine-engineering/` (offshore-marine production-vessel operations), `engineering-standards/` (API production specs)
5. Concepts mentioned but lacking their own page
6. Data gaps fillable by external sources

## Cross-domain anchor map

- **drilling-engineering** — the hand-off boundary. Well construction completes when the production tubing is run and the well is handed to production-engineering. The drilling-engineering `concepts/artificial-lift-method-selection.md` page is the **founding-trigger anchor** for this wiki; rod-pump deep coverage stays there, the other 4 methods (ESP, gas lift, PCP, plunger lift) develop here.
- **naval-architecture** — FPSO hull and processing-topside coupling. Production tubing connects to FPSO topsides via a riser-and-manifold system; this wiki's coverage stops at the wellhead, naval-arch covers the floater.
- **marine-engineering** — offshore-marine production-vessel operations (mooring, station-keeping during production).
- **engineering-standards** — the API 11 series (artificial lift), API 14 series (production-facility design), API 17 series (subsea production systems).

## Notes

This wiki was founded 2026-05-13 by user directive as the **10th llm-wiki domain**, completing the upstream value-chain coverage alongside drilling-engineering (9th, founded earlier same day). The founding event is documented in `wiki/overview.md` and `wiki/log.md`. No external LinkedIn-post trigger (unlike drilling-engineering's Papkov founding) — the trigger was the scope-edge note on drilling-engineering's `artificial-lift-method-selection.md`.
