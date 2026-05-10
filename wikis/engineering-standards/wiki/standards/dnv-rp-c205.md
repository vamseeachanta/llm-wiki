---
title: "DNV-RP-C205 Environmental Conditions and Environmental Loads — bounded summary"
tags: ["dnv", "standards", "environmental-loads", "metocean", "metadata-only"]
added: 2026-05-02
last_updated: 2026-05-09
domain: engineering-standards
code_id: dnv-rp-c205
publisher: DNV
revision: "2010"
revision_source: "/mnt/ace/O&G-Standards/DNV/DNV_RP_C205_(2010)_Environmental_Conditions_and_Environmental_Loads.pdf"
verified_on: 2026-05-02
public_url: https://standards.dnv.com/explorer/
publisher_catalog_url: https://www.dnv.com/energy/standards-guidelines/
sources:
  - /mnt/ace/O&G-Standards/DNV/DNV_RP_C205_(2010)_Environmental_Conditions_and_Environmental_Loads.pdf
extraction_policy: metadata-only
raw_copy_allowed: false
---

# DNV-RP-C205 Environmental Conditions and Environmental Loads

## Scope

DNV recommended practice providing methodology for selecting environmental conditions and computing environmental loads on offshore and coastal structures. Coverage includes:

- Wind climate parameterization (mean-wind profiles, gust spectra, turbulence intensity, directionality);
- Wave climate description (significant wave height, peak period, spectral models — JONSWAP, Pierson-Moskowitz, Torsethaugen — short-crested vs long-crested seas);
- Current profiles (tidal, wind-driven, density-driven, loop currents) and combined wave-current kinematics;
- Tide and storm-surge water-level components;
- Sea-ice and iceberg load definitions for arctic and sub-arctic deployments;
- Earthquake ground motion for offshore foundations where seismic activity governs;
- Marine growth thickness, density, and roughness for hydrodynamic-load adjustment;
- Design environmental contour (DEC) methodology for joint wave-wind-current return-period selection.

The RP is the canonical metocean-input source for the DNV offshore-design suite and is referenced by virtually every downstream DNV offshore-services document for load definition.

## Revision history

- **2010 edition** — On-disk reference revision (`/mnt/ace/O&G-Standards/DNV/DNV_RP_C205_(2010)_Environmental_Conditions_and_Environmental_Loads.pdf`). Aligned the metocean-input framework with parallel updates to DNV-OS-C101 (design of offshore steel structures).
- **2007 edition** — Earlier revision also held on disk (`(2007)` artifact); precursor wave-spectrum and current-profile formulation.
- **Origin** — RP-C205 traces to mid-1990s DNV consolidation of metocean guidance previously distributed across multiple class notes and rules.
- **Post-2013 (DNV GL era)** — Republished under the DNV-GL service-document scheme; spectral models and design-contour methodology remained backward-compatible.
- **Post-2021 (DNV rebrand) through 2023** — Document continues in the DNV-RP series; users should verify the current portal revision against the on-disk 2010 reference for new field developments.

## Key sections

- **Sec. 1 — Introduction** — purpose, applicability, references, definitions.
- **Sec. 2 — Environmental conditions** — return-period selection, joint-probability framework, design environmental contour.
- **Sec. 3 — Wind conditions** — mean-wind profile, gust factor, Kaimal / Davenport spectra, turbulence intensity.
- **Sec. 4 — Wave conditions** — JONSWAP, Pierson-Moskowitz, Torsethaugen spectra; short-crested seas; rogue wave treatment.
- **Sec. 5 — Current** — tidal, wind-driven, density-driven, loop-current profiles; wave-current interaction.
- **Sec. 6 — Water level** — tide, storm surge, atmospheric-pressure components.
- **Sec. 7 — Ice** — sea-ice and iceberg load definitions for arctic deployments.
- **Sec. 8 — Marine growth** — thickness, density, roughness for hydrodynamic-coefficient adjustment.
- **Sec. 9 — Combined environmental loads** — Morison-equation regimes, drag and inertia coefficients, diffraction-regime selection.

## Practitioner application

In practice, DNV-RP-C205 is the cited basis for:

- **Metocean input specifications** (wind, wave, current spectra) for offshore platforms, FPSOs, FLNG/FSRU, jacket structures, semisubmersibles, spars, TLPs, and subsea systems;
- **Morison-equation hydrodynamic coefficients** (drag Cd, inertia Cm) for slender-member loading on jackets, risers, and pipelines — used in `digitalmodel/src/digitalmodel/` modules covering wave-load and current-load calculation;
- **Design environmental contour** selection for joint-probability load combinations (e.g., 100-year wave with associated wind and current);
- **Marine growth profiles** for hydrodynamic re-coefficient adjustment over service life;
- **Documentation deliverables** (Metocean Design Basis, Environmental Load Report) that DNV class surveyors expect at design certification.

## Industry adoption

- **DNV-classed offshore facilities worldwide** — primary metocean and environmental-load acceptance basis;
- **ABS / BV / LR class procedures** — frequently reference DNV-RP-C205 as an acceptable alternative to in-house metocean methodology, particularly on multi-class projects;
- **ISO 19901-1** (Metocean design and operating considerations) — closely aligned scope; many EPC contractors work to a "DNV-RP-C205 OR ISO 19901-1" dual-acceptance basis;
- **North Sea, Brazilian, West African, and Asia-Pacific operators** — RP-C205 is broadly accepted as a defensible metocean methodology globally;
- **Onshore wind and bridge engineering** — wind-spectra sections occasionally referenced for non-offshore structures, though ISO 4354 and Eurocode EN 1991-1-4 are typically preferred onshore.

## Why this page exists

This page is a citation resolver for downstream calc modules under the calc-citation contract at `.claude/rules/calc-citation-contract.md`. It contains no clause text, parameter tables, or formula reproductions from the source. RP-C205 is the canonical environmental-loads input for many DNV calc paths; 63 internal-reference hits in `digitalmodel` make it a high-priority resolver target alongside the position-mooring (E301) and fatigue (C203) standards.

## Where to find the full text

- Raw PDF (2010 edition): `/mnt/ace/O&G-Standards/DNV/DNV_RP_C205_(2010)_Environmental_Conditions_and_Environmental_Loads.pdf` (read-only, vendor-derivative; do not copy into git)
- Older edition on disk: `(2007)` of the same title
- Publisher catalog and free full-text portal: https://standards.dnv.com/explorer/
- Internal callers: `digitalmodel/src/digitalmodel/` (63 hits)

## Cross-references

- [dnv-os-e301](dnv-os-e301.md) — position mooring uses RP-C205 environmental load definitions
- [dnv-rp-c203](dnv-rp-c203.md) — fatigue stress histories driven by RP-C205 wave climate
- [dnv-rp-b401](dnv-rp-b401.md) — cathodic-protection design uses RP-C205 current and marine-growth inputs
- [dnv-rp-h103](dnv-rp-h103.md) — marine operations modelling uses RP-C205 metocean inputs
- [dnv-rp-f109](dnv-rp-f109.md) — on-bottom pipeline stability uses RP-C205 wave-current loads
- [dnv-os-f201](dnv-os-f201.md) — dynamic-riser environmental load input
- [iso-19901-1](iso-19901-1.md) — ISO peer metocean standard, frequently co-cited
- Calc citation contract: `.claude/rules/calc-citation-contract.md`

**Cross-wiki (engineering)**: [DNV-RP-C205: Environmental Conditions and Loads](../../../engineering/wiki/standards/dnv-rp-c205.md) — similar slugs (100%); similar titles (74%); shared tags: dnv; shared entities: DNV, DNV-RP-C205
**Cross-wiki (engineering)**: [DNV-RP-C203: Fatigue Design](../../../engineering/wiki/standards/dnv-rp-c203.md) — similar slugs (91%); shared tags: dnv; shared entities: DNV, DNV-RP-C205
