---
title: "Controllable-Pitch Propellers"
tags: [controllable-pitch-propeller, cpp, hub-sealing, marine-propulsion, od-box, combinator]
sources:
  - linkedin-lloyds-maritime-institute-2026-cpp-hub-sealing
  - principles-of-naval-architecture-volume-ii---resistance-propulsion-and-vibration
added: 2026-05-13
last_updated: 2026-05-13
see_also:
  - concepts/marine-propulsors.md
  - concepts/propeller-theory.md
  - concepts/resistance-propulsion.md
---

# Controllable-Pitch Propellers

## Scope

This page covers the **controllable-pitch propeller (CPP)** as a mechanism — hub layout, pitch-actuation, seawater-side sealing, control philosophy, and selection rationale. It expands the one-line CPP entry on [Marine Propulsors](marine-propulsors.md) into a dedicated concept page for the hub-sealing and control-mode detail that the propulsor-catalog page deliberately omits. Open-water performance (KT/KQ/J characteristics) lives on [Propeller Theory](propeller-theory.md) and applies to CPP with the additional dimension that the J-axis becomes a J–pitch-ratio surface.

Synonyms and near-synonyms in industry usage:

- **CPP** — controllable-pitch propeller. Canonical term in Carlton, PNA Vol II, ITTC procedures, and IACS rules.
- **CRP** — controllable / reversible-pitch propeller. Older usage emphasizing that astern thrust is achieved by pitch reversal rather than shaft-direction reversal.
- **VPP** — variable-pitch propeller. Colloquial; appears in popular and trade press. Functionally equivalent to CPP in modern usage.

Fixed-pitch propellers (FPP) are the constant-pitch counterpart and are covered in [Marine Propulsors](marine-propulsors.md).

## Mechanism

A CPP carries blades bolted to the hub through a **blade-foot mechanism** that allows rotation about the blade spindle axis. Pitch is varied by a hydraulically-actuated servo internal to the hub. Control oil pressure is supplied from an **oil-distribution box (OD-box)** mounted at the engine end of the shaft and conducted to the hub through internal passages in a hollow propeller shaft. A pitch-feedback line returns blade-angle telemetry to the bridge / engine-control room. Pitch sweeps continuously from forward (positive) through zero (neutral, no net thrust at any RPM) to astern (negative), enabling thrust reversal without shaft-rotation reversal.

The fundamental design trade against a fixed-pitch propeller:

- **CPP wins** for vessels operating significantly off the design point — tugs and offshore support vessels with frequent thrust-reversal duty, dynamic-positioning vessels requiring fine thrust control, ferries with rapid speed transitions, and twin-screw warships needing reverse without engaging an astern turbine. CPP also enables a shaft-driven generator (PTO) to operate at constant RPM while propulsion thrust is modulated by pitch.
- **FPP wins** at the design point on peak open-water efficiency, mechanical simplicity, weight, and acquisition cost. The CPP hub is larger (typically 0.28–0.35 of propeller diameter vs ~0.18 for FPP) which costs efficiency through reduced effective blade-root work.

## Hub sealing and seawater-side integrity

The CPP hub contains pressurized hydraulic oil at the inboard side of a dynamic rotating seal that interfaces directly with seawater. Hub-sealing integrity is the load-bearing reliability concern for CPP propulsion. Failure modes:

1. **Seawater ingress** through degraded or contaminated seals. Consequence chain: oil emulsification → loss of servo response → seizure or unintended pitch drift → potential thrust-control loss. Onboard symptom is rising water-in-oil from the OD-box drain.
2. **Hydraulic-oil discharge** to the seawater side through outboard seal-lip wear or fouling damage. When the hub charge is petroleum-based, this becomes a regulated discharge under MARPOL Annex I and, in US waters, the Vessel General Permit. The industry response has been a transition to **Environmentally Acceptable Lubricants (EALs)** — synthetic esters, polyalkylene glycols, or vegetable-oil-based fluids — for the hub charge of vessels operating in regulated waters.
3. **Seal-wear from fishing-gear / debris ingestion** abrading the dynamic seal. A specific risk for fishing vessels, OSVs, and any vessel operating in coastal debris fields.
4. **Pressure-loss events** (line rupture, OD-box failure) that drop hub charge pressure below ambient seawater hydrostatic pressure, reversing the seal pressure gradient and admitting seawater.

Modern dynamic-seal designs (lip-seal stacks with redundancy, air-purged or air-pressurized barrier-gas configurations, condition-monitoring on the seal cavity) are vendor-specific and outside the scope of this concept page; the textbook references below introduce the design space.

## Control modes

CPP allows two distinct propulsion-control philosophies:

- **Combinator mode** — engine RPM and propeller pitch are scheduled together along a lookup curve (the *combinator curve*) chosen to track a chosen engine operating line (typically peak fuel economy or peak power) as the vessel demands varying thrust. Combinator mode is the default for vessels without a constant-frequency shaft-driven generator.
- **Constant-RPM mode** — shaft RPM is held fixed (typical reason: the shaft drives a PTO alternator feeding ship's-service electrical load that needs constant frequency). Thrust is then modulated entirely by pitch. The propeller spends most of its life off the open-water peak-efficiency J–pitch combination, accepted as the price for eliminating a separate diesel-generator.

Selection of combinator vs constant-RPM mode is an integrated power-and-propulsion architecture decision, not a propeller decision.

## Class-society and procedural framing

- IACS Unified Requirement M68 covers propulsion shafting; the OD-box and hollow-shaft pitch-line geometry are governed by member-society rules (DNV, ABS, LR, BV, ClassNK, KR, RINA, BV, RS, IRS, CRS, PRS).
- ITTC Recommended Procedures cover propulsion testing including CPP at varying pitch.
- IMO MARPOL Annex I governs oil-content discharge limits; the US EPA Vessel General Permit (2013 revision and successors) imposed the EAL requirement for stern-tube and CPP-hub charges where the seal faces seawater.

These are named here as the routing framework; specific clauses, thresholds, and tables are not reproduced on this page and live (or will live) under the `engineering-standards/` corpus.

## Public references

- Carlton, J.S., *Marine Propellers and Propulsion*, 4th edition, Butterworth-Heinemann, 2018. ISBN 978-0-08-100366-4. The dedicated CPP chapter covers hub geometry, blade-foot mechanism, OD-box, and seal-design space.
- Lewis, E.V. (ed.), *Principles of Naval Architecture, Volume II — Resistance, Propulsion and Vibration*, SNAME, 1988. ISBN 0-939773-00-2. Already a source page in this wiki: [PNA Vol II](../sources/principles-of-naval-architecture-volume-ii---resistance-propulsion-and-vibration.md). Covers CPP in the propulsor chapters.
- Molland, A.F., Turnock, S.R., Hudson, D.A., *Ship Resistance and Propulsion: Practical Estimation of Ship Propulsive Power*, 2nd edition, Cambridge University Press, 2017. ISBN 978-1-107-14206-0. Covers propulsor selection including CPP and the design-point vs off-design trade.
- ITTC, *Recommended Procedures and Guidelines*, propulsion-test-procedure family. Public at https://www.ittc.info/.
- IACS, *Unified Requirement M68 — Propulsion Shafting*. Public at https://www.iacs.org.uk/.
- IMO, *MARPOL Annex I — Regulations for the Prevention of Pollution by Oil*. Public via IMO Document Library.
- US EPA, *Vessel General Permit (VGP) 2013*. Public at https://www.epa.gov/npdes/vessels-vgp.

## Cross-references

- [Marine Propulsors](marine-propulsors.md) — propulsor catalog; CPP is one row, this page is the expansion.
- [Propeller Theory](propeller-theory.md) — open-water KT/KQ/J performance; for CPP, J becomes a J–pitch-ratio surface.
- [Ship Resistance and Propulsion](resistance-propulsion.md) — parent router page.
- [Lloyd's Maritime Institute (2026) — CPP and Hub Sealing](../sources/lloyds-maritime-institute-2026-cpp-hub-sealing.md) — the trigger source for this page.
