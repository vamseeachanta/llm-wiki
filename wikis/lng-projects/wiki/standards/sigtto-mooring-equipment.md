---
title: "SIGTTO Mooring Equipment Guidelines for Gas Carriers"
slug: sigtto-mooring-equipment
code_id: sigtto-mooring-equipment
publisher: "SIGTTO (Society of International Gas Tanker and Terminal Operators)"
revision: "varies by current publication — link to SIGTTO publications list for live edition and most recent reissue"
jurisdiction: "international (industry best-practice; not a regulatory instrument)"
tags: [sigtto, lng-mooring, gas-carrier, terminal-operations, breakaway-prevention, transfer-safety, lng-projects, standards]
added: 2026-05-09
last_updated: 2026-05-09
sources:
  - https://www.sigtto.org/publications/
domain: lng-projects
extraction_policy: metadata-only
raw_copy_allowed: false
instrument_type: recommended-practice
publisher_catalog_url: https://www.sigtto.org/publications/
cross_links: []
---

# SIGTTO Mooring Equipment Guidelines for Gas Carriers

> **Industry-best-practice framing.** SIGTTO publishes consensus guidance for the liquefied-gas carrier and terminal industry; SIGTTO publications are not regulatory instruments and do not have force of law on their own. They are widely adopted by terminal operators, charterers, classification societies, and flag/port-state administrations as the baseline for safe gas-carrier mooring + transfer operations, and are commonly invoked by reference in port regulations, terminal rule-books, and ship-vetting regimes (CDI Marine, OCIMF SIRE 2.0). Most SIGTTO titles are paywalled through the Witherbys distributor — this page is metadata-only and a reference-pointer per the spinout's vendor-derivative governance; no clauses, tables, or formulas are reproduced.

## Scope

Industry-best-practice guidelines for the design, selection, inspection, and operation of mooring equipment specifically for liquefied-gas carriers (LNG, LPG, LEG, ammonia) at terminal jetties, FSRU/FRU berths, and ship-to-ship transfer locations. Coverage typically includes:

- Mooring-line selection — steel-wire-rope (SWR), conventional synthetic (polyester, polyamide/nylon), and high-modulus polyethylene (HMPE/Dyneema) tail-and-line combinations
- Bollard and winch design — minimum breaking load (MBL), brake-rendering setpoints, render-recovery cycle, redundancy
- Fender and breasting-dolphin design — energy-absorption envelope, reaction force, contact pressure on hull
- Weather-window planning — wind-and-current criteria for arrival/departure, transfer continuation, and emergency disconnect
- Emergency-disconnection coordination with the linked ship/shore Emergency Shutdown (ESD) chain
- Inspection regime, line-retirement criteria, and mooring-equipment-management plans (MEMP)
- Side-by-side ship-to-ship transfer mooring arrangements (post-2014 IGC amendments enabling LNG-as-fuel bunkering)

This page is a reference-pointer to the SIGTTO publication catalog and the surrounding standards landscape; it does not restate clauses or design tables.

## Why dedicated gas-carrier mooring guidance

- **Loss-of-containment consequence.** Gas carriers face vapor-cloud-explosion and jet-fire hazards that crude tankers do not — driving tighter mooring-force margins, ESD-coordination requirements, and weather-window criteria than crude-oil terminals require.
- **Hull-form windage.** LNG carrier hull form, with high freeboard and a relatively shallow draft when partly loaded, presents large windage area and a different mooring-force balance vs. typical tanker geometry; SIGTTO methodology accounts for the gas-carrier-specific force envelope.
- **Exposed-water terminal locations.** LNG export and import terminals are frequently sited in open or marginally sheltered water (e.g., Australian NW Shelf, Gulf of Mexico ship-channel berths, US-Pacific NW deep-water sites). Generic crude-oil-terminal mooring guidance, developed largely for sheltered estuarine berths, does not bound the long-period swell, sea-state, and squall conditions encountered at LNG sites.
- **Side-by-side LNG bunkering and STS.** The 2014 IGC-Code amendments and subsequent LNG-as-fuel uptake created a new operational scenario — side-by-side bunker-vessel + LNG carrier transfers — for which legacy crude-tanker guidance offers little coverage.

## Key publications and how they fit

- **SIGTTO — Mooring Equipment Guidelines for Gas Carriers** (specific to gas-carrier service; the most directly relevant title for jetty + ship mooring design for LNG/LPG carriers).
- **OCIMF MEG4** — *Mooring Equipment Guidelines, 4th edition*. Broader marine industry baseline; cross-referenced by SIGTTO and widely adopted across tanker terminals. MEG4 has gas-carrier sections and is often invoked alongside the SIGTTO title as the companion engineering reference.
- **SIGTTO — Site Selection and Design for LNG Ports and Jetties.** Front-end terminal-siting guidance covering metocean assessment, jetty layout, and approach/departure analysis; sets the design envelope into which the mooring-equipment guidance lands.
- **SIGTTO — Recommendations and Guidelines for Linked Ship/Shore Emergency Shut-Down of Liquefied Gas Cargo Transfer.** Ship/shore ESD-link signalling, response-time budget, and coordination protocol — directly bound to mooring-system performance via the ESD-1 / ESD-2 trigger thresholds and emergency-release-coupling envelope.
- **OCIMF — Tanker-Terminal Interface Guidelines** (broader; gas-carrier subset). Covers the management interface between vessel and terminal, including pre-arrival, mooring acceptance, transfer, and departure coordination.
- **CDI Marine — LPG/Chemical inspection regime.** The vetting regime under which gas-carrier mooring-equipment compliance is verified in commercial operation; the inspection-question set draws on SIGTTO + OCIMF guidance.

> Publication titles, editions, and successor-document numbering can change. Consult the live SIGTTO publications list at <https://www.sigtto.org/publications/> for current titles and revisions before citing in calculations or vetting deliverables. Some SIGTTO titles have been reissued or rebranded under joint OCIMF authorship in recent years.

## Notable industry incidents motivating SIGTTO guidance

The following incidents (drawn from public regulator filings, classification-society advisories, and industry-conference proceedings) shape the operational evidence base for the current SIGTTO mooring-equipment guidance:

- **NW Shelf LNG (Withnell Bay, Karratha, Australia), 2005–2014.** Multiple LNG-carrier mooring-line failures over a multi-year window. Investigation identified long-period swell at sub-50 mm amplitude resonating the moored-vessel-mooring system, producing line tensions far in excess of those predicted by conventional wind/current static analysis. Discussed in industry forums (notably the SIGTTO 2015 panel chaired by D. Allery) and a primary driver for tighter long-period-swell screening in subsequent SIGTTO + OCIMF revisions.
- **Prelude FLNG, 2018 (NOPSEMA Incident Report 5415).** During side-by-side LNG-carrier offload alongside the Prelude FLNG (Australia), nylon mooring lines on the LNG carrier *Gallina* failed; investigation cited heat build-up plus abrasion at the FLNG-side fairlead under sustained side-by-side conditions, with 16 lines damaged in a single event. Reinforced gas-carrier-specific concerns about polyamide/nylon line behaviour in side-by-side service and supports the present SIGTTO emphasis on synthetic-line management plans.
- **Port Hedland (BHP iron-ore export terminals).** Although not a gas-carrier site, Port Hedland's adoption of real-time mooring-line tension monitoring (Baird study) reportedly reduced mooring-failure frequency by approximately 35%. The data informs the SIGTTO + OCIMF MEG4 push toward continuous tension-monitoring as a recommended (and increasingly expected) safeguard for high-consequence berths, including LNG.

These incidents are tracked in more detail in the workspace-hub `mooring-failures-knowledge` corpus (private; not reproduced here). Public synthesis of the incident chain motivates the current SIGTTO + OCIMF MEG4 evolution toward (i) long-period-swell screening, (ii) synthetic-line management plans, and (iii) real-time tension monitoring for high-consequence gas-carrier berths.

## Cross-references

**Within lng-projects (this wiki):**

- [LNG Marine Transfer Systems](../concepts/lng-marine-transfer-systems.md) — the surrounding marine-transfer concept page; SIGTTO is the publisher cited for the mooring side of the transfer interface alongside OCIMF MEG4
- [LNG Process Safety](../concepts/lng-process-safety.md) — the ESD chain and vapor-release consequence model that the linked ship/shore ESD coordination guidance is built around
- [LNG Regulatory Framework](../concepts/lng-regulatory-framework.md) — SIGTTO is the industry-best-practice layer above the IMO + flag-state + port-state regulatory layer
- [LNG Boil-Off Gas Management](../concepts/lng-boil-off-gas-management.md) — BOG handling during transfer is bounded by the same ESD envelope SIGTTO addresses
- [LNG Project Shapes](../concepts/lng-project-shapes.md) — onshore terminal vs FSRU vs FLNG projects each present a distinct mooring-equipment scope
- [LNG Project Lifecycle](../concepts/lng-project-lifecycle.md) — SIGTTO inputs feed front-end engineering (FEED) for the marine facilities
- [LNG Storage Tanks](../concepts/lng-storage-tanks.md) — terminal-side cargo-containment counterpart to the ship-side mooring + transfer envelope
- [LNG Liquefaction Processes](../concepts/lng-liquefaction-processes.md) — process-train rate sets the cargo-loading throughput against which the mooring weather-window must hold

**Companion / sibling standards pages:**

- [FERC 18 CFR Part 153](./ferc-18-cfr-153.md) — US-federal LNG facility-siting authority; FERC's safety review at the marine interface routinely cites SIGTTO + OCIMF MEG4 as the recognised industry baseline
- `standards/igc-code.md` — IMO IGC Code (ship-side regulations: Ch. 4 cargo containment, Ch. 16 cargo as fuel; the regulatory layer SIGTTO sits above) — *forthcoming gap*
- `standards/nfpa-59a.md` — terminal-side construction code; Ch. 12 covers marine activities and is frequently cited together with SIGTTO at LNG-terminal jetty design reviews — *forthcoming gap*
- `standards/ocimf-meg4.md` — companion + parallel mooring-equipment guidance; MEG4 is the broader marine baseline that SIGTTO's gas-carrier-specific content extends — *forthcoming gap*

**Adjacent industry references (not standards pages, but bound to gas-carrier mooring practice):**

- **OCIMF SIRE 2.0** — vessel-vetting regime; mooring-equipment compliance is a routine inspection focus
- **CDI Marine** — LPG/Chemical-carrier inspection regime; counterpart to SIRE for gas-carrier vetting
- **Witherbys publishing** — SIGTTO publication distributor (<https://www.witherbys.com/>); paywalled; the canonical purchase route for SIGTTO titles
- **Classification-society guidance** — ABS, DNV, LR, BV, KR, ClassNK each publish gas-carrier mooring guidance notes that align with and extend the SIGTTO baseline

## Sources

- **SIGTTO publications list** — <https://www.sigtto.org/publications/> (authoritative live catalog of current titles, revisions, and reissues; metadata-only access without purchase)
- **Witherbys distributor** — <https://www.witherbys.com/> (paywalled retail channel for SIGTTO titles)
- **OCIMF publications** — <https://www.ocimf.org/> (companion guidance: MEG4, Tanker-Terminal Interface)
- **NOPSEMA incident reports** — <https://www.nopsema.gov.au/> (Australian offshore-petroleum regulator; primary public source for the Prelude FLNG incident referenced above)

> **Source-page gap.** A consolidated `sources/lng-regulatory-portals.md` page covering SIGTTO, OCIMF, IMO, USCG, NOPSEMA, FERC, and Witherbys does not yet exist in this wiki. The forthcoming source page should centralize publication-catalog links to avoid drift across future standards pages (IGC Code, NFPA 59A, OCIMF MEG4) and minimize stale-link risk as SIGTTO's publication list rebrands or reissues. Per the spinout's vendor-derivative governance, no SIGTTO or OCIMF document text, clauses, tables, or figures may be ingested into this public wiki under any circumstances; only metadata, public synthesis, and public incident records are permitted on this page.
