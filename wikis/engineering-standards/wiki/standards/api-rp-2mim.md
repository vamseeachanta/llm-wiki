---
title: "API RP 2MIM — Mooring Integrity Management"
slug: api-rp-2mim
code_id: api-rp-2mim
publisher: API
publisher_full: "American Petroleum Institute"
revision: "1st ed (2019); consult API publications catalog for any subsequent reaffirmation"
jurisdiction: "Global offshore (US GoM, North Sea, West Africa, offshore Brazil, Australia NWS); referenced by class societies"
instrument_type: recommended-practice
supersedes: None
extraction_policy: metadata-only
raw_copy_allowed: false
sources:
  - https://www.api.org/products-and-services/standards
public_url: https://www.api.org/products-and-services/standards
publisher_catalog_url: https://www.api.org/products-and-services/standards
tags:
  - api
  - standards
  - mooring
  - integrity-management
  - station-keeping
  - in-service-inspection
  - rbi
  - floating-production
  - metadata-only
added: 2026-05-10
last_updated: 2026-05-10
domain: engineering-standards
---

# API RP 2MIM — Mooring Integrity Management

**code_id:** `api-rp-2mim` &nbsp;·&nbsp; **publisher:** API (American Petroleum Institute) &nbsp;·&nbsp; **revision:** 1st edition (2019)

> Bounded metadata-only resolver page for downstream `Citation(...)` callers under the calc-citation contract at `.claude/rules/calc-citation-contract.md`. Page contains no clause text, inspection intervals, anomaly-acceptance criteria, or risk-matrix categorizations from the source.

## Scope

API RP 2MIM is the consensus US recommended practice for **integrity management of permanent mooring systems** on floating production units (FPUs): semi-submersibles, spars, FPSOs, TLPs, and similar facilities operating beyond the design return period. It covers an integrity-management lifecycle: system definition and baseline (chain, wire-rope, polyester segments, connectors, anchors, fairleads), threat identification (corrosion, wear, fatigue, overload, anchor drag, foundation degradation, marine growth), inspection strategy selection (general visual, close-visual, NDE, dimensional, anchor-position survey), anomaly disposition (component-level fitness-for-service, replacement, derating), risk-based inspection-interval setting, and re-baselining after life-extension or after mooring-line replacement.

The recommended practice is positioned as the in-service operations counterpart to **API RP 2SK** (mooring system design) and **API RP 2I** (in-service inspection of mooring hardware), pulling them into a coherent integrity-management framework aligned with operator audit and class-society survey expectations.

## Revision history

- **1st edition (2019)** — first published edition; consolidated prior operator-specific mooring-IMS practice and Joint Industry Project recommendations (notably the post-2014 GoM mooring-failure data review) into a single API recommended practice.

Consult the API publications catalog for any subsequent reaffirmation, errata, or addenda before procurement use.

## Key sections

The 1st-edition section structure (verify against the publisher copy in any normative work):

- **Threat assessment** — corrosion (atmospheric, splash-zone, fully-submerged, mud-line, internal-link wear-corrosion), fatigue (out-of-plane bending at fairleads/chain-stoppers, in-plane ultimate-fatigue cycling), overload, foundation/anchor degradation.
- **Component baseline** — chain link diameter, wear measurements, connector identification, polyester rope condition (sheath integrity, abrasion), wire-rope socket and termination condition.
- **Inspection strategy** — risk-based selection across surface visual, ROV close-visual, dimensional measurement, NDT (MPI on accessible chain links / connectors), anchor-position monitoring.
- **Anomaly disposition** — disposition rules for diameter loss, broken wires, link cracking, marine-growth thresholds; pathway into component-level fitness-for-service or replacement.
- **Risk-based inspection** — likelihood/consequence categorization driving interval selection; align with [api-rp-580](api-rp-580.md) / [api-rp-581](api-rp-581.md) RBI methodology adapted to mooring-specific failure modes.
- **Mooring management plan** — documentation, baseline/inspection records, change-management.

## Practitioner application

- FPU operators (offshore O&G majors, IOCs, NOCs operating permanent moorings) maintaining mooring integrity-management plans across the US GoM and global deepwater portfolios.
- Mooring-integrity specialists (Vryhof, Delmar, Bardex, INTECSEA, TechnipFMC) executing IMS lifecycle work for operator clients.
- Class societies (ABS, DNV, BV, LR) reviewing operator IMS plans and conducting mooring surveys against API RP 2MIM-aligned scope.
- Insurance loss-prevention engineers benchmarking operator practice against API RP 2MIM as the de facto mooring-IMS reference.

## Industry adoption

API RP 2MIM is the canonical North American recommended practice for permanent-mooring integrity management and is widely adopted by GoM operators after the 2014 mooring-failure cluster prompted consolidation of disparate operator practices. Internationally it is referenced alongside class-society offshore-mooring rules (DNV-OS-E301, ABS Floating Production Systems guide) and the operations-side companion to API RP 2SK design and API RP 2I inspection. Probabilistic-fatigue inspection-planning specialists pair it with [dnv-rp-c210](dnv-rp-c210.md) for analytical interval-setting on fatigue-driven mooring threats.

## Why this page exists

Resolver target for digitalmodel `Citation` instances per `.claude/rules/calc-citation-contract.md` and substrate-fill landing for the wikilink in `dnv-rp-c210.md` referencing API RP 2MIM mooring-integrity-management practice. Surfaced as 1 of 5 ASME-process/RBI substrate-gap residuals after iter-50 W231 sweep; created under iter-51 W232 ASME-process/RBI substrate-fill batch. **Metadata-only** per spinout 2026-05-05 governance.

## Where to find the full text

API Publications subscription required; ANSI catalog also lists the document. Vendor-derivative full text is **not** stored in this repo per spinout vendor-derivative deny-list governance. Calc-citation callers resolve only against this page's frontmatter (`code_id`, `publisher`, `revision`); they do not require body text.

## Cross-references

- [api-rp-2sk](api-rp-2sk.md) — Stationkeeping systems for floating structures; design-side companion to API RP 2MIM.
- [api-rp-2sim](api-rp-2sim.md) — Structural Integrity Management of Fixed Offshore Structures; jacket-side analogue of mooring IMS scope.
- [dnv-rp-c210](dnv-rp-c210.md) — Probabilistic methods for inspection-planning for fatigue cracks; analytical sister for fatigue-driven mooring-line interval setting.
- [dnv-os-e301](dnv-os-e301.md) — DNV offshore standard for position mooring; design-side international counterpart.
- [api-rp-580](api-rp-580.md) — RBI methodology base; adapted to mooring-specific threats inside API RP 2MIM.
- [api-rp-581](api-rp-581.md) — Quantitative RBI; methodology reference for mooring likelihood/consequence categorization.
- [Risk-Based Inspection (RBI)](../concepts/risk-based-inspection.md) — concept page on RBI paradigm.
- Calc citation contract: `.claude/rules/calc-citation-contract.md`

## Notes

- This page is **metadata-only**; no clause text, inspection intervals, anomaly-acceptance criteria, or risk-matrix categorizations are reproduced from API RP 2MIM. All technical descriptions above are paraphrased general engineering knowledge.
- For normative mooring-IMS work, cite the API-published edition directly (API RP 2MIM, 1st ed 2019, or the current edition at time of citation).
- Substrate-fill resolver created under W232 iter-51 ASME-process/RBI batch (1 reference in `dnv-rp-c210.md`).
