---
title: "API RP 2SK — Stationkeeping systems for floating structures (bounded summary)"
tags: ["api", "standards", "mooring", "stationkeeping", "metadata-only"]
added: 2026-05-02
last_updated: 2026-05-02
domain: engineering-standards
code_id: api-rp-2sk
publisher: API
revision: "3e-2005-r2008"
revision_source: /mnt/ace/O&G-Standards/API/Recommended-Practice/
verified_on: 2026-05-02
public_url: https://www.api.org/products-and-services/standards
publisher_catalog_url: https://www.api.org/products-and-services/api-publications
sources:
  - /mnt/ace/O&G-Standards/API/Recommended-Practice/API_RP_2SK_3rd_Ed_(2005).pdf
  - /mnt/ace/O&G-Standards/API/Recommended-Practice/API_RP_2SK_Addendum_1_(2007).pdf
extraction_policy: metadata-only
raw_copy_allowed: false
---

# API RP 2SK — Stationkeeping systems for floating structures

## Scope

API recommended practice for the design, analysis, and operation of
stationkeeping systems serving floating structures (mooring systems for
permanent and mobile units). Third edition (2005) with R2008 addendum.
Bounded metadata-only resolver target; no clause text or factor values
reproduced.

## Why this page exists

Resolver target for digitalmodel `Citation` instances per
`.claude/rules/calc-citation-contract.md`. Most-referenced API code under
mooring-design calc paths; this page is the future-needed citation target
for `mooring_design.py`-class modules wired post-W1-A. Frontmatter triple
(`code_id`, `publisher`, `revision`) supports fail-closed resolution.

## Where to find the full text

- Raw PDFs (vendor-derivative, do NOT copy into git per #2482):
  - `/mnt/ace/O&G-Standards/API/Recommended-Practice/API_RP_2SK_3rd_Ed_(2005).pdf`
  - `/mnt/ace/O&G-Standards/API/Recommended-Practice/API_RP_2SK_Addendum_1_(2007).pdf`
- Publisher catalog: <https://www.api.org/products-and-services/standards>
- Internal callers: `digitalmodel/src/digitalmodel/marine_ops/marine_engineering/calm_buoy_fatigue.py`,
  `…/mooring_analysis/component_database.py` plus other mooring modules
  (66 occurrences across digitalmodel/src/ as of 2026-05-02).

## Cross-references

- [api-rp-2a-wsd](api-rp-2a-wsd.md) — fixed-platform recommended practice
- [api-std-2rd](api-std-2rd.md) — dynamic risers
- [Calc citation contract](../../../../../.claude/rules/calc-citation-contract.md)

## Cross-References

- **Cross-wiki (maritime-law)**: [Salvage Convention 1989](../../../maritime-law/wiki/standards/salvage-convention-1989.md) — **bidirectional bridge**: API RP 2SK (Design and Analysis of Stationkeeping Systems for Floating Structures) governs FPSO/FLNG/FSRU/semi-submersible mooring-system design across catenary, taut-leg, spread-mooring, and thruster-assisted/DP-supplemented configurations. **Mooring-system failures** — chain-link wear (interlink fretting + corrosion-fatigue), polyester-rope creep + axial-compression fatigue, fairlead/stopper failure, anchor-drag, and turret-bearing seizure — trigger **salvage events** when a moored unit drifts uncontrolled or threatens shoreline impact. The **Salvage Convention 1989 Article 14** (Special Compensation) provides the environmental-protection compensation framework engaged when salvors intervene on mooring-failed floating units; the **SCOPIC 2014** contractual addendum sets the practical tariff under Lloyd's Open Form (LOF). The **Banff FPSO 2011** (North Sea, mooring-line breakage during Hurricane Bawbag) and **Volve FPSO 2016** (Norwegian sector, anchor-leg failure cascading to platform-supply-vessel emergency tow) incidents demonstrated this interplay — design-stage RP 2SK envelope selection (intact + damaged + survival cases) directly conditions whether casualty escalation reaches the Article 14 / SCOPIC threshold. Use the bridge for mooring-failure casualty digests bridging stationkeeping-design non-conformance to salvage-compensation analysis.
