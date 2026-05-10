---
title: "DNV-RP-F112 — Design of Duplex SS Subsea Equipment under Cathodic Protection"
slug: dnv-rp-f112
tags: ["dnv", "duplex-stainless-steel", "cathodic-protection", "hydrogen-embrittlement", "hisc", "subsea", "standards", "metadata-only"]
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
code_id: dnv-rp-f112
publisher: DNV
revision: "2008"
revision_source: "/mnt/ace/O&G-Standards/DNV/DNV_RP_F112_(2008)_Stainless_steel_subsea_equipment_exposed_to_cathodic_protection.pdf"
verified_on: 2026-05-09
public_url: https://standards.dnv.com/explorer/
sources:
  - /mnt/ace/O&G-Standards/DNV/DNV_RP_F112_(2008)_Stainless_steel_subsea_equipment_exposed_to_cathodic_protection.pdf
  - /mnt/ace/O&G-Standards/DNV/DNV_RP_F112_DRAFT_(2006)_Stainless_steel_subsea_equipment_exposed_to_cathodic_protection.pdf
  - wiki/sources/og-standards-dnv.md
extraction_policy: metadata-only
raw_copy_allowed: false
---

# DNV-RP-F112 — Design of Duplex Stainless Steel Subsea Equipment under Cathodic Protection

## Scope

Design recommendations for duplex stainless steel (DSS) subsea components exposed to cathodic protection (CP), where over-protection drives hydrogen absorption and risks Hydrogen-Induced Stress Cracking (HISC) of the ferrite phase. The recommended practice defines material qualification, geometric and design-stress constraints, residual-stress and fabrication controls, and inspection criteria for DSS forgings, castings, welded assemblies, and bolted connections operating in seawater under galvanic or impressed-current CP. Applies to standard duplex (22Cr) and super-duplex (25Cr) grades used in subsea trees, manifolds, jumpers, hubs, and connectors.

## Edition history

| Edition | Status | Year | On-disk path |
|---------|--------|------|--------------|
| 1st (DRAFT) | superseded | 2006 | `/mnt/ace/O&G-Standards/DNV/DNV_RP_F112_DRAFT_(2006)_*.pdf` |
| 1st (issued) | superseded by 2019 per public knowledge | 2008 | `/mnt/ace/O&G-Standards/DNV/DNV_RP_F112_(2008)_*.pdf` |
| 2nd | latest (publisher catalog) | 2019 | not on disk; see https://standards.dnv.com/explorer/ |

The 2008 issued edition is the latest copy on the consolidated standards mount; the 2019 revision (publisher-current) is referenced via the DNV explorer portal. Latest-on-disk is the resolver target for the calc-citation contract until the 2019 PDF is added under the same vendor-firewall governance.

## Why this page exists

This page is a citation resolver for downstream calc and material-qualification modules under the calc-citation contract at `.claude/rules/calc-citation-contract.md`. It contains no clause text, design-stress tables, geometry charts, or formula reproductions from the source. RP-F112 is the de facto industry reference for any DSS exposed to seawater with CP — invoked by subsea-tree, manifold, jumper, hub, and connector design across DNV-domain calcs. Concept-page consumers `[[concepts/cathodic-protection]]` and `[[concepts/sour-service-materials]]` cross-reference RP-F112 for HISC-mitigation guidance.

## Key recommendations (topic-only, no clause text)

- **Material control** — PREN ≥40 (super-duplex preferred) for HISC-resilient grades; ferrite-content limits in parent metal and weld metal; absence of sigma-phase and other intermetallics demonstrated per ASTM A923 or ISO 17781 screen tests.
- **CP protection-potential limits** — bound the protection potential less negative than approximately -1050 mV vs. Ag/AgCl/seawater to limit hydrogen evolution; coordinate with anode design under [dnv-rp-b401](dnv-rp-b401.md).
- **Design-stress limits** — lower allowable stresses (vs. parent-material yield) in zones exposed to CP, with separate allowables for base metal, weld metal, and HAZ; geometry-dependent reductions where stress-concentration plus residual-tensile-stress combine.
- **Bolted connection design** — paint coatings, dielectric isolation, or shielding to reduce direct CP exposure on high-strength duplex bolting; controls on preload-induced tensile residual stress.
- **Residual-stress control** — avoid as-welded high-restraint joints; PWHT or solution-annealing where applicable; tight tolerances on weld profile to reduce stress-raisers.
- **Surface finish** — avoid sharp stress-raisers (machining marks, undercut, weld-toe geometry) at CP-exposed surfaces; specify finish criteria for fatigue- and HISC-critical zones.
- **Inspection criteria** — surface-NDT acceptance for crack-like indications stricter than non-CP service; ferrite-content QC sampling plan; intermetallic-screen sampling on welds and forgings.

## Why it matters

Multiple high-profile FPSO and subsea-pipeline duplex-component HISC failures in the early 2000s drove this standard. CP — designed to protect the carbon-steel structure — over-protects DSS components mounted on the same circuit, evolving hydrogen at the steel surface that is absorbed by the ferrite phase. Combined with high residual or service tensile stress and sharp stress-raisers, this triggers brittle cracking in service. RP-F112 is the de facto industry reference for HISC mitigation in DSS subsea hardware; by 2008 it had become a baseline call-out in subsea-tree, manifold, and jumper specifications across operators.

## Where to find the full text

- Raw PDF (latest on disk, 2008 edition): `/mnt/ace/O&G-Standards/DNV/DNV_RP_F112_(2008)_Stainless_steel_subsea_equipment_exposed_to_cathodic_protection.pdf` (read-only, vendor-derivative; do not copy into git per spinout 2026-05-05 governance)
- Earlier revision on disk (2006 DRAFT): `/mnt/ace/O&G-Standards/DNV/DNV_RP_F112_DRAFT_(2006)_*.pdf`
- Publisher catalog (current 2019 edition): https://standards.dnv.com/explorer/
- Source-summary page: [O&G Standards catalog — DNV](../sources/og-standards-dnv.md)

## Cross-references

- [dnv-rp-b401](dnv-rp-b401.md) — offshore CP design; sets protection potentials that RP-F112 then bounds for DSS exposure
- [[concepts/cathodic-protection]] — concept-level treatment of galvanic and ICCP systems
- [[concepts/sour-service-materials]] — DSS qualification overlap with sour-service requirements
- ASTM A923 — DSS intermetallic-phase detection (sigma, chi); referenced for ferrite-phase QC
- ISO 17781 — DSS test methods for intermetallic detection (parallel to A923)
- ASTM G48 — pitting/crevice corrosion screen for DSS material qualification (CP-exposure complement)
- ISO 15156-3 / NACE MR0175 Part 3 — sour-service CRA (corrosion-resistant alloy) qualification, often co-applied with RP-F112 on subsea hardware
- API Spec 6A / API Spec 17D — wellhead and subsea-tree DSS components subject to RP-F112 controls
- Calc citation contract: `.claude/rules/calc-citation-contract.md`

## Sources

- [O&G Standards catalog — DNV](../sources/og-standards-dnv.md) — publisher-catalog source page listing the 2006 DRAFT and 2008 issued editions on the consolidated standards mount.
