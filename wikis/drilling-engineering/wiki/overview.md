---
domain: drilling-engineering
created: 2026-05-13
last_updated: 2026-05-13
---

# Overview: Drilling Engineering

This wiki captures **drilling-rig technical specifications and drilling-engineering practice** as a structured knowledge corpus, with downstream use cases including AI-assisted drilling-tender evaluation, offset-well analysis automation, and rig-fleet comparison.

## Strategic role

Founded 2026-05-13 by user directive. The corpus is the load-bearing knowledge layer for any downstream effort that needs to reason over drilling-rig capabilities, tender bids, well-plan inputs, or AFE construction. Per the broader [llm-wiki strategic role](../../../README.md), gaps in coverage are first-class defects — a missing rig-spec or standard here is a real product hole for the AI agents and decision-support tools that ground on this corpus.

The founding source page — [Papkov (2026) — Drilling-Tender AI Agent](sources/papkov-2026-drilling-tender-ai-agent.md) — captures a practitioner-stated problem: "Most operators—particularly independents—award drilling service contracts based on incomplete technical evaluation." The implied data-quality dependency (rigorous evaluation needs rigorous source data on rigs, equipment, and offset wells) is exactly what this wiki is built to satisfy.

## Scope (in)

- **Rig classes and individual rigs** — jackup, semi-submersible, drillship, platform rig, land rig, modular MODU, special-purpose (arctic, harsh-environment, ultra-deepwater). Specific named rigs as `entities/`.
- **Drilling equipment** — derrick / mast / substructure (hoisting), rotary table / top drive (rotating), mud pumps / mud system (circulating), BOP stack / well-control hardware. Specific equipment models as `entities/`.
- **Drilling-fluid systems** — mud types, additives, fluid loss, ECD management.
- **Well design and planning** — well plan, casing program design, BHA, directional / horizontal-well design, drilling-program optimization.
- **Drilling-tender process** — AFE construction, RFP scoping, bid evaluation methodology, offset-well analysis, contractor performance benchmarking.
- **AI/ML applied to drilling** — practitioner literature, agent prototypes, technical-evaluation automation.

## Scope (out)

- **Production operations** post-completion (production engineering, artificial lift, surface facilities)
- **Reservoir engineering** — characterization, simulation, recovery-factor analysis
- **Downstream** — refining, petrochemicals (LNG terminals are in `lng-projects/`)
- **Vendor-confidential drilling-equipment manuals** — vendor PDFs stay off-repo per the 2026-05-05 governance rule
- **Generic project management** — drilling-specific PM concepts (rig-day economics, NPT / IPT analysis) are in scope; generic PM theory is not

## Cross-wiki linkages

- `marine-engineering/` — MODU stability, transit / mooring / station-keeping, marine operations during rig-move
- `naval-architecture/` — drillship hull design, MODU intact and damage stability (the [Damage Stability](../../naval-architecture/wiki/concepts/damage-stability.md) and [Intact Stability Criteria](../../naval-architecture/wiki/concepts/intact-stability-criteria.md) pages are direct dependencies for drillships and semis)
- `engineering-standards/` — API drilling specs (4F structures, 7K equipment, 8C hoisting), IADC standards
- `asset-management/` — drilling-rig integrity, safety-critical-element classification for rigs as offshore assets

## Structured rig-fleet data — pointer to worldenergydata

This wiki holds **knowledge and methodology** (rig classes, MODU framework, API/IADC standards, Papkov AI-agent consumer pack). The **structured rig-fleet data corpus** lives in a sibling repo:

- **Repository**: [vamseeachanta/worldenergydata](https://github.com/vamseeachanta/worldenergydata) — public
- **Curated CSV**: [`data/modules/vessel_fleet/curated/drilling_rigs.csv`](https://github.com/vamseeachanta/worldenergydata/blob/main/data/modules/vessel_fleet/curated/drilling_rigs.csv) (2,211 rigs, BSEE-WAR-anchored, refreshed 2026-05-05)
- **Vendor-scrape raw JSON**: [`data/modules/vessel_fleet/raw/contractor_scrape/`](https://github.com/vamseeachanta/worldenergydata/tree/main/data/modules/vessel_fleet/raw/contractor_scrape) (Noble + Seadrill captured 2026-02-13; Transocean / Borr scrapable per validation doc but not yet captured)
- **Site validation provenance**: [`docs/data/rig-fleet-website-validation.md`](https://github.com/vamseeachanta/worldenergydata/blob/main/docs/data/rig-fleet-website-validation.md) (2026-02-13 contractor-site accessibility audit)
- **Tracker issue for vendor→curated merge**: [worldenergydata#127 WRK-1204](https://github.com/vamseeachanta/worldenergydata/issues/127)

Per the off-repo intel routing convention, **vendor-marketing and structured-data content does not go into this CC-BY-4.0 wiki**. The 6 drilling-contractor fleet-entity stubs in this wiki (Transocean, Valaris, Noble, Diamond Offshore, Seadrill, H&P FlexRig) are knowledge-layer anchors pointing at worldenergydata as the data home.

## Seed roadmap (post-founding ingests)

The following are anticipated near-term ingests, listed here as scope intent and not yet executed:

1. **API Spec 4F** — Specification for Drilling and Well Servicing Structures (`standards/api-spec-4f.md`)
2. **API Spec 7K** — Drilling and Well Servicing Equipment (`standards/api-spec-7k.md`)
3. **API Spec 8C** — Drilling and Production Hoisting Equipment (`standards/api-spec-8c.md`)
4. **IADC Drilling Manual** — industry-canonical practitioner reference (`sources/iadc-drilling-manual.md`)
5. **IADC Daily Drilling Report (DDR) format** — standard reporting taxonomy (`concepts/iadc-ddr-format.md`)
6. **Rig-class concept pages** — jackup, semi-submersible, drillship, platform rig, land rig (each as a concept page)
7. **Well-plan / AFE / offset-well concept pages** — the procurement-input artifacts named in the Papkov post
