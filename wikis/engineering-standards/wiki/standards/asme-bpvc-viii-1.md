---
title: "ASME BPVC Section VIII Division 1 — Rules for Construction of Pressure Vessels (bounded summary)"
tags: ["asme", "bpvc", "standards", "pressure-vessels", "metadata-only"]
added: 2026-05-02
last_updated: 2026-05-02
domain: engineering-standards
code_id: asme-bpvc-viii-1
publisher: ASME
revision: "2010"
revision_source: "/mnt/ace/O&G-Standards/ASME/ASME VIII/ASME VIII DIV 1 (2010) Rules for Construction of High Pressure Vessels.pdf"
publisher_current_edition: "2023"
methodology_status: "unknown"
verified_on: 2026-05-02
public_url: https://www.asme.org/codes-standards/bpvc-standards
sources:
  - /mnt/ace/O&G-Standards/ASME/ASME VIII/ASME VIII DIV 1 (2010) Rules for Construction of High Pressure Vessels.pdf
extraction_policy: metadata-only
raw_copy_allowed: false
---

# ASME BPVC Section VIII Division 1 — Rules for Construction of Pressure Vessels (bounded summary)

## Scope

BPVC Section VIII Division 1 provides design-by-rule requirements for the construction of pressure vessels operating above and below specified pressure thresholds. Coverage includes minimum-thickness rules for shells, heads, nozzles, openings, reinforcement, and supports, together with materials, fabrication, examination, testing, inspection, and stamping requirements for the in-scope vessels.

## Why this page exists

Resolver target for digitalmodel `Citation` instances per `.claude/rules/calc-citation-contract.md`. Contains no clause text, no formulas, and no tables from the source. Downstream callers wire VIII Division 1 minimum-thickness and joint-efficiency constants through this page rather than parsing the source PDF. The combined `ASME VIII` token is referenced 33 times across `digitalmodel/src/` (shared with Division 2).

## Where to find the full text

- Raw PDF: `/mnt/ace/O&G-Standards/ASME/ASME VIII/ASME VIII DIV 1 (2010) Rules for Construction of High Pressure Vessels.pdf` (read-only, vendor-derivative; do not copy into git per #2482)
- Publisher catalog: https://www.asme.org/codes-standards/bpvc-standards
- Internal callers: `digitalmodel/src/digitalmodel/` modules referencing `ASME VIII` / `ASME_VIII_DIV1` symbols

## Cross-references

- [[asme-bpvc-viii-2]] — alternative design-by-analysis route
- [[asme-bpvc-ii-d]] — material allowable stresses sourced upstream
- [[asme-bpvc-ix]] — welding qualification basis
- [Calc citation contract](../../../../../.claude/rules/calc-citation-contract.md)

## Cross-wiki bridges

- [SOLAS 1974](../../../maritime-law/wiki/standards/solas-1974.md)
  (maritime-law) — **bidirectional bridge**: BPVC Section VIII Division 1
  is the design-by-rule code that flag-state inspection regimes and
  IACS class-society rules import by reference for shipboard unfired
  pressure vessels under SOLAS Ch. II-1 (machinery installations) and
  Ch. II-2 (fire-protection-related pressure systems). For gas
  carriers under SOLAS Ch. VII Part C, the IGC Code Ch.5 process
  pressure vessels and Ch.8 vent / PRV systems likewise lean on
  Section VIII (Div. 1 and Div. 2) for cargo-tank, knock-out drum,
  and reliquefaction-plant pressure-vessel construction. SOLAS
  itself carries no numeric design rules for unfired pressure
  vessels — Section VIII is the engineering-standards substrate the
  treaty regime delegates to.
