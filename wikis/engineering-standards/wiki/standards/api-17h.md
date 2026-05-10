---
title: "API Spec 17H — Specification for Remotely Operated Vehicles for Subsea Production"
slug: api-17h
code_id: api-17h
publisher: API
revision: "latest edition (consult API publications)"
jurisdiction: "industry standard for offshore subsea production"
instrument_type: specification
supersedes: None
extraction_policy: metadata-only
raw_copy_allowed: false
sources:
  - https://www.api.org/products-and-services/standards
public_url: https://www.api.org/products-and-services/standards
publisher_catalog_url: https://www.api.org/products-and-services/standards
tags: [api-17h, rov, remotely-operated-vehicle, subsea-intervention, subsea-production]
added: 2026-05-10
last_updated: 2026-05-10
domain: engineering-standards
legacy_slug: api-spec-17h
also_known_as: [api-spec-17h]
---

# API Spec 17H — Specification for Remotely Operated Vehicles for Subsea Production

Bounded metadata-only resolver page for downstream `Citation(...)` callers under the calc-citation contract at `.claude/rules/calc-citation-contract.md`. Page contains no clause text, interface-geometry tables, hot-stab port dimensions, or torque-bucket specifications; the procedural detail must be read from a procured copy of the publisher source. The legacy long-slug pairing `api-spec-17h` is retained as historical alias via `legacy_slug` for backward link compatibility.

## Scope

API Spec 17H specifies the standardized ROV-intervention interfaces between subsea production equipment and class-of-vehicle remotely-operated vehicles. Interface taxonomy includes torque-bucket (rotary actuation) geometry, hot-stab port classes (hydraulic fluid transfer), paddle-handle reach envelopes (linear actuation), override-tooling interfaces, and ROV-readable indicator surfaces (lock status, valve position). The standard's intent is class-of-vehicle compatibility: a 17H-compliant ROV must be able to operate any 17H-compliant tree, manifold, or distribution unit without bespoke tooling. Used in conjunction with API Spec 17D (subsea trees), API Spec 17F (subsea control systems), and API Spec 17J (flexible pipe) to ensure the as-installed subsea field can be intervened by a generic-fleet ROV.

## Revision history

- 1st Edition — 2004 (initial publication; harmonized with ISO 13628-8)
- 2nd Edition — 2013 (dual-numbered with ISO 13628-8 second cycle)
- Subsequent revisions — consult API publications catalog for the current edition before procurement use

## Key sections

- Section 4 — Class-of-vehicle ROV definitions (work-class, observation-class)
- Section 5 — Torque-bucket interfaces (Class 1-4 geometry, drive shaft, reaction lugs)
- Section 6 — Hot-stab interfaces (port classes, fluid-cleanliness ratings, sealing)
- Section 7 — Paddle-handle and linear-actuation interfaces
- Section 8 — Override-tooling interfaces (manual valve override, pin-pull, latch-release)
- Section 9 — ROV-readable indicators (lock status, position confirmation, marking)
- Annex — Interface qualification testing and verification protocols

## Practitioner application

- Subsea EPCs and tree manufacturers — TechnipFMC, Aker Solutions, OneSubsea, Baker Hughes — for designing 17H-compliant intervention surfaces.
- ROV operators — Oceaneering, Subsea7, DOF Subsea, Saipem — for fleet ROV-tooling standardization.
- Operators specifying subsea-intervention scope of work for installation, commissioning, and IRM (Inspection, Repair, Maintenance).
- Certification chain typically pairs API Spec 17H with API Spec 17D (trees and tree-cap interfaces), API Spec 17F (subsea control system override paths), and API Spec 17J (flexible-pipe end-fitting intervention surfaces).

## Industry adoption

API Spec 17H is the global default for subsea-intervention interface standardization. Sister codes form the subsea-production envelope:

- **API Spec 17A** — subsea-production-systems master design framework.
- **API Spec 17D** — subsea wellhead and tree equipment (the primary 17H interface consumer).
- **API Spec 17F** — subsea control systems (override and indicator paths).
- **API Spec 17J** — unbonded flexible pipe (end-fitting intervention).
- **ISO 13628-8** — international parallel; the 17H editions are dual-numbered with ISO 13628-8.

## Cross-references

- [api-17a](api-17a.md) — subsea-production-systems master framework that 17H interfaces plug into
- [api-17d](api-spec-17d.md) — subsea trees as the primary 17H interface consumer
- [api-17j](api-17j.md) — flexible-pipe end-fitting intervention surfaces
- [api-17e](api-17e.md) — subsea umbilicals sister-specification
- [api-spec-6a](api-spec-6a.md) — surface-equipment progenitor

**Cross-wiki bridges:**

- ROV-intervention envelope interfaces with marine-operations and offshore-installation scopes; see also marine-engineering wiki for vessel-launched-ROV operability.
- Calc citation contract: `.claude/rules/calc-citation-contract.md`

## Where to find the full text

API Publications subscription required; ANSI catalog also lists the document. The publisher-derivative full text is **not** stored in this repo per the vendor-derivative deny-list governance in workspace-hub #2482. Calc-citation callers resolve only against this page's frontmatter (`code_id`, `publisher`, `revision`); they do not require body text.
