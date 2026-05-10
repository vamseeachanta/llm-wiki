---
title: "ASME BPVC Section IX — Welding, Brazing, and Fusing Qualifications (bounded summary)"
tags: ["asme", "bpvc", "standards", "welding", "metadata-only"]
added: 2026-05-02
last_updated: 2026-05-09
domain: engineering-standards
code_id: asme-bpvc-ix
publisher: ASME
revision: "2010"
revision_source: "/mnt/ace/O&G-Standards/ASME/asme.bpvc.ix.2010.pdf"
publisher_current_edition: "2023"
methodology_status: "unknown"
verified_on: 2026-05-02
public_url: https://www.asme.org/codes-standards/bpvc-standards
publisher_catalog_url: https://www.asme.org/codes-standards/find-codes-standards
sources:
  - /mnt/ace/O&G-Standards/ASME/asme.bpvc.ix.2010.pdf
extraction_policy: metadata-only
raw_copy_allowed: false
---

# ASME BPVC Section IX — Welding, Brazing, and Fusing Qualifications (bounded summary)

## Scope

BPVC Section IX establishes qualification requirements for welding, brazing, and fusing procedures and for the personnel performing those operations on Code-stamped construction. Coverage includes:

- Welding Procedure Specifications (WPS) and Procedure Qualification Records (PQR) governing welding on pressure vessels, piping, and boilers;
- Welder Performance Qualification (WPQ) and Welding Operator Performance Qualification (WOPQ);
- Brazing Procedure Specifications (BPS) and Brazer Performance Qualification (BPQ);
- Fusing Procedure Specifications (FPS) for nonmetallic and polyethylene piping (added in modern revisions);
- Essential, supplementary essential, and nonessential variables that govern when requalification is required;
- P-Number, F-Number, and A-Number groupings of base metals, filler metals, and weld-deposit chemistry;
- Standard test methods (mechanical bend, tensile, macro, fillet-weld) and acceptance criteria.

The standard is invoked by reference from BPVC Sections I, III, IV, VIII (Divisions 1, 2, 3), XII, and the ASME B31 piping codes (B31.1, B31.3, B31.4, B31.8, etc.) as the unified basis for procedure and personnel qualification across pressure-equipment construction.

## Revision history

- **Pre-1971** — Welding qualification rules originally embedded in individual BPVC construction sections.
- **1971** — Section IX consolidated into a separate BPVC section serving as the unified qualification reference for all construction sections.
- **1980s — 1990s** — Progressive expansion of P-Number / F-Number groupings and welding-process coverage (GTAW, GMAW, FCAW, SAW, PAW additions).
- **2010 edition** — On-disk reference revision (`/mnt/ace/O&G-Standards/ASME/asme.bpvc.ix.2010.pdf`); modern essential-variable framework with QW-461 weld-orientation figures.
- **2013 / 2015 / 2017 / 2019 / 2021 / 2023 editions** — Modern two-year ASME BPVC code-cycle revisions, including the 2010s addition of plastic-pipe fusing rules and ongoing alignment with AWS D1.1 / D1.6 personnel-qualification practice.

## Key sections

- **Part QG — General Requirements** — definitions, responsibilities, units.
- **Part QW — Welding** —
  - QW-100 to QW-300: general, procedure qualification, performance qualification.
  - QW-400 series: variables (essential, supplementary essential, nonessential) by process and joint type.
  - **QW-461 figures** — weld-test-coupon orientation positions (1G/2G/3G/4G/5G/6G groove, 1F/2F/3F/4F/5F/6F fillet) governing welder-performance position qualification.
  - QW-470 series: tables of base metals, filler metals, P/F/A-Numbers.
  - QW-480 series: standard welding variables.
- **Part QB — Brazing** — brazing-specific procedure and performance rules.
- **Part QF — Plastic Fusing** — polyethylene and other plastic-pipe fusion qualification.
- **PQR-by-rule vs PQR-by-test** — modern Section IX permits some standard-WPS adoption (Standard Welding Procedure Specifications, SWPS) without project-specific PQR, alongside the historical project-specific PQR-by-test path.

## Practitioner application

In practice, BPVC Section IX is the cited basis for:

- **Refinery and petrochemical construction** — every shop and field weld on pressure vessels (Section VIII Div 1 / Div 2), process piping (B31.3), and utility piping (B31.1) is qualified per Section IX;
- **Offshore topsides and subsea fabrication** — ASME-stamped pressure equipment on platforms and FPSOs uses Section IX qualification, often in parallel with AWS D1.1 for structural welding;
- **LNG facility construction** — cryogenic-service vessels and piping require Section IX qualification with low-temperature impact-testing supplementary essential variables;
- **Pipeline construction** — B31.4 (liquid) and B31.8 (gas) reference Section IX for procedure and welder qualification, alongside API 1104 as an alternative on cross-country pipelines;
- **Documentation deliverables** — WPS, PQR, WPQ records signed by the Manufacturer and witnessed by the Authorized Inspector; retained in the Manufacturer's Quality Control records and shared with the Owner / Operator.

## Industry adoption

- **Mandatory under BPVC Section VIII (all divisions)** — every Code-stamped pressure-vessel weld is qualified per Section IX.
- **Mandatory under ASME B31.x piping codes** — B31.3 process piping, B31.1 power piping, B31.4 / B31.8 pipeline transport all reference Section IX for welder and procedure qualification.
- **Globally adopted via national code references** — jurisdictions referencing ASME BPVC (United States, Canada CSA B51, and via equivalence acceptance in many international markets) require Section IX qualification on pressure-equipment construction.
- **EPC contractor practice** — typically maintain libraries of pre-qualified WPS / PQR per Section IX P-Number groupings to streamline project mobilization.
- **Inspection-authority reliance** — Authorized Inspectors and third-party inspection agencies treat Section IX records as the primary qualification audit trail.

## Why this page exists

This page is a citation resolver target for downstream calc modules per `.claude/rules/calc-citation-contract.md`. Section IX is the qualification basis for every weld covered by the B31.x and Section VIII calc paths in the in-scope codebase. Contains no clause text, no formulas, and no qualification-variable tables from the source — only public metadata and practitioner-context for resolver use.

## Where to find the full text

- Raw PDF (2010 edition): `/mnt/ace/O&G-Standards/ASME/asme.bpvc.ix.2010.pdf` (read-only, vendor-derivative; do not copy into git per #2482)
- Publisher catalog: https://www.asme.org/codes-standards/bpvc-standards
- Internal callers: `digitalmodel/src/digitalmodel/` modules resolving welding-qualification compliance markers

## Cross-references

- [asme-b31-3](asme-b31-3.md) — process piping welds qualified per Section IX
- [asme-bpvc-viii-1](asme-bpvc-viii-1.md) — pressure-vessel welds qualified per Section IX (Division 1)
- [asme-bpvc-viii-2](asme-bpvc-viii-2.md) — pressure-vessel welds qualified per Section IX (Division 2)
- [asme-bpvc-ii-c](asme-bpvc-ii-c.md) — welding rods, electrodes, and filler metals (F-Number groupings)

**Cross-wiki bridge (lng-projects):**

- [IMO IGC Code](../../../lng-projects/wiki/standards/igc-code.md) — **bidirectional bridge**: ASME BPVC Section IX (Welding, Brazing, and Fusing Qualifications) governs Welding Procedure Specifications (WPS), Procedure Qualification Records (PQR), and Welder Performance Qualifications (WPQ) for pressure-containment construction. IGC Code Chapter 6 (Materials of Construction) imports ASME Section IX by reference for **cargo-tank welding qualification** on Type-B Moss spherical tanks, Type-B SPB self-supporting prismatic tanks, and Type-C pressure tanks; the membrane-system anchor welds connecting GTT NO 96 / Mark III primary and secondary barriers to the inner-hull steel structure also qualify under Section IX with cryogenic-toughness supplementary essential variables (Charpy V-notch impact testing at −196 °C). The 9% Ni cargo-tank-plate welds (ASTM A553 Type I) require Section IX qualification with QW-403 base-metal-grouping P-Number 11A and QW-404 filler-metal F-Number 43 (matching nickel-base ENiCrFe-X consumables) per the IGC Ch.6 envelope. Class-society gas-carrier rules (ABS, DNV, LR, BV, ClassNK) implement IGC welding-qualification scope by invoking Section IX rather than publishing parallel welding-qualification rules.

- Calc citation contract: `.claude/rules/calc-citation-contract.md`
