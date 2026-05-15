---
title: "Electric Submersible Pumps (ESP)"
tags: [esp, artificial-lift, centrifugal-pump, vfd, downhole-motor]
sources:
  - api-rp-11s
  - api-rp-11s2
  - api-rp-11s4
added: 2026-05-14
last_updated: 2026-05-15
---

# Electric Submersible Pumps (ESP)

## Scope

The ESP is a downhole multi-stage centrifugal pump driven by an electric motor and powered via armored cable from a surface variable-frequency drive (VFD). ESP dominates **high-rate** artificial lift — typical operating range 500-30,000 bbl/d with specialty units to 60,000+ bbl/d. The system has more failure modes than rod pump but produces vastly more fluid per well.

## System anatomy (bottomhole to surface)

1. **Motor** — induction motor, two-pole 60 Hz (3,500 RPM nominal); 480 V to 5,000 V depending on horsepower. Cooled by produced-fluid flow past the motor housing.
2. **Seal section (protector)** — separates motor oil from well fluid; equalizes pressure; absorbs thrust. See [API RP 11S7](../standards/api-rp-11s7.md).
3. **Intake** — bell-mouthed entry (standard) or rotary/vortex gas separator for high-GOR applications.
4. **Pump stages** — stack of impeller + diffuser pairs; each stage adds incremental head; total stages count drives total TDH.
5. **Pump head** — discharges into tubing; carries upper bearing.
6. **Cable splice** — connects motor pigtail to power cable; common failure point.
7. **Armored power cable** — clamped to tubing; runs to surface VFD via wellhead penetrator.
8. **Surface VFD** — variable-frequency drive provides RPM control + soft-start + real-time current/voltage telemetry.
9. **Surface choke** — controls pump discharge pressure; works with VFD to set operating point.

## Operating principle

VFD adjusts motor frequency → motor RPM → pump RPM (essentially linear). Pump head and flow rate scale via centrifugal-pump affinity laws: head ∝ RPM², flow ∝ RPM, power ∝ RPM³. This makes ESP unique among artificial-lift methods: rate is tunable in real time via VFD without pulling tubing.

## Strengths and weaknesses

| Strength | Weakness |
|---|---|
| Very high rate capacity (500-30,000+ bbl/d) | Cable failures dominate workover triggers |
| Compact downhole footprint | Intolerant of significant free gas at intake |
| Real-time VFD monitoring (current, voltage, frequency) | Intolerant of high solids / sand |
| Tunable rate without pulling | Mid-cost to high-cost CAPEX + OPEX |
| Works in deviated and horizontal wells (with appropriate intake placement) | Run-life typically 18-36 months (varies by service) |

## Cross-domain interactions

- **Reservoir pressure decline + IPR shifts** → re-sizing trigger (see [ESP Sizing](esp-sizing.md))
- **Free-gas at intake** → use rotary/vortex gas separator OR set intake below perforations
- **High-water-cut** → motor-cooling improves, but corrosion / scale considerations grow
- **HPHT** → motor temperature rating + insulation system + seal-section rating need upgrading

## Sand-handling — abrasive-sensitivity and screen-pump compatibility

ESPs are among the **most sand-intolerant** artificial-lift methods. Centrifugal-pump impellers and diffusers wear progressively against any abrasive (sand, scale, paraffin solids), and the failure mode is gradual head-degradation followed by mechanical seizure. Two operational considerations:

- **Sand-control completion type sets the ESP envelope.** Wells completed with frac-pack or gravel-pack architectures present near-zero produced-sand to the ESP intake under normal operation and are excellent ESP candidates. Wells completed with standalone screens present low-but-nonzero produced sand and require either a sand-tolerant ESP variant (abrasion-resistant stages, tungsten-carbide bearings) or a sand-tolerant lift method (PCP) instead. Wells with no sand control should not be completed with conventional ESP.
- **Sand-control completion failure is an ESP killer.** A breached gravel-pack or screen leaks formation sand at rates well above the ESP's design tolerance; impeller erosion accelerates and the pump fails within weeks-to-months. Operators monitoring ESP head-degradation curves should treat any sustained acceleration as a potential sand-control-completion-integrity signal.

The sand-control framework lives in a dedicated cluster: see [Sand Control](sand-control.md) for the architecture catalogue and decision framework, [Sand Control Screens](sand-control-screens.md) for the screen-family selection logic, and [Gravel Packing](gravel-packing.md) for gravel-pack completions that pair best with ESP.

## Perforation density and phasing — IPR coupling

The IPR curve that ESP sizing is built on is sensitive to **perforation skin**. The standard Karakas–Tariq decomposition makes shot density and phasing first-order inputs to the productivity index that flows directly into ESP head, stage count, and motor selection. Two operationally-relevant interactions:

- **Gas-separation at the pump intake** is degraded when perforations are too closely spaced above the intake (free gas does not have enough vertical distance to coalesce before entering the pump). Setting intake well below the lowest active perforation is the standard mitigation, but perforation policy upstream of completion influences how far below.
- **Re-perforation campaigns** are a common ESP-well intervention when IPR has decayed (skin growth, near-wellbore damage) — the ESP itself may be healthy, but the inflow has collapsed. Modelling the post-re-perforation IPR is the planning gate.

See [Perforation Strategy](perforation-strategy.md) for the shot-density / phasing / EHL framework that sets the IPR floor.

## Public references

- **API RP 11S family** — [api-rp-11s.md](../standards/api-rp-11s.md), [api-rp-11s1.md](../standards/api-rp-11s1.md), [api-rp-11s2.md](../standards/api-rp-11s2.md), [api-rp-11s4.md](../standards/api-rp-11s4.md), [api-rp-11s7.md](../standards/api-rp-11s7.md)
- **Takacs, Gabor** — *Electrical Submersible Pumps Manual*, Gulf Professional Publishing, 2e 2017 (ISBN 978-0-12-814570-8)
- **Brown, Kermit E.** — *The Technology of Artificial Lift Methods*, Vol 2b, PennWell 1980 (ISBN 0-87814-031-X)
- **Lyons (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, Elsevier (ISBN 978-0-7506-7785-1)
- **SPE OnePetro ESP literature** — gas-handling, sand-tolerance, HPHT-ESP applications

## Cross-references

- [Artificial Lift Overview](artificial-lift-overview.md) — production-engineering-side method-selection router
- [ESP Sizing](esp-sizing.md), [ESP Failure Modes](esp-failure-modes.md), [ESP Vendor Archetypes](esp-vendor-archetypes.md)
- [Perforation Strategy](perforation-strategy.md) — perforation density / phasing / EHL sets the IPR floor that ESP sizing depends on
- Drilling-engineering rod-pump cluster (cross-link for method-selection context): [Sucker-Rod Pumping Overview](../../../drilling-engineering/wiki/concepts/sucker-rod-pumping-overview.md), [Artificial-Lift Method Selection](../../../drilling-engineering/wiki/concepts/artificial-lift-method-selection.md)
