---
title: "Chemical Disclosure (FracFocus)"
tags: [fracfocus, chemical-disclosure, hydraulic-fracturing-disclosure, gwpc, iogcc, frac-fluid-transparency, state-mandate, license-discipline, production-engineering, regulatory-handover]
sources: []
added: 2026-05-16
last_updated: 2026-05-16
---

# Chemical Disclosure (FracFocus)

## Scope

Chemical-disclosure regulation is the operator-facing reporting regime that captures the chemical constituents of hydraulic-fracturing fluids pumped on each fractured well. The dominant operator-facing platform for chemical disclosure in the United States is FracFocus.org, a registry operated jointly by the Ground Water Protection Council (GWPC) and the Interstate Oil and Gas Compact Commission (IOGCC). FracFocus is the platform mechanism; the underlying reporting obligation comes from state-by-state regulatory mandates that require operators to disclose hydraulic-fracturing chemistry, typically through FracFocus as the designated reporting mechanism.

This page covers the FracFocus registry, the state-by-state mandate framework that drives FracFocus reporting, the per-record vs bulk-download licence distinction (which is operationally important and demands explicit discipline), and the cross-link to the [Hydraulic Fracturing](hydraulic-fracturing.md) coverage that the disclosure regime regulates.

## FracFocus registry framing

FracFocus is operated as a joint project of GWPC and IOGCC. The registry serves several distinct functions:

- **Operator-side reporting platform** — operators submit per-job disclosure records (one record per fractured well, capturing the well identity, the fracture-stimulation date, the volumes of base fluid and proppant, and the chemical constituents of the fracturing fluid by additive class and concentration)
- **Regulator-side reporting platform** — for states that have designated FracFocus as the official reporting mechanism for their chemical-disclosure mandate, FracFocus serves as the regulator's record of operator compliance with the state mandate
- **Public-facing query interface** — the public can query the registry for chemical-disclosure records by well, by lease, or by geographic area; the per-record query interface is free and publicly accessible
- **Research-facing bulk-download interface** — academic and research users can request bulk-download access to the registry's data corpus; the bulk-download access operates under different licence terms than the per-record query

The registry has accumulated millions of disclosure records since its 2011 launch, covering the substantial majority of hydraulic-fracturing operations in the United States during the 2011-present period. The registry's coverage and quality have evolved over its operational history; early-period records have lower completeness than recent records, and the disclosure-format conventions have been revised across registry generations.

## State-by-state mandate framework

The state-by-state mandate for hydraulic-fracturing chemical disclosure emerged over the 2009-2015 period as state regulators responded to public-and-political pressure for transparency on hydraulic-fracturing chemistry. The mandate framework varies across states:

- **Texas (RRC), Colorado (COGCC/ECMC), Pennsylvania (DEP), North Dakota (NDIC), Oklahoma (OCC), Wyoming (WOGCC), Ohio (DNR), West Virginia (DEP)** — among the early-mover states, with mandates established in the 2010-2013 period. Most designate FracFocus as the official reporting mechanism.
- **California (CalGEM), New Mexico (OCD)** — among the later-mover states, with mandates established in the 2013-2015 period. Some operate state-specific disclosure platforms in parallel with FracFocus.
- **Alaska (AOGCC), other smaller-volume producing states** — varying mandate maturity; some designate FracFocus, some operate independent state-side disclosure platforms

The specific mandate-content (which chemicals must be disclosed, what concentration thresholds apply, what trade-secret protection is available for proprietary additives, what aggregation is acceptable for additive classes) differs across states. Operators with multi-state portfolios manage the cross-state differences as part of their chemical-disclosure infrastructure.

### Trade-secret carve-outs

A common feature across state mandates is a trade-secret carve-out that allows operators to withhold the specific chemical identity of additives that the operator's chemical-additive supplier has designated as trade secrets, subject to state-defined criteria. Trade-secret-withholding rates vary substantially across operators and across additive types; the trade-secret carve-out has been one of the more politically-contested features of the state mandate framework. Some states have tightened trade-secret-withholding criteria over time; others have maintained the original carve-out structure.

### Federal-side framing

Federal-side chemical-disclosure mandates have been narrower than state-side mandates. The EPA's 2015 final rule under the Toxic Substances Control Act addressed hydraulic-fracturing-fluid chemical disclosure narrowly; the Department of the Interior's proposed BLM-onshore chemical-disclosure rule was promulgated in 2015, rescinded in 2017, and has since cycled through additional regulatory iterations. Operators primarily satisfy chemical-disclosure obligations through the state-side framework rather than through a unified federal-side framework.

## License discipline (CRITICAL)

The licence terms governing FracFocus data access differ between the per-record query interface and the bulk-download interface, and the distinction is operationally important for this wiki:

### Per-record query interface

The FracFocus per-record query interface is publicly accessible and machine-readable for individual records. The registry's query API permits structured retrieval of individual disclosure records, and citation of specific records by URL or by registry-assigned identifier is the standard reference mechanism. This wiki may cite individual FracFocus records by URL where useful for grounding specific factual claims about disclosed chemistry.

### Bulk-download interface

The FracFocus bulk-download interface operates under separate, more-restrictive licence terms. Bulk-download access typically requires registration, may be restricted to research or regulatory users, and frequently carries licence restrictions on resale, redistribution, or aggregated republication. The specific bulk-download licence terms differ across registry generations and are subject to revision; operators or researchers requesting bulk-download access should consult the current licence terms at FracFocus.org directly.

### Wiki posture on FracFocus data

**This wiki does NOT ingest FracFocus bulk-download data.** The bulk-download licence restrictions are not amenable to the CC-BY-4.0 wiki content licence under which this wiki operates. Any reference to chemical-disclosure data on this wiki is by per-record URL citation only; aggregated chemical-disclosure analyses are not performed within this wiki and the wiki does not republish FracFocus bulk-download data in any form. Operators or researchers wishing to perform aggregated analyses of FracFocus data should access the bulk-download interface directly under its own licence terms and produce their analyses outside this wiki's content boundary.

This posture matches the broader wiki convention that vendor-or-licence-restricted data sources are referenced by URL only and not ingested. The FracFocus bulk-download case is a worked example of the licence-discipline pattern: a publicly-visible registry whose per-record interface is permissively-licensed but whose bulk-download interface is restrictively-licensed. The discipline applies even though the underlying chemical-disclosure data is publicly visible at per-record level.

## What gets disclosed

A typical FracFocus disclosure record includes:

- **Well identity** — API well number (a 14-digit federal identifier issued by API/IHS Markit; not to be confused with the API the standards-publisher), state-and-county location, operator name, lease and well name
- **Fracture-stimulation date** — the date the hydraulic-fracturing operation was performed
- **Base-fluid volume** — total water (or alternative base fluid) volume pumped, typically in thousands of gallons or barrels
- **Proppant volume and type** — total proppant mass pumped, broken down by proppant type (sand / resin-coated sand / ceramic; see [Proppants](proppants.md))
- **Additive list** — each chemical additive used in the fluid, broken down by:
  - **Trade name / supplier identity** — the commercial product name (subject to trade-secret carve-out)
  - **Function class** — friction reducer, gellant, crosslinker, breaker, biocide, scale inhibitor, surfactant, clay control, iron control, etc.
  - **Chemical constituent breakdown** — the specific chemicals comprising the additive (subject to trade-secret carve-out) and their CAS numbers
  - **Concentration** — the constituent concentration in the additive and the additive concentration in the total fluid pumped

The disclosure schema has evolved across registry generations; older records use a less-structured schema than recent records. The schema-evolution is documented at FracFocus.org and is operationally relevant for users performing time-series analyses across the registry's full operational history.

## Cross-link to hydraulic-fracturing wiki coverage

FracFocus disclosure regulates the chemistry of fluids pumped during hydraulic-fracturing operations covered at concept level on [Hydraulic Fracturing](hydraulic-fracturing.md), [Frac Fluids](frac-fluids.md), and [Frac Design](frac-design.md). The five frac-fluid families catalogued on the Frac Fluids page (slickwater / linear gel / crosslinked gel / energized CO2-N2 / foamed) correspond to different additive-class patterns in FracFocus records; operators selecting a fluid family on engineering grounds (per the Frac Fluids page) generate FracFocus records whose additive profile follows the fluid-family pattern.

Sand-control completion choices (see [Sand Control](sand-control.md), [Perforating](perforating.md)) interact with hydraulic-fracturing operations on completions that combine fracture stimulation with sand-control (frac-pack and related architectures; see [Frac Packing](frac-packing.md)). Disclosure records for these combined operations capture the combined-fluid chemistry.

## Schema-evolution history

The FracFocus disclosure schema has evolved across several generations:

- **FracFocus 1.0 (2011-2013)** — first-generation schema; less-structured records with substantial operator-side discretion in additive categorisation
- **FracFocus 2.0 (2013-2016)** — second-generation schema; more-structured records with tighter additive categorisation and improved CAS-number capture
- **FracFocus 3.0+ (2016 onward)** — third-generation schema and subsequent revisions; substantially more-structured records with detailed function-class categorisation, improved trade-secret-protection framing, and improved bulk-download formatting

Operators performing time-series analyses across the registry's full operational history must account for the schema-evolution, since the comparability of records across registry generations is bounded. Public-facing research on FracFocus data typically frames its conclusions around the schema generation of the underlying records. The schema-evolution documentation is available at FracFocus.org and is operationally relevant for users approaching the registry as a research corpus.

## Operational consumption pattern

Operators consume the chemical-disclosure regime in two operational modes:

- **Compliance-reporting mode** — submitting disclosure records to FracFocus on the cadence required by the relevant state mandate. The submission discipline is operationally similar to other regulatory-reporting workflows (see [State Production Reporting](state-production-reporting.md), [Federal Production Reporting](federal-production-reporting.md)) — vendor-software-mediated bulk-submission with format-and-deadline compliance.
- **Public-engagement mode** — operators may receive public-or-stakeholder inquiries about specific disclosure records and need to engage with the records that they themselves have submitted. The per-record query interface supports this engagement directly.

## International framing

The US-centric framing of this page reflects the historical centre-of-gravity of hydraulic-fracturing operations and the relatively-developed state of US chemical-disclosure regulation. Other jurisdictions have addressed hydraulic-fracturing chemical disclosure with varying maturity:

- **Canada** — disclosure framework operates at provincial level (BCOGC in British Columbia, AER in Alberta, ECCC at federal level). FracFocus.ca is the Canadian counterpart registry operated by GWPC's Canadian sister organisation; the Canadian framework follows a similar pattern to the US framework with provincial variations.
- **United Kingdom** — chemical-disclosure framing under the Environment Agency and HSE; UK shale-gas activity has been substantially constrained by the 2019 effective moratorium on commercial hydraulic-fracturing operations.
- **European Union** — chemical-disclosure framing emerging under the broader methane-and-environmental regulatory framework; the operational impact has been limited by the broadly-constrained level of EU shale-gas activity.
- **Australia** — chemical-disclosure framing at state-and-territory level; the operational impact varies across states with varying levels of unconventional-gas activity.

This wiki's coverage is primarily US-focused on the basis that the FracFocus framework is the most operationally-developed worldwide; operators in other jurisdictions face jurisdictionally-specific frameworks that should be consulted directly.

## Vendor-software framing

Production-accounting and stimulation-management software vendors that handle FracFocus reporting workflows include Halliburton-affiliated, Schlumberger-affiliated, and several specialty independents (operating on the same vendor-archetype framing applied across this wiki). The vendors are cited by name and general capability only; proprietary form-encoding internals, FracFocus-platform-integration details, and chemical-additive-cataloguing engine internals are not transcribed.

## Public-research framing on FracFocus data

Substantial public-research literature has used FracFocus data to characterise hydraulic-fracturing chemistry patterns, trade-secret-withholding rates, and time-series trends in chemical use. The research literature is typically published in environmental-science, public-health, and water-resources journals; representative analyses include national-level studies of additive-use patterns and basin-level studies of chemistry trends.

This wiki does not cite specific public-research analyses in detail (the analyses are derivative of FracFocus bulk-download data and the wiki's licence discipline limits the derivative-content surface that can be ingested). Researchers needing public-research framing should consult the published literature directly through standard academic-search infrastructure.

## Cross-references

- [Hydraulic Fracturing](hydraulic-fracturing.md) — the operations the disclosure regime regulates
- [Frac Fluids](frac-fluids.md) — fluid families whose chemistry the disclosure regime captures
- [Proppants](proppants.md) — proppants reported in FracFocus records alongside fluid chemistry
- [Frac Design](frac-design.md) — design choices that influence disclosure profile
- [Frac Packing](frac-packing.md), [Sand Control](sand-control.md) — combined frac-and-sand-control operations
- [Perforating](perforating.md) — perforation strategy interacts with fracture-stimulation operations
- [State Production Reporting](state-production-reporting.md) — state-side reporting infrastructure on which disclosure reporting frequently builds
- [Federal Production Reporting](federal-production-reporting.md) — federal-side reporting framework adjacent to disclosure
- [Production Allowable Rates](production-allowable-rates.md) — allowable-rate framing adjacent to disclosure framework
- [Gas Flaring Rules](gas-flaring-rules.md) — adjacent state-and-federal regulatory regime

## Public references

- **FracFocus.org** — the registry's public-facing portal; operator submission gateway, per-record public query interface, bulk-download access (under separate licence; see License discipline section).
- **Ground Water Protection Council (GWPC)** — gwpc.org, one of the two co-operating bodies; publishes context documentation on the FracFocus registry's framework and its role in groundwater-protection regulation.
- **Interstate Oil and Gas Compact Commission (IOGCC)** — iogcc.ok.gov, the other co-operating body; coordinates inter-state regulatory matters across oil-and-gas-producing states.
- **State regulator publications** — each state with a chemical-disclosure mandate publishes the mandate-text and the reporting-mechanism designation through its regulator portal (see [State Production Reporting](state-production-reporting.md) for the state-by-state regulator catalogue).
- **EPA Hydraulic Fracturing study** (2016 final report) — *Hydraulic Fracturing for Oil and Gas: Impacts from the Hydraulic Fracturing Water Cycle on Drinking Water Resources in the United States*. EPA-published synthesis covering the hydraulic-fracturing water cycle including chemical-disclosure framing; retrievable from epa.gov.
- **National Academies of Sciences, Engineering, and Medicine** — multiple published studies on shale-gas hydraulic-fracturing and the regulatory framework; useful framing references for the disclosure-regime context.

## Notes

- The chemical-disclosure regulatory framework is subject to ongoing revision at both state and federal levels. Operators preparing chemical-disclosure compliance documentation should consult the current state-side mandate text directly; this page summarises the framework at concept level only.
- FracFocus per-record records are publicly retrievable and per-record citation is the standard reference mechanism. **FracFocus bulk-download data is NOT ingested into this wiki under any circumstances.** Aggregated chemical-disclosure analyses produced from bulk-download access must be performed outside the wiki's content boundary and may be cited from this wiki only by URL to the publication that produced the analysis (subject to that publication's own licence).
- Trade-secret carve-outs in state mandates have produced controversy and ongoing regulatory iteration; this page does not adjudicate the policy debate but notes the framework feature.
- Federal-side chemical-disclosure regulation has been narrower and more politically-contested than state-side regulation; operators primarily satisfy disclosure obligations through the state-side framework.
- The API well number (14-digit federal identifier) referenced in FracFocus records should not be confused with the American Petroleum Institute (the standards publisher); the identifier was assigned by API and the assignment has been transferred to IHS Markit over time. The disambiguation is operationally important when reading FracFocus records.
