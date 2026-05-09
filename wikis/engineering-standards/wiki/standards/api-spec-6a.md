---
title: "API Spec 6A — Wellhead and Christmas Tree Equipment"
slug: api-spec-6a
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
code_id: api-spec-6a
publisher: API
revision: "20e-2011"
tags:
  - api
  - wellhead
  - christmas-tree
  - subsea
  - surface-equipment
  - standards
  - api-spec
sources:
  - ../sources/og-standards-api.md
extraction_policy: metadata-only
raw_copy_allowed: false
---

# API Spec 6A — Wellhead and Christmas Tree Equipment

> Bounded metadata-only standards page. Per llm-wiki spinout governance (2026-05-05), vendor PDFs are not copied into this repo; this page records only publisher facts and a domain-knowledge scope description.
> **code_id:** `api-spec-6a` &nbsp;•&nbsp; **publisher:** API &nbsp;•&nbsp; **revision:** 20th edition (2011) is the latest edition present in the local catalog.

## Scope

API Specification 6A defines requirements for the design, manufacture,
testing, and marking of **wellhead and christmas tree equipment** used in
oil and gas production — including casing-head and tubing-head spools,
hangers, valves, chokes, actuators, tees, crosses, adapters, and the
associated flanged, studded, and clamped end and outlet connections —
covering both **surface and subsea** wellheads and trees. The
specification is built around two orthogonal grading axes:

- **Product Specification Levels (PSL 1 / 2 / 3 / 3G / 4)** — increasing
  levels of quality control, materials traceability, NDE coverage,
  and qualification testing applied at the manufacturing stage.
- **Performance Requirements (PR1 / PR2)** — qualification levels for
  the equipment's operational duty (e.g., valves and actuators tested
  to PR2 endure extended cycle counts under temperature/pressure
  extremes that PR1 does not cover).

The standard further classifies equipment by **temperature class**
(K/L/N/P/R/S/T/U/V/X/Y), **material class** (AA/BB/CC/DD/EE/FF/HH —
ranging from general service to sour service compatible per
[NACE MR-0175 / ISO 15156](../standards/ampp-mr-0175-pt1.md)), and
**rated working pressure** (typical 2,000 / 3,000 / 5,000 / 10,000 /
15,000 / 20,000 psi rated bores). It cross-references API
Specifications and Recommended Practices for line pipe (Spec 5L /
5CT), pipeline valves (Spec 6D), drill-through and BOP equipment
(Spec 16A), and the subsea production-equipment family (Spec 17D
derives its tree-and-wellhead requirements directly from 6A).

## Edition history

| Edition / year | Catalog-detected artefacts | Local catalog parent_root |
|----------------|----------------------------|----------------------------|
| 17th ed (1999) — base + Errata 1 + Supplement 1 | 2 catalog entries | `/mnt/ace/O&G-Standards/API/` |
| 17th ed Errata 1 (2003) | 1 catalog entry | `/mnt/ace/O&G-Standards/API/` |
| 19th ed Errata 1 (2004) | 1 catalog entry | `/mnt/ace/O&G-Standards/API/` |
| 19th ed Errata 2 (2004) | 1 catalog entry | `/mnt/ace/O&G-Standards/API/` |
| 19th ed (filename-tagged "July 2004") | 1 catalog entry | `/mnt/ace/O&G-Standards/API/` |
| 20th ed (2011) — base + Addenda 1–3 + Errata 1–6 | 10 catalog entries (3 addenda + 6 errata + 1 base) | `/mnt/ace/O&G-Standards/API/` |
| Untagged compilation (`API 6A.pdf`) | 1 catalog entry | `/mnt/ace/O&G-Standards/API/` |

> **Notes.** (1) The 20th-edition addenda and errata are stored as
> separate PDFs in the catalog rather than stitched into a single
> consolidated file — a per-edition manifest is suggested in the
> [API source-page catalog hygiene actions](../sources/og-standards-api.md).
> (2) The current published edition at the API store is later than
> the 20th (the API catalog has progressed beyond the locally-cached
> 2011 edition); downstream consumers should re-pin against the
> current published revision before procurement use. (3) ISO 10423
> is the dual-numbered international equivalent of API Spec 6A.

## Key clauses / sections

> Section names below identify the recurring high-traffic clusters of the standard
> (titles paraphrased from publicly-known API metadata; no clause text reproduced).

- **Product Specification Levels (PSL 1 → PSL 4)** — graded quality
  controls covering materials, NDE coverage (UT, MT, RT, PT
  thresholds), traceability, hardness testing, and impact-test
  requirements. PSL 4 carries the strictest acceptance criteria and
  is reserved for highest-criticality service.
- **Performance Requirements (PR1, PR2)** — qualification testing
  for valves, actuators, and chokes. PR2 mandates extended
  cycle-count and temperature/pressure-range testing beyond PR1; it
  is the typical subsea-tree procurement floor.
- **Materials and material classes (AA → HH)** — body, bonnet, end,
  outlet, and stem material requirements with explicit sour-service
  classes (DD/EE/FF/HH) compatible with the
  [AMPP/NACE MR-0175 / ISO 15156](../standards/ampp-mr-0175-pt1.md)
  H₂S-environment limits.
- **Pressure ratings and design** — design methodology for pressure-
  containing and pressure-controlling parts at standard rated
  working pressures (2 ksi → 20 ksi), including end- and outlet-
  connection design (API flanges, studded outlets, clamp hubs).
- **Hydrostatic and gas pressure testing** — factory acceptance
  testing protocol, including hydrostatic shell test, hydrostatic
  seat test, and (for PR2 / gas-rated) gas-test sequences with
  hold-time and leak-rate acceptance criteria.
- **Temperature classes (K → Y)** — minimum/maximum operating-
  temperature envelopes that drive material toughness (Charpy
  V-notch impact requirements) and elastomer selection.
- **Quality control and traceability** — heat-treatment records,
  raw-material certifications, NDE records, and serial-number
  traceability requirements that escalate with PSL.
- **Marking and documentation** — equipment marking (manufacturer
  ID, API monogram, PSL, PR, material class, temperature class,
  rated working pressure, serial number) and certification-package
  contents.

## Cross-references

- [AMPP MR-0175 / ISO 15156 (Pt 1)](../standards/ampp-mr-0175-pt1.md) —
  sour-service materials qualification (drives 6A material classes
  DD, EE, FF, HH).
- [AMPP MR-0175 (Pt 2)](../standards/ampp-mr-0175-pt2.md),
  [Pt 3](../standards/ampp-mr-0175-pt3.md) — carbon-steel and
  CRA-specific sour-service requirements respectively.
- **API Spec 6D** — pipeline valves (also adopted as ISO 14313);
  shares end-connection and pressure-test heritage with Spec 6A but
  scopes to pipeline rather than wellhead service.
  *(Standalone wiki/standards page not yet present; see
  [API source-page recommendation](../sources/og-standards-api.md).)*
- **API Spec 17D** — design and operation of subsea production
  systems; subsea wellhead and tree equipment requirements derive
  directly from Spec 6A, with subsea-specific additions (ROV
  interfaces, external pressure, marinisation).
  *(Standalone wiki/standards page not yet present.)*
- [API Spec 17J — unbonded flexible pipe](../standards/api-spec-17j.md) —
  downstream of the tree on flexible riser systems; not directly
  cited by 6A but interfaces at the tree outlet.
- [API 17E (subsea umbilicals)](../standards/api-17e.md) —
  control-fluid and chemical-injection lines connecting topsides
  to the subsea tree.
- [API Spec 5L — line pipe](../standards/api-spec-5l.md) — the
  pipeline-side counterpart for material traceability and
  hydrostatic-test conventions.
- [ASME B31.4](../standards/asme-b31-4.md),
  [ASME B31.8](../standards/asme-b31-8.md) — downstream piping
  codes for liquid and gas pipelines respectively; the tree's
  outlet connections feed into these systems.

## Sources

- Catalog reference: [O&G Standards catalog — API](../sources/og-standards-api.md)
- Publisher catalog: <https://www.api.org/products-and-services/standards>
- Local catalog source: `/mnt/ace/O&G-Standards/_catalog.json`
  (organization=API, filename matches `6A`).
- Calc citation contract:
  [`.claude/rules/calc-citation-contract.md`](https://github.com/vamseeachanta/workspace-hub/blob/main/.claude/rules/calc-citation-contract.md)
  — workspace-hub-side rule referenced for downstream `Citation`
  resolver targets that pin against this page's frontmatter
  (`code_id`, `publisher`, `revision`).
