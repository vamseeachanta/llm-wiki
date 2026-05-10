---
title: "NFPA 59A — Standard for Production, Storage, Handling of LNG"
slug: nfpa-59a
tags:
  - nfpa
  - lng
  - fire-protection
  - storage
  - design
  - peak-shaving
  - fuel-station
  - ferc-incorporated
  - standards
  - metadata-only
added: 2026-05-09
last_updated: 2026-05-09
domain: lng-projects
code_id: nfpa-59a
publisher: NFPA (National Fire Protection Association)
revision: "2023 latest published"
revision_source: https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=59A
verified_on: 2026-05-09
public_url: https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=59A
jurisdiction: United States (incorporated by reference into 49 CFR Part 193)
sources:
  - https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=59A
extraction_policy: metadata-only
raw_copy_allowed: false
cross_links: []
---

# NFPA 59A — Standard for the Production, Storage, and Handling of Liquefied Natural Gas (LNG)

> **code_id:** `nfpa-59a` &nbsp;·&nbsp; **publisher:** NFPA &nbsp;·&nbsp; **revision:** 2023 (latest published)

## Scope

NFPA 59A is the substantive design, construction, operations, and safety
standard for facilities that produce, store, transfer, handle, vaporize, or
dispense liquefied natural gas (LNG) on land in the United States. The
standard's scope spans the full LNG-facility taxonomy: peak-shaving plants,
small-scale liquefaction, mid-scale and large-scale export terminals,
import / regasification terminals, marine and truck-loading installations,
and LNG vehicle fueling stations. It is the dominant US LNG design code
because it is **incorporated by reference into PHMSA 49 CFR Part 193**, the
federal pipeline-safety regulation governing onshore LNG facilities — that
incorporation makes 59A the de-facto US federal LNG-safety design code for
any installation falling within Part 193's jurisdiction. The standard
governs siting and impoundment, process-equipment design, stationary
storage containers (including single-, double-, and full-containment
tanks and membrane tanks), transfer systems, fire-protection and
gas-detection systems, operations, training, marine activities on the
terminal side, and ancillary heat-transfer fluids. This page is a
metadata-only resolver entry: it identifies the code, its publisher,
edition, and chapter outline so that downstream consumers (calc modules,
project specifications, regulatory crosswalks) can re-pin to a specific
revision; it does **not** reproduce clauses, formulas, or tables from the
NFPA-published text.

## Why this page exists

This page exists to back `Citation` instances under
`.claude/rules/calc-citation-contract.md` for any LNG calculation module
that derives a constant or methodology from NFPA 59A — most commonly
thermal-radiation exposure limits, spill-impoundment sizing, and
flammable-vapor-cloud exclusion-zone methodology. The frontmatter
`code_id` / `publisher` / `revision` triplet is what calc-time citation
resolution matches against; downstream consumers must pin to the specific
edition they cite (currently `2023`) rather than depending on this page
drifting to a future revision. The page is also the standards-side anchor
for the eight existing concept pages in `lng-projects/wiki/concepts/` —
those pages name NFPA 59A in their *Standards / References* sections, and
this page closes the bidirectional link.

## Edition history

| Edition | Year | Notable |
|---------|------|---------|
| 2009    | 2009 | Pre-shale-gas-era edition; minimal liquefaction-export guidance; reflected the era when most US LNG facilities were peak-shavers or import terminals |
| 2013    | 2013 | First export-terminal-focused revisions in response to the post-2010 US LNG-export project pipeline |
| 2016    | 2016 | Added a dedicated LNG vehicle fueling-station chapter, codifying small-scale LNG dispensing |
| 2019    | 2019 | Mid-scale LNG and inherently-safer-design (ISD) provisions strengthened; expanded treatment of dispersion modeling |
| 2023    | 2023 | Cybersecurity considerations added; dispersion-modeling and consequence-analysis refinements; current published edition as of 2026-05-09 |

## Key chapters

- **Ch. 1–3 — Administration / Definitions / Reference Documents.** Standard scope, applicability, definitions, and the list of normatively-referenced publications.
- **Ch. 4 — General Requirements.** Cross-cutting requirements that apply across the rest of the standard.
- **Ch. 5 — Site Selection.** Plant siting, plot-plan requirements, separation distances between facility components and to property lines, and impoundment-system design philosophy.
- **Ch. 6 — Process Equipment.** Towers, heat exchangers, pumps, compressors, and other process equipment used in liquefaction or regasification trains.
- **Ch. 7 — Stationary LNG Storage Containers.** Design rules and containment categories for single-containment, double-containment, full-containment, and membrane tanks.
- **Ch. 8 — Stationary LNG Transfer Systems.** Loading arms, transfer lines, hose connections, and the associated mechanical and instrumentation requirements.
- **Ch. 9 — Fire Protection, Safety, Security.** Water-spray and water-curtain systems, dry-chemical and high-expansion-foam systems, gas and flame detection, and dispersion-detection systems.
- **Ch. 10 — Operations and Maintenance.** Operating procedures, inspection programmes, and recordkeeping for in-service facilities.
- **Ch. 11 — Plant Personnel and Training.** Personnel qualification and training-programme requirements.
- **Ch. 12 — Marine Shipping Activities.** Terminal-side requirements for marine LNG transfer; complements the IMO IGC Code on the ship side (see `igc-code` standards page when landed).
- **Ch. 13 — LNG Vehicle Fueling Stations.** Small-scale LNG dispensing for trucks, buses, and rail.
- **Ch. 14 — Ancillary Heat-Transfer Fluids.** Requirements for heat-transfer fluids used in LNG service.

## Tank types

| Tank type | Description | Containment behaviour |
|-----------|-------------|------------------------|
| Single-containment | Inner tank only; outer steel jacket provides thermal insulation but not liquid containment | Inner-tank leak is contained by an external impoundment dike, not by the tank's outer wall |
| Double-containment | Inner self-supporting tank plus an outer tank (concrete or steel); insulation occupies the annulus | Outer tank is designed to hold LNG if the inner tank leaks, but is not vapor-tight |
| Full-containment | Inner and outer walls both rated for LNG and vapor; outer is typically post-tensioned concrete | Most modern and safest configuration; widely used at recent export terminals |
| Membrane | Cryogenic membrane (e.g., Invar / GTT-derived) bonded inside a concrete outer; load path is membrane-on-insulation-on-concrete | LNG-carrier-derived containment family adopted at several recent onshore terminals |

See [lng-storage-tanks](../concepts/lng-storage-tanks.md) for the broader containment taxonomy and how
these categories apply across onshore and floating service.

## Notable design constraints

- **Thermal-radiation exposure limit** at facility boundary: 5 kW/m² (≈ 1600 BTU/hr/ft²) for the design fire scenarios.
- **Flammable-vapor-cloud distance** to the lower-flammability limit (LFL) for postulated spill scenarios — the deterministic exclusion-zone basis.
- **Spill-impoundment volume** sized to ≥ 110 % of the largest tank's contents (or per dispersion calculations where larger).
- **Cryogenic spill-control design** features: passivated concrete impoundment surfaces, slope-to-impoundment site grading, and dike heights set to keep flammable-vapor and thermal-radiation isopleths inside the property line.

These constraints are listed for orientation only; the binding numeric
basis for any specific project is the cited edition of NFPA 59A read
together with the project's PHMSA 49 CFR 193 authorization. Calc modules
must `Citation`-resolve to this page at a pinned revision.

## Cross-references

**Sibling lng-projects standards** _(populate as more standards/ pages land)_

- `phmsa-49-cfr-193` — federal pipeline-safety regulation that incorporates NFPA 59A by reference (file when landed)
- `ferc-18-cfr-153` — companion siting-authorization regulation for LNG export and import terminals (precedent reference, see W99)
- `igc-code` — IMO International Gas Carrier Code; ship-side counterpart to NFPA 59A Chapter 12 marine-shipping requirements (file when landed)

**lng-projects concepts** _(8 pages exist; this page is named in each)_

- [lng-project-lifecycle](../concepts/lng-project-lifecycle.md) — phases at which 59A applicability is locked in
- [lng-project-shapes](../concepts/lng-project-shapes.md) — peak-shaver vs export vs import vs fuel-station shapes that 59A covers
- [lng-regulatory-framework](../concepts/lng-regulatory-framework.md) — bodies-and-codes synthesis; this page is the NFPA arm
- [lng-process-safety](../concepts/lng-process-safety.md) — release / consequence categories driven by 59A Chapter 5 / 9 methodology
- [lng-liquefaction-processes](../concepts/lng-liquefaction-processes.md) — process-equipment side that 59A Chapter 6 governs
- [lng-storage-tanks](../concepts/lng-storage-tanks.md) — tank-type taxonomy aligned with 59A Chapter 7
- [lng-marine-transfer-systems](../concepts/lng-marine-transfer-systems.md) — terminal-side marine transfer; 59A Chapter 12 scope
- [lng-boil-off-gas-management](../concepts/lng-boil-off-gas-management.md) — BOG handling, downstream of 59A Chapter 7 storage-design choices

**International / regulatory parallels and companions**

- **CSA Z276** — Canadian LNG production-storage-handling parallel to 59A (referenced in workspace-hub#2227); sibling lng-projects standards page when landed
- **API Std 625** — Tank Systems for Refrigerated Liquefied Gas Storage; companion design code for the tank-system scope of 59A Chapter 7
- **API Std 620** — Design and Construction of Large, Welded, Low-Pressure Storage Tanks; companion for low-pressure storage configurations
- **EN 1473** — Installation and Equipment for LNG; the European Union onshore parallel to 59A
- **IEC 61882** — HAZOP studies application guide; the methodology backbone for hazard-identification programmes that 59A Chapters 9–10 expect
- **PHMSA 49 CFR Part 193** — federal regulation that incorporates 59A by reference; binding authority for US onshore LNG facilities

## Sources

- `sources/lng-regulatory-portals.md` — link to the (future) lng-projects sources catalog page summarizing the NFPA, PHMSA, FERC, IMO, CSA, and CEN public catalogs
- [Calc citation contract](../../../../.claude/rules/calc-citation-contract.md) — the schema this page resolves for downstream `Citation` instances
- Publisher catalog: <https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=59A>
