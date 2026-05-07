---
title: "Wave Shoaling and Depth-Dependent Loading"
tags: [metocean, wave-shoaling, breaking-waves, hs-thresholds, operational-limits, shallow-water, offshore, foundations]
sources:
  - rotzer-2026-wave-shoaling-depth-dependent
added: 2026-05-07
last_updated: 2026-05-07
---

# Wave Shoaling and Depth-Dependent Loading

The phenomenon by which a wave train transforms as it propagates from deeper into shallower water — slowing, shortening, steepening, and ultimately breaking — and the corresponding regime change in load character that the transformation imposes on fixed structures, foundations, and vessels operating in the 20–50 m water-depth band.

The practical consequence: **a single Hs-based operational-limit threshold does not represent equal risk across regions of differing water depth.** A 2.5–3.0 m Hs cutoff calibrated for deeper water can describe a materially more hazardous condition in the shallower parts of the same regional sea.

## Core kinematics

As a wave enters shallower water, four changes occur simultaneously:

| Quantity | Direction | Mechanism |
|---|---|---|
| Celerity (wave speed) | Decreases | Phase speed becomes depth-limited as `kh` falls below the deep-water threshold |
| Wavelength | Shortens | Period is conserved while celerity drops, so wavelength tracks celerity |
| Wave height | Can increase | Energy is redistributed into a shorter wavelength; height grows until breaking limits it |
| Wave profile | Steepens | Crest sharpens and trough flattens as nonlinearity grows |

The transformation is continuous and reversible-by-depth — a wave that re-enters deeper water relaxes back toward its prior kinematics — until it crosses the breaking threshold.

## Breaking threshold

At a depth-and-steepness combination the wave becomes unstable and breaks. The transition is **not** a smooth scaling. Pre-break, the wave loads a fixed structure or moored vessel with relatively smooth, rolling forces whose magnitude scales predictably with height. Post-break, the wave delivers short-duration impact loads whose peak magnitude can be **several times higher** than non-breaking waves of the same height.

The implication for design and for operational decision-making is that a structure's exposure regime can change abruptly across a small change in water depth, sea state, or tide, even with a held-constant nominal Hs.

## The Hs-threshold caveat

Operational-limit-setting frequently uses a single Hs cutoff (e.g. 2.5–3.0 m) to gate vessel transfers, foundation operations, or crew movements. That cutoff is implicitly calibrated to a wave kinematic regime — typically a deep-water reference where shoaling and breaking are not active. Transferring the same numeric cutoff to a shallower part of the same regional sea, without adjusting for the depth-induced regime change, can underweight the breaking-wave impact-load hazard the structure actually faces.

Practical zone where this matters most: structures, foundations, and vessels in the **20–50 m water-depth band**, e.g. fixed-bottom offshore wind foundations, jack-up legs, and shallower fixed jackets.

## Public references

The Rötzer essay is the trigger for this page; the technical anchors below are the public, citable references that ground the kinematics, the breaking-wave-force regime change, and the depth-dependent design treatment.

- **USACE Coastal Engineering Manual (CEM), EM 1110-2-1100.** US Army Corps of Engineers, Coastal and Hydraulics Laboratory. Public-domain technical manual; Part II (Coastal Hydrodynamics) covers shoaling and breaking, and Part VI (Design of Coastal Project Elements) covers wave-load design including breaking-wave force on piles and walls. Available via [USACE Publications](https://www.publications.usace.army.mil/USACE-Publications/Engineer-Manuals/) — search EM 1110-2-1100.
- **Wienke, J. & Oumeraci, H. (2005).** "Breaking wave impact force on a vertical and inclined slender pile — theoretical and large-scale model investigations." *Coastal Engineering*, 52(5), 435–462. DOI: [10.1016/j.coastaleng.2004.12.008](https://doi.org/10.1016/j.coastaleng.2004.12.008). Canonical reference for the slamming-load regime change on offshore wind monopiles in the 20–50 m water-depth band; quantifies the impact-vs-quasi-static decomposition the Rötzer essay describes qualitatively.
- **Dean, R.G. & Dalrymple, R.A. (1991).** *Water Wave Mechanics for Engineers and Scientists.* Advanced Series on Ocean Engineering, Vol. 2. World Scientific. Standard textbook treatment of shoaling, refraction, and the linear-wave-theory baseline this concept page critiques as non-transferable to shallow water.
- **Goda, Y. (2010).** *Random Seas and Design of Maritime Structures*, 3rd ed. Advanced Series on Ocean Engineering, Vol. 33. World Scientific. Definitive reference for random-wave breaking, depth-limited Hs distributions, and design-load formulations under shoaling/breaking conditions.
- **Battjes, J.A. & Janssen, J.P.F.M. (1978).** "Energy loss and set-up due to breaking of random waves." *Proceedings of the 16th International Conference on Coastal Engineering* (Hamburg). The classic random-wave-breaking dissipation model, still embedded in operational shallow-water spectral wave models (SWAN and successors).

The Rötzer essay's "Hs cutoff doesn't transfer across depths" critique is consistent with — and operationally framed by — the random-wave-breaking depth-limit treatment in Battjes & Janssen 1978 and Goda 2010, and with the breaking-wave impact-force regime change quantified by Wienke & Oumeraci 2005.

## Cross-references

- **Source**: [Rötzer (2026) — Why a 3 m Wave Doesn't Mean the Same Everywhere](../sources/rotzer-2026-wave-shoaling-depth-dependent.md)
- **Related concept**: [Long-Period Swell & Resonance](long-period-swell-resonance.md) — distinct mechanism: period-driven resonance amplification at very low amplitude, not depth-driven shoaling
- **Related concept**: [LNG Berth Operability](lng-berth-operability.md) — operability framing where Hs-based uptime decisions are made and where this caveat applies directly
- **Related concept**: [Stability in Waves](stability-in-waves.md) — vessel-response side of the wave-condition operability question
- **Cross-wiki (engineering-standards)**: [DNV-RP-C205 — Environmental Conditions and Environmental Loads](../../../engineering-standards/wiki/standards/dnv-rp-c205.md)
- **Cross-wiki (engineering-standards)**: [API-RP-2MET — Derivation of Metocean Design and Operating Conditions](../../../engineering-standards/wiki/standards/api-rp-2met.md)
- **Cross-wiki (engineering-standards)**: [ISO 19901-1 — Metocean Design and Operating Considerations](../../../engineering-standards/wiki/standards/iso-19901-1.md)
- **Cross-wiki (engineering)**: [Wave Theory for Offshore Engineering](../../../engineering/wiki/concepts/wave-theory-offshore.md) — wave-spectra and linear-wave-theory anchor for the deep-water baseline this page critiques as non-transferable
