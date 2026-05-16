---
title: "Hydraulic Fracturing"
tags: [hydraulic-fracturing, stimulation, frac, completions, low-permeability, shale, tight-oil, tight-gas, proppant, frac-fluid]
sources:
  - api-rp-39
added: 2026-05-16
last_updated: 2026-05-16
---

# Hydraulic Fracturing

## Scope

Hydraulic fracturing is the **production-rate-amplifier** stimulation: high-pressure injection of viscosified fluid carrying a granular proppant induces a tensile fracture from the wellbore into the surrounding reservoir, then the proppant holds the fracture open against in-situ stress after pumping stops. The resulting high-conductivity flow path bypasses near-wellbore damage and extends the effective wellbore radius by orders of magnitude. Hydraulic fracturing is the dominant intervention for **low-permeability reservoirs** (tight gas, shale, tight oil) and a major intervention in moderate-permeability fields where deliverability rather than skin is the limit.

This page is the **router** for hydraulic-fracturing coverage in the production-engineering wiki. It synthesises the frac-mechanics framework, the design-decision hierarchy, the fluid-and-proppant selection logic, the pump-schedule template, and the cross-domain interactions, and links out to dedicated pages for [Frac Fluids](frac-fluids.md), [Proppants](proppants.md), and [Frac Design](frac-design.md).

## Why hydraulic fracturing is the largest-scope Phase 3 topic

Hydraulic fracturing is the production engineer's single most consequential stimulation tool, and its design touches more upstream and downstream decisions than any other completion-class intervention:

- **Reservoir-side coupling** — frac geometry (half-length, height, conductivity) sets the long-term well deliverability, decline rate, and ultimate recovery. The frac is effectively a structural modification of the reservoir's near-well drainage geometry.
- **Completion-side coupling** — frac initiation requires the right perforation policy (oriented phasing, cluster spacing, perforation density); the wrong perforation policy in a frac well leaves treating pressure on the surface and proppant in the wellbore. See [Perforating](perforating.md) and [Perforation Strategy](perforation-strategy.md).
- **Sand-control coupling** — frac-packs ([Frac Packing](frac-packing.md)) combine a deliberately tip-screen-out hydraulic frac with a sand-control gravel pack, sitting on the Phase 2 / Phase 3 boundary in this wiki. See [Sand Control](sand-control.md).
- **Drilling-engineering coupling** — production-casing burst margin must accommodate frac treating pressure plus a burst safety factor; this load case is typically the largest single burst-design driver for a production-casing string in a fracced well. See [Casing Program Design](../../../drilling-engineering/wiki/concepts/casing-program-design.md).
- **Artificial-lift coupling** — fracced wells experience characteristic post-stimulation production profiles (initial high rates, steep decline) that drive artificial-lift selection differently from conventional wells; the lift method must accommodate the early-life high rate and the late-life low rate within a single completion.

## The four hydraulic-fracturing design questions

Any hydraulic-fracturing job answers four operator questions, in roughly this order:

1. **What is the target frac geometry?** — required half-length, height, and propped conductivity to meet the deliverability target. Driven by reservoir permeability, formation thickness, and stress profile. The simulator-aided answer lives in [Frac Design](frac-design.md).
2. **Which fluid system?** — slickwater for shale (proppant transport via turbulence, cleanup-friendly), linear gel for moderate-temp moderate-perm conventional, crosslinked gel for high-temp / high-conductivity-needed jobs, energized (CO2/N2) for water-sensitive formations, foamed for water-sensitive low-pressure formations. See [Frac Fluids](frac-fluids.md).
3. **Which proppant?** — sand (cheapest, lowest crush strength), resin-coated sand (RCS, intermediate strength, anti-flowback), ceramic (highest strength + conductivity, highest cost), ultra-light (specialty for water-frac transport). See [Proppants](proppants.md).
4. **What pump schedule?** — pad volume, slurry stages, proppant concentration ramp, flush volume, rate. The design integrates the answers to questions 1-3 into a pumping-truck-ready timeline. See [Frac Design](frac-design.md).

These four decisions interlock: a slickwater frac in tight shale demands a fundamentally different pump schedule than a crosslinked-gel frac in a conventional high-perm formation. The frac-design page lays out the framework; this overview gives the system-level synthesis.

## Frac-mechanics summary

A hydraulic fracture initiates and propagates by exceeding the **minimum horizontal stress** (σ_hmin) at the perforation tunnel. Once initiated, the fracture grows perpendicular to σ_hmin (the path of least resistance), creating a planar feature whose orientation is determined by far-field stress, not by the wellbore. The fracture mechanics framework is conserved across pump rates and fluid systems:

- **Initiation pressure** — pressure required to open a tensile crack at the perforation. Set by σ_hmin plus the tensile strength of the rock plus the perforation friction. Higher than steady-state propagation pressure (a "breakdown" event is observed as a pressure spike at frac initiation).
- **Propagation pressure** — pressure required to extend the fracture during steady pumping. Set by σ_hmin plus the net pressure (a function of fluid viscosity, fluid-loss coefficient, frac geometry, and pump rate).
- **Closure pressure** — pressure at which the fracture would close without proppant. Equal to σ_hmin in most formations. Measured pre-treatment via a "step-rate test" or "minifrac" diagnostic.
- **Net pressure** — treating pressure (corrected for friction) minus closure pressure. Drives frac propagation; positive net pressure grows the frac, negative net pressure stops it.

The minimum-horizontal-stress orientation in most basins favours **vertical** fractures (because the overburden stress σ_v is the largest principal stress, so the minimum horizontal stress is the smallest). Horizontal fractures are observed only in shallow formations where σ_v has become less than σ_hmin. Practical implication: most hydraulic fractures are tall planar features oriented perpendicular to the regional σ_hmin direction.

## Frac geometry models — the four-model hierarchy

Frac geometry — how wide, how long, how tall the fracture grows for a given pump schedule — is calculated by simulators using one of four model classes, in ascending order of complexity:

| Model | Geometric assumption | When it applies |
|---|---|---|
| **PKN** (Perkins-Kern-Nordgren) | Constant frac height; ellipsoidal cross-section; width controlled by elastic deformation of the frac wall (plane-strain in the vertical direction) | Long-frac, contained-height geometry where frac length >> frac height; typical mature-conventional moderate-permeability frac |
| **KGD** (Khristianovich-Geertsma-de Klerk) | Constant frac height; rectangular cross-section; width controlled by elastic deformation in the horizontal direction (plane-strain horizontally) | Short-frac geometry where frac length is comparable to frac height; some unconventional frac geometries and the early-time behaviour of all fracs |
| **Pseudo-3D** | Frac height varies along length per stress-and-rock-strength constraints; the height-vs-stress profile is computed at each grid-block | Industry workhorse for production-scale frac design; the model class behind most commercial frac-design tools |
| **3D (planar / fully-3D)** | Full 3D fracture mechanics; height growth, multiple-fracture interaction, height-confinement breakthrough all modelled explicitly | Research and high-value characterisation (e.g. microseismic-validated multi-fracture geometry in shale); too computationally expensive for routine design |

Practical frac design uses the **simplest model that captures the controlling physics**. Most modern operator workflows use pseudo-3D simulators by default and reserve fully-3D for high-value characterisation or unusual geometries. See [Frac Design](frac-design.md) for the model-selection logic and the width-equation formulas.

## Pump-schedule architecture

A hydraulic-fracturing pump schedule has a fixed sequence of stages, regardless of fluid family or proppant choice:

1. **Pad** — clean fluid pumped first to initiate and grow the fracture before proppant transport begins. Pad volume is sized so that frac geometry reaches the target half-length before the slurry stages begin.
2. **Slurry stages** — fluid with proppant, typically pumped on a ramp of increasing proppant concentration (0.5 → 1 → 2 → 4 → 6 → 8+ PPA — pounds-of-proppant-added per gallon). Ramp design balances proppant transport (higher concentration is harder to suspend) against propped-pack conductivity (higher concentration gives a fatter pack).
3. **Flush** — clean fluid pumped after the last slurry stage to displace the wellbore-volume slug of proppant into the formation. Under-flushing leaves proppant in the wellbore; over-flushing washes proppant out of the near-wellbore frac and creates an unpropped near-wellbore choke.
4. **Shut-in / monitoring** — after pumping stops, pressure decay is monitored to characterise frac closure and to detect any post-treatment screen-out signature.

The schedule integrates with the frac-design model: pad volume is sized to the planned half-length, slurry stages are sized to the planned propped-pack area, flush volume is sized to the wellbore volume between perfs and surface. Pump-rate selection couples to fluid viscosity (high-viscosity fluid generates high friction pressure at high rate; pump rate is bounded by surface treating-pressure capacity and downhole burst margin). See [Frac Design](frac-design.md) for the schedule-design framework.

## Fluid-family overview

Five frac-fluid families cover the spectrum from cleanup-friendly low-viscosity systems to high-conductivity high-temperature systems:

- **Slickwater** — water with friction reducer at low concentration (~ppm range); very low viscosity. Workhorse for **shale** frac jobs (Bakken, Eagle Ford, Marcellus, Permian Basin) where proppant transport is via turbulence rather than viscosity, and cleanup-friendliness is critical. Disadvantage: limited proppant-transport capability, so proppant concentration is limited and most proppant settles at the wellbore.
- **Linear gel** — water + linear-polymer thickener (typically guar derivative). Moderate viscosity, no crosslinker. Used in moderate-temperature conventional frac jobs where higher viscosity than slickwater is needed but the cleanup penalty of crosslinker is unacceptable.
- **Crosslinked gel** — water + linear-polymer thickener + crosslinker (borate, zirconate, titanate). Very high viscosity at downhole shear rate, characterised under [API RP 39](../standards/api-rp-39.md). The workhorse for conventional high-temperature, high-conductivity, high-rate frac jobs. Disadvantage: significant cleanup penalty (residual polymer reduces propped-pack conductivity if not fully degraded post-treatment).
- **Energized (CO2 / N2)** — frac fluid pre-charged with carbon dioxide or nitrogen gas. The gas provides flowback drive when treatment pressure is released. Used in **water-sensitive formations** (water-sensitive clays in some tight-gas plays) and in **low-pressure reservoirs** where the formation cannot drive flowback unaided. Disadvantage: cost and surface-equipment complexity.
- **Foamed** — frac fluid with very high gas fraction (>50% by volume) created at the surface. Acts as a viscous foam for proppant transport with very low water content. Used where water sensitivity is severe (some coal-bed methane and some tight-gas plays). Disadvantage: highest cost and most surface-equipment complexity.

The frac-fluid choice is driven by formation temperature, formation water-sensitivity, target proppant concentration, and post-treatment cleanup-time tolerance. See [Frac Fluids](frac-fluids.md) for the rheology + cleanup framework.

## Proppant-family overview

Four proppant families cover the spectrum from cheapest-lowest-strength to highest-strength-highest-cost:

- **Sand** (frac sand / brown sand / Northern White) — natural quartz sand, sized and graded. Cheapest proppant; lowest crush strength (suitable to ~6,000 psi closure stress). Workhorse for **shale** plays where conductivity demands are moderate and cost dominates.
- **Resin-coated sand** (RCS) — sand with a thin resin coating applied at the manufacturing plant. The resin cures at downhole temperature, bonding the proppant pack into a coherent matrix. Intermediate crush strength; significant anti-flowback property (the resin bond prevents proppant flowback during early-time flowback at high rate).
- **Ceramic** (intermediate-density / high-density) — manufactured sintered ceramic spheres. Highest crush strength (intermediate-density to ~10,000 psi, high-density to ~15,000+ psi), highest conductivity for a given closure stress, highest cost (3-10x sand on a per-pound basis). Used in deep, high-stress formations where sand and RCS crush.
- **Ultra-light** — specialty proppants (e.g. resin-impregnated lightweight ceramic) engineered for very low density (close to or below water density). Used in **slickwater fracs** where standard-density proppant cannot be transported away from the wellbore in low-viscosity carrier fluid.

The proppant choice is driven by closure stress at depth, conductivity target, cost tolerance, and the carrier-fluid's proppant-transport capability. ISO 13503-series tests (pack permeability, conductivity, embedment, crush resistance) qualify candidate proppants for service. See [Proppants](proppants.md) for the proppant-family framework and the ISO 13503 qualification methodology.

## Microseismic monitoring

Real-time microseismic monitoring records the seismic-acoustic signature of frac propagation, giving the operator near-real-time visibility into frac geometry as it grows. A typical microseismic survey deploys an array of geophones (in offset monitor wells or surface arrays) and processes arrival times to map the spatial distribution of microseismic events that mark frac extension.

Microseismic-derived frac geometry frequently differs from frac-design-simulator predictions, especially in **horizontal-well multi-stage fracs in shale**:

- Simulators commonly under-predict effective frac height in stacked-pay shale.
- Microseismic shows multi-fracture (parallel) propagation rather than single-planar fracture growth in many shale stages.
- Stage-to-stage interference (frac-into-frac connection) and well-to-well interference (frac-into-offset-well-frac) are observed routinely in close-spaced multi-well pads.

The Cipolla et al. SPE-OnePetro corpus (2008+) documents the microseismic-to-simulator divergence and forms the empirical basis for many of the frac-design simulator calibrations in current use. See [Frac Design](frac-design.md) for how microseismic data feeds back into frac-design choices.

## Decision framework — selecting a frac architecture

A simplified operator decision tree:

1. **Reservoir permeability first.** Shale / tight gas / tight oil (sub-millidarcy) → slickwater + sand frac, multi-stage horizontal-well architecture. Moderate-perm conventional → linear-gel or crosslinked-gel + sand or RCS, vertical-well or single-stage horizontal architecture.
2. **Closure stress second.** Closure stress at depth drives proppant family: < 6,000 psi → sand acceptable; 6,000-10,000 psi → RCS or intermediate-density ceramic; > 10,000 psi → high-density ceramic.
3. **Formation temperature third.** High BHST (> 275°F) → crosslinker chemistry must be high-temp tolerant; the API RP 39 viscosity-vs-time data is the operator's primary fitness check.
4. **Water sensitivity fourth.** Water-sensitive clays or low-pressure formations → energized (CO2 / N2) or foamed; otherwise water-based slickwater / linear / crosslinked dominate.
5. **Geometry target fifth.** Target half-length, height, conductivity drive the pump schedule design (pad volume, slurry-stage ramp, flush volume). The frac-design simulator integrates the fluid-and-proppant choices with the target geometry to produce the pump-truck-ready schedule.

## Vendor archetype framing

Frac services are dominated by the integrated majors plus a strong independent-specialist contingent — particularly in the North American unconventional plays where pumping-fleet capacity is the limiting resource:

- **Halliburton frac services** — comprehensive frac-service portfolio across all fluid families, proppant families, and basin geographies.
- **Schlumberger frac services** — comprehensive frac-service portfolio; historically strong in international and offshore frac work.
- **Baker Hughes frac services** — comprehensive frac-service portfolio.
- **Liberty Energy** — large independent frac-specialist focused on North American unconventional plays.
- **ProFrac** — large independent frac-specialist focused on North American unconventional plays.

Other notable independents serve the North American frac-pumping market at scale. Vendor proprietary frac-fluid chemistry recipes, proppant manufacturing methods, and frac-design simulator algorithms are not reproduced in this wiki — vendors are named at the concept level only, with the explicit "no proprietary content reproduced" framing.

**Frac-design simulator archetypes** — industry-standard frac-design simulators include FracPro, GOHFER, StimPlan, and Mfrac. These are named here at the concept level only with no algorithm internals reproduced; they implement the pseudo-3D and 3D model classes described in [Frac Design](frac-design.md) using vendor-proprietary numerical methods, calibration databases, and post-processing workflows.

## Cross-domain interactions

- **Reservoir-engineering coupling** — frac geometry sets the long-term well deliverability and decline rate. In low-permeability reservoirs, the frac is the dominant control on ultimate recovery; reservoir characterisation feeds frac design and frac design feeds reservoir-recovery forecasting in a tight loop.
- **Perforating coupling** — perforation phasing (oriented vs isotropic) controls fracture-initiation azimuth, cluster-spacing (in multi-stage horizontal wells) controls how many fractures initiate per stage, and shot density controls per-cluster flow distribution. See [Perforating](perforating.md) and [Perforation Strategy](perforation-strategy.md).
- **Sand-control coupling** — frac-packs ([Frac Packing](frac-packing.md)) combine a deliberately tip-screen-out frac with a sand-control gravel pack. The frac-pack sits on the Phase 2 / Phase 3 boundary in this wiki because the design draws on both sand-control and hydraulic-fracturing engineering. See [Sand Control](sand-control.md).
- **Multi-zone coupling** — in multi-zone selective completions (see [Multi-Zone Completions](multi-zone-completions.md)), each zone may receive an independent frac job, requiring zonal-isolation hardware that can withstand the frac treating pressure plus burst margin.
- **Casing-program coupling** — production-casing burst margin must accommodate frac treating pressure (typically 8,000-15,000+ psi surface treating pressure for unconventional shale fracs, with corresponding casing pressure at depth) plus a burst safety factor. See [Casing Program Design](../../../drilling-engineering/wiki/concepts/casing-program-design.md).
- **Artificial-lift coupling** — fracced wells produce on a characteristic high-initial-rate, steep-decline profile. Artificial-lift selection must accommodate the early-life high rate (often unassisted, with the frac alone providing enough drive) and the late-life low rate (which usually requires a lift method matched to the late-life conditions, not the early-life conditions). See [ESP](electric-submersible-pumps.md), [Gas Lift Overview](gas-lift-overview.md), [Plunger Lift](plunger-lift.md).

## Standards anchor

- [API RP 39 — Measuring the Viscous Properties of a Cross-linked Water-Based Fracturing Fluid](../standards/api-rp-39.md) — the practitioner-canonical frac-fluid viscosity-testing methodology
- API RP 42 — *Recommended Practices for Laboratory Testing of Surface Active Agents for Well Stimulation* — sister standard for surfactant-additive testing
- ISO 13503 series — proppant qualification (pack permeability, conductivity, embedment); see [Proppants](proppants.md)
- NACE MR0175 / ISO 15156 — sour-service material requirements for frac equipment (treating iron, treating-line connections, wellhead components)

## Cross-references

- [Frac Fluids](frac-fluids.md), [Proppants](proppants.md), [Frac Design](frac-design.md)
- [API RP 39](../standards/api-rp-39.md)
- [Perforating](perforating.md), [Perforation Strategy](perforation-strategy.md)
- [Sand Control](sand-control.md), [Frac Packing](frac-packing.md)
- [Multi-Zone Completions](multi-zone-completions.md), [Intelligent-Well Completions](intelligent-well-completions.md)
- [Electric Submersible Pumps](electric-submersible-pumps.md), [Gas Lift Overview](gas-lift-overview.md), [Plunger Lift](plunger-lift.md)
- Drilling-engineering: [Casing Program Design](../../../drilling-engineering/wiki/concepts/casing-program-design.md)

## Public references

- **Economides, M. J. & Nolte, K. G. (eds.)** — *Reservoir Stimulation*, 3rd ed., Wiley, 2000 (ISBN 978-0-471-49192-7). Industry-canonical reference; primary anchor for PKN, KGD, pseudo-3D, 3D frac-width formulas and the comprehensive frac-design framework.
- **Howard, G. C. & Fast, C. R.** — *Hydraulic Fracturing*, SPE Monograph Series Vol. 2, 1970. Foundational hydraulic-fracturing reference; pre-microseismic-era frac mechanics.
- **SPE Monograph 12** — *Recent Advances in Hydraulic Fracturing*, Society of Petroleum Engineers, 1989. Mid-era reference covering the transition from conventional vertical-well fracs to horizontal-well multi-stage fracs.
- **Cipolla, C. L. et al.** — extensive SPE OnePetro corpus (2008+) on microseismic-monitored frac geometry in shale, including the multi-fracture propagation and stage-to-stage interference observations that drive modern frac-design calibration.
- **Lyons, W. C. (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, Elsevier (ISBN 978-0-7506-7785-1). Hydraulic-fracturing chapter.
- **SPE OnePetro hydraulic-fracturing literature** — extensive corpus on frac-design methodology, frac-fluid systems, proppant performance, and microseismic-monitored field results across all major unconventional plays (Bakken, Eagle Ford, Marcellus, Permian Basin, Haynesville, Niobrara, others).
