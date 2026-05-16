---
title: "Casing Program Design"
tags: [casing, well-design, collapse-design, burst-design, tension-design, triaxial, biaxial, lubinski]
sources:
  - api-spec-5ct
  - api-rp-5c5
  - api-rp-5c1
added: 2026-05-13
last_updated: 2026-05-16
---

# Casing Program Design

## Scope

Engineering design of the casing program for a well — selecting the number of casing strings (conductor → surface → intermediate → production → liner), the setting depth of each, the grade, weight, and connection of each string, and verifying that each string meets the four design-load criteria (collapse, burst, tension, triaxial) with adequate design factors. This is the load-bearing well-design concept that ties casing-spec inputs to safety-of-well outputs.

## Casing-string sequence

- **Conductor** — typically 30" or 36", driven or jetted; isolates surface unconsolidated formations.
- **Surface** — typically 13⅜" or 20"; isolates shallow freshwater aquifers, anchors BOP stack.
- **Intermediate** — one or more strings (e.g., 9⅝", 11¾"); isolates problem formations (lost-circulation zones, sloughing shales, salt sections).
- **Production** — typically 7" or 5½"; isolates the producing zone, hosts the production tubing.
- **Liner** — partial-length casing run from the previous shoe to TD; alternative to a full production string.

## Four design loads

1. **Collapse** — external pressure tries to crush the casing inward. Worst case typically during lost-circulation event where mud column drops below the casing-shoe pressure.
2. **Burst** — internal pressure tries to split the casing outward. Worst case during well-control kick scenarios with full reservoir gas to surface (gas-to-surface or BHP-1-EPP design).
3. **Tension** — weight of the casing string in air + buoyant weight + setting overpull + cementing differential pressure forces.
4. **Triaxial (von Mises)** — combined-load envelope. Casing in a triaxial state can fail at loads below individual collapse / burst / tension limits.

## Biaxial reduction (Lubinski ellipse / API ellipse)

Tension reduces collapse capacity and increases burst capacity; compression does the inverse. The API ellipse (in API Bul 5C3 historically, now in 5C5 / textbook restatements) plots the biaxial reduction. Casing checked at high tension near surface may fail collapse at depths where it would otherwise pass.

## Design-factor convention

Typical operator design factors (not API-mandated thresholds; operator-specified):

- Collapse: 1.0 to 1.125
- Burst: 1.1 to 1.25
- Tension: 1.4 to 1.8 (highest because tension failures are catastrophic)
- Triaxial: 1.25 to 1.4

## Selection workflow

1. **Setting depths first** — driven by formation pressures, lost-circulation zones, salt sections, kick tolerance.
2. **Worst-case loads second** — for each string, evaluate the worst credible collapse, burst, tension scenario.
3. **Grade-and-weight selection** — pick the lightest, cheapest combination meeting design factors at every depth point. Often "tapered" strings with heavier sections at the top (high tension) and lighter sections near the shoe (low tension, moderate burst).
4. **Connection selection** — API for routine, premium for high-pressure or gas-tight requirements.
5. **PSL specification** — PSL-2 or PSL-3 for sour service, HPHT, or critical wells.

## Perforation policy — burst-rating interaction

Casing burst design carries a load-case from a domain that drilling-engineering does not own: **perforation policy**. Detonation of a downhole shaped-charge gun creates a transient overpressure pulse in the wellbore (thousands of psi for milliseconds for a typical large-OD TCP gun), which adds to the static wellbore pressure to define a **transient burst load** at the perforating depth.

Practical interactions:

- Heavy / high-shot-density gun strings are checked against the production-casing burst envelope before being scheduled into completion design.
- For HPHT wells with marginal production-casing burst headroom, the completion engineer may be forced to reduce shot density or select lower-energy charges — derating the well's IPR floor to preserve casing integrity.
- The production-casing design factor margin selected during well construction effectively budgets for the perforation-job load case. Operators with stable completion designs can use a tighter casing factor; operators with uncertain or evolving completion designs need more margin.

The perforation-strategy framework lives in the production-engineering wiki: see [Perforating](../../../production-engineering/wiki/concepts/perforating.md) for the system-level synthesis and [Perforating Gun Systems](../../../production-engineering/wiki/concepts/perforating-gun-systems.md) for the gun-detonation-pulse considerations that interact with the burst-design margin established here.

## Sand-control completion impact on production-casing ID requirements

A second production-engineering load class enters the casing-program design through the **sand-control completion type**: the production-casing ID must accommodate the sand-control assembly OD plus running clearance, plus any service-tool clearance required for execution of the placement job (gravel-pack, frac-pack) inside the same casing. This requirement is set in the production-engineering wiki and propagates back to the casing-program design here.

Practical interactions:

- **Standalone screens** add modest OD over a bare production tubing string; production casing sized for the tubing string typically accommodates standalone-screen completions with no design change.
- **Cased-hole gravel-pack assemblies** add a screen-and-blank assembly inside the casing plus a gravel-pack packer plus crossover service tools during placement. The production-casing ID must accommodate the largest of these tool ODs, with running clearance, during the placement job. Operators planning gravel-pack completions should confirm production-casing ID adequacy at the casing-program-design phase rather than discover the gap during completion-job planning.
- **Frac-pack assemblies** carry the same production-casing ID requirements as cased-hole gravel-packs, plus a higher transient-treating-pressure load on the production casing during the frac portion of the pumping job. Marginal-burst-headroom production casing may force the operator to derate the frac-pack treatment pressure, which in turn caps the deliverability gain available from the frac-pack — a coupling that should be surfaced and resolved during well design, not during completion execution.
- **Expandable screens** are designed precisely to fit through tight production-casing IDs; they relax the gravel-pack-style ID floor at the cost of expansion-execution complexity downhole.

The sand-control framework lives in the production-engineering wiki: see [Sand Control](../../../production-engineering/wiki/concepts/sand-control.md) for the architecture catalogue and decision framework, [Gravel Packing](../../../production-engineering/wiki/concepts/gravel-packing.md) for the cased-hole-vs-open-hole pack architecture and assembly OD considerations, and [Frac Packing](../../../production-engineering/wiki/concepts/frac-packing.md) for the production-casing-burst-margin coupling specific to frac-pack treatments.

## Hydraulic fracturing — production casing must accommodate frac treating pressure + burst margin

A third (and often largest) production-engineering load on the production casing comes from **hydraulic fracturing**. A frac job pumps high-pressure viscosified slurry through the production casing into the perforations, exposing the casing to a sustained treating pressure that can range from 5,000-15,000+ psi at the surface (with corresponding casing-pressure profiles at depth modified by hydrostatic head and friction). For modern unconventional-play multi-stage horizontal-well frac jobs, the frac treating pressure is frequently the single largest burst-design driver for the production-casing string.

Practical interactions:

- **Treating-pressure budget** — the production-casing burst rating at the worst-case depth, less the burst safety factor (typically 1.1-1.25 per the design-factor convention above), defines the maximum treating pressure that can be safely pumped. Operators planning frac jobs must confirm the casing budget *before* dispatching pumping equipment; an under-rated production casing forces a treating-pressure derate that may cap the frac geometry below the target half-length / conductivity.
- **Friction-pressure budget** — high-viscosity frac fluid generates significant friction pressure in the tubing and casing string. Surface treating pressure equals downhole treating pressure plus friction; the friction-pressure budget eats into the available pumping margin, sometimes requiring the operator to switch to a lower-viscosity carrier fluid or to accept a lower pump rate.
- **Repeated cycling** — multi-stage horizontal-well frac jobs cycle the production-casing pressure dozens of times over the course of a single completion sequence. Fatigue effects on the casing (and especially on the casing connections) are a known integrity concern; some operators specify premium connections precisely to handle the cyclic loading.
- **Sour-service compatibility** — frac jobs in sour-service formations require sour-rated casing per NACE MR0175 / ISO 15156 because the frac-fluid pressure-cycling occurs in the presence of hydrogen-sulphide-bearing produced fluid in re-frac scenarios.
- **Frac-design-vs-casing-design feedback** — well-planning teams should iterate the casing-program design and the planned frac-design together. A casing program optimised for drilling and run-in-place efficiency may be inadequate for the planned frac, and a frac-design optimised for productivity may exceed the casing budget. Surfacing this feedback during well design rather than during completion-job planning avoids costly late-stage redesigns.

The hydraulic-fracturing framework lives in the production-engineering wiki: see [Hydraulic Fracturing](../../../production-engineering/wiki/concepts/hydraulic-fracturing.md) for the system-level synthesis, [Frac Design](../../../production-engineering/wiki/concepts/frac-design.md) for the pump-schedule architecture and pump-rate selection logic, [Frac Fluids](../../../production-engineering/wiki/concepts/frac-fluids.md) for the fluid-friction-pressure considerations, and [Proppants](../../../production-engineering/wiki/concepts/proppants.md) for the proppant-pack conductivity that the casing-pressure budget ultimately delivers.

## Public references

- **Bourgoyne, Chenevert, Millheim, Young** — *Applied Drilling Engineering*, SPE Textbook Series Vol. 2, 1986 (ISBN 1-55563-001-4). Chapter 7 casing design.
- **Mitchell & Miska** — *Fundamentals of Drilling Engineering*, SPE 2011 (ISBN 978-1-55563-207-6). Tubular design chapter.
- **Lyons (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, Elsevier (ISBN 978-0-7506-7785-1). Casing-design section.
- **API Spec 5CT** 10th Edition (identical adoption of ISO 11960) — see [api-spec-5ct.md](../standards/api-spec-5ct.md).

## Cross-references

- [Casing Grades and PSL](casing-grades-and-psl.md) — grade families and PSL framework
- [Casing Shoe Track](casing-shoe-track.md) — shoe / float-collar geometry and cement-bond design boundary
- [API Spec 5CT](../standards/api-spec-5ct.md), [API RP 5C5](../standards/api-rp-5c5.md), [API RP 5C1](../standards/api-rp-5c1.md)
- Production-engineering: [Perforating](../../../production-engineering/wiki/concepts/perforating.md), [Perforating Gun Systems](../../../production-engineering/wiki/concepts/perforating-gun-systems.md) — perforation policy / gun-detonation-pulse interaction with burst design
- Production-engineering: [Sand Control](../../../production-engineering/wiki/concepts/sand-control.md), [Gravel Packing](../../../production-engineering/wiki/concepts/gravel-packing.md), [Frac Packing](../../../production-engineering/wiki/concepts/frac-packing.md) — sand-control completion architectures impose production-casing ID floor requirements (and frac-pack imposes a transient burst-pressure load)
- Production-engineering: [Hydraulic Fracturing](../../../production-engineering/wiki/concepts/hydraulic-fracturing.md), [Frac Design](../../../production-engineering/wiki/concepts/frac-design.md), [Frac Fluids](../../../production-engineering/wiki/concepts/frac-fluids.md), [Proppants](../../../production-engineering/wiki/concepts/proppants.md) — hydraulic fracturing imposes the largest single burst-design load on the production-casing string in modern unconventional-play multi-stage horizontal-well frac jobs (treating-pressure budget, friction-pressure budget, cyclic-load fatigue)
- Downstream consumer: [vamseeachanta/workspace-hub#1958](https://github.com/vamseeachanta/workspace-hub/issues/1958) — slim-hole well-engineering calc module (casing-program comparison + economics) — this concept page is the design-rationale anchor that module's outputs should cite
- Founding source: [Papkov (2026)](../sources/papkov-2026-drilling-tender-ai-agent.md) — AI-tender-evaluation downstream consumer
