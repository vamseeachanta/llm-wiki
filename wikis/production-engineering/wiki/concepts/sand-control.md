---
title: "Sand Control"
tags: [sand-control, completions, gravel-pack, frac-pack, sand-screen, unconsolidated-reservoir, deliverability]
sources:
  - iso-17824
added: 2026-05-15
last_updated: 2026-05-15
---

# Sand Control

## Scope

Sand control is the family of completion practices that prevents formation sand from being produced into the wellbore — or that manages the produced-sand stream when prevention is impossible. In **unconsolidated** or **weakly consolidated** reservoirs (offshore West Africa, Gulf of Mexico shelf, North Sea Tertiary, South China Sea Tertiary, and many onshore Tertiary basins), sand production is the dominant deliverability-and-failure-mode lever in the well's life. Choice of sand-control architecture locks in the deliverability ceiling, the intervention envelope, and the long-term integrity profile of the well.

This page is the **router** for sand-control coverage in the production-engineering wiki. It synthesises the failure modes, the architecture catalogue, the decision framework, the perforation-strategy coupling, and the cross-domain interactions, and links out to dedicated pages for [gravel packing](gravel-packing.md), [frac packing](frac-packing.md), and [sand-control screens](sand-control-screens.md).

## Why sand control is high-leverage

Sand production interacts directly with every other production-engineering decision:

- **Deliverability ceiling** — the maximum sand-free rate is set by completion architecture. Standalone screens may be limited to drawdowns 200-400 psi below critical; gravel-packs and frac-packs typically support 1,000-3,000+ psi; chemical consolidation sits between depending on consolidation effectiveness.
- **Artificial-lift compatibility** — sand erodes ESP impellers, abrades PCP elastomers, plugs gas-lift valves, and damages plunger-lift seals. The sand-control completion type effectively gates the available lift options; see [Electric Submersible Pumps](electric-submersible-pumps.md), [Progressing-Cavity Pumps](progressing-cavity-pumps.md).
- **Intervention envelope** — gravel-packed and frac-packed completions are extremely difficult to recomplete; the design choice locks the well into the original perforated interval for the rest of its life. Standalone screens are slightly more recoverable but still fragile.
- **Surface-handling cost** — produced-sand streams require surface separators, dump-and-clean cycles, sand-erosion-rated piping, and disposal logistics. Even modest produced-sand rates impose six- and seven-figure surface-cost bills over field life.
- **Well-integrity profile** — sand-influx events that breach the screen or pack initiate cavity growth behind casing, leading to lost circulation pathways, casing collapse from formation-sand load, and in extreme cases loss of the well.

Sand-control choice also couples back to **upstream** decisions made in well construction (production-casing ID must accommodate the sand-control assembly OD plus running clearance) and in completion design (perforation strategy, in particular shot-density floor and big-hole charge selection); see the perforation-strategy coupling section below.

## Failure modes — what sand control prevents

Operators design sand-control completions against four well-recognised failure modes:

### 1. Continuous sand production

The reservoir produces a steady fines-and-sand stream alongside the hydrocarbon. Even small mass fractions (10-50 lb / 1,000 bbl) cause cumulative damage to surface and downhole equipment. Continuous production is the **default outcome** in unconsolidated sand without any sand-control architecture in place.

### 2. Catastrophic sand influx

A drawdown step-change, a pressure transient, a water-cut breakthrough, or a perforation-tunnel collapse triggers a sudden, large sand-volume influx. The sand fills the wellbore, kills the well, and frequently buries the bottomhole assembly. Recovery requires a costly intervention (coiled tubing washover, workover) and often a re-completion.

### 3. Sand bridging across the production tubing

Produced sand drops out of suspension at flow restrictions or rate decreases, accumulating at the bottom of the tubing string. Eventually the bridge restricts flow, then chokes off the well. Resolution requires intervention or an artificial-lift change.

### 4. Erosional failure of downhole or surface hardware

Sand-laden flow erodes choke trim, valve seats, ESP impellers, gas-lift valves, surface-piping bends, and separator inlet diverters. Failure rates scale strongly with both rate and sand cut. Some failures (e.g. choke-trim breach) initiate well-control events.

## Completion-architecture catalogue

Sand-control architectures, in roughly ascending order of mechanical and capital intensity:

| Architecture | Where it works | What it doesn't handle |
|---|---|---|
| **Selective perforating + drawdown management** | Mildly consolidated reservoirs where conservative drawdown floors sand production | Aggressive drawdowns; long-term reservoir-pressure-decline operation |
| **Chemical consolidation** | Short, well-defined sand intervals (typically <30 ft); shallow wells | Long intervals; high-temperature wells (consolidant degradation); recompletion flexibility |
| **Standalone screens** | Wells with well-sorted formation sand (PSD with low fines fraction); moderate drawdown | Poorly-sorted PSDs (fines plug screen); aggressive drawdown; aggressive workover sediment |
| **Pre-packed screens** | Cased and perforated completions in modestly poorly-sorted PSDs | Very-fine-fines-dominated formations; very-aggressive drawdown |
| **Open-hole gravel pack** | Long horizontal sections in unconsolidated sand; high-rate wells | Short vertical sections (capital not justified); cased-hole completions (use cased-hole gravel pack instead) |
| **Cased-hole gravel pack** | Cased and perforated multi-zone completions; high-rate wells | Open-hole completions; very-fine PSDs that demand frac-pack |
| **Frac-pack** | Wells where deliverability and sand control are *both* gating; high-rate Gulf of Mexico shelf and similar service | Low-rate wells (cost not justified); very fragile reservoirs (frac may breach overburden) |
| **Expandable screens** | Long open-hole sections where running clearance is tight; horizontal infill wells | Heavy fines loading; aggressive drawdowns where the screen-formation gap remains (residual annular space) |

See dedicated pages for [Gravel Packing](gravel-packing.md), [Frac Packing](frac-packing.md), and [Sand Control Screens](sand-control-screens.md).

## The four design questions

Any sand-control job answers four operator questions, in roughly this order:

1. **Will the formation produce sand at planned drawdown?** — particle-size distribution analysis, formation-strength testing, offset-well sand history. If no, sand control may be unnecessary.
2. **Open-hole or cased-and-perforated?** — driven by reservoir architecture and well type. Open-hole favours gravel-pack or expandable; cased-hole favours frac-pack, cased-hole gravel-pack, or screens deployed inside casing.
3. **Which architecture?** — driven by the matrix above plus the deliverability-ceiling target and the artificial-lift method.
4. **Which screen and gravel sizing?** — driven by the formation PSD and the [Saucier criterion](gravel-packing.md) (or its descendants for non-uniform PSDs). This is where the dominant in-service failure mode originates: undersized gravel allows fines flow-through; oversized gravel allows formation sand to migrate into the pack and bridge it.

These four decisions interlock: a poor PSD characterisation in question 4 wastes the investment made answering questions 1-3 well.

## Perforation-strategy coupling

Sand-control architectures impose hard requirements on perforation strategy that the perforation engineer must accept upstream of the sand-control job:

- **Big-hole charges are mandatory for cased-hole gravel-pack and frac-pack** — the casing-wall area is the throttle for both gravel placement (during pack execution) and high-rate proppant slurry (during frac-pack pumping). Deep-penetrating charges that are correct for natural completion are wrong for sand-control.
- **Shot-density floors are dictated by sand-control type** — gravel-packs require 12-18+ spf to give the gravel a uniform pack-and-flow geometry; frac-packs require 6-12 spf because the frac dominates near-wellbore flow but the gravel must still distribute; standalone screens are often fed by 8-12 spf perforations.
- **Phasing is isotropic (60° / 90°)** for sand-control completions because the gravel pack must distribute uniformly around the wellbore. Oriented (0° / 180°) phasing is reserved for cased-hole frac-only completions and is wrong for any sand-control architecture.
- **Underbalanced perforating gives cleaner tunnels** for gravel-pack execution because crushed-zone debris is flushed *out* rather than packed *in*. UBP is preferred where surface equipment supports it; the post-perforation gravel-pack execution then has clean tunnels to fill.
- **Big-hole charges in unconsolidated sand are themselves a known sand-influx trigger** — the same big-hole geometry that makes the casing-wall area conducive to gravel placement also makes it conducive to formation sand entering uncontrolled if the gravel pack is poorly placed or breached. The sand-control completion is therefore not an optional addition to a perforated unconsolidated-sand interval — it is required by the perforation-policy choice.

For the perforation-strategy framework that pairs with sand-control completions, see [Perforation Strategy](perforation-strategy.md). For the perforating physics that makes big-hole charges different from deep-penetrating charges, see [Perforating](perforating.md) and [Perforating — Shaped Charges](perforating-shaped-charges.md).

## Decision framework — selecting a sand-control architecture

A simplified operator decision tree:

1. **Confirm sand will be produced.** PSD analysis, formation-strength testing, offset-well sand history. If formation strength comfortably exceeds expected drawdown stress, no sand control may be required (defensive perforating policy may suffice).
2. **Determine well architecture.** Open-hole horizontal → gravel-pack or expandable screens. Cased-hole vertical or deviated → frac-pack, cased-hole gravel-pack, or screens.
3. **Determine deliverability target.** High-rate (multi-thousand bbl/d) requires gravel-pack or frac-pack. Moderate-rate may allow standalone or pre-packed screens.
4. **Characterise formation PSD.** Fine-fines-dominated PSD biases toward frac-pack (the proppant pack handles fines better than a screen-only design); well-sorted moderate-coarse PSD allows standalone screens; intermediate PSDs are gravel-pack territory.
5. **Match to artificial-lift plan.** Sand-tolerant lift (PCP, plunger lift) gives more architectural flexibility; sand-intolerant lift (ESP, gas lift) demands the most aggressive sand-control architecture available.
6. **Check intervention envelope.** Operators planning multi-zone recompletion must avoid frac-packs (essentially permanent) and prefer gravel-packs or screens (more amenable to washover-and-redo).

## Vendor archetype framing

Sand-control services are dominated by the four integrated majors plus screen-specialist independents:

- **Halliburton sand-control services** — integrated gravel-pack, frac-pack, screen, and chemical-consolidation portfolio.
- **Schlumberger sand-control services** — comparable portfolio; historically strong in frac-packing and openhole gravel-pack execution.
- **Baker Hughes sand-control services** — comparable portfolio; multi-zone gravel-pack systems are a notable specialty.
- **Weatherford sand-control services** — specialty hardware including expandable-screen offerings.

Independent screen specialists also serve operators who source screens separately from the rest of the completion contract; vendor archetypes are named at the concept level only and no proprietary algorithm or hardware-design content is reproduced. Operators evaluating sand-control vendors should consult vendor data sheets and the [ISO 17824](../standards/iso-17824.md) qualification records for the specific screen products under consideration.

## Cross-domain interactions

- **Inflow performance** — sand-control completions add a near-wellbore pressure-drop component (perforation skin × screen-and-pack pressure drop). Frac-packs reduce or invert this skin via the frac-conductivity contribution; gravel-packs typically add modest pressure drop; standalone screens add the smallest pressure drop but at the cost of fragility.
- **Artificial lift** — see [Electric Submersible Pumps](electric-submersible-pumps.md) for ESP-side sand sensitivity; PCP and plunger lift are also sand-touched.
- **Casing and tubing design** — production-casing ID must accommodate the gravel-pack assembly OD plus running clearance. The sand-control assembly typically forces the completion engineer back to drilling-engineering to confirm casing-program adequacy. See [Casing Program Design](../../../drilling-engineering/wiki/concepts/casing-program-design.md).
- **Perforating** — see the perforation-strategy coupling section above; sand-control type dictates charge family and shot-density floor.
- **Stimulation interaction** — frac-packs are themselves a stimulation; matrix-acid stimulation post-installation must be designed not to chemically degrade the screen or destabilise the gravel pack.
- **Subsea / FPSO integration** — produced-sand handling at the FPSO topside imposes separator and disposal requirements that scale with the sand-control completion's effectiveness; the design margin in the topside sand-handling system is set in part by the sand-control completion's design margin.

## Standards anchor

- [ISO 17824 — Sand Control Screens](../standards/iso-17824.md) — open-hole gravel-pack screen qualification (canonical international reference).
- ISO 17825 — sister standard for cased-hole gravel-pack screens (adjacent; not yet a standalone wiki page).
- API-equivalent screen-qualification practices — typically cited alongside ISO 17824 / 17825 in dual-standard procurement specs.
- NACE MR0175 / ISO 15156 — sour-service material requirements applicable to sand-control hardware in CO2 / H2S service (adjacent).
- [API RP 19B](../standards/api-rp-19b.md) — perforator evaluation; sand-control jobs use big-hole charges that this RP characterises (cross-link only; no direct sand-control content).

## Cross-references

- [Gravel Packing](gravel-packing.md), [Frac Packing](frac-packing.md), [Sand Control Screens](sand-control-screens.md)
- [Perforating](perforating.md), [Perforation Strategy](perforation-strategy.md), [Perforating — Shaped Charges](perforating-shaped-charges.md)
- [Electric Submersible Pumps](electric-submersible-pumps.md), [Progressing-Cavity Pumps](progressing-cavity-pumps.md), [PCP Heavy-Oil Application](pcp-heavy-oil-application.md)
- [ISO 17824](../standards/iso-17824.md), [API RP 19B](../standards/api-rp-19b.md)
- Drilling-engineering: [Casing Program Design](../../../drilling-engineering/wiki/concepts/casing-program-design.md)

## Public references

- **Penberthy, W. L. & Shaughnessy, C. M.** — *Sand Control* (SPE Monograph Series Vol. 1), Society of Petroleum Engineers, 1992 (ISBN 978-1-55563-041-6). The practitioner-canonical companion volume.
- **Saucier, R. J.** — "Considerations in Gravel Pack Design," JPT 26(2), February 1974. The foundational gravel-sizing-criterion paper; framework still in active operator use.
- **Stein, N., Odeh, A. S. & Jones, L. G.** — "Estimating Maximum Sand-Free Production Rates from Friable Sands for Different Well Completion Geometries," JPT 26(10), October 1974. Foundational sand-influx framework.
- **Bellarby, J.** — *Well Completion Design*, Developments in Petroleum Science Vol 56, Elsevier, 2009 (ISBN 978-0-444-53210-7). Comprehensive sand-control completion-design chapter.
- **Lyons, W. C. (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, Elsevier (ISBN 978-0-7506-7785-1). Sand-control chapter.
- **SPE OnePetro sand-control literature** — extensive corpus on screen design, gravel-pack execution, frac-pack design and post-installation performance evaluation.
- **ISO 17824 / 17825** — see [the standards page](../standards/iso-17824.md) for ISO 17824; ISO 17825 is the sister standard for cased-hole gravel-pack screens.
