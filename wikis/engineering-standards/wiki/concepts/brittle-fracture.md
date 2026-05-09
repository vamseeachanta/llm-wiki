---
title: "Brittle Fracture and the Brittle-Ductile Transition"
slug: brittle-fracture
tags:
  - fracture-mechanics
  - brittle-fracture
  - transition-temperature
  - master-curve
  - charpy
  - dbtt
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
sources:
  - standards/astm-e1921.md
  - standards/api-std-579.md
---

# Brittle Fracture and the Brittle-Ductile Transition

## What is brittle fracture?

Brittle fracture is **sudden, low-energy fracture** in which a crack
propagates at a velocity approaching a substantial fraction of the
material's shear-wave speed with little or no measurable plastic
deformation ahead of the crack tip. In ferritic body-centred-cubic
(BCC) steels the operative micro-mechanism is **transgranular cleavage
on `{100}` planes**, triggered when the crack-tip stress field reaches
the cleavage strength of a critical micro-feature (typically a brittle
carbide or non-metallic inclusion) sampled by the high-stress volume
ahead of the crack. Macroscopically the fracture surface is faceted,
shiny, and **shows no shear lips**, and the absorbed energy in a
notched-bar test is a small fraction of the upper-shelf value.

Brittle fracture is contrasted with **ductile tearing**, in which
voids nucleate at second-phase particles, grow under hydrostatic
stress, and coalesce into a dimpled "cup-and-cone" fracture surface
that absorbs orders of magnitude more energy per unit area of crack
extension. The same material can exhibit either mode depending on
temperature, loading rate, constraint, and stress state — which is
why the **brittle-ductile transition** is treated as a population
property of the material-plus-loading combination, not a binary
property of the material alone.

The engineering significance of the brittle mode is **catastrophic
unstable propagation** in pressure-containing systems. The historical
case file is well-known: WWII Liberty-ship hull cleavage at low sea
temperature, the King's Bridge (Melbourne 1962) bridge-girder failure,
the Sayano-Shushenskaya turbine cover at low temperature, and the
classic reactor-pressure-vessel pressurised-thermal-shock (PTS)
analyses motivated by surveillance-capsule embrittlement. In each
case a small flaw in cold, constrained, high-stress material drove
end-to-end fracture before any leak-detection or pressure-relief
protection could intervene.

## The transition region

For ferritic structural steels the same set of test specimens, tested
across a temperature sweep, will trace out a **three-stage transition
curve** in three correlated outputs simultaneously:

- **Charpy V-notch absorbed energy** (`CVN`, J or ft·lbf) versus
  temperature — low and roughly constant on the lower shelf, rising
  steeply through the transition window, plateauing on the upper
  shelf at the fully-ductile micro-void-coalescence energy.
- **Lateral expansion** (`LE`, mm or mils) at the notch root — a
  geometric proxy for absorbed plastic work, transitions over the
  same window.
- **Fracture appearance** — the **percent-shear** read off the
  fracture surface (versus the brittle, faceted cleavage area)
  transitions from `0% shear` on the lower shelf to `100% shear` on
  the upper shelf.

All three curves shift in temperature when **loading rate** changes:
faster loading (impact, dynamic, shock) **raises** the transition
temperature, because cleavage is a stress-controlled mechanism and
strain-rate hardening pushes the crack-tip stress to the cleavage
threshold at a higher temperature. The same shift is observed for
**constraint** (thicker plate, deeper notches, plane-strain bending
all raise the transition) and for **microstructural embrittlement**
(temper embrittlement, neutron irradiation in reactor pressure
vessels, hydrogen exposure).

The three-stage Charpy curve is therefore not a property of the steel
in isolation, but of the steel-rate-constraint-environment combination.
This is the core reason that **fracture-mechanics-based** transition
descriptors ([[fracture-toughness-measurement]] via [[astm-e1921]])
have largely displaced bare Charpy correlations for safety-critical
service.

## Reference temperature concepts

A **reference temperature** is a single scalar that locates the
transition curve on the temperature axis, allowing materials to be
compared and design margins to be specified relative to a known
anchor. Several reference-temperature definitions coexist in current
standards:

**Charpy-based reference temperatures.**

- **`T27J` / `T41J` / `T50%-shear`** — the temperature at which
  Charpy V-notch absorbed energy reaches **27 J** (typical European
  ship-grade and pipeline criterion), **41 J** (typical North-American
  pressure-vessel criterion), or fracture appearance reaches **50%
  shear**. These are operational acceptance temperatures, not physical
  constants; the choice of threshold reflects the standard committee's
  calibration against historical service experience.
- **`NDT` — Nil-Ductility Transition** temperature per [ASTM E208]
  drop-weight test, the highest temperature at which a small,
  prescribed weld-bead-cracked specimen still propagates a brittle
  crack to one or both edges of the plate. NDT was the original
  reactor-pressure-vessel reference temperature underlying the
  legacy `RT_NDT` construction in ASME BPVC Section III / XI.
- **`DWTT` — Drop-Weight Tear Test** per API 5L Annex G (with
  laboratory roots also in NACE TM-0177-style impact testing), the
  pipeline-industry transition test for high-thickness line-pipe
  steels. DWTT reports the **shear-area transition temperature** at
  which `≥85%` of the fracture surface is shear, typically the
  contractual cold-temperature acceptance criterion for X65 / X70 /
  X80 line pipe.

**Master-curve-based reference temperature.**

- **`T₀`** per [[astm-e1921]] — the temperature at which the
  **median 1T-equivalent cleavage toughness `K_Jc(med)` equals
  `100 MPa·m^0.5`**, fitted by maximum likelihood from a small set
  of valid `K_Jc` data points using a fixed-shape Weibull
  distribution. `T₀` is a fracture-mechanics quantity (a toughness
  reference), not a Charpy-energy threshold, and it is the
  contemporary replacement reference temperature in ASME Code Cases
  N-629 / N-631 (`RT_T0 = T₀ + 19.4 °C`).
- **`T₁₀₀`** — informal shorthand for `T₀ + 50 °C`, the temperature
  at which the master-curve median toughness reaches roughly
  `200 MPa·m^0.5`. Used as a soft "comfortable upper-transition"
  anchor in some pressure-vessel and offshore acceptance specs.

**Pellini curves and FATT.** Earlier RPV practice used **Pellini
curves** (FAD-style plots of allowable stress versus `T − NDT`) and
the **fracture-appearance transition temperature (FATT)**, also
called the 50%-shear temperature, as the design anchor. These are
retained for backward compatibility but are superseded by master-curve
methodology for new construction and for life-extension assessment of
embrittled material.

## Why offshore and arctic infrastructure cares

For offshore, sub-sea, and arctic-class infrastructure the
governing material-selection driver is the **minimum design
temperature (MDT)** — the lowest metal temperature the structure can
credibly experience under any operating, transient, or upset
scenario. The fracture-toughness acceptance criterion is then almost
always specified at **`MDT − 10 °C`** (sometimes `MDT − 20 °C`) to
build in test-temperature margin against the natural population
scatter of small-specimen toughness data. This 10 °C floor appears
in DNV-OS-F101 (submarine pipelines), DNV-OS-C101 (offshore-steel
structures), API RP 2A (fixed offshore platforms), and the ABS /
DNV / class-society rule sets for ship and FPSO hulls.

Specific design choices it drives:

- **Hull plate grade selection** — IACS-harmonised ship-grade
  steels are graded **A / B / D / E** (mild) and **AH / DH / EH / FH**
  (higher-strength) by their **Charpy minimum at a specified test
  temperature**: A steels at `0 °C`, D at `−20 °C`, E at `−40 °C`,
  and **F at `−60 °C`**. F-grade plate is the default for
  arctic-service hull construction precisely because its specified
  Charpy floor sits below any credible plate temperature in service.
- **Arctic-class flow lines and jumpers** — sub-sea pipeline
  systems in the Beaufort Sea, Sakhalin, and the Barents Sea
  routinely specify **CTOD `≥ 0.20 mm` at `MDT − 10 °C`** on weld
  metal, HAZ, and parent-pipe coupons per DNV-OS-F101 ECA appendix.
  Master-curve `T₀` measurements on the same coupons increasingly
  replace blind CTOD acceptance.
- **Cold-stretch and crack-arrest sizing** — for high-pressure
  CO₂, ethylene, and LNG transport piping the design must
  demonstrate **crack arrest** (the toughness must outrun the
  decompression-wave-driven driving force) at the lowest credible
  in-service temperature; the calculation consumes the same
  master-curve lower-bound toughness used in the FFS Failure
  Assessment Diagram.
- **FPSO topside vessels and process piping** — local cold-spot
  temperatures (e.g., Joule-Thomson cooling at depressurisation
  blowdown) can drop well below ambient; **MAT screening** in
  [API 579-1 / ASME FFS-1 Part 3](../standards/api-std-579.md)
  identifies the pressure-temperature operating envelope and
  prescribes Charpy or master-curve toughness floors for
  in-service equipment that lacks original mill-test toughness
  records.

## Standards mapping

Each phenomenon and design-anchor concept above is operationalised
by one (or several) standards. The mapping is:

| Phenomenon | Standard | Method |
|---|---|---|
| `K_Jc` data + `T₀` | [ASTM E1921](../standards/astm-e1921.md) | Master-curve, multi-temperature Weibull fit |
| `K_Ic` plane-strain | [ASTM E399](../standards/astm-e399.md) | LEFM, narrow-scope SSY |
| `J–R` / CTOD-R | [ASTM E1820](../standards/astm-e1820.md) | Elastic-plastic, ductile-tearing |
| NDT temperature | ASTM E208 | Drop-weight Pellini |
| Charpy V-notch | ASTM E23 + ASTM A370 | Sub-size adjusted |
| DWTT pipeline | API 5L SR6 + API 5L Annex G | Three-quarter-thickness DWTT |
| Material grade | ABS Rules + DNV / class-society | Min-Charpy at design-`T_low` |
| FFS brittle screening | [API 579-1 / ASME FFS-1 Part 3](../standards/api-std-579.md) | MAT curves + exemption logic |
| ECA / FAD at low T | [BS 7910](../standards/bs-7910-flaw-assessment.md) | FAD Levels 1–3, Annex J brittle path |

The **upstream-downstream relationship** in this table is important:
ASTM E399 / E1820 / E1921 produce the **toughness data**, ASTM E208
/ E23 / A370 / API 5L Annex G produce the **transition-temperature
data**, and API 579-1 Part 3 / BS 7910 Annex J **consume** both as
inputs to the brittle-fracture screening or assessment that licenses
operation. Class-society rules and grade specifications are the
**procurement-side gate** that ensures the as-delivered material
clears the toughness floor before fabrication begins.

## Standards

Bidirectional links to standards pages whose normative content
governs the brittle-fracture assessment workflow:

- [[astm-e1921]] — *Master Curve and Reference Temperature `T₀`*.
  Primary fracture-mechanics reference-temperature method for
  ferritic steels in the transition region. See
  [`standards/astm-e1921.md`](../standards/astm-e1921.md).
- [[astm-e399]] — *Plane-Strain Fracture Toughness `K_Ic`*. The LEFM
  toughness regime that applies on the **lower shelf** of the
  transition curve, where small-scale yielding holds and `K_Ic`
  is the defensible toughness measure. See
  [`standards/astm-e399.md`](../standards/astm-e399.md).
- [[astm-e1820]] — *Measurement of Fracture Toughness*. The unified
  J / CTOD / J–R / δ–R method that applies on the **upper shelf**
  and into the upper transition where ductile tearing dominates;
  also produces the `K_Jc` data points consumed by E1921. See
  [`standards/astm-e1820.md`](../standards/astm-e1820.md).
- [[api-std-579]] — *Fitness-for-Service*. **Part 3** (Brittle
  Fracture) consumes Charpy and master-curve toughness inputs to
  derive the **Minimum Allowable Temperature (MAT)** screening
  curves and the operating pressure-temperature envelope; **Part 9**
  (Crack-Like Flaws) consumes E1820 / E1921 toughness for the FAD
  evaluation. See [`standards/api-std-579.md`](../standards/api-std-579.md).
- [[bs-7910-flaw-assessment]] — *Guide to methods for assessing the
  acceptability of flaws in metallic structures*. **Annex J** brittle-
  fracture procedure with FAD assessment at low temperature; accepts
  master-curve lower-bound toughness or Charpy-correlation inputs.
  See [`standards/bs-7910-flaw-assessment.md`](../standards/bs-7910-flaw-assessment.md).

## Related concepts

- [[fracture-toughness-measurement]] — companion concept page
  covering the laboratory-measurement side (`K_Ic`, `J_Ic`, `J–R`,
  CTOD, master-curve `T₀`) that produces the toughness inputs
  consumed by the brittle-fracture screening described here.
- [[fitness-for-service]] — downstream operational consumer; FFS
  Level 1 / 2 / 3 brittle-fracture assessment uses the reference
  temperatures and lower-bound toughness curves defined here.
- [[weld-toughness]] — weldment-specific sampling, HAZ targeting,
  and pipeline girth-weld ECA practice for brittle-fracture
  acceptance at low temperature.
- [[hydrogen-embrittlement]] — low-temperature hydrogen
  embrittlement and HISC overlap with brittle-fracture mechanics
  through their shared cleavage-initiation mechanism in BCC steels.
- [[arctic-design]] — system-level design-temperature philosophy,
  MDT derivation, and class-society mapping for arctic and
  cold-region infrastructure.

## Cross-wiki bridges

- [LNG Process Safety](../../../lng-projects/wiki/concepts/lng-process-safety.md)
  (lng-projects) — **bidirectional bridge**: cryogenic-temperature
  service is the dominant brittle-fracture driver for LNG containment
  and process piping. The Charpy / `T₀` / MDT-anchored toughness
  acceptance described here is what governs material selection for
  9% Ni inner tanks, Invar membranes, and stainless / aluminium
  cryogenic process piping under EN 1473 and NFPA 59A. The LNG
  process-safety page enumerates the release scenarios (pool fire,
  RPT, rollover) whose **upset-temperature transients** define the
  MDT that the brittle-fracture screening must clear.

## Source materials

- [`sources/og-standards-astm-e-series.md`](../sources/og-standards-astm-e-series.md)
  — catalog summary of the ASTM E-series fracture-mechanics test
  methods (E208, E399, E647, E1290, E1820, E1921, E813), including
  edition history. The bound metadata for E1921 / E399 / E1820
  cited above flow from this source page.
