---
title: "ASME B31J — Stress Intensification Factors (i-Factors) and Flexibility Factors (k-Factors)"
slug: asme-b31j
code_id: asme-b31j
publisher: ASME
publisher_full: "American Society of Mechanical Engineers"
revision: "2017 (B31J-2017); prior issues 2008, B31.3 Appendix D legacy charts (pre-2018)"
jurisdiction: "US (mandatory replacement for B31.3 Appendix-D legacy charts post-2018); international by adoption"
instrument_type: standard
supersedes: "Legacy B31.3 Appendix-D SIF/FF charts (post-2018 mandatory replacement per B31.3 referenced-code update)"
extraction_policy: metadata-only
raw_copy_allowed: false
sources:
  - https://www.asme.org/codes-standards
public_url: https://www.asme.org/codes-standards
publisher_catalog_url: https://www.asme.org/codes-standards
tags:
  - asme
  - standards
  - piping
  - sif
  - flexibility-factor
  - stress-analysis
  - process-piping
  - power-piping
  - metadata-only
added: 2026-05-10
last_updated: 2026-05-10
domain: engineering-standards
---

# ASME B31J — Stress Intensification Factors (i-Factors) and Flexibility Factors (k-Factors)

**code_id:** `asme-b31j` &nbsp;·&nbsp; **publisher:** ASME (American Society of Mechanical Engineers) &nbsp;·&nbsp; **revision:** ASME B31J-2017

> Bounded metadata-only resolver page for downstream `Citation(...)` callers under the calc-citation contract at `.claude/rules/calc-citation-contract.md`. Page contains no SIF formulae, k-factor expressions, or component-specific equation tables from the source.

## Scope

ASME B31J is the consensus US standard supplying **stress intensification factors (i-factors / SIF) and flexibility factors (k-factors)** for piping components, including welded and unwelded reducing branch tees, weld-in branch fittings, integrally reinforced branches, butt-welding tees, fabricated tees, sweepolets, weldolets, threaded joints, miter bends, and other common piping geometries. The factors are inputs to the elastic stress analysis methodology used by the B31 piping codes (B31.1 Power Piping, B31.3 Process Piping, B31.4 Liquid Pipeline, B31.5 Refrigeration, B31.8 Gas Pipeline, B31.9 Building Services, B31.12 Hydrogen) for occasional, sustained, displacement-stress-range, and cyclic-fatigue calculations.

Post-2018, B31J supersedes the legacy SIF/FF data set previously embedded as **ASME B31.3 Appendix D** (and equivalent chart sets in sister B31 codes). The B31 codes now reference B31J normatively; pre-2018 calc-module legacy carrying Appendix-D charts is **stale-as-of-publisher-cycle** and should be migrated to B31J-2017 references.

## Revision history

- **Legacy era (pre-2008)** — SIF/FF data embedded as charts/tables in each B31 code's appendix (e.g., B31.3 Appendix D); inconsistencies across B31 sections.
- **ASME B31J-2008** — first standalone publication; consolidated SIF/FF data for branch connections and bends.
- **ASME B31J-2017** — current edition; expanded component coverage; revised SIF/FF expressions reflecting later WRC bulletins and finite-element validation; mandatory referenced citation post-2018 across the B31 family.

Consult the ASME publications catalog for any subsequent reaffirmation, errata, or addenda before procurement use.

## Key sections

Section structure (verify against the publisher copy in any normative work):

- **Introduction and scope** — applicability across the B31 piping-code family; relationship to elastic-stress methodology.
- **Definitions and notation** — i-factor, k-factor, in-plane, out-of-plane, torsional, branch-on-run convention.
- **SIF and FF tables** — by component class: butt-welding elbows, miter bends, fabricated tees, weld-in branch fittings, integrally reinforced branch fittings, threaded and socket-welded fittings.
- **Test procedures** — for component vendors developing SIF/FF data on novel geometries (cyclic-bending fatigue test method).
- **Sustained-stress index (SSI) framework** — companion to SIF for sustained-load-stress evaluation introduced in the post-2017 revisions of the B31 codes.

## Practitioner application

- Process-piping stress engineers running CAESAR II / AutoPIPE / ROHR2 / TRIFLEX models on B31.1 / B31.3 / B31.4 / B31.8 piping systems; B31J SIF/FF values are the input data layer feeding the code-compliance check.
- Pipe-stress consultancies (Bechtel, Fluor, Worley, Jacobs, KBR, McDermott, Wood) executing piping flexibility analysis for refining, petrochemical, LNG, gas-transmission, and power projects.
- Piping-component vendors qualifying novel branch fittings or integrally reinforced fittings via the B31J cyclic-bending fatigue test method.
- Calc-module maintainers updating legacy B31.3 Appendix-D-derived SIF/FF data sets to the B31J-2017 referenced citation post-2018.

## Industry adoption

ASME B31J-2017 is the mandatory referenced data source for SIF and flexibility factors across the ASME B31 piping-code family in the US and is widely adopted internationally by EPCs running B31-code-jurisdiction projects. CAESAR II, AutoPIPE, ROHR2, and the other major piping-stress-analysis software families embed B31J data in their component libraries; verify the software-library version pins to B31J-2017 (or later) and not the legacy Appendix-D chart set when running post-2018 analyses.

## Why this page exists

Resolver target for digitalmodel `Citation` instances per `.claude/rules/calc-citation-contract.md` and substrate-fill landing for the wikilink in `asme-b31-3.md` referencing ASME B31J. Surfaced as 1 of 5 ASME-process/RBI substrate-gap residuals after iter-50 W231 sweep; created under iter-51 W232 ASME-process/RBI substrate-fill batch. **Metadata-only** per spinout 2026-05-05 governance.

## Where to find the full text

ASME publications subscription required; ANSI catalog also lists the document. Vendor-derivative full text is **not** stored in this repo per spinout vendor-derivative deny-list governance. Calc-citation callers resolve only against this page's frontmatter (`code_id`, `publisher`, `revision`); they do not require body text.

## Cross-references

- [asme-b31-1](asme-b31-1.md) — Power Piping; consumes B31J SIF/FF.
- [asme-b31-3](asme-b31-3.md) — Process Piping; consumes B31J SIF/FF (Appendix-D-replacement).
- [asme-b31-4](asme-b31-4.md) — Pipeline Transportation Systems for Liquid Hydrocarbons; consumes B31J SIF/FF.
- [asme-b31-8](asme-b31-8.md) — Gas Transmission and Distribution Piping Systems; consumes B31J SIF/FF.
- [asme-b31-12](asme-b31-12.md) — Hydrogen Piping and Pipelines; consumes B31J SIF/FF.
- [asme-b16-5](asme-b16-5.md) — Pipe Flanges and Flanged Fittings NPS 1/2–24; component family with B31J SIF/FF data.
- [asme-b16-47](asme-b16-47.md) — Large-diameter flanges (NPS 26 and larger) Series A / Series B.
- Pipe Stress Analysis (concept page TBD) — B31 elastic-stress methodology.
- [Calc citation contract](../../../../../.claude/rules/calc-citation-contract.md)

## Notes

- This page is **metadata-only**; no SIF formulae, k-factor expressions, or component-specific equation tables are reproduced from ASME B31J. All technical descriptions above are paraphrased general engineering knowledge.
- For normative piping-stress work, cite the ASME-published edition directly (ASME B31J-2017 or the current edition at time of citation).
- Substrate-fill resolver created under W232 iter-51 ASME-process/RBI batch (1 reference in `asme-b31-3.md`).
