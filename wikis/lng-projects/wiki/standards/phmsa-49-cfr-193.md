---
title: "PHMSA 49 CFR Part 193 — LNG Facility Safety Standards"
slug: phmsa-49-cfr-193
tags: ["phmsa", "lng-safety", "design", "construction", "operations", "security", "us-regulation", "standards", "metadata-only"]
added: 2026-05-09
last_updated: 2026-05-09
domain: lng-projects
# --- standards-page extra fields (engineering-standards-imported convention) ---
code_id: phmsa-49-cfr-193
publisher: "PHMSA (US Pipeline and Hazardous Materials Safety Administration)"
revision: "latest CFR codification — link to eCFR"
revision_source: https://www.ecfr.gov/current/title-49/subtitle-B/chapter-I/subchapter-D/part-193
verified_on: 2026-05-09
public_url: https://www.ecfr.gov/current/title-49/subtitle-B/chapter-I/subchapter-D/part-193
methodology_status: catalog-absent-publisher-only
jurisdiction: "United States — federal (PHMSA, US DOT)"
sources:
  - https://www.ecfr.gov/current/title-49/subtitle-B/chapter-I/subchapter-D/part-193
extraction_policy: metadata-only
raw_copy_allowed: false
cross_links: []
---

# PHMSA 49 CFR Part 193 — LNG Facility Safety Standards

## Scope

49 CFR Part 193 is the US federal safety regulation for **liquefied natural gas (LNG) facilities**, administered by the **Pipeline and Hazardous Materials Safety Administration (PHMSA)** within the US Department of Transportation. It establishes minimum federal standards for **siting, design, construction, equipment, operations, maintenance, personnel qualification, fire-protection, security, and emergency procedures** at LNG facilities subject to federal jurisdiction — covering the full size spectrum from large import/export terminals through utility peak-shaving plants down to small-scale liquefaction and LNG fueling stations.

Part 193 is the operational-safety counterpart to **FERC 18 CFR Part 153** (the LNG-import/export authorization regime). The two together form the **US LNG-facility regulatory dyad**: FERC handles **siting authorization and project approval** for import/export facilities under §3 of the Natural Gas Act, while PHMSA handles **operational safety standards** for the facility once it is built and during its working life. A facility may be subject to both regimes (an import/export terminal sited under FERC and operated under PHMSA), to PHMSA only (a utility peak-shaver, intrastate plant, or LNG fueling station outside FERC §3 jurisdiction), or — for some upstream/maritime arrangements — to a different federal regime entirely (USCG 33 CFR 127 governs the marine-transfer waterfront; DOT 49 CFR 192 governs gas pipelines outside the LNG plant fence).

Page is **metadata-only**: do not transcribe regulatory text, tables, or numeric thresholds from the CFR into this repo. Always link operators and reviewers to the live eCFR text — federal regulations are amended frequently and the eCFR is the only authoritative current source.

## Why this page exists

Resolver page for the US LNG operational-safety regulatory anchor. Concept pages in lng-projects (notably `lng-regulatory-framework`, `lng-process-safety`) reference Part 193 by name; calc modules and reviewers that need to cite a US federal LNG safety basis route here for `code_id` / `publisher` / `revision` (per the workspace-hub `calc-citation-contract.md` schema). For cited numeric constants, the page also documents that **NFPA 59A is incorporated by reference** under § 193.2007 — meaning a Part 193 citation often resolves transitively to a specific frozen edition of NFPA 59A.

## Subparts

The current Part 193 structure on eCFR organizes substantive requirements across the following subparts. Section titles only — link to eCFR for clause text:

- **Subpart A — General Provisions.** Applicability, definitions, and scope thresholds. Notably, Part 193 does **not** apply to LNG facilities below a defined small-inventory threshold (historically expressed as a **70,000 lb LNG inventory** cutoff for small stationary LNG facilities, with separate carve-outs for LNG used as a vehicle fuel).
- **Subpart B — Siting.** Fire-protection-criteria distances (thermal-radiation and flammable-vapor-cloud exclusion zones), soil-stability, and seismic-design considerations governing where an LNG facility may be located relative to property lines and off-site populations.
- **Subpart C — Design.** Engineering basis requirements. **Incorporates NFPA 59A by reference** (see next section) for the bulk of the design requirements; layers federal-specific provisions on top.
- **Subpart D — Construction.** Construction quality, inspection, weld qualification, and pressure-test requirements during build-out.
- **Subpart E — Equipment.** Containment systems, transfer systems (loading arms, hoses, manifolds), instrumentation and controls, and active fire-protection equipment.
- **Subpart F — Operations.** Operating procedures, written manuals, abnormal-operation handling, and operating-limit enforcement.
- **Subpart G — Maintenance.** Inspection schedules, repair authorizations, and equipment-history recordkeeping.
- **Subpart H — Personnel Qualification and Training.** Operator qualification, training programs, and recurrent-training intervals for personnel performing covered tasks.
- **Subpart I — Fire-Protection.** Fire-water systems, dry-chemical systems, foam systems, detection (gas, flame, smoke), and alarm systems.
- **Subpart J — Security.** Perimeter security, surveillance, access control, and coordination with the **Department of Homeland Security** and federal partners.

## NFPA 59A incorporation

Part 193 incorporates **NFPA 59A — Standard for the Production, Storage, and Handling of Liquefied Natural Gas** by reference at multiple subparts. PHMSA codifies a **specific edition** of NFPA 59A under § 193.2007 (the "Incorporated by Reference" section). When NFPA publishes a new 59A edition, PHMSA must run a notice-and-comment rulemaking before the new edition becomes federally enforceable; the typical lag from NFPA publication to PHMSA adoption is **2–5 years**. Practical consequence for engineering teams:

- For US federal compliance, the binding NFPA 59A edition is whichever PHMSA has codified at § 193.2007 — **not necessarily** the latest NFPA edition on the NFPA catalog page.
- For state-jurisdictional or international project work, the NFPA-current edition may apply through a different adoption path.
- Any `Citation` instance under `calc-citation-contract.md` that resolves through Part 193 to NFPA 59A should record both the Part 193 revision and the NFPA 59A edition codified at § 193.2007 as of that date — this is what makes the citation reproducible if PHMSA updates its IBR later.

See `[nfpa-59a](nfpa-59a.md)` (future page) for the NFPA-side metadata.

## Fire-protection-criteria distances

Part 193 establishes two exclusion-zone concepts that drive site layout and adjacent-land-use compatibility studies. **Numeric thresholds and the precise scenario set are defined in the regulation; consult eCFR for the binding values.** At the conceptual level:

- **Thermal-radiation exclusion zone** — the distance from a postulated fire (e.g., a confined-spill pool fire) at which the incident heat flux falls to a defined safety threshold, historically **5 kW/m² (≈ 1,600 BTU/hr/ft²)** in the IBR-adopted criteria.
- **Flammable-vapor-cloud exclusion zone** — the distance from a postulated LNG spill at which the dispersing vapor concentration falls to the **lower flammable limit (LFL)** under defined meteorological conditions.
- **Modeling tools** — PHMSA-approved consequence-modeling tools are used to compute these distances. Common industry tools include **PHAST**, **FLACS** (CFD-based for complex geometries), and **FERC-LNG** (the FERC-specific dispersion model maintained for the parallel siting regime). Tool selection, source-term assumptions, and atmospheric stability class drive the resulting zone, so PHMSA review focuses heavily on input justification.

## Major incidents driving Part 193 evolution

The federal LNG safety regime is heavily incident-driven. Key events that shaped Part 193 and the underlying NFPA 59A:

- **Cleveland LNG fire — East Ohio Gas Co., 1944.** Tank failure released LNG into a residential neighborhood; fire and ground-soaked vapor ignition killed approximately **130 people**. Catalyzed the early development of **NFPA 59A** and entrenched the principle that LNG storage demands containment redundancy and exclusion-distance discipline.
- **Skikda, Algeria — 2004.** Liquefaction-train explosion at the Sonatrach Skikda terminal killed **27** and injured many more. Drove industry attention to **Inherently Safer Design (ISD)** principles — minimizing inventory, segregating ignition sources from refrigerant-leak paths, and improving boiler/process-area separation. Influenced subsequent revisions of NFPA 59A and PHMSA inspection focus.
- **Plymouth, WA — Williams NW Pipeline, 2014.** A 12-inch pipeline-segment failure at the Plymouth peak-shaving facility caused a release and LNG fire. Reinforced PHMSA emphasis on weld integrity, in-service inspection, and the interaction between Part 193 plant-side requirements and Part 192 pipeline-side requirements at the fence-line.

These incidents are anchors, not an exhaustive list — see `[lng-process-safety](../concepts/lng-process-safety.md)` for the broader incident learning corpus.

## Cross-references

**Sibling lng-projects standards** _(populate as more standards/ pages land)_
- [ferc-18-cfr-153](ferc-18-cfr-153.md) — FERC LNG import/export siting + authorization (companion US regime; PHMSA = ops safety, FERC = siting)
- [nfpa-59a](nfpa-59a.md) — NFPA Standard for Production, Storage, and Handling of LNG (incorporated by reference into Part 193 § 193.2007)
- [igc-code](igc-code.md) — IMO international parallel for LNG-carrier construction (shipping side; complements PHMSA shore-side)

**lng-projects concepts** _(8 pages exist as of 2026-05-09; bidirectional return-links to be added in those pages' Cross-references sections)_
- [lng-regulatory-framework](../concepts/lng-regulatory-framework.md) — US/international regulatory landscape
- [lng-process-safety](../concepts/lng-process-safety.md) — process-safety doctrine and incident learning
- [lng-project-lifecycle](../concepts/lng-project-lifecycle.md) — siting → permitting → ops phases
- [lng-project-shapes](../concepts/lng-project-shapes.md) — terminals vs. peak-shavers vs. small-scale
- [lng-storage-tanks](../concepts/lng-storage-tanks.md) — containment and tank-design requirements feeding Part 193 Subpart E
- [lng-marine-transfer-systems](../concepts/lng-marine-transfer-systems.md) — interface with USCG 33 CFR 127 at the dock
- [lng-liquefaction-processes](../concepts/lng-liquefaction-processes.md) — process units governed under Subparts C/E/F
- [lng-boil-off-gas-management](../concepts/lng-boil-off-gas-management.md) — BOG handling subject to operating-procedure requirements

**Adjacent US federal regimes** _(out of Part 193 scope but routinely interacting at the same facility)_
- **DHS C-FATS** — Chemical Facility Anti-Terrorism Standards; security overlay where LNG facilities meet the chemicals-of-interest threshold.
- **USCG 33 CFR 127** — Waterfront facilities handling LNG and LHG; governs the **marine-transfer area** where Part 193 jurisdiction stops.
- **DOT 49 CFR 192** — Gas pipelines (different scope; ends at the LNG-plant fence-line where Part 193 picks up).
- **FERC 18 CFR 153** — LNG import/export siting and authorization (the upstream-of-construction regime; see sibling standards page).

**International parallels**
- IMO **IGC Code** — international gas-carrier construction and equipment.
- **SIGTTO** publications — operational best-practice complement to formal codes.
- **EU Seveso III Directive** — closest EU analogue for major-accident-hazard siting, with different regulatory mechanics.

## Sources

- Live regulation text: <https://www.ecfr.gov/current/title-49/subtitle-B/chapter-I/subchapter-D/part-193> — eCFR is the authoritative current source; PHMSA does not maintain a separate canonical PDF.
- Future: `[[lng-regulatory-portals]]`(../sources/lng-regulatory-portals.md) — sources/* catalog summary aggregating eCFR, FERC, USCG, and PHMSA portals (stub — to be created when sources/ catalog reaches the US federal LNG cluster).
- [Calc citation contract](../../../../../.claude/rules/calc-citation-contract.md) — schema for `Citation` instances resolving to this page.
- Publisher catalog: PHMSA portal at <https://www.phmsa.dot.gov/> (LNG program pages); NFPA 59A catalog entry at <https://www.nfpa.org/> for the IBR'd edition.
