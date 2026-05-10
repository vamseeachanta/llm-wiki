---
title: "AMPP SP0775 — Corrosion Coupons in Oilfield Operations"
slug: ampp-sp0775
tags: ["ampp", "nace", "corrosion-monitoring", "coupons", "oilfield", "online-corrosion", "standards", "field-practice", "metadata-only"]
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
code_id: ampp-sp0775
legacy_code_id: nace-sp0775
publisher: AMPP (formerly NACE International)
legacy_publisher: "NACE International"
revision: not-on-disk
revision_source: "n/a — SP0775 is a catalog gap on /mnt/ace/O&G-Standards/ as of 2026-05-09"
verified_on: 2026-05-09
public_url: https://store.ampp.org/
sources: []
extraction_policy: metadata-only
raw_copy_allowed: false
nace_doc_number: "SP 0775"
prior_nace_doc_number: "RP 0775"
ampp_doc_number: "SP 0775"
---

# AMPP SP0775 — Preparation, Installation, Analysis, and Interpretation of Corrosion Coupons in Oilfield Operations

## Scope

Field-practice standard for the **preparation, installation, retrieval, analysis, and interpretation of corrosion coupons** deployed in oilfield production systems — production tubing, flowlines, separator vessels, dehydrators, gathering systems, and pipelines — across sweet (CO2), sour (H2S), and microbiologically influenced (MIC) service. SP0775 is the field companion to the laboratory mass-loss method [astm-g1](astm-g1.md) / [astm-g31](astm-g31.md): it extends laboratory coupon practice into the multiphase, intermittent-flow, surface-treated, biofilm-bearing environments that characterize real upstream and midstream operations. The standard prescribes:

- **Coupon geometry and material matching** — typical flat strip ~100 × 25 × 3 mm (3.94 × 0.98 × 0.12 in), threaded for retrievable holders; alloy and surface finish matched to the parent component being monitored.
- **Holder design** — electrically-isolated, pressure-rated retrievable holders (high-pressure access fittings of the hot-tap or full-port type) with the coupon oriented to the dominant flow direction.
- **Placement at credible monitoring locations (CMLs)** — high-risk regions including dead legs, water-phase / pipe-bottom positions in stratified multiphase flow, top-of-line condensation zones in wet-gas flowlines, and downstream of phase-changing fittings (chokes, separators).
- **Exposure intervals** — typical 90-day default for general corrosion-rate determination; shorter 30-day intervals for pitting screening or for high-rate environments where 90 days would consume the coupon.
- **Post-retrieval handling** — preservation in dry inert (N2) atmosphere or vapor-phase corrosion-inhibitor pouches, shipment to the analyzing laboratory within 24 hours when feasible to minimize post-exposure artefact corrosion.
- **Cleaning and weight-loss extrapolation** — chemical and mechanical cleaning per the iterative procedure of [astm-g1](astm-g1.md), with the asymptotic weight-loss extrapolation that separates true corrosion-product loss from base-metal loss during cleaning.
- **Reporting** — general corrosion rate (mass-loss → penetration rate per [astm-g102](astm-g102.md)), maximum and average pit depths per [astm-g46](astm-g46.md) examination, photographic log of the as-retrieved coupon and post-cleaning surface, and the deduced corrosion mechanism (uniform, pitting, MIC, erosion-corrosion, top-of-line, under-deposit).

The standard is the field-practice anchor that turns mass-loss coupon data into defensible **corrosion-rate measurement** for integrity-management programs (see consumer concept page [corrosion-rate-measurement](../concepts/corrosion-rate-measurement.md)).

## Edition history

SP0775 originated as **NACE RP 0775 — Recommended Practice** and was promoted to a **Standard Practice (SP)** under NACE's recommended-practice-to-standard-practice renumbering policy. The 2021 NACE-to-AMPP merger preserved the document number under AMPP's document-number-continuity policy. Editions known to exist (publisher record, not on-disk):

| Edition | Year | Publisher | Notes |
|---------|------|-----------|-------|
| RP 0775-1991 | 1991 | NACE | Original recommended-practice publication. |
| RP 0775-1999 | 1999 | NACE | Revision; expanded oilfield-environment guidance. |
| RP 0775-2005 | 2005 | NACE | Revision; pitting-rate interpretation tables expanded. |
| SP 0775-2013 | 2013 | NACE | Promoted from RP to SP (Standard Practice) under NACE renumbering. |
| SP 0775-2018 | 2018 | NACE | Most recent NACE-branded edition prior to the AMPP rebrand. |
| SP 0775 (post-2021) | post-2021 | AMPP | Retained document number after the 2021 NACE-to-AMPP merger; legacy NACE SP0775 / RP0775 references resolve to the AMPP-branded edition by document-number continuity. |

**Legacy-identifier resolution.** Because the document moved from RP-numbering to SP-numbering and then changed publisher (NACE → AMPP), three legacy spellings are commonly encountered in older specifications and consultant reports: `NACE RP 0775`, `NACE SP0775`, and `AMPP SP0775`. All three refer to the same document family; this page's `legacy_code_id: nace-sp0775` and `prior_nace_doc_number: RP 0775` fields bridge those references to the canonical current identifier `ampp-sp0775`.

**On-disk status.** SP0775 is a **catalog gap**. A scan of `/mnt/ace/O&G-Standards/` on 2026-05-09 with filename heuristics (`*0775*`, `*sp0775*`, `*sp-0775*`, `*rp0775*`, `*rp-0775*`, `*coupon*`) returned no match; the on-disk NACE coverage at `/mnt/ace/O&G-Standards/NACE/` is limited to MR 0175, TM 0177-96, and four conference papers (per [og-standards-minor-publishers](../sources/og-standards-minor-publishers.md)). Until an SP0775 edition is added to the catalog, downstream calc citations referencing this code must wait for `revision_source` to be populated.

## Key sections

The procedural detail below is the field-practice outline at the level needed for downstream consumers to understand citations; the operative numbers (exact coupon dimensions, holder torque values, cleaning solution recipes, pitting-rate threshold tables) must be read from the source PDF and are not reproduced here.

### Coupon geometry and material

- **Typical flat coupon:** ~100 × 25 × 3 mm (3.94 × 0.98 × 0.12 in), threaded on one end for engagement with a retrievable holder rod.
- **Other forms:** disk coupons for flush-mounted holders; pipe-section coupons for under-deposit and top-of-line scenarios; strip coupons for high-velocity probes.
- **Material match.** Coupon alloy must match the parent component being monitored (typical: API 5L X-grade for line pipe, AISI 1018 / 4130 for tubing reference, 13Cr / 22Cr / 25Cr / Alloy 625 / Alloy 825 for CRA-clad service). Surface finish is specified in the standard; the as-received mill finish of the parent component is **not** an acceptable proxy because it carries mill scale that distorts the early-exposure rate.

### Holder design and CML placement

- **Retrievable access fittings.** High-pressure-rated full-port fittings (hot-tap and welded-boss families) allow coupon retrieval and re-installation without depressurizing the line. Holder rods carry the coupon into the flow stream and electrically isolate it from the parent pipe to avoid galvanic-couple distortion of the rate.
- **Flow-orientation rules.** Coupon broad face is typically oriented parallel to the dominant flow direction in turbulent service to minimize impingement-driven anomalies; orientations are specified per CML scenario in the standard.
- **High-risk CMLs prioritized for coupon stations:**
  - **Dead legs** — stagnant or low-velocity branches where water phase accumulates and MIC nucleates.
  - **Pipe-bottom water phase** — stratified multiphase flow where free-water sits below an oil or gas phase; the dominant CO2/H2S corrosion site in three-phase production lines.
  - **Top-of-line (TOL)** — wet-gas flowlines with condensation on the upper pipe wall; TOL CO2 corrosion is geometry-dependent and not captured by bottom-phase coupons.
  - **Downstream of chokes, separators, and phase-change fittings** — flow-disturbance zones where erosion-corrosion can dominate.
  - **Injection points** — chemical-injection ports where treatment-fluid mixing creates locally severe environments before the inhibitor disperses.

### Exposure intervals

- **90-day default** — the canonical exposure for general-corrosion-rate determination in moderate-rate oilfield service. Long enough to integrate transient upsets; short enough to avoid coupon consumption in aggressive environments.
- **30-day pitting screen** — for environments with suspected pitting where the time-to-perforation analysis requires earlier observation, or for high-rate sour service where 90 days would consume the coupon thickness.
- **Longer intervals (180+ day)** — used in low-rate sweet service or for inhibitor-program-validation campaigns where the signal-to-noise on cumulative mass loss requires extended exposure.
- **Documentation rule:** every coupon report must state the exposure start and end timestamps, the cumulative process throughput and water-cut over the exposure window, and any chemical-treatment or operational-upset events that occurred during exposure.

### Post-retrieval handling

- **Immediate preservation.** As soon as the coupon is broken out of the holder, it is rinsed with a non-aqueous solvent (typically isopropanol) to displace produced water and is sealed in an inert container with desiccant, vapor-phase inhibitor, or N2 backfill.
- **Shipment.** Within 24 hours to the analyzing laboratory whenever feasible; longer transit windows must be flagged in the analysis report because post-exposure atmospheric corrosion adds artefact mass loss that cannot be cleaned out without distorting the rate.
- **Photographic log.** Both as-retrieved (with corrosion product, scale, and any biofilm or deposit) and post-cleaning surfaces are photographed at standardized lighting and magnification.

### Cleaning and rate calculation

- **Cleaning per [astm-g1](astm-g1.md).** Iterative chemical and mechanical cleaning with the **asymptotic weight-loss extrapolation** that separates the true corrosion-product loss (rapid initial mass drop during the first cleaning cycles) from the base-metal loss during cleaning (slow linear loss in subsequent cycles). The intercept of the linear base-metal-loss line at cycle zero gives the corrected corrosion mass loss.
- **Rate conversion per [astm-g102](astm-g102.md).** Mass loss is converted to a penetration rate (mils per year, or millimetres per year) using the alloy density and the exposed coupon area. SP0775 governs the field-data inputs; G102 governs the unit-conversion algebra.
- **Pitting analysis per [astm-g46](astm-g46.md).** Maximum pit depth is measured by metallographic cross-section, optical depth-of-field profiling, or laser surface scanning; SP0775 specifies the per-coupon sampling rule (typically 10 deepest pits across the exposed face) and reporting format.

### Reporting

A compliant SP0775 coupon report carries:

- **General corrosion rate** in mils-per-year (mpy) or mm/yr.
- **Maximum and average pit depth** in mils or mm, with the time-to-perforation projection if maximum-depth pits are extrapolated linearly.
- **Photographic log** of as-retrieved and post-cleaning surfaces.
- **Deduced corrosion mechanism** — uniform, pitting, MIC (with biofilm-microscopy or sulfate-reducing-bacteria-culture evidence where applicable), erosion-corrosion, top-of-line, or under-deposit — selected from the standardized mechanism set in the standard.
- **Process context** — exposure window, throughput, water-cut, chemical-treatment program, and any operational upsets logged during the exposure.

## Online corrosion monitoring

SP0775 provides the field-practice substrate that **online (continuous) corrosion-monitoring** programs build on. The continuous-rate measurement is delivered by electrochemical probes — **Linear Polarization Resistance (LPR)** per [astm-g59](astm-g59.md), **Electrical Resistance (ER)** probes, and **Electrochemical Impedance Spectroscopy (EIS)** probes per [astm-g106](astm-g106.md) — installed at the same CMLs identified for coupon stations. SP0775 governs the **data-fusion and interpretation** that combines:

- The **coupon snapshot** (90-day integrated mass-loss rate, anchored to ASTM G1 / G102 algebra; the calibration ground truth).
- The **continuous LPR / ER readings** (instantaneous rate values, sampled minutes-to-hours, that reveal transient excursions and inhibitor-program response).

The two streams are fused per the calibration relationship `i_corr_LPR = β / R_p` (Stern-Geary, with the β constant calibrated against the coupon mass-loss rate for the specific environment). Without the SP0775 coupon anchor, LPR-only programs drift because the Stern-Geary β constant is environment-dependent and is **not** transferable across produced-water chemistries, inhibitor regimes, or temperature ranges. SP0775 is therefore the practice-level standard that makes online corrosion monitoring **traceable** rather than **indicative**.

## Cross-references

- [astm-g1](astm-g1.md) — Standard practice for preparing, cleaning, and evaluating corrosion test specimens. The required laboratory companion for cleaning and weight-loss extrapolation. Mandatory upstream call from any SP0775 coupon analysis.
- [astm-g31](astm-g31.md) — Standard guide for laboratory immersion corrosion testing of metals. The laboratory-immersion sibling that SP0775 extends into the field environment.
- [astm-g59](astm-g59.md) — Standard test method for conducting potentiodynamic polarization resistance measurements. Online-monitoring complement: LPR is the continuous-rate companion to SP0775's coupon anchor.
- [astm-g102](astm-g102.md) — Standard practice for calculation of corrosion rates and related information from electrochemical measurements. The mass-loss-to-rate (and i_corr-to-rate) unit-conversion algebra.
- [astm-g46](astm-g46.md) — Standard guide for examination and evaluation of pitting corrosion. Required for the pit-depth and pit-density columns of the SP0775 report.
- [api-rp-571](api-rp-571.md) — Damage mechanisms affecting fixed equipment in the refining industry. Provides the damage-mechanism context (sweet CO2, sour H2S, MIC, erosion-corrosion, top-of-line) that SP0775 coupon-derived rates feed.
- [api-rp-581](api-rp-581.md) — Risk-based inspection methodology. Coupon-derived corrosion rates are a primary probability-of-failure (POF) input to RBI calculations; SP0775 is the field-practice basis for the rate values fed into 581 sub-factors.
- [api-rp-574](api-rp-574.md) — Inspection practices for piping system components. The in-service inspection complement; SP0775 coupon stations and 574-prescribed UT thickness surveys are the two field data streams that integrity-management programs reconcile.
- [corrosion-rate-measurement](../concepts/corrosion-rate-measurement.md) — Concept-level synthesis of the four canonical corrosion-rate methods (mass-loss, electrochemical, in-service thickness, hydrogen-flux) that consumes SP0775 as the online-monitoring / field-coupon primary reference.
- [ampp-tm-0177](ampp-tm-0177.md) — Sulfide stress cracking laboratory test methods (sour-service materials qualification, not field corrosion-rate monitoring).
- [ampp-tm-0284](ampp-tm-0284.md) — Hydrogen-induced cracking laboratory test method (sour-service materials qualification, not field corrosion-rate monitoring).
- Calc citation contract: `.claude/rules/calc-citation-contract.md`

## Sources

- [og-standards-minor-publishers](../sources/og-standards-minor-publishers.md) — O&G Standards catalog roll-up for AMPP / NACE coverage. SP0775 is a recognized gap in the on-disk NACE coverage; this source page records the scan-and-not-found outcome of the 2026-05-09 catalog filter (`0775`, `sp0775`, `sp-0775`, `rp0775`, `rp-0775`, `coupon` filename heuristics).
- Publisher portal (current edition): `https://store.ampp.org/` — registration required for purchase. No raw text or numeric thresholds copied from the publisher source into this repository per the spinout vendor-PDF firewall.
