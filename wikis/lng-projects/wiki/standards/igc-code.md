---
title: "IMO IGC Code — International Code for Construction and Equipment of Ships Carrying Liquefied Gases in Bulk"
slug: igc-code
code_id: imo-igc-code
publisher: "IMO (International Maritime Organization)"
revision: "MSC.370(93) 2014 amendments — current applicable to ships built since 2016"
jurisdiction: "International (SOLAS contracting flag states)"
tags: [imo, igc, lng-carrier, marine-safety, solas-vii, ship-design, cryogenic-cargo, lng-projects, standards, metadata-only]
added: 2026-05-09
last_updated: 2026-05-09
sources:
  - https://www.imo.org/en/OurWork/Safety/Pages/IGC-Code.aspx
domain: lng-projects
extraction_policy: metadata-only
raw_copy_allowed: false
---

# IMO IGC Code — International Code for Construction and Equipment of Ships Carrying Liquefied Gases in Bulk

> **Regulatory framing.** The IGC Code is a mandatory IMO instrument adopted under SOLAS Chapter VII Part C and binding on all SOLAS-contracting flag states. It is the marine-side counterpart to land-side LNG facility codes such as NFPA 59A (US) and CSA Z276 (Canada). This page is metadata-only; no clause text, formula, table, or figure is reproduced.

## Scope

Mandatory IMO code under SOLAS Chapter VII Part C governing the design, construction, equipment, surveys, and certification of ships carrying liquefied gases in bulk. The IGC Code applies to LNG carriers, LPG carriers, ammonia carriers, and ethylene/ethane carriers.

Coverage:

- Ship survival capability + cargo-tank location (collision/grounding survivability)
- Cargo containment systems (independent tanks, membrane tanks, integral tanks)
- Cargo-handling and process systems (piping, pumps, vapor return, reliquefaction)
- Materials of construction for cryogenic and low-temperature service
- Cargo pressure/temperature control and boil-off-gas (BOG) management
- Pressure-relief and venting systems
- Atmosphere control (inerting, drying)
- Electrical, fire-protection, ventilation, instrumentation, and personnel-protection systems
- Use of cargo as fuel (direct relevance to dual-fuel and steam-turbine LNG carriers)

The IGC Code applies to ships whose keel is laid on or after **1 July 1986**; the **MSC.370(93) major revision** is mandatory for ships built on or after **1 July 2016**. Older gas carriers built before 1986 fall under the GC Code (predecessor) or the EGC Code (existing-gas-carrier provisions).

## Why this page exists

Resolver page for any lng-projects calc module or wiki cross-reference that targets IGC Code as a citation. The marine cargo-containment, BOG management, and materials-of-construction sections feed directly into LNG-carrier sizing, terminal compatibility studies, and bunkering-vessel design. Frontmatter `code_id: imo-igc-code` + `publisher: IMO` + `revision: MSC.370(93) 2014 amendments` are the defensible-citation triple per `.claude/rules/calc-citation-contract.md`.

## Edition history

| Edition / revision | Year | IMO instrument | Notes |
|--------------------|------|----------------|-------|
| Original IGC Code | 1983 | Resolution MSC.5(48) | First mandatory IMO code; effective 1 July 1986 for new ships |
| Amendments | 1990s–2000s | Multiple MSC resolutions | Incremental updates aligning with double-hull tanker era, AIS, radar, and updated firefighting standards |
| **MSC.370(93) major revision** | 2014 (effective 1 July 2016) | Resolution MSC.370(93) | Stricter cargo-tank survey requirements, updated PRV sizing methodology, expanded provisions for LNG bunker vessels and use of cargo as fuel |
| Subsequent amendments | post-2016 | Various MSC resolutions | Periodic technical corrections; consult IMO catalog for current revision |

The GC Code (Code for Existing Ships Carrying Liquefied Gases in Bulk, Resolution A.329(IX), 1975) and the EGC Code (Resolution A.328(IX)) cover ships predating IGC applicability and are not interchangeable with the IGC Code.

## Key chapters

- **Ch.1 — General**: scope, definitions, surveys, certification (Certificate of Fitness)
- **Ch.2 — Ship Survival Capability + Location of Cargo Tanks**: collision/grounding survivability, side-impact protection, freeboard, damage-stability assumptions
- **Ch.3 — Ship Arrangements**: cargo-area boundaries, gas-dangerous-zone classification, ventilation, escape arrangements
- **Ch.4 — Cargo Containment**: tank-type taxonomy (Type A, Type B, Type C, membrane, integral); secondary-barrier requirements; partial vs full secondary barrier
- **Ch.5 — Process Pressure Vessels + Liquid/Vapor Piping**: cargo-handling system, manifold, segregation
- **Ch.6 — Materials of Construction**: cryogenic and low-temperature material requirements (e.g., 9% Ni steel — ASTM A553 — for inner tanks; Invar / 36% Ni alloy for membrane systems; aluminum alloys for some independent tanks)
- **Ch.7 — Cargo Pressure/Temperature Control**: boil-off management, reliquefaction plants, gas combustion units (GCU), cargo conditioning
- **Ch.8 — Cargo Tank Vent Systems**: pressure-relief-valve (PRV) sizing for fire scenario and cargo-property envelope; vent mast geometry
- **Ch.9 — Cargo Containment System Atmosphere Control**: nitrogen inerting, dry-air purging for selected cargoes, interbarrier-space monitoring
- **Ch.10 — Electrical Installations**: hazardous-area classification, certified electrical equipment, intrinsic safety
- **Ch.11 — Fire Protection + Fire Extinction**: water-spray systems, dry-chemical, foam, fire pumps, structural fire protection
- **Ch.12 — Mechanical Ventilation in the Cargo Area**: air-change rates, intake/exhaust geometry, fan certification
- **Ch.13 — Instrumentation + Automation Systems**: level/temperature/pressure monitoring, gas detection, ESD systems
- **Ch.14 — Personnel Protection**: PPE, decontamination showers, breathing apparatus, medical supplies for cargo-specific exposures
- **Ch.16 — Use of Cargo as Fuel**: BOG-to-engine routing — directly relevant to dual-fuel diesel-electric (DFDE), tri-fuel (TFDE), ME-GI / X-DF two-stroke, and legacy steam-turbine LNG carriers
- **Ch.17 — Special Requirements**: cargo-specific provisions — including LNG bunker-vessel-specific provisions added under the 2014 amendments

(Ch.15 is reserved/skipped in the codified numbering — this is intentional in the IGC Code structure, not a gap on this page.)

## Tank-type taxonomy

| Type | Description | Most-common service |
|------|-------------|---------------------|
| **Type A** | Independent prismatic tank with full secondary barrier | Older LPG carriers; legacy fully-refrigerated trades |
| **Type B (Moss)** | Spherical independent tank with partial secondary barrier (drip tray) | Moss-design LNG carriers (Kvaerner Moss Rosenberg lineage) |
| **Type B (SPB)** | Self-supporting prismatic with partial secondary barrier | IHI-designed LNG carriers; hybrid prismatic geometry |
| **Type C** | Pressure-rated independent tank (no secondary barrier required) | Semi-refrigerated and pressurized LPG carriers; small-scale LNG and LNG bunker vessels |
| **Membrane (GTT NO 96)** | Invar (36% Ni) primary + secondary membrane in IMO-classified hold | Modern LNG carriers (legacy MARK-I lineage) |
| **Membrane (GTT Mark III)** | Stainless-steel corrugated primary + composite secondary in IMO-classified hold | Most LNG carriers built since 2000s |
| **Integral** | Tank forms part of ship's hull structure | Limited use; specialized service |

Membrane systems dominate the modern LNG-carrier fleet; Moss-type independent spheres are visually distinctive but represent a shrinking share of the orderbook. Type C dominates the LNG bunker-vessel and small-scale LNG segment.

## Cross-references

**Within lng-projects (this wiki):**

- [LNG Marine Transfer Systems](../concepts/lng-marine-transfer-systems.md) — ship-side interface to terminal jetty / FSRU / STS operations governed by IGC Code Ch.5 + Ch.13 cargo-handling and ESD provisions
- [LNG Storage Tanks](../concepts/lng-storage-tanks.md) — ship-side cargo containment under Ch.4 + Ch.6 is the marine counterpart to land-side full-containment tank design
- [LNG Boil-Off Gas Management](../concepts/lng-boil-off-gas-management.md) — Ch.7 (pressure/temperature control) and Ch.16 (use of cargo as fuel) are the IGC chapters that drive vessel-side BOG handling
- [LNG Liquefaction Processes](../concepts/lng-liquefaction-processes.md) — terminal-side liquefaction feeds carrier loading; IGC Code Ch.5 governs the ship-side receiving system
- [LNG Process Safety](../concepts/lng-process-safety.md) — ship-side hazard controls (Ch.8 venting, Ch.11 fire, Ch.13 instrumentation) parallel land-side process-safety frameworks
- [LNG Regulatory Framework](../concepts/lng-regulatory-framework.md) — IGC Code is the IMO/SOLAS pillar of the international LNG regulatory map
- [LNG Project Lifecycle](../concepts/lng-project-lifecycle.md) — vessel selection, charter, and class society review map onto the IGC Certificate of Fitness milestone
- [LNG Project Shapes](../concepts/lng-project-shapes.md) — FSRU, FLNG, conventional carrier, and LNG bunker vessel each have distinct IGC chapter applicability

**Sibling lng-projects standards (this wiki):**

- [FERC 18 CFR Part 153](./ferc-18-cfr-153.md) — US-side authorization for LNG import/export facilities; the USCG Letter of Recommendation (LOR) coordinates waterway-suitability for IGC-flagged carriers calling US terminals
- `standards/nfpa-59a.md` — terminal-side US LNG facility safety code (forthcoming — gap); IGC governs the ship side, NFPA 59A governs the terminal side
- `standards/phmsa-49-cfr-193.md` — US-flag PHMSA interface (forthcoming — gap); incorporates NFPA 59A by reference for terminal safety

**Cross-wiki bridge (maritime-law):**

- [SOLAS 1974](../../../maritime-law/wiki/standards/solas-1974.md) — **bidirectional bridge**: SOLAS Chapter VII Part C is the parent convention text under which the IGC Code is mandatory for gas carriers (LNG, LPG, ethylene, ammonia).
- [MARPOL 73/78](../../../maritime-law/wiki/standards/marpol-73-78.md) — **bidirectional bridge**: pollution-prevention companion. MARPOL Annex VI air-pollution provisions govern BOG-combustion emissions from IGC-certified carriers; Annex I governs slops/oily-water handling on IGC vessels with diesel-fuel systems.
- [HNS Convention 2010](../../../maritime-law/wiki/standards/hns-convention-2010.md) — **bidirectional bridge**: IGC defines gas-carrier construction; HNS Convention 2010 (not yet in force) defines compensation regime for cargo releases. HNS Fund LNG/LPG sub-accounts apply to IGC-certified vessels.

**International / regulatory parallels:**

- **SOLAS** — parent IMO convention; IGC Code is mandatory under SOLAS Chapter VII Part C
- **MARPOL** — pollution-prevention companion; relevant to cargo-tank cleaning, slops handling, and air emissions from BOG combustion
- **STCW Convention** — crew certification including LNG-specific and LNG-bunkering training endorsements (IGF Code crosswalk for fuel-side competencies)
- **IGF Code** — mandatory companion code (Resolution MSC.391(95)) governing ships using gases or other low-flashpoint fuels (LNG-fueled ships that are NOT gas carriers); IGC Ch.16 vs IGF Code carve up the cargo-as-fuel vs fuel-only territory
- **SIGTTO publications** — industry-best-practice complement covering operational guidance, ESD systems, and terminal/ship interface (not mandatory, but heavily referenced by class societies)
- **Class society rules** — ABS, DNV, LR, BV, ClassNK, KR, RINA, CCS each issue gas-carrier rules that implement IGC Code requirements with classification-specific scantling and survey detail

## Sources

- **IMO IGC Code portal** — https://www.imo.org/en/OurWork/Safety/Pages/IGC-Code.aspx (publisher catalog; mandatory-instrument status, current amendments, and links to consolidated edition)
- **IMO MSC resolution catalog** — Resolution MSC.5(48) (1983 original) and Resolution MSC.370(93) (2014 major revision) accessible via IMODOCS
- **SOLAS Chapter VII Part C** — parent convention text via IMO catalog; binds IGC Code to flag-state implementation
- **SIGTTO publications** — https://www.sigtto.org/publications (industry-best-practice companion; not mandatory but routinely incorporated into class-society rules and charterer vetting)

> **Source-page gap.** A consolidated `sources/lng-regulatory-portals.md` page covering IMO, FERC, DOE/FECM, PHMSA, USCG, and class-society catalogs does not yet exist in this wiki. The same gap was flagged from `standards/ferc-18-cfr-153.md`; this page extends the gap to the international layer. A future-promotion stub should be filed when raw-corpus indexing reaches the IMO and class-society publisher catalogs. The in-flight `sources/igu-2025-lng-report.md` (W104) will provide industry-state context that complements but does not substitute for the publisher catalog.

- [Calc citation contract](../../../../.claude/rules/calc-citation-contract.md)
