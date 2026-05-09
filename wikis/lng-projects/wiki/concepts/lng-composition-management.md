---
title: "LNG Composition Management"
tags: [lng-projects, concept, composition, wobbe-index, heating-value, lean-rich, ethane, propane, gas-quality, downstream-customer, dehydration, mercury-removal]
added: 2026-05-09
last_updated: 2026-05-09
sources: [concept-synthesis]
domain: lng-projects
cross_links:
  - ../../standards/nfpa-59a.md
  - ../../standards/igc-code.md
  - ./lng-liquefaction-processes.md
  - ./lng-storage-tanks.md
  - ./lng-process-safety.md
---

# LNG Composition Management

## Scope

This page surveys LNG-stream composition variation across producing basins, the gas-quality framework (Wobbe Index, heating value) that downstream receivers use to bound acceptable cargo, and the upstream-and-terminal operations that keep delivered LNG inside contracted specifications. It does **not** restate sales-and-purchase agreement (SPA) clause language, jurisdictional pipeline-tariff numerical bands, or proprietary fractionation flowsheets — those belong in standards-page or contract-document surfaces.

## Why composition management matters

- **Downstream burner compatibility** — residential, commercial, and industrial gas appliances are designed for a specific Wobbe Index range; out-of-band gas can over-fire or under-fire burners and create combustion-safety issues at the burner tip.
- **Pipeline injection specs** — receiving-pipeline operators set composition tolerances enforced through tariffs (for example, FERC-approved tariffs at US import terminals) covering Wobbe Index, heating value, inerts, and trace contaminants.
- **Industrial customer specs** — petrochemical and power-generation customers may require lean (low-C2/C3) gas to meet feedstock or turbine-fuel specifications, while LPG-extraction economics may favor rich gas at terminals with downstream fractionation.
- **Cargo-quality tracking** — long-term LNG SPAs include composition specifications and heating-value-based pricing; chain-of-custody compositional analysis at load and discharge is the basis for invoicing and dispute resolution.

## LNG composition spectrum

- **Lean LNG** (>95% CH4) — Qatar (Ras Laffan), US Gulf Coast (Sabine Pass, Cameron, Freeport), and Norway (Snøhvit / Hammerfest). Ethane and heavier components are pre-extracted via upstream fractionation, leaving a methane-dominant stream.
- **Rich LNG** (85–92% CH4) — Trinidad, Indonesia (Bontang historic), Algeria (Bethioua), and some Australian streams. Higher C2 and C3 content; "wet" liquefaction in which heavier hydrocarbons remain in the LNG.
- **Variable** — Russia (Sakhalin-2, Yamal) and Malaysia (Bintulu) deliver streams whose composition shifts with field conditions and feed-gas blending decisions.

Indicative composition shorthand for the three reference points:

- Qatar lean: ~98% CH4
- Trinidad rich: ~85% CH4 / ~12% C2 / ~2% C3
- US Gulf Coast: ~95% CH4 (lean)

## Wobbe Index framework

- **Definition** — Wobbe Index (WI) = HHV / √(specific gravity); a proxy for gas-burner thermal-output equivalence at constant inlet pressure and orifice geometry. Two gases with the same WI deliver the same heat through the same burner.
- **Common ranges** — Asia-Pacific receivers ~1390–1420 BTU/scf (~51.7–52.8 MJ/m³); EU receivers ~1390–1410 BTU/scf; US Henry Hub ~1330–1370 BTU/scf (lower-Wobbe pipeline gas).
- **HHV ranges** — 1010–1180 BTU/scf depending on composition.
- **Tolerance bands** — typical ±2% of Wobbe Index target for routine operation; hard-band limits (often ±5%) trigger off-spec procedures.

## Composition-driven operations

- **Liquefaction-side composition control** — feed-gas pre-treatment and LPG-extraction tuning at upstream gas plants set the leaving-product composition envelope before liquefaction.
- **Storage-tank stratification and rollover** — compositional variation drives density variation between layers; dense-over-light stratification can trigger spontaneous rollover (see [LNG Process Safety](./lng-process-safety.md) and the storage-tank page).
- **Cargo blending** — receiving terminals may co-mingle cargoes from different producers in storage to meet downstream Wobbe Index and HHV specifications; some terminals add nitrogen or LPG to adjust the delivered stream.
- **Heating-value pricing** — SPAs typically price on HHV (energy-delivered) rather than volume; composition management is therefore directly a revenue-management activity.

## Mercury and sulfur considerations

- **Mercury removal** — performed at the upstream gas plant; HgT is typically held below ~50 ng/Nm³ at the LNG plant outlet to protect downstream cryogenic-aluminum equipment integrity (mercury embrittlement of brazed-aluminum heat exchangers).
- **Sulfur removal** — H2S and COS are removed at the upstream gas plant; LNG-plant H2S is typically held below ~3 ppm.
- **CO2 removal** — required upstream of liquefaction because CO2 freezes at ~ -78 °C and would plug cryogenic heat-exchanger passages; amine wash plus molecular-sieve polishing is the standard combination, with CO2 driven below ~50 ppm before pre-cooling.

## Dehydration

- **Water removal** — feed gas is dried to <0.1 ppm water before liquefaction; otherwise water freezes in cryogenic equipment and heat-exchanger passages.
- **Process** — tri-ethylene-glycol (TEG) contactor dehydration units followed by molecular-sieve beds at the upstream gas plant deliver the required dryness.

## SPA and dispute considerations

- **Sales and Purchase Agreements (SPAs)** — long-term LNG SPAs include composition specifications (Wobbe Index, HHV, inerts, trace contaminants); gas-quality disputes are a recurring source of arbitration in the LNG trade.
- **Off-spec cargo handling** — typical SPA language permits the buyer to reject an off-spec cargo or accept it at a discount with a remedy obligation on the seller; load-port and discharge-port composition surveys form the evidentiary record.

## Future trends

- **Carbon-intensity composition reporting** — lifecycle CO2-equivalent intensity (CI) is emerging as a per-cargo metric; low-carbon LNG buyers increasingly tie purchase decisions to CI alongside conventional composition.
- **Bio-LNG and e-LNG composition** — synthetic methane streams (from biomethane upgrading or power-to-methane) are reaching commercial scale, and composition-tracking conventions are adapting to cover renewable-origin attestation alongside molecular composition.
- **Lower-carbon Wobbe-target shift** — some markets are reducing target Wobbe Index to align imported LNG with renewable-natural-gas pipeline-injection specifications, narrowing the acceptable composition envelope at receiving terminals.

## Cross-References

- [NFPA 59A](../standards/nfpa-59a.md) — composition-related design provisions for US onshore LNG facilities
- [IMO IGC Code](../standards/igc-code.md) — cargo-spec verification and cargo-handling provisions for LNG carriers
- [LNG Liquefaction Processes](./lng-liquefaction-processes.md) — composition envelope is determined upstream of and inside the liquefaction train
- [LNG Storage Tanks](./lng-storage-tanks.md) — rollover-prevention practice depends on composition tracking across stored cargoes
- [LNG Process Safety](./lng-process-safety.md) — cryogenic-equipment integrity (mercury, CO2-freeze, water-ice) ties composition limits to safety design
