---
title: "ABS GUI-002 Guide for Building and Classing FPSO — bounded summary"
tags: ["abs", "standards", "fpso", "guide", "metadata-only"]
added: 2026-05-02
last_updated: 2026-05-09
domain: engineering-standards
code_id: abs-gui-002-fpso
publisher: ABS
publisher_full: "American Bureau of Shipping"
revision: "1994"
abs_doc_number: "GUI-002"
ledger_id: ABS-GUI-002
sources:
  - /mnt/ace/O&G-Standards/ABS/Guidance-Notes/ABS-GUI-002-Guide-for-Building-and-Classing-FPSO-1994.pdf
extraction_policy: metadata-only
raw_copy_allowed: false
---

# ABS GUI-002 Guide for Building and Classing FPSO

## Scope
Guidance document for the building and classing of Floating Production, Storage, and Offloading (FPSO) systems. GUI-002 (1994 edition on disk) covers FPSO hull, mooring, process-system topside-to-hull interfaces, and class-specific design considerations applied above and beyond the steel-vessels rule book.

## Why this page exists
Resolver target for downstream `digitalmodel` `Citation` instances per `.claude/rules/calc-citation-contract.md`. The standards-transfer ledger already carries the `ABS-GUI-002` row (one of two pre-existing ABS rows). The 1994 edition is the on-disk revision; ABS may have published newer editions on the publisher portal that are not in the local corpus. The page contains no clause text or formula reproductions.

## Where to find the full text
- Raw PDF (1994 edition): `/mnt/ace/O&G-Standards/ABS/Guidance-Notes/ABS-GUI-002-Guide-for-Building-and-Classing-FPSO-1994.pdf` (read-only, vendor-derivative; do not copy into git per #2482)
- Publisher catalog: https://ww2.eagle.org/en/rules-and-resources/rules-and-guides.html (anonymous browse; newer editions may exist there)
- Internal callers: no live structured `Citation(...)` call yet; this page satisfies future calc-citation routing for FPSO design-classification logic

## Cross-references
- [abs-gui-101-fpso-dla](abs-gui-101-fpso-dla.md) — companion FPSO Dynamic Loading Approach Guide
- [abs-rules-steel-vessels-part3](abs-rules-steel-vessels-part3.md) — base steel-vessel hull rule book GUI-002 sits above
- [abs-rules-offshore-installations](abs-rules-offshore-installations.md) — offshore-installations rule book referenced for class scope

**Cross-wiki bridge (maritime-law):**

- [SOLAS 1974](../../../maritime-law/wiki/standards/solas-1974.md) — **bidirectional bridge**: ABS GUI-002 (Guide for Building and Classing FPSO) governs FPSO hull structure, mooring-system classification, offloading-system interfaces, and topside-to-hull integration for Floating Production, Storage, and Offloading installations including their FLNG and FSRU variants. SOLAS Chapter II-1 (Construction — Subdivision and Stability, Machinery and Electrical Installations) governs damage-stability indices, watertight subdivision, machinery redundancy, and intact-stability margins for SOLAS-registered ships. The two regimes converge on **ship-shape FPSOs operating under flag-state jurisdiction** — particularly disconnectable-turret FPSOs (NW Australia cyclone corridor, Gulf of Mexico hurricane corridor) and trading FSRUs that move between terminal and lay-up berths — where the asset is simultaneously a moored offshore installation (ABS GUI-002 hull and mooring rules) and a SOLAS-flagged ship (Ch. II-1 stability + watertight integrity). The IMO MODU Code (Resolution A.1023(26)) provides the harmonization precedent for self-propelled or detachable units; class-society FPSO rules implement GUI-002 hull scantlings while preserving SOLAS Ch. II-1 intact and damage-stability margins for the disconnect-and-transit case. Ship-shape FPSO survival-loadcase analysis (extreme storm + post-disconnect transit) sits exactly at this intersection.

- Calc citation contract: `.claude/rules/calc-citation-contract.md`
