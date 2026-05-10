---
title: "ASTM A553 / A553M — Pressure Vessel Plates, Quenched and Tempered 8% and 9% Nickel"
slug: astm-a553
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
code_id: astm-a553
publisher: ASTM
revision: "latest at publisher (A553/A553M-17 family); confirm against publisher catalog"
public_url: https://www.astm.org/a0553_a0553m-17.html
extraction_policy: metadata-only
raw_copy_allowed: false
tags:
  - astm
  - a-series
  - pressure-vessel-plate
  - 9-percent-nickel
  - 8-percent-nickel
  - cryogenic
  - lng
  - quenched-and-tempered
  - igc-code
---

# ASTM A553 / A553M — Standard Specification for Pressure Vessel Plates, Alloy Steel, Quenched and Tempered 7%, 8%, and 9% Nickel

> **Standard identity (L0 prose).** `code_id`: astm-a553 · `publisher`: ASTM · `revision`: A553/A553M-17 family (confirm at publisher catalog).

## Scope

ASTM A553 / A553M covers **quenched-and-tempered nickel-alloyed plate** for **welded pressure vessels in cryogenic service**. The specification defines three nickel-content types — **Type I (9% Ni)**, **Type II (8% Ni)**, and **Type III (7% Ni — newer addition)** — each with specific minimum-yield, minimum-tensile, and Charpy V-notch impact-energy requirements down to design temperatures as low as **−196 °C (LNG, liquid nitrogen)** and **−170 °C (LNG cargo-tank inner shell)**. Type I (9% Ni) is the dominant LNG-industry grade for atmospheric-pressure cargo-tank inner shells, regasification-terminal storage tanks, and ground-storage cryogenic vessels.

The specification is invoked by:

- **ASME BPVC Section II Part A** as **SA-553 / SA-553M** for unfired pressure-vessel plate;
- **API Std 620 Appendix Q** for low-pressure refrigerated above-ground storage of LNG;
- **API Std 625** for LNG full-containment refrigerated storage tanks;
- **IMO IGC Code Chapter 6** for marine cargo-containment material qualification on LNG carriers and LNG bunker vessels;
- **EN 10028-4** carries the European technical-equivalent grades (X8Ni9 / 1.5662) for parallel European procurement.

## Why this page exists

Resolver target for `Citation(code_id="astm-a553", ...)` per `.claude/rules/calc-citation-contract.md`. A553 is the highest-frequency cryogenic-plate citation when LNG-tank, LNG-carrier-cargo-tank, or liquid-nitrogen-vessel calc modules emit standards-derived numeric constants (minimum-yield, Charpy-impact-energy floor, allowable-stress envelope). The IGC Code, API Std 620 Appendix Q, API Std 625, and ASME BPVC SA-553 all import A553 by reference; this page closes the resolver loop.

## Type taxonomy

| Type | Nominal nickel content | Indicative minimum-design temperature | Most-common service |
|------|------------------------|---------------------------------------|---------------------|
| **Type I** | 9% Ni | −196 °C | LNG cargo-tank inner shells (IGC Code Ch.6); LNG full-containment ground storage (API 625); large industrial liquid-nitrogen storage |
| **Type II** | 8% Ni | −170 °C | LNG storage where slightly relaxed temperature envelope applies; some FSRU and FLNG service |
| **Type III** | 7% Ni | −165 °C | Newer (post-2010) variant introduced for cost-optimized LNG storage; reduced nickel content with controlled microalloying |

Heat treatment is **double-normalized + tempered** or **quenched + tempered** depending on plate thickness and procurement; QT processing dominates for the heaviest sections used in LNG-tank annular plates and inner-shell barrel courses.

## Mechanical and chemical requirements

A553 specifies the following property and qualification envelopes (numerical values vary by Type and thickness):

- **Tensile properties.** Minimum yield (≥515 MPa for Type I in heavier sections), minimum tensile (≥690 MPa for Type I), and minimum elongation. Tested per [ASTM A370](astm-a370.md).
- **Charpy V-notch impact.** **Mandatory at the minimum design temperature** for the Type — typically −196 °C for Type I, −170 °C for Type II. Lateral-expansion criterion frequently applied as supplementary requirement; per IGC Code Ch.6 and API 625 the LNG industry overlays additional impact-energy floors above the base A553 envelope.
- **Chemistry.** Tight controls on C, Mn, P, S, Si, Ni; restricted residuals (P+S limits) for cryogenic toughness retention. Type-specific Ni-content envelopes drive the cryogenic-toughness performance.
- **Heat treatment.** Quenched-and-tempered or double-normalized-and-tempered per the Type; Type I QT plates are the dominant LNG-industry procurement.
- **NDE.** Ultrasonic examination required for plates above specified thickness and for Class-1 / Class-2 service categorization in the consumer code.

## Practitioner application

- **LNG terminal full-containment storage tanks** — outer-shell concrete, inner-shell A553 Type I 9% Ni plate. Tank diameters of 80–100 m and capacities of 180,000–270,000 m³ are typical post-2010 procurement.
- **LNG carrier cargo-tank inner shells** — 9% Ni plate is the dominant material for Moss-type spherical tanks (Type B) and Type-C pressure tanks; Invar (36% Ni) competes for membrane-tank primary barriers (GTT NO 96 / Mark III) but A553 dominates for self-supporting independent-tank construction.
- **FSRU / FLNG cargo-containment systems** — A553 Type I service extends to floating LNG storage with the additional dynamic-load and ship-motion fatigue overlay imposed by IGC Code Ch.4.
- **LNG bunker vessels** — Type-C pressure tanks for small-scale LNG bunkering use 9% Ni or austenitic stainless (304L) depending on cargo capacity and pressure rating.
- **Liquid nitrogen and oxygen storage** — A553 Type I serves industrial-gas cryogenic storage above the LNG sector.

## Cross-references

A553 sits at the convergence of LNG facility codes, marine cargo-containment codes, and ASME pressure-vessel design codes:

**Upstream test-method standard**

- **[ASTM A370](astm-a370.md)** — Mechanical testing of steel products. Qualifying test method for tension, Charpy V-notch impact, and hardness on every A553 Type.

**Sibling material specifications (alternative cryogenic plate procurement)**

- **ASTM A645 / A645M** — 5% Ni quenched-and-tempered plate for less demanding cryogenic service (down to ~−170 °C with reduced impact-energy floor).
- **ASTM A203 / A203M** — 2.25–3.5% Ni and 3.5% Ni plate for moderate-cryogenic service (−45 °C to −101 °C) — process-LPG tanks rather than LNG.
- **EN 10028-4** — European technical-equivalent procurement for X8Ni9 (1.5662); often co-specified for European LNG-terminal procurement.

**Downstream pressure-design + cryogenic-storage consumers**

- **ASME BPVC Section II Part A** — republishes A553 as **SA-553 / SA-553M** and tabulates allowable stress against design temperature in the BPVC II-D stress tables that ASME VIII-1 / VIII-2 consume for unfired pressure vessels.
- **ASME BPVC Section VIII Division 1 + 2** — design rules for LNG ground-storage and FSRU pressure vessels using SA-553 plate.
- **API Std 620 Appendix Q** — design and construction of low-pressure refrigerated above-ground storage tanks for LNG.
- **API Std 625** — Tank Systems for Refrigerated Liquefied Gas Storage; LNG full-containment tank consumer for A553 inner-shell plate. Co-cited with API 620 Appendix Q.
- **CSA Z276** — Canadian LNG facilities code; imports SA-553 for terminal storage in Canadian jurisdiction.
- **NFPA 59A** — US LNG facilities standard; references A553 for cryogenic-service plate.

**Wiki concept-page consumers**

- LNG storage-tank inner shells, FLNG / FSRU cargo containment, and LNG carrier Type-B / Type-C cargo-tank construction in the lng-projects wiki cite A553 by reference.

**Cross-wiki bridge (lng-projects)**

- [IGC Code](../../../lng-projects/wiki/standards/igc-code.md) — **bidirectional bridge**: IGC Code Chapter 6 (Materials of Construction) imports ASTM A553 Type I (9% Ni) by reference for marine cargo-containment qualification on LNG carriers, LNG bunker vessels, FSRUs, and FLNG units. The IGC Code overlays additional Charpy-impact-energy floors and lateral-expansion criteria above the A553 base envelope, plus dynamic-load and ship-motion fatigue overlays for marine service. Type-B Moss spherical tanks, Type-B SPB prismatic tanks, and Type-C pressure tanks all consume A553 plate through this delegation; membrane systems (GTT NO 96 / Mark III) compete with Invar (36% Ni) for the primary barrier but A553 dominates self-supporting independent-tank construction. Land-side LNG terminal storage (API 625, NFPA 59A, CSA Z276) and marine-side LNG cargo containment (IGC Code Ch.6) share A553 as the common cryogenic-plate substrate; this is the materials-of-construction convergence between the marine and terminal LNG codes.

**Wiki cross-links**

- [Calc citation contract](../../../../../.claude/rules/calc-citation-contract.md) — frontmatter contract (`code_id`, `publisher`, `revision`) this page satisfies for fail-closed citation resolution.

## Sources

- **Publisher catalog.** ASTM International — A553 / A553M product page at `https://www.astm.org/a0553_a0553m-17.html` and successor revisions (search "A553" at `https://www.astm.org`).
- **Cross-references in this wiki:** [`iso-15156.md`](iso-15156.md) cites A553 in the cryogenic-LNG materials context; this page is the resolver target.
