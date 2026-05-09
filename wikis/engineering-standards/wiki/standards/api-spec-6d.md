---
title: "API Spec 6D — Pipeline and Piping Valves"
slug: api-spec-6d
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
code_id: api-spec-6d
publisher: API
revision: "23e (catalog-latest, with Errata 1–6 + Addendum 1)"
tags:
  - api
  - valves
  - pipeline-equipment
  - ball-valve
  - gate-valve
  - plug-valve
  - check-valve
  - standards
  - api-spec
sources:
  - ../sources/og-standards-api.md
extraction_policy: metadata-only
raw_copy_allowed: false
---

# API Spec 6D — Pipeline and Piping Valves

> Bounded metadata-only standards page. Per llm-wiki spinout governance
> (2026-05-05), vendor PDFs are not copied into this repo; this page
> records only publisher facts and a domain-knowledge scope description.
> **code_id:** `api-spec-6d` &nbsp;•&nbsp; **publisher:** API
> &nbsp;•&nbsp; **revision:** 23rd edition (filename-tagged `e23`,
> dual-numbered with ISO 14313, plus Errata 1–6 and Addendum 1) is the
> latest edition present in the local catalog.

## Scope

API Specification 6D defines requirements for the **design, manufacture,
testing, and documentation of pipeline valves** used in hydrocarbon
transmission and gathering service — covering **ball, gate, plug, and
check valves**, together with their end connections, stem extensions,
operators, and accessory connections. The standard distinguishes
**pipeline service** — high-cycle, full-bore (full-port), pig-passable
trunkline duty — from the broader **piping service** category covered
by ASME B16.34 and the B31-series piping codes; it is the procurement
basis for valves on cross-country oil and gas pipelines, gathering
systems, terminals, and pump/compressor station block-valve stations.

The specification organises requirements around five families of
valves and three orthogonal grading axes:

- **Valve type** — ball (trunnion or floating), gate (slab or
  expanding), plug (lubricated, sleeved, or non-lubricated), and check
  (swing, axial/nozzle, dual-plate, lift) valves.
- **Pressure class** — ASME/ANSI Class 150, 300, 600, 900, 1500, and
  2500, plus API rated working pressures of 5,000 / 10,000 / 15,000
  psi for higher-rated upstream/midstream service.
- **Bore designation** — full opening (full-bore, pig-passable) versus
  reduced opening, with body-bore equivalence rules that govern the
  drift-test diameter for through-conduit configurations.

Sour-service valve qualification is layered on top via cross-reference
to [NACE / AMPP MR-0175 / ISO 15156](../standards/ampp-mr-0175-pt1.md);
fugitive-emission qualification is provided as an optional annex
(Annex F — see Key requirements below). Spec 6D is dual-numbered with
**ISO 14313** as the international parallel.

## Edition history

| Edition / year                                           | Catalog-detected artefacts                                                | Local catalog parent_root      |
| -------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------ |
| Earlier editions (Errata-only artefacts; base PDF absent) | `6D Errata 4 FEDF2d01.pdf` (2011-06), `6D errata 1547Ed01.pdf` (2011-06)  | `/mnt/ace/O&G-Standards/API/`  |
| 23rd ed (filename-tagged `e23`) — base + Errata 3 + Addendum 1 | `API Spec 6D_14313_e23wErr3Ad1 Pipeline Valves.pdf` (2.24 MB, 2011-06)    | `/mnt/ace/O&G-Standards/API/Specifications/` |
| 23rd ed Errata 6                                         | `6D_14313_e23_Errata6.pdf` (2011-08)                                       | `/mnt/ace/O&G-Standards/API/`  |
| Annex F (fugitive emissions, edition-untagged)           | `6D_AnnexF.pdf` (404 KB, 2011-06)                                          | `/mnt/ace/O&G-Standards/API/`  |

> **Notes.** (1) Five 6D-tagged catalog entries total (organization=API,
> filename matches `6D`). The base specification is captured only for
> the 23rd edition (the dual-numbered `API Spec 6D / ISO 14313` PDF);
> earlier-edition Errata files (`Errata 4`, untagged Errata) lack a
> matched base PDF in the local catalog. (2) The 23rd-edition errata
> sequence is split across multiple PDFs (Err3+Ad1 stitched into the
> base; Err6 standalone) — a per-edition errata manifest is suggested
> in the [API source-page catalog hygiene actions](../sources/og-standards-api.md).
> (3) The current published edition at the API store is later than
> the locally-cached 23rd; downstream consumers should re-pin against
> the current published revision before procurement use. (4) ISO 14313
> is the dual-numbered international equivalent of API Spec 6D.

## Key requirements

> Section names below identify the recurring high-traffic clusters of
> the standard (titles paraphrased from publicly-known API metadata;
> no clause text reproduced).

- **Pressure–temperature ratings and design** — design methodology for
  pressure-containing and pressure-controlling parts at ASME/ANSI
  Class 150–2500 and API 5 ksi / 10 ksi / 15 ksi rated working
  pressures, with pressure–temperature derating curves harmonised
  with [ASME B16.34](../standards/asme-b16-34.md) for class-rated
  flanged valves.
- **Body-bore equivalence and drift testing** — full-opening valves
  must pass a drift-test gauge of specified diameter relative to
  nominal pipe size; this is the through-conduit pig-passability
  criterion that distinguishes pipeline-service ball/gate valves
  from general piping-service B16.34 valves.
- **End connections** — flanged (raised-face / ring-joint per
  [ASME B16.5](../standards/asme-b16-5.md) and API 6A flange
  geometry), butt-welding ends per
  [ASME B31.4](../standards/asme-b31-4.md) /
  [ASME B31.8](../standards/asme-b31-8.md) bevel preparations,
  threaded, hub/clamp, and proprietary compact-flange options.
  Welding-end valve girth welds to adjoining pipe are qualified
  per [API Std 1104](../standards/api-std-1104.md) (see also
  [Welding procedures and acceptance](../concepts/welding-procedures-and-acceptance.md)).
- **Materials — carbon-steel and CRA upgrades** — base material
  options span carbon-steel body/closure forgings (e.g., A105, A350
  LF2) through low-alloy and martensitic/austenitic/duplex stainless
  upgrades for sour or corrosive service, with sour-service
  qualification cross-referenced to
  [NACE / AMPP MR-0175 / ISO 15156](../standards/ampp-mr-0175-pt1.md)
  (see also [Sour-service materials](../concepts/sour-service-materials.md)).
  Trim materials and seat/seal elastomer selection are governed by
  service temperature and produced-fluid composition.
- **Quality control and Factory Acceptance Testing (FAT)** —
  hydrostatic shell test, hydrostatic seat test, and (for gas-rated
  service) gas-seat test, each with hold-time and leak-rate acceptance
  criteria; supplementary low-pressure gas seat tests for tight
  shut-off duty; drift test (above) for through-conduit configurations;
  anti-static continuity test for ball/plug valves in dry-gas service;
  and high-pressure cycle/operability tests for actuated valves.
- **Traceability and marking** — heat-traceability of pressure-
  containing parts, NDE records, and equipment marking per the
  specification's marking clause (manufacturer ID, API monogram,
  size, pressure class, material designation, ring-joint number where
  applicable, and serial number).
- **Double Block-and-Bleed (DBB) configuration** — explicit
  definitions and qualification for **double block-and-bleed** and
  **double isolation-and-bleed (DIB-1 / DIB-2)** valve configurations,
  used for positive isolation at custody-transfer, pig-trap,
  and station block-valve duty. Spec 6D fixes the seat-test
  protocol that determines whether a given ball/plug/expanding-gate
  valve qualifies as DBB versus DIB.
- **Fugitive-emission qualification (Annex F, optional)** —
  type-test protocol for stem-seal fugitive-emission performance,
  with leakage-rate acceptance classes; commonly invoked alongside
  ISO 15848-1 by purchaser specification for VOC-regulated service.
  The Annex F PDF is captured separately in the local catalog
  (`6D_AnnexF.pdf`).

## Cross-references

- [API Spec 6A](../standards/api-spec-6a.md) — wellhead and christmas
  tree equipment; **upstream** of the pipeline at the wellhead /
  tree outlet. Shares end-connection geometry (API flanges, ring-
  joint grooves) and hydrostatic-test heritage with 6D, but scopes to
  surface and subsea wellhead service rather than pipeline trunk
  service.
- **API Spec 17D** — design and operation of subsea production
  systems; subsea valves on tree and manifold outlets derive from
  6A rather than 6D, but ROV-operated isolation valves on subsea
  pipelines may be specified to 6D.
  *(Standalone wiki/standards page not yet present.)*
- [API Std 1104](../standards/api-std-1104.md) — welding of pipelines
  and related facilities; governs **field girth-weld qualification**
  for butt-welding-end 6D valves welded into pipeline service.
- [ASME B16.34](../standards/asme-b16-34.md) — valves flanged,
  threaded, and welding end (parallel scope for piping-service
  valves). Spec 6D borrows pressure–temperature rating curves from
  B16.34 for class-rated flanged ball/gate/plug/check valves; the
  scopes overlap on piping-service pressure ratings but diverge on
  pipeline-service requirements (full-bore drift test, DBB, pig
  passability).
- [ASME B16.5](../standards/asme-b16-5.md) — pipe flanges and flanged
  fittings (companion flange geometry for 6D flanged-end valves
  through Class 2500).
- **BS 5351 — UK steel ball valves** — historical British Standard
  for petroleum/petrochemical ball valves; parallel scope to the
  ball-valve subset of API 6D, now largely superseded by BS EN ISO
  17292 / API 6D adoption in UK procurement.
  *(Standalone wiki/standards page not yet present.)*
- **ISO 14313 — Pipeline transportation systems / pipeline valves**
  — the dual-numbered international parallel of API 6D; the local
  catalog filename `6D_14313_e23` reflects the joint API/ISO
  publication.
  *(Standalone wiki/standards page not yet present.)*
- [NACE / AMPP MR-0175 / ISO 15156 — sour-service materials](../standards/ampp-mr-0175-pt1.md)
  ([Pt 2](../standards/ampp-mr-0175-pt2.md),
   [Pt 3](../standards/ampp-mr-0175-pt3.md),
   [ISO 15156 umbrella](../standards/iso-15156.md)) —
  qualification of valve body, closure, stem, and trim materials for
  H₂S-bearing service; cross-referenced from 6D's materials clause.
  See also the concept page
  [Sour-service materials](../concepts/sour-service-materials.md).
- [ASME B31.4](../standards/asme-b31-4.md),
  [ASME B31.8](../standards/asme-b31-8.md) — liquid and gas pipeline
  piping codes that **specify** 6D valves at block-valve and station
  locations along the pipeline route.
- [API Spec 5L](../standards/api-spec-5l.md) — line pipe; the
  pipe-side counterpart that 6D welding-end valves are joined to.
- Concept consumers within this wiki:
  - [Welding procedures and acceptance](../concepts/welding-procedures-and-acceptance.md)
    — qualification of valve girth welds (welding-end valves into
    pipeline service).
  - [Sour-service materials](../concepts/sour-service-materials.md)
    — sour-service qualification of valve materials per MR-0175.

## Sources

- Catalog reference: [O&G Standards catalog — API](../sources/og-standards-api.md)
- Publisher catalog: <https://www.api.org/products-and-services/standards>
- Local catalog source: `/mnt/ace/O&G-Standards/_catalog.json`
  (organization=API, filename matches `6D`; 5 entries —
  base 23rd edition + Errata 6 standalone + Annex F + 2 prior-edition
  Errata orphans).
- Calc citation contract:
  [`.claude/rules/calc-citation-contract.md`](https://github.com/vamseeachanta/workspace-hub/blob/main/.claude/rules/calc-citation-contract.md)
  — workspace-hub-side rule referenced for downstream `Citation`
  resolver targets that pin against this page's frontmatter
  (`code_id`, `publisher`, `revision`).
