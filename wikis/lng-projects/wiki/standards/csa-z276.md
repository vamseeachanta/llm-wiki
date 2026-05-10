---
title: "CSA Z276 — LNG Production, Storage, and Handling"
slug: csa-z276
tags:
  - csa
  - lng
  - canada
  - design
  - fire-protection
  - regulatory
  - ngas
  - standards
  - metadata-only
added: 2026-05-09
last_updated: 2026-05-09
domain: lng-projects
code_id: csa-z276
publisher: CSA Group (Canadian Standards Association)
revision: "latest-in-catalog (typically 2018 or 2022 in field use; CSA Z276:23 is the publisher-current edition)"
revision_source: https://www.csagroup.org/store/product/CSA%20Z276:23/
verified_on: 2026-05-09
public_url: https://www.csagroup.org/store/product/CSA%20Z276:23/
methodology_status: catalog-absent-publisher-only
jurisdiction: Canada (adopted by reference into provincial regulations and into CSA Z662 Annex H for natural-gas pipeline LNG sub-systems)
sources:
  - https://www.csagroup.org/store/product/CSA%20Z276:23/
extraction_policy: metadata-only
raw_copy_allowed: false
cross_links: []
---

# CSA Z276 — Liquefied Natural Gas (LNG) Production, Storage, and Handling

> **code_id:** `csa-z276` &nbsp;·&nbsp; **publisher:** CSA Group &nbsp;·&nbsp; **revision:** latest-in-catalog (publisher-current `Z276:23`)

## Scope

CSA Z276 is the Canadian national standard for the design, construction,
operation, and maintenance of LNG facilities. It is the Canadian
counterpart to the US `nfpa-59a` standard and governs the same scope
families: production / liquefaction plants, peak-shaving plants, marine
import and export terminals, and LNG-as-fuel stations (truck, rail, and
marine fueling). In Canadian jurisdictions Z276 is the binding LNG-safety
design code: it is adopted by reference into provincial regulations and
is invoked by `CSA Z662` (the Oil & Gas Pipeline Systems standard) at
**Annex H**, which routes natural-gas-pipeline-asset LNG sub-systems
back to Z276 rather than re-deriving LNG-specific rules in Z662 itself.
Where a Canadian project also touches US infrastructure (cross-border
pipelines, US-flagged carriers, or jointly-permitted terminals), Z276
co-applies with the US-side codes — `phmsa-49-cfr-193` (which
incorporates NFPA 59A by reference) and `ferc-18-cfr-153` for FERC-jurisdictional
siting — but Z276 remains the controlling code on the Canadian side. This
page is a metadata-only resolver entry: it identifies the code, its
publisher, edition, and clause outline so downstream consumers (calc
modules, project specifications, regulatory crosswalks) can re-pin to a
specific revision; it does **not** reproduce clauses, formulas, or
tables from the CSA-published text.

## Why this page exists

This page exists to back `Citation` instances under
`.claude/rules/calc-citation-contract.md` for any LNG calculation module
that derives a constant or methodology from CSA Z276 — most commonly
thermal-radiation exposure limits, vapor-cloud / dispersion exclusion
zones, spill-impoundment volumes, and Canadian-specific siting
distances. The frontmatter `code_id` / `publisher` / `revision` triplet
is what calc-time citation resolution matches against; downstream
consumers must pin to the specific edition they cite (e.g. `2018` or
`2022` or publisher-current `Z276:23`) rather than depending on this
page drifting to a future revision. The page also closes the bidirectional
link from the eight existing concept pages in `lng-projects/wiki/concepts/`,
which name Z276 in their *Standards / References* sections, and it
finally retires workspace-hub#2227, the long-standing scope ticket
(W3-C) requesting a Z276 standards page in the lng-projects wiki.

## Edition history

| Edition / revision | Year | On disk? | Catalog doc-id | Notes |
|--------------------|------|----------|----------------|-------|
| 1st ed (Z276)      | 1976 | no       | n/a            | Original Canadian LNG production-storage-handling standard |
| Z276-2007          | 2007 | no       | n/a            | Major revision; aligned with the export-terminal era beginning to develop in BC |
| Z276-2011          | 2011 | no       | n/a            | Refresh ahead of the 2011-2014 BC LNG-export project pipeline |
| Z276-2015          | 2015 | no       | n/a            | Added LNG-as-fuel-station provisions (truck / marine fueling) |
| Z276-2018          | 2018 | no       | n/a            | Common in field use on Canadian LNG terminals reaching FID 2017-2020 |
| Z276-2022 / Z276:23| 2022-2023 | no  | n/a            | Strengthened cybersecurity provisions; dispersion-modeling alignment with NFPA 59A 2023 cycle; publisher-current as of 2026-05-09 |

> No CSA Z276 PDF is present in the locally-cached `/mnt/ace/O&G-Standards/_catalog.json`
> (the catalog is dominated by API / ASME / ASTM / DNV / ISO content);
> hence `methodology_status: catalog-absent-publisher-only`. Downstream
> consumers must pin to the specific edition cited in their calc and
> verify against the CSA Group publisher catalog.

## Key clauses

- **Clause 4 — Site selection.** Plant siting, plot-plan requirements, impoundment-system design, and minimum distances driven by thermal-radiation and flammable-vapor-cloud exclusion zones.
- **Clause 5 — Design.** Process equipment, stationary LNG storage tanks (single, double, full, membrane), and LNG transfer systems.
- **Clause 6 — Construction.** Construction-phase rules for the equipment families covered in Clause 5.
- **Clause 7 — Equipment and components.** Component-level requirements (valves, instrumentation, piping, pumps, vaporizers, refrigeration trains).
- **Clause 8 — Operations and maintenance.** Operating procedures, in-service inspection programmes, recordkeeping.
- **Clause 9 — Personnel qualifications.** Training and qualification requirements for LNG-facility operating personnel.
- **Clause 10 — Fire protection.** Water-spray and water-curtain systems, dry-chemical and high-expansion-foam systems, gas and flame detection, and dispersion-detection systems.
- **Clause 11 — Security.** Perimeter security, access control, and (post-2015 revisions) cybersecurity provisions for LNG-facility ICS / SCADA.
- **CSA Z662 Annex H** *(external reference)* — Z662's Annex H routes natural-gas-pipeline-asset LNG sub-systems back to Z276 rather than restating them inside the pipeline standard.

Section *titles only* — no clause text. Cite the publisher catalog for
full normative text.

## Z276 vs. NFPA 59A

| Aspect                    | CSA Z276 (Canada)                                                                                        | NFPA 59A (US)                                                                       |
|---------------------------|-----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| Authority                 | CSA Group plus provincial regulators; adopted by reference into provincial law                            | NFPA published; PHMSA 49 CFR 193 incorporates by reference for US-jurisdiction LNG  |
| Update cycle              | ~5–6 years between full revisions                                                                         | ~3 years                                                                             |
| Distance criteria         | Generally aligned with NFPA 59A; minor differences in dispersion-modeling assumptions and methodology     | 5 kW/m² thermal-radiation limit; LFL distance for flammable-vapor cloud             |
| Tank-type taxonomy        | Single / double / full / membrane (aligned with NFPA 59A categories)                                      | Single / double / full / membrane                                                    |
| Marine-side scope         | Cross-references CSA W47 / W48 welding standards on the terminal side                                     | NFPA 59A Chapter 12 — terminal-side marine shipping activities                       |
| Major project examples    | LNG Canada (Kitimat), Woodfibre LNG (Squamish), Pacific NorthWest LNG (cancelled), Bear Head LNG          | Sabine Pass, Plaquemines, Cove Point                                                 |

The two codes are functionally close cousins — siting, impoundment, tank
typology, fire protection, and operations-and-training scope all overlap
substantially. Cross-border projects routinely run a 59A↔Z276 crosswalk
during FEED to identify the small set of clauses where the codes
diverge.

## Canadian project context

- **LNG Canada (Kitimat, BC)** — largest Canadian LNG export terminal currently under construction; Phase 1 commissioning targeted 2025; the headline reference project for current Z276 application.
- **Woodfibre LNG (Squamish, BC)** — small-scale floating-storage LNG export project at the former Woodfibre pulp-mill site; tracked in the workspace-hub corpus as ACMA project 31522 (see `sources/woodfibre-corpus-pointer.md`).
- **Pacific NorthWest LNG (Lelu Island, BC)** — proposed export terminal cancelled by the proponent in 2017 ahead of FID.
- **Bear Head LNG (Point Tupper, NS)** — proposed Atlantic-Canada export terminal; not yet at FID.
- **Saint John LNG (NB)** — operating import terminal historically (Canaport LNG); evaluated for conversion toward export service.
- All Canadian onshore LNG terminals are governed by **Z276** in their Canadian-jurisdiction permits. NFPA 59A is **informative-but-not-binding** in Canada — it is routinely cited in Canadian project documents as a cross-check, but the regulator-binding code is Z276.

## Cross-references

**Sibling lng-projects standards**

- [nfpa-59a](nfpa-59a.md) — US LNG production-storage-handling standard; the most-aligned parallel to Z276 (cross-border crosswalk).
- [igc-code](igc-code.md) — IMO International Gas Carrier Code; ship-side counterpart applicable to LNG-carrier visits at Canadian terminals.
- [ferc-18-cfr-153](ferc-18-cfr-153.md) — FERC siting authorization for US-side LNG terminals (companion when a project is jointly permitted across the Canada-US border).
- [phmsa-49-cfr-193](phmsa-49-cfr-193.md) — US federal pipeline-safety regulation that incorporates NFPA 59A by reference; the US-side regulatory parallel to provincial-Z276 adoption.
- [sigtto-mooring-equipment](sigtto-mooring-equipment.md) — SIGTTO mooring-equipment guidance applicable to LNG-carrier mooring at Canadian terminals.

**External standards that Z276 invokes or that operate alongside it**

- **CSA Z662** — Oil and Gas Pipeline Systems; **Annex H** of Z662 references Z276 for natural-gas-pipeline-asset LNG sub-systems.
- **CSA W47 / CSA W48** — Canadian welding qualification and consumables standards invoked by Z276 on the construction and welding side.
- **API Std 625** — Tank Systems for Refrigerated Liquefied Gas Storage; companion design code referenced by both Z276 and NFPA 59A for refrigerated LNG storage tank systems.

**lng-projects concepts**

- [lng-project-lifecycle](../concepts/lng-project-lifecycle.md) — phases at which Z276 applicability is locked in for a Canadian project.
- [lng-project-shapes](../concepts/lng-project-shapes.md) — peak-shaver / export / import / fuel-station shapes that Z276 covers.
- [lng-regulatory-framework](../concepts/lng-regulatory-framework.md) — bodies-and-codes synthesis; this page is the Canadian-jurisdiction arm.
- [lng-process-safety](../concepts/lng-process-safety.md) — release / consequence categories driven by Z276 Clauses 4 and 10.
- [lng-liquefaction-processes](../concepts/lng-liquefaction-processes.md) — process-equipment side governed by Z276 Clause 5.
- [lng-storage-tanks](../concepts/lng-storage-tanks.md) — tank-type taxonomy aligned with Z276 (single / double / full / membrane).
- [lng-marine-transfer-systems](../concepts/lng-marine-transfer-systems.md) — terminal-side marine transfer at Canadian export terminals.
- [lng-boil-off-gas-management](../concepts/lng-boil-off-gas-management.md) — BOG handling, downstream of Z276 Clause 5 storage-design choices.

**International / regulatory parallels**

- **EN 1473** — European Union onshore LNG installation-and-equipment standard; the EU-side parallel.
- **IEC 61882** — HAZOP application guide; methodology backbone for hazard-identification programmes Z276 Clauses 8 / 10 expect.

## Sources

- [woodfibre-corpus-pointer](../sources/woodfibre-corpus-pointer.md) — Woodfibre LNG ACMA-31522 corpus pointer; Z276 is the binding design code for the Woodfibre project deliverables tracked there.
- [igu-2025-lng-report](../sources/igu-2025-lng-report.md) — IGU 2025 World LNG Report; capacity context for the Canadian LNG project landscape governed by Z276.
- [ferc-lng-portal](../sources/ferc-lng-portal.md) — FERC LNG portal; complementary US-side regulatory portal for jointly-permitted cross-border projects.
- [Calc citation contract](../../../../.claude/rules/calc-citation-contract.md) — the schema this page resolves for downstream `Citation` instances.
- Publisher catalog: <https://www.csagroup.org/store/product/CSA%20Z276:23/>
