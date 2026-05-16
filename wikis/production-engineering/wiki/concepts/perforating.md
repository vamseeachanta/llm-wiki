---
title: "Perforating"
tags: [perforating, completions, shaped-charge, gun-system, perforation-skin, ipr, well-completion]
sources:
  - api-rp-19b
added: 2026-05-15
last_updated: 2026-05-16
---

# Perforating

## Scope

Perforating is the operation that creates hydraulic communication between a cased wellbore and the producing formation. Shaped charges, mounted on a gun assembly and conveyed downhole, are detonated to drive metal jets through the casing wall, the cement sheath behind it, and a measurable distance into the surrounding rock. The resulting perforation tunnels are the **only** flow path into a cased completion; their geometry, density, phasing, and depth-of-penetration set a hard upper bound on the inflow performance of the well.

This page is the **router** for perforating coverage in the production-engineering wiki. It synthesises the operational decisions, the physics summary, the strategy framework, and the cross-domain interactions, and links out to dedicated pages for shaped-charge mechanics, perforation strategy, and gun-system selection.

## Why perforating is the highest-leverage Phase 2 topic

Perforation geometry interacts directly with every artificial-lift method covered in Phase 1:

- **Rod pump** — perforation density above the pump intake affects gas-separation efficiency at the pump.
- **ESP** — perforation depth and phasing control the IPR shape that ESP sizing is built on; see [Electric Submersible Pumps](electric-submersible-pumps.md).
- **Gas lift** — the IPR curve coupled to gas-lift design is sensitive to perforation skin; see [Gas Lift Overview](gas-lift-overview.md).
- **Plunger lift** — perforation policy in low-rate gas wells determines whether the well can be held in a stable cycle.
- **PCP** — heavy-oil perforation strategy interacts with sand production and elastomer wear.

Perforating also interacts with **well construction** decisions made upstream of completion: production-casing burst rating, cement-bond quality across the producing interval, and the casing-design factor margin all see perforation as an externally-imposed load case. See drilling-engineering [Casing Program Design](../../../drilling-engineering/wiki/concepts/casing-program-design.md).

## The four perforating-design questions

Any perforating job answers four operator questions, in roughly this order:

1. **Which gun system?** (TCP / wireline / coiled-tubing; expendable vs retrievable; charge family) — see [Perforating Gun Systems](perforating-gun-systems.md)
2. **Which charge?** (deep-penetrating vs big-hole; specific charge size and weight) — driven by completion type (cased flow vs gravel-pack vs frac-pack)
3. **What shot density and phasing?** — see [Perforation Strategy](perforation-strategy.md)
4. **Underbalanced, overbalanced, or extreme-overbalanced perforating?** — see [Perforation Strategy](perforation-strategy.md)

These four decisions are interlocked: a deep-penetrating charge in a 6 spf / 60° gun fired underbalanced produces a very different completion than a big-hole charge in a 12 spf / 0° gun fired overbalanced. The strategy page lays out the framework; this overview gives the system-level synthesis.

## Shaped-charge physics summary

A shaped charge is a precisely engineered explosive geometry that focuses detonation energy into a metallic jet. The configuration is conserved across vendors:

- A **case** (steel or zinc alloy) houses the charge.
- An **explosive load** (RDX, HMX, HNS, or HTX-class compositions for higher temperature tolerance) sits behind a precisely-shaped metallic **liner** (typically a conical, hemispherical, or composite-powder liner).
- A **primer cord** or **detonator** initiates the explosive.
- On detonation, the liner is driven inward, collapses on the central axis, and emerges as a coherent metallic jet travelling at several kilometres per second.

The jet — not the explosive blast itself — does the perforating work. It is the **kinetic energy density** of the jet tip, not the explosive yield, that controls penetration depth in rock. This is why charge design (liner geometry, liner material chemistry, stand-off distance) matters more than raw explosive mass.

See [Perforating Shaped Charges](perforating-shaped-charges.md) for the mechanism in depth.

## Performance metrics

A shaped charge's downhole performance is captured by four numbers:

| Metric | Symbol convention | What it controls |
|---|---|---|
| Penetration depth | EHL ("entry-hole-to-end length") or sometimes TPL ("total penetration length") | How far into the rock the perforation tunnel reaches; directly affects perforation-skin and damage-bypass |
| Entrance-hole diameter | EHD | Sets the flow area through the casing wall; first-order in big-hole / gravel-pack jobs |
| Shot density | spf (shots per foot) | Number of perforations per linear foot of gun |
| Phasing | degrees (e.g. 60°, 90°, 0°) | Angular distribution of shots around the wellbore axis |

**Key idea:** Deep-penetrating charges optimise EHL (small EHD, long tunnel) — used to bypass formation damage in natural-completion or matrix-stimulation jobs. Big-hole charges optimise EHD (short tunnel, large hole) — used where the casing-wall area itself is the throttle (gravel-pack, frac-pack, high-rate gas).

Vendor-quoted EHL and EHD numbers should be matched to the **API RP 19B test section** that produced them — surface flat-target numbers overstate downhole performance. See [API RP 19B](../standards/api-rp-19b.md).

## Perforation skin

Even a well-executed perforation introduces a localised flow restriction near the wellbore — the **perforation skin** — relative to the open-hole ideal. The classic Karakas–Tariq (1991) framework decomposes perforation skin into three additive components:

- **s_h** (horizontal pseudo-skin) — accounts for the change in 3D flow geometry from radial-open-hole to perforation-by-perforation entry.
- **s_v** (vertical-converging skin) — accounts for crowding of flowlines as fluid converges to each tunnel.
- **s_wb** (wellbore-blockage skin) — accounts for the presence of the unperforated casing as a flow obstacle.

Total perforation skin = s_h + s_v + s_wb, all functions of:

- Penetration length (longer → smaller s_v)
- Shot density (higher → smaller s_v and s_h)
- Phasing (better-distributed → smaller s_h)
- Tunnel diameter relative to wellbore diameter
- Anisotropy ratio k_v / k_h (vertical vs horizontal permeability)

In a damaged formation, the perforation can either **bypass** the damage (if penetration length > damage zone depth) or **multiply** it (if penetration ends inside the damage). This is why deep-penetrating charges are mandatory in formations with measured drilling-fluid invasion or filtercake skin.

See [Perforation Strategy](perforation-strategy.md) for the operator-facing skin-management framework.

## Underbalanced vs overbalanced

The **differential pressure** between wellbore and formation at the instant of detonation controls the post-perforation tunnel condition:

### Underbalanced (UBP)

- Wellbore pressure < formation pressure at detonation
- Surge flow from formation immediately after detonation flushes crushed-zone debris out of the tunnels
- Result: **clean tunnels**, minimal perforation skin (often s_total ~ 0 or slightly negative on idealised math)
- Practical constraint: the operator must control the surge to avoid blowing out the tubing-conveyed gun or unseating the packer
- Cannot be used when surface equipment cannot handle the immediate post-perforation surge (e.g. some pumpdown-bridge-plug operations)

### Overbalanced (OBP)

- Wellbore pressure > formation pressure at detonation
- Crushed-zone debris is forced **into** the rock immediately surrounding each tunnel
- Result: a **damaged crushed zone** rings each tunnel, contributing to elevated perforation skin
- Often unavoidable in operations where the wellbore must remain pressurised for well-control reasons (e.g. wireline gun runs against a kicked well)

### Extreme overbalanced (EOB) / dynamic-overbalance

- Wellbore pressure intentionally raised far above formation pressure immediately before detonation (often using nitrogen-charged accumulator or a gas-cushion)
- The high-pressure differential at detonation generates a transient fracture network at each tunnel tip
- Effectively a mini-stimulation co-incident with perforating
- Trade-off: requires more sophisticated surface and downhole equipment; the fracture network is uncontrolled in azimuth

The selection between these modes is part of [Perforation Strategy](perforation-strategy.md).

## Gun-system families

Perforating guns are categorised first by **conveyance method**:

| Family | Conveyance | When chosen |
|---|---|---|
| **TCP** — Tubing-Conveyed Perforating | Production tubing + packer | Long intervals, high-rate completions, simultaneous perforate-and-test; the workhorse of modern completions |
| **Wireline-conveyed** | Slickline or e-line | Short intervals, recompletion add-on perfs, low-cost workover scope |
| **Coiled-tubing-conveyed** | Coiled tubing with internal e-line | Highly deviated and horizontal wells where wireline gravity-conveyance fails |
| **Through-tubing** | E-line, gun small enough to pass through completion tubing | Recomplete a producing well without pulling tubing |

Secondary axes:

- **Expendable vs retrievable** — expendable guns drop debris into the wellbore (must be tolerated by downstream operations); retrievable guns leave clean wellbores at the cost of larger gun OD.
- **Big-bore vs slim** — sized to casing ID; phasing patterns scale with gun OD.
- **Charge family compatibility** — each gun OD class accommodates a finite envelope of charge sizes.

See [Perforating Gun Systems](perforating-gun-systems.md) for the in-depth selection framework.

## Decision framework — selecting a perforating system

A simplified operator decision tree:

1. **Well architecture first.** Is the producing interval vertical / deviated / horizontal? Open-hole or cased? This decides conveyance class.
2. **Completion type second.** Cased-flow producer? Gravel-pack? Frac-pack? This decides charge type (deep-penetrating vs big-hole) and shot-density floor.
3. **Damage profile third.** Is there measurable invasion / filtercake skin? Determines penetration-length target.
4. **Differential strategy fourth.** Underbalanced if surface and downhole equipment can tolerate it; otherwise overbalanced with the expectation of post-perforation cleanup via clean-fluid surge or matrix acid.
5. **Density-and-phasing last.** Highest spf the gun system supports if the productivity case justifies the cost; phasing matched to anisotropy (0° in highly-laminated bedded rock, 60° / 120° in isotropic sand).

## Vendor archetype framing

The perforating-services landscape is dominated by three integrated majors plus one independent specialist:

- **Halliburton** — Wellhead-to-bottom perforating services; broad portfolio across all gun-system families.
- **Schlumberger** — Comparable scope; historically strong in TCP and through-tubing portfolios.
- **Baker Hughes** — Comparable scope; portfolio includes specialty oriented-perforating systems.
- **Owen Oil Tools** — The largest independent perforating-specialist; supplies charges and gun hardware to operators who prefer not to bundle perforating with a fluids/cementing contract.

Other notable independents: **GEODynamics**, **DynaEnergetics**, **Hunting Titan**. Vendor proprietary algorithm details (jet-formation modelling, charge-design optimisation methods) are not reproduced in this wiki — see the **Hard constraints** note in the index for the vendor-confidentiality firewall.

## Cross-domain interactions

- **IPR shape** — Perforation skin enters the inflow-performance-relationship calculation directly. Re-perforation campaigns are a common response to under-performing wells; see [Gas Lift Overview](gas-lift-overview.md) for the IPR / artificial-lift coupling.
- **ESP intake placement** — Perforation density above the ESP intake controls gas-separation behaviour; see [Electric Submersible Pumps](electric-submersible-pumps.md).
- **Sand production** — Perforation strategy is the first sand-control intervention. Big-hole charges with low phasing density in unconsolidated sand are a known sand-influx trigger.
- **Casing burst rating** — Perforation policy interacts with the burst-design margin of the production casing; see [Casing Program Design](../../../drilling-engineering/wiki/concepts/casing-program-design.md).
- **Frac initiation** — Perforation phasing controls fracture-initiation azimuth in cased-hole frac jobs. Oriented (180° / 0°) phasing is standard for stimulation; isotropic phasing is standard for natural completion.

## Sand-control coupling — big-hole charge selection and shot-density floor for gravel-pack completions

Perforating into an unconsolidated sand interval that will be completed with a sand-control architecture imposes hard requirements on the perforating job that are different from natural-completion perforating:

- **Big-hole (BH) charges are mandatory** for cased-hole gravel-pack and frac-pack completions because the casing-wall area is the throttle for both gravel placement (during pack execution) and high-rate proppant slurry (during frac-pack pumping). Deep-penetrating charges that are correct for natural completion are wrong for these sand-control completions.
- **Shot-density floors are dictated by sand-control type** — gravel-pack completions require 12-18+ spf to give the gravel a uniform pack-and-flow geometry; frac-pack completions require 6-12 spf because the frac dominates near-wellbore flow but the gravel must still distribute around the wellbore; standalone screens are commonly fed by 8-12 spf perforations.
- **Phasing is isotropic (60° / 90°)** for sand-control completions because the gravel pack must distribute uniformly around the wellbore. Oriented (0° / 180°) phasing is reserved for cased-hole frac-only completions and is wrong for any sand-control architecture.
- **Underbalanced perforating yields cleaner tunnels** for subsequent gravel-pack execution because crushed-zone debris is flushed *out* of the tunnels rather than packed *in*. UBP is preferred where surface equipment supports it, since the post-perforation gravel-pack execution then has clean tunnels to fill.

The sand-control framework lives in a dedicated cluster: see [Sand Control](sand-control.md) for the architecture catalogue and decision framework, [Gravel Packing](gravel-packing.md) for the Saucier-criterion gravel-sizing logic and pack-placement methodology, and [Frac Packing](frac-packing.md) for the tip-screen-out hybrid completion design.

## Multi-zone completion coupling — selective-production perforation strategy

In multi-zone selective completions (see [Multi-Zone Completions](multi-zone-completions.md)), perforation policy must be tuned **per zone**, not averaged across the wellbore. Distinct considerations:

- **Per-zone charge selection** — each zone's reservoir conditions (permeability, damage profile, fluid type) drive its own deep-penetrating vs big-hole choice; a single completion may carry deep-penetrating charges in one zone and big-hole charges in another.
- **Per-zone density and phasing** — shot density and phasing should be matched to each zone's anisotropy and intended flow path, not set uniformly.
- **Underbalanced perforating discipline** — selective completions complicate UBP planning because the surge-flow comes from the perforated zone only; surface-equipment sizing must account for which zone(s) are isolated open at the time of detonation.
- **Zonal-isolation hardware coupling** — the perforation interval must align with the zone defined by the upper and lower isolation packers; perforating across a packer location creates communication paths that defeat the selective architecture.
- **Smart-completion overlay** — when ICVs are installed (see [Intelligent-Well Completions](intelligent-well-completions.md)), per-zone perforation policy can be designed for the specific reservoir-management strategies the ICVs will support.

Cross-link: see [Multi-Zone Completions](multi-zone-completions.md) for the architectural overview and [Selective Production](selective-production.md) for the zonal-isolation hardware framework.

## Matrix-acid stimulation coupling — perforation strategy affects acid placement and tunnel-bypass effectiveness

Perforating policy and matrix-acid stimulation are tightly coupled because the acid must travel through the perforation tunnels to reach the formation matrix where damage-bypass dissolution takes place. The coupling runs in both directions:

- **Perforation EHL controls the starting position of the acid front.** Deep-penetrating (DP) charges place the acid at the tunnel tip — already past most or all of the drilling-fluid invasion damage. Big-hole (BH) charges leave the acid front close to the casing wall and force the acid to chew through the damage zone before reaching fresh rock. For matrix-acid jobs targeting damage-bypass stimulation, DP charges are preferred whenever the completion type allows.
- **Overbalanced perforating produces a crushed-zone damage ring** around each tunnel that contributes 5-30 elevated perforation-skin units. The standard cleanup for overbalanced-perforated wells is a matrix-acid job — sandstone-acid for sandstone formations (HCl preflush + HCl/HF mud-acid main treatment + postflush), or HCl for carbonate formations. The expected post-perforation matrix-acid cleanup is part of the perforation-strategy decision: when underbalanced perforating is infeasible, the operator plans the cleanup acid job as part of the completion program rather than treating it as a remedial intervention.
- **Shot density and phasing affect acid placement uniformity.** Higher shot density and isotropic (60° / 90°) phasing distribute acid more uniformly around the wellbore, reducing the diversion burden for the matrix-acid job. Low shot density and oriented phasing (designed for cased-hole frac initiation rather than for matrix-acid placement) concentrate acid flow through a few perforations and increase diversion-failure risk.
- **Perforation crushed-zone debris does not always need acid.** Underbalanced perforating (UBP) flushes crushed-zone debris out of the tunnels during the post-detonation surge, often producing tunnels clean enough that no matrix-acid cleanup is required. Operators planning UBP can sometimes defer or eliminate the post-completion matrix-acid stage entirely.

See [Matrix Acid Stimulation](matrix-acid-stimulation.md) for the chemistry-family framework and the candidate-selection logic. The sandstone-and-carbonate-specific treatment design lives at [Sandstone Acidizing](sandstone-acidizing.md) and [Carbonate Acidizing](carbonate-acidizing.md). The diversion problem — which is amplified by perforation-cluster geometry — is at [Matrix Acid Diversion](matrix-acid-diversion.md).

## Hydraulic fracturing coupling — oriented perforating + cluster spacing

Cased-hole hydraulic-fracturing completions impose perforation-policy requirements that are largely orthogonal to (and partly in tension with) the policies optimal for natural completion, sand-control, and multi-zone selective completions:

- **Oriented phasing (0° / 180°) is standard for cased-hole frac initiation** — perforations must align with the maximum in-situ horizontal stress so that fractures initiate in a coherent plane. Isotropic phasing (60° / 90°) optimal for natural completion or sand-control produces tortuous near-wellbore frac geometry with high screen-out risk, treating-pressure spikes, and restricted near-wellbore conductivity. The Phase 3 [Hydraulic Fracturing](hydraulic-fracturing.md) router covers the frac-mechanics that drives this orientation requirement.
- **Cluster spacing controls per-cluster fracture-initiation distribution in multi-stage horizontal wells** — modern unconventional-play multi-stage fracs initiate multiple clusters per stage; cluster spacing (typical 20-60 ft) and the within-cluster perforation density together control how uniformly the treating fluid initiates fractures across the stage. Stress-shadow effects between adjacent clusters can suppress some clusters from initiating at all if the design is wrong.
- **Charge selection for frac initiation** — deep-penetrating (DP) charges are typical for low-permeability shale fracs (to bypass formation damage and reach the in-situ stress field cleanly); big-hole (BH) charges are used in some high-rate gas frac jobs where the casing-wall area becomes a flow-rate throttle during the slurry stages.
- **Density floor for frac jobs** — 4-8 spf is typical for cased-hole frac jobs because the frac dominates near-wellbore productivity once initiated; per-cluster density in a multi-cluster stage may be higher to drive uniform initiation across the cluster.
- **Frac-pack distinction** — frac-pack completions (see [Frac Packing](frac-packing.md)) require both isotropic phasing (for the gravel-pack distribution function) AND big-hole charges (for the proppant-slurry flow function), with 6-12 spf density. This is a distinct policy from standalone-frac initiation; the frac-pack policy is set by the sand-control function, not by the frac-initiation function.

Cross-link: see [Hydraulic Fracturing](hydraulic-fracturing.md) for the Phase 3 stimulation router, [Frac Design](frac-design.md) for the pump-schedule architecture that the perforation-initiation policy enables, and [Perforation Strategy](perforation-strategy.md) for the operator-facing perforation-design framework.

## Re-perforation in refrac jobs

Refrac jobs ([Refrac](refrac.md)) require new perforations placed independently of the legacy completion's perforation set, because the new fracture must initiate at depths and orientations chosen by the refrac designer rather than at the path-of-least-resistance defined by the legacy perforations and the legacy fracture network. Re-perforation policy for refrac differs from initial-completion perforation policy in several respects:

- **Re-perforation depth and orientation are dictated by the recompletion architecture.** In a cement-and-perf refrac, the legacy perforations are squeeze-cemented closed and new perforations are shot at the refrac-designer's chosen depths and orientations in the squeeze cement. In a mechanical-isolation refrac, perforations are shot into the new isolated stages defined by bridge plugs or sliding-sleeve liner. In an expandable-liner refrac, perforations are shot through the new liner into the cement annulus and across into the formation.
- **Charge selection accommodates the cement-and-casing flow path.** Cement-and-perf refrac jobs require charges that penetrate squeeze cement (typically several inches of fresh cement) plus the legacy cement sheath plus the casing wall before reaching formation; deep-penetrating (DP) charges are typical. Expandable-liner refrac jobs require charges that penetrate the new liner wall plus the annular cement plus the legacy cement plus the legacy casing wall plus the original cement plus the formation; charge sizing must account for the multiple barrier layers.
- **Phasing must align with the present-day stress field.** Refrac DFIT diagnostics ([Diagnostic Fracture Injection Test](diagnostic-fracture-injection-test.md)) often reveal that depletion has re-oriented the in-situ minimum-horizontal-stress relative to the original-completion stress state. Re-perforation phasing must align with the present-day stress field, not the original-completion stress field; isotropic phasing (60° / 90°) is sometimes selected for refracs in highly re-oriented stress fields where the new initiation direction is uncertain.
- **Cluster spacing reflects modern frac-design practice.** Many vintage refrac candidates (typically 2008-2014 horizontal-well multi-stage fracs) were originally completed with cluster spacing that is now understood to leave un-stimulated rock between clusters. Refrac re-perforation typically uses tighter cluster spacing than the original completion to access the un-contacted rock.

Cross-link: see [Refrac](refrac.md) for the refrac decisioning router, [Diagnostic Fracture Injection Test](diagnostic-fracture-injection-test.md) for the DFIT diagnostic that drives refrac phasing decisions, and [Production History Decline Analysis](production-history-decline-analysis.md) for the candidate-selection methodology.

## Standards anchor

- [API RP 19B — Evaluation of Well Perforators](../standards/api-rp-19b.md) — the practitioner-canonical test methodology
- API Spec 16A — BOP equipment, applicable to HPHT perforating operations (adjacent)
- NACE MR0175 / ISO 15156 — sour-service material requirements applicable to perforating tools (adjacent)

## Cross-references

- [Perforating Shaped Charges](perforating-shaped-charges.md), [Perforation Strategy](perforation-strategy.md), [Perforating Gun Systems](perforating-gun-systems.md)
- [API RP 19B](../standards/api-rp-19b.md)
- [Electric Submersible Pumps](electric-submersible-pumps.md), [Gas Lift Overview](gas-lift-overview.md)
- Drilling-engineering: [Casing Program Design](../../../drilling-engineering/wiki/concepts/casing-program-design.md)

## Public references

- **Bell, W. T. & Behrmann, L. A.** — *Perforating Applications in the Petroleum Industry* (SPE Reprint Series). Practitioner-canonical companion to RP 19B.
- **Behrmann, L. A.** — multiple SPE papers on shaped-charge performance evaluation methodology.
- **Karakas, M. & Tariq, S.** — "Semianalytical Productivity Models for Perforated Completions," SPE Production Engineering 6(1), 1991 — the foundational perforation-skin decomposition framework.
- **McLeod, H. O.** — "The Effect of Perforating Conditions on Well Performance," JPT 35(1), 1983 — earlier perforation-skin and underbalanced-perforating framework.
- **Locke, S.** — "An Advanced Method for Predicting the Productivity Ratio of a Perforated Well," JPT 33(12), 1981 — productivity-ratio framework still in operator use.
- **SPE OnePetro perforating literature** — extensive corpus on charge-design / penetration / skin / EOB methodology.
- **Lyons, W. C. (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, Elsevier (ISBN 978-0-7506-7785-1) — perforating chapter.
