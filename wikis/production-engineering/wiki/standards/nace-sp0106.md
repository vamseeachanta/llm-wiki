---
title: "NACE SP0106 — Control of Internal Corrosion in Steel Pipelines and Piping Systems"
code_id: nace-sp0106
publisher: AMPP (formerly NACE International)
revision: "2018 reaffirmed edition (current at 2026-05-16; supersedes 2006 original)"
tags: [nace, ampp, internal-corrosion, pipeline, piping, integrity, paywalled-standard]
sources:
  - nace-sp0106
added: 2026-05-16
last_updated: 2026-05-16
---

# NACE SP0106 — Control of Internal Corrosion in Steel Pipelines and Piping Systems

## Scope

NACE SP0106 is the practitioner-canonical standard practice for **integrity-management of internal corrosion in steel pipelines and piping systems** carrying hydrocarbon production fluids, processed liquids, and gas. It defines the structured methodology by which operators identify internal-corrosion threats, deploy a combination of monitoring and mitigation techniques, and verify that the integrity-management program achieves and sustains the intended corrosion-control performance.

NACE was rebranded to AMPP (Association for Materials Protection and Performance) following the NACE-SSPC merger in 2021; the original NACE SP0106 designation remains in active use across operator specifications, regulatory submissions, and procurement documents. The current edition is the 2018 reaffirmation of the 2006 original. Practitioners commonly cite it as "NACE SP0106" or interchangeably as "AMPP SP0106"; both refer to the same standard.

This page is the **standards anchor** for steel-pipeline and -piping internal-corrosion management in the production-engineering wiki. SP0106 complements [ISO 21457](iso-21457.md) (system-level material selection and corrosion-control philosophy) at the line-item operating-management level for internal-corrosion threats specifically.

## Why operators read it

- **Pipeline-and-piping integrity-management framework** — SP0106 provides the methodology that pipeline-and-piping operators use to design, execute, and audit their internal-corrosion integrity-management programs. Adoption is dominant across US onshore production-gathering pipelines, midstream gathering systems, offshore flowlines, and topside-processing piping.
- **Regulator-recognised methodology** — US PHMSA (Pipeline and Hazardous Materials Safety Administration) cites NACE SP0106 in pipeline-integrity-management rulemakings (49 CFR 192 for gas, 49 CFR 195 for liquid). Operators submitting pipeline integrity-management plans typically structure them around SP0106 methodology.
- **Insurance and audit basis** — third-party audit firms verifying operator integrity-management programs use SP0106 as one of the standard methodology references. Insurance underwriters and joint-venture-partner reviewers similarly recognise SP0106 conformance as evidence of competent integrity management.
- **Bridge to operating-time monitoring** — SP0106 explicitly addresses the operating-time monitoring discipline (coupon analysis, ER probe trends, UT survey programs, inhibitor-residual analysis) that translates design-time corrosion-control philosophy into day-to-day operating practice. The standard is therefore a heavily-cited reference in production-time well-integrity work covered by this wiki's [Integrity Monitoring](../concepts/integrity-monitoring.md) page.

## Methodology (structural overview, paraphrased)

The exact clause structure, decision-tree layouts, and specific threshold values are not transcribed here (paywalled standard); the structural intent is captured at framework level:

- **Threat identification** — the methodology requires the operator to identify the credible internal-corrosion threats applicable to each line segment based on the carried fluid composition, operating conditions, and service history. Threat categories typically addressed include sweet (CO2-driven) corrosion, sour (H2S-driven) corrosion, microbiologically-influenced corrosion (MIC), oxygen-ingress corrosion, top-of-line corrosion (TLC) in stratified-flow gas lines, and under-deposit corrosion in lines with solids deposition. The threat-identification step is foundational and frames every subsequent decision.
- **Operating-condition characterisation** — the methodology requires characterisation of the operating conditions that drive the identified threats: fluid composition (water content, water chemistry, dissolved gas partial pressures, microbial activity indicators), operating pressure and temperature ranges, flow regime, and the presence of solids that can support under-deposit attack.
- **Mitigation-strategy selection** — the methodology structures mitigation strategies including chemical inhibition (corrosion inhibitor selection and dosage logic at a programmatic level), biocide treatment for MIC, oxygen scavenging, internal coatings or linings, dehydration to reduce water content, pigging to remove deposits and water hold-up, and material upgrades to corrosion-resistant alloys for high-severity service.
- **Monitoring program** — the methodology specifies a monitoring program that combines direct mass-loss measurement (corrosion coupons per NACE SP0775 methodology), electrical-resistance probe trending, UT and other wall-thickness surveying techniques, inhibitor-residual analysis, microbiological-monitoring techniques, and water-chemistry monitoring. The monitoring program is designed to provide multiple independent indicators of corrosion-control performance rather than depending on a single technique.
- **Performance verification and program adjustment** — the methodology requires that monitoring data be reviewed periodically against the predicted or required performance, with explicit decision logic for adjusting the mitigation program when performance falls short. The program-adjustment loop is the bridge from initial design-time program specification to operating-time program evolution.
- **Documentation and records** — the methodology specifies records that the operator should maintain to support both internal review and external audit: monitoring data, inhibitor-procurement and -injection records, treatment-event records, inspection findings, and program-change rationale.

## Coverage scope

NACE SP0106 explicitly addresses internal-corrosion management of:

- **Hydrocarbon-production pipelines** — flowlines from wellhead manifolds to processing facilities, gathering pipelines collecting production from multiple wells, and trunk lines moving processed product to export points.
- **Processed-product pipelines** — oil-product lines (crude, condensate), gas lines (sales gas, fuel gas), water lines (produced-water disposal, water-injection supply).
- **Topside-processing piping** — separator outlet piping, treater piping, dehydration-unit piping, and the associated headers and manifolds. The discipline crosses the line-item boundary with NACE SP0106 frequently being cited alongside facility-specific standards.
- **Downhole-tubing internal corrosion** — by analogy, the threat-identification and mitigation-strategy framework is widely applied to internal corrosion of production tubing inside the well, although the standard is formally targeted at pipelines and piping rather than downhole tubulars. The framework's applicability to downhole-tubing corrosion is well-established in practitioner literature.

## Boundary with adjacent standards

NACE SP0106 sits in a corrosion-management standards ecosystem with explicit boundaries to adjacent standards:

- **NACE SP0775 / AMPP SP0775** — preparation, installation, analysis, and interpretation of corrosion coupons in oilfield operations. SP0775 provides the line-item coupon methodology that SP0106 monitoring programs deploy. See engineering-standards [AMPP SP0775](../../../engineering-standards/wiki/standards/ampp-sp0775.md).
- **NACE MR0175 / ISO 15156** — sour-service material qualification for carbon steel, low-alloy steel, and corrosion-resistant alloys. MR0175 governs the material-class selection that determines whether a given line is suitable for sour service at all; SP0106 governs the operating-time internal-corrosion management of the line once selected. See engineering-standards [ISO 15156](../../../engineering-standards/wiki/standards/iso-15156.md), [AMPP MR0175 Part 1](../../../engineering-standards/wiki/standards/ampp-mr-0175-pt1.md), [AMPP MR0175 Part 2](../../../engineering-standards/wiki/standards/ampp-mr-0175-pt2.md), [AMPP MR0175 Part 3](../../../engineering-standards/wiki/standards/ampp-mr-0175-pt3.md).
- **ISO 21457** — system-level materials-selection and corrosion-control methodology for upstream production systems. ISO 21457 sits above SP0106 in the standards hierarchy: ISO 21457 specifies the design-time material-selection and corrosion-control philosophy, SP0106 specifies the operating-time internal-corrosion management methodology for steel pipelines and piping selected under that philosophy. See [ISO 21457](iso-21457.md).
- **API RP 581** — risk-based inspection methodology. RBI methodology under API RP 581 typically consumes SP0106-style monitoring data as the input for corrosion-rate distribution that drives inspection-interval optimisation. See engineering-standards [API RP 581](../../../engineering-standards/wiki/standards/api-rp-581.md).
- **API RP 1160 / API RP 1173** — pipeline integrity management (RP 1160 for hazardous-liquid pipelines, RP 1173 for pipeline safety-management systems). These complement SP0106 at the program-management and culture levels; SP0106 provides the internal-corrosion-specific methodology that integrates into a broader pipeline-integrity-management system.
- **Norsok M-506** — Norwegian sector standard for CO2 corrosion-rate calculation; provides one of the predictive-modelling framework options that SP0106 programs use for corrosion-rate prediction during design and program-adjustment review. The framework is described qualitatively in [Corrosion Management](../concepts/corrosion-management.md).

## Operating-time application

SP0106 is the most-cited standards reference in this wiki's operating-time internal-corrosion management discussions because it explicitly addresses the operating-time methodology rather than only design-time material selection. Specific operating-time touch-points include:

- **Coupon-program design** — SP0106 monitoring-program guidance combined with SP0775 line-item coupon methodology gives operators the framework for designing coupon programs that produce defensible operating-time corrosion-rate data.
- **Inhibitor-program management** — the chemical-inhibition mitigation strategy in SP0106 framework requires operating-time verification through inhibitor-residual analysis, corrosion-monitoring response, and program-adjustment when performance is sub-optimal. This is the discipline covered at framework level in [Corrosion Management](../concepts/corrosion-management.md).
- **Pigging-program coordination** — SP0106 monitoring data informs pigging frequency (deposit-removal, water-removal) that supports under-deposit corrosion mitigation and top-of-line corrosion mitigation in stratified-flow gas lines.
- **MIC monitoring and biocide programs** — SP0106 framework requires that microbiologically-influenced corrosion threats receive specific monitoring (microbial counts, sessile-vs-planktonic biofilm characterisation) and mitigation (biocide selection and dosage logic at programmatic level).

## Concept-page references

- [Well Integrity During Production](../concepts/well-integrity-during-production.md) — router for production-time well-integrity coverage; SP0106 is the operating-time internal-corrosion management anchor
- [Corrosion Management](../concepts/corrosion-management.md) — production-system internal-corrosion mechanisms and inhibition / mitigation framework
- [Integrity Monitoring](../concepts/integrity-monitoring.md) — wall-thickness surveying, coupon programs, and the monitoring techniques that SP0106 programs deploy
- [Intervention Triggers](../concepts/intervention-triggers.md) — risk-based-inspection-driven workover decisioning that consumes SP0106-style monitoring data

## Cross-references

- **ISO 21457** — [ISO 21457](iso-21457.md) (system-level material-selection and corrosion-control philosophy; sister standard above SP0106 in the standards hierarchy)
- **Engineering-standards** — [AMPP SP0775](../../../engineering-standards/wiki/standards/ampp-sp0775.md), [AMPP MR0175 Part 1](../../../engineering-standards/wiki/standards/ampp-mr-0175-pt1.md), [AMPP MR0175 Part 2](../../../engineering-standards/wiki/standards/ampp-mr-0175-pt2.md), [AMPP MR0175 Part 3](../../../engineering-standards/wiki/standards/ampp-mr-0175-pt3.md), [API RP 581](../../../engineering-standards/wiki/standards/api-rp-581.md), [API RP 571](../../../engineering-standards/wiki/standards/api-rp-571.md), [ISO 15156](../../../engineering-standards/wiki/standards/iso-15156.md)
- **Marine-engineering** — [Corrosion Control](../../../marine-engineering/wiki/concepts/corrosion-control.md) (external structural corrosion of submerged offshore structures; complementary scope to SP0106 internal-pipeline-and-piping corrosion)

## Public references

- **AMPP / NACE** — official AMPP standard catalogue entry for NACE SP0106-2018 (retrievable from ampp.org). The standard is paywalled; no verbatim text reproduced.
- **Heidersbach, R.** — *Metallurgy and Corrosion Control in Oil and Gas Production*, 2nd ed., Wiley 2018 (ISBN 978-1-119-25925-6). Practitioner-oriented coverage of pipeline-and-piping internal-corrosion management that complements SP0106 framework.
- **Papavinasam, S.** — *Corrosion Control in the Oil and Gas Industry*, Elsevier 2014 (ISBN 978-0-12-397022-0). Comprehensive industry-practitioner reference; covers SP0106 framework in operating context with field-case examples.
- **API RP 1160** — *Managing System Integrity for Hazardous Liquid Pipelines*, 3rd ed., 2019. Pipeline-integrity-management program-level guidance that integrates SP0106-style internal-corrosion management.
- **49 CFR 192 / 49 CFR 195** — US federal pipeline-safety regulations (gas pipelines / liquid pipelines respectively); incorporate NACE SP0106 by reference for internal-corrosion integrity-management methodology. Retrievable from ecfr.gov.

## Notes

- NACE SP0106 is paywalled. This wiki paraphrases the structural intent and references the standard for operators who already have a licensed copy. No verbatim text reproduced.
- The NACE-to-AMPP rebrand following the 2021 NACE-SSPC merger has not changed the technical content of SP0106 nor the standard's designation; operator specifications, procurement documents, and regulatory submissions continue to cite "NACE SP0106" as the canonical reference.
- The 2018 reaffirmation of the 2006 original indicates the methodology framework remains fit-for-purpose; substantive technical revisions would have required a re-issued version rather than reaffirmation. Operators citing SP0106 in long-tenor contracts typically pin to the 2018 edition for clarity.
- SP0106's pipeline-and-piping focus formally excludes downhole production-tubing internal-corrosion management, although the methodology framework is widely applied to downhole tubulars by analogy. Operators applying SP0106 to downhole service typically note the analogy explicitly in their integrity-management documentation.
