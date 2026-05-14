# Wiki Schema: drilling-engineering

> Founded 2026-05-13 under explicit user signal to build a drilling-rig technical-specs corpus.
> Edit this file to customize wiki conventions for this domain.

## Scope boundary

This wiki covers **drilling engineering and well construction** — drilling-rig technical specifications (jackup / semi-submersible / drillship / platform / land-rig classes), drilling equipment (hoisting, rotating, circulating, well-control), drilling-fluid systems, well planning and design (well plan, casing/tubing design, BHA, directional and horizontal-well design), AFE (Authorization For Expenditure) framing, offset-well analysis, drilling-tender RFP / evaluation methodology, and the practitioner literature applying AI/ML to these problems.

This wiki does **NOT** cover:

- **Production operations** post-completion — production engineering belongs elsewhere
- **Reservoir engineering** — characterization, simulation, recovery factor analysis
- **Downstream** — refining, petrochemicals, LNG-process (LNG terminals are in `lng-projects/`)
- **Subsea production hardware** unrelated to drilling (Christmas trees, jumpers, flowlines)
- **Vendor-confidential drilling-equipment manuals** — vendor PDFs stay off-repo per the 2026-05-05 governance rule

Drilling-rig **as a marine vessel** (stability, transit, mooring) is dual-listed with `naval-architecture/` and `marine-engineering/`; the technical-specs corpus for drilling functions lives here.

## Directory Structure

```
raw/          # Immutable source documents (LLM reads, never modifies)
  papers/     # Academic papers, SPE / IADC papers
  standards/  # Standards documents (API, IADC, ISO drilling-related)
  articles/   # Web articles, blog posts, LinkedIn-essay snapshots
  assets/     # Images and figures extracted from sources
wiki/         # LLM-maintained markdown pages
  index.md    # Content catalog — every page listed with link + 1-line summary
  log.md      # Chronological timeline of ingests, queries, lint passes
  overview.md # High-level domain synthesis
  entities/   # Entity pages (specific rigs, rig classes, drilling-contractor fleets)
  concepts/   # Concept pages (well plan, AFE, offset-well analysis, BHA, tender evaluation)
  sources/    # Source summary pages (one per ingested document)
  comparisons/# Filed query outputs (rig-spec comparisons, tender-evaluation worked examples)
  visualizations/ # matplotlib plots, diagrams
  standards/  # Standards pages (publisher-agnostic; code_id, publisher, revision required)
```

## Conventions

### Frontmatter Schema

All wiki pages use YAML frontmatter (`---` delimited) with the following fields:

| Field | Required | Type | Description |
|-------|----------|------|-------------|
| `title` | **required** | string | Page title |
| `tags` | **required** | list | Classification tags |
| `added` | **required** | date | ISO date when page was created (`YYYY-MM-DD`) |
| `last_updated` | **required** | date | ISO date of last modification (`YYYY-MM-DD`) |
| `sources` | recommended | list | Source documents referenced |
| `domain` | optional | string | Explicit domain classification |
| `cross_links` | optional | list | Cross-wiki references |

### Standards page extra fields (`wiki/standards/*.md`)

| Field | Required | Description |
|-------|----------|-------------|
| `code_id` | required (L0 prose) | Canonical code identifier, e.g. `api-spec-4f`, `api-spec-7k`, `api-spec-8c`, `iadc-drilling-manual` |
| `publisher` | required (L0 prose) | Publishing body, e.g. `API`, `IADC`, `ISO`, `IOGP` |
| `revision` | required (L0 prose) | Revision/edition/year |
| `jurisdiction` | optional | Geographic or regulatory scope |
| `supersedes` | optional | Prior revisions or codes replaced |

> L0-prose enforcement only.

### Page format
- Title in YAML frontmatter (see schema above)
- Tags for categorization
- Cross-references as markdown links: `[[entity-name]]` or `[text](../concepts/topic.md)`

### Index format (index.md)
```yaml
---
last_updated: YYYY-MM-DD
page_count: N
source_count: N
---

## Entities

| Page | Summary | Last Updated |
|------|---------|-------------|

## Concepts

...

## Sources

...

## Standards

...
```

### Log format (log.md)
Each entry starts with a consistent prefix for easy grep:
```
## [YYYY-MM-DD] ingest | Source Title
- Processed: source_file.pdf
- Pages updated: index.md, entities/entity1.md, concepts/concept1.md
- Notes: <brief notes>
```

## Ingest Workflow

1. Read source document
2. Extract key entities (specific rigs, contractor fleets), concepts (well plan, AFE, tender eval), facts (rig specs)
3. Create/update source summary in wiki/sources/
4. Update/create entity pages in wiki/entities/
5. Update/create concept pages in wiki/concepts/
6. Update wiki/index.md with new entries
7. Append entry to wiki/log.md

## Lint Workflow

Check for:

1. Contradictions between rig-spec values across sources
2. Stale claims superseded by newer rig surveys / inspection reports
3. Orphan pages (no inbound links)
4. Missing cross-references to `marine-engineering/` (MODU stability), `naval-architecture/` (drillship hull), `engineering-standards/` (API drilling specs)
5. Concepts mentioned but lacking their own page
6. Data gaps fillable by external sources (IADC Daily Reports format, API specs, IOGP reports)

## Notes

This wiki was founded 2026-05-13 by user directive ("we need to get all technical specs of drilling rigs lined up i.e. all the data; then unleash AI into it"). The founding source page is Papkov (2026) — drilling-tender AI agent prototype, which both motivates the corpus (operators lack rigorous technical evaluation tools) and is a literature data point about applying AI to drilling-tender evaluation. The first follow-on ingests should target the API drilling-rig specs (API Spec 4F drilling-structures, API Spec 7K drilling equipment, API Spec 8C hoisting equipment), IADC standards (drilling manual, daily-report format DDR), and IOGP guidance on rig inspection.
