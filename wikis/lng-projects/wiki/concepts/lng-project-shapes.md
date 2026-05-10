---
title: "LNG Project Shapes"
tags: [lng-projects, concept, project-shapes, flng, fsru, mid-scale, small-scale, greenfield, brownfield]
added: 2026-05-03
last_updated: 2026-05-10
sources: [concept-synthesis]
domain: lng-projects
cross_links:
  - ../concepts/lng-project-lifecycle.md
  - ../concepts/lng-marine-transfer-systems.md
  - ../concepts/lng-regulatory-framework.md
  - ../concepts/lng-storage-tanks.md
  - ../concepts/lng-liquefaction-processes.md
  - ../../standards/ferc-18-cfr-153.md
  - ../../standards/phmsa-49-cfr-193.md
  - ../../standards/nfpa-59a.md
  - ../../standards/csa-z276.md
  - ../../standards/en-1473.md
  - ../../standards/igc-code.md
  - ../../standards/sigtto-mooring-equipment.md
---

# LNG Project Shapes

## Scope

This page defines the canonical project-shape taxonomy that distinguishes liquefaction, regasification, and storage-only configurations across onshore and offshore deployments. It does **not** name or commercially characterize any specific facility, recite owner / operator commercial terms, or rank archetypes by economic merit; those are project-bound determinations and belong on facility-specific source pages or in private commercial workspaces. It also stays at concept depth — capacity ranges, duration ranges, and capex / opex notes are indicative magnitudes drawn from public industry surveys, not project-specific budgets.

## Why project shape governs everything downstream

- **Regulatory pathway is shape-determined** — onshore-greenfield triggers full siting review (FERC 18 CFR 153 + NEPA in the US, full national competent-authority review in EU jurisdictions). Brownfield expansions can re-use prior siting determinations under amendment procedures. FLNG and FSRU shift authority toward IMO IGC Code + flag-state + class society. Each shape selects its own primary standards stack at the conceptualization phase.
- **Capex / opex profile differs by an order of magnitude** — onshore-greenfield carries the highest absolute capex (multi-billion USD per train) but the lowest unit opex per ton over a 20-30 year operating life. FLNG carries a lower absolute capex per MTPA but higher unit opex (offshore logistics, vessel-class manning). Mid-scale modular trades unit-cost-of-capacity for first-cargo speed.
- **Project duration scales with shape complexity** — pre-FEED through first-cargo on an onshore-greenfield typically runs 6-9 years; brownfield expansions can compress to 4-6 years; FLNG newbuild runs 4-6 years from FID; FSRU conversions of existing carriers can deliver in 18-24 months. Shape selection is therefore a market-timing decision as much as a technology decision.
- **Market positioning and offtake-contract structure** — long-haul base-load LNG (Asian utility, European pipeline-replacement) historically anchored on onshore-greenfield with 20-25 year SPAs. FLNG and FSRU enabled smaller, shorter contracts and stranded-gas monetization. Mid-scale and small-scale LNG opened bunkering, virtual-pipeline, and peak-shaving markets that base-load greenfield could not address.

## Onshore-greenfield archetype

- **New-build liquefaction plant on a previously undeveloped site** — full marine, utility, and logistics scope. Capacity typically 3.0-8.0 MTPA per train, multi-train developments reaching 10-30 MTPA total nameplate. US Gulf Coast and East African export developments are the canonical reference shapes.
- **Capex profile** — heaviest absolute capex (front-loaded EPC, marine works, tankage, utilities); strongest economy-of-scale per ton at multi-train sites.
- **Regulatory complexity** — full siting review, full Resource Reports under FERC, full national competent-authority review in EU. Long permitting tail; environmental review can drive critical path.
- **Trains** — once-through axial-flow propane-precooled mixed-refrigerant (C3MR), AP-X, mixed-fluid cascade (MFC), and ConocoPhillips Optimized Cascade are the canonical large-train liquefaction process families. See [LNG Liquefaction Processes](./lng-liquefaction-processes.md) for the process-family taxonomy.
- **Worked anchor — Sabine Pass** — Cheniere's US Gulf Coast facility transitioned from a planned regasification terminal to a multi-train greenfield liquefaction complex during the early-2010s shale-gas pivot; canonical reference for parallel-train ConocoPhillips Optimized Cascade modularization and for the FERC 18 CFR 153 siting pathway. See [LNG Liquefaction Processes](./lng-liquefaction-processes.md).
- **Worked anchor — East African and Pacific greenfield** — Mozambique LNG (onshore) and PNG LNG illustrate jurisdictions where greenfield siting carries the additional complexity of nation-building infrastructure (port, road, power, workforce-housing), pushing pre-FEED durations toward the upper bound of the 6-9 year range.

## Onshore-brownfield archetype

- **Capacity addition adjacent to an existing plant** — re-uses common marine berth, utilities, BOG handling, and (frequently) a portion of feed-gas conditioning. Train sizes typically match the parent project's train architecture for spare-parts and operating-procedure commonality.
- **Capex profile** — lower absolute capex per MTPA than greenfield; opex tracks the parent facility. Brownfield is often the first capacity-addition shape considered when an existing operator has spare site footprint.
- **Regulatory complexity** — siting amendment rather than de novo siting in many jurisdictions; reduced critical-path duration.
- **Constraint interaction** — exclusion zones from the parent facility, residual cryogenic-spill-containment capacity at the shared bund, and shared marine-loading slot availability all bind expansion sizing. See [LNG Process Safety](./lng-process-safety.md) for the exclusion-zone interaction.
- **Worked anchor — Cove Point** — Dominion Energy's Maryland facility added a liquefaction train to a long-running regas terminal; reference example of converting a receiving-terminal site to bidirectional service while re-using marine works and tankage.
- **Worked anchor — Kenai** — the Kenai LNG plant (Alaska, ConocoPhillips legacy) illustrates the long-running peak-shaver-and-export brownfield mode where the same site cycles through liquefaction, mothball, and re-start phases against multi-decade demand cycles.

## Floating archetypes — FLNG and FSRU

- **FLNG (Floating Liquefied Natural Gas)** — vessel-mounted liquefaction over a gas field or near-shore mooring. Canonical capacity range 1.0-4.0 MTPA per unit. Enables monetization of stranded offshore gas without subsea pipeline to onshore plant. Authority stack centers on IMO IGC Code, IACS class-society rules, and flag-state administration; onshore design codes apply only where an onshore tie-in or jetty exists.
- **FSRU (Floating Storage and Regasification Unit)** — vessel-mounted regasification of imported LNG. Faster to deploy than onshore regas (existing carrier conversion in 18-24 months; newbuild FSRU in 30-36 months). Used as bridging capacity, peak-demand response, and rapid-import response (post-2022 European response is the most-cited recent precedent).
- **Mooring and offtake interfaces** — turret moorings, tower-yoke moorings, and side-by-side / tandem offtake configurations interact with sea-state criteria; SIGTTO mooring practice and OCIMF MEG4 govern the marine-side. See [LNG Marine Transfer Systems](./lng-marine-transfer-systems.md).
- **Class-society type approval** — gas-carrier and floating-LNG class notations differ from carrier service notations; cargo containment system (membrane, Moss spherical, SPB prismatic, Type C pressure) selection drives the type-approval pathway.
- **Worked FLNG anchors** — Shell Prelude (Australia, ~3.6 MTPA, turret-moored, the largest-displacement floating asset ever launched at delivery), ENI Coral Sul (Mozambique, ~3.4 MTPA, deepwater stranded-gas monetization), and BP Greater Tortue Ahmeyim (Mauritania-Senegal cross-border, hub-and-spoke FLNG with breakwater) span the canonical FLNG operating envelope from harsh-environment cyclonic basin (Prelude) to deepwater frontier (Coral Sul) to cross-border hub (Tortue).
- **Worked FSRU anchors** — Excelerate Energy's Excellence-class units pioneered the conversion-FSRU pathway in the mid-2000s; Höegh Esperanza's 2022 Wilhelmshaven deployment is the canonical post-Russia-Ukraine European bridging case (chartered, repositioned, and commissioned in months rather than years).
- **Boundary cases** — onshore-tied FLNG with jetty offtake (Coral Sul side-by-side regimes), cylindrical-hull FLNG (smaller-displacement Petronas units), and converted-carrier FSRU with steam plant retained vs. dual-fuel re-engined units span the design-margin frontiers.

## Mid-scale modular and small-scale archetypes

- **Mid-scale modular** — pre-fabricated trains in the 0.5-2.0 MTPA per train range. Modular fabrication in dedicated yards reduces site work and shortens schedule from FID to first cargo (typically 24-36 months). Favored for tight market windows, brownfield additions, and emerging-market deployments where mega-train financing is unavailable.
- **Small-scale LNG (SS-LNG, < 0.5 MTPA)** — peak-shaving plants on natural-gas distribution networks (decades of US precedent), marine bunkering production, and virtual-pipeline distribution to off-grid demand. Capex per ton is the highest of any archetype; demand-side proximity offsets the unit-cost penalty.
- **Marine bunkering** — LNG-as-fuel supply for ships under the IGF Code framework. Distinct from cargo LNG; transfer interfaces, custody-transfer practice, and crew qualifications differ. SIGTTO and IGF Code provisions govern the safety envelope.
- **Standards interaction** — CSA Z276 explicitly covers peak-shaving, fuel-station, and import / export shapes as a single national standard; EN 1473 covers the same shapes within a unified European umbrella. NFPA 59A historically focused on onshore liquefaction and storage with separate provisions for receiving terminals.
- **Worked anchor — Trinidad ATB** — Atlantic LNG's Trinidad complex includes mid-scale brownfield train additions on the parallel-train ConocoPhillips Cascade architecture, illustrating the mid-scale-within-greenfield mode where parent-facility infrastructure underwrites incremental capacity at sub-greenfield-greenfield unit cost.
- **Worked anchor — bunkering and small-scale** — bunker-vessel newbuilds (Shell-chartered units serving Rotterdam, Algeciras, Singapore) and yard-built small-scale liquefaction (e.g., Stabilis Energy's Texas yards serving virtual-pipeline customers) span the demand-proximate small-scale envelope. The IGF-Code-governed safety envelope on the bunker-receiving ship side, and the IMO-MSC-CIRC.1321/1591 guidance on bunkering operations, complement onshore CSA-Z276 / EN-1473 / NFPA-59A coverage of the supply-side small-scale plant.

## Multi-criteria comparison across archetypes

| Criterion | Greenfield | Brownfield | FLNG | FSRU | Mid-scale | Small-scale |
|---|---|---|---|---|---|---|
| Per-unit capacity (MTPA) | 3.0-8.0 per train | matches parent | 1.0-4.0 | 3.0-6.0 send-out | 0.5-2.0 | <0.5 |
| Capex order-of-magnitude | highest absolute | lower per MTPA | lower per MTPA, higher per unit | lowest absolute | mid | highest unit cost |
| Opex unit-cost over operating life | lowest | tracks parent | higher (offshore manning) | mid | mid-high | highest |
| Pre-FEED to first cargo | 6-9 years | 4-6 years | 4-6 years | 18-36 months | 24-36 months | 18-30 months |
| Regulatory complexity | full siting + NEPA / EIA | siting amendment | IGC + flag + class | IGC + port + class | onshore code stack | onshore code + IGF for bunker |
| Market positioning | base-load long-term SPA | base-load expansion | stranded-gas / harsh-environment | bridging / crisis-response | flexible / emerging-market | demand-proximate / bunker / peak |
| Modularization friendliness | medium-high (parallel-train) | high (drop-in) | high (yard-built hull) | high (carrier conversion) | very high (yard-prefab) | very high |
| Carbon / methane gating | high (pipeline + plant footprint) | medium | high (offshore venting) | low (regas only) | medium | low-medium |

## Capacity-range and duration reference table (indicative)

| Archetype | Per-unit capacity (MTPA) | Pre-FEED to first cargo | Primary authority stack |
|---|---|---|---|
| Onshore-greenfield | 3.0-8.0 per train; 10-30 total | 6-9 years | National siting + NFPA 59A / EN 1473 / CSA Z276 |
| Onshore-brownfield | matches parent train | 4-6 years | Siting amendment + parent facility's stack |
| FLNG | 1.0-4.0 | 4-6 years | IGC Code + IACS + flag state |
| FSRU (carrier conversion) | 3.0-6.0 send-out | 18-24 months | IGC Code + IACS + port state |
| FSRU (newbuild) | 3.0-6.0 send-out | 30-36 months | IGC Code + IACS + flag/port state |
| Mid-scale modular | 0.5-2.0 per train | 24-36 months | NFPA 59A / CSA Z276 / EN 1473 |
| Small-scale (peak / bunker) | < 0.5 | 18-30 months | NFPA 59A / CSA Z276 / EN 1473 + IGF for bunker |

Values are indicative magnitudes from public industry surveys (Oxford Institute for Energy Studies NG149, US DOE Global LNG Fundamentals, GIIGNL Annual Reports); project-specific values vary by site, train architecture, and market.

## Standards / References

- [FERC 18 CFR 153](../standards/ferc-18-cfr-153.md) — US LNG siting authority differentiating onshore-greenfield from brownfield from offshore export shapes.
- [PHMSA 49 CFR 193](../standards/phmsa-49-cfr-193.md) — US LNG facility safety operations applicable to onshore and shore-based regasification shapes.
- [NFPA 59A](../standards/nfpa-59a.md) — US onshore design code that distinguishes liquefaction-plant from receiving-terminal scope.
- [CSA Z276](../standards/csa-z276.md) — Canadian LNG standard covering peak-shaver / export / import / fuel-station onshore shapes.
- [EN 1473](../standards/en-1473.md) — European onshore LNG umbrella covering import / export / peak-shaving / fuel-station shapes.
- [IGC Code](../standards/igc-code.md) — IMO international gas-carrier code governing FLNG, FSRU, and carrier-side project shapes.
- [SIGTTO Mooring Equipment Guidelines](../standards/sigtto-mooring-equipment.md) — terminal-mooring practice that varies by jetty, FSRU, and FLNG shape.
- Oxford Institute for Energy Studies, NG149 Floating LNG Update: <https://www.oxfordenergy.org/>
- US DOE Global LNG Fundamentals: <https://www.energy.gov/fecm/global-lng-fundamentals>
- GIIGNL Annual Report (capacity-by-shape statistics): <https://giignl.org/>

## Recent industry trends 2020-2025

- **2020-2022 FID hesitancy** — pandemic-era demand shock, EPC inflation in long-lead cryogenic equipment, and offtake-portfolio reformation slipped FID on multiple announced greenfield and brownfield projects by 12-24 months. Shape selection became more conservative, with brownfield and mid-scale proposals competing more equally against greenfield mega-trains.
- **Post-Russia-Ukraine demand pull (2022-2024)** — the European supply shock pulled FID forward on US Gulf Coast greenfield and brownfield with European offtake, accelerated FSRU charters / conversions / newbuilds for European bridging capacity, and re-priced long-term offtake contracts upward. Several previously-stalled greenfield projects re-entered the FID queue with revised offtake portfolios.
- **Modularization shift across mid-scale and brownfield** — fabrication-yard pre-assembly of trains reduces site labor and weather risk; trend is most visible in 1.0-2.0 MTPA additions and in conversion of legacy peak-shaver designs. Yamal LNG and Arctic LNG 2 demonstrated module-yard fabrication for greenfield in extreme climates; the modularization pattern is now standard for parallel-train US Gulf Coast greenfield as well.
- **US LNG dominance post-2020** — sustained Henry-Hub-indexed feed-gas pricing combined with rapid permitting through FERC has made US Gulf Coast greenfield and brownfield the dominant new-supply shape through the early 2020s. Asia-Pacific demand and post-Russia-Ukraine European demand pull have anchored the offtake side. The DOE export-pause / resumption cycles (2024 pause, subsequent reactivation) introduced regulatory-timing risk into the FEED-to-FID window.
- **FSRU as crisis-response capacity** — the 2022-2024 European response demonstrated FSRU's role as bridging regas capacity that can deploy in months rather than years; multiple new FSRUs were chartered or repositioned to Northwest European and Mediterranean ports during this window. Wilhelmshaven, Eemshaven, Mukran, Piombino, and Alexandroupolis represent the canonical 2022-2024 European FSRU deployment cohort.
- **Climate-policy headwinds and methane-intensity gating** — EU Methane Regulation (Regulation (EU) 2024/1787) and US EPA Subpart W reporting place a methane-intensity requirement on cargoes into EU regasification terminals; project-shape selection now factors in upstream methane intensity as an additional design and contracting variable. See [LNG Regulatory Framework](./lng-regulatory-framework.md) for the regulatory layer.
- **Small-scale and bunkering growth** — IGF Code maturation and increasing dual-fuel newbuild orderbook for container, cruise, and PCTC fleets has expanded marine bunkering demand; small-scale LNG plants and bunker-vessel fleets are growing in line with this demand. The 2020s saw rapid expansion of LNG-bunker-fuel infrastructure at major hub ports and the standardization of ship-to-ship bunkering practice under SIGTTO and IGF coverage.
- **FLNG second-generation scaling** — ENI Coral Sul (2022 first cargo) and BP Greater Tortue Ahmeyim (delayed but progressing) demonstrate the second-generation FLNG operating envelope: deepwater frontier, cross-border hub, and breakwater-protected near-shore. The trend is toward smaller, repeatable hulls rather than Prelude-class single-asset gigantism.

## Cross-references

- [LNG Project Lifecycle](./lng-project-lifecycle.md) — phase-duration differences across the archetypes above.
- [LNG Marine Transfer Systems](./lng-marine-transfer-systems.md) — shape-specific transfer interfaces (jetty vs. side-by-side vs. tandem).
- [LNG Storage Tanks](./lng-storage-tanks.md) — onshore-storage selection differs from FLNG / FSRU cargo-containment.
- [LNG Liquefaction Processes](./lng-liquefaction-processes.md) — process-family selection by archetype (large-train C3MR / AP-X for greenfield; mixed-refrigerant for FLNG; nitrogen-expander for small-scale).
- [LNG Process Safety](./lng-process-safety.md) — exclusion-zone interaction with shape selection.
- [LNG Regulatory Framework](./lng-regulatory-framework.md) — authority-stack differences between onshore and floating archetypes.
- **Cross-wiki (marine-engineering)**: [Mooring Systems](../../../marine-engineering/wiki/concepts/mooring-systems.md) — FLNG and FSRU mooring-system selection (turret, tower yoke, spread mooring) is a marine-engineering interface.
