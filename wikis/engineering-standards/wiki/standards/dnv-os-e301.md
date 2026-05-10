---
title: "DNV-OS-E301 Position Mooring — bounded summary"
tags: ["dnv", "standards", "mooring", "metadata-only"]
added: 2026-05-02
last_updated: 2026-05-09
domain: engineering-standards
code_id: dnv-os-e301
publisher: DNV
revision: "2010"
revision_source: "/mnt/ace/O&G-Standards/DNV/DNV_OS_E301_(2010)_Position_Mooring.pdf"
verified_on: 2026-05-02
public_url: https://standards.dnv.com/explorer/
publisher_catalog_url: https://www.dnv.com/energy/standards-guidelines/
sources:
  - /mnt/ace/O&G-Standards/DNV/DNV_OS_E301_(2010)_Position_Mooring.pdf
extraction_policy: metadata-only
raw_copy_allowed: false
cross_links:
  - engineering/wiki/standards/dnv-os-e301.md
---

# DNV-OS-E301 Position Mooring

## Scope

DNV offshore standard providing design requirements for position mooring systems on floating offshore units (FPSOs, FSOs, semisubmersibles, MODUs, spars, TLPs in passive-mooring mode). Coverage includes:

- Mooring line strength acceptance under intact and damaged (one-line-failure) conditions;
- Fatigue limit-state acceptance for chain, wire rope, and synthetic fiber rope components;
- Anchor selection, holding-capacity verification, and proof-load criteria for fluke, drag-embedment, suction, and pile anchors;
- Design factors (partial safety factors) for consequence Class 1, Class 2, and Class 3 facilities;
- Thruster-assisted mooring (DP-Class 0/1/2) and pure-passive configurations;
- Component certification, manufacturing inspection, and recertification basis.

The standard is the DNV companion to API RP 2SK and ISO 19901-7 in the global offshore-mooring standards triplet. The on-disk artifact is the 2010 edition; DNV consolidated the offshore-services rulebook into the DNV-ST-E301 / DNV-OS-E301 numbering system after the 2013 DNV-GL merger and the 2021 GL-divestiture rebrand.

## Revision history

- **2010 edition** — On-disk reference revision (`/mnt/ace/O&G-Standards/DNV/DNV_OS_E301_(2010)_Position_Mooring.pdf`). The 2010 edition aligned the line-component fatigue framework with the parallel S-N / T-N methodology in DNV-RP-C203 (fatigue assessment of offshore steel structures).
- **2008 edition** — Earlier revision also held on disk (`(2008)` artifact); predecessor consequence-class formulation.
- **Post-2013 (DNV GL era)** — Republished under the DNV-GL service-document scheme; numerical safety factors and consequence-class definitions remained backward-compatible at the typical-engineering-precision level.
- **2021 onward (DNV rebrand)** — Document is currently in the DNV-OS / DNV-ST split; users should verify the current portal revision against the on-disk 2010 reference when emitting calc citations against newer field developments.

## Key sections

- **Sec. 1 — General** — purpose, applicability, references.
- **Sec. 2 — Environmental conditions and loads** — metocean inputs to mooring response (wind, wave, current spectra), reference-period selection, wave-frequency vs low-frequency response decomposition.
- **Sec. 3 — Mooring system analysis** — quasi-static and dynamic analysis methods, time-domain vs frequency-domain selection, low-frequency damping treatment.
- **Sec. 4 — Strength analysis (ULS)** — line-tension acceptance for intact and one-line-damaged conditions, partial safety factors keyed to consequence class.
- **Sec. 5 — Fatigue limit state** — T-N curve methodology for chain and wire, fatigue safety factors, in-service inspection planning interaction.
- **Sec. 6 — Mooring equipment** — chain, wire rope, fiber rope, connectors, fairleads, winches, stoppers; manufacturing and certification.
- **Sec. 7 — Anchors** — drag-embedment, suction, pile, gravity anchor design and proof-load testing.
- **Sec. 8 — Tests + commissioning** — line-installation proof tension, system commissioning, periodic recertification.

## Practitioner application

In practice, DNV-OS-E301 is the cited basis for:

- **Mooring safety factors** (intact ULS, damaged ULS, fatigue limit state) by consequence class — used in `digitalmodel/src/digitalmodel/orcaflex/mooring_design.py` and the broader `digitalmodel/src/digitalmodel/marine_ops/` mooring stack;
- **Fatigue T-N curves** for chain (studless and studlink) and spiral-strand wire — paired with DNV-RP-C203 S-N curves at structural connections;
- **Anchor holding-capacity** acceptance criteria and proof-load specification for procurement and offshore commissioning;
- **Documentation deliverables** (Mooring Analysis Report, Mooring System Description, In-Service Inspection Plan) that DNV class surveyors expect at certification.

## Industry adoption

- **DNV-classed FPSOs and MODUs worldwide** — primary acceptance basis;
- **North Sea operators** — DNV-OS-E301 is the regional default; UK HSE and Norwegian PSA both reference DNV class for mooring acceptance on installations they regulate;
- **Global EPC contractors** — typically work to a "DNV-OS-E301 OR API RP 2SK / ISO 19901-7" dual-acceptance basis on multi-class projects, with the operator's classification society driving the primary standard;
- **Brazilian, West African, and Asia-Pacific operators** — frequent secondary or co-cited use alongside ISO 19901-7 and API RP 2SK.

## Why this page exists

This page is the citation resolver target for the calc-citation pilot in `digitalmodel/src/digitalmodel/orcaflex/mooring_design.py`, which cites DNV-OS-E301 mooring safety factors. The engineering-domain peer page `engineering/wiki/standards/dnv-os-e301.md` is prose-rich and lacks `extraction_policy: metadata-only` frontmatter; per cross-wiki uniqueness contract, this engineering-standards page is the resolver-preferred target. The page contains no clause text or formula reproductions.

## Where to find the full text

- Raw PDF (2010 edition): `/mnt/ace/O&G-Standards/DNV/DNV_OS_E301_(2010)_Position_Mooring.pdf` (read-only, vendor-derivative; do not copy into git)
- Earlier revision on disk: `(2008)`
- Publisher catalog and free full-text portal: https://standards.dnv.com/explorer/
- Internal callers: `digitalmodel/src/digitalmodel/orcaflex/mooring_design.py` and broader marine-ops modules (35 hits total)

## Cross-references

- [dnv-rp-c203](dnv-rp-c203.md) — fatigue assessment of offshore steel structures; mooring fatigue uses parallel S-N / T-N methodology
- [dnv-rp-c205](dnv-rp-c205.md) — environmental conditions and environmental loads input to position mooring response
- [dnv-os-f201](dnv-os-f201.md) — dynamic risers companion offshore standard (TLP / FPSO riser systems)
- [api-rp-2sk](api-rp-2sk.md) — API peer mooring standard, frequently co-cited
- [iso-19901-7](iso-19901-7.md) — ISO peer stationkeeping standard, frequently co-cited
- Calc citation contract: `.claude/rules/calc-citation-contract.md`

**Cross-wiki (engineering)**: [DNV-OS-E301 — Position Mooring](../../../engineering/wiki/standards/dnv-os-e301.md) — similar slugs (100%); similar titles (74%); shared tags: dnv, mooring; shared entities: DNV, DNV-OS-E301
