---
title: "Froude Number"
tags: [froude-number, similitude, dimensionless, ship-resistance, wave-making, hydrodynamics, planing, shallow-water]
sources:
  - naval-architecture-resources
  - linkedin-miah-2026-froude-number
added: 2026-05-12
last_updated: 2026-05-12
see_also:
  - concepts/ship-resistance-components.md
  - concepts/resistance-propulsion.md
  - concepts/hull-form-geometry.md
  - concepts/seakeeping.md
  - concepts/wave-theory-and-spectra.md
---

# Froude Number

## Scope

This page covers the Froude number as the central dimensionless governing free-surface gravity-wave effects in ship hydrodynamics: its definition, its principal variants, the speed regimes it delineates, and the practical limit it imposes on model-scale testing. It is the similitude-side hub for the resistance family — detailed component decomposition of total resistance lives at [Ship Resistance Components](ship-resistance-components.md), and the router page is [Ship Resistance and Propulsion](resistance-propulsion.md). It does **not** restate ITTC procedural formulas — those are deferred to a future standards page.

## Definition

The length-based Froude number is

  Fn = V / sqrt(g · L)

where V is ship speed (m/s), g is gravitational acceleration (≈ 9.81 m/s²), and L is a characteristic length — typically the waterline length L_WL. Fn is dimensionless and represents the ratio of inertial to gravitational forces in the free-surface flow around the hull.

## Why it matters

Two geometrically similar hulls advancing at the same Froude number produce geometrically similar free-surface wave patterns. This is the basis for towing-tank model testing: a scaled model run at V_m = V_s · sqrt(L_m / L_s) reproduces the wave-making resistance regime of the full-scale ship. The Froude number therefore controls:

- Wave-making and wave-breaking resistance prediction.
- Hull-form scaling and the comparison of vessels of different size on a like-for-like basis.
- The wave system signature used in seakeeping and wash studies.

## Variants

Three Froude-number variants recur in practice:

- **Length-Froude (Fn)** — the form above; the default in ship-resistance work.
- **Volumetric Froude (Fn∇)** — Fn∇ = V / sqrt(g · ∇^(1/3)), where ∇ is the displaced volume. Used when waterline length is ill-defined (planing craft, semi-displacement tugs, small fast craft). Savitsky's planing-hull work is parameterised in terms of Fn∇.
- **Depth-Froude (Fnh)** — Fnh = V / sqrt(g · h), where h is the local water depth. Critical at Fnh = 1, separating sub-critical (Fnh < 1) and super-critical (Fnh > 1) regimes; relevant for shallow-water resistance, ship-generated wash, squat, and canal/restricted-channel effects.

## Speed regimes

Length-Froude segregates hull-operating modes. Approximate regime bands (boundaries vary slightly by author):

| Regime | Fn band | Dominant physics | Reference |
|---|---|---|---|
| Displacement | Fn ≲ 0.4 | Buoyancy supports the hull; wave-making rises with speed; resistance dominated by friction at low Fn, wave-making becomes significant approaching the upper bound. | Tupper 5e; Molland, Turnock, Hudson |
| Semi-displacement (transitional, "hump") | ~0.4 < Fn < ~1.0 | Dynamic lift begins to contribute; a local resistance maximum ("hump") appears near Fn ≈ 0.5 where ship length is comparable to the generated wavelength. | Tupper 5e; Bertram |
| Planing | Fn ≳ 1.0 (length-Fn) or Fn∇ ≳ 3 (volumetric) | Dynamic lift supports most of the hull weight; resistance physics shifts from wave-making to a balance of friction on the wetted planing area and pressure drag. | Savitsky (1964) |

This regime distinction is the principal nuance missing from many short popular treatments of the Froude number, including the [Miah (2026)](../sources/miah-2026-froude-number.md) trigger source.

## The model-scale Froude/Reynolds dilemma

Geometric similitude requires matching every dimensionless governing group. For surface-piercing hulls the two relevant groups are Fn and the Reynolds number Rn = V · L / ν (ν = kinematic viscosity). At model scale λ = L_m / L_s:

- Matching Fn fixes the model speed at V_m = V_s · sqrt(λ).
- That model speed gives Rn_m / Rn_s = sqrt(λ) · λ = λ^(3/2), which is much smaller than the ship Rn for any λ < 1.

Fn and Rn therefore **cannot** be matched simultaneously at model scale in the same fluid. Standard practice is to run the model at Froude similitude (the wave pattern is preserved) and apply a friction-coefficient correction between model and ship using a flat-plate friction line — the ITTC 1957 model-ship correlation line is the canonical example. The residuary (wave-making + form) coefficient is scaled by Fn similarity; the frictional coefficient is corrected at the actual model and ship Rn values. This is the heart of the resistance-decomposition workflow detailed in [Ship Resistance Components](ship-resistance-components.md).

## Historical note

The Froude number is named for William Froude (1810–1879), whose towing-experiments on HMS *Greyhound* (1874) demonstrated the law of comparison: that the wave-making component of resistance scales geometrically when speeds are scaled by the square root of the length ratio. Froude's *Greyhound* paper, presented to the Institution of Naval Architects, established the rational basis for systematic model testing that the field still follows.

## Cross-References

- [Ship Resistance Components](ship-resistance-components.md) — frictional / wave-making / form decomposition and ITTC scaling.
- [Ship Resistance and Propulsion](resistance-propulsion.md) — parent router for the resistance/propulsion topic family.
- [Hull-Form Geometry](hull-form-geometry.md) — block, prismatic, midship coefficients that enter resistance estimation alongside Fn.
- [Seakeeping and Ship Motions](seakeeping.md) — Froude scaling also governs free-surface motion response.
- [Wave Theory and Spectra](wave-theory-and-spectra.md) — the linear-wave framework underlying wave-making resistance.

## Public references

The treatments below are the public-citable anchors for the material above. The LinkedIn trigger source is on the [Miah (2026)](../sources/miah-2026-froude-number.md) page and is **not** the anchor for any technical claim on this page.

- Tupper, E.C. (2013). *Introduction to Naval Architecture*, 5th edition. Butterworth-Heinemann. ISBN 978-0-08-098237-3. — General introductory treatment of Froude similitude, regime bands, and model-testing practice. (See in-wiki source: [Introduction to Naval Architecture](../sources/introduction-to-naval-architecture.md).)
- Lewis, E.V. (ed.) (1988). *Principles of Naval Architecture, Volume II: Resistance, Propulsion and Vibration*. The Society of Naval Architects and Marine Engineers (SNAME), Jersey City. ISBN 0-939773-00-2. — Authoritative reference for resistance decomposition and ITTC scaling. (See in-wiki source: [Principles of Naval Architecture, Vol II](../sources/principles-of-naval-architecture-volume-ii---resistance-propulsion-and-vibration.md).)
- Larsson, L. and Raven, H.C. (2010). *Ship Resistance and Flow*. SNAME Principles of Naval Architecture Series. ISBN 978-0-939773-76-3. — Modern resistance and CFD treatment within the PNA series. (See in-wiki source: [PNA Series — Ship Resistance and Flow](../sources/principles-of-naval-architecture-series-—-ship-resistance-an.md).)
- Bertram, V. (2012). *Practical Ship Hydrodynamics*, 2nd edition. Butterworth-Heinemann. ISBN 978-0-08-097150-6. — Working-engineer treatment of similitude, regime characterisation, and model-test extrapolation. (See in-wiki source: [Practical Ship Hydrodynamics](../sources/practical-ship-hydrodynamics.md).)
- Molland, A.F., Turnock, S.R., Hudson, D.A. (2017). *Ship Resistance and Propulsion: Practical Estimation of Ship Propulsive Power*, 2nd edition. Cambridge University Press. ISBN 978-1-107-14206-0. — Combined regime treatment for displacement, semi-displacement, and planing hulls.
- Savitsky, D. (1964). "Hydrodynamic Design of Planing Hulls". *Marine Technology*, Vol 1, No 1 (October 1964), pp 71–95. SNAME. — Canonical reference for planing-regime hydrodynamics and the volumetric-Froude parametrisation.
- Froude, W. (1874). "On Experiments with HMS *Greyhound*". *Transactions of the Institution of Naval Architects*, Vol XV. — Historical primary source establishing the law of comparison; in the public domain.
- ITTC Recommended Procedures, 7.5-02-02-01 *Resistance Test* (current revision). International Towing Tank Conference. https://ittc.info/. — Procedural anchor for Froude-scaled model-resistance testing and the ITTC 1957 friction-line correction.
