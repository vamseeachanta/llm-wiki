---
title: "Gravel Packing"
tags: [gravel-pack, sand-control, completions, saucier-criterion, open-hole, cased-hole, screen]
sources:
  - iso-17824
added: 2026-05-15
last_updated: 2026-05-15
---

# Gravel Packing

## Scope

Gravel packing is the workhorse sand-control completion. A graded gravel (sized against the formation particle-size distribution) is placed in the annular space between the wellbore wall (open-hole) or the inside of perforated casing (cased-hole) and a downhole sand-control screen. The gravel acts as a **filter cake** — it retains formation sand, while the screen retains the gravel. Properly designed and properly placed, a gravel pack gives the operator high deliverability with sand-free production for the bulk of well life.

This page covers gravel-pack architecture (open-hole vs cased-hole), gravel-sizing logic via the [Saucier criterion](#the-saucier-criterion), and pack-placement methodology. It is a deeper-dive companion to the [Sand Control](sand-control.md) router page.

## Why gravel packing dominates

Gravel-pack completions are the most-deployed sand-control architecture worldwide because they balance four operator priorities:

1. **High deliverability** — properly placed packs support 1,000-3,000+ psi drawdown without sand influx, giving sand-free deliverability close to a damage-free perforated completion.
2. **Long service life** — well-designed gravel packs commonly serve the producing life of the well (10-25+ years) without intervention.
3. **Established execution methodology** — the placement workflow (washover, pack, circulate, displace) is well understood and reproducible across vendors.
4. **Wide formation-PSD envelope** — gravel-packing tolerates a broader range of formation PSDs than standalone screens; only the most fines-dominated formations push operators to frac-pack instead.

The cost is mechanical complexity (downhole assembly is intricate), capital intensity (gravel, screen, packer, service-tool rental), and irreversibility (a placed gravel-pack is essentially a permanent installation).

## Architecture — open-hole vs cased-hole

### Open-hole gravel pack (OHGP)

The wellbore is left bare across the producing interval. A screen-and-blank assembly is run on the production tubing, positioned across the open-hole interval, and a gravel slurry is pumped down to fill the annular space between the screen and the wellbore wall.

**When chosen:**
- Long horizontal sections in unconsolidated sand (the dominant deepwater sand-control completion).
- Wells where avoiding cased-hole perforation is desired (no perforation skin, no big-hole-charge cost, simpler completion sequence).
- Reservoirs where the open-hole geometry maximises productive contact (geometry advantage over a cased-and-perforated alternative).

**Key design constraint:**
- Wellbore-stability lifetime must exceed the placement-and-pack window. Open-hole sand can collapse during placement, ruining the pack. Drilling-fluid filter-cake quality is therefore in scope of the gravel-pack design.

**ISO standard reference:** [ISO 17824](../standards/iso-17824.md) is the canonical screen-qualification standard for OHGP screens.

### Cased-hole gravel pack (CHGP)

The producing interval is cased and perforated (with big-hole charges, see [Perforation Strategy](perforation-strategy.md)). The screen-and-blank assembly is run inside the casing across the perforated interval, and gravel is pumped to fill both the casing-screen annular space and (via the perforations) the immediate near-wellbore region.

**When chosen:**
- Cased-hole multi-zone completions where individual zones are gravel-packed in sequence.
- Reservoirs requiring zonal isolation between intervals that cannot be achieved in open-hole.
- Wells where regulatory or operational requirements mandate a cased producing interval.

**Key design constraint:**
- Perforation tunnels must be packed in addition to the casing-screen annulus. Tunnel packing is an order-of-magnitude harder than annulus packing because the tunnels are tortuous, are separated by the casing wall, and are far less hydrodynamically accessible to the placement slurry. The shot-density floor of 12-18+ spf for CHGP is set precisely to give enough tunnel-distribution density that statistical packing succeeds.

**ISO standard reference:** ISO 17825 is the sister standard for CHGP screens (adjacent to [ISO 17824](../standards/iso-17824.md)).

## The Saucier criterion

The single most operationally-relevant gravel-pack design calculation is the gravel-sizing criterion attributed to **R. J. Saucier (1974, JPT)**: gravel-pack sand should be sized so that the median gravel-grain diameter (D₅₀ of the gravel) is approximately **5 to 6 times** the median formation-sand grain diameter (D₅₀ of the formation).

The reasoning is mechanical: at this ratio, gravel grains and formation grains form a stable interlocked structure where the formation grains bridge across gravel-pack interstices without flowing through, while the gravel itself is large enough to retain its packed structure under drawdown stress.

### Saucier ratio behaviour

| Gravel D₅₀ / Formation D₅₀ | Outcome |
|---|---|
| < 4 | Gravel is too fine; pack itself flows or compacts under drawdown stress. |
| 4 to 5 | Marginal; works for narrow PSDs only. |
| **5 to 6** | **Operating sweet spot** — formation grains bridge across gravel interstices stably. |
| 6 to 8 | Marginal; formation fines may invade and bridge inside the pack, reducing permeability. |
| > 8 | Formation sand passes freely through the pack and accumulates against the screen — pack effectively fails. |

### Where Saucier needs amendment

The Saucier criterion is calibrated against well-sorted sands. Modern operators handle non-uniform PSDs via:

- **Penberthy & Shaughnessy** (1992 SPE Monograph 1) — broader-PSD treatment using D₁₀ / D₉₀ ratios alongside D₅₀.
- **Schwartz** (later refinement) — empirical extension for very fines-dominated PSDs where Saucier's bridging assumption breaks down.
- **Field-calibrated proprietary methods** (vendor-specific, not transcribed here) — applied when offset-well sand-influx history is available.

Operators ingesting a new field should always run formation-sand PSD analysis on multiple core samples (lateral and stratigraphic variability is common) before locking gravel-size selection. Single-sample PSD characterisation is a known root cause of gravel-pack failure.

## Pack-placement methodology

A gravel pack is placed via a sequence of pumping operations executed with the production tubing in place but the gravel-pack packer not yet set:

1. **Run-in-hole** — screen-and-blank assembly conveyed on production tubing to the producing interval. Wash-over crossover tool positioned at the planned packer setting depth.
2. **Establish circulation** — clear-fluid circulation through the screen-and-blank establishes baseline rates and confirms hydraulic communication.
3. **Pump gravel slurry** — gravel suspended in a carrier fluid (commonly viscosified brine or water-based gel) is pumped down the tubing, exits at the crossover, and travels into the screen-casing or screen-formation annulus.
4. **Detect screen-out** — pumping continues until pressure rises sharply, indicating the annulus has filled with gravel ("screen-out" detection). The pumping engineer decides at that signal whether placement is complete or whether a follow-up pump is needed.
5. **Reverse-circulate excess gravel** — any gravel above the screen-and-blank top is reverse-circulated out through the tubing.
6. **Set the gravel-pack packer** — packer is set at planned depth, isolating the gravel-packed interval from the upper completion.
7. **Displace to completion fluid** — completion-brine displacement removes the carrier fluid and prepares the well for production.

### Placement variants

- **High-rate water pack (HRWP)** — gravel placed at high pump rates (often >20 bpm) using clear water as carrier fluid. Relies on high carrier velocity to suspend gravel; works well in long horizontal open-hole sections.
- **Slurry pack** — gravel placed in viscosified carrier fluid at moderate rates. The viscosified carrier suspends gravel without requiring high velocity; works well in intervals with restrictive geometry.
- **Alpha-beta wave pack** — gravel placed in two sequential waves. The "alpha" wave fills the lower portion of the annulus by gravity-bedding; the "beta" wave fills above the alpha by bottom-up transport. Standard in long horizontal open-hole packs.

## Common operator mistakes

1. **Over-relying on a single core sample for PSD characterisation.** Lateral variability in sand-grain size is common; a single sample's D₅₀ may not represent the full producing interval. Multiple-sample averaging is mandatory for any non-trivial pack design.
2. **Sizing gravel against the wrong PSD percentile.** The Saucier 5-6× ratio applies to D₅₀; using D₁₀ or D₉₀ instead inflates or deflates the gravel-size selection by enough to push the pack out of the operating sweet spot.
3. **Specifying insufficient shot density for CHGP.** A 6 spf perforation density is fine for natural completion but is far too low for CHGP — the perforation tunnels cannot be reliably packed because they are not closely-enough spaced for the gravel slurry to bridge between them.
4. **Skipping pre-pack circulation.** Running the assembly to depth and immediately pumping gravel skips the chance to confirm hydraulic communication. A blocked screen or a poorly-set crossover is much harder to recognise mid-pack than during the pre-pack circulation step.
5. **Ignoring drilling-fluid filter-cake quality in OHGP design.** A poor-quality filter cake collapses during placement, exposing fresh formation sand into the placement zone, which then mixes with the gravel and ruins the pack. The drilling-fluids program for the producing interval is therefore in scope of the gravel-pack designer.

## Cross-references

- [Sand Control](sand-control.md) — the production-engineering router
- [Frac Packing](frac-packing.md) — the high-rate / fine-fines alternative
- [Sand Control Screens](sand-control-screens.md) — screen-family selection feeding into gravel-pack assemblies
- [ISO 17824](../standards/iso-17824.md) — open-hole gravel-pack screen-qualification standard
- [Perforating](perforating.md), [Perforation Strategy](perforation-strategy.md) — big-hole-charge selection and shot-density floors for CHGP
- [Electric Submersible Pumps](electric-submersible-pumps.md) — IPR / artificial-lift coupling
- Drilling-engineering: [Casing Program Design](../../../drilling-engineering/wiki/concepts/casing-program-design.md) — production-casing ID requirements driven by gravel-pack assembly OD

## Public references

- **Saucier, R. J.** — "Considerations in Gravel Pack Design," JPT 26(2), February 1974. The foundational gravel-sizing-criterion paper.
- **Penberthy, W. L. & Shaughnessy, C. M.** — *Sand Control* (SPE Monograph Series Vol. 1), Society of Petroleum Engineers, 1992 (ISBN 978-1-55563-041-6). The practitioner-canonical companion volume; Chapter on gravel-pack design and execution.
- **Stein, N. & Hilchie, D. W.** — "Estimating the Maximum Production Rate Possible from Friable Sandstones Without Using Sand Control," JPT 24(9), 1972. Foundational complement to the Saucier criterion.
- **Bellarby, J.** — *Well Completion Design*, Developments in Petroleum Science Vol 56, Elsevier, 2009 (ISBN 978-0-444-53210-7). Sand-control completion-design chapter, gravel-pack design treatment.
- **Lyons, W. C. (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, Elsevier (ISBN 978-0-7506-7785-1). Sand-control chapter.
- **SPE OnePetro gravel-pack literature** — extensive corpus on alpha-beta wave-packing, high-rate water-pack, and field-calibrated PSD-vs-Saucier comparisons.
- **ISO 17824 / 17825** — see [the standards page](../standards/iso-17824.md) for ISO 17824 (open-hole). ISO 17825 covers cased-hole.
