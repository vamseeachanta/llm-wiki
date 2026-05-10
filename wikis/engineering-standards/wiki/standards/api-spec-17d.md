---
title: "API Spec 17D — Subsea Wellhead and Tree Equipment"
slug: api-spec-17d
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
code_id: api-spec-17d
publisher: API
revision: "2e-2011"
tags:
  - api
  - subsea
  - wellhead
  - christmas-tree
  - tubing-hanger
  - vertical-tree
  - horizontal-tree
  - oct
  - standards
  - api-spec
sources:
  - ../sources/og-standards-api.md
extraction_policy: metadata-only
raw_copy_allowed: false
---

# API Spec 17D — Design and Operation of Subsea Production Systems — Subsea Wellhead and Tree Equipment

> Bounded metadata-only standards page. Per llm-wiki spinout governance
> (2026-05-05), vendor PDFs are not copied into this repo; this page
> records only publisher facts and a domain-knowledge scope description.
> **code_id:** `api-spec-17d` &nbsp;•&nbsp; **publisher:** API
> &nbsp;•&nbsp; **revision:** 2nd edition (2011) is the latest edition
> present in the local catalog.

## Scope

API Specification 17D covers the design, manufacture, testing, and
qualification of **subsea wellhead and tree equipment** used in subsea
oil and gas production systems — specifically the **subsea wellhead
housing**, **casing hangers and seal assemblies**, **tubing-spool**,
**tubing hangers**, **subsea christmas trees** in both **vertical**
(VXT) and **horizontal** (HXT) configurations, **tree-running tools
(TRT)** and **tree-cap assemblies**, **flow-loop and choke modules**,
and the **interfaces** to the downhole-safety-valve (DHSV) hydraulic
control circuit and the topsides umbilical termination.

17D is the subsea derivative of [API Spec 6A](./api-spec-6a.md):
materials, PSL grading, PR-functional qualification, temperature
classes, and rated-working-pressure architecture are inherited from
6A and then **augmented with subsea-specific provisions** that 6A's
surface-equipment scope does not address:

- **External (hyperbaric) pressure** — design and qualification for
  ambient seawater pressure on the outboard side of pressure-
  containing parts; verification by hyperbaric chamber testing in
  addition to internal hydrostatic test.
- **ROV / ROT interfaces** — torque-bucket, hot-stab, paddle-handle,
  and override interfaces aligned with ISO 13628-8 (now folded into
  [API Spec 17H](./api-17h.md)) so a class-of-vehicle ROV can
  operate the tree without bespoke tooling.
- **Marinisation** — corrosion-allowance, external coating systems,
  cathodic-protection (CP) anode sizing/attachment, and seawater-
  immersion sealing for elastomers and metallic seals
  (cross-references the
  [cathodic-protection concept page](../concepts/cathodic-protection.md)
  for subsea-wellhead CP).
- **Install / retrieve verification** — running-tool latch, lock,
  test, and unlock sequences validated end-to-end with the tree
  in-place; remote pressure-test ports and lock-status indicators
  ROV-readable from outside the tree envelope.
- **Integration with [API 17A](./api-17a.md)** — the master
  subsea-production-systems framework that 17D plugs into; system-
  level pressure-control philosophy, valve-block topology, and
  isolation-barrier policies originate in 17A and are realised at
  the tree by 17D-compliant equipment.

## Edition history

| Edition / year | Catalog-detected artefacts | Local catalog parent_root |
|----------------|----------------------------|----------------------------|
| 1st ed (1992) — base | 1 catalog entry | `/mnt/ace/O&G-Standards/API/` |
| 1st ed Supplement 1 (1993) | 1 catalog entry | `/mnt/ace/O&G-Standards/API/` |
| 1st ed Supplement 2 (1996) | 1 catalog entry | `/mnt/ace/O&G-Standards/API/` |
| 1st ed (filename-tagged "1996", consolidated) | 1 catalog entry | `/mnt/ace/O&G-Standards/API/` |
| Untagged compilation (`API_17D 2003.pdf`) | 1 catalog entry | `/mnt/ace/O&G-Standards/API/` |
| 1st ed supplements (`SU1.PDF`, `SU2.PDF`) | 2 catalog entries | `/mnt/ace/O&G-Standards/API/` |
| 2nd ed (2011) | 1 catalog entry | `/mnt/ace/O&G-Standards/API/` |
| Untagged compilation (`API SPEC 17D.pdf`) | 1 catalog entry | `/mnt/ace/O&G-Standards/API/` |

> **Notes.** (1) The 2nd edition (2011) is the latest revision present
> in the local catalog. The 2nd edition is dual-numbered with
> **ISO 13628-4** (subsea wellhead and tree equipment, international
> parallel) and the two documents share clause structure and
> functional-requirement language. (2) The current published edition
> at the API store may be later than the 2011 2nd edition; downstream
> consumers should re-pin against the current published revision
> before procurement use. (3) The two 1st-edition supplements (1993,
> 1996) are stored as separate PDFs rather than stitched into a
> consolidated 1st-edition file — a per-edition manifest is suggested
> in the [API source-page catalog hygiene actions](../sources/og-standards-api.md).

## Key requirements

> Section names below identify the recurring high-traffic clusters of
> the standard (titles paraphrased from publicly-known API metadata;
> no clause text reproduced).

- **Material classes and sour-service options aligned with 6A** —
  body, bonnet, end, outlet, and stem material requirements inherited
  from [API Spec 6A](./api-spec-6a.md) classes AA → HH, with explicit
  sour-service classes (DD/EE/FF/HH) compatible with the
  [AMPP/NACE MR-0175 / ISO 15156](./ampp-mr-0175-pt1.md) H₂S-
  environment limits. The
  [sour-service-materials concept page](../concepts/sour-service-materials.md)
  consumes this clause for subsea-tree material selection.
- **PSL and PR grading inherited from 6A** — PSL 1 → PSL 4 (manu-
  facturing-stage quality control, NDE coverage, traceability) and
  **PR1 / PR2 functional qualification** (extended cycle-count and
  temperature/pressure-range testing). PR2 is the typical subsea-
  tree procurement floor for valves and actuators.
- **PR2F functional verification** — 17D adds a subsea-specific
  functional-verification regime (the "F" qualifier denotes flow-
  loop and ROV-interface inclusion) that exercises the tree as an
  installed assembly, not just per-component, including ROV-
  override demonstrations and lock-status-indicator validation.
- **Hyperbaric pressure-test protocols** — external-pressure
  qualification of pressure-containing and pressure-controlling
  parts in a hyperbaric chamber simulating water-depth ambient,
  in addition to the internal hydrostatic shell and seat tests
  inherited from 6A. Hold times, leak-rate acceptance, and
  combined internal+external loading sequences are specified.
- **In-place + retrievable test specifications** — the standard
  distinguishes **factory-acceptance testing (FAT)**, **system-
  integration testing (SIT)** at the tree-and-running-tool stack,
  and **post-installation in-place tests** performed via ROV or
  topsides-controlled subsea-control-module commands. Retrievable
  components (valve actuators, choke inserts, tree caps) carry
  their own re-installation test sequence.
- **ROV interface clauses (ISO 13628-8 alignment)** — torque-bucket
  geometry, hot-stab port classes, paddle-handle reach envelopes,
  and override-tooling interfaces conform to ISO 13628-8 / API 17H
  so any class-of-vehicle ROV can operate any 17D-compliant tree.
  The [API 17H standards page](./api-17h.md) carries the
  detailed interface taxonomy.
- **Vertical vs. horizontal tree (VXT / HXT) architecture** — the
  standard accommodates both topologies. In a **VXT** the master
  valves sit above the tubing hanger in the tree body; the tubing
  hanger lands in the tubing-spool below the tree, and tubing is
  pulled by removing the tree. In an **HXT** the master valves sit
  to the side of the tubing hanger, the tubing hanger lands in the
  tree body itself, and the tree need not be removed to pull
  tubing — but the tree must be installed before the tubing is
  run. Both topologies share the 17D PSL/PR/material-class grading.
- **Downhole-safety-valve (DHSV) interface** — hydraulic-control-
  line porting from the tree-mounted production-master to the
  tubing-hanger penetrator, including double-block-and-bleed
  isolation philosophy and fail-safe-close demonstration.
- **Cathodic protection and external coatings** — sacrificial-
  anode mass calculation, anode mounting, dielectric-shield
  coordination with adjacent structures, and external-coating
  qualification for design-life immersion (typically 20–25 years).
  Consumed by the
  [cathodic-protection concept page](../concepts/cathodic-protection.md).
- **Marking and documentation** — equipment marking (manufacturer
  ID, API monogram, PSL, PR, material class, temperature class,
  rated working pressure, water-depth rating, serial number) and
  the subsea-specific certification-package contents (FAT records,
  SIT records, hyperbaric-test records, ROV-interface verification,
  CP design report).

## Cross-references

- [API Spec 6A — Wellhead and Christmas Tree Equipment](./api-spec-6a.md)
  — parent surface-equipment specification. 17D inherits material
  classes, PSL/PR grading, temperature classes, and pressure-rating
  architecture from 6A and adds subsea-specific provisions on top.
- [API Spec 17A — Subsea Production Systems (master design)](./api-17a.md) —
  the system-level framework that 17D plugs into; pressure-control
  philosophy, isolation-barrier policy, and field-architecture
  requirements originate here.
- [API Spec 17H — Subsea ROV Interfaces](./api-17h.md) — torque-bucket, hot-
  stab, paddle-handle, and override interface taxonomy that 17D
  references for ROV operability of trees and tree caps.
- **ISO 13628-4 — Petroleum and natural gas industries — Design
  and operation of subsea production systems — Part 4: Subsea
  wellhead and tree equipment** — the international parallel; the
  17D 2nd edition is dual-numbered with ISO 13628-4.
  *(Standalone wiki/standards page not yet present.)*
- [AMPP MR-0175 / ISO 15156 (Pt 1)](./ampp-mr-0175-pt1.md) —
  sour-service materials qualification for subsea tree components
  in H₂S service; drives selection of 17D material classes
  DD/EE/FF/HH.
- [AMPP MR-0175 (Pt 2)](./ampp-mr-0175-pt2.md),
  [Pt 3](./ampp-mr-0175-pt3.md) — carbon-steel and CRA-specific
  sour-service requirements respectively.
- **DNV-OS-E101 / DNV-OS-E201** — subsea-equipment hyperbaric
  verification and drilling-equipment scopes; parallel hyperbaric
  test-protocol references that downstream operators may invoke
  alongside 17D for harsh-environment qualification.
  *(Standalone wiki/standards pages not yet present.)*
- [API Spec 17J — unbonded flexible pipe](./api-spec-17j.md) —
  flexible-riser interface to the tree outlet; the riser end-
  fitting lands on a 17D-compliant tree flange or hub.
- [API 17E — subsea umbilicals](./api-17e.md) — the control-fluid,
  electrical-power, and chemical-injection lines that terminate at
  the tree's umbilical-termination assembly (UTA) and feed the
  subsea-control-module commanding 17D-compliant valve actuators.

## Sources

- Catalog reference: [O&G Standards catalog — API](../sources/og-standards-api.md)
- Publisher catalog: <https://www.api.org/products-and-services/standards>
- Local catalog source: `/mnt/ace/O&G-Standards/_catalog.json`
  (organization=API, filename matches `17D` / `17d`).
- Calc citation contract:
  [`.claude/rules/calc-citation-contract.md`](https://github.com/vamseeachanta/workspace-hub/blob/main/.claude/rules/calc-citation-contract.md)
  — workspace-hub-side rule referenced for downstream `Citation`
  resolver targets that pin against this page's frontmatter
  (`code_id`, `publisher`, `revision`).
