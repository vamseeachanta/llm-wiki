---
title: "LNG Composition Management"
tags: [lng-projects, concept, composition, wobbe-index, heating-value, lean-rich, ethane, propane, gas-quality, downstream-customer, dehydration, mercury-removal]
added: 2026-05-09
last_updated: 2026-05-10
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

### Composition-spectrum reference table

| Source basin | Stream class | Indicative CH4 | Indicative C2+ | Notes |
|---|---|---|---|---|
| Qatar (Ras Laffan) | Lean | ~98% | <2% | Heavy upstream fractionation; ethane export as separate product |
| US Gulf Coast (Sabine Pass, Cameron, Freeport, Corpus Christi) | Lean | ~95-97% | 2-4% | Pipeline-spec feed gas; lean by upstream-pipeline default |
| Norway (Snøhvit / Hammerfest) | Lean | ~96% | <3% | Dry feed; CO2 captured and reinjected |
| Trinidad (Atlantic LNG / ALNG) | Rich | ~85% | ~12% C2 / ~2% C3 | Historic richest mainstream cargo |
| Indonesia (Bontang historic) | Rich | ~88-90% | C2+C3 ~8-10% | Historic rich; modern trains drift leaner |
| Algeria (Bethioua / Skikda) | Rich | ~88% | ~10% | Wet-liquefaction tradition |
| Australia (NW Shelf, Gorgon, Ichthys, Wheatstone) | Mixed | ~88-95% | varies by train | Composition shifts by field tie-back |
| Russia (Sakhalin-2, Yamal) | Variable | varies | varies | Field-condition-dependent |
| Malaysia (Bintulu) | Variable | varies | varies | Multi-train blend |

### Wobbe Index regional-spec reference table

| Region | Wobbe target band (BTU/scf) | Wobbe target band (MJ/m³) | Notes |
|---|---|---|---|
| Asia-Pacific (JP / KR / TW high-Wobbe) | ~1390-1420 | ~51.7-52.8 | Receiving-tariff bands favor rich-end gas |
| Europe (EU continental + UK) | ~1390-1410 | ~51.7-52.4 | National tariffs vary; UK NTS slightly lower |
| US (Henry Hub pipeline-spec) | ~1330-1370 | ~49.5-51.0 | Lower than Asian receivers; lean LNG re-blended with N2 if needed |
| Brazil + Argentina | ~1340-1380 | ~49.9-51.4 | Receiving-tariff influenced by domestic pipeline gas |

The Asia-Pacific / EU / US gap is the structural reason that lean US Gulf Coast cargoes routinely require treatment (LPG enrichment or N2 ballasting elsewhere) to enter Asia-Pacific receiving terminals at-spec.

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

## Worked-cases (precedent classes)

Specific LNG SPA composition disputes are commercially confidential and arbitrated under bilateral or institutional rules; the public record reflects classes-of-event rather than per-cargo numbers. The recurring patterns are:

- **HHV-pricing dispute precedents** — class-of-event: an SPA priced on $/MMBTU on an HHV basis reaches discharge with a measured HHV outside the ±2% routine tolerance band. The buyer either invokes the discount-and-remedy clause or rejects the cargo; the seller's invoicing position is supported by the load-port chain-of-custody analysis. Resolution turns on the agreed compositional-survey method (sampling frequency, witnessed analysis, third-party verification) rather than on the molecular composition itself.
- **Off-spec cargo handling under SPA** — class-of-event: the FERC-style LNG SPA boilerplate (used as a template by many US export terminal SPAs) prescribes a measured-and-witnessed analysis at load and discharge, with a deviation-band that triggers either acceptance-with-discount or rejection-with-remedy. Composition is the evidentiary spine of either path.
- **Cargo-blending at receiving terminals** — class-of-event: a receiving terminal accepts a sequence of cargoes with mixed compositions and blends them in storage to satisfy a downstream pipeline-tariff Wobbe Index band. The blending decision can include N2 injection, LPG enrichment, or simple co-storage; the operational record turns into evidence in any pipeline-tariff dispute.
- **Lean-cargo entry to Asia-Pacific markets** — class-of-event: lean US Gulf Coast cargoes (~95% CH4) entering Asia-Pacific receiving terminals at the high-Wobbe end of the band require either LPG enrichment at a producer-side adjustment unit or contractual receiver-side handling under a bespoke tariff allowance.

## Future trends

- **Carbon-intensity (CI) tagging post-2024** — lifecycle CO2-equivalent intensity (CI) is now a routinely-reported per-cargo metric in the post-2024 LNG trade; low-carbon LNG buyers increasingly tie purchase decisions and price differentials to CI alongside conventional composition. The CI metric stacks production, transport, and discharge methane and CO2 emissions, and combines naturally with the methane-intensity reporting required under [EU Methane Regulation 2024/1787](./lng-boil-off-gas-management.md) and [EPA Subpart W](./lng-vapor-handling.md). The implication for composition management is that the molecular spec (Wobbe Index, HHV, inerts) no longer fully describes a delivered cargo — CI is now a parallel acceptance dimension.
- **Bio-LNG and e-LNG composition** — synthetic methane streams (from biomethane upgrading or power-to-methane) are reaching commercial scale, and composition-tracking conventions are adapting to cover renewable-origin attestation alongside molecular composition.
- **Lower-carbon Wobbe-target shift** — some markets are reducing target Wobbe Index to align imported LNG with renewable-natural-gas pipeline-injection specifications, narrowing the acceptable composition envelope at receiving terminals.

## Cross-References

- [NFPA 59A](../standards/nfpa-59a.md) — composition-related design provisions for US onshore LNG facilities
- [IMO IGC Code](../standards/igc-code.md) — cargo-spec verification and cargo-handling provisions for LNG carriers
- [LNG Liquefaction Processes](./lng-liquefaction-processes.md) — composition envelope is determined upstream of and inside the liquefaction train
- [LNG Storage Tanks](./lng-storage-tanks.md) — rollover-prevention practice depends on composition tracking across stored cargoes
- [LNG Process Safety](./lng-process-safety.md) — cryogenic-equipment integrity (mercury, CO2-freeze, water-ice) ties composition limits to safety design
