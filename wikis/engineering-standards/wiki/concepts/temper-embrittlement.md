---
title: "Temper Embrittlement (J-Factor + X-Factor)"
slug: temper-embrittlement
tags:
  - temper-embrittlement
  - j-factor
  - x-factor
  - watanabe
  - bruscato
  - cr-mo
  - hydroprocessing
  - rpv
  - weld-metallurgy
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
sources:
  - standards/api-rp-571.md
  - standards/api-rp-941.md
---

# Temper Embrittlement (J-Factor + X-Factor)

> Concept page. Definitional and link-rich; load-bearing acceptance numbers, clause text, and method detail live on the standards pages this concept routes into. The J-factor and X-factor formulae below are reproduced for definitional purposes; for design or contractual use, cite the publisher edition of the relevant material specification (API 934-A, ASTM A387, ASTM A832, or the applicable Cr-Mo welding consumable standard) directly.

## What is temper embrittlement?

**Temper embrittlement** is a **reversible decrease in fracture toughness** of certain low-alloy steels — most prominently Cr-Mo, Ni-Cr-Mo, and Ni-Cr-Mo-V grades — caused by **prolonged exposure to the 350–565 degC (~660–1050 degF) window** during service or during slow cooldown through that window after PWHT. The damage is observable as:

- a **shift in the fracture-appearance transition temperature (FATT)** to higher temperature,
- a **drop in upper-shelf and transition-region Charpy energy**,
- a **drop in `K_Ic` and `K_Jc` toughness**, and
- a **change in fracture path** from transgranular cleavage or microvoid coalescence to **intergranular separation along prior-austenite grain boundaries**.

The mechanism is **segregation of trace impurity elements** — phosphorus (P), tin (Sn), antimony (Sb), and arsenic (As) — to prior-austenite grain boundaries during exposure in the embrittlement window. The segregants weaken cohesion across the boundary, opening a brittle intergranular fracture path on subsequent cooling to the service or test temperature. Nickel and manganese **co-segregate with phosphorus** and aggravate the effect; silicon also raises susceptibility through its co-segregation behaviour. The damage is **reversible**: a high-temperature de-embrittling soak above ~600 degC followed by rapid cooling will redistribute the segregants and largely recover the toughness, which is the basis for the [step-cooling test](#step-cooling-test) qualification protocol.

Temper embrittlement is contrasted with **temper martensite embrittlement** (a separate ~250–400 degC mechanism in quenched-and-tempered martensitic steels associated with cementite precipitation) and with **475 degC embrittlement** (a ferritic stainless-steel and duplex mechanism associated with α′ phase separation). The three share the surface-level signature of toughness loss but operate on different alloy families and at different temperatures.

## Why it matters

The economically dominant temper-embrittlement exposure is **refinery hydroprocessing service** — hydrocrackers, hydrotreaters, and naphtha hydrofiners — whose reactor pressure vessels operate at **350–450 degC** for design lives of **30 years or more**. Over that exposure, plate, forging, and weld-metal toughness can degrade from the as-fabricated condition to a **substantially elevated transition temperature**, while the operating temperature itself remains comfortably above the transition. The risk is therefore **not the operating condition** — it is the **start-up and shutdown traverse** through the transition window down to ambient, when the embrittled material must carry pressurisation loads at temperatures where its toughness is lowest.

The historical case file is the principal driver of modern impurity-control specifications:

- Multiple **hydroprocessing reactor brittle-fracture incidents in the 1960s–1980s** in U.S. and European refineries, several involving cooldown rupture from a small weld-zone flaw in heavily embrittled 2.25Cr-1Mo plate or weld metal.
- The **1996 Texaco hydrocracker incident** (a near-miss reactor failure with severe brittle-fracture indications during shutdown) prompted a further round of industry tightening, including stricter J-factor / X-factor caps in API 934-A and equivalent project specifications.
- **Reactor pressure vessel (RPV) surveillance programmes** in nuclear service track temper embrittlement alongside neutron-irradiation embrittlement in Ni-Cr-Mo-V forging steels (A508 Class 3, 16MND5 / 18MND5), with the same impurity-segregation mechanism operating, at lower temperatures, across the long irradiation life.

The combined response to this case file is a **dual envelope** that controls both the **start-up / shutdown thermal path** (via the [minimum-pressurization-temperature](#inspection) procedure) and the **as-procured material chemistry** (via the [J-factor and X-factor caps](#j-factor--x-factor-formulae) below).

## J-Factor + X-Factor formulae

Two empirical impurity-content indices are in industry-wide use to **rank susceptibility** at the procurement gate. Both index **chemical composition only** — they do not measure toughness directly; they correlate composition with the magnitude of toughness loss observed in the calibrated step-cooling test (below).

- **J-factor (Watanabe, 1980, JFE / Nippon Kokan calibration)** for Cr-Mo and low-alloy **plate and forging base metal**:

  ```
  J = (Si + Mn) × (P + Sn) × 10^4
  ```

  with all elements in **weight percent**. Threshold for hydroprocessing-service Cr-Mo plate: typically **`J ≤ 100`** as a baseline, tightened to **`J ≤ 80`** or **`J ≤ 60`** in many project specifications and in API 934-A for the most demanding new-build reactor service.

- **X-factor (Bruscato, 1970, Combustion Engineering calibration)** for Cr-Mo and low-alloy **weld metal**:

  ```
  X = (10 P + 5 Sb + 4 Sn + As) / 100
  ```

  with all elements in **weight ppm**. Threshold for hydroprocessing-service Cr-Mo weld metal: typically **`X ≤ 15`** as a baseline, tightened to **`X ≤ 12`** in API 934-A and in many project welding-consumable specifications.

Lower values are better for both indices. The two formulae are **not interchangeable**: J was calibrated on plate compositions and base-metal heat-treatment histories, X on weld-metal compositions and as-deposited / PWHT histories. Procurement specifications therefore call **J on plate and forging mill certificates** and **X on welding-consumable certificates** separately. Some specifications additionally cap **P content alone** (typically ≤ 0.010 wt%) on weld metal as a redundant defence-in-depth control.

## How impurity control evolved

The procurement-side impurity-control regime was assembled incrementally over roughly a 30-year window in response to the hydroprocessing case file:

- **1970s.** Cr-Mo plate specifications added **phosphorus and sulfur limits** beyond the generic ASTM A387 minima. The **J-factor formula** was calibrated by JFE and Nippon Kokan from plate Charpy data and entered Japanese refiner project specifications.
- **1980s.** Cr-Mo welding-consumable specifications added the **X-factor cap and a standalone weld-metal phosphorus limit**. The Bruscato formula was calibrated by Combustion Engineering and Bristol-Myers from weld-metal step-cooling Charpy data and entered U.S. and European refiner project specifications.
- **1990s–2000s.** **API 934-A** (*Materials and Fabrication of 2.25Cr-1Mo, 2.25Cr-1Mo-V, 3Cr-1Mo, and 3Cr-1Mo-V Steel Heavy Wall Pressure Vessels for High-Temperature, High-Pressure Hydrogen Service*) consolidated the impurity-control regime into a standalone API standard for new-build hydroprocessing reactors, combining **`J ≤ 80`** for plate/forging and **`X ≤ 12`** for weld metal with step-cooling qualification on production-test coupons.
- **Post-1996 Texaco incident.** Industry tightening pushed many project specifications to **`J ≤ 60`** and added explicit **PWHT cooldown-rate controls** (e.g., specified maximum cooling rate through 500–400 degC) to limit in-shop embrittlement during fabrication.

The arc of the regime is from **toughness testing as the only gate** (1960s) through **composition-plus-toughness as parallel gates** (1980s) to **composition-plus-step-cooling-plus-cooldown-control as a defence-in-depth stack** (post-2000s). API 934-A is the current consolidation point for new-build hydroprocessing reactor practice; ASTM A387 (plain Cr-Mo plate) and ASTM A832 (V-modified Cr-Mo plate) are the underlying material specifications.

## Step-cooling test

The **step-cooling test** is a laboratory accelerated-embrittlement protocol used to qualify a heat of plate, forging, or weld metal against a contractual temper-embrittlement Charpy-shift cap. The protocol (an ASTM A335-style modification, with project-specific variants) is:

1. Solution-treat and temper the test coupon to the specified production heat-treatment condition.
2. Measure baseline **Charpy V-notch energy at a reference temperature** (typically near the as-fabricated FATT) and baseline **FATT** by Charpy temperature sweep.
3. Heat to **593 degC (1100 degF)** and hold for ~1 hour.
4. **Slow-cool through the embrittlement window** along a stepped path: hold at 538 degC (1000 degF), 524 degC (975 degF), 496 degC (925 degF), 469 degC (875 degF), 441 degC (825 degF), 315 degC (600 degF) for prescribed dwell times totalling ~250 hours.
5. Re-measure Charpy energy at the reference temperature and re-measure FATT.
6. Compute **`ΔFATT = FATT_after − FATT_before`** as the temper-embrittlement Charpy shift.

The **acceptance criterion** is project-specific but is typically **`ΔFATT ≤ 27 degC (50 degF)`** for hydroprocessing-reactor Cr-Mo plate and weld metal qualified to API 934-A or equivalent. A heat that fails step-cooling is rejected at the procurement gate even if its J-factor or X-factor passes the composition cap, because the composition indices are correlations rather than direct measurements. The two gates **operate in series, not in parallel**.

## Inspection

For in-service hydroprocessing reactors and other temper-embrittlement-credible equipment, the operational controls are:

- **Minimum-pressurization-temperature (MPT) procedure** during start-up and shutdown. The MPT defines a **pressure-versus-metal-temperature envelope** that keeps the operating point safely above the embrittled-material transition temperature throughout the cooldown traverse. Pressurisation is held off until the reactor metal temperature exceeds a project-specific floor (typically a function of cumulative service hours and the most recent step-cooling re-qualification result on a removed surveillance coupon). The MPT envelope is the load-bearing operational defence and is recomputed across the asset life as the material continues to embrittle.
- **FFS Level 3 brittle-fracture assessment** with embrittled-material toughness inputs per [API 579-1 / ASME FFS-1](../standards/api-std-579.md) **Part 3** (brittle fracture) and **Part 9** (crack-like flaws). Inputs are sampled or surveillance-coupon-derived toughness curves rather than mill-certificate as-fabricated data, and the FFS run produces the operating P-T envelope and the **MAT** (Minimum Allowable Temperature) curve consumed by the MPT procedure above. **Part 4 / Part 5** general and local metal-loss assessment may run in parallel where wall thinning is also present.
- **Embrittlement monitoring** via two complementary streams: **cumulative-time-at-temperature tracking** in the operating-data historian (an embrittlement-dose proxy that drives the re-evaluation cadence), and **periodic Charpy testing of removed equipment, archive coupons, or weld-pad surveillance specimens** to recalibrate the assumed toughness curve. The latter is the only direct measurement available without destructive removal of in-service material.

The detection asymmetry parallels that of [HTHA](htha-nelson-curves.md): the damage is a **microstructural state change** that does not show as wall thinning, leakage, or surface flaw on routine UT/MT/PT inspection, so the load-bearing controls are **upstream procurement** (J/X caps + step-cooling) and **downstream operational envelope** (MPT + FFS), with toughness sampling as the recalibration input. Inspection alone cannot manage temper embrittlement.

## Standards

Bidirectional links to the standards-page resolvers (each carries `code_id`, `publisher`, `revision` frontmatter per the wiki schema):

- [api-rp-571](../standards/api-rp-571.md) — *Damage Mechanisms Affecting Fixed Equipment in the Refining Industry.* Temper embrittlement appears in the high-temperature mechanism catalogue with affected materials (Cr-Mo and Ni-Cr-Mo low-alloy steels), critical factors (impurity content, exposure time-temperature, prior austenite grain size), morphology (intergranular separation along prior-austenite boundaries on cooldown rupture), prevention / mitigation (composition control, cooldown-rate control, MPT procedure), and inspection / monitoring (surveillance coupons, step-cooling re-qualification).
- [api-rp-941](../standards/api-rp-941.md) — *Steels for Hydrogen Service at Elevated Temperatures and Pressures.* HTHA and temper embrittlement **co-occur** in Cr-Mo hydroprocessing reactor service: the alloy ladder selected for HTHA resistance (1.25Cr-0.5Mo, 2.25Cr-1Mo, 2.25Cr-1Mo-V) is the same family on which temper-embrittlement composition control bites hardest, and the operating envelope must clear both Nelson-curve and embrittled-toughness MAT constraints simultaneously.
- [api-std-579](../standards/api-std-579.md) — *Fitness-for-Service.* **Part 3** (brittle fracture) and **Part 9** (crack-like flaws) consume embrittled-material Charpy or master-curve toughness inputs to derive the MAT screening curve and the operating P-T envelope; **Part 4 / Part 5** (general and local metal-loss assessment) run in parallel where wall thinning is also present.
- [asme-bpvc-viii-1](../standards/asme-bpvc-viii-1.md) and [asme-bpvc-viii-2](../standards/asme-bpvc-viii-2.md) — *Rules for Construction of Pressure Vessels.* The design code under which hydroprocessing reactors are originally constructed; allowable-stress tables in Section II-D anchor the design margin used in the MAT-derivation FFS run, and the post-construction surveillance-coupon programme is the means by which the construction-time toughness assumption is revisited across the asset life.
- **API 934-A** — *Materials and Fabrication of 2.25Cr-1Mo, 2.25Cr-1Mo-V, 3Cr-1Mo, and 3Cr-1Mo-V Steel Heavy Wall Pressure Vessels for High-Temperature, High-Pressure Hydrogen Service.* The consolidation point for the impurity-control regime — `J ≤ 80` plate/forging cap, `X ≤ 12` weld-metal cap, step-cooling qualification on production-test coupons. **Future-promotion candidate** — not yet a dedicated standards page in this wiki.
- **ASTM A387** — *Pressure Vessel Plates, Alloy Steel, Chromium-Molybdenum.* Underlying plate specification for plain Cr-Mo grades (Grade 11 = 1.25Cr-0.5Mo, Grade 22 = 2.25Cr-1Mo). Future-promotion candidate.
- **ASTM A832** — *Pressure Vessel Plates, Alloy Steel, Chromium-Molybdenum-Vanadium.* Underlying plate specification for V-modified Cr-Mo grades (Grade 22V = 2.25Cr-1Mo-V) used in modern hydrocracker reactors. Future-promotion candidate.

## Related concepts

- [brittle-fracture](brittle-fracture.md) — **the failure mode temper embrittlement produces**. A temper-embrittled component fails by sudden cleavage- or intergranular-cleavage rupture during cooldown traverse through the elevated transition temperature, indistinguishable on the failure surface from a low-temperature DBTT-driven rupture.
- [weld-toughness](weld-toughness.md) — **weld-metal X-factor most-cited**. Cr-Mo welding consumables for hydroprocessing service are the load-bearing X-factor application; the weld-toughness page covers the broader weldment-qualification regime under which X is one of several composition-and-test gates.
- [htha-nelson-curves](htha-nelson-curves.md) — **parallel hydroprocessing-reactor damage mechanism**. HTHA and temper embrittlement co-occur on the same Cr-Mo alloy ladder in the same hydroprocessing reactors; alloy selection, fabrication chemistry, and operational envelope must clear both at once.
- [fitness-for-service](fitness-for-service.md) — **downstream operational consumer**. FFS Part 3 / Part 9 consumes embrittled-material toughness inputs to produce the MAT and operating P-T envelope that the MPT procedure enforces.

## Source materials

- [og-standards-api](../sources/og-standards-api.md) — catalog summary covering API RP 571, RP 941, Std 579, and the API 934-x family on the consolidated standards mount.

## Notes

- Concept page only — no clause text or contractual acceptance numbers from API 934-A, ASTM A387, ASTM A832, or the welding-consumable specifications are reproduced here. The J-factor and X-factor formulae are reproduced for definitional purposes; the **threshold values** (`J ≤ 100 / 80 / 60`, `X ≤ 15 / 12`) are project- and standard-specific and must be cited from the publisher edition of the relevant standard for any design or contractual use.
- Per the [calc citation contract](../../../../../.claude/rules/calc-citation-contract.md), any calc module that consumes a temper-embrittlement composition cap, a step-cooling acceptance shift, or an embrittled-material toughness floor must emit a `Citation` instance pinning the relevant `code_id` (e.g., `api-934-a`, `astm-a387`, `astm-a832`, or the project welding-consumable spec) with the applicable revision.
- Vendor PDFs are read-only at the consolidated standards mount and never enter this repo per the spinout 2026-05-05 governance and the vendor-derivative firewall in the repo-root `CLAUDE.md`.
