---
title: "API Spec 17J — Specification for Unbonded Flexible Pipe"
slug: api-17j
code_id: api-17j
publisher: API
revision: "4th Edition (2014, addendum 2018)"
jurisdiction: "industry standard for offshore subsea production"
instrument_type: specification
supersedes: None
extraction_policy: metadata-only
raw_copy_allowed: false
sources:
  - https://www.api.org/products-and-services/standards/important-standards-announcements/standard-17j
tags: [api-17j, flexible-pipe, unbonded, subsea, offshore, riser, dynamic-flexible, sxqs, vivs]
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
also_known_as: [api-spec-17j]
---

# API Spec 17J — Specification for Unbonded Flexible Pipe

Bounded metadata-only resolver page for downstream `Citation(...)` callers under the calc-citation contract at `.claude/rules/calc-citation-contract.md`. Page contains no clause text, layer-property tables, design formulas, or testing-protocol detail; the procedural detail must be read from a procured copy of the publisher source. The companion long-slug page `api-spec-17j.md` predates this canonical short-slug entry and is retained as historical alias.

## Scope

API Spec 17J specifies design, materials, fabrication, testing, and documentation requirements for unbonded flexible pipe. Used for static and dynamic subsea applications: production risers, flowlines, and jumpers. The specification covers metallic and polymeric layer functional requirements, qualification protocols, and minimum manufacturer documentation deliverables. It does not cover bonded flexible pipe (which is governed by API Spec 17K) nor ancillary equipment such as end fittings beyond their interface to the pipe body (covered under API Spec 17L1 and API Spec 17L2).

## Revision history

- 1st Edition — 1996
- 2nd Edition — 1999
- 3rd Edition — 2008
- 4th Edition — 2014 (current)
- Addendum — 2018

## Key sections

- Section 4 — Design and analysis requirements
- Section 5 — Layer specifications (carcass, pressure-sheath, tensile-armor, anti-wear, outer-sheath)
- Section 6 — Materials qualification
- Section 7 — Fabrication
- Section 8 — Testing
- Section 9 — Documentation and quality
- Annex A — Factory acceptance test (FAT), system integration test (SIT), pre-installation test (PIT), and commissioning protocols
- Annex B — Service-life prediction methodology

## Practitioner application

- Operators specifying flexible-pipe procurement (riser and flowline procurement packages).
- Manufacturers — TechnipFMC, Subsea7, NOV (formerly NKT Flexibles), Saipem.
- Class societies — DNV, ABS, BV, LR — used in conjunction with DNV-RP-F112 for HISC-susceptibility envelopes on duplex tensile-armor wires under cathodic protection.
- Certification chain typically pairs API Spec 17J with API RP 17B (recommended practice for unbonded flexible-pipe selection and use).

## Industry adoption

API Spec 17J is the global default for unbonded flexible pipe specification. Sister codes form a complete flexible-pipe family:
- **API Spec 17K** — bonded flexible pipe.
- **API Spec 17L1** — ancillary equipment (bend stiffeners, bend restrictors, buoyancy modules).
- **API Spec 17L2** — ancillary equipment qualification testing.
- **DNV-OS-F201** — dynamic riser companion design code (adjacent technology envelope, applies to both metallic and flexible risers).
- **BS EN ISO 13628-2** — BSI/ISO adopted technical equivalent of API 17J (UK jurisdictional traceability).

## Cross-references

- [api-rp-17b](api-rp-17b.md) — companion recommended practice for unbonded flexible-pipe selection and use
- [api-spec-17j](api-spec-17j.md) — historical long-slug alias; retained for backward link compatibility
- [dnv-rp-f112](dnv-rp-f112.md) — HISC of duplex tensile-armor wires under cathodic protection
- [api-17e](api-17e.md) — subsea umbilicals sister-specification
- [bs-13628-2-flexible-pipe-subsea](bs-13628-2-flexible-pipe-subsea.md) — BSI/ISO technically-equivalent adoption
- Cathodic protection of flexible-pipe carcass, tensile-armor, and outer-sheath: see engineering-standards `concepts/cathodic-protection.md` (when authored)

**Cross-wiki bridges:**

- [IGC Code](../../../lng-projects/wiki/standards/igc-code.md) — offshore-LNG-loading-service interface for offshore loading terminals + STS transfer hoses; flexible-pipe envelopes apply to cryogenic LNG transfer through the IGC Code Ch.5 cargo-handling provisions.
- [MARPOL 73/78](../../../maritime-law/wiki/standards/marpol-73-78.md) — **bidirectional bridge**: API Spec 17J's design, materials, fabrication, and integrity-management requirements for unbonded flexible pipe directly affect oil-pollution-prevention performance of offshore subsea production systems regulated by MARPOL Annex I. The dominant flexible-pipe failure modes catalogued under API Spec 17J + API RP 17B service-life prediction methodology — **carcass collapse** (annulus flooding, hydrostatic crush), **tensile-armor wire fracture** (corrosion-fatigue, HISC of duplex wires under cathodic protection per DNV-RP-F112), **end-fitting leakage** (epoxy-resin debonding, vent-port blockage), **outer-sheath rupture** (seawater ingress to annulus, accelerated tensile-armor corrosion), and **pressure-sheath aging** (CO2/H2S permeation, polymer plasticization) — feed pollution-incident root-cause analysis and MARPOL Annex I non-conformance inquiries when subsea releases reach the marine environment from FPSO / FSO / subsea-tieback systems. Industry-loss databases (OGP, IADC, DNV) map flexible-riser-failure incidents onto Annex I oil-pollution reportable thresholds; the API 17J integrity-management envelope and the MEPC casualty-reporting regime share root-cause-analysis vocabulary through this bridge. The pairing also feeds Annex VI air-pollution accounting where flexible-riser failure triggers blowdown/flaring events on host floating production systems.

- Calc citation contract: `.claude/rules/calc-citation-contract.md`

## Where to find the full text

API Publications subscription required; ANSI catalog also lists the document. The publisher-derivative full text is **not** stored in this repo per the vendor-derivative deny-list governance in workspace-hub #2482. Calc-citation callers resolve only against this page's frontmatter (`code_id`, `publisher`, `revision`); they do not require body text.
