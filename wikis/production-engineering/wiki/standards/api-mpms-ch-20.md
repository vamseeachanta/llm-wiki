---
title: "API MPMS Chapter 20 — Allocation Measurement"
code_id: api-mpms-ch-20
publisher: American Petroleum Institute
revision: "verify-at-publish-time"
jurisdiction: international
tags: [standard, api, mpms, allocation-measurement, allocation-by-difference, allocation-by-proportion, uncertainty-allocation, production-accounting, custody-transfer-bridge]
sources:
  - api-mpms-ch-20
added: 2026-05-16
last_updated: 2026-05-16
---

# API MPMS Chapter 20 — Allocation Measurement

## Scope

API MPMS Chapter 20 is the practitioner-canonical publisher-framework for **allocation measurement** in petroleum production operations. It provides the structured framework that bridges custody-transfer-grade measurement at facility-export or sales meters back to per-well, per-stream allocated volumes that are then booked to leases, partners, and royalty accounts.

The chapter sits within the broader API Manual of Petroleum Measurement Standards (MPMS) framework (introduced in [Custody-Transfer Overview](../concepts/custody-transfer-overview.md)), and is the structural anchor that production-allocation procedures cite. It coexists with Chapters 4, 5, 6, 8, 11, 14, and 21 (which cover the custody-transfer-grade measurement technology and procedures that produce Chapter 20's measurement inputs), and with Chapter 13 (statistical aspects, which bridges to the uncertainty-quantification framework used in allocation arithmetic).

**Edition / revision note** — this page records the revision field as `verify-at-publish-time`. API MPMS Chapter 20 is published in multiple parts (subchapters) covering different facets of allocation measurement; specific parts and their currently-active editions are subject to periodic API revision and reaffirmation cycles. The current edition status should be verified against the API publication catalog at the time the page is consumed. Operator-side procedures pin to a specific edition in the contract; this wiki page does not fabricate a revision year in the absence of independent verification (per the Phase 4 paywalled-standards fact-verification discipline).

## Why operators read it

- **Allocation policy basis** — operators specifying allocation methodology in joint-operating agreements, partner-allocation procedures, royalty-payment procedures, and field-development AFEs cite Chapter 20 as the structural framework.
- **Allocation-by-difference vs allocation-by-proportion** — Chapter 20 names and frames both canonical methods (see [Production Allocation](../concepts/production-allocation.md) for the per-well/per-stream context) and provides the structured methodology that allocation procedures select from.
- **Uncertainty allocation across the measurement chain** — Chapter 20 addresses how uncertainty from custody-transfer-grade meters propagates into per-well allocated volumes (see [Flow-Measurement Uncertainty](../concepts/flow-measurement-uncertainty.md) for the GUM-framework consumption pattern).
- **Reconciliation framing** — the chapter frames the closure-residual reconciliation activity that operators run monthly (or more frequently for operational-allocation purposes) — see [Well Test and Reconciliation](../concepts/well-test-and-reconciliation.md) for the workflow context.
- **Audit and dispute resolution** — partner-allocation disputes and royalty-payment disputes typically adjudicate by reference to the documented allocation procedure, which in turn cites Chapter 20 as the structural framework. The chapter's role in the dispute-resolution framework is what makes its adoption widespread.

## Methodology (structural overview, paraphrased)

The exact section labels, equation forms, and worked-example numerics are not transcribed here (paywalled standard, paraphrase-only discipline); the structural intent is summarised:

- **Measurement chain definition** — Chapter 20 starts by defining the measurement chain from per-well measurement (well-test or MPFM) through commingling through custody-transfer-grade fiscal measurement at the facility export. Each measurement event in the chain carries an uncertainty that propagates into the allocation arithmetic.
- **Theoretical contribution computation** — each well's theoretical contribution to the commingled stream over an allocation period is computed from its periodic-test-derived rate scaled to its producing time across the period. The structural form is straightforward; operational complexity sits in well-test-rate stability and in the producing-time accounting (uptime accounting must reconcile against control-system event logs).
- **Method-selection framework** — the chapter frames both allocation-by-proportion and allocation-by-difference (see [Production Allocation](../concepts/production-allocation.md) for the per-well-per-stream framing) and provides the basis for operator selection. Method selection is an operator-side accounting policy and is documented in the production-allocation procedure.
- **Uncertainty-allocation framework** — Chapter 20 addresses how the uncertainty on the measured commingled volume (the custody-transfer meter uncertainty) and the uncertainties on the per-well theoretical contributions combine into per-well allocated-volume uncertainties. The framework is GUM-consistent (see [Flow-Measurement Uncertainty](../concepts/flow-measurement-uncertainty.md)) and applies the law of propagation of uncertainty across the allocation arithmetic.
- **Reconciliation procedure** — the closure residual is computed period-by-period; the chapter frames the residual disposition (under allocation-by-proportion, residual distributes proportionally; under allocation-by-difference, residual concentrates in the designated well).
- **Procedural documentation requirements** — the chapter sets expectations on the documentation that allocation procedures should carry: method election, measurement-chain documentation, well-test schedule and history, reconciliation history, audit trail. Documentation completeness is what enables dispute-resolution.

## Allocation-by-difference vs allocation-by-proportion (structural framing)

Both methods are framed by Chapter 20 at structural level; selection is an operator-side accounting-policy decision:

**Allocation by proportion** — each well's allocated volume is its theoretical-contribution fraction (well theoretical contribution / sum of theoretical contributions) times the measured commingled volume. The closure residual is distributed across all wells in proportion to their contribution. Symmetric and transparent; dominant in onshore lease-allocation practice and in most partner-allocation contexts.

**Allocation by difference** — one designated well is allocated as the difference between the measured commingled volume and the sum of the other wells' theoretical contributions. Other wells take theoretical contribution at face value; designated well absorbs all closure residual. Used when one well dominates the commingled stream or when one well's metering is materially less certain than the others.

See [Production Allocation](../concepts/production-allocation.md) for the per-well-per-stream worked framing and the operator-policy considerations.

## Uncertainty allocation across the chain

A central methodological contribution of Chapter 20 is the framework for **propagating uncertainty** from the measurement chain into per-well allocated-volume uncertainties. The structural intent (paraphrased; see GUM consumption in [Flow-Measurement Uncertainty](../concepts/flow-measurement-uncertainty.md)):

- **Custody-transfer meter uncertainty** — the closure-reference uncertainty bounds the achievable allocation accuracy. Per-well allocation uncertainty cannot be smaller than the custody-transfer-meter uncertainty.
- **Well-test rate uncertainty** — the per-well theoretical-contribution input uncertainty propagates into per-well allocated-volume uncertainty through the allocation arithmetic.
- **GOR and water-cut sampling uncertainty** — the chemistry-input uncertainty enters the three-phase allocation arithmetic separately on the gas and water streams.
- **Period-rate-drift uncertainty** — the gap between the test rate (at test time) and the well's true rate across the allocation period contributes uncertainty that grows with the test-to-period gap.

The structural form is GUM-consistent (sum-of-squared-partial-derivatives propagation with covariance handling); the operational form follows the allocation-method selection.

## Cross-references

- [Production Allocation](../concepts/production-allocation.md) — router page; allocation-factor methodology and theoretical-vs-actual reconciliation framing that consumes this chapter's framework
- [Well Test and Reconciliation](../concepts/well-test-and-reconciliation.md) — periodic well-test workflow that produces the per-well theoretical-contribution input to Chapter 20 allocation arithmetic
- [GOR and Water-Cut Tracking](../concepts/gor-and-water-cut-tracking.md) — chemistry inputs to the three-phase allocation arithmetic
- [Custody-Transfer Overview](../concepts/custody-transfer-overview.md) — custody-transfer measurement chain that produces the closure-reference measured volume
- [Flow-Measurement Uncertainty](../concepts/flow-measurement-uncertainty.md) — GUM-framework uncertainty propagation consumed by Chapter 20's uncertainty-allocation methodology

## Adjacent standards

- **API MPMS Chapters 4, 5, 6** — Proving, Metering, Metering Assemblies; the custody-transfer-grade liquid measurement framework that produces inputs to Chapter 20 allocation arithmetic
- **API MPMS Chapter 8** — Sampling; sample-representativeness methodology consumed by GOR / water-cut sampling on well tests and custody transfer
- **API MPMS Chapter 11** — Physical Properties Data (volume-correction factors); applied to measurement results in the allocation arithmetic
- **API MPMS Chapter 13** — Statistical Aspects of Measurement and Sampling; bridges to GUM uncertainty quantification
- **API MPMS Chapter 14** — Natural Gas Fluids Measurement; gas-stream measurement methodology
- **API MPMS Chapter 21** — Electronic Metering Systems; EFM (electronic flow computer) audit-trail framework that allocation arithmetic relies on
- **ISO/IEC Guide 98-3 (GUM)** — Guide to the Expression of Uncertainty in Measurement; the international metrological framework consumed by Chapter 20's uncertainty-allocation methodology
- **ISO 5168** — Measurement of fluid flow — Procedures for the evaluation of uncertainties (flow-measurement-specific GUM extension)
- **Energy Institute (UK) HM Series** — UK metering-standards counterpart to API MPMS; in North-Sea operations the HM Series is often cited alongside API MPMS Chapter 20 for allocation methodology

## Public references

- **API** — official publication page for API MPMS Chapter 20 (current edition retrievable from api.org). Operators specifying allocation procedures pin to a specific edition.
- **API MPMS** — the broader Manual of Petroleum Measurement Standards corpus; Chapter 20 sits within and consumes the methodology of other MPMS chapters.
- **Smith Jr., M.** — *Practical Industrial Flow Measurement*, Wiley 2007 (ISBN 978-0-470-04162-7). Practitioner reference for the measurement-technology context within which allocation arithmetic operates.
- **Miller, R. W.** — *Flow Measurement Engineering Handbook*, 3rd edition, McGraw-Hill 1996 (ISBN 978-0-07-042366-4). Comprehensive metering reference covering allocation-relevant measurement technology.
- **Lyons, W. C. (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, Elsevier (ISBN 978-0-7506-7785-1). Production-operations chapters cover allocation methodology in the broader operations context.
- **SPE OnePetro allocation literature** — practitioner corpus on allocation field cases, multiphase-meter allocation duty, virtual-metering for allocation, and partner-allocation contractual frameworks.

## Notes

- API MPMS Chapter 20 is published in multiple parts (subchapters); specific parts and their currently-active editions are subject to periodic API revision and reaffirmation. The `revision` frontmatter field is recorded as `verify-at-publish-time` pending independent fact-verification of the currently-active edition at consumption time. Operators specifying allocation procedures in AFE / joint-operating-agreement / partner-allocation documents should pin to a specific edition.
- The standard is paywalled. This wiki paraphrases the structural intent and references the standard for operators who already have a licensed copy. No verbatim text reproduced (paraphrase-only discipline; >30-word transcription bar).
- The methodology framed by Chapter 20 is implemented in operator-side production-accounting systems, in midstream-pipeline allocation-engine systems, and in third-party measurement-and-allocation services. The standard provides the structural framework; the implementations carry the operational and contractual specifics. Allocation procedures themselves are operator-and-partner documents that cite the standard.
- This page is the L0-prose standards anchor for the production-engineering Phase 5 production-accounting-and-measurement cluster. Concept-page consumers ([Production Allocation](../concepts/production-allocation.md), [Well Test and Reconciliation](../concepts/well-test-and-reconciliation.md), [Custody-Transfer Overview](../concepts/custody-transfer-overview.md), [Flow-Measurement Uncertainty](../concepts/flow-measurement-uncertainty.md)) link here for the publisher-framework context.
