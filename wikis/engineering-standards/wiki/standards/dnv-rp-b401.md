---
title: "DNV-RP-B401 Cathodic Protection Design — bounded summary"
tags: ["dnv", "standards", "cathodic-protection", "corrosion", "metadata-only"]
added: 2026-05-02
last_updated: 2026-05-09
domain: engineering-standards
code_id: dnv-rp-b401
publisher: DNV
revision: "2011"
revision_source: "/mnt/ace/O&G-Standards/DNV/DNV_RP_B401_(2011)_Cathodic_Protection_Design.pdf"
verified_on: 2026-05-02
public_url: https://standards.dnv.com/explorer/
publisher_catalog_url: https://www.dnv.com/energy/standards-guidelines/
sources:
  - /mnt/ace/O&G-Standards/DNV/DNV_RP_B401_(2011)_Cathodic_Protection_Design.pdf
extraction_policy: metadata-only
raw_copy_allowed: false
---

# DNV-RP-B401 Cathodic Protection Design

## Scope

DNV recommended practice providing design requirements for cathodic protection (CP) of submerged offshore and marine structures, pipelines, and components. Coverage includes:

- Galvanic (sacrificial-anode) and impressed-current cathodic protection (ICCP) systems for permanent installations;
- Anode mass and current-output sizing keyed to design life and exposure;
- Design current densities by climatic zone, depth, and exposure (initial, mean, final);
- Coating breakdown factors for paint and field-joint coatings on pipelines and structures;
- Mean and final-period current-demand calculations supporting anode mass reservoir sizing;
- Anode resistance formulas for slender stand-off, flush-mounted, and bracelet anode geometries;
- Material and quality-assurance requirements for aluminum-alloy and zinc-alloy anode procurement.

The recommended practice is the DNV companion to NACE SP0176 / SP0387 / SP0492 (cathodic-protection of offshore structures and pipelines) in the global CP-design reference set, with DNV-RP-B401 the dominant choice on DNV-class projects and joint-industry contracts.

## Revision history

- **DNV 1986 original** — first DNV CP-design guidance for offshore structures issued under the legacy DNV technical-note series.
- **DNV-RP-B401 1993 edition** — first numbered RP edition; established the current-density-by-zone framework and the coating-breakdown-factor methodology.
- **2005 edition with 2008 amendments** — earlier revision held on disk (`(2005)_with_2008_amendments`); pre-merger DNV revision incorporating accumulated North-Sea operating experience.
- **2010 / 2011 edition** — On-disk reference revision (`/mnt/ace/O&G-Standards/DNV/DNV_RP_B401_(2011)_Cathodic_Protection_Design.pdf`); incorporated updated current-density tables and clarified design-life calculation methodology.
- **2017 edition** — DNV-GL-era revision under the consolidated DNV-RP-B401 numbering.
- **2021 latest** — current published revision under DNV-RP-B401 post-rebrand; users should verify the current portal revision against the on-disk 2011 reference when emitting calc citations against newer field developments.

## Key sections

- **Sec. 1 — General** — scope, references, definitions.
- **Sec. 2 — Operational and structural design parameters** — design life, environmental zones, coating systems.
- **Sec. 3 — Cathodic protection design parameters** — current densities (initial, mean, final), coating breakdown factors, anode utilization factors.
- **Sec. 4 — Galvanic anodes** — anode types, mass and resistance calculations, manufacturing and material requirements.
- **Sec. 5 — Cathodic protection design** — current-demand calculation, anode mass reservoir sizing, anode distribution, structure-to-electrolyte potential criteria.
- **Sec. 6 — Documentation** — CP-design report, anode procurement specification, installation and survey requirements.
- **Annexes** — anode resistance formulas, material requirements (Mn, Mg-equivalent, Cu/Zn limits), quality-assurance test plans, electrochemical performance qualification testing.

## Practitioner application

In practice, DNV-RP-B401 is the cited basis for:

- **Offshore platform jackets and topsides modules** — current-density and anode-sizing calcs for fixed-jacket cathodic protection on North Sea, Gulf of Mexico, and West Africa installations;
- **Subsea pipelines** — bracelet-anode sizing, coating-breakdown methodology, and design-life current-demand calculations for trunk-line and infield CP design;
- **LNG carriers and FPSO hulls** — supplemental hull CP design alongside class-society rules (ABS, BV, LR), particularly for permanent-mooring and FPSO converted-tanker hulls;
- **Subsea production equipment** — manifolds, PLEMs, jumpers, and tree CP-design and anode procurement;
- **Documentation deliverables** — CP Design Report, Anode Procurement Specification, and CP Survey / Inspection Plan that DNV class surveyors and operator engineering review accept at FEED and EPC handover.

## Industry adoption

- **DNV-classed offshore installations** — primary acceptance basis for galvanic-anode CP design.
- **DNV / ABS / BV / LR class procedures** — class societies typically accept DNV-RP-B401 design as compliant with their own offshore-CP requirements; some operators issue dual-acceptance specs.
- **North Sea operators** — DNV-RP-B401 is the regional default for jackets, subsea, and pipeline CP design.
- **Global EPC contractors** — routinely standardize on DNV-RP-B401 for joint-industry projects regardless of operator class society.
- **Brazilian, West African, and Asia-Pacific operators** — frequent secondary or co-cited use alongside NACE SP0176 / SP0387 / SP0492.

## Why this page exists

This page is a citation resolver for downstream calc modules under the calc-citation contract at `.claude/rules/calc-citation-contract.md`. RP-B401 is the dominant cathodic-protection design reference for DNV-domain calcs; 56 internal-reference hits in `digitalmodel` plus underscore-spelling variants. The standards page is the resolver-preferred target; the concept page at `concepts/cathodic-protection.md` covers the underlying electrochemistry. Contains no clause text, current-density tables, or formula reproductions from the source.

## Where to find the full text

- Raw PDF (2011 edition): `/mnt/ace/O&G-Standards/DNV/DNV_RP_B401_(2011)_Cathodic_Protection_Design.pdf` (read-only, vendor-derivative; do not copy into git)
- Earlier revisions on disk: `(1993)`, `(2005)_with_2008_amendments`
- Publisher catalog and free full-text portal: https://standards.dnv.com/explorer/
- Internal callers: `digitalmodel/src/digitalmodel/` (56 hits)

## Cross-references

- [[dnv-st-f101]] — pipeline systems reference RP-B401 for external corrosion control
- [[dnv-rp-f101]] — corroded-pipeline assessment complements CP-design
- [[dnv-rp-c203]] — fatigue assessment of offshore steel structures; CP design interacts with crack-tip cathodic environment
- [Calc citation contract](../../../../../.claude/rules/calc-citation-contract.md)

**Cross-wiki (engineering)**: [DNV-RP-F101: Corroded Pipelines](../../../engineering/wiki/standards/dnv-rp-f101.md) -- similar slugs (82%); shared tags: corrosion, dnv; shared entities: DNV, DNV-RP-B401
**Cross-wiki (engineering)**: [DNV-RP-C203: Fatigue Design](../../../engineering/wiki/standards/dnv-rp-c203.md) -- similar slugs (73%); shared tags: dnv; shared entities: DNV, DNV-RP-B401
**Cross-wiki (asset-management)**: [DNV-RP-G101 — Risk-Based Inspection of Offshore Topsides Static Mechanical Equipment](../../../asset-management/wiki/standards/dnv-rp-g101.md) -- similar slugs (82%); shared tags: dnv; shared entities: DNV
