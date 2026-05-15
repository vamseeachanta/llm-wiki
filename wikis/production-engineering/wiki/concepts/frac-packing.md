---
title: "Frac Packing"
tags: [frac-pack, sand-control, completions, tip-screenout, hydraulic-fracturing, hrwp, deliverability]
sources:
  - iso-17824
added: 2026-05-15
last_updated: 2026-05-15
---

# Frac Packing

## Scope

Frac packing — sometimes called "frac-and-pack" or just "frac-pack" — is a hybrid sand-control completion that combines a short, controlled hydraulic fracture with a gravel-pack-style screen completion. The frac is intentionally designed to **screen out at the tip** (tip-screenout, "TSO" design), creating a high-conductivity proppant pack in the near-wellbore region while simultaneously filling the casing-screen annular space. The well exits the frac-pack job with both **stimulation benefit** (the propped frac reduces near-wellbore skin) and **sand control** (the proppant + screen retains formation sand).

This page covers frac-pack design philosophy, tip-screenout mechanics, hybrid execution with high-rate water packing, and the operating envelope where frac-packs win versus straight gravel-packs. It is a deeper-dive companion to the [Sand Control](sand-control.md) router and complements [Gravel Packing](gravel-packing.md).

## Why frac-packing exists

Frac-packing was developed for service where straight gravel-packing leaves performance on the table — most prominently in **Gulf of Mexico shelf** completions in the 1990s, where unconsolidated sand deliverability bottlenecks demanded both sand control and stimulation in a single completion job. The economic motivation:

- **Deliverability** — gravel-pack completions in moderate-permeability unconsolidated sands often deliver below the open-hole-equivalent rate by 20-40%, due to perforation skin + gravel-pack pressure drop. A frac-pack restores or exceeds the open-hole rate by adding a high-conductivity flow path.
- **Fines mitigation** — formations dominated by very-fine fines plug standalone or pre-packed screens within months. The propped frac extends the effective reservoir contact past the fine-fines invasion zone, sustaining productivity in a class of formation that otherwise resists sand-control completion.
- **High-rate sand control** — wells where target rates exceed standalone-screen or straight-gravel-pack capacity (deepwater wells with multi-thousand-bbl/d production targets, for example) often have frac-pack as the only viable architecture.

The cost is execution complexity (frac pumping equipment, proppant logistics, real-time pressure monitoring), capital intensity (frac-pack jobs are 2-4x the cost of equivalent gravel-packs), and reduced intervention flexibility (the propped frac is essentially a permanent installation).

## Tip-screenout (TSO) design

A frac-pack is **not** a standard hydraulic frac. The fundamental design difference is the **tip-screenout**: the frac is intentionally designed so that proppant bridges and screens out at the frac tip *before* the frac is fully extended. This creates a short, fat, high-conductivity propped pack instead of the long, slim, conventional-stim frac geometry.

### Why tip-screenout is the right shape

| Attribute | Conventional frac | Frac-pack TSO |
|---|---|---|
| Frac half-length | Long (hundreds of ft) | Short (10s of ft) |
| Frac width at wellbore | Modest | Wide (inches, propped) |
| Proppant concentration | Conventional placement | High (TSO drives concentration up) |
| Conductivity | Modest, length-dominant | High, width-dominant |
| Contained-height risk | Larger | Smaller (short frac stays in zone) |
| Sand-control role | None (frac alone does not retain sand) | Pack-equivalent (proppant retains formation sand near-wellbore) |

The wide, high-concentration propped pack at the wellbore is what makes the frac-pack a sand-control completion as well as a stimulation. The short frac length keeps the treatment contained within the producing zone (out-of-zone frac growth is a serious risk in gravel-pack candidate formations because the same poorly-consolidated sand that drove the sand-control decision also offers little frac-barrier resistance).

### How tip-screenout is engineered

A TSO design has three engineering levers:

1. **Pump rate scheduling** — start at moderate rate to establish frac geometry; ramp up rate to drive proppant transport into the propagating frac.
2. **Proppant concentration ramp** — start at low proppant concentration ("ramp-up" sequence: 1 PPA → 2 PPA → 4 PPA → 6 PPA → 8+ PPA over a planned time profile) to fill the frac progressively from the tip back.
3. **Carrier-fluid viscosity profile** — viscosified carrier suspends proppant during transport; viscosity is selected to give the right balance between proppant transport (high viscosity wins) and screen-out time at the tip (lower viscosity wins).

The classic Smith-Hannah TSO design framework (and its descendants) gives operators a structured workflow: pre-frac mini-fracs to characterise leak-off, then a main-treatment design that matches the proppant ramp to the planned tip-screen-out time. Operators typically run a real-time treatment pressure-monitoring chart during pumping and stop the job at the first clear tip-screen-out signature.

## Execution sequence

A frac-pack is executed as a continuous pumping job with the screen-and-blank assembly already in the wellbore:

1. **Pre-job circulation and pad** — clear-fluid circulation through the screen confirms hydraulic communication; the pad fluid begins the frac initiation.
2. **Mini-frac (if planned)** — short, low-volume injection to measure formation closure pressure and leak-off; data is used to refine the main treatment.
3. **Main-treatment ramp-up** — proppant concentration is ramped per the design sequence; pump rate is held or stepped up.
4. **Tip-screen-out detection** — treating pressure rises sharply when the tip screens out. The pumping engineer holds rate to drive proppant into the casing-screen annular space (the "pack" portion of the job).
5. **Annular packing** — additional proppant placement fills the casing-screen annulus, just as in a conventional gravel pack.
6. **Final screen-out** — pumping continues until a clear annular-packing screen-out is detected.
7. **Reverse out, set packer, displace** — final operations match conventional gravel-pack execution.

The total job duration is typically 4-12 hours depending on interval length, proppant volume, and rate.

## High-rate water pack (HRWP) hybrid

A common variant of the frac-pack family is the **high-rate water pack** (HRWP). HRWP omits the deliberate frac-tip screen-out step and instead relies on very high pump rate (often >20 bpm) using clear-water carrier fluid to:

- Place proppant in the casing-screen annulus (as in a conventional pack);
- Drive a low-amplitude near-wellbore frac that stops short of true tip-screen-out;
- Achieve a shorter, wider proppant footprint than a TSO frac-pack but a wider footprint than a straight gravel-pack.

HRWP is often selected when:
- Formation strength is uncertain and a full TSO frac-pack carries unacceptable out-of-zone-frac-growth risk.
- Equipment availability or cost favours a simpler execution profile.
- Reservoir characterisation data is insufficient to confidently design a TSO ramp profile.

The performance trade-off is reduced frac-conductivity benefit relative to a true TSO design. Operators with extensive offset-well frac-pack history will often start with full TSO designs; operators in less-characterised areas will start with HRWP and move to TSO as confidence builds.

## Operating envelope — frac-pack vs gravel-pack

| Driver | Favours frac-pack | Favours gravel-pack |
|---|---|---|
| Permeability | Moderate (10-1,000 mD) | High (>1 D) |
| Formation PSD | Fine-fines-dominated | Well-sorted moderate-to-coarse |
| Deliverability target | Aggressive | Moderate |
| Stimulation requirement | Stimulation desired | Stimulation not needed |
| Frac-barrier confidence | High (reliable barriers) | Less critical (no frac) |
| Intervention flexibility | Less critical (well planned end-of-life) | More flexible recompletion desired |
| Cost tolerance | Higher | Lower |
| Offset-well experience | Frac-pack history available | Less experience with frac-pack |

Mixed cases (e.g. moderate-perm formation with poor frac-barrier confidence) often resolve toward HRWP as a middle ground.

## Common operator mistakes

1. **Conflating frac-pack design with conventional-frac design.** A conventional-frac engineer dropped into a frac-pack job will design too long a frac at too low a near-wellbore concentration. The TSO ramp profile and short-frac-length target are non-negotiable for the sand-control function to work.
2. **Skipping the mini-frac step.** Without leak-off and closure-pressure data, the main-treatment design is a guess. Frac-packs that screen out too early (insufficient annular pack) or screen out late (too-long frac, out-of-zone risk) usually trace back to insufficient pre-frac characterisation.
3. **Out-of-zone frac growth.** Frac-pack candidate formations are by definition unconsolidated; the frac barriers above and below the producing interval may also be weak. A frac-pack that grows out of zone connects the producing interval to a non-target zone (water-bearing or otherwise undesirable). Frac-barrier confirmation via offset-well data and microseismic monitoring is the operator's protection.
4. **Inadequate perforation density.** Like conventional gravel-pack, frac-pack requires distributed perforations to give the proppant placement uniform access; 6-12 spf is the typical floor. Below 6 spf the frac initiation azimuth becomes irregular and the annular pack is patchy.
5. **Wrong charge selection.** Big-hole charges are correct for frac-pack (the casing-wall area is the throttle for high-rate proppant slurry); deep-penetrating charges leave perforation tunnels too narrow for high-rate proppant transport. See [Perforation Strategy](perforation-strategy.md).

## Cross-references

- [Sand Control](sand-control.md) — the production-engineering router
- [Gravel Packing](gravel-packing.md) — the lower-rate / well-sorted-PSD alternative
- [Sand Control Screens](sand-control-screens.md) — screen-family selection feeding into frac-pack assemblies
- [ISO 17824](../standards/iso-17824.md) — sand-control screen qualification
- [Perforating](perforating.md), [Perforation Strategy](perforation-strategy.md) — big-hole-charge selection and shot-density floors for frac-pack
- [Electric Submersible Pumps](electric-submersible-pumps.md) — IPR / artificial-lift coupling (frac-pack typically gives the highest sand-control IPR)
- Drilling-engineering: [Casing Program Design](../../../drilling-engineering/wiki/concepts/casing-program-design.md) — production-casing burst margin must accommodate frac-pack treating pressures

## Public references

- **Smith, M. B., Miller, W. K. & Haga, J.** — "Tip Screenout Fracturing: A Technique for Soft, Unstable Formations," SPE Production Engineering 2(2), May 1987 (SPE-13273). The foundational TSO frac-pack paper.
- **Hannah, R. R. & Walker, E. J.** — multiple SPE papers on tip-screenout design and field-evidence (1980s-1990s era).
- **Penberthy, W. L. & Shaughnessy, C. M.** — *Sand Control* (SPE Monograph Series Vol. 1), Society of Petroleum Engineers, 1992 (ISBN 978-1-55563-041-6). Frac-pack and HRWP coverage.
- **Bellarby, J.** — *Well Completion Design*, Developments in Petroleum Science Vol 56, Elsevier, 2009 (ISBN 978-0-444-53210-7). Comprehensive frac-pack and HRWP design treatment.
- **Economides, M. J. & Nolte, K. G. (eds.)** — *Reservoir Stimulation*, 3rd ed., Wiley, 2000 (ISBN 0-471-49192-6). Hydraulic fracturing reference; relevant for the frac-mechanics underpinning of frac-pack design.
- **SPE OnePetro frac-pack literature** — extensive corpus on Gulf of Mexico shelf frac-pack execution, deepwater frac-pack design, HRWP-vs-TSO field comparisons.
- **Lyons, W. C. (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, Elsevier (ISBN 978-0-7506-7785-1). Sand-control chapter.
