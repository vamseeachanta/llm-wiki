---
title: "Mechanical Fatigue (HCF + LCF)"
slug: mechanical-fatigue
tags:
  - fatigue
  - hcf
  - lcf
  - sn-curve
  - vibration-fatigue
  - riser-fatigue
  - ffs-input
added: 2026-05-09
last_updated: 2026-05-10
domain: engineering-standards
sources:
  - standards/api-rp-571.md
  - standards/dnv-rp-c203.md
  - standards/bs-7608-fatigue-design.md
extraction_policy: metadata-and-doctrinal-synthesis
---

# Mechanical Fatigue (HCF + LCF)

> Concept anchor for the **stress-controlled cyclic-mechanical-loading damage family** that drives crack initiation and propagation in equipment subjected to vibration, pressure cycling, wave-induced motion, pump- and compressor-induced pulsation, and start-stop service. Sits between the [fatigue-design-and-assessment](fatigue-design-and-assessment.md) parent concept (which catalogues the methodology — S-N, FCG, hot-spot stress, Palmgren-Miner) and the [fitness-for-service](fitness-for-service.md) consumer (which uses FFS Part 14 + Part 9 to convert measured or postulated mechanical-fatigue damage into remaining-life). Companion to [thermal-fatigue](thermal-fatigue.md) (strain-controlled, ΔT-driven) and distinct from corrosion-fatigue (chemistry-amplified) and creep-fatigue (high-temperature time-at-load coupling). Routes into [api-rp-571](../standards/api-rp-571.md) (mechanism catalogue — fatigue §3 covers mechanical, thermal, and corrosion-fatigue variants), [dnv-rp-c203](../standards/dnv-rp-c203.md) (offshore S-N curves and hot-spot extrapolation), [bs-7608-fatigue-design](../standards/bs-7608-fatigue-design.md) (UK / Eurocode-aligned S-N catalogue), [dnv-rp-c210](../standards/dnv-rp-c210.md) (probabilistic fatigue methods), [fatigue-crack-growth](fatigue-crack-growth.md) (Paris-law sibling for the propagation phase), and the FCG-measurement basis in ASTM E647.

## What is mechanical fatigue?

**Mechanical fatigue** is cyclic mechanical loading — vibration, pressure cycling, wave-induced motion, pump-induced pulsation, reciprocating-cylinder cycling, and start-stop cycling — producing crack initiation and propagation at stresses well below the static yield strength. The damage accumulates at stress raisers (notches, weld toes, geometry transitions, surface flaws, machining marks) and progresses through three sequential stages: **crack initiation** at the most-stressed feature, **stable crack propagation** under repeated cycles, and **final failure** by net-section yielding, fast fracture, or plastic collapse once the remaining ligament cannot carry the peak load.

Mechanical fatigue is **distinct from thermal fatigue** in being **stress-controlled** rather than strain-controlled — the applied cyclic stress range is set by the imposed mechanical load, and the strain follows from the elastic constitutive response (mostly-elastic in HCF, plastic-dominated in LCF). It is **distinct from corrosion fatigue** in being chemistry-independent at first order, although seawater + cathodic-protection knock-downs are tabulated in offshore S-N catalogues as a parallel surface. It is **distinct from creep-fatigue** in being cycle-driven rather than time-at-temperature-driven, although the two interact in elevated-temperature cycled service per ASME B31.1 and ASME III NB-3221 time-fraction summation rules.

## HCF vs. LCF

Mechanical-fatigue regime is partitioned by total cycles to failure, with characteristic stress regimes and assessment methods:

| Regime | Cycles to failure | Stress regime | Method |
|---|---|---|---|
| **Low-Cycle Fatigue (LCF)** | 10² – 10⁵ | Plastic-strain dominated; cyclic stress-strain hysteresis loops with measurable plastic strain on each cycle | Coffin-Manson / Manson-Halford strain-life equations; multiaxial criteria for biaxial states |
| **High-Cycle Fatigue (HCF)** | 10⁵ – 10⁹ | Elastic-stress dominated; nominally-elastic response with localised plasticity at stress raisers only | Basquin / S-N curve fits with Palmgren-Miner damage summation; FCG (Paris) for postulated flaws |
| **Very-High-Cycle Fatigue (VHCF)** | > 10⁹ | Sub-surface inclusion-driven; failure originates at internal inclusions ("fish-eye" morphology) rather than surface | Newer modelling (Murakami √area, SWT-based VHCF criteria); gigacycle ultrasonic test rigs |

The HCF / LCF boundary at ~10⁵ cycles is conventional, not physical — the regime transition is driven by whether the stress-strain response on each cycle is mostly-elastic or plastic-dominated. VHCF emerged as a distinct regime once gigacycle test rigs (20 kHz ultrasonic resonance) demonstrated that "endurance limit" is not absolute for many steels and Ti-alloys; sub-surface inclusion-driven failures continue to occur beyond 10⁹ cycles at amplitudes below the conventional knee. Offshore service is dominated by HCF (wave-frequency cycling at ~0.1 Hz over 25-year design life ≈ 10⁸ cycles), while pressure-equipment start-stop cycling is LCF-dominant.

## S-N methodology — Wöhler 1860 to modern hot-spot stress

The S-N (stress-versus-life) framework traces to August Wöhler's 1860s railway-axle rotating-bending experiments at the Royal Prussian railways, which established that ferrous components fail at cyclic stress amplitudes well below the static yield strength and that the cycles-to-failure scale log-linearly with stress range over a finite-life regime — the original empirical observation that "fatigue" is a distinct failure mode. Basquin (1910) formalised the log-linear regime as `σ_a · N^k = C`, and Palmgren (1924) and Miner (1945) supplied the linear-damage-summation rule that generalises the constant-amplitude Basquin curve to variable-amplitude service.

Modern offshore and pressure-equipment S-N usage diverges from the original smooth-specimen Wöhler curves in three respects: **detail classification** (DNV-RP-C203 weld classes B1–W and BS 7608 classes B–W tabulate the S-N curve as a function of weld geometry and residual-stress regime, not as a base-metal property), **hot-spot stress extrapolation** (the geometric-stress concentration at a weld toe is captured by FE extrapolation of the surface stress to the toe at standardised distances 0.5t and 1.5t per IIW recommendations, separating geometric-stress from notch-stress), and **bilinear two-slope formulation** (the conventional knee at 10⁷ cycles transitions from a steeper finite-life slope to a shallower variable-amplitude slope, reflecting the empirical observation that VA service damages below the constant-amplitude endurance limit but at a reduced rate).

## Stress-cycle counting — rainflow + Markov chain + Palmgren-Miner

Variable-amplitude service produces an irregular stress-time history that must be reduced to a closed-loop range/mean histogram before damage summation. **Rainflow counting** per ASTM E1049 (Endo and Matsuishi 1968 origin) extracts hysteresis-closing cycle pairs by traversing the time history and pairing peaks and valleys that close in stress-strain space. The four-point algorithm (modern operational form) processes the time history in a single forward pass and emits each closed cycle's range, mean, and count to a 2-D histogram.

**Markov-chain cycle-counting** (transition-matrix approach) is an equivalent reduction for stationary stochastic stress histories — the joint-probability matrix of stress-state transitions feeds the same Palmgren-Miner damage summation. Offshore wave-frequency stress-time histories are commonly reduced via spectral methods (Dirlik, Tovo-Benasciutti) that close-form-approximate the rainflow histogram from the stress PSD, avoiding time-domain simulation altogether for narrow-banded or mildly-broad-banded processes.

**Palmgren-Miner linear damage summation** `D = Σ (n_i / N_i) ≤ 1.0` is the closure rule — at each histogram bin `i` with count `n_i` and S-N-curve-allowable `N_i` at that bin's range, the partial damage `n_i / N_i` accumulates linearly until `D = 1.0` triggers the design fatigue life. Real-world failure scatter at `D ≈ 1.0` spans roughly 0.3 to 3.0; design-fatigue-factor (DFF) margins of 3 to 10 (DNV-RP-C203 Table 5-3) absorb this scatter plus the other Class-IV uncertainties.

## Mean-stress effects — Goodman + Gerber + Soderberg + R-ratio

Constant-amplitude S-N curves are typically reported at fully-reversed (R = -1) loading, where R is the cyclic stress ratio `σ_min / σ_max`. Service stress states with non-zero mean (R ≠ -1) require a **mean-stress correction** to convert the applied range/mean pair to an equivalent fully-reversed range:

- **Goodman line** — linear interpolation in the (σ_a, σ_m) plane between the fatigue strength at zero mean (σ_a-allowable at R = -1) and the ultimate tensile strength σ_u on the static axis. Conservative for ductile metals at positive mean stress.
- **Gerber parabola** — quadratic in (σ_a, σ_m) with the same endpoint conditions; less conservative than Goodman, often a better fit for ductile-steel test data.
- **Soderberg line** — linear interpolation to the yield strength σ_y rather than σ_u; the most conservative of the three because the static endpoint is reduced.

For **welded details**, all three corrections are explicitly **suppressed** in DNV-RP-C203 and BS 7608 — the as-welded residual stress field is assumed to be tensile and yield-magnitude regardless of applied mean, so external mean-stress is already saturated and the constant-amplitude S-N curve applies at any applied R-ratio. Post-weld-heat-treatment (PWHT) and high-frequency mechanical impact (HFMI) treatments partially restore mean-stress sensitivity, with code-tabulated benefit factors. R-ratio dependence persists in FCG (Paris-law) integration via the Forman, Walker, and NASGRO closure-corrected forms — see [fatigue-crack-growth](fatigue-crack-growth.md).

## Welded-joint S-N classes

Weld-detail classification is the load-bearing abstraction in offshore and structural-steel fatigue codes — each detail is binned into a class, and the class indexes a constant-amplitude S-N curve with documented slope, intercept, knee, and bilinear extension:

- **BS 7608** — UK / Eurocode-parallel catalogue with classes B (highest, base-metal-grade) through W (lowest, fillet-weld with poor profile). Detail tables span ground butt welds, transverse butt welds, longitudinal load-carrying fillets, attachment welds, and tubular connections with chord-brace SCFs.
- **DNV-RP-C203** — offshore-service catalogue with classes B1, B2, C, C1, C2, D, E, F, F1, F3, G, T, W1, W2, W3. The T-class is a tubular-joint-specific curve calibrated against UK Department of Energy and HSE pooled offshore weld-test data. Environmental-modifier curves (in-air, seawater + CP, free-corrosion) are tabulated alongside the in-air baseline.
- **ASME BPVC III NB-3222 / NB-3653** — nuclear-Class-1-component fatigue design with smooth-specimen design fatigue curves (Langer fits) and explicit elastic-plastic-strain partition; weld-class concept is replaced by detail-specific stress-intensification factors (SIFs) and notch-fatigue strength reduction factors (K_f).
- **Eurocode 3 EN 1993-1-9** — civil/structural-steel fatigue design with detail categories indexed by ΔσC at 2×10⁶ cycles (e.g., 160, 140, 125, 112, 100, 90, 80, 71, 63, 56, 50, 45, 40, 36 MPa). Detail-category tables span riveted, bolted, welded, and base-metal details for bridges, cranes, and steel-frame structures.

## Multi-axial fatigue

Service stress states at offshore tubular joints, reciprocating-machinery cylinder ports, pulsation-loaded pump casings, and pressure-vessel nozzle/shell intersections are biaxial or triaxial, and uniaxial S-N or Coffin-Manson curves under-predict damage for non-proportional cycling (where principal-stress directions rotate during the cycle). Three critical-plane and equivalent-stress families dominate:

- **Sines criterion** — equivalent-stress on the octahedral shear plane combined with hydrostatic mean-stress; suitable for proportional biaxial loading in HCF.
- **Crossland criterion** — similar octahedral-shear basis with hydrostatic-stress amplitude rather than mean; better for non-proportional HCF.
- **Findley critical-plane** — searches the candidate-plane orientation that maximises a shear+normal-stress damage parameter on each plane; well-validated against torsion-tension test data and adopted in API 579 Annex 14B for plate/shell-with-attachment fatigue assessment.
- **Brown-Miller and Fatemi-Socie** — strain-based critical-plane methods for LCF and finite-life fatigue with non-proportional loading; used in pressure-equipment start-stop and reciprocating-cylinder service.

## Mini-case-study patterns

Worked-example patterns (synthesis only — no proprietary client data):

- **Offshore deck-girder topsides** — wave-frequency loading at ~0.1 Hz dominates a 25-year service life ≈ 8 × 10⁷ cycles. Detail-classification is per DNV-RP-C203 D, E, or F at full-penetration butt welds and longitudinal stiffener attachments; hot-spot stress is FE-extrapolated at 0.5t and 1.5t. Damage is summed via rainflow + Palmgren-Miner with DFF = 2 to 10 depending on accessibility for in-service inspection. Mitigation when DFF margin is exhausted: detail upgrade (E → D), grinding the weld toe, or HFMI treatment.
- **Pressure-vessel cyclic-load** — start-stop and pressure-test cycling at 10² to 10⁴ lifetime cycles is LCF-dominant. ASME III NB-3222 design-fatigue-curve assessment at the most-loaded nozzle/shell intersection uses elastic-plastic stress concentration factors and Coffin-Manson-style strain-amplitude inputs. Cumulative-damage factor (CUF) closure at 1.0 sets the scheduled-inspection or repair trigger.
- **Pipeline VIV** — vortex-induced vibration on free-spanning subsea pipeline per DNV-RP-F105. Modal analysis identifies cross-flow and in-line natural frequencies; lock-in occurs when reduced-velocity `V_R = U / (f_n · D)` enters the response window. Damage at the hot-spot is summed across modal contributions against a DNV-RP-C203 F1 or F3 weld-class S-N curve. Mitigation: span-shortening (rock-dump, mattress), strake fitment, or pipeline re-routing.
- **Ship structural longitudinals** — wave-frequency hull-girder bending plus local panel pressure-cycling drive longitudinal-stiffener fatigue at the bracket-toe and connection-detail. IACS Common Structural Rules (CSR) for bulk carriers and tankers prescribe direct-calculation hot-spot fatigue assessment with DNV-RP-C203 or BS 7608 weld-class S-N curves and a 25-year North-Atlantic wave-scatter histogram for damage summation.

## O&G mechanical-fatigue scenarios

Components in upstream and downstream service that experience cyclic mechanical loading drive a portfolio of mechanism / standards pairings:

| Service | Cycle source | Reference |
|---|---|---|
| Offshore platform topsides | Wave + wind cyclic loads | API RP 2A WSD; DNV-OS-C201 |
| Drilling riser | VIV (vortex-induced vibration) + heave + drilling vibration | API RP 16Q; DNV-RP-F204 |
| Production riser (flexible) | VIV + slug flow + thermal cycling | API Spec 17J + DNV-RP-F204 |
| Sub-sea jumper | Slug flow + thermal cycling | DNV-RP-F112; OS-F101 |
| Pipeline supports | Settlement + vibration | DNV-OS-F101 + DNV-RP-F105 |
| Pump suction/discharge | Pump-induced pulsation | API 610 |
| Reciprocating compressor | Pulsation + cylinder cyclic | API 618 |
| Heat-exchanger tube vibration | Flow-induced (TEMA shell-side) | TEMA + API 660 |
| Atmospheric tank | Wind-induced settling + filling/emptying cycles | API 650 + 653 |

The shared feature across the population is a **periodic mechanical excitation** — wave, vibration, pulsation, or pressure-cycle — coupled to a structural detail with a stress-concentration that initiates and grows fatigue cracks. Mitigation is mechanism-specific: mass tuning and damping for VIV, pulsation dampeners for reciprocating service, baffle redesign for HX tube-vibration, and weld-detail upgrades for offshore topsides.

## VIV — Vortex-Induced Vibration

Vortex-induced vibration is the dominant fatigue driver for slender deepwater members — TLP tendons, drilling and production risers, free-spanning pipelines, tubular jacket braces. Vortex shedding at the Strouhal frequency (St ≈ 0.18–0.22 for circular cylinders in the relevant Reynolds range) **locks-in** with the structural natural frequency when the two are within the lock-in band, producing sustained large-amplitude cross-flow oscillation and accelerated fatigue at the harmonic of the shedding frequency. In-line VIV at ~2× the cross-flow frequency adds a second damage channel.

DNV-RP-F105 (free-spanning pipelines) and DNV-RP-F204 (riser fatigue) provide the quantitative methods — modal analysis to identify candidate natural frequencies, hydrodynamic coefficients (added-mass, damping, lift) from public test campaigns, and a mode-superposition damage summation against a hot-spot S-N curve. Strake fitment and span-shortening are the standard mitigations; full elimination is rarely practical for long deepwater members.

## Modeling tools

The mechanical-fatigue analysis stack runs from new-build design through FFS remaining-life, with the choice of method driven by cycle-count regime and stress-state:

- **S-N + Palmgren-Miner (HCF)** — per [dnv-rp-c203](../standards/dnv-rp-c203.md) / [bs-7608-fatigue-design](../standards/bs-7608-fatigue-design.md) weld-class S-N curves with linear damage summation `D = Σ n_i / N_i`. Mean-stress correction (Goodman / Gerber / Soderberg) for non-welded details; for welded details, residual-stress is implicitly absorbed into the as-welded S-N curve and explicit mean-stress correction is suppressed. Bilinear two-slope formulation with the slope-change knee at the variable-amplitude endurance threshold.
- **FCG da/dN-vs-ΔK (HCF + LCF tail)** — Paris-law integration `da/dN = C(ΔK)^m` per ASTM E647 measurement methodology, integrated from initial postulated or NDE-detected flaw size `a₀` to critical size `a_crit` set by the toughness floor. Threshold ΔK<sub>th</sub> bounds the integration at low driving force; environmental modifiers (seawater + CP, sour service) are layered on the in-air baseline. Cross-link: [fatigue-crack-growth](fatigue-crack-growth.md).
- **Strain-life Coffin-Manson (LCF)** — `Δε_t / 2 = (σ'_f / E)(2N_f)^b + ε'_f (2N_f)^c` separating elastic (Basquin exponent b) and plastic (Coffin-Manson exponent c) strain-amplitude contributions. Useful for thermal- and mechanical-strain-controlled service with cycles in the 10²–10⁵ range, including pressure-equipment start-stop cycling and reciprocating-machinery cylinder service.
- **Multiaxial criteria** — Brown-Miller, Fatemi-Socie, Sines, Crossland, and Findley critical-plane methods extend uniaxial Coffin-Manson and S-N to **biaxial stress states** typical at offshore tubular joints, reciprocating-compressor cylinder ports, and pulsation-loaded pump casings. Critical-plane methods identify the plane of maximum damage and integrate the chosen damage parameter on that plane rather than on a scalar equivalent stress.
- **Rainflow + cycle-counting** — ASTM E1049 four-point algorithm extracts closed hysteresis loops from a variable-amplitude stress-time history; output is a histogram (range, mean, count) that feeds either S-N damage summation or FCG cycle integration. Standard for wave-frequency offshore service, irregular topsides loading, and reciprocating-machinery pulsation histories.
- **Probabilistic / reliability-based** — DNV-RP-C210 supplies probabilistic-fatigue methods with explicit uncertainty quantification on S-N intercept, slope, and Miner-sum closure, used when design-fatigue-factor margins are aggressive or when life-extension assessment beyond original design life is required.

Each method is calibrated against a specific cycle-count regime and stress-state assumption — mixing methods across regimes (e.g., applying high-cycle S-N curves to a single-event impact load) is unsafe.

## FFS

In-service mechanical-fatigue damage is assessed under [fitness-for-service](fitness-for-service.md):

- **API 579-1 / ASME FFS-1 Part 14** — *Assessment of Fatigue Damage*. Levels 1 / 2 / 3 fatigue-assessment surfaces. Level 1 is screening against the design fatigue life; Level 2 is S-N + Palmgren-Miner against a classified detail curve with documented operating-history cycle counts; Level 3 is FCG-based assessment with explicit crack-driving-force integration and toughness-floor closure. The FFS consumer for in-service vessel and piping equipment with documented mechanical-cycle history.
- **BS 7910 §7 (S-N) + Annex M (FCG)** — UK / Eurocode-parallel methodology for in-service crack-bearing components. §7 covers S-N-based fatigue assessment with classified-detail curves consistent with [bs-7608-fatigue-design](../standards/bs-7608-fatigue-design.md); Annex M provides Paris-law constants for ferritic / austenitic steels and aluminium, threshold ΔK<sub>th</sub>, environmental modifiers, and R-ratio handling. Cross-cited with [bs-7608-fatigue-design](../standards/bs-7608-fatigue-design.md) for the S-N companion and with the ASTM E647 measurement basis for the FCG inputs.

## Inspection

Mechanical-fatigue detection runs from operational monitoring through through-wall sizing:

- **Vibration monitoring** — accelerometers and DAS (distributed-acoustic-sensing) strain gauges on critical components (riser stress joints, compressor cylinders, pump casings, jacket-leg hot-spots) capture in-service excitation amplitudes against alarm thresholds calibrated from the design fatigue analysis.
- **Periodic UT / AET** on known fatigue hot-spots — UT (ultrasonic-testing) for conventional sizing; AET (acoustic-emission-testing) for active-crack-growth detection during pressure or load testing.
- **MT / PT (magnetic-particle / penetrant testing)** on weld toes — the dominant crack-initiation site for HCF in welded structures. MT/PT is the standard surface-NDE method during scheduled in-service inspection.
- **AUT / PAUT (automated and phased-array ultrasonic testing)** for through-wall propagation tracking of detected indications. The AUT/PAUT result is the FCG-input crack size for FFS Part 9 / Part 14 Level 3 assessment.

## Standards

Bidirectional cross-references — each standards page below should cross-link back to this concept page once the convention propagates.

- [dnv-rp-c203](../standards/dnv-rp-c203.md) — *Fatigue Design of Offshore Steel Structures.* Primary multi-edition S-N catalogue for offshore service: weld-classes B1–W, hot-spot extrapolation methodology, environmental modifiers (in-air, seawater + CP, free-corrosion), and design-fatigue-factor framework. The single most-cited offshore mechanical-fatigue code.
- [dnv-rp-c210](../standards/dnv-rp-c210.md) — *Probabilistic Methods for Planning of Inspection for Fatigue Cracks in Offshore Structures.* Probabilistic complement to RP-C203 supporting risk-based-inspection and life-extension assessment.
- [bs-7608-fatigue-design](../standards/bs-7608-fatigue-design.md) — *Code of Practice for Fatigue Design and Assessment of Steel Structures* (BSI). UK / Eurocode-parallel S-N catalogue with detail classes B–W; cross-cited from [bs-7910-flaw-assessment](../standards/bs-7910-flaw-assessment.md) Annex M as the S-N companion to FCG-based fatigue.
- [bs-7910-flaw-assessment](../standards/bs-7910-flaw-assessment.md) — *Guide to Methods for Assessing the Acceptability of Flaws in Metallic Structures.* §7 S-N assessment + Annex M FCG constants; the in-service consumer for crack-bearing components.
- **ASTM E647** — *Standard Test Method for Measurement of Fatigue Crack Growth Rates.* The primary measurement methodology for da/dN-vs-ΔK Paris-law constants used in FCG integration. Provides specimen geometries (CT, M(T), SEN(B)), data-reduction procedures, and threshold ΔK<sub>th</sub> determination.
- **ASTM E466** — *Standard Practice for Conducting Force-Controlled Constant-Amplitude Axial Fatigue Tests of Metallic Materials.* The smooth-specimen S-N test methodology supplying the base-metal Wöhler curves that anchor the welded-detail catalogues.
- **ASTM E739** — *Standard Practice for Statistical Analysis of Linear or Linearised Stress-Life (S-N) and Strain-Life (ε-N) Fatigue Data.* The statistical-fitting methodology converting smooth-specimen test data into design-curve mean and lower-bound forms.
- [api-rp-571](../standards/api-rp-571.md) — *Damage Mechanisms Affecting Fixed Equipment in the Refining Industry.* Mechanism-catalogue entry for fatigue (§3, mechanical / metallurgical class) covering mechanical, thermal, and corrosion-fatigue variants. Description, susceptible materials, critical operating factors, morphology, prevention, and inspection-technique recommendations are anchored here.
- **ASME BPVC III NB-3222 / NB-3653** — nuclear-Class-1 design fatigue curves and stress-intensification methodology; supplies the LCF design surface for nuclear pressure-vessel and piping components.
- **Eurocode 3 EN 1993-1-9** — civil/structural-steel fatigue design with detail-category-indexed S-N curves for bridges, cranes, and steel-frame structures.
- **DNV-RP-F204 / DNV-RP-F205** — riser-fatigue methodology; companion to DNV-RP-C203 for dynamic risers in VIV, wave-frequency, and slug-flow service. Already routed under standards/dnv-rp-c203.md / standards/dnv-os-f201.md cross-links; explicit standards pages are future-promotion candidates.
- **API 610 / API 618 / API 660** — pump, reciprocating-compressor, and shell-and-tube heat-exchanger standards covering pulsation-driven and flow-induced vibration design envelopes. Future-promotion candidates for first-class standards pages.
- **TEMA** — *Standards of the Tubular Exchanger Manufacturers Association.* Adjacent reference for HX shell-side flow-induced tube vibration design; pairs with API 660 for refining-service heat-exchangers.

## Related concepts

- [fatigue-design-and-assessment](fatigue-design-and-assessment.md) — parent concept; mechanical-fatigue inherits its assessment surfaces (S-N, FCG, Palmgren-Miner, hot-spot stress, mean-stress correction, environmental modifiers) directly.
- [fatigue-crack-growth](fatigue-crack-growth.md) — sibling concept; the propagation-phase Paris-law sibling that consumes the rainflow + ΔK driving-force input from the mechanical-fatigue stress history. The W222 iteration-48 reference for fatigue-domain density.
- [thermal-fatigue](thermal-fatigue.md) — sibling; strain-controlled, ΔT-driven fatigue with characteristic crazing morphology and LCF-regime cycle counts. The two concepts share methodology but partition on whether the load is stress- or strain-controlled.
- [fitness-for-service](fitness-for-service.md) — downstream consumer; FFS Part 14 governs in-service mechanical-fatigue assessment, with Part 9 governing FCG of detected crack-like flaws.
- [weld-toughness](weld-toughness.md) — Charpy and CTOD acceptance for weld procedure qualification; sets the toughness floor on the FCG `a_crit` closure for fatigue-cracked welds.
- [fracture-toughness-measurement](fracture-toughness-measurement.md) — K<sub>Ic</sub>, J-integral, CTOD test methods (ASTM E399 / E1820 / E1921 / BS 7448) supplying the toughness inputs that bound the FCG integration at `a_crit`.
- [brittle-fracture](brittle-fracture.md) — adjacent failure-mode concept; the toughness-floor exit condition for fatigue-driven crack growth into the unstable-fracture regime.

## Source materials

- [og-standards-api](../sources/og-standards-api.md) — API publisher catalog (RP 571, RP 2A-WSD, Std 579, RP 16Q, Spec 17J, RP 610 / 618 / 660 future-promotion).
- [og-standards-dnv](../sources/og-standards-dnv.md) — DNV publisher catalog (RP-C203, RP-C210, OS-F201, RP-F105, RP-F112, RP-F204 / F205 future-promotion).
- [og-standards-bsi](../sources/og-standards-bsi.md) — BSI publisher catalog (BS 7608, BS 7910).

## Notes

- This is a concept page, not a standards page. No clause text, S-N curve constants, Paris-law `C` and `m` values, Coffin-Manson exponents, design-fatigue-factor tables, or VIV hydrodynamic coefficients are reproduced here. For normative use, cite the publisher edition of DNV-RP-C203 / DNV-RP-C210 / BS 7608 / BS 7910 / ASTM E647 / E466 / E739 / API RP 571 / API 579-1 / ASME BPVC III / Eurocode 3 directly.
- The component / mechanism table is illustrative of typical upstream and downstream experience; actual susceptibility for any specific asset must consider as-built weld-detail classification, anchor and support condition, vibration history, and operating-cycle reconstruction from process logs.
- Mini-case-study patterns are synthesis-only doctrinal walkthroughs, not records of any specific project. They illustrate the standard analysis flow and the choice of method per regime; project-specific assessments must use as-built drawings, measured operating-history data, and an independent peer-reviewed FE model.
- The HCF / LCF / VHCF cycle-count partition is conventional; the regime boundaries depend on the material's cyclic stress-strain response and on the chosen failure criterion. VHCF behaviour for offshore steels remains an active research area and is not yet codified in DNV-RP-C203 or BS 7608.
- General engineering knowledge described above is paraphrased from public textbook sources (Suresh, *Fatigue of Materials*, 2nd ed., CUP 1998; Schijve, *Fatigue of Structures and Materials*, 2nd ed., Springer 2009; Almar-Næss, *Fatigue Handbook — Offshore Steel Structures*, Tapir 1985; Hertzberg, *Deformation and Fracture Mechanics of Engineering Materials*, 5th ed., Wiley 2012; Murakami, *Metal Fatigue: Effects of Small Defects and Nonmetallic Inclusions*, Elsevier 2002 for VHCF; Dowling, *Mechanical Behavior of Materials*, 4th ed., Pearson 2013 for mean-stress and strain-life formulations) and is independent of any vendor PDF in the deny-list catalogue.
