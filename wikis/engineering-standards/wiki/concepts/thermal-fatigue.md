---
title: "Thermal Fatigue"
slug: thermal-fatigue
tags:
  - thermal-fatigue
  - low-cycle-fatigue
  - lcf
  - thermal-shock
  - mixing-tee
  - davis-besse
  - bypass-leakage
  - refinery
  - ffs-input
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
sources:
  - standards/api-rp-571.md
  - standards/api-std-579.md
---

# Thermal Fatigue

> Concept anchor for the **temperature-driven cyclic-strain damage family** that drives crack initiation and propagation in equipment subjected to thermal gradients, thermal cycling, and constraint. Sits between the [[damage-mechanism-screening]] catalogue (which flags thermal fatigue as credible for cycled equipment with restrained thermal expansion) and the [[fitness-for-service]] FFS Part 14 fatigue assessment that quantifies remaining life from a measured or postulated damage state. Distinct from [[fatigue-design-and-assessment]] in being **strain-controlled** (driven by ΔT × restrained-thermal-expansion-strain) rather than stress-controlled, and from [[creep-and-stress-rupture]] in being cycle-driven rather than time-at-temperature-driven (though the two interact in high-temperature cycled service). Routes into [[api-rp-571]] (mechanism description and morphology) and [[api-std-579]] Part 14 (Level 2 S-N and Level 3 FCG fatigue assessment for low-cycle service).

## What is thermal fatigue?

**Thermal fatigue** is cyclic mechanical strain induced by **temperature gradients**, **temperature cycling**, and **constraint** producing low-cycle-fatigue (LCF) crack initiation and propagation. The damage is driven by the differential thermal expansion of restrained material — when a component cannot freely expand or contract in response to a temperature change, the imposed strain is converted into mechanical stress. Repeated heating and cooling cycles accumulate plastic strain at stress raisers (notches, weld toes, geometry transitions, anchor points), and crack initiation follows on a strain-life rather than a stress-life surface.

Thermal fatigue is **distinct from purely mechanical fatigue** in three load-bearing ways. First, it is **strain-controlled**: the thermal expansion strain is imposed by ΔT and α (coefficient of thermal expansion); the stress at the constrained section is whatever the constitutive law produces at that strain, often well into the plastic range on each cycle. Second, the cycle counts are **low** — thousands or tens of thousands of cycles over a service life, versus millions for wave-frequency or rotating-machinery fatigue. Third, the **morphology** is characteristic: thermal fatigue often produces **multiple parallel cracks** ("crazing" or "elephant-skin" pattern) rather than a single dominant crack, because the strain field at the constrained surface drives initiation across a population of nominally-similar stress raisers more or less simultaneously.

Cracks initiate at the surface where the thermal gradient is sharpest (typically the inner-diameter wall of pressure equipment exposed to a fluid-temperature swing), propagate inward, and may link or branch as they progress through the wall. Through-wall propagation is the terminal state and is the trigger for [[fitness-for-service]] FFS Part 9 / Part 14 assessment.

## Three thermal-fatigue regimes

Thermal-fatigue damage is produced by three operationally-distinct loading regimes, each with its own characteristic ΔT, frequency, and crack-initiation envelope:

1. **Steady-state ΔT cycling.** Equipment cycled between two operating temperatures — start-up and shutdown of refinery units, batch-process reactors, equipment cycled between standby and operating mode. Cycle frequency is on the order of cycles per day to cycles per month. Total cycle count over life is **thousands to tens of thousands**. Strain per cycle is moderate. Crack initiation is gradual and dominated by the cumulative LCF damage at the most-strained section. The dominant regime for refinery-unit cycle-fatigue assessment.
2. **Thermal shock.** Sudden ΔT > approximately **100 °C** from upset events — boiler-feed-water injection into a hot reactor, cold start-up of a turbine into a hot casing, depressuring blow-down on a hot vessel, fire-water spray on hot piping. Strain in a single event can be very high, and crack initiation can be **faster** than under steady-state cycling because each upset cycle consumes a disproportionate fraction of the LCF strain budget. Damage accumulates in the upset-history rather than the design-cycle history; FFS practitioners must reconstruct upset frequency from operating logs.
3. **Mixing-tee thermal striping.** Hot and cold streams co-flow at a piping or vessel-nozzle junction with imperfect mixing, producing **high-frequency temperature fluctuation at the wall** — frequencies are typically in the **Hz range** (1–10 Hz) and amplitudes can be tens of degrees. The physics is different: the cycle count over a service life is **very high** (10⁸ to 10⁹ cycles), and the damage mechanism is closer to high-cycle stress-amplitude fatigue at the wall surface than to LCF. Mixing-tee thermal striping is the mechanism behind the **Davis-Besse RPV head 2002** event archetype and is the canonical example of bypass-leakage thermal-fatigue at process-stream injection points and let-down valves.

The three regimes overlap operationally — a reactor inlet sees both steady-state ΔT cycling at start-up / shutdown and thermal-shock from upset feedwater injection. The FFS practitioner partitions the service history by regime before assigning damage shares to each mechanism.

## Where thermal fatigue bites in O&G

Components that experience either restrained thermal expansion under cyclic temperature, sharp thermal gradients on transient events, or wall-temperature striping at flow-mixing interfaces drive the upstream and downstream thermal-fatigue portfolio. Representative service examples:

| Equipment | Mechanism |
|---|---|
| Atmospheric crude-tower transfer line | Start / shutdown ΔT 25–340 °C cycling |
| Hydroprocessing reactor inlet | Start / shutdown + upset thermal shock |
| Mixing tee at injection points | Thermal striping at flow boundary |
| Boiler steam-drum nozzles | Start / shutdown thermal-stress amplification at nozzle-to-shell junction |
| FCC slide-valve actuator | Cyclic thermal-strain at hot-cold interface |
| Furnace tube-stub | Cyclic creep + thermal fatigue interaction at radiant-section transition |
| Pressure-vessel anchor saddles | Thermal-restraint at the saddle amplifies anchor stress on every cycle |
| LNG-cryogenic pipeline anchor | Cold thermal-shock + thermal cycling at anchor and at insulation discontinuities |
| Davis-Besse RPV head 2002 | Boric-acid + cooled-leak driven thermal cycling — landmark case study for bypass-leakage thermal-fatigue |

The shared feature across the population is **constraint** — every example involves a geometric or anchor feature that prevents the cyclic thermal strain from being absorbed by free expansion. Where constraint is removed (free-floating components, well-designed expansion loops, sliding supports working as intended), thermal-fatigue susceptibility drops sharply.

## Modeling tools

The thermal-fatigue analysis stack runs from new-build code-compliance through FFS remaining-life:

- **ASME BPVC NB / VIII Div 2 fatigue analysis** — cumulative usage factor (CUF) computed by Lemaitre-style damage summation, with mean-stress correction (Sines / Goodman) layered on the strain-amplitude calculation. The reference methodology for new-build vessels in cyclic thermal service.
- **API 579-1 Part 14 fatigue assessment** — Level 2 (S-N) for screening with classified detail curves and Level 3 (FCG) for postulated or detected crack-like flaws under combined thermal and mechanical loading. The FFS consumer for in-service equipment with documented thermal-cycle history.
- **Coffin-Manson + Manson-Halford strain-life equations** for LCF — separates elastic and plastic strain-amplitude contributions with material-specific Coffin-Manson exponents (b for elastic, c for plastic). The methodology of choice when total strain per cycle is plastic-dominated, which is typical for thermal-shock and steady-state ΔT cycling at constrained sections.
- **Multiaxial-fatigue criteria** — Brown-Miller, Fatemi-Socie, and related critical-plane methods extend uniaxial Coffin-Manson to the **biaxial thermal-stress states** typical at nozzle-to-shell junctions, mixing tees, and anchor supports. Critical-plane methods identify the plane of maximum damage and integrate Coffin-Manson on that plane rather than on a scalar equivalent stress.
- **Computational FE-driven cycle counting** — full-history thermal-stress reconstruction via transient FE coupled with **rainflow filtering** of the resulting stress-time history (ASTM E1049 four-point algorithm). The output histogram (range, mean, count) feeds either S-N damage summation or FCG cycle integration, depending on whether the assessment is for screening or remaining-life.

Each method is calibrated against a specific cycle-count regime and stress-state assumption — mixing methods across regimes (e.g., applying high-cycle S-N curves to a thermal-shock event) is unsafe.

## Inspection

Thermal-fatigue detection is multi-modal and progresses from surface-pattern reconnaissance to through-wall sizing:

- **Visual inspection** for the characteristic crazing / elephant-skin pattern on the surface most exposed to the thermal swing. The presence of multiple parallel cracks at sub-millimetre spacing is diagnostic of thermal-fatigue origin versus mechanical-fatigue origin.
- **MT (magnetic-particle) and PT (penetrant) testing** for surface-cracks at known stress raisers — weld toes, geometry transitions, anchor points, nozzle-to-shell junctions.
- **AUT / PAUT (automated and phased-array ultrasonic testing)** for through-wall progression of detected indications. The AUT/PAUT result is the FCG-input crack size for FFS Part 9 / Part 14 Level 3 assessment.
- **Replication metallography** where through-wall progression is shallow and access permits — distinguishes thermal-fatigue cracking (multiple parallel transgranular cracks at the surface, often with oxide-filled tips) from creep cavity (intergranular voids), where the two mechanisms are coupled, both must be characterised separately.
- **Thermography during operation** where access permits and the thermal gradient is visible from outside — captures hot-spot striping at mixing tees and confirms the postulated thermal-cycle pattern against the as-built geometry.

## Standards

Bidirectional cross-references — each standards page below should cross-link back to this concept page once the convention propagates.

- [[api-rp-571]] — *Damage Mechanisms Affecting Fixed Equipment in the Refining Industry.* Mechanism catalogue entry for thermal fatigue (mechanical / metallurgical class). Description, susceptible materials, critical operating factors, morphology (crazing pattern, multiple parallel cracks), prevention, and inspection-technique-recommendations are anchored here.
- [[api-std-579]] — *Fitness-for-Service.* Part 14 *Assessment of Fatigue Damage* covers LCF assessment via Level 2 S-N and Level 3 FCG, with thermal-loading inputs handled per the operating-history reconstruction guidance. Part 9 *Assessment of Crack-Like Flaws* governs the FCG integration for detected thermal-fatigue cracks.
- [[asme-b31-1]] — *Power Piping.* Section governs cyclic-temperature service for power-plant piping, with stress-range reduction factors and displacement-stress allowables that bound the new-build envelope for piping in thermal-cycle service.
- [[asme-b31-3]] — *Process Piping.* **Appendix W** *Cyclic Service* governs displacement-stress and thermal-cycle assessment for process-piping in refining and petrochemical service. Reference for new-build and re-rating.
- [[asme-bpvc-viii-1]] — *Pressure-Vessel Construction (Design-by-Rule).* Allowable stress and design-margin envelope for new-build vessels in cyclic thermal service; cyclic-fatigue acceptance flows through to VIII-2 for Class 1 and high-cycle applications.
- [[asme-bpvc-viii-2]] — *Pressure-Vessel Construction (Design-by-Analysis Alternative Rules).* Stress-classification and CUF methodology for design-by-analysis vessels in cyclic thermal service. The new-build companion to FFS Part 14 for in-service assessment.
- **API RP 941** — *Steels for Hydrogen Service at Elevated Temperatures and Pressures (Nelson curves).* Cross-cuts at high-temperature thermal cycling for hydroprocessing-reactor shells where HTHA and thermal fatigue can be co-credible. Future explicit cross-link candidate.
- **ASME III NB-3000** — *Nuclear Pressure-Vessel Construction (Class 1).* The most rigorous published thermal-fatigue methodology in the ASME catalogue, including transient classification, fatigue strength reduction factors, and creep-fatigue interaction rules for elevated-temperature components. Future first-class standards page candidate for cross-domain reference.

## Related concepts

Wikilinks below point to concept pages — leave as wikilinks where the page does not yet exist, per the spinout's link-and-fill convention.

- [[fatigue-design-and-assessment]] — parent concept; mechanical-fatigue methodology framework (S-N, FCG, Palmgren-Miner, hot-spot stress) from which thermal-fatigue inherits the assessment surfaces and adapts them to strain-controlled LCF cycles.
- [[fitness-for-service]] — downstream consumer; FFS Part 14 governs in-service thermal-fatigue assessment, with Part 9 governing FCG of detected crack-like flaws.
- [[damage-mechanism-screening]] — upstream concept; flags thermal fatigue as credible for cycled equipment with restrained thermal expansion and routes the asset into the API RP 571 / API 579 Part 14 catalogue pair.
- [[creep-and-stress-rupture]] — paired high-temperature mechanism; **creep-fatigue interaction** is governed by ASME B31.1 / B31.3 time-fraction summation and by ASME III NB-3221 for the most rigorous treatment. Where steady-state ΔT cycling overlaps with creep-range service (furnace tube-stubs, hydroprocessing-reactor inlets), the two mechanisms must be assessed jointly rather than independently.
- [[brittle-fracture]] — paired low-temperature mechanism; cold thermal-shock at low T can drive a postulated crack-like flaw into fast-fracture rather than fatigue-crack-growth, particularly for ferritic steels below the ductile-brittle transition. The FFS Part 9 fast-fracture check is the gating assessment for cold-thermal-shock events.

## Source materials

- [og-standards-api](../sources/og-standards-api.md) — parent source page for the API RP 571 / API 579 / API RP 941 catalogue references underpinning the thermal-fatigue assessment framework above.
- [og-standards-asme](../sources/og-standards-asme.md) — parent source page for the ASME B31.1 / B31.3 / BPVC VIII-1 / VIII-2 / III references underpinning the new-build and design-by-analysis envelope for cyclic thermal service.

## Notes

- This is a concept page, not a standards page. No clause text, S-N curve constants, Coffin-Manson exponents, fatigue-strength-reduction factors, or thermal-shock allowable-stress curves are reproduced here. For normative use, cite the publisher edition of API RP 571 / API 579-1 / ASME B31.1 / ASME B31.3 / ASME BPVC VIII-1 / VIII-2 / III directly.
- The component / mechanism table is illustrative of typical refining, petrochem, and power-cycle experience; actual susceptibility for any specific asset must consider service-fluid chemistry, anchor-as-built condition, insulation history, and upset-event frequency from operating logs.
- The Davis-Besse RPV head 2002 event is referenced as a landmark bypass-leakage thermal-fatigue case study; full root-cause documentation lives in the NRC LER record and post-event industry analyses, not reproduced here.
- General engineering knowledge described above is paraphrased from public textbook sources (Suresh, *Fatigue of Materials*, 2nd ed., CUP 1998; Manson and Halford, *Fatigue and Durability of Structural Materials*, ASM International 2006; Hertzberg, *Deformation and Fracture Mechanics of Engineering Materials*, 5th ed., Wiley 2012) and is independent of any vendor PDF in the deny-list catalogue.
