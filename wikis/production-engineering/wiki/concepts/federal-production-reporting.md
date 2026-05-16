---
title: "Federal Production Reporting"
tags: [federal-regulation, bsee, onrr, ocsla, 30-cfr-250, royalty-reporting, ewell, rrol, production-engineering, regulatory-handover]
sources:
  - 30-cfr-250
added: 2026-05-16
last_updated: 2026-05-16
---

# Federal Production Reporting

## Scope

Federal production reporting is the operator-facing regulatory workflow that satisfies the federal-side requirements for production-volume reporting, royalty-payment calculation, and related compliance obligations on wells producing under federal jurisdiction. Federal jurisdiction covers the Outer Continental Shelf (OCS) (where federal authority is primary), federal onshore lands administered by the Bureau of Land Management (BLM), and federal mineral interests in mixed-ownership tracts.

This page covers the BSEE-side production-operations reporting framework under 30 CFR 250 Subpart E and the ONRR-side royalty-reporting interface that consumes the production-volume data. The two regulatory authorities (BSEE for production operations, ONRR for royalty accounting) operate under separate regulatory titles but are operationally coupled through shared production-volume data. The Outer Continental Shelf Lands Act (OCSLA) is the umbrella statute under which both frameworks operate.

## Federal-vs-state jurisdiction split

Federal-side reporting applies to:

- **US Outer Continental Shelf wells** — wells producing in federal offshore waters beyond the state-jurisdiction boundary (typically 3 nautical miles from the coast for most states, with Texas and west-coast Florida operating under different historical jurisdictional lines). OCS wells operate under federal-only reporting; state regulators have no jurisdiction.
- **Federal onshore wells (BLM-administered)** — wells producing on federally-administered onshore lands. BLM operates under 43 CFR with regulatory authority over the federal mineral interest; the state regulator retains some authority over the well operation itself (orphan-well prevention, conservation regulation, environmental compliance). Operators on federal onshore lands typically face dual reporting and dual compliance requirements.
- **Federal mineral interests on private surface** — where the federal government owns the mineral rights underlying a private-surface tract, federal-side mineral-management reporting applies to the federal interest. The operational pattern is complex and depends on the specific federal-interest arrangement.
- **Indian and tribal-trust lands** — wells producing on Indian or tribal-trust lands operate under a federal-administered framework that parallels the BLM framework with tribal-trust-specific variations. The Bureau of Indian Affairs (BIA) coordinates with BLM and ONRR on these wells; the operational pattern is sufficiently distinct from the BLM-only pattern that operators in Indian-country typically build dedicated infrastructure for it.

State-side reporting (see [State Production Reporting](state-production-reporting.md)) applies to wells outside federal jurisdiction — fee-lands onshore wells, state-lands onshore wells, and state-tideland offshore wells within the state-jurisdiction boundary.

## BSEE production-reporting framework

BSEE (Bureau of Safety and Environmental Enforcement) is the Department of the Interior agency responsible for safety and environmental regulation of OCS oil-and-gas operations. The production-reporting framework operates under 30 CFR 250 Subpart E (Oil and Gas Production Requirements). See [30 CFR 250](../standards/30-cfr-250.md) for the regulatory anchor.

### Reporting flows

BSEE production reporting covers:

- **Monthly production reports** — operators report monthly produced volumes of oil, gas, condensate, and water for each lease and for each well within a lease. The reporting cadence and form-content requirements are set by 30 CFR 250 Subpart E and operationalised through BSEE's electronic-reporting platforms (the eWell platform and related platforms; specific platform names and capabilities are subject to BSEE-side IT-infrastructure revisions).
- **Well-test reporting** — well-test data feeding the production-allocation framework is reportable to BSEE on the cadence specified in Subpart E. See sister sub-issue 1 page `well-test-and-reconciliation.md`.
- **Sustained-casing-pressure (SCP) reporting** — operators report SCP exceeding regulatory threshold values within specified time intervals and develop remediation plans on regulator-mandated cadences. SCP reporting is one of the most operationally-visible parts of Subpart E.
- **Drilling and completion reports** — well-construction events are reported through forms parallel to the state-side W-1/W-2 pattern.
- **Pollution and incident reporting** — events including spills, releases, equipment failures, and personnel injuries are reported on event-triggered cadences. The reporting framework is operationally distinct from the production-volume reporting workflow.

### Electronic-platform interface

BSEE operates electronic-reporting platforms for the production-reporting workflows. The platforms accept bulk-upload submissions in BSEE-published formats and support web-based interactive submission for smaller-volume operators. Specific platform names, file-format specifications, and submission cadences are subject to revision; operators should consult the current BSEE technical documentation for platform-side detail.

### NTL framing

BSEE Notices to Lessees and Operators (NTLs) periodically address reporting expectations — clarifying form-content requirements, establishing new reporting workflows, addressing electronic-platform updates. NTLs are publicly retrievable from bsee.gov. See [Intervention Triggers](intervention-triggers.md) for the integrity-management NTL coverage and [30 CFR 250](../standards/30-cfr-250.md) for the NTL umbrella framing.

## ONRR royalty-reporting framework

ONRR (Office of Natural Resources Revenue) is the Department of the Interior agency responsible for collecting, accounting for, and disbursing royalty revenues from federal and Indian mineral leases. The royalty-reporting framework operates under regulations at 30 CFR 1200-1299 and is operationally coupled to the BSEE production-reporting framework — produced-volume data reported to BSEE feeds the royalty calculation that operators report to ONRR.

### Reporting flows

ONRR royalty reporting covers:

- **Royalty calculation and payment** — operators calculate the royalty due on each unit of production based on the lease-specific royalty rate, the produced-volume base, and the lease-specific allowances (transportation allowances, processing allowances, marketing allowances). The royalty calculation is reported to ONRR on the monthly cadence specified by 30 CFR 1200-series rules.
- **Production-allocation reporting** — for commingled production, the allocation of produced volumes to individual leases (which determines the royalty-base allocation) is reported to ONRR through a workflow that parallels the BSEE-side allocation reporting. The two reporting flows must reconcile.
- **Sales-and-disposition reporting** — produced volumes are tracked through sales to purchasers, processing into refined products, lease-fuel use, and disposition events. The sales-and-disposition data feeds the royalty calculation.
- **Audit-and-reconciliation workflows** — ONRR conducts post-payment audits to verify that operator-reported royalty calculations are correct. The audit-and-reconciliation workflow can extend years after the original royalty payment and can produce material adjustments to historical reporting.

### RROL platform

ONRR operates the Reporting and Royalty Online (RROL) platform (formal name and platform-side detail subject to ONRR IT-infrastructure revisions) for royalty-reporting submissions. RROL accepts bulk-upload submissions in ONRR-published formats and supports web-based interactive submission. Operators with multi-lease portfolios typically build automation around the RROL bulk-upload pathway through vendor-supplied or in-house infrastructure.

### Royalty-rate and lease-specific framing

The royalty rate is set in each lease at the time of lease issuance and varies across leases. OCS leases typically carry royalty rates between 12.5% and 18.75% of produced value (specific rates are publicly visible on the BOEM lease catalogue). Onshore federal leases under BLM administration carry comparable rates with onshore-specific variations. The royalty-base calculation differs between oil and gas (oil royalty is typically calculated on gross-proceeds from sale; gas royalty calculation involves processing-and-transportation allowances that are more complex). The lease-specific rate and the royalty-base calculation method are determinative inputs to the royalty calculation that the operator reports.

### Interface with BSEE production data

The BSEE-side production volumes feed the ONRR-side royalty calculation. Discrepancies between the BSEE-side produced-volume data and the ONRR-side royalty-base data are flagged through cross-agency reconciliation workflows. Operators with material discrepancies face audit attention; the cross-agency reconciliation is one of the operational reasons that production-accounting infrastructure must reconcile both BSEE and ONRR reporting outputs against the same underlying production-allocation source.

## BLM onshore framework

For wells producing on BLM-administered onshore lands, BLM operates a regulatory framework under 43 CFR that parallels the BSEE OCS framework with onshore-specific variations. BLM production reporting feeds ONRR royalty calculation through the same coupled-reporting workflow that applies on the OCS.

BLM-onshore operators also face state-side reporting obligations under the state regulatory framework. The dual-reporting pattern (BLM + state regulator) is operationally distinct from the federal-OCS pattern (federal-only). Operators with BLM-onshore portfolios maintain reporting infrastructure that handles both flows.

## OCSLA umbrella framing

The Outer Continental Shelf Lands Act (43 USC Chapter 29) is the umbrella statute under which both the BSEE production-reporting framework and the ONRR royalty-reporting framework operate for OCS wells. OCSLA establishes:

- **Federal jurisdiction over OCS resources** — defining the federal regulatory authority over OCS oil-and-gas activity
- **Lease-issuance authority** — delegating lease-issuance authority to BOEM
- **Operational regulatory authority** — delegating operational regulatory authority to BSEE
- **Royalty-collection authority** — delegating royalty-collection authority to ONRR
- **Enforcement framework** — establishing the civil-and-criminal enforcement framework for OCSLA violations

OCSLA itself is a statute (Congressional law); the regulatory frameworks under 30 CFR 250 (BSEE) and 30 CFR 1200-1299 (ONRR) are delegated regulatory instruments that implement OCSLA's statutory framework.

## Operator and lease-administration interface

Underlying the BSEE and ONRR reporting flows is the operator-and-lease administrative infrastructure that both agencies maintain in coordination with BOEM (which issues OCS leases) and BLM (which issues onshore federal leases). Operators must register with both BSEE and ONRR (and with BOEM on the lease-issuance side), and the lease-and-operator identifiers must align across the agencies for the reporting flows to reconcile.

Operationally, the administrative interface produces several recurring workflows:

- **Operator registration and qualification** — operators must qualify under each agency's framework before operating on federal leases; qualification includes financial-assurance posting (bonding) and operator-fitness verification
- **Lease assignment and transfer** — sales of lease interests between operators trigger administrative-side update workflows that must be completed at BSEE, BOEM, and ONRR before the production-and-royalty reporting can transition to the new operator
- **Bonding and financial-assurance management** — federal lease operations require posted bonds at the lease, operator, or company-wide level; the bonding-and-financial-assurance management workflow is operationally distinct from the production-reporting workflow but is administratively coupled
- **Decommissioning-cost estimation and reservation** — operators on federal leases must estimate and reserve for decommissioning costs (well plug-and-abandonment, platform removal, site clearance) under BSEE's decommissioning framework; the reservation requirements interact with the bonding-and-financial-assurance management

The administrative interface is operationally substantive and operators with material federal-lease portfolios typically maintain dedicated administrative staff (often called Regulatory Affairs or Government Compliance) who navigate the multi-agency framework on behalf of the operational organisation.

## Coupling with state-side reporting

For wells with mixed federal-and-state mineral interests, or wells producing across federal-and-state jurisdictional boundaries (rare but operationally non-zero), operators face dual or split reporting obligations. The specific allocation depends on the lease structure and the inter-agency coordination; operators in mixed-jurisdiction situations typically engage legal-and-regulatory specialists to navigate the operational pattern.

For most operators, the federal-and-state jurisdictions are cleanly partitioned: federal-OCS wells operate under federal-only reporting; state-onshore wells (on fee or state lands) operate under state-only reporting; BLM-onshore wells face dual federal-and-state reporting.

## Coupling with allowable-rate compliance

Federal-side allowable-rate authority operates through 30 CFR 250 Subpart E for OCS wells and through 43 CFR for BLM-onshore wells. See [Production Allowable Rates](production-allowable-rates.md) for the conservation-regulation framing.

## Vendor-software framing

Production-accounting software vendors that handle federal-side reporting workflows include TIBCO, OGsys, Quorum, Enverus (formerly Drillinginfo), and several specialty independents. These vendors abstract the BSEE-and-ONRR reporting workflows behind unified operator-facing interfaces and typically include automation pathways for the BSEE eWell and ONRR RROL platforms. Vendors are cited by name and general capability only; proprietary form-encoding internals, platform-integration details, and royalty-calculation engine internals are not transcribed in this wiki.

## Cross-references

- [Production Allowable Rates](production-allowable-rates.md) — federal-side rate-control authority under 30 CFR 250
- [State Production Reporting](state-production-reporting.md) — state-side reporting frameworks
- [Gas Flaring Rules](gas-flaring-rules.md) — federal-side flaring authorization under 30 CFR 250 Subpart E
- [Chemical Disclosure FracFocus](chemical-disclosure-fracfocus.md) — adjacent state-and-federal disclosure framework
- [Well Integrity During Production](well-integrity-during-production.md) — integrity-reporting interface (SCP reporting under Subpart E)
- [Intervention Triggers](intervention-triggers.md) — regulator-mandated triggers including BSEE NTLs
- [30 CFR 250](../standards/30-cfr-250.md) — federal OCS regulatory framework
- [Electric Submersible Pumps (ESP)](electric-submersible-pumps.md), [Gas Lift Overview](gas-lift-overview.md) — Phase 1 artificial-lift coverage; lift-method choice affects reporting category
- [Perforating](perforating.md), [Sand Control](sand-control.md) — completion-design choices captured on completion reports
- [Hydraulic Fracturing](hydraulic-fracturing.md) — fracture-stimulation operations captured on completion-related reports
- Sister sub-issue 1: `production-allocation.md`, `well-test-and-reconciliation.md` — allocation and well-test discipline feeding both BSEE and ONRR reporting

## Public references

- **eCFR** — 30 CFR 250 (BSEE) and 30 CFR 1200-1299 (ONRR); retrievable from ecfr.gov.
- **BSEE** — bsee.gov publishes the agency's regulatory guidance, NTLs, INC data, and the electronic-reporting platform documentation.
- **ONRR** — onrr.gov publishes the royalty-reporting framework documentation, the RROL platform documentation, and the audit-and-reconciliation framework.
- **BOEM** — boem.gov publishes the lease catalogue and the lease-and-plan administrative framework.
- **BLM** — blm.gov publishes the federal-onshore administrative framework under 43 CFR.
- **OCSLA** — Outer Continental Shelf Lands Act, 43 USC Chapter 29; statutory text retrievable from the US Code.
- **Federal Register** — proposed rules and final rules promulgating amendments to 30 CFR 250 and 30 CFR 1200-1299 appear in the Federal Register; the rule-making preamble provides regulatory rationale that the rule text alone often does not.
- **Lyons, W. C. (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, Elsevier (ISBN 978-0-7506-7785-1). Production-operations chapters cover federal-side reporting at framework level.

## Notes

- Form-content requirements, electronic-platform specifications, and reporting cadences are subject to revision. Operators preparing compliance documentation should consult the current rule-text and current platform-specification documentation from BSEE and ONRR directly; this page summarises the framework at concept level only.
- The 30 CFR 1200-1299 royalty-reporting regulations cited here are the regulatory framework under which the ONRR royalty-reporting workflow operates; the specific cite-points within the 30 CFR 1200-1299 range are subject to revision and operators should consult the current eCFR text.
- Federal regulatory text is publicly retrievable from eCFR; the verbatim text is public domain (US federal regulation). Per the wiki's discipline, verbatim text greater than 30 words is not transcribed even for public-domain federal-regulatory text — operators should consult the eCFR canonical source directly.
- The BSEE and ONRR platform names cited here (eWell, RROL) are subject to ongoing IT-infrastructure evolution at both agencies; specific platform names and capabilities should be verified against current agency documentation.
- Cybersecurity-side reporting (TSA Pipeline Security Guidelines, pipeline-side cybersecurity-incident-reporting) is explicitly **OUT OF SCOPE** for this wiki phase per the Phase 5 scope-edge.
