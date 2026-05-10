---
title: "ASCE 7 — Minimum Design Loads and Associated Criteria for Buildings and Other Structures (bounded resolver)"
slug: asce-7
tags: ["asce", "wind-loads", "seismic-loads", "snow-loads", "live-loads", "minimum-design-loads", "us-onshore", "metadata-only"]
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
code_id: asce-7
publisher: ASCE
revision: "ASCE/SEI 7-22 (publisher-current); local catalog holds ASCE 7-05 as best-catalogued edition; revision history spans 7-98 → 7-02 → 7-05 → 7-10 → 7-16 → 7-22"
publisher_current_edition: "ASCE/SEI 7-22"
jurisdiction: "United States (referenced by IBC, NFPA 5000, and adopted as code by most US jurisdictions); informative reference outside US"
instrument_type: standard
supersedes: None
extraction_policy: metadata-only
raw_copy_allowed: false
sources:
  - ../sources/og-standards-asce.md
  - https://ascelibrary.org/doi/book/10.1061/9780784415788
public_url: https://ascelibrary.org/doi/book/10.1061/9780784415788
publisher_catalog_url: https://www.asce.org/publications-and-news/asce-7
---

# ASCE 7 — Minimum Design Loads and Associated Criteria for Buildings and Other Structures (bounded resolver)

> Bounded metadata-only standards page. Per llm-wiki spinout governance (2026-05-05), vendor PDFs are not copied into this repo; this page records only publisher facts and a domain-knowledge scope description. No clause text, basic-wind-speed-map reproductions, response-spectrum-coefficient tables, or pressure-coefficient-figure reproductions are included.
> **code_id:** `asce-7` &nbsp;•&nbsp; **publisher:** American Society of Civil Engineers (ASCE) / Structural Engineering Institute (SEI) &nbsp;•&nbsp; **revision:** ASCE/SEI 7-22 publisher-current; the local O&G-Standards catalog records ASCE 7 across multiple editions (best-catalogued: 7-05).

## Scope

ASCE 7 — *Minimum Design Loads and Associated Criteria for Buildings and Other Structures* — is the **dominant US load standard** referenced by the International Building Code (IBC), NFPA 5000, and most state and local building codes. It specifies the **minimum design loads** that a structural-engineering analysis must consider for buildings and a wide range of "other structures" (including industrial facilities, towers, tanks, equipment supports, and selected onshore oil-and-gas-facility components).

Load chapters covered:

- **Dead loads** (Chapter 3) — self-weight of permanent components.
- **Live loads** (Chapter 4) — occupancy, use, and concentrated load schedules; reduction provisions.
- **Soil and hydrostatic pressure** (Chapter 3 / earth-retaining provisions).
- **Rain loads** (Chapter 8) — ponding and primary-drainage scenarios.
- **Snow and ice loads** (Chapters 7, 10) — ground snow contour map, exposure-factor adjustments, drift, ice from freezing rain.
- **Atmospheric ice loads** (Chapter 10) — for transmission, communication, and equipment-support structures.
- **Wind loads** (Chapters 26–31) — the offshore-and-onshore industrial workhorse; basic-wind-speed contour maps with hurricane-coast 700-yr ultimate envelope, MWFRS (Main Wind Force Resisting System) and C&C (Components and Cladding) splits, directionality and gust-effect factors, topographic-effect factor K_zt, and exposure-category C/D adjustments.
- **Seismic loads** (Chapters 11–22) — Risk Category, Site Class, response-spectrum coefficients (S_S, S_1), Seismic Design Category, equivalent-lateral-force and modal-response-spectrum analysis methods, design-coefficient tables (R, Ω_0, C_d).
- **Tsunami loads** (Chapter 6, added in 7-16) — for tsunami-prone US Pacific coastline structures.
- **Flood loads** (Chapter 5) — hydrodynamic, hydrostatic, wave, and debris-impact loads in flood-hazard zones.
- **Load combinations** (Chapter 2) — LRFD and ASD combinations that govern controlling design forces.

ASCE 7 is the **referenced wind-load code** for US onshore industrial facilities — refining, downstream chemical, LNG-onshore, terminals, gas-processing — that fall outside the offshore metocean envelope of [api-rp-2met](api-rp-2met.md), [dnv-rp-c205](dnv-rp-c205.md), [iso-19901-1](iso-19901-1.md), and the offshore wind-and-wave class society guidance. For seismic, it is the load-side companion to ACI 318 / AISC 341 / ASME equipment-design standards.

## Revision history

ASCE 7 evolves on a roughly six-year cycle synchronized with IBC adoption rounds:

| Edition | Year | Status | Notes |
|---------|------|--------|-------|
| ASCE 7-95 | 1995 | superseded | Pre-ATC modern-revision baseline. |
| ASCE 7-98 | 1998 | superseded | Modern wind-load substantive revision (700-yr basic wind speeds introduced for hurricane coast). |
| ASCE 7-02 | 2002 | superseded | Refinements to wind-load directionality and seismic Site Class. |
| ASCE 7-05 | 2005 | superseded | **Best-catalogued edition in the local O&G-Standards corpus** per [og-standards-asce](../sources/og-standards-asce.md); referenced by IBC 2006/2009. |
| ASCE 7-10 | 2010 | superseded | Risk-targeted seismic ground motions (MCE_R) introduced; wind-speed map switch to ultimate strength-design basis. |
| ASCE 7-16 | 2016 | superseded | Tsunami chapter added; further wind-load refinements. |
| ASCE/SEI 7-22 | 2022 | **publisher-current** | Most recent edition; fire-load chapter under development for future editions. Adopted by IBC 2024. |

## Key sections

- **Chapters 26–31 (wind):** basic-wind-speed map (V) by Risk Category, exposure category (B/C/D) reflecting upwind terrain roughness, gust-effect factor (G or G_f), directionality factor K_d, topographic factor K_zt, velocity-pressure exposure coefficient K_z and K_h, **velocity pressure** q_z = 0.00256·K_z·K_zt·K_d·V² (lb/ft²; metric form with 0.613 coefficient gives Pa), MWFRS pressure coefficients (C_p) and C&C pressure coefficients (GC_p); special envelopes for low-rise buildings, open structures, parapets, signs, towers, and roof appurtenances.
- **Chapters 11–22 (seismic):** Risk Category I-IV, mapped MCE_R short- and 1-s spectral accelerations (S_S, S_1), Site Class A-F, site-coefficient F_a / F_v, design spectral accelerations S_DS / S_D1, Seismic Design Category (SDC) A-F, structural-system R / Ω_0 / C_d coefficients, equivalent-lateral-force base shear V = C_s · W, vertical distribution, story-drift limits, and load combinations including vertical seismic E_v.
- **Chapter 2 (load combinations):** LRFD combinations 1.4D; 1.2D + 1.6L + 0.5(L_r or S or R); 1.2D + 1.6(L_r or S or R) + (L or 0.5W); 1.2D + 1.0W + L + 0.5(L_r or S or R); 1.2D + 1.0E + L + 0.2S; 0.9D + 1.0W; 0.9D + 1.0E. ASD parallel set with 0.6 / 0.7 multipliers on seismic and wind contributions.

## Practitioner application

- **US onshore industrial facility wind design** — refineries, gas plants, onshore-LNG, tank farms, terminals, and pipeline metering / pumping facilities default to ASCE 7 wind for stack, equipment-support, vessel-wind, and structural-frame design. The wind-load result feeds vendor equipment qualification (vessel base-shear and overturning), pipe-rack analysis, and substation-structure design.
- **US seismic design** — Risk Category, SDC, and design coefficients drive the equivalent-lateral-force or modal-response-spectrum analysis used by ACI 318 / AISC 341 / ASME B31.1 / B31.3 for piping, vessels, and structures.
- **Onshore wind-load split (MWFRS vs C&C)** — global stability of the structural frame uses MWFRS coefficients; cladding, fasteners, parapet attachments, and roof-appurtenance design uses C&C coefficients with smaller-area-pressure amplification.
- **Hurricane-coast 700-yr basic wind speed envelope** — the wind speed contour map embeds the strength-level (700-yr return for Risk Category II) values; conversion to allowable-stress (50-yr) basis uses the 0.6 multiplier on velocity pressure.
- **Topographic effect K_zt** — required for sites on hills, ridges, and escarpments with H/L_h > 0.2 and other geometric thresholds.
- **Exposure category** — terrain-roughness-driven (B = urban / suburban; C = open; D = open water / unobstructed coast); selection drives K_z magnitude.

## Industry adoption

ASCE 7 is the **referenced load standard** of the IBC, NFPA 5000, and most US state / local building codes. Adoption is essentially universal for US-jurisdictional onshore facilities. Outside the US, ASCE 7 is referenced informationally and is sometimes specified by US-headquartered owners on international projects when no host-country code applies; otherwise EN 1991 (Eurocode 1) wind / seismic provisions govern in Europe, and country-specific codes elsewhere.

For offshore facilities, ASCE 7 is **not** the wind-load anchor — that role is filled by [api-rp-2met](api-rp-2met.md) (US-side metocean), [dnv-rp-c205](dnv-rp-c205.md) (DNV-class environmental loads), [iso-19901-1](iso-19901-1.md) (ISO offshore metocean), and class-society guidance.

## Why this page exists

This page is the citation resolver target for `code_id = asce-7` under `.claude/rules/calc-citation-contract.md`. W204 audit V9 surfaced `asce-7` as a substrate-gap slug — referenced explicitly from the [wind-loads](../concepts/wind-loads.md) concept page (W198 iter-42), which carried a "placeholder — not yet wiki-resolved" parenthetical for the link. This page closes that placeholder and provides the bounded metadata-only resolver for the broader US-onshore wind / seismic / general-load citing pattern.

## Where to find the full text

ASCE catalog (registration / purchase): `https://www.asce.org/publications-and-news/asce-7`; current edition publisher page: `https://ascelibrary.org/doi/book/10.1061/9780784415788`. ASCE provides commentary volumes alongside the standard. The publisher-derivative full text is **not** stored in this repo per the vendor-derivative deny-list governance. Calc-citation callers resolve only against this page's frontmatter (`code_id`, `publisher`, `revision`); they do not require body text.

## Cross-references

- [wind-loads](../concepts/wind-loads.md) — primary consumer concept page for ASCE 7 wind provisions; iter-42 W198 authored.
- [api-rp-2met](api-rp-2met.md) — US-side **offshore** metocean code; ASCE 7 is the onshore wind-load companion that picks up where API RP 2MET ends.
- [dnv-rp-c205](dnv-rp-c205.md) — DNV-class offshore environmental-load code; class-society parallel to ASCE 7 for the offshore branch.
- [iso-19901-1](iso-19901-1.md) — ISO offshore metocean code; international companion.
- [api-rp-14e](api-rp-14e.md) — offshore production-platform piping; uses offshore wind / wave / current rather than ASCE 7.
- [og-standards-asce](../sources/og-standards-asce.md) — parent source page recording ASCE 7 as the only ASCE code with standards content present in the local catalog (best-catalogued edition: 7-05).
- [Calc citation contract](../../../../../.claude/rules/calc-citation-contract.md) — emit a `Citation(...)` whenever a calc module hard-codes an ASCE 7-derived basic wind speed, pressure coefficient, exposure factor, design-spectral-acceleration coefficient, or load-combination factor.

## Sources

- [og-standards-asce](../sources/og-standards-asce.md) — parent source page (32 token-matched docs; wind / seismic / COPRI-MRE).
- Publisher catalog (current edition): https://www.asce.org/publications-and-news/asce-7
- Current edition product page: https://ascelibrary.org/doi/book/10.1061/9780784415788
