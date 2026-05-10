---
title: "ASME B16.5 — Pipe Flanges and Flanged Fittings NPS 1/2 through NPS 24 (bounded summary)"
tags: ["asme", "standards", "flanges", "metadata-only"]
added: 2026-05-02
last_updated: 2026-05-09
domain: engineering-standards
code_id: asme-b16-5
publisher: ASME
revision: "2013"
revision_source: "/mnt/ace/O&G-Standards/ASME/BS/ASME B16.5-2013.pdf"
publisher_current_edition: "2020"
methodology_status: "unknown"
verified_on: 2026-05-02
public_url: https://www.asme.org/codes-standards/find-codes-standards/b16-5-pipe-flanges-flanged-fittings-nps-12-nps-24-metric-inch-standard
sources:
  - /mnt/ace/O&G-Standards/ASME/BS/ASME B16.5-2013.pdf
extraction_policy: metadata-only
raw_copy_allowed: false
---

# ASME B16.5 — Pipe Flanges and Flanged Fittings NPS 1/2 through NPS 24 (bounded summary)

## Scope

ASME B16.5 covers pipe flanges and flanged fittings in nominal pipe sizes one-half through twenty-four inches and in pressure classes from the lowest standard rating up through the highest commonly tabulated rating. Coverage includes pressure-temperature ratings, materials, dimensions, tolerances, marking, and testing for the in-scope flange and flanged-fitting products. The standard is the canonical reference for bolted-flange-joint geometry and rating consumed by the ASME B31 piping codes (B31.1, B31.3, B31.4, B31.8) and by ASME BPVC Section VIII pressure-vessel nozzles when the nozzle terminates in a B16.5 flange. Flanges above NPS 24 fall under the companion standard ASME B16.47 (Series A and Series B large-diameter flanges) and are out of scope for B16.5.

## Revision history

- **B16.5 lineage** — Originating as the ANSI/ASA B16.5 standard, B16.5 has been the dominant U.S.-jurisdiction flange-rating standard for several decades, evolving in step with the B31 piping family and the BPVC Section II Part D allowable-stress framework.
- **2013 edition** — On-disk reference revision (`/mnt/ace/O&G-Standards/ASME/BS/ASME B16.5-2013.pdf`).
- **2017 / 2020 editions** — Modern code-cycle revisions following ASME's published cadence; users emitting calc citations against current projects should re-pin to the publisher's currently active edition.
- **2024 cycle** — Most recent publisher cycle for the standard; minor editorial alignment with B16.47 large-flange nomenclature and the BPVC Section II Part D allowable-stress reset that propagates into B16.5 pressure-temperature ratings.

## Key sections

B16.5 is organised around dimension and rating tables tied to flange Class. The standard tabulates pressure-temperature ratings for seven flange Classes — **150, 300, 400, 600, 900, 1500, and 2500** — across the listed material groups (carbon steel, low-alloy, stainless, nickel alloys), and dimensional data for the standard face configurations:

- **Raised Face (RF)** — the workhorse process-piping face with a small raised seating area, paired with sheet, spiral-wound, or kammprofile gaskets.
- **Ring-Type Joint (RTJ)** — high-pressure / high-temperature face with a machined groove for an octagonal or oval metal ring gasket; standard for higher-class refining and offshore service where leak-tightness above Class 600 governs.
- **Flat Face (FF)** — full-face seating used against cast-iron flanges or thermoplastic / GRP equipment to avoid bolt-tightening-induced flange-bending failures.
- **Tongue-and-Groove and Male-and-Female** — recessed faces used in specific process services where gasket retention or alignment matters.

Companion data covered: bolt-circle diameter, number and size of bolt holes, hub and neck dimensions for weld-neck / slip-on / socket-weld / lap-joint / threaded / blind flange types, and flange-thickness tolerances. The standard also defines the marking convention (manufacturer, material, Class, size) and the hydrostatic shell test pressure for flanged fittings.

## Practitioner application

In practice, ASME B16.5 is the cited basis for:

- **Flange-rating selection** — the design pressure-temperature operating point determines minimum Class on the rating curve (the design point must fall on or below the rating line for the chosen material group); the standard's tabulated ratings are the resolver target for most calc-side flange-class lookups.
- **Bolt-circle and bolt-up calculations** — bolt material, bolt area, and target preload are derived from B16.5 flange dimensions combined with ASME PCC-1 (Guidelines for Pressure Boundary Bolted Flange Joint Assembly) on the assembly side; B16.5 provides the geometry, PCC-1 provides the assembly methodology.
- **Equipment-nozzle interface design** — pressure vessels (BPVC Section VIII Div 1 / Div 2) and rotating equipment (API 610 pumps, API 617 compressors) terminate process-piping interfaces in B16.5 flanges; the nozzle bolt-load capacity must match the connecting B16.5 flange-class capacity.
- **Material group selection** — Class rating curves vary with material group (Group 1.1 carbon steel, Group 2.x stainless, etc.), so material substitution requires re-checking the design point against the new group's rating curve.

## Industry adoption

- **U.S. refining and petrochemical** — dominant flange standard for onshore process-plant piping; refiner / petrochem owner specifications routinely require B16.5 flanges for NPS 1/2 through 24 with B16.47 above.
- **Offshore topsides and subsea** — used on topsides process piping and on subsea structures where API 6A (wellhead / Christmas-tree) flanges are not the controlling specification; subsea hydrocarbon-process flanges typically follow API 6A above the wellhead boundary and B16.5 below the process-fence.
- **LNG facilities** — used for cryogenic and ambient-temperature process piping, with the material-group rating curves driving stainless / nickel-alloy selection for cryogenic service down to LNG temperatures (~-162 °C).
- **Power, pulp-and-paper, pharma, chemical** — referenced via ASME B31.1 (power) and B31.3 (process); B16.5 is effectively the universal U.S.-jurisdiction process-flange standard, with international acceptance via ASME-equivalence or harmonised national codes (CSA Canada, AS/NZS via local adoption).

## Why this page exists

Resolver target for digitalmodel `Citation` instances per `.claude/rules/calc-citation-contract.md`. Contains no clause text, no pressure-temperature rating tables, and no dimensional tables from the source. Downstream callers wire flange-class rating lookups through this page rather than parsing the source PDF. B16.5 is the canonical flange-rating consumer for the B31.x process and pipeline calc paths and pairs with PCC-1 on the assembly side.

## Where to find the full text

- Raw PDF: `/mnt/ace/O&G-Standards/ASME/BS/ASME B16.5-2013.pdf` (read-only, vendor-derivative; do not copy into git per #2482)
- Publisher catalog: https://www.asme.org/codes-standards/find-codes-standards/b16-5-pipe-flanges-flanged-fittings-nps-12-nps-24-metric-inch-standard
- Internal callers: `digitalmodel/src/digitalmodel/` modules resolving flange-class pressure-temperature ratings

## Cross-references

- [asme-pcc-1](asme-pcc-1.md) — assembly-side complement governing bolt-up methodology
- [asme-b16-34](asme-b16-34.md) — valve flange-rating cross-link (valves rated to the same Class system)
- [asme-b16-47](asme-b16-47.md) — large-diameter flanges above NPS 24 (Series A / Series B)
- [asme-b31-3](asme-b31-3.md) — process-piping consumer
- [asme-b31-4](asme-b31-4.md) — liquid-pipeline consumer
- [asme-bpvc-viii-1](asme-bpvc-viii-1.md) — pressure-vessel-nozzle flange interface
- [asme-bpvc-ii-d](asme-bpvc-ii-d.md) — material allowable stresses sourced upstream of the rating curves
- [Calc citation contract](../../../../../.claude/rules/calc-citation-contract.md)
