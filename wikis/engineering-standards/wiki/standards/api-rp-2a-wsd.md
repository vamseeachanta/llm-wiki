---
title: "API RP 2A-WSD — Fixed offshore platform planning, design, construction (bounded summary)"
tags: ["api", "standards", "offshore-structures", "metadata-only"]
added: 2026-05-02
last_updated: 2026-05-09
domain: engineering-standards
code_id: api-rp-2a-wsd
publisher: API
revision: "22e-2014-r2025"
revision_source: https://store.accuristech.com/standards/api-rp-2a-wsd-r2025
verified_on: 2026-05-02
public_url: https://www.api.org/products-and-services/standards
publisher_catalog_url: https://www.api.org/products-and-services/api-publications
sources:
  - /mnt/ace/O&G-Standards/API/Recommended-Practice/API_RP_2A-WSD_22nd_Edition_Nov_2014.pdf
extraction_policy: metadata-only
raw_copy_allowed: false
---

# API RP 2A-WSD — Fixed offshore platform planning, design, construction

## Scope

API recommended practice covering planning, design, and construction considerations for fixed offshore platforms using working stress design (WSD) methodology. Coverage spans:

- Site characterization and metocean criteria for fixed-platform design;
- Structural analysis (in-place strength, fatigue, accidental, seismic, ice);
- Tubular member design, joint capacity, and connection detailing under WSD allowable-stress framework;
- Foundation design (driven piles, drilled piles, suction caissons) including axial and lateral capacity;
- Materials, welding, and fabrication tolerances;
- Inspection, monitoring, assessment, and re-qualification of existing platforms.

API RP 2A-WSD is the working-stress-design companion to API RP 2A-LRFD (load-and-resistance-factor design) and is the dominant fixed-platform standard for the US Gulf of Mexico shelf inventory. It interfaces upstream with API RP 2MET (metocean), API RP 2GEO (geotechnical), and API RP 2SIM (structural integrity management).

## Revision history

- **22nd edition, November 2014** — Current substantive edition; on-disk reference revision (`/mnt/ace/O&G-Standards/API/Recommended-Practice/API_RP_2A-WSD_22nd_Edition_Nov_2014.pdf`).
- **Reaffirmed 2025 (R2025)** — Reaffirmation of the 22nd edition without substantive technical change; the citation revision token is `22e-2014-r2025`.
- **Earlier editions** — 21st edition (December 2000) was the long-running prior reference; revisions before that go back to the original 1969 first edition. Older Gulf of Mexico inventory was designed against earlier editions and re-qualified under API RP 2SIM rather than re-designed against the current edition.

## Key sections

- **Section 1 — Planning** — facility planning, environmental criteria selection, exposure-category framework (L-1, L-2, L-3 manned/unmanned).
- **Section 2 — Design criteria + procedures** — load combinations, WSD allowable-stress increments for one-third overstress under environmental loads.
- **Section 3 — Loads** — gravity, environmental, seismic, ice, accidental.
- **Section 4 — Structural steel design** — tubular members, joints, fatigue under WSD framework.
- **Section 5 — Connections** — tubular joint capacity, joint can design, gusset and stiffener detailing.
- **Section 6 — Foundation design** — pile axial capacity (skin friction + end bearing), lateral capacity (p-y curves), pile-driveability, mudmat design.
- **Section 7 — Other systems + components** — risers, conductor framing, boat landings, walkways.
- **Section 8 — Material** — structural steel grades, weldability requirements.
- **Section 9 — Welding** — qualification, NDE, acceptance criteria.
- **Section 14 — Survey + assessment + management of existing structures** — re-qualification framework for legacy platforms.
- **Section 17 — Assessment of existing platforms** — exposure-category-based assessment criteria for hurricane-survivability of legacy GOM jackets.

## Practitioner application

In practice, API RP 2A-WSD is the cited basis for:

- **Tubular member capacity** under combined axial + bending + hydrostatic conditions for new fixed jackets;
- **Tubular joint capacity** (T, Y, K, X joint geometries) with the WSD allowable-stress methodology;
- **Pile capacity** for driven steel pipe piles in clay (alpha, lambda methods) and sand (Nq, beta methods);
- **Hurricane re-qualification** of legacy Gulf of Mexico jackets per Section 17, with consequence-class L-1/L-2/L-3 driving the metocean recurrence interval;
- **Documentation deliverables** for in-place, fatigue, seismic, and accidental analyses on new-build platforms.

## Industry adoption

- **US Gulf of Mexico** — the dominant fixed-platform standard; BSEE incorporates API RP 2A by reference in 30 CFR 250 Subpart I for OCS facility design;
- **International operators** — frequent primary or co-cited use on shelf-water fixed installations outside the US;
- **Class societies** — ABS, DNV, BV, LR all reference API RP 2A as an acceptable basis for offshore-jacket design when it is the operator's selected primary standard;
- **Cross-standard pairing** — typically co-cited with ISO 19902 (the ISO peer fixed-steel-structure standard) on international projects; ISO 19902 is LRFD-based and parallels API RP 2A-LRFD more directly than API RP 2A-WSD.

## Why this page exists

Resolver target for digitalmodel `Citation` instances per `.claude/rules/calc-citation-contract.md`. The page exists to satisfy fail-closed citation resolution against the API frontmatter contract (`code_id`, `publisher`, `revision`); it deliberately contains no clause text, no equations, no design-criteria tables.

## Where to find the full text

- Raw PDF (read-only, vendor-derivative; do NOT copy into git per #2482):
  `/mnt/ace/O&G-Standards/API/Recommended-Practice/API_RP_2A-WSD_22nd_Edition_Nov_2014.pdf`
- Publisher catalog: <https://www.api.org/products-and-services/standards>
- Reaffirmation status (R2025): <https://store.accuristech.com/standards/api-rp-2a-wsd-r2025>
- Internal callers (top references via grep): see digitalmodel/src/ for modules that name "API RP 2A" — top-frequency code paths under `digitalmodel/src/digitalmodel/marine_ops/` and `digitalmodel/src/digitalmodel/orcaflex/`.

## Cross-references

- [api-rp-2met](api-rp-2met.md) — metocean criteria input
- [api-rp-2geo](api-rp-2geo.md) — geotechnical inputs (pile capacity)
- [api-rp-2sim](api-rp-2sim.md) — structural integrity management (in-service phase)
- [api-17e](api-17e.md) — sibling subsea umbilicals stub (same publisher)
- [iso-19902](iso-19902.md) — ISO peer fixed-steel-structure standard (LRFD)
- Calc citation contract: `.claude/rules/calc-citation-contract.md`
