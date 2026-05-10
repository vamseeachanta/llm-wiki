---
title: "Ductile Tearing and J-Controlled Crack Growth"
slug: ductile-tearing
tags:
  - fracture-mechanics
  - ductile-tearing
  - j-r-curve
  - ctod-r
  - eqct
  - ffs-input
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
sources:
  - standards/astm-e1820.md
  - standards/api-std-579.md
---

# Ductile Tearing and J-Controlled Crack Growth

## What is ductile tearing?

Ductile tearing is **stable, slow crack-growth in elastic-plastic
materials** at temperatures and loading rates where the material can
dissipate energy through crack-tip plasticity. The crack extends
incrementally as the applied load (or `J` / CTOD) rises — each new
increment of crack extension `Δa` requires a new increment of driving
force. This is fundamentally different from the unstable cleavage of
[brittle-fracture](brittle-fracture.md): tearing is not a single catastrophic event but a
load-history-dependent process that the structure can be operated
into, paused, inspected, and (within limits) operated through.

The defining experimental signature is a rising
**resistance curve** (`J–R` or CTOD-R): apparent toughness *increases*
with crack extension because plastic-zone development, void-sheet
linkage, and shear-lip formation all consume energy ahead of the
moving crack tip.

## Why ductile tearing matters in oil and gas

Modern offshore and petrochemical structural steels — API 5L X65/X70
line-pipe, ASTM A707 / A350 forgings, P91 power-plant steel, and
modern ferritic-pearlitic plate — operate **above the brittle-ductile
transition** for the bulk of service life. Their fracture-toughness
budget is governed by ductile tearing, not by linear-elastic
plane-strain `K_Ic` ([astm-e399](../standards/astm-e399.md) regime). Consequently:

- FFS Level-2 and Level-3 assessments under
  [API 579-1 / ASME FFS-1](../standards/api-std-579.md) Part 9 and
  [BS 7910 Annex B](../standards/bs-7910-flaw-assessment.md) need
  **`J–R` or CTOD-R curves**, not single-valued `K_Ic`.
- Pipeline girth-weld [engineering-critical-assessment](engineering-critical-assessment.md) (ECA)
  workflows license tolerable flaw sizes by sliding the applied
  driving force up the resistance curve until tearing instability or
  a critical `Δa` is reached.
- [leak-before-break](leak-before-break.md) arguments rely on stable tearing through the
  remaining ligament rather than abrupt cleavage; the LBB margin
  collapses if the operating temperature drops below transition.

## J-R curves and CTOD-R curves

| Quantity | Definition | Source |
|----------|------------|--------|
| `J` | Path-independent integral around the crack tip; energy release rate per unit crack extension in the elastic-plastic regime | Rice (1968); [ASTM E1820](../standards/astm-e1820.md) |
| `J–R` curve | `J` versus crack extension `Δa` | Multi-specimen *or* single-specimen elastic-compliance method per E1820 |
| CTOD-R curve | Crack-tip opening displacement `δ` versus `Δa` | Same source data, displacement-based output measure |
| `J_Ic` / `δ_Ic` | Initiation toughness — `J` (or `δ`) at the onset of stable tearing, read at the intersection of the `R`-curve with a 0.2 mm offset blunting line | [ASTM E1820](../standards/astm-e1820.md) §A9 |
| Tearing modulus `T_R` | `T_R = (E / σ_flow²) · (dJ_R / da)` — non-dimensional slope of the resistance curve | E1820; FFS practice |
| EQCT (engineering quasi-cleavage T) | Temperature / rate condition at which ductile tearing collapses to pop-in cleavage | Source-material-specific; reported per heat |

The CTOD-R curve and the `J–R` curve are duals — the same specimen
yields both. Choice between them is operational: CTOD has a longer
weldment-ECA tradition (BS 7448 / [weld-toughness](weld-toughness.md)); `J` is the
modern unified currency in [ASTM E1820](../standards/astm-e1820.md).

## Tearing instability

A flaw-bearing component is stable while **both** of the following
hold simultaneously:

1. `J_applied(a) < J_R(Δa)` — the driving force has not exceeded the
   material's accumulated resistance at the current crack length.
2. `dJ_applied / da < dJ_R / da` — the driving force is not rising
   faster with `a` than the resistance curve. Equivalently, the
   applied tearing modulus `T_app` is below the material tearing
   modulus `T_R`.

Failure occurs when both conditions fail simultaneously: the driving
force catches the resistance curve **and** the slope flips. This is
the classical **`T_R`-criterion** of Paris–Hutchinson tearing
instability theory; it is the geometric statement that the
`J_applied(a)` curve becomes tangent to, and then exits above, the
`J_R(Δa)` curve.

## How J-R feeds FFS

[API 579 Part 9](../standards/api-std-579.md) and
[BS 7910 §3 / Annex B](../standards/bs-7910-flaw-assessment.md) take
the `J–R` curve (or its CTOD-R equivalent) as toughness input and
apply ductile-tearing analysis up to a critical `Δa` or a critical
`J`. The acceptance criterion combines:

- Remaining-ligament condition (uncracked section can carry primary
  load without plastic collapse, captured by the `L_r` axis of the
  failure-assessment diagram).
- Applied stress / residual stress / weld misalignment package.
- `J_applied` versus `J_R(Δa)` *and* the tearing-modulus stability
  check of the previous section.

The FAD construction in [fitness-for-service](fitness-for-service.md) is the geometric
union of these checks, with the `K_r` axis built from `J_applied` /
`J_mat` and the `L_r` axis built from collapse load.

## Specimen-to-component transfer

`J`-controlled crack growth is only valid while the specimen geometry
maintains **small-scale yielding** (SSY) — i.e. while the plastic
zone is contained inside a `J`-dominated annulus and bounded by an
elastic far-field. The standard SSY size requirement in
[ASTM E1820](../standards/astm-e1820.md) is

```
B, b ≥ 25 · J / σ_ys
```

where `B` is specimen thickness, `b = W − a` is the remaining
ligament, and `σ_ys` is the room-temperature 0.2%-offset yield
strength (more strictly, the flow stress `σ_flow = (σ_ys + σ_uts) / 2`
in some formulations).

When the specimen or component falls outside SSY — thin sections,
shallow cracks, tension-dominated loading, biaxial loading — the
single-parameter `J`-description loses uniqueness and a
**constraint correction** must be applied. The standard tools are:

- **Q-parameter** (O'Dowd–Shih): a second parameter quantifying
  hydrostatic-stress deviation from the SSY reference field.
- **T-stress** (Williams expansion): the elastic-asymptotic second
  term, which correlates with `Q` in the contained-yielding regime.
- **`M(R)` parameter** / `J–Q–M` formalism: extended descriptors used
  in some pipeline-girth-weld and shallow-crack ECA workflows.

Constraint loss generally raises apparent toughness — i.e. the
`J–R` curve from a low-constraint geometry sits above the
high-constraint reference curve. This is conservative for fitness
arguments only when the *component* is also low-constraint;
otherwise it is an unconservative transfer.

## Boundary with the brittle regime

At low temperatures or fast loading rates the material's energy-
dissipation mechanism switches from microvoid coalescence to
transgranular cleavage, and stable tearing is interrupted by **pop-in
events** — abrupt local crack jumps visible as load drops on the
load-displacement record. Operationally:

- The [ASTM E1921](../standards/astm-e1921.md) **master curve**
  characterizes this transition through a single reference
  temperature `T₀`. Below approximately `T₀ + 50 °C`, cleavage
  dominates and a ductile-tearing assessment becomes inapplicable —
  the toughness budget reverts to a `K_Jc` (cleavage `K` from `J`)
  formulation with statistical-size scatter.
- Above `T₀ + 100 °C` (upper-shelf), tearing is fully developed and
  the `J–R` description is the appropriate tool.
- The transition band between these limits is the regime where pop-in
  classification and EQCT (engineering quasi-cleavage temperature)
  judgments matter — a ductile-tearing assessment must check that no
  qualifying pop-in occurred during the rising-`J` test record.

This is why a coherent flaw assessment requires *both* a `J–R` curve
*and* a master-curve `T₀` (or equivalent transition characterization)
for the operating temperature range — the two pages of toughness
input are non-overlapping.

## Standards

- [astm-e1820](../standards/astm-e1820.md) — primary J-R and CTOD-R measurement method; defines
  the SSY size requirement, single-specimen compliance procedure, and
  pop-in qualification rules. See
  [`standards/astm-e1820.md`](../standards/astm-e1820.md).
- [astm-e399](../standards/astm-e399.md) — LEFM plane-strain `K_Ic` regime; predecessor /
  sub-method that ductile-tearing analysis supersedes once SSY is
  exceeded. See
  [`standards/astm-e399.md`](../standards/astm-e399.md).
- [api-std-579](../standards/api-std-579.md) — Fitness-for-Service consumer; Part 9 crack-like
  flaw assessment ingests the J-R curve as material resistance and
  applies the tearing-modulus stability check. See
  [`standards/api-std-579.md`](../standards/api-std-579.md).
- [bs-7910-flaw-assessment](../standards/bs-7910-flaw-assessment.md) — UK / international parallel; Annex B
  is the explicit ductile-tearing-analysis route built on R-curve
  inputs. See
  [`standards/bs-7910-flaw-assessment.md`](../standards/bs-7910-flaw-assessment.md).

## Related concepts

- [fracture-toughness-measurement](fracture-toughness-measurement.md) — parent topic; the parameter
  families (`K_Ic`, `J_Ic`, CTOD, master curve) of which J-R and
  CTOD-R are the elastic-plastic resistance-curve members.
- [brittle-fracture](brittle-fracture.md) — the negative-criterion sibling: cleavage
  regime where ductile-tearing analysis does **not** apply.
- [fitness-for-service](fitness-for-service.md) — downstream FFS consumer of `J–R` data
  through API 579-1 / BS 7910.
- [engineering-critical-assessment](engineering-critical-assessment.md) — pipeline / weldment ECA
  workflow that licenses tolerable flaw sizes via tearing analysis.
- [leak-before-break](leak-before-break.md) — stability argument that depends on stable
  tearing through the remaining ligament before through-wall
  penetration triggers loss of containment.

## Source materials

- [`sources/og-standards-astm-e-series.md`](../sources/og-standards-astm-e-series.md)
  — catalog summary of ASTM E1820 (J-R and CTOD-R primary method),
  E399 (LEFM regime), E1921 (master curve transition).
- [`sources/og-standards-api.md`](../sources/og-standards-api.md) —
  catalog summary of API 579-1 / ASME FFS-1 Part 9 crack-like-flaw
  assessment, the FFS consumer of resistance-curve data.
- [`sources/og-standards-bsi.md`](../sources/og-standards-bsi.md) —
  catalog summary of BS 7910 Annex B (ductile-tearing analysis) and
  BS 7448 (UK J / CTOD measurement parallel to E1820).
