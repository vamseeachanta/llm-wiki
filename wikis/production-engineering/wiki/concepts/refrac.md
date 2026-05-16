---
title: "Refrac (Re-Fracturing)"
tags: [refrac, re-fracturing, recompletion, hydraulic-fracturing, candidate-selection, stimulation, asset-management, decision-framework, cement-and-perf, mechanical-isolation, expandable-liner]
added: 2026-05-16
last_updated: 2026-05-16
---

# Refrac (Re-Fracturing)

## Scope

Refrac is the deliberate re-stimulation of a previously hydraulically-fractured well, with the goal of restoring or improving deliverability after the original fracture network has degraded. The original fractures may have lost conductivity through proppant crushing, embedment, or fines plugging; the original stimulated rock volume may have been substantially under-stimulated by then-current technology relative to what current technology can place; or the depletion-induced stress field may have re-oriented in a way that allows a re-frac to access reservoir volume the original treatment missed.

Refrac is **hydraulic fracturing applied to a well with a stimulation history**, and the mechanics of fracture initiation, propagation, and proppant transport remain those covered in [Hydraulic Fracturing](hydraulic-fracturing.md). What distinguishes refrac as a topic is the **asset-management decision layer that sits in front of the frac job**: refrac vs new-well economics, candidate-well selection methodology, recompletion-architecture choice, and the diagnostic workflow that determines whether a particular well is in fact a refrac candidate.

This page is the **router** for refrac coverage in the production-engineering wiki. It synthesises the refrac-vs-new-well economic frame, the candidate-selection methodology, the three recompletion-architecture families (cement-and-perf, mechanical isolation, expandable liner), and the cross-domain interactions, and links out to dedicated pages for [Diagnostic Fracture Injection Test](diagnostic-fracture-injection-test.md) and [Production History Decline Analysis](production-history-decline-analysis.md).

## Why refrac is the closing-out Phase 3 topic

Refrac is the natural closing topic of the stimulation phase because it is the topic where stimulation engineering, completion engineering, reservoir engineering, and asset-management economics converge:

- **Stimulation-engineering coupling** — the refrac itself is a hydraulic-fracturing job; design choices around fluid, proppant, pump schedule, and geometry come straight from the [Hydraulic Fracturing](hydraulic-fracturing.md) framework, with adjustments for the pre-existing wellbore geometry, the depleted in-situ stress state, and the legacy completion hardware.
- **Completion-engineering coupling** — the recompletion architecture (cement-and-perf, mechanical isolation, expandable liner) is a major completion-design problem in its own right, distinct from the frac-design problem and frequently dominating the project cost.
- **Reservoir-engineering coupling** — refrac candidate selection rests on understanding the depletion state of the original stimulated rock volume, the in-situ stress evolution since the original treatment, and the remaining-recoverable estimate. These are reservoir-engineering quantities that production-engineering decisions consume.
- **Asset-management economics** — the dominant decision in refrac is not "how do we design the job" but rather "is this well a refrac candidate at all, and is refrac the right capital allocation versus drilling a new well or accepting the natural-decline outcome?" This is an economics decision that operates above the engineering decisions.

## The refrac-vs-new-well economic frame

The first question on every refrac evaluation is whether the candidate well's expected post-refrac uplift justifies refrac capital relative to the alternative of drilling a new offsetting well. The economic frame compares three options:

| Option | Capital | Time to first oil | Production profile | Risk |
|---|---|---|---|---|
| **Refrac the existing well** | Lowest (no new drilling, existing wellbore re-used) | Shortest (weeks, not months) | Recovery of declined rate plus contacted-rock-volume uplift | Frac job may fail to initiate, may communicate with offset wells, may produce minimal uplift |
| **Drill a new offsetting well** | Highest (drilling cost dominates) | Longest (months to drill + complete + tie in) | Full new-well IP-rate-and-decline curve from previously-undrained rock | Drilling risk, completion risk, lower per-foot cost if multiple wells share a pad |
| **Accept natural decline** | Zero | Immediate | Continued exponential or hyperbolic decline per the established decline curve | Zero upside; production trends to abandonment |

Refrac is favoured economically when:

- **The original completion under-stimulated the available rock volume** — many vintage horizontal-well multi-stage fracs in the early shale-development era (typically 2008-2014) used cluster spacing, stage spacing, fluid volumes, and proppant volumes that are now understood to have left significant un-stimulated rock between stages. Re-fracturing with modern tight-cluster-spacing geometry can access this volume.
- **The well's original frac geometry has lost conductivity but the surrounding rock is undepleted** — proppant crush, fines plugging, and proppant embedment all reduce conductivity over time; if the surrounding rock has not been drained, re-fracturing restores deliverability.
- **The drilling cost of a new offset well is prohibitive** — refrac becomes more attractive as new-well drilling cost rises relative to refrac cost. Onshore unconventional plays where new-well drilling is relatively cheap have a different refrac-vs-new-well break-even than offshore or remote-onshore plays.
- **The lease economics demand near-term production** — refrac brings production weeks-to-months sooner than a new well. Lease-retention drilling obligations, joint-venture cash-call constraints, and short-tenor production-sharing-agreement obligations can favour refrac over new-drill purely on a time-to-production basis.

Refrac is **dis-favoured** when:

- **The well has produced most of the recoverable rock volume already** — refrac on a depleted well delivers minimal uplift because the rock the new frac contacts is already drained.
- **The original wellbore has integrity problems** — casing collapse, cement-bond failure, parted tubing, or fish-in-hole make the refrac job a fish-and-repair operation before any stimulation can begin; the all-in cost can approach a new-well cost without the new-well-rock-volume upside.
- **Offset-well frac communication risk is high** — close-spaced infill drilling around the candidate well creates risk that the refrac will frac into a producing offset well, damaging the offset's productivity and triggering inter-operator dispute.
- **The well is in a play where refrac field-data is poor** — refrac economics depend on a credible estimate of post-refrac uplift; in plays where the operator does not have a track record of refrac field-results, the estimated uplift carries large uncertainty and the economic decision is correspondingly risky.

## Candidate-selection methodology

The refrac candidate-selection workflow rests on three diagnostic legs:

### Leg 1: Production-history decline analysis

The first diagnostic is whether the well's production history is consistent with a refrac-treatable condition. The candidate-selection production-history analysis answers:

- **Is the decline steeper than offset wells of the same vintage?** A well declining steeper than its cohort suggests either a fundamentally smaller stimulated rock volume than its peers or accelerated conductivity loss. Both conditions are addressable by refrac.
- **Has the well bypassed the typical end-of-transient-flow inflection?** Wells that transition from steep early decline to a flatter boundary-dominated decline are operating against drained rock volume; refrac uplift will be limited. Wells that continue in steep transient-flow decline have un-contacted rock and refrac uplift can be substantial.
- **What does the Arps b-factor (the hyperbolic-decline shape parameter) tell us?** High b-factor (b > 1 in transient flow, b > 0.5 in boundary-dominated flow) suggests low-permeability rock where conductivity loss dominates decline; refrac that restores conductivity has high uplift. Low b-factor (b near 0, exponential decline) suggests rock-volume depletion dominates decline; refrac uplift is limited.

The decline-analysis methodology and its underlying Arps and Fetkovich frameworks are covered in detail at [Production History Decline Analysis](production-history-decline-analysis.md).

### Leg 2: Diagnostic Fracture Injection Test (DFIT)

The second diagnostic is whether the depleted in-situ stress state will accept a new fracture in a usable orientation. The DFIT — also known as the pre-frac mini-frac test — pumps a small volume of clean fluid into the formation at low rate, then monitors the pressure decline after shut-in to characterise:

- **Closure pressure** — the in-situ minimum-horizontal-stress at refrac time, which controls fracture initiation pressure and propped-pack stress
- **ISIP (instantaneous shut-in pressure)** — the pressure at the instant pumping stops, used to bound the closure-pressure estimate
- **Leak-off coefficient** — fluid loss per unit fracture-face area per unit square-root of time, which controls how much pad volume is required to grow a fracture
- **Stress orientation** (where instrumented) — the present-day maximum-horizontal-stress azimuth, which controls the orientation of any new fractures

Depletion of the original stimulated rock volume reduces the in-situ pore pressure, which can re-orient the local stress field. A refrac DFIT often reveals that the present-day minimum-horizontal-stress is at a different orientation than the original frac was designed against. The refrac design must accommodate this re-orientation, which is one reason a refrac DFIT is treated as mandatory rather than optional in modern practice.

The DFIT methodology — pre-frac procedure, pressure-derivative analysis, common pitfalls, and the literature consensus on closure-pressure interpretation — is covered in detail at [Diagnostic Fracture Injection Test](diagnostic-fracture-injection-test.md).

### Leg 3: Wellbore-integrity inspection

The third diagnostic is whether the existing wellbore can support a frac job. Refrac jobs impose loads on the production casing, the tubing, the wellhead, and the cement sheath that are comparable to or higher than the original frac loads, and the legacy hardware has had years of corrosion and cycling exposure since installation. The inspection typically includes:

- **Cement-bond log (CBL) and ultrasonic imaging tool (USIT) survey** to characterise the present-day cement-sheath integrity, particularly the bond between casing and cement and any micro-annulus that frac pressure could open
- **Multi-finger caliper survey** to characterise the inside-diameter profile of the casing and detect any wall-thickness reduction from corrosion
- **Pressure-test of the casing and wellhead** at planned refrac treating pressure plus margin
- **Tubing integrity log and packer-set verification** if the refrac will be pumped through tubing rather than down the casing

The recompletion architecture chosen for the refrac depends directly on what this inspection finds: a well with intact cement and clean casing can use cement-and-perf; a well with marginal cement bond or marginal casing condition needs mechanical isolation; a well with worse casing condition needs expandable liner. The three architectures are described next.

## The three recompletion architectures

Refrac requires that the new fracture initiate at the operator's chosen depth and orientation, not at the path-of-least-resistance defined by the legacy perforations and the legacy frac. The recompletion architecture is the engineering solution to "how do we force the new frac to initiate where we want, given that the old wellbore has old perforations and old fractures in it." Three architecture families are in industry use:

### Architecture 1: Cement-and-perf

The simplest and lowest-cost refrac architecture. The legacy wellbore is squeeze-cemented through and across the legacy perforations to isolate them mechanically, then new perforations are shot in the cement at the chosen depths and orientations. The new frac initiates at the new perforations.

**When it applies:**
- The legacy cement-sheath bond is intact and the squeeze cement can be reliably placed
- The legacy perforations are clustered (typical vintage 4-8 spf clusters, easy to squeeze)
- The casing is in good condition and can accept new perforations and frac treating pressure
- The refrac design does not require radically different cluster spacing than the legacy completion

**Strengths:** lowest cost; shortest schedule; least disruption to the legacy wellbore.

**Weaknesses:** squeeze cement may not isolate the legacy perforations reliably (squeeze-cement quality is hard to verify); the legacy frac network may still steal fluid during the refrac if pressure communication is not fully eliminated; works only on legacy completions with manageable perforation density.

### Architecture 2: Mechanical isolation

The legacy wellbore is mechanically isolated using one of:

- **Solid-body bridge plugs** placed below each legacy frac stage to isolate it from the wellbore
- **Inflatable or composite plugs** set at chosen depths to define new frac stages
- **Sliding-sleeve isolation systems** run on a small liner inside the existing casing, providing a fresh casing surface for new perforations and frac initiation

**When it applies:**
- The legacy cement sheath is not fully reliable for squeeze cementing (cement-and-perf is too risky)
- The casing condition is acceptable but the operator wants a stronger isolation barrier than squeeze cement
- The refrac design requires significantly tighter cluster spacing than the legacy completion (the mechanical isolation hardware enables clean new-stage definition)
- The legacy perforations are too dense or too unevenly distributed to squeeze reliably

**Strengths:** more reliable isolation than cement-and-perf; allows redesign of stage and cluster spacing; well-suited to long-horizontal multi-stage refracs.

**Weaknesses:** higher cost than cement-and-perf; mechanical-isolation hardware adds run-time and a risk of stuck-plug or stuck-tool fish; reduces the available wellbore ID for subsequent intervention.

### Architecture 3: Expandable liner

A small-diameter liner (typically expandable steel) is run inside the existing casing across the refrac interval, sealed to the casing at top and bottom, and then expanded to a larger ID. The new liner provides a fresh inside-surface for new perforations and frac initiation; the annulus between the new liner and the old casing isolates the legacy perforations from the refrac.

**When it applies:**
- The casing condition is too marginal to support new perforations and frac pressure (corrosion, wall-thickness reduction, micro-fractures, deformations)
- The cement sheath is unreliable and squeeze cementing is unlikely to succeed
- The refrac job is high-value enough to justify the cost of the expandable-liner hardware
- The well's ID and trajectory allow expandable-liner deployment

**Strengths:** strongest isolation of the three architectures; gives the refrac job a fresh casing surface independent of the legacy hardware condition; allows aggressive redesign of cluster spacing and frac geometry.

**Weaknesses:** highest cost of the three architectures; operationally complex (expandable-liner deployment carries non-trivial fishing-and-stuck-tool risk); reduces the available wellbore ID by the liner wall thickness plus annular clearance, constraining future intervention.

The architecture choice is driven by the wellbore-integrity inspection results, the legacy-frac geometry and the desired refrac geometry, and the per-architecture cost-vs-risk trade-off. A typical operator workflow defaults to cement-and-perf where wellbore integrity supports it, mechanical isolation where cement-and-perf cannot guarantee isolation, and expandable liner only on high-value candidates where the other architectures cannot meet the integrity requirement.

## Decision framework — selecting a refrac approach

A simplified operator decision tree:

1. **Production-history check first.** [Production History Decline Analysis](production-history-decline-analysis.md) — if the well's b-factor and decline shape suggest depletion has consumed most of the recoverable rock, do not refrac. If the decline-analysis result supports refrac, proceed.
2. **DFIT diagnostic second.** [Diagnostic Fracture Injection Test](diagnostic-fracture-injection-test.md) — if the present-day closure pressure and stress orientation support a usable refrac geometry, proceed. If not, the refrac will produce a poorly-oriented or operationally-unsafe fracture and should be deferred.
3. **Wellbore-integrity inspection third.** If the casing and cement-sheath are intact, consider cement-and-perf. If the cement bond is marginal, consider mechanical isolation. If the casing condition is marginal, consider expandable liner.
4. **Refrac-vs-new-well economic check fourth.** Compare the expected uplift from the chosen refrac architecture against the all-in cost of drilling a new offsetting well to the same target. Refrac is favoured when the expected uplift covers refrac cost with significant cushion and when offset-well risk (drilling cost, time-to-production, lease-retention obligations) tilts away from new-drill.
5. **Frac design last.** Apply the [Hydraulic Fracturing](hydraulic-fracturing.md) framework — fluid, proppant, pump schedule, geometry — adjusted for the depleted in-situ stress state, the chosen recompletion architecture, and the legacy wellbore geometry.

## Vendor archetype framing

Refrac services are delivered by the integrated majors and several independent stimulation specialists. Vendor archetypes are named at concept level only; no proprietary refrac chemistry, no proprietary diversion algorithms, no proprietary recompletion-hardware designs, and no field-case treatment recipes are reproduced in this wiki.

- **Halliburton refrac services** — comprehensive refrac-service portfolio covering all three recompletion architectures (cement-and-perf, mechanical isolation, expandable liner).
- **Schlumberger refrac services** — comparable scope; historically strong in expandable-liner refrac systems.
- **Baker Hughes refrac services** — comparable scope; portfolio includes proprietary diversion-additive systems for refrac applications.

Vendor proprietary algorithm details (refrac candidate-selection software, refrac diversion-chemistry recipes, proprietary expandable-liner metallurgy) are not reproduced in this wiki. Operators evaluating refrac vendors should consult vendor data sheets and the public-literature anchors below.

## Cross-domain interactions

- **Hydraulic fracturing** — refrac is hydraulic fracturing applied to a previously-stimulated well; the design framework is the same plus adjustments for depleted stress state and legacy completion. See [Hydraulic Fracturing](hydraulic-fracturing.md), [Frac Fluids](frac-fluids.md), [Proppants](proppants.md), [Frac Design](frac-design.md).
- **Perforating** — refrac architectures rely on new perforations (cement-and-perf, expandable-liner) or new flow ports (mechanical isolation) to initiate the new fracture; perforation strategy for refrac differs from initial-completion perforation strategy. See [Perforating](perforating.md), [Perforation Strategy](perforation-strategy.md).
- **Matrix acid stimulation** — refrac wells with sandstone-acid-treatable post-stimulation damage sometimes benefit from a matrix-acid stage in advance of or following the refrac; the candidate-selection logic for matrix acid still applies. See [Matrix Acid Stimulation](matrix-acid-stimulation.md).
- **Casing-program coupling** — refrac treating pressure plus burst margin is a load case the original casing design may or may not have accommodated; wellbore-integrity inspection (caliper, CBL, pressure test) is mandatory before any refrac. See [Casing Program Design](../../../drilling-engineering/wiki/concepts/casing-program-design.md).
- **Reservoir-engineering coupling** — refrac economics depend on a credible remaining-recoverable estimate, which is a reservoir-engineering output that production engineering consumes. The decline-analysis methodology at [Production History Decline Analysis](production-history-decline-analysis.md) sits at the production-engineering / reservoir-engineering interface.

## Standards anchor

Refrac does **not** have a dedicated API recommended-practice anchor. The closest standards-derived references are:

- **API RP 39** — covers frac-fluid viscosity testing methodology applicable to refrac fluids; see [API RP 39](../standards/api-rp-39.md).
- **NACE MR0175 / ISO 15156** — sour-service material requirements applicable to refrac equipment and any new expandable-liner hardware in sour service.
- **SPE Monograph 17** (*Reservoir Stimulation*, 3rd ed., Economides & Nolte 2000) — the de-facto practitioner-canonical reference; the refrac chapter and the DFIT chapter are the closest things to industry-canonical methodology.

Refrac practice is therefore primarily anchored to **textbook and SPE-paper consensus** rather than to a standards-published procedure, similar in this regard to matrix-acid stimulation (see [Matrix Acid Stimulation](matrix-acid-stimulation.md)).

## Refrac candidacy depends on cumulative integrity-state degradation

Refrac candidate-selection workflows treat **wellbore-integrity inspection as leg 3** of the three-leg diagnostic process (alongside production-history decline analysis and DFIT, see above). The cumulative operating-time integrity-state of the candidate well determines both *whether* a refrac is feasible at all and *which* of the three recompletion architectures (cement-and-perf / mechanical isolation / expandable liner) is appropriate.

The operating-time integrity-state that the refrac decisioning consumes comes directly from the well-integrity-during-production discipline:

- **Production-tubing wall-thickness condition** — UT, ECT, and multi-finger-caliper survey data accumulated through the producing life characterises the tubing's ability to withstand refrac treating pressure plus burst margin. Heavily-corroded tubing requires either replacement (adding tubing-string-replacement cost to the refrac job scope) or cannot accept the refrac at all.
- **Production-casing wall-thickness condition** — same diagnostic family for the casing; refrac treating pressure can exceed the original frac treating pressure when modern higher-rate frac designs are applied, and corroded casing may not have the burst-margin headroom to accept the modern refrac design.
- **Cement-sheath condition** — periodic CBL / VDL / ultrasonic-imaging-tool re-survey through the producing life produces the operating-time cement-condition data that determines whether cement-and-perf is feasible (sound cement supports squeeze-cementing isolation) or whether the operator must escalate to mechanical isolation or expandable-liner architecture.
- **Sustained casing pressure (SCP) history** — APB and SCP-monitoring history is a strong indicator of cement-sheath integrity; wells with SCP history typically require mechanical isolation or expandable liner rather than cement-and-perf.
- **Sand-control-completion integrity** — wells with sand-control completions face additional refrac complexity because the refrac job must either accommodate the existing sand-control completion (which constrains refrac geometry and proppant placement) or include sand-control-completion replacement (which dramatically expands job scope).
- **Cumulative corrosion-management-program performance** — the operating-time corrosion-monitoring record (coupon data, inhibitor-residual analysis, observed-rate trending) characterises the corrosion-control success of the well's operating history; wells with poor corrosion-management track records have higher uncertainty in their wellbore-integrity baseline and warrant tighter pre-refrac inspection.

The wellbore-integrity inspection that initiates the refrac decisioning workflow (caliper / CBL / pressure-test / tubing-integrity logging, see Leg 3 above) is therefore a focused intensification of the operating-time integrity-monitoring program rather than a standalone diagnostic; the operating-time data accumulated through years of producing-life monitoring is part of the input to the refrac decisioning, and the focused pre-refrac inspection extends and confirms the cumulative picture.

For the operating-time well-integrity discipline that feeds refrac candidate-selection, see [Well Integrity During Production](well-integrity-during-production.md), [Integrity Monitoring](integrity-monitoring.md), [Corrosion Management](corrosion-management.md), and [Intervention Triggers](intervention-triggers.md).

## Cross-references

- [Diagnostic Fracture Injection Test](diagnostic-fracture-injection-test.md) — DFIT methodology, pre-frac procedure, closure-pressure / ISIP / leak-off interpretation
- [Production History Decline Analysis](production-history-decline-analysis.md) — Arps, Fetkovich, b-factor framework for refrac candidate selection
- [Hydraulic Fracturing](hydraulic-fracturing.md) — the underlying frac-mechanics framework
- [Frac Fluids](frac-fluids.md), [Proppants](proppants.md), [Frac Design](frac-design.md) — refrac fluid, proppant, design references
- [Perforating](perforating.md), [Perforation Strategy](perforation-strategy.md) — re-perforation hardware and strategy
- [Matrix Acid Stimulation](matrix-acid-stimulation.md) — adjunct matrix-acid stage in some refrac workflows
- [API RP 39](../standards/api-rp-39.md) — frac-fluid viscosity testing methodology
- Drilling-engineering: [Casing Program Design](../../../drilling-engineering/wiki/concepts/casing-program-design.md) — casing-burst margin and wellbore-integrity considerations

## Public references

- **Economides, M. J. & Nolte, K. G. (eds.)** — *Reservoir Stimulation*, 3rd Edition (SPE Monograph 17), Wiley 2000, ISBN 978-0-471-49192-7. The canonical industry reference; refrac chapter and DFIT methodology chapter are practitioner-standard.
- **Cipolla, C. L. et al.** — SPE 119366 and the broader Cipolla SPE OnePetro corpus on refrac candidate selection and field cases in shale plays.
- **Lyons, W. C. (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, Elsevier (ISBN 978-0-7506-7785-1). Stimulation chapters cover refrac at practitioner level.
- **SPE OnePetro refrac literature** — extensive corpus on refrac candidate-selection methodology, recompletion-architecture choice, field-case uplift documentation, and lessons-learned across major unconventional plays (Bakken, Eagle Ford, Marcellus, Permian Basin, Haynesville).
- **Barree, R. D. et al.** — SPE 167165 and SPE 124292; the Barree DFIT-methodology papers establish the pressure-derivative-based DFIT interpretation framework that refrac candidate-selection workflows rely on. See [Diagnostic Fracture Injection Test](diagnostic-fracture-injection-test.md).
- **Arps, J. J.** — "Analysis of Decline Curves," Trans. AIME 160(1), 1945. Foundational decline-curve framework; the b-factor diagnostic for refrac candidate-selection traces to this paper. See [Production History Decline Analysis](production-history-decline-analysis.md).
- **Fetkovich, M. J.** — "Decline Curve Analysis Using Type Curves," JPT 32(6), 1980. Modern type-curve-matching decline-analysis methodology; refrac candidate-selection workflows use this framework when transient-vs-boundary-dominated-flow discrimination matters.
