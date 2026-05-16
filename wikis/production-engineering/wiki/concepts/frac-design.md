---
title: "Frac Design"
tags: [frac-design, hydraulic-fracturing, pkn, kgd, pseudo-3d, fully-3d, pump-schedule, frac-width, frac-geometry, simulator]
sources:
  - api-rp-39
added: 2026-05-16
last_updated: 2026-05-16
---

# Frac Design

## Scope

Frac design is the engineering workflow that translates reservoir-and-economic targets into a concrete pumping schedule for a hydraulic-fracturing job. The workflow integrates frac-mechanics models (PKN, KGD, pseudo-3D, 3D) with fluid-rheology data (from [API RP 39](../standards/api-rp-39.md) testing) and proppant-conductivity data (from [ISO 13503 testing](proppants.md)) to produce a stage-by-stage pump schedule: pad volume, slurry-stage proppant concentration ramp, flush volume, pump rate, and total fluid + proppant requirement.

This page covers the four frac-geometry model classes, the dimensionless-fracture-conductivity (F_CD) optimisation framework, the pump-schedule architecture, and the simulator-aided workflow that integrates everything into an executable treatment design.

## The four-model hierarchy

Frac geometry — how wide, long, and tall a fracture grows for a given pumping schedule — is calculated by simulators using one of four model classes, in ascending order of complexity. Each model rests on a different set of geometric and mechanical assumptions, suiting it to a different class of frac problem.

### PKN (Perkins-Kern-Nordgren)

The PKN model assumes a fracture of **constant height** with an **elliptical cross-section**, where the frac width at the wellbore is controlled by the elastic deformation of the rock under plane-strain conditions in the vertical direction.

- **Assumption envelope** — applies when the frac length is much greater than the frac height; geometry is "long and slim" rather than "tall and short"
- **Width formula** — width scales with pumping pressure, fluid viscosity, and frac length per a closed-form elastic-mechanics expression. The classical Perkins-Kern (1961) and Nordgren (1972) formulas give the wellbore width as a function of pump rate, fluid rheology, and elapsed pumping time
- **Typical application** — mature-conventional moderate-permeability fracs in well-bounded zones; pre-microseismic-era frac-design workhorse

### KGD (Khristianovich-Geertsma-de Klerk)

The KGD model assumes a fracture of **constant height** with a **rectangular cross-section**, where the frac width is controlled by the elastic deformation of the rock under plane-strain conditions in the horizontal direction.

- **Assumption envelope** — applies when the frac length is comparable to (or less than) the frac height; geometry is "short and tall" or "square"
- **Width formula** — width scales with pumping pressure, fluid viscosity, and frac length per a different closed-form expression than PKN, reflecting the different plane-strain orientation
- **Typical application** — short-frac geometries (mini-fracs, very-short shale clusters, frac initiation in some unconventional geometries) and the early-time behaviour of all fracs (before the frac geometry has elongated enough for PKN to apply)

### Pseudo-3D (P3D)

The pseudo-3D model allows **frac height to vary along the frac length** per a height-vs-stress profile computed at each grid block, while still treating the width-vs-length-vs-height geometry with a simplified-3D approximation rather than fully-3D fracture mechanics.

- **Assumption envelope** — applies broadly to most field-scale frac jobs where height containment is partial (some height growth into zones above and below the target zone, modulated by stress and rock-strength contrasts)
- **Implementation** — the simulator computes the local frac height at each grid block from the local stress profile, then assembles the overall frac geometry as a stack of grid-block segments. Industry workhorse model class.
- **Typical application** — production-scale frac design for nearly all commercial frac jobs across all play types — conventional, tight, and unconventional

### Fully 3D (planar / fully-3D)

The fully-3D model treats the fracture as a 3D feature with **full fracture-mechanics-correct propagation** (including stress-shadow effects between adjacent fractures, height containment breakthrough at stress contrasts, and 3D-correct fluid flow inside the fracture).

- **Assumption envelope** — applies where the simpler models cannot capture controlling physics; particularly important for **multi-fracture cluster geometry in unconventional plays** where the simulator must predict simultaneous propagation of multiple fractures interacting through stress shadows
- **Implementation** — fully numerical solution to the 3D fluid-flow + 3D elastic-mechanics + 3D propagation problem; computationally expensive. Some commercial frac-design simulators implement fully-3D mode as an optional analysis path.
- **Typical application** — research-scale characterisation, high-value microseismic-validated calibration of pseudo-3D models, and increasingly some operational use in close-cluster multi-fracture unconventional designs where stress-shadow effects materially influence treatment design

### Model selection rule

Use the **simplest model that captures the controlling physics**. Default to pseudo-3D for production-scale design. Escalate to fully-3D only for high-value characterisation or when pseudo-3D systematically misses microseismic-observed geometry. Reserve PKN and KGD for back-of-envelope checks and for academic / undergraduate context.

## Dimensionless fracture conductivity (F_CD) optimisation

The well-deliverability gain from a hydraulic frac is governed by the **dimensionless fracture conductivity** F_CD:

F_CD = (k_f × w) / (k × x_f)

where:
- k_f = propped-pack permeability (mD), from [ISO 13503-5 testing](proppants.md)
- w = propped frac width (ft), from frac-design simulator output
- k = reservoir permeability (mD)
- x_f = propped frac half-length (ft), from frac-design simulator output

F_CD captures the ratio of "frac conductivity per unit length" to "reservoir conductivity per unit length", and it sits at the centre of the frac-design optimisation problem.

### The F_CD = 1.6 rule

For a given reservoir permeability k, there is a frac-design optimum at F_CD ≈ 1.6 (sometimes quoted as 1-2): below this value, the frac is "conductivity-limited" (adding more half-length doesn't help productivity because the frac itself can't carry the flow); above this value, the frac is "length-limited" (adding more conductivity doesn't help productivity because the frac is plenty conductive and the flow is choked by the far-field reservoir).

The implication for frac design:

- **High-perm reservoirs** — F_CD = 1.6 requires very high frac conductivity (high-density ceramic proppant, high concentration, optimised carrier fluid). Frac jobs in high-perm formations target short, wide, high-conductivity propped packs.
- **Low-perm reservoirs (shale)** — F_CD = 1.6 is easy to exceed; the question becomes "how much half-length can I generate" rather than "how do I balance conductivity vs length". Slickwater + sand at modest concentration suffices to exceed F_CD = 1.6.
- **Moderate-perm reservoirs** — the balance between conductivity and length is the central design question; the operator's choice of fluid family, proppant family, and proppant concentration sits exactly on this balance.

The F_CD framework is the canonical lens through which frac-design tradeoffs are evaluated. See Economides & Nolte for the comprehensive derivation and application.

## Pump-schedule architecture

The pump schedule is the stage-by-stage timeline of fluid and proppant pumped at the surface during a frac job. The schedule has four major sections:

### 1. Pad

The **pad** is clean fluid (no proppant) pumped at the start of the job. Its purpose is to:
- Initiate the fracture by exceeding σ_hmin at the perforation
- Establish frac geometry (length, height) before proppant transport begins
- Generate sufficient frac volume to accept the planned proppant slurry without screening out

Pad volume sizing is a major design lever. Under-sized pad → frac doesn't grow large enough before proppant arrives → screen-out near the wellbore. Over-sized pad → wastes fluid and creates an unpropped tip region beyond the slurry-stage propped region.

Pad volume scales with the planned half-length, the fluid leak-off coefficient, and the rock-mechanics inputs to the simulator.

### 2. Slurry stages

The **slurry stages** are pumped after the pad and carry proppant from surface to the frac. Slurry-stage design is captured by the **proppant-concentration ramp**:

- **Ramp profile** — proppant concentration increases through the slurry stages on a stepped or smooth ramp (typical: 0.5 → 1 → 2 → 4 → 6 → 8+ PPA, where PPA = pounds-of-proppant-added per gallon of carrier fluid)
- **Ramp duration** — total ramp time is set by total proppant tonnage / target average proppant concentration / pump rate
- **End-of-job concentration** — the maximum concentration at the end of the slurry sequence sets the propped frac width and the propped-pack conductivity near the wellbore

The slurry-stage ramp is the operator's primary handle on propped-pack thickness and conductivity. Higher peak concentration → thicker pack → higher conductivity, but at the cost of more transport-limited fluid behaviour and higher screen-out risk if proppant transport in the carrier fluid is inadequate.

### 3. Flush

The **flush** is clean fluid pumped after the last slurry stage to displace the wellbore-volume slug of proppant into the formation. Flush volume = the volume from the perforations to the surface mixing point at the time of the last slurry stage — typically equal to the wellbore volume plus a small safety margin.

Under-flushing → proppant left in the wellbore (requires intervention to clean out). Over-flushing → proppant washed out of the near-wellbore frac, creating an unpropped near-wellbore choke that destroys the deliverability uplift.

The flush stage is the operationally most-sensitive part of the pump schedule because the wellbore-volume calculation must be exactly right. Real-time density monitoring of the flush fluid + pressure monitoring confirms correct execution.

### 4. Shut-in / monitoring

After pumping stops, the **shut-in pressure decay** is monitored. The shut-in pressure decay reveals:
- Closure pressure (the pressure at which frac surfaces touch — equal to σ_hmin)
- Closure time (the time for the frac to fully close on the proppant)
- Any post-treatment screen-out signature (anomalous pressure behaviour after pumping stops)

Modern frac jobs incorporate the shut-in decay analysis into the post-job evaluation; the closure pressure is a high-value piece of reservoir-mechanics data that feeds back into subsequent frac designs in the same field.

## Pump-rate selection

Pump rate is bounded by:
- **Surface treating-pressure capacity** — surface pumping equipment is limited to ~10,000-15,000 psi maximum treating pressure (with most equipment well below this maximum)
- **Downhole burst margin** — production-casing burst rating at depth, less safety factor, bounds the treating pressure that can be safely held at depth (see [Casing Program Design](../../../drilling-engineering/wiki/concepts/casing-program-design.md))
- **Fluid friction pressure** — high-viscosity fluids generate high friction at high pump rate; the operator's friction-pressure budget reduces the maximum sustainable pump rate at the surface for a given downhole pressure target
- **Net-pressure / propagation requirement** — the minimum pump rate at which positive net pressure can be sustained during proppant transport, given the carrier-fluid leak-off coefficient and the planned frac geometry

The pump-rate selection is iteratively optimised against the pump-schedule design — higher pump rate generally produces shorter, fatter fracs (PKN width scales with rate); lower pump rate produces longer, thinner fracs.

## Frac-design simulator workflow

A typical modern frac-design workflow uses a commercial frac-design simulator (industry-standard examples include **FracPro**, **GOHFER**, **StimPlan**, **Mfrac** — named here at concept level only with no algorithm internals reproduced). The simulator integrates:

1. **Reservoir model** — formation thickness, depth, stress profile, pore pressure, rock-mechanics properties
2. **Mechanical-earth model** — closure stress (σ_hmin) profile, Young's modulus, Poisson's ratio, fluid-loss coefficient, frac-toughness parameter
3. **Frac-fluid model** — viscosity-vs-time-vs-temperature curves from [API RP 39](../standards/api-rp-39.md) testing (see [Frac Fluids](frac-fluids.md))
4. **Proppant model** — particle-size distribution, conductivity-vs-stress curve from [ISO 13503 testing](proppants.md) (see [Proppants](proppants.md))
5. **Pump schedule** — operator-defined pump rate, pad volume, slurry-stage ramp, flush volume

The simulator computes the resulting frac geometry (half-length, height, width, propped area) and the resulting propped-pack conductivity profile. The operator iterates the pump-schedule design against the geometry output until the target geometry is achieved.

### Pre-frac diagnostics

Before the main treatment, a typical workflow runs one or both of:
- **Step-rate test** — pump-rate is stepped through a series of values; the inflection in the rate-vs-pressure curve identifies the fracture-extension pressure (a direct proxy for σ_hmin at the perforation)
- **Mini-frac (DFIT — diagnostic fracture injection test)** — short, low-volume injection followed by extended shut-in; the pressure-decay-vs-time analysis gives closure pressure, fluid-loss coefficient, and tip-extension-pressure data that feed the main-treatment design

The pre-frac diagnostics are the operator's primary defence against design assumptions that don't match the formation; without them, the simulator design is a guess.

### Post-frac diagnostics

After the main treatment, the typical workflow analyses:
- **Pressure-decline curve** — post-treatment shut-in pressure decay vs square-root-of-time gives an estimate of frac-closure time, post-frac fluid efficiency, and any post-treatment screen-out signature
- **Production-log evaluation** (PLT) — confirms which intervals are flowing post-frac (typically in multi-stage horizontal-well fracs, PLT identifies underperforming stages)
- **Microseismic survey** (where deployed) — real-time during the treatment + post-treatment analysis of the spatial distribution of microseismic events that mark the frac's growth

## Common operator mistakes

1. **Wrong model class.** Using PKN for short-frac geometry or KGD for long-frac geometry gives wrong width predictions. Use pseudo-3D as default; escalate to fully-3D for high-stake characterisation; use PKN/KGD only for back-of-envelope checks.
2. **Skipping pre-frac diagnostics.** Without step-rate-test or mini-frac data, the simulator's closure-pressure and fluid-loss inputs are estimates from offset data — and offset data may not represent the current well. Skipping diagnostics is a known root cause of screen-out and underperformance.
3. **Pad-volume mismatch.** Pad volume sized from a generic offset-well design may not match the current well's leak-off coefficient. The mini-frac is the primary data source for pad-volume sizing.
4. **Flush-volume mismatch.** Wellbore-volume calculation must be precise; a small error in flush volume can wash proppant out of the near-wellbore region.
5. **Ignoring net-pressure history.** The treatment-pressure-vs-time history during pumping carries direct information about frac growth, fluid-loss, and screen-out risk. Operators who run frac jobs without real-time net-pressure analysis are flying blind.
6. **Over-designing for ceramic.** F_CD optimisation in moderate-perm formations often shows that the marginal benefit of switching from sand to ceramic is small; the economic case for ceramic is built on a real productivity-uplift-vs-cost calculation, not on a rule-of-thumb.
7. **Under-estimating multi-fracture interaction in clusters.** Modern horizontal-well multi-stage fracs with close cluster spacing show significant stress-shadow effects; designing each cluster independently ignores the per-cluster width-reduction-from-stress-shadow that pseudo-3D simulators with stress-shadow modules can capture.

## Microseismic-validated simulator calibration

Microseismic monitoring (see [Hydraulic Fracturing](hydraulic-fracturing.md)) provides the operator with field-observation data on frac geometry that can be compared against simulator predictions. The Cipolla et al. SPE-OnePetro corpus (2008+) documents systematic divergences between simulator predictions and microseismic-observed geometry, especially in:

- **Multi-fracture (rather than single planar) propagation** in shale clusters
- **Out-of-zone height growth** in stacked-pay sequences
- **Stage-to-stage interference** in close-spaced multi-stage horizontal wells
- **Well-to-well interference** in close-spaced multi-well pads

Modern simulator calibration practice uses microseismic data to tune the simulator's stress profile, fluid-loss coefficient, and stress-shadow modules to better match observation. Iterative calibration across a sequence of wells in the same field steadily improves the simulator's predictive accuracy.

## Vendor archetype framing

Frac-design simulators are vendor-proprietary software products. Industry-standard simulators include **FracPro**, **GOHFER**, **StimPlan**, and **Mfrac**. These are named here at the concept level only; **no algorithm internals are reproduced** in this wiki. Each simulator implements the model classes (PKN, KGD, pseudo-3D, fully-3D) using vendor-proprietary numerical methods, calibration databases, stress-shadow modules, and post-processing workflows. The selection-between-simulators decision typically integrates with vendor-fleet selection for the actual pumping job.

Frac-service vendors (Halliburton, Schlumberger, Baker Hughes, Liberty, ProFrac, and independents) deliver the frac design through their integrated frac-design + frac-execution offerings, typically using one of the named simulators (sometimes vendor-internal, sometimes the operator's licensed instance). The boundary between operator-side design and vendor-side execution is increasingly fluid in unconventional plays where multi-well-pad multi-stage operations are run on a continuous schedule.

## Cross-references

- [Hydraulic Fracturing](hydraulic-fracturing.md) — the production-engineering router for hydraulic fracturing
- [Frac Fluids](frac-fluids.md) — frac-fluid families that the design integrates
- [Proppants](proppants.md) — proppant families and ISO 13503 qualification that the design integrates
- [Frac Packing](frac-packing.md) — TSO frac-pack design has a specialised pump-schedule architecture (tip-screen-out target rather than half-length-target)
- [API RP 39](../standards/api-rp-39.md) — frac-fluid viscosity testing methodology that feeds simulator inputs
- [Perforating](perforating.md), [Perforation Strategy](perforation-strategy.md) — perforation phasing and density that the frac job initiates from
- Drilling-engineering: [Casing Program Design](../../../drilling-engineering/wiki/concepts/casing-program-design.md) — production-casing burst margin gates the maximum treating pressure that can be safely pumped

## Public references

- **Economides, M. J. & Nolte, K. G. (eds.)** — *Reservoir Stimulation*, 3rd ed., Wiley, 2000 (ISBN 978-0-471-49192-7). Primary anchor for frac-design model derivations (PKN, KGD, pseudo-3D, 3D), F_CD optimisation framework, pump-schedule design, and pre-/post-frac diagnostics.
- **Perkins, T. K. & Kern, L. R.** — "Widths of Hydraulic Fractures," JPT 13(9), September 1961 (SPE-89). The foundational PKN-model paper.
- **Nordgren, R. P.** — "Propagation of a Vertical Hydraulic Fracture," SPE Journal 12(4), August 1972 (SPE-3009). The Nordgren extension of the Perkins-Kern framework.
- **Geertsma, J. & de Klerk, F.** — "A Rapid Method of Predicting Width and Extent of Hydraulically Induced Fractures," JPT 21(12), December 1969 (SPE-2458). The foundational KGD-model paper.
- **Howard, G. C. & Fast, C. R.** — *Hydraulic Fracturing*, SPE Monograph Series Vol. 2, 1970. Foundational hydraulic-fracturing reference; pre-PKN-era frac design.
- **SPE Monograph 12** — *Recent Advances in Hydraulic Fracturing*, Society of Petroleum Engineers, 1989. Coverage of pseudo-3D simulator development through the 1980s.
- **Cipolla, C. L. et al.** — extensive SPE OnePetro corpus (2008+) on microseismic-monitored frac geometry, simulator-vs-microseismic calibration, and stage-to-stage / well-to-well interference observations in unconventional plays.
- **Lyons, W. C. (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, Elsevier (ISBN 978-0-7506-7785-1) — hydraulic-fracturing chapter covering frac design framework.
- **SPE OnePetro hydraulic-fracturing-design literature** — extensive corpus on simulator development, F_CD optimisation, pump-schedule design, pre-/post-frac diagnostics across all major unconventional plays and many conventional contexts.
