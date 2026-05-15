---
title: "Perforation Strategy"
tags: [perforating, shot-density, phasing, ehd, ehl, perforation-skin, underbalanced, completion-policy]
sources:
  - api-rp-19b
added: 2026-05-15
last_updated: 2026-05-15
---

# Perforation Strategy

## Scope

This page covers the **operator-facing design framework** for perforating: how to choose shot density (spf), phasing, charge type (entrance-hole-diameter vs entrance-hole-length trade-off), and pressure differential (underbalanced / overbalanced / extreme-overbalanced) for a given completion type. The physics of shaped charges is in [Perforating — Shaped Charges](perforating-shaped-charges.md); the hardware framework is in [Perforating Gun Systems](perforating-gun-systems.md); the system-level synthesis is in [Perforating](perforating.md).

## The four design dimensions

A perforation job is specified by four largely-orthogonal dimensions:

1. **Shot density** — perforations per foot (spf); typically 4, 6, 8, 12, sometimes 18+
2. **Phasing** — angular spacing of perforations around the wellbore axis (0°, 60°, 90°, 120°, 180°)
3. **Charge type** — deep-penetrating (DP, optimising EHL) vs big-hole (BH, optimising EHD)
4. **Pressure differential** at detonation — underbalanced (UBP) / overbalanced (OBP) / extreme-overbalanced (EOB)

The four dimensions interact, but the interactions are constrained: a given gun system supports only a finite envelope of (density × phasing × charge-type) combinations, and the differential dimension is largely set by surface-equipment capability and well-control posture.

## Dimension 1: Shot density

### What density controls

Higher shot density reduces every component of perforation skin in the Karakas–Tariq framework:

- **s_v (vertical-converging skin)** decreases because flowlines have less rock to traverse between adjacent perforations.
- **s_h (horizontal pseudo-skin)** decreases because the perforation pattern more closely approximates open-hole geometry.
- **s_wb (wellbore-blockage skin)** is largely density-independent (geometric).

The IPR-improvement from doubling shot density (e.g. 4 → 8 spf) is typically a 10-30% production increase, depending on permeability and anisotropy. The benefit diminishes at higher densities — going 12 → 18 spf gives a smaller marginal lift than 4 → 8 spf.

### Density floor by completion type

| Completion | Typical shot density |
|---|---|
| Cased-flow natural completion | 4-6 spf (low-end), 8-12 spf (best-practice) |
| Matrix-acid pre-stimulation | 6-12 spf |
| Gravel-pack | 12-18+ spf (high density mandatory) |
| Frac-pack | 6-12 spf (lower than gravel-pack because frac dominates) |
| Hydraulic fracturing (cased-hole frac) | 4-8 spf with oriented phasing |
| High-rate gas wells | 12 spf where gun geometry allows |

### Gun-system constraints on density

Maximum spf is bounded by:

- **Gun OD** — wider guns accommodate larger charges and higher density patterns
- **Charge size** — bigger charges (deeper penetration) take more circumferential space per shot
- **Casing ID** — sets gun OD upper bound, which sets density upper bound transitively

A typical 4½" OD gun supports up to ~ 12 spf; a 7" OD gun supports up to ~ 18+ spf with appropriate charge geometry.

## Dimension 2: Phasing

### What phasing controls

Phasing is the angular distribution of perforations around the wellbore axis. Standard options:

| Phasing | Description | Use case |
|---|---|---|
| 0° | All shots aligned (all on one azimuth) | Oriented perforating: cased-hole frac initiation aligned to preferred fracture azimuth |
| 60° | Six shots per density-period rotation (alternating shots offset 60°) | Most common general-purpose phasing |
| 90° | Four shots per density-period rotation | Common for medium-density patterns |
| 120° | Three shots per density-period rotation | Used in some specific gun systems |
| 180° | Two shots per density-period rotation (alternating opposite sides) | Bi-wing patterns; oriented perforating for frac initiation in two preferred directions |

### When isotropic phasing wins

In **isotropic** sand (k_v ≈ k_h, no preferred-direction permeability), distributing perforations evenly around the wellbore minimises s_h (horizontal pseudo-skin) by approximating a fully-open-hole flow geometry. Standard 60° or 90° phasing wins.

### When oriented phasing wins

Two scenarios favour oriented (0° / 180°) phasing:

1. **Cased-hole hydraulic fracturing** — perforations must align with the **maximum in-situ horizontal stress** so that fractures initiate in a coherent plane. Mis-aligned perforations produce tortuous near-wellbore fracture geometry, with the well-known consequences (high screen-out risk, treating-pressure spikes, restricted frac-conductivity).
2. **Highly anisotropic bedded rock** (k_h >> k_v in layered sandstones / shaley intervals) — perforations aligned along the bedding plane (typically horizontal) connect to more high-k pay than perforations distributed around the wellbore.

Oriented perforating requires either a **gyroscopically-oriented gun** or an **oriented-firing-head** system; the gun must be conveyed in a known azimuthal orientation. This is a substantial cost adder over standard isotropic-phased guns.

## Dimension 3: Charge type — EHL vs EHD

The fundamental charge-design trade-off (see [Perforating — Shaped Charges](perforating-shaped-charges.md)) is between **deep penetration** (small entrance-hole diameter, long tunnel) and **big entrance hole** (short tunnel, large hole).

### Deep-penetrating (DP) — chosen when EHL matters

- **Matrix-acid pre-stimulation**: acid must travel through perforation tunnels into the formation; deep tunnels bypass near-wellbore damage and put acid in fresh rock.
- **Natural completion with measured invasion damage**: the only way to bypass a measured damage zone is to perforate deeper than the damage radius. If invasion depth is 8 inches and EHL is 10 inches, the perforation tip is in undamaged rock.
- **Low-permeability formations**: every additional inch of penetration counts when permeability is the rate-limiter.

### Big-hole (BH) — chosen when EHD matters

- **Gravel-pack**: sand-control screens depend on gravel filling all interstitial space between casing wall and screen. Big entrance holes give the gravel a wider entry path.
- **Frac-pack**: the casing wall area is the throttle for high-rate proppant flow; big holes reduce perforation-friction losses.
- **High-rate gas**: friction loss across the perforation is proportional to (rate / EHD²); big holes minimise this loss in high-velocity flow.

### Rule of thumb

If the design question is "**can fluid get out of the formation, through the tunnel, into the wellbore?**" — choose DP.

If the design question is "**can a high mass-rate of fluid (or sand-laden fluid, or proppant slurry) get through the casing-wall cross-section?**" — choose BH.

Vendor catalogues separate DP and BH charges into distinct product families. Selecting the wrong family is the most common high-impact perforating-design error after temperature-rating mistakes.

## Dimension 4: Pressure differential at detonation

### Underbalanced perforating (UBP) — preferred when feasible

- Wellbore pressure < formation pressure at the instant of detonation.
- After detonation, formation surge-flow flushes crushed-zone debris **out** of the tunnels.
- Result: clean tunnels, minimal perforation skin, often s_total ≈ 0 or slightly negative on idealised math.
- McLeod (1983) framework defines a minimum-underbalance pressure required to achieve effective tunnel cleanup as a function of permeability — typically 200-2000 psi underbalance depending on k.
- Constraint: surface and downhole equipment must handle the immediate post-perforation flow; rate and pressure cannot exceed casing, tubing, packer, and flowline ratings.
- Standard practice for TCP completion-and-test operations where the well is being put on production immediately after perforation.

### Overbalanced perforating (OBP)

- Wellbore pressure > formation pressure at detonation.
- Crushed-zone debris is forced **into** the rock surrounding each tunnel.
- Result: a damaged crushed zone ringing each tunnel, contributing 5-30 elevated perforation-skin units depending on rock type and fluid contamination.
- Mandated when well-control posture requires positive overbalance (e.g. wireline gun runs against a kicked well, or recompletion add-on perfs in a high-pressure interval).
- Mitigation: post-perforation matrix-acid stimulation to dissolve the crushed-zone damage; partly effective.

### Extreme overbalanced (EOB) / dynamic-overbalance

- Wellbore pressure intentionally raised far above formation pressure immediately before detonation (often using nitrogen-charged accumulator or a gas-cushion column).
- The high differential at detonation drives a transient fracture network at each tunnel tip.
- Co-incident mini-stimulation: the tunnels themselves are cleaned and the near-wellbore rock is fractured.
- Trade-off: requires specialised surface and downhole equipment; the fracture network is uncontrolled in azimuth and length.
- Used where neither UBP nor OBP-plus-acid is the right answer — for example, in moderate-permeability formations where the operator wants stimulation but not a full frac job.

### Selection framework

1. **Default to UBP** if surface equipment can handle the surge and well-control posture permits.
2. **Use OBP** only when UBP is infeasible; plan for post-perforation matrix-acid cleanup.
3. **Consider EOB** for moderate-permeability formations where the marginal stimulation justifies the operational complexity.

## Policy by completion type

### Cased-flow natural completion

- Charge: deep-penetrating (DP)
- Density: 6-12 spf
- Phasing: 60° or 90° (isotropic)
- Differential: UBP if feasible, else OBP + matrix-acid cleanup
- Goal: bypass any near-wellbore damage; minimise perforation skin to floor the IPR penalty

### Cased-hole hydraulic fracturing

- Charge: DP for low-perm fracs, sometimes BH for high-rate gas fracs
- Density: 4-8 spf (low; the frac dominates productivity, not the perforations)
- Phasing: 0° / 180° **oriented** to maximum in-situ horizontal stress
- Differential: OBP standard; the frac will dominate near-wellbore conductivity anyway

### Gravel-pack completion

- Charge: big-hole (BH)
- Density: 12-18+ spf
- Phasing: 60° or 90° (isotropic, to give the gravel pack uniform contact)
- Differential: UBP if feasible (clean tunnels = better gravel placement); else OBP

### Frac-pack completion

- Charge: BH (high-rate proppant slurry must flow through perforation cross-section)
- Density: 6-12 spf
- Phasing: 60° or 90° (isotropic) unless oriented frac initiation is required
- Differential: UBP if feasible; OBP common

### High-rate gas

- Charge: BH (minimise perforation-friction loss)
- Density: 12 spf where gun geometry allows
- Phasing: 60° (isotropic)
- Differential: UBP

### Recompletion add-on perfs

- Charge: DP (typically; the existing perforations are already established)
- Density: matched to existing pattern
- Phasing: 60° or 90°
- Differential: typically OBP (well-control posture during recompletion)

## Damage-bypass design check

When invasion damage has been measured (well-test buildup with positive skin, drilling-fluid lab data, offset-well learnings), perforation EHL should be set to **exceed the measured damage radius** by a comfortable margin (e.g. 25-50%). If the damage radius is 12 inches, target EHL ≥ 15-18 inches.

If EHL exceeds damage radius, the perforation tip is in fresh rock and the perforation skin is dominated by the geometric (Karakas–Tariq) contribution. If EHL is shorter than damage radius, the perforation skin can be **worse** than the original damage skin — because the perforation now multiplies the damage by the geometric skin factor.

This is the single most operationally-relevant perforation-design calculation, and a leading reason that DP charges dominate natural-completion catalogues.

## Anisotropy and phasing interaction

In bedded rock with k_h / k_v >> 1, perforations aligned along the bedding plane (typically horizontal) connect to more pay than perforations distributed around the wellbore. Practical implications:

- **Vertical well in horizontal bedding**: distributed phasing (60° / 90°) still works because each perforation has approximately equal access to bedded pay.
- **Horizontal well in horizontal bedding**: the well is aligned with bedding; phasing should distribute perforations along the wellbore length, not around its axis. A 0° phasing (all on top or all on bottom) intersects only one or two bedding planes; 180° phasing helps; oriented phasing tuned to the bedding plane wins.
- **Highly-anisotropic bedded shale gas**: the high stress contrast typically forces oriented (0° / 180°) phasing for cased-hole frac, regardless of bedding direction, because the frac plane is determined by stress, not bedding.

## Sand-control completion-type-driven shot-density floors

Sand-control completion architecture sets a **floor** on perforation shot density that the perforation engineer must meet, regardless of what the natural-completion IPR optimisation would suggest. The floor is set by the placement physics of the sand-control job:

| Sand-control completion | Shot-density floor | Why |
|---|---|---|
| Standalone screen | 8-12 spf | Distribute production around the wellbore so no single perforation tunnel becomes a sand-influx hot spot |
| Cased-hole gravel-pack | 12-18+ spf | Tunnels must be packed in addition to the casing-screen annulus; only at high density does statistical tunnel-packing succeed |
| Frac-pack | 6-12 spf | Frac dominates near-wellbore flow, but the gravel still must distribute uniformly; below 6 spf the annular pack is patchy |
| Open-hole gravel-pack | (no perforations — open hole) | Floor is replaced by screen-and-blank assembly placement methodology |

Charge family is also locked: **big-hole (BH) charges are mandatory** for cased-hole gravel-pack and frac-pack because the casing-wall area is the throttle for gravel and proppant placement. Deep-penetrating charges optimal for natural completion are wrong for these sand-control jobs.

Phasing is **isotropic (60° / 90°)** for sand-control completions, in contrast to oriented (0° / 180°) phasing used for cased-hole frac-only completions. The gravel pack must distribute uniformly around the wellbore, so the perforations must too.

See [Sand Control](sand-control.md) for the architecture catalogue, [Gravel Packing](gravel-packing.md) for the Saucier-criterion gravel-sizing logic, and [Frac Packing](frac-packing.md) for the tip-screen-out hybrid completion design.

## Common operator mistakes

1. **Conflating RP 19B Section I (surface flat-target) with Section II (stressed Berea) penetration numbers.** Section I numbers are 30-50% larger than Section II for the same charge. Using the surface-test number inflates field-performance expectations.
2. **Selecting big-hole charges for natural completion** because "bigger seems better." Big-hole charges have short tunnels and elevated perforation skin from near-wellbore damage.
3. **Failing to specify temperature rating** when a charge will sit downhole for an extended period before firing (TCP guns left in the hole during testing). An RDX charge in a 350 °F well is a job-failure waiting to happen.
4. **Ignoring stand-off mismatch** when running a slim gun in a big-bore casing or vice versa. Vendor data-sheet numbers assume the design stand-off.
5. **Specifying isotropic phasing for a cased-hole frac job.** Frac initiation across multiple azimuths produces tortuous near-wellbore frac geometry; oriented phasing to maximum-stress azimuth wins.

## Cross-references

- [Perforating](perforating.md) — system-level synthesis
- [Perforating — Shaped Charges](perforating-shaped-charges.md) — physics
- [Perforating Gun Systems](perforating-gun-systems.md) — hardware framework
- [API RP 19B](../standards/api-rp-19b.md) — charge-performance evaluation
- [Electric Submersible Pumps](electric-submersible-pumps.md) — IPR / artificial-lift coupling
- [Gas Lift Overview](gas-lift-overview.md) — IPR / artificial-lift coupling
- Drilling-engineering: [Casing Program Design](../../../drilling-engineering/wiki/concepts/casing-program-design.md)

## Public references

- **Karakas, M. & Tariq, S.** — "Semianalytical Productivity Models for Perforated Completions," SPE Production Engineering 6(1), 1991. The foundational perforation-skin framework.
- **McLeod, H. O.** — "The Effect of Perforating Conditions on Well Performance," JPT 35(1), 1983. The foundational underbalanced-perforating framework.
- **Locke, S.** — "An Advanced Method for Predicting the Productivity Ratio of a Perforated Well," JPT 33(12), 1981.
- **Bell, W. T. & Behrmann, L. A.** — *Perforating Applications in the Petroleum Industry* (SPE Reprint Series).
- **Behrmann, L. A.** — multiple SPE papers on underbalanced-perforating field-evidence (1990s, 2000s).
- **Lyons, W. C. (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, Elsevier (ISBN 978-0-7506-7785-1).
- **API RP 19B** — see [the standards page](../standards/api-rp-19b.md).
