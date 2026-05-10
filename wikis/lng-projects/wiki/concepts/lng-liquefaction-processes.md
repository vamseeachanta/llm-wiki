---
title: "LNG Liquefaction Processes"
tags: [lng-projects, concept, liquefaction, process-technology, refrigeration, c3mr, ap-x, cascade, dmr, mfc, smr]
added: 2026-05-03
last_updated: 2026-05-09
sources: [concept-synthesis]
domain: lng-projects
cross_links:
  - ../concepts/lng-storage-tanks.md
  - ../concepts/lng-boil-off-gas-management.md
  - ../concepts/lng-process-safety.md
  - ../concepts/lng-composition-management.md
  - ../../standards/nfpa-59a.md
  - ../../standards/ferc-18-cfr-153.md
  - ../../standards/phmsa-49-cfr-193.md
  - ../../standards/igc-code.md
---

# LNG Liquefaction Processes

## Scope

This page surveys the liquefaction-process families licensed by the major industrial-gas, oil-major, and engineering-company licensors for baseload onshore LNG, mid-scale LNG, and floating LNG (FLNG) service. It is a neutral overview only; it does **not** rank technologies, enumerate per-train MTPA capacity caps, restate proprietary process diagrams or process-licensing royalty schedules, or rank licensors against active project FIDs. Vendor names appear as canonical industry references, not endorsements. Cold-box mechanical design depth, refrigerant-loop control philosophy, and turbo-expander specification depth are reserved for vendor-spec authoring routes outside this public wiki.

## Why liquefaction-process choice governs project economics

- **Capital intensity** — onshore baseload LNG trains typically run in the 4-8 MTPA range and represent multi-billion-dollar capital commitments per train; the choice of liquefaction process drives heat-exchanger arrangement, compressor selection, and modularization strategy, all of which set capex within an order of magnitude.
- **Specific power consumption** — competing processes differ by single-digit percentages in specific-power per ton of LNG produced; over the 20-30 year operating life of a baseload terminal, those percentages compound into substantial fuel-gas-burn or electricity differences.
- **Train scaling vs. parallelization** — APCI processes (C3-MR, AP-X) scale single-train capacity high; ConocoPhillips Optimized Cascade favors parallelizable two-train arrangements that share infrastructure. The two scaling philosophies imply different plot plans, sparing strategies, and shutdown-availability profiles.
- **FLNG and mid-scale fit** — single-mixed-refrigerant (SMR) and small-cascade variants dominate floating and mid-scale projects, where deck-area constraints, sea-state motion sensitivity, and modular fabrication trade differently against thermodynamic efficiency.

## Major liquefaction-process families

### APCI C3-MR (propane pre-cooled mixed refrigerant)

- Air Products & Chemicals Inc. workhorse process for large baseload trains; dominant historic share of installed capacity globally.
- Two refrigeration loops: a propane (C3) pre-cooling loop chills feed gas and the mixed-refrigerant stream to roughly minus 30 to minus 40 degrees C; the mixed-refrigerant (MR) loop (typically nitrogen, methane, ethane, propane) delivers the deep liquefaction down to LNG temperature.
- Spool-wound main cryogenic heat exchanger (MCHE) is a defining APCI element — large diameter, long, multi-tube-bundle vessel manufactured at a small number of qualified shops.
- Train capacity has scaled from early-generation roughly 2 MTPA up through modern roughly 4-5 MTPA single-train designs.

### APCI AP-X

- APCI variant adding a nitrogen sub-cooling loop downstream of the C3-MR core; the nitrogen loop assumes the deep sub-cooling duty that would otherwise constrain a pure C3-MR scaling envelope.
- Adopted on Qatargas mega-trains targeting train capacities historically up to roughly 7.8 MTPA.
- Three-loop arrangement (propane pre-cool, mixed refrigerant, nitrogen sub-cool) increases compressor-train count and capital intensity but unlocks the high-end of single-train scaling.

### ConocoPhillips Optimized Cascade

- Three pure-component refrigerant loops: propane (pre-cool), ethylene (intermediate), methane (deep liquefaction).
- Pure-component refrigerants simplify make-up management and inventory control relative to mixed-refrigerant systems; brazed-aluminum heat exchangers (BAHX) replace the spool-wound MCHE characteristic of APCI processes.
- Favoured for parallel-train modular designs (Sabine Pass, Corpus Christi, Freeport, Cheniere portfolio) where two or more trains share infrastructure.
- Specific power and unit capex are competitive with APCI for the modular two-train arrangement; train capacity per train is typically lower than AP-X.

### Shell Dual Mixed Refrigerant (DMR)

- Two mixed-refrigerant loops: a "warm" MR loop replaces propane in the pre-cool duty, and a "cold" MR loop carries deep liquefaction.
- Used on cold-climate baseload projects (Sakhalin LNG) where ambient temperature lets the warm MR loop run more efficiently than a propane loop.
- Mixed-refrigerant composition flexibility allows tuning to ambient and feed-gas conditions.

### Linde Mixed Fluid Cascade (MFC)

- Three mixed-refrigerant loops: pre-cool, liquefaction, and sub-cool stages each running a tailored MR composition.
- Adopted at Snøhvit (Hammerfest LNG, Norway) — the first European-Arctic baseload project — and at select onshore and floating LNG installations.
- Plate-fin heat exchangers (PFHE) are the heat-transfer workhorse, suiting Linde's exchanger-fabrication base.

### Single Mixed Refrigerant (SMR) and small-cascade variants

- **Black & Veatch PRICO** — single-loop mixed-refrigerant process; the canonical SMR baseline for mid-scale and small-scale LNG.
- **Other SMR variants** — Air Products LiMuM, Linde StarLNG, Wärtsilä Hamworthy, Saipem variants, and ChartLNG / IPSMR for mid-scale and FLNG service.
- **Small cascade** — pure-component or mixed cascade variants in the 0.1-2 MTPA range used for peak-shaving, virtual-pipeline, and bunker-fuel LNG facilities.
- SMR is the dominant FLNG choice — Petronas FLNG Satu, Petronas FLNG Dua, ENI Coral South, Golar Hilli (re-purposed Moss carrier hull), and similar deployments use SMR or compact dual-MR variants.

## Process-component vendors and integration

- **Cryogenic compressors** — GE / Baker Hughes (formerly GE Oil & Gas), Siemens Energy, Atlas Copco for the propane, MR, ethylene, methane, and nitrogen-loop services.
- **Heat exchangers** — Air Products (spool-wound MCHE), Chart Industries (BAHX, PFHE), Linde Engineering (PFHE), Kelvion, Alfa Laval for the smaller-duty exchangers.
- **EPC contractors** — Bechtel (Cheniere portfolio), McDermott / CB&I, JGC, Chiyoda, Saipem, TechnipFMC (now Technip Energies), Kentz / SNC-Lavalin.
- **Floating-hull yards** — Samsung Heavy Industries, Daewoo Shipbuilding & Marine Engineering (DSME), Hyundai Heavy Industries, Hudong-Zhonghua, Jiangnan, Wison Offshore & Marine, CSSC Offshore & Marine Engineering have delivered FLNG/FSRU hulls; relevant for licensor-vs-hull distinction in capability surveys.

## Train sparing and modularization

- **Single-train projects** — historically common up through the late 2000s; one APCI C3-MR or AP-X train at 4-7 MTPA. Single-train availability and turnaround economics drove later moves toward parallelization.
- **Parallel-train modular designs** — Cheniere portfolio (Sabine Pass, Corpus Christi, Plaquemines), Freeport LNG, Cameron LNG. Multiple smaller trains (typically 4-6 MTPA each) sharing storage, marine berths, utilities, and outloading infrastructure.
- **Modular fabrication** — Yamal LNG and Arctic LNG 2 demonstrated module-yard fabrication of liquefaction trains shipped to Arctic site, reducing on-site labor exposure to extreme-climate construction conditions.
- **FLNG single-train hulls** — single liquefaction train per hull is the rule; Petronas FLNG Satu (~1.2 MTPA), Petronas FLNG Dua (~1.5 MTPA), Prelude (~3.6 MTPA), and Coral South (~3.4 MTPA) operate single-train SMR or compact-DMR processes.

## Standards / References

- [NFPA 59A](../standards/nfpa-59a.md) — design code for the liquefaction-train cold box, refrigerant containment, and onshore plant siting.
- [FERC 18 CFR 153](../standards/ferc-18-cfr-153.md) — US LNG siting authority for liquefaction export terminals (Resource Reports + NEPA).
- [PHMSA 49 CFR 193](../standards/phmsa-49-cfr-193.md) — US LNG facility safety operations governing liquefaction plants in service.
- [IGC Code](../standards/igc-code.md) — IMO ship-construction code for the marine cargo-side interface to the liquefaction product.
- [API Std 625](../standards/api-std-625.md) — companion design code for the storage-tank system that receives the liquefaction-train product.
- IACS class rules for gas carriers and floating LNG units (process containment interfaces): <https://iacs.org.uk/>
- IMO IGC Code reference: <https://www.imo.org/en/OurWork/Safety/Pages/IGC-Code.aspx>

## Future trends

- **Electrified liquefaction** — electric-motor-driven compressors replacing gas-turbine drivers, supporting decarbonization of the liquefaction Scope 1 footprint and enabling renewable-power integration. Adopted in Hammerfest LNG (Snøhvit) historically and increasingly specified on new projects.
- **Methane-emission-aware design** — integration of liquefaction-process design with leak-detection-and-repair (LDAR), routine-vent elimination, and methane-intensity reporting under EU Methane Regulation 2024/1787 and US EPA Subpart W.
- **Carbon capture integration** — pre-combustion CO2 capture on liquefaction-train fuel-gas (electrified processes reduce the in-plant CO2 source) and post-combustion capture on gas-turbine drivers; Snøhvit-style geological sequestration as a project-level integration option.
- **FLNG scaling** — second-generation FLNG hulls targeting larger train capacities and reduced cost-per-ton; ENI Coral South, BP Greater Tortue Ahmeyim, and Mozambique LNG floating units demonstrate the operating envelope.
- **Hydrogen and ammonia liquefaction parallel** — many of the heat-exchanger and cryogenic-compressor technologies above are scaling toward liquid-hydrogen liquefaction; KHI Suiso Frontier (2022) demonstrated cryogenic hydrogen carrier service. Cross-pollination of LNG liquefaction know-how into the energy-transition cryogenic-fuels space is active.

## Cross-references

- [LNG Storage Tanks](./lng-storage-tanks.md) — downstream containment of the liquefaction product.
- [LNG Boil-Off Gas Management](./lng-boil-off-gas-management.md) — heat-leak management at the train cold box and storage interface.
- [LNG Process Safety](./lng-process-safety.md) — release-scenario consequences from cold-box, refrigerant-storage, and feed-gas inventories.
- [LNG Composition Management](./lng-composition-management.md) — feed-gas and product-LNG composition envelope that drives liquefaction-loop refrigerant-blend specification.
- [LNG Cargo Containment Systems](./lng-cargo-containment-systems.md) — ship-side containment that receives the liquefaction-train product at outloading.
- [LNG Marine Transfer Systems](./lng-marine-transfer-systems.md) — outloading interface between the liquefaction terminal and the receiving carrier.
