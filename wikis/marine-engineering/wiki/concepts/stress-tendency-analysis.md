---
title: "Stress Tendency Analysis"
tags: [geomechanics, structural-geology, stress, faulting, fault-reactivation, reservoir]
sources:
  - morris-1996
  - ferrill-morris-2003
  - anderson-1951
  - sibson-1985
added: 2026-05-07
last_updated: 2026-05-07
---

# Stress Tendency Analysis

A geomechanical method for assessing the mechanical behavior of pre-existing
faults and fractures under a given stress state. Given an in-situ stress
tensor and a population of fault orientations, stress tendency analysis
computes per-orientation scalars that quantify how close each surface is to
slipping (slip tendency) and how close it is to opening as a fluid pathway
(dilation tendency). Used in reservoir geomechanics, fault-seal evaluation,
fluid-migration prediction, and induced-seismicity risk screening.

## Inputs

The analysis requires:

1. **Effective stress tensor** — principal stresses σ₁ ≥ σ₂ ≥ σ₃ and their
   orientations, with pore pressure subtracted from the total stress to give
   effective stresses (Terzaghi's principle).
2. **Fault/fracture orientations** — strike and dip of each surface to be
   evaluated. Often a population from seismic interpretation, FMI logs, or
   outcrop mapping.
3. **Friction coefficient μ** for slip-tendency thresholding (typical
   reactivation values μ = 0.6–0.85 per Byerlee's law; values down to 0.2
   are observed on weak phyllosilicate-rich faults).

## Slip Tendency

Slip tendency Tₛ on a planar surface is the ratio of resolved shear stress
to effective normal stress on that plane:

    T_s = τ / σ_n

where τ and σ_n are computed by resolving the effective stress tensor onto
the fault-plane normal. A surface is *prone to slip* when Tₛ approaches the
friction coefficient μ; surfaces with Tₛ ≥ μ are predicted to slip under
the current stress state.

Introduced as a quantitative reactivation indicator by Morris et al. (1996),
who demonstrated that mapping Tₛ over fault-orientation space identifies
critically stressed populations consistent with observed seismicity.

## Dilation Tendency

Dilation tendency Tₐ measures how close a surface is to opening (i.e.,
acting as a fluid pathway) under the current stress:

    T_d = (σ_1 - σ_n) / (σ_1 - σ_3)

bounded between 0 (surface normal aligned with σ₁ — least dilatant, most
compressed) and 1 (surface normal aligned with σ₃ — most dilatant). Surfaces
with high Tₐ are candidates for transmitting fluids; surfaces with low Tₐ
tend to seal.

The complementarity of Tₛ and Tₐ — high-slip surfaces are not necessarily
high-dilation surfaces — is the central operational insight: a fault can be
critically stressed for slip yet poorly oriented for fluid transmission, and
vice versa. Discussed in detail by Ferrill & Morris (2003) in the context
of dilational normal faults.

## Stress Regime Context (Andersonian Classification)

The orientation of σ₁, σ₂, σ₃ relative to vertical determines the
expected style of new faulting (Anderson 1951):

| Regime | Vertical principal stress | Expected fault style |
|--------|---------------------------|----------------------|
| Normal | σ₁ vertical | Normal faults dipping ~60° |
| Strike-slip | σ₂ vertical | Vertical strike-slip faults |
| Reverse / thrust | σ₃ vertical | Reverse faults dipping ~30° |

Stress tendency analysis is regime-aware: the same fault population yields
different Tₛ / Tₐ distributions under normal versus strike-slip versus
reverse stress states. *Evolving* stress states — e.g., basin inversion,
fluid injection, depletion-driven stress rotation — therefore change the
reactivation and fluid-pathway picture without any geometric change to the
fault network.

## Fault Reactivation

Pre-existing faults can slip at orientations that would not form new faults,
because they lack intact-rock cohesion (Sibson 1985). For a frictional
surface with cohesion ≈ 0, the Coulomb criterion τ ≥ μ σ_n reduces to the
slip-tendency criterion Tₛ ≥ μ. Reactivation therefore occurs on a wider
range of orientations than primary fracture, and is the dominant failure
mode in basins with structural inheritance.

## Operational Use

Typical workflow:

1. Build the effective stress tensor from leak-off, mini-frac, and pore-pressure
   data.
2. Project fault-plane orientations onto a stereonet or 3-D geometric model.
3. Compute Tₛ and Tₐ per orientation; threshold against μ for reactivation
   classification and against domain experience for fluid-pathway risk.
4. Re-run under perturbed stress states (depletion, injection, tectonic
   loading) to forecast reactivation and pathway evolution over time.

Typical applications:

- **Fault-seal analysis** for hydrocarbon traps — Tₐ identifies leak-prone
  fault segments.
- **CO₂ storage caprock integrity** — pre-injection Tₛ screening flags
  faults likely to slip under injection-driven pore-pressure rise.
- **Induced-seismicity risk** — wastewater-injection and EGS operations use
  Tₛ to identify critically stressed basement faults.
- **Wellbore stability** in fractured formations — Tₐ predicts fluid loss
  on drilling-induced or natural fractures intersecting the well.

## Limitations

- **Stress-state uncertainty dominates results.** σ₃ azimuth uncertainty of
  ±15° can flip a fault from "stable" to "critical." Sensitivity analysis
  over the stress-tensor uncertainty envelope is mandatory, not optional.
- **Assumes planar surfaces and homogeneous stress.** Does not capture
  stress concentrations at fault tips, segmentation, or geometric
  irregularity.
- **Friction coefficient is not universal.** Phyllosilicate-rich faults
  reactivate at μ well below Byerlee's law; using μ = 0.6 by default
  overestimates stability for clay-smear and shale-gouge zones.
- **Pore pressure feedback is dynamic.** Slip can dilate the fault, drop
  pore pressure, and arrest itself; modeling this requires hydro-mechanical
  coupling beyond static stress tendency.

## Primary References

- Anderson, E.M. (1951). [*The Dynamics of Faulting and Dyke Formation*, 2nd
  ed.](../sources/anderson-1951-dynamics-of-faulting.md) Oliver & Boyd,
  Edinburgh. — canonical stress-regime / fault-style classification.
- Morris, A.P., Ferrill, D.A., & Henderson, D.B. (1996). ["Slip-tendency
  analysis and fault reactivation."](../sources/morris-ferrill-henderson-1996-slip-tendency.md)
  *Geology*, 24(3), 275-278.
  doi:[10.1130/0091-7613(1996)024<0275:STAAFR>2.3.CO;2](https://doi.org/10.1130/0091-7613(1996)024%3C0275:STAAFR%3E2.3.CO;2)
  — original slip tendency formulation and reactivation interpretation.
- Sibson, R.H. (1985). ["A note on fault reactivation."](../sources/sibson-1985-fault-reactivation.md)
  *Journal of Structural Geology*, 7(6), 751-754.
  doi:[10.1016/0191-8141(85)90150-6](https://doi.org/10.1016/0191-8141(85)90150-6)
  — frictional reactivation criterion for cohesionless pre-existing surfaces.
- Ferrill, D.A. & Morris, A.P. (2003). ["Dilational normal faults."](../sources/ferrill-morris-2003-dilational-normal-faults.md)
  *Journal of Structural Geology*, 25(2), 183-196.
  doi:[10.1016/S0191-8141(02)00029-9](https://doi.org/10.1016/S0191-8141(02)00029-9)
  — dilation tendency in normal-faulting regimes and slip/dilation
  complementarity.

## Cross-References

- **Related concept**: [[mooring-line-failure]] — distinct, but shares the
  general pattern of stress-state-driven failure assessment under
  uncertainty.
- **Cross-wiki (engineering)**: stress-tendency analysis is also relevant
  to onshore reservoir geomechanics; if/when an `engineering` concept page
  on reservoir geomechanics is authored, link here.
- **Source-stub seam**: the legacy ingest stub at
  `sources/deepwater-geomechanics-model.md` is a batch-ingest placeholder
  for a vendor-derivative deepwater geomechanics paper; this concept page
  is the properly-cited replacement for the *methodology* portion of that
  topic.
