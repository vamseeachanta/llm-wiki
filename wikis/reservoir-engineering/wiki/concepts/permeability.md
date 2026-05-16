---
title: "Permeability"
tags: [permeability, rock-properties, formation-evaluation, darcy, core-analysis, log-analysis, well-test, petrophysics]
added: 2026-05-16
last_updated: 2026-05-16
sources:
  - tiab-donaldson-petrophysics-4e-2015
  - cosentino-integrated-reservoir-studies-2001
  - ahmed-reservoir-engineering-handbook-5e-2018
cross_links:
  - drilling-engineering/concepts/formation-evaluation-basics.md
  - drilling-engineering/concepts/mwd-lwd-overview.md
  - production-engineering/concepts/hydraulic-fracturing.md
---

# Permeability

## Scope

**Permeability** (k) is the foundational rock-transport property: a measure of a rock's capacity to transmit fluid through its connected pore network. It is the upstream variable for every reservoir-engineering deliverability calculation: well productivity index, drawdown, recovery rate, and recovery time all start with permeability. This page is the rock-transport counterpart to [porosity](porosity.md), which covers rock storage; together they form the foundational rock-property pair this wiki is founded on.

## Calc-citation contract status (this page)

Concept pages in this wiki describe foundational equations **structurally and qualitatively only** — engineering-unit equation forms with numeric coefficients are deferred to standards-anchor pages and to downstream calc modules. When a downstream consumer (e.g., a `digitalmodel` reservoir-calc module) emits a value derived from one of these frameworks, that module is expected to carry an explicit citation to a standards page (API / SPE / SPWLA / equivalent). This page does not transcribe equation forms; it is the explanatory anchor. The foundational equations referenced here are flagged as **calc-citation candidates** for downstream consumers. Decision recorded explicitly (avoiding the ambiguous-middle anti-pattern surfaced in the production-engineering Phase 4 plan review):

- **Darcy's law** — doc-only metadata anchor in this wiki; if/when a `digitalmodel` reservoir-calc module emits a Darcy-derived value (e.g., a well productivity index), the calc module MUST cite an API / SPE standards page (or equivalent) per the contract; this wiki page is the explanatory anchor only.
- **Klinkenberg slip-correction** — same posture; named here, equation not transcribed.
- **Kozeny-Carman / Timur / Wyllie-Rose** porosity-permeability empirical correlations — same posture; named here with structural descriptions, equation forms with engineering-unit numeric coefficients NOT transcribed.

This page therefore describes the foundational frameworks **structurally and qualitatively only**. Engineering-unit equation forms with numeric coefficients are deferred to the standards anchor pages (Wave 5) and to downstream calc modules with proper citation emission.

## Definition

Permeability quantifies the rate at which a fluid flows through a porous medium under an imposed pressure gradient. The defining framework is **Darcy's law** (Henry Darcy, 1856), which relates volumetric flow rate per unit cross-sectional area to the pressure gradient and to a proportionality constant — the permeability — divided by the fluid viscosity. The framework is named here at structural level only; engineering-unit forms are NOT transcribed (see calc-citation discipline above).

Permeability is a property of the **rock alone** when the rock is fully saturated with a single fluid that does not chemically interact with the rock surface — this is **absolute permeability**. When multiple phases coexist in the pore network (oil + water, oil + gas, oil + water + gas), each phase's flow rate is reduced by the presence of the other phase(s), giving rise to the **effective permeability** (the permeability seen by one phase in the presence of others) and **relative permeability** (the dimensionless ratio of effective to absolute permeability). See [Absolute vs effective vs relative](#absolute-vs-effective-vs-relative-permeability) below.

## Units

Permeability has dimensions of area (length squared). The petroleum-industry practical unit is the **Darcy** (D), with the **millidarcy** (mD) as the more common working unit for conventional reservoirs.

| Unit | Approximate SI equivalent | Typical reservoir class |
|---|---|---|
| Darcy (D) | ≈ 9.87 × 10⁻¹³ m² (≈ 0.987 μm²) | very high-permeability conventional reservoirs (rare); coarse unconsolidated sand |
| millidarcy (mD), 1 mD = 10⁻³ D | ≈ 9.87 × 10⁻¹⁶ m² | conventional oil and gas reservoirs |
| microdarcy (μD), 1 μD = 10⁻⁶ D | — | tight conventional reservoirs and tight gas |
| nanodarcy (nD), 1 nD = 10⁻⁹ D | — | unconventional shale gas and shale oil reservoirs |

Conversion to SI (the square metre) is rarely used in industry practice; the Darcy and its decimal subdivisions are the practical units throughout core-analysis reporting, well-test interpretation, and reservoir-simulation input decks.

## Absolute vs effective vs relative permeability

The three-way distinction is foundational; it is one of the most common confusion sources in formation-evaluation work.

- **Absolute permeability (k or k_abs)** — measured with a single fluid that fully saturates the pore network and does not chemically interact with the rock. The classic lab measurement uses dry gas (typically air or helium) or a non-wetting hydrocarbon liquid. Reported on core plugs as the **air permeability** (k_air) or **liquid permeability** (k_L) depending on the measuring fluid. A property of the rock alone.
- **Effective permeability (k_eff,phase)** — the permeability seen by a single phase when multiple phases coexist in the pore network. Always less than or equal to absolute permeability because the presence of the other phase(s) occupies pore-network volume that would otherwise be available for the phase of interest.
- **Relative permeability (k_r,phase)** — the dimensionless ratio of effective permeability to absolute permeability for a given phase, expressed as a function of saturation. Reported as a curve, k_r,phase(S_phase), measured on core plugs by SCAL methodology (steady-state or unsteady-state displacement experiments).

**Relative permeability is explicitly DEFERRED from this founding wiki's scope** per plan #40 (see [overview.md](../overview.md) scope-out list). A future plan — possibly emerging from `#2667 Domain Knowledge Sweep` when it reaches reservoir engineering — will provide the deep-coverage relative-permeability concept page. This page names the scope-distinction so downstream readers know where the boundary lies; the relative-perm page placeholder is at `concepts/relative-permeability.md` (does not yet exist; cross-link forward-reference).

## Measurement

Permeability is measured by four broad approaches, each with a characteristic scale and a characteristic interpretation framework.

### Core analysis

Direct measurement on a physical sample. Two principal flow methods:

- **Steady-state core analysis** — a fluid is flowed through a core plug under a constant inlet/outlet pressure differential until the flow rate stabilizes; permeability is computed from the steady-state form of Darcy's law. The reference method; most precise but slow. Used for special core analysis (SCAL) work where high precision is required.
- **Unsteady-state core analysis** — a pressure pulse is applied at one end of the core plug and the pressure response at the other end is recorded; permeability is computed from the transient response. Faster than steady-state; the working method for routine core analysis on large datasets.

Core-derived permeability is typically reported as **air permeability** (k_air, on dried plugs at ambient stress) or as **k_L** (a liquid permeability, sometimes Klinkenberg-corrected — see below). SCAL permeability adds net-confining-stress conditions and sometimes formation-brine saturation, both of which reduce the measured value relative to routine ambient-condition measurements.

### Well-test analysis

The pressure-vs-time response of a producing well during a transient test (drawdown, pressure-buildup, drillstem test, falloff) is interpreted to yield **permeability-thickness product (kh)**. The classical interpretation framework is the **Horner plot** for pressure-buildup tests; modern interpretation uses **type-curve matching** and the **Bourdet pressure-derivative** plot. Well-test analysis is in scope for a future plan, not this founding session; see [overview.md](../overview.md) scope-out. Cross-link forward-reference placeholder at `concepts/well-test-interpretation.md` (does not yet exist).

Well-test permeability is averaged over the reservoir volume seen by the pressure transient (drainage radius scale), which is many orders of magnitude larger than core-scale measurements. Reconciling core-scale, log-scale, and well-test-scale permeability is a standing problem in reservoir characterization.

### Log analysis

Wireline and LWD logs do not measure permeability directly. **NMR logs** can estimate permeability through empirical correlations (Coates / SDR / Timur — named only; see [Empirical correlations](#porosity-permeability-empirical-correlations) below) that relate the NMR-derived bound-water-to-free-fluid ratio (or T2 distribution) to permeability. NMR-derived permeability is the modern continuous-log permeability estimator; it is an empirical estimate, not a direct measurement, and should be calibrated against core-derived permeability in each well.

Older log-based permeability estimators (Wyllie-Rose-type from sonic logs) are still seen in legacy datasets.

### Mini-frac / DFIT analysis

A **diagnostic fracture injection test (DFIT)** — see [production-engineering/concepts/diagnostic-fracture-injection-test.md](../../../production-engineering/wiki/concepts/diagnostic-fracture-injection-test.md) — performs a small-volume injection-and-falloff test specifically designed to constrain in-situ stress, leak-off coefficient, and (via after-closure analysis) **reservoir permeability** and pressure. DFIT-derived permeability is the dominant industry method for unconventional reservoirs where core retrieval is impractical and conventional well-test interpretation is challenged by low permeability. It is named here as the unconventional-reservoir permeability-measurement pathway; the methodology is fully described on the cross-linked production-engineering page.

## Klinkenberg slip-correction

Gas permeability measured on core plugs in the lab is **higher** than the equivalent liquid permeability for the same plug because of **gas-slippage** at the pore walls — at the small pore sizes of typical reservoir rocks, gas molecules do not stick to the wall as fully as liquid molecules do, so the effective flow cross-section is slightly larger for gas than for liquid. The **Klinkenberg correction** (Klinkenberg, 1941) is the standard correction that removes this slippage effect from the measured air permeability to yield the equivalent absolute liquid permeability.

The Klinkenberg correction is named here; the engineering-unit equation form is NOT transcribed per calc-citation discipline. The correction is most significant for low-permeability rocks (< 1 mD) where pore sizes approach the gas mean free path; for high-permeability rocks the correction is small and often neglected. Tight gas and shale reservoirs require careful Klinkenberg-aware permeability reporting.

## Typical ranges

Permeability values span more than nine orders of magnitude across the realistic reservoir spectrum. Practitioner heuristic ranges by reservoir class (absolute permeability, single-phase context):

| Reservoir class | Typical absolute permeability range |
|---|---|
| Highly permeable conventional sandstone (very rare) | > 1 D (1000+ mD) |
| Conventional oil reservoir (good quality) | 10 - 1000 mD |
| Conventional oil reservoir (moderate quality) | 1 - 10 mD |
| Conventional gas reservoir | 0.1 - 100 mD |
| Tight gas sandstone | 0.001 - 1 mD (μD scale) |
| Shale gas / shale oil | < 0.001 mD (nD scale) |
| Fractured tight reservoir, matrix vs fracture | matrix < 0.1 mD; fracture-system effective permeability orders of magnitude higher |

The matrix-vs-fracture distinction is critical for fractured reservoirs: the matrix-permeability number alone radically understates well deliverability when natural fractures provide high-permeability transport pathways. Dual-porosity and dual-permeability reservoir-simulation models exist precisely to handle this case; framework descriptions belong to a future plan.

## Porosity-permeability empirical correlations

Several empirical correlations relate permeability to porosity and to grain-size or pore-throat-size proxies. These correlations are reservoir-class-specific and should be re-calibrated for each new reservoir; transferring a correlation from one field to another without recalibration is a classic source of well-deliverability forecasting error.

Named here at structural level only — equation forms with engineering-unit numeric coefficients are NOT transcribed per calc-citation discipline. Standards-anchor pages (Wave 5) and downstream calc modules will carry the cited equation forms with the appropriate provenance.

- **Kozeny-Carman** — the classical theoretical framework. Relates permeability to porosity, grain (or pore) size, and a tortuosity factor (a geometric factor capturing how non-straight the flow paths through the pore network are). Structural-relationship form: permeability scales with the square of a characteristic pore-throat dimension, with porosity entering through a cubed-to-squared functional form, and is inversely proportional to tortuosity squared. Useful as a theoretical anchor; calibration is required for any specific reservoir.
- **Timur** — an empirical correlation (Timur, 1968) derived from NMR-log analysis of clean sandstones. Relates permeability to porosity raised to a positive power and to the irreducible water saturation (a proxy for pore-throat size, since rocks with small pore throats hold more bound water by capillary forces). The dominant NMR-log permeability estimator for sandstones throughout the late 20th century.
- **Wyllie-Rose** — an earlier empirical correlation (Wyllie & Rose, 1950) of similar functional form. Less commonly used in modern practice but appears in legacy interpretation workflows.

Modern NMR-permeability estimators (Coates / SDR) extend this framework using the full T2 distribution as additional information beyond porosity and irreducible-water saturation. Named here; deferred to the future NMR-log-interpretation concept page.

## Standards anchors

- **API RP 40 — Recommended Practices for Core Analysis** — the canonical practitioner reference for core-derived permeability measurement methodology (steady-state, unsteady-state, Klinkenberg correction, SCAL conditions). Same standards-page anchor as for porosity. *Standards-page revision metadata to be verified at Wave-5 publish time*; default `revision: "verify-at-publish-time"` until confirmed.
- **SPWLA formation-evaluation references** — the Society of Petrophysicists and Well Log Analysts maintains a body of practitioner literature on log-derived permeability methodology. Paywalled — cited here at structural level + general framework only; no verbatim chunks > 30 words. Standards-page revision is the journal-issue-number granularity; *to be enumerated at Wave-5 publish time*.

## Public references

Textbook citations below are cited by **name + ISBN only**. These textbooks are NOT ingested into this repository per the plan #40 license-fail-closed posture; readers consult their own licensed copies.

- **Tiab & Donaldson** — *Petrophysics: Theory and Practice of Measuring Reservoir Rock and Fluid Transport Properties*, 4th edition (Gulf Professional Publishing, 2015, ISBN 978-0-12-803188-9). Public textbook reference for the full core-and-log permeability methodology stack and the absolute-vs-effective-vs-relative permeability framework.
- **Cosentino** — *Integrated Reservoir Studies* (Editions Technip, 2001, ISBN 978-2-7108-0797-7). Public textbook reference for the integrated geological-petrophysical workflow that combines porosity, lithology, permeability, and saturation determinations.
- **Ahmed** — *Reservoir Engineering Handbook*, 5th edition (Gulf Professional Publishing, 2018, ISBN 978-0-12-813649-2). Public textbook reference for the well-test-derived permeability framework and the reservoir-deliverability application of permeability (productivity index, drawdown, recovery rate). Note: the full reservoir-engineering substrate covered in this handbook is *deferred* from this founding wiki's scope per plan #40; the reference is included here because it is the standard textbook anchor for permeability-as-reservoir-property.

## Cross-references

Within this wiki:

- [Porosity](porosity.md) — the rock-storage counterpart to permeability; together they form the foundational rock-property pair this wiki is founded on.
- [Gamma-ray log interpretation](./gamma-ray-log-interpretation.md) — lithology indicator that feeds porosity-permeability correlation selection. *(Wave 3 — page does not yet exist; placeholder forward-reference.)*
- [Formation tops](./formation-tops.md) — stratigraphic correlation surface that determines which intervals' permeability is integrated into kh and net-pay deliverability. *(Wave 3 — page does not yet exist; placeholder forward-reference.)*
- [Relative permeability](./relative-permeability.md) — explicitly DEFERRED from this founding wiki; future-plan placeholder forward-reference. *(Does not yet exist; deferred scope per plan #40.)*
- [Well-test interpretation](./well-test-interpretation.md) — the well-test-derived kh framework. *(Does not yet exist; deferred scope per plan #40.)*

To other wikis:

- [drilling-engineering/concepts/formation-evaluation-basics.md](../../../drilling-engineering/wiki/concepts/formation-evaluation-basics.md) — the well-construction-time framing of formation evaluation; bidirectional cross-link with this page.
- [drilling-engineering/concepts/mwd-lwd-overview.md](../../../drilling-engineering/wiki/concepts/mwd-lwd-overview.md) — the LWD sensor systems that produce some of the permeability-relevant log measurements (NMR-LWD in particular).
- [production-engineering/concepts/diagnostic-fracture-injection-test.md](../../../production-engineering/wiki/concepts/diagnostic-fracture-injection-test.md) — the DFIT methodology for unconventional-reservoir permeability estimation.
- [production-engineering/concepts/hydraulic-fracturing.md](../../../production-engineering/wiki/concepts/hydraulic-fracturing.md) — the downstream consumer of low-permeability reservoir characterization; frac-design optimization is driven by matrix permeability as a primary input.
