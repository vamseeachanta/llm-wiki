---
title: "Proppants"
tags: [proppant, hydraulic-fracturing, frac-sand, resin-coated-sand, ceramic-proppant, ultra-light-proppant, iso-13503, conductivity, crush-strength]
sources:
  - iso-13503
added: 2026-05-16
last_updated: 2026-05-16
---

# Proppants

## Scope

Proppants are the granular materials placed in a hydraulic fracture to **hold the fracture open against in-situ closure stress** after pumping stops. Without proppant, the fracture would close immediately at the cessation of treating pressure and the stimulation benefit would be zero. With well-designed proppant placement, the propped fracture creates a permanent high-conductivity flow path from the far-field reservoir to the wellbore. Proppant selection and qualification is therefore the second load-bearing piece of frac-design hardware (alongside [frac fluids](frac-fluids.md)) that determines the success of a hydraulic-fracturing job.

This page covers the four proppant families (sand, resin-coated sand, ceramic, ultra-light), the ISO 13503 qualification framework that gates them for service, the conductivity-vs-stress framework that drives selection, and the operating envelopes where each family wins.

## The four proppant families

| Family | Specific gravity | Crush strength (typical) | Conductivity at design stress | Cost (relative) | Workhorse application |
|---|---|---|---|---|---|
| **Sand** (frac sand / Northern White / brown) | 2.65 | Up to 6,000 psi | Moderate | 1x | Shale fracs (cost-dominant) |
| **Resin-coated sand (RCS)** | 2.55-2.65 | Up to 8,000 psi | Moderate-to-high | 2-3x | Anti-flowback applications |
| **Ceramic** (intermediate / high density) | 2.7-3.5 | 10,000-15,000+ psi | High | 3-10x | Deep / high-stress formations |
| **Ultra-light** | 1.0-2.0 | Variable | Specialty | 5-15x | Slickwater proppant-transport solutions |

Each family is qualified for service under the ISO 13503 series of standards, which defines the laboratory test methodology that produces vendor-comparable performance data.

## Sand (frac sand)

Natural quartz sand, sourced from specific high-purity sand deposits, sized and graded to defined particle-size envelopes (typically 30/50 mesh, 40/70 mesh, 100 mesh). The most cost-competitive proppant — basis of the cost economics that make shale fracs commercially viable.

### Sources
- **Northern White** — high-purity quartz sand from the U.S. Upper Midwest (Wisconsin, Minnesota, Illinois). Industry-canonical reference grade.
- **Brown sand** — slightly lower purity, lower crush strength, lower cost. Used in shallower and lower-stress fracs.
- **In-basin sand** — local sand sources developed near major unconventional plays (West Texas, others) to reduce transportation cost. Quality varies; qualified per ISO 13503-2 for each source.

### Crush strength
- **Up to ~6,000 psi closure stress** — sand pack maintains adequate conductivity
- **6,000-8,000 psi** — sand starts to crush, conductivity drops sharply
- **Above 8,000 psi** — sand is generally inadequate; RCS or ceramic must be considered

### Application
- **Workhorse for shale plays** where typical closure stress at depth (4,000-8,000 psi) is within sand's working envelope and where the per-pound cost is the dominant economic driver
- **Cost-driven applications** generally, even outside shale, where moderate conductivity is sufficient

## Resin-coated sand (RCS)

Sand particles coated with a thin thermoset resin layer applied at the proppant-manufacturing plant. The resin cures at downhole temperature, bonding the proppant pack into a coherent matrix that resists individual grain crushing and flowback.

### Two RCS variants
- **Pre-cured RCS** — the resin is fully cured during manufacturing; the pack remains as discrete grains in the well. Anti-flowback effect comes from the resin's surface friction; crush strength is modestly higher than sand because the resin coating distributes point loads.
- **Curable RCS** — the resin remains uncured during pumping and cures only at downhole temperature, bonding the proppant grains into a consolidated matrix. The matrix is much more resistant to flowback than discrete grains, and the crush strength is meaningfully higher than sand because point-loads are distributed across the bonded matrix.

### Crush strength
- **Up to ~8,000 psi closure stress** — RCS pack maintains adequate conductivity
- **8,000-10,000 psi** — borderline; curable RCS may extend slightly higher than pre-cured

### Anti-flowback
- RCS's primary differentiator vs sand is **anti-flowback performance** — the resin bond prevents proppant grains from migrating with produced fluid during early-time flowback at high rate.
- Particularly valuable in **shallow and high-rate flowback conditions** where standard sand would migrate into the wellbore and choke production.

### Application
- **Flowback-rate-sensitive applications** where sand would migrate
- **Intermediate-depth wells** (10,000-15,000 ft) where closure stress exceeds sand's envelope but ceramic cost is unjustified
- Increasingly used as a **tail-in stage** at the end of an otherwise-sand frac job to give an anti-flowback near-wellbore layer

## Ceramic proppants

Manufactured sintered ceramic spheres produced from selected raw materials (bauxite, kaolin clay, or specialty mineral mixes). The spheres are precisely sized, shaped (high sphericity, high roundness), and sintered to a defined density and crush strength.

### Density classes
- **Intermediate-density ceramic (IDC)** — specific gravity ~ 2.7-3.0. Working envelope to ~ 10,000 psi closure stress.
- **High-density ceramic (HDC)** — specific gravity ~ 3.2-3.7. Working envelope to ~ 15,000+ psi closure stress.

### Performance
- **Highest crush strength** of any common proppant family — extends propped-pack conductivity to closure stresses where sand and RCS fail.
- **Highest sphericity and roundness** — the geometric uniformity gives higher pack permeability per unit of pack volume than sand.
- **Highest conductivity at a given stress** — combines high pack permeability with low crush damage.

### Cost
- 3-10x sand on a per-pound basis. Cost is dominated by the energy-intensive sintering process.
- In a typical frac job, ceramic proppant cost can be 30-60% of total job cost (vs ~5-15% for sand). The economic case for ceramic is built on the productivity-uplift-vs-sand calculation, which must exceed the cost premium across the well's life.

### Application
- **Deep wells** (15,000-25,000+ ft TVD) where closure stress at depth exceeds sand and RCS envelope
- **HPHT formations** where closure stress is high and conductivity demand is high
- **High-rate / high-conductivity-need fracs** where sand-proppant-pack conductivity would be the bottleneck
- **Tail-in stages** at the end of a sand-dominant job to give a near-wellbore high-conductivity layer

## Ultra-light proppants

Specialty proppants engineered for very low density — close to or below water density. Achieved through engineered-porous ceramic, resin-impregnated lightweight ceramic, hollow ceramic spheres, or polymer-based hybrid materials.

### Operating principle
- **Density-matched to carrier fluid** — at specific gravity close to 1.0, the proppant settling velocity per Stokes' law approaches zero in water-based carrier fluid.
- The proppant is **transported by the carrier fluid as a near-suspension**, dramatically extending the effective frac half-length over which proppant is distributed.

### Application
- **Slickwater fracs** where standard-density proppant settling is the gating problem on far-field proppant placement
- **Specialty applications** where standard-density proppant cannot reach the target frac geometry

### Limitations
- Highest cost per pound of any proppant family
- Crush strength generally lower than ceramic (depends on specific product chemistry)
- Operational complexity (specialised handling, blending, surface logistics)

## ISO 13503 qualification framework

The ISO 13503 series — *Petroleum and natural gas industries — Completion fluids and materials* — provides the standardised laboratory test methodology that qualifies a candidate proppant for service. The series covers multiple test methods, each addressing a specific performance dimension:

| Test | Property measured | Why operators care |
|---|---|---|
| **ISO 13503-2** | Sieve analysis, sphericity, roundness, acid solubility, turbidity | Confirms the proppant meets specified physical specifications |
| **ISO 13503-5** | Long-term proppant-pack conductivity at controlled closure stress | Primary input for the conductivity-vs-stress curve that drives proppant selection |
| **ISO 13503-3** | Slurry-friendly suspension testing | Confirms the proppant is transportable in the specified carrier fluid |
| **Crush resistance** (within ISO 13503-2 framework) | Percent fines generated under defined closure stress | Direct measure of the proppant's ability to maintain pack integrity at depth |

The specific test conditions, sample sizes, and reporting formats are defined in each part of the series. The standard is paywalled; this wiki paraphrases the structural intent and references the standards for operators who already have licensed copies. No verbatim text reproduced.

### What the qualification data is used for

Frac-design simulators (see [Frac Design](frac-design.md)) consume ISO 13503 conductivity-vs-stress data to:

1. **Convert frac geometry to deliverability** — the propped-pack conductivity at the expected closure stress, combined with the frac half-length and frac width, gives the dimensionless fracture conductivity F_CD that feeds the well-deliverability model.
2. **Select proppant for target stress envelope** — the operator's expected closure stress at depth must lie within the proppant's working envelope (conductivity must not degrade below the design target across the expected stress range).
3. **Plan proppant-concentration ramp** — higher proppant concentration in the carrier fluid gives a thicker, higher-conductivity propped pack. The ramp design balances transport limitations against conductivity targets.

## Conductivity-vs-stress framework

A propped-pack's conductivity (permeability × pack width) is the primary performance metric. Conductivity is governed by:

- **Proppant crush strength** — at closure stress above the crush threshold, conductivity drops sharply as fines are generated
- **Pack permeability** — controlled by particle size distribution (larger sieve → higher permeability) and sphericity / roundness
- **Pack width** — controlled by the proppant concentration in the carrier fluid (more proppant per square foot → thicker pack)
- **Embedment** — pressure-driven embedding of proppant grains into the formation face reduces effective pack width. Soft formations (some shales, unconsolidated sands) suffer significant embedment.
- **Non-Darcy flow** — at high flow velocities (typical in gas wells immediately after frac), inertial losses add an additional pressure-drop component beyond Darcy permeability. Non-Darcy effects scale with the inverse of proppant size, so larger proppants are favoured for high-rate gas wells.
- **Residual-fluid damage** — incomplete cleanup of crosslinked frac-fluid polymer reduces effective pack permeability (see [Frac Fluids](frac-fluids.md))

The composite effect — measured under ISO 13503-5 at controlled closure stress with field-representative carrier-fluid residue — gives the operator the "effective" propped-pack conductivity that feeds the deliverability calculation.

## Selection framework — matching proppant to stress envelope

A simplified operator decision tree for proppant selection:

1. **Calculate closure stress at depth.** Closure stress ≈ overburden gradient × TVD minus pore-pressure, often ~ 0.7-0.9 psi/ft in normally-pressured sediments (the actual closure-stress value comes from a step-rate test or mini-frac diagnostic, not from a rule-of-thumb).
2. **Pick proppant family by stress envelope.** < 6,000 psi → sand (cost-dominant). 6,000-10,000 psi → RCS or intermediate-density ceramic. > 10,000 psi → high-density ceramic.
3. **Assess flowback-rate sensitivity.** High-rate / shallow / flowback-aggressive wells → RCS for anti-flowback, or RCS tail-in on a sand-dominant job.
4. **Assess proppant-transport capability of carrier fluid.** Slickwater → standard sand or ultra-light. Linear / crosslinked → standard or ceramic per the stress envelope.
5. **Apply economic check.** Compute productivity uplift vs cost for each candidate proppant family; the marginal-productivity-vs-marginal-cost calculation often gates the ceramic-vs-sand or RCS-vs-sand decision.

## Common operator mistakes

1. **Sand in a high-stress well.** Closing stress is computed for early-life conditions; late-life closure stress (after reservoir-pressure depletion) is higher. A sand pack that works at frac time may crush at late-life conditions, choking the well's late-life productivity precisely when the operator is least equipped to remediate.
2. **Standard-density proppant in slickwater.** Slickwater's low viscosity cannot transport standard-density proppant beyond near-wellbore; the operator pumps proppant volume far in excess of what reaches the far-field frac. Ultra-light proppant or slickwater-optimised proppant placement is the alternative.
3. **Ceramic over-design.** Ceramic is the highest-conductivity proppant but the highest cost. Operators have repeatedly over-designed ceramic where intermediate-density-ceramic or RCS would have delivered adequate performance at much lower cost.
4. **Embedment under-design.** Soft formations (shale, unconsolidated sand) embed proppant into the formation face. The frac-design simulator must account for embedment; underestimating embedment over-states propped-pack thickness and over-states deliverability.
5. **Ignoring non-Darcy flow.** High-rate gas wells immediately after frac experience significant non-Darcy pressure losses in the propped pack. Selecting proppant size for steady-state Darcy flow under-designs the early-life deliverability gain.

## Vendor archetype framing

Proppant supply is dominated by a few large mining and ceramic-manufacturing operators plus many regional sand suppliers in the unconventional plays. Frac-service vendors (Halliburton, Schlumberger, Baker Hughes, Liberty, ProFrac, and independents) typically procure proppant from the manufacturers rather than mining it themselves; some integrated frac-service companies have vertically integrated specific proppant sources. Specific proppant brand names, proppant-manufacturing methods, and proppant-quality optimisation workflows are vendor-proprietary and are **not reproduced** in this wiki.

## Cross-references

- [Hydraulic Fracturing](hydraulic-fracturing.md) — the production-engineering router for hydraulic fracturing
- [Frac Fluids](frac-fluids.md) — frac-fluid families (the carrier-fluid-side counterpart to this proppant-side framework)
- [Frac Design](frac-design.md) — pump-schedule and frac-geometry design that integrates proppant choice with fluid choice
- [Frac Packing](frac-packing.md) — TSO frac-pack design specifies proppant differently from conventional frac (higher concentration, narrower size distribution for the pack-quality role)
- [Sand Control](sand-control.md) — the gravel-pack-pack-side counterpart for sand-control completions (where the "gravel" plays a sand-control role rather than a frac-conductivity role)

## Public references

- **Economides, M. J. & Nolte, K. G. (eds.)** — *Reservoir Stimulation*, 3rd ed., Wiley, 2000 (ISBN 978-0-471-49192-7). Comprehensive proppant-pack conductivity and selection-framework coverage; primary anchor for the framework on this page.
- **Howard, G. C. & Fast, C. R.** — *Hydraulic Fracturing*, SPE Monograph Series Vol. 2, 1970. Foundational proppant-conductivity testing era reference.
- **SPE Monograph 12** — *Recent Advances in Hydraulic Fracturing*, Society of Petroleum Engineers, 1989. Coverage of ceramic-proppant development through the 1980s.
- **Lyons, W. C. (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, Elsevier (ISBN 978-0-7506-7785-1) — hydraulic-fracturing chapter covering proppant families and selection.
- **SPE OnePetro proppant literature** — extensive corpus on proppant-pack conductivity testing, embedment effects, non-Darcy flow effects, in-basin sand qualification (especially West Texas Wolfcamp / Bone Spring), and proppant-flowback mitigation strategies.
- **ISO 13503 series** — see [API RP 39](../standards/api-rp-39.md) for the frac-fluid-side counterpart; ISO 13503 is the proppant-side qualification standard.
