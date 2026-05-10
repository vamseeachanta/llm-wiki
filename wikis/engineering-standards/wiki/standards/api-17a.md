---
title: "API Spec 17A — Specification for Subsea Wellhead and Christmas Tree Equipment"
slug: api-17a
code_id: api-17a
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
tags: [api-17a, subsea-wellhead, christmas-tree, subsea-production]
added: 2026-05-10
last_updated: 2026-05-10
domain: engineering-standards
legacy_slug: api-spec-17a
also_known_as: [api-spec-17a]
---

# API Spec 17A — Specification for Subsea Wellhead and Christmas Tree Equipment

Bounded metadata-only resolver page for downstream `Citation(...)` callers under the calc-citation contract at `.claude/rules/calc-citation-contract.md`. Page contains no clause text, system-architecture diagrams, design formulas, or testing-protocol detail; the procedural detail must be read from a procured copy of the publisher source. The legacy long-slug pairing `api-spec-17a` is retained as historical alias via `legacy_slug` for backward link compatibility.

## Scope

API Spec 17A is the foundational specification for subsea-production-system design and operation. It defines the system-level framework — pressure-control philosophy, isolation-barrier policies, valve-block topology, and field-architecture requirements — that the rest of the API 17-series component specifications plug into. The standard governs subsea wellhead and christmas tree equipment as the load-bearing pressure boundary between the well and the topsides production facility, covering the integration interfaces with subsea trees (per API 17D), production umbilicals (per API 17E), flexible pipe (per API 17J), and ROV intervention systems (per API 17H). It does not by itself reproduce the detailed component-level qualification rules of those companion specifications; rather it sets the system-level requirements those components must satisfy when assembled into a complete subsea production system.

## Revision history

- 1st Edition — 1996 (initial publication as systems-level subsea umbrella)
- 2nd Edition — 2006 (dual-numbered with ISO 13628-1, harmonized international scope)
- 3rd Edition — 2017 (current widely-deployed edition)
- Subsequent revisions — consult API publications catalog for the current edition before procurement use

## Key sections

- Section 4 — System design philosophy (pressure-control, isolation barriers)
- Section 5 — Field architecture and tie-in requirements
- Section 6 — Component-interface specifications (tree, manifold, umbilical, riser interfaces)
- Section 7 — System integration testing (SIT) and pre-installation testing (PIT)
- Section 8 — Installation, commissioning, and operations
- Section 9 — Documentation and quality
- Annex — System-level FAT/SIT/PIT protocols and operability verification

## Practitioner application

- Operators specifying subsea-development field architecture (greenfield + brownfield tie-back).
- Subsea EPCs — TechnipFMC, Subsea7, Saipem, McDermott, Aker Solutions — for system-integration scope of work.
- Class societies — DNV, ABS, BV, LR — for subsea-production-system certification chains.
- Certification chain typically pairs API Spec 17A with API Spec 17D (trees), API Spec 17E (umbilicals), API Spec 17F (subsea control systems), API Spec 17H (ROV interfaces), and API Spec 17J (flexible pipe).

## Industry adoption

API Spec 17A is the global default for subsea-production-system specification. It anchors the API 17-series family:

- **API Spec 17D** — subsea wellhead and tree equipment (component-level).
- **API Spec 17E** — subsea umbilicals.
- **API Spec 17F** — subsea control systems.
- **API Spec 17H** — ROV interfaces for subsea production.
- **API Spec 17J** — unbonded flexible pipe.
- **ISO 13628-1** — international parallel; the 17A revisions are dual-numbered with ISO 13628-1.

## Cross-references

- [api-17d](api-spec-17d.md) — subsea wellhead and tree equipment (component spec under the 17A umbrella)
- [api-17e](api-17e.md) — subsea umbilicals sister-specification
- [api-17h](api-17h.md) — ROV intervention interface specification
- [api-17j](api-17j.md) — unbonded flexible pipe specification
- [api-spec-6a](api-spec-6a.md) — surface wellhead/tree progenitor specification

**Cross-wiki bridges:**

- Subsea-system design interfaces with the broader offshore-production envelope; see also marine-engineering and naval-architecture wikis for adjacent scopes.
- Calc citation contract: `.claude/rules/calc-citation-contract.md`

## Where to find the full text

API Publications subscription required; ANSI catalog also lists the document. The publisher-derivative full text is **not** stored in this repo per the vendor-derivative deny-list governance in workspace-hub #2482. Calc-citation callers resolve only against this page's frontmatter (`code_id`, `publisher`, `revision`); they do not require body text.
