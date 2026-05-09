---
audit_id: W162
iter_under_review: 33
iter_planned: 35
audit_date: 2026-05-09
auditor: cross-wiki-audit-v4
scope: [engineering-standards, lng-projects, maritime-law]
prior_audits: [W90 (iter-22), W111 (iter-24), W134 (iter-28), W143 (iter-30), W152 (iter-32)]
new_dimension: depth-check (per-page lines + sections vs sibling-pattern average; <50% flagged stub)
---

# W162 cross-wiki audit v4 — iter-35 priority recommendation

## Executive summary

All three W152 priorities landed cleanly in iter-33 (W157 thickened the eng-stds bridge axes via api-rp-571↔marpol, asme-b31-3↔igc, iso-15156↔lng-process-safety; W158/W159/W160 deployed the Mediterranean + Black Sea + Riyadh MoU template-substitutions; W161 authored the opa-90 + llmc-1996 doctrinal-synthesis concepts at full depth — 115 and 118 lines respectively). The substrate is now a fully-connected, depth-balanced 3-wiki graph at the edge layer, but **the new depth-check dimension exposes a previously-invisible defect class**: 10 of 11 maritime-law entities are seed-migration stubs at 29-30 lines / 3 sections (vs. the only authored-fresh entity Volcafe at 61/7), and 7 of the 2026-05-02 maritime-law doctrinal concepts (general-average, salvage, limitation-of-liability, port-state-control, flag-state-jurisdiction, charterparties, environmental-liability) sit at 43-48 lines / 3-5 sections — doctrinally complete but section-shallow vs. the recently-authored opa-90/llmc-1996 reference standard. iter-35 should formalize depth-check as a permanent audit dimension and prioritize entity-page expansion over further bridge-density work.

## State change since W152

- **engineering-standards**: 167 → 167 pages (no new authoring; iter-33 was edit-only on bridges). Outbound bridge files 3 → **6** (added asme-b31-3.md, iso-15156.md, api-rp-571.md). Outbound link-instances 4 → **6**.
- **lng-projects**: 24 → **26** measured pages (12 concepts + 9 standards + 5 sources after iter-32 W154/W155 landed). No new authoring this iter; cross-wiki return-edges added on igc-code, lng-process-safety.
- **maritime-law**: 55 → **60** measured pages (23 concepts + 24 standards + 2 sources + 11 entities). +3 standards (mediterranean-mou, black-sea-mou, riyadh-mou) + 2 concepts (opa-90, llmc-1996). Volcafe entity (W156) confirmed at 11/11.
- **Cross-wiki bridges**: 9 bidirectional pairs → **12 bidirectional pairs**; eng-stds depth lifted from 4 → 13 link-instances across both axes (api-rp-571, asme-b31-3, iso-15156 added 9 instances total counting bidirectional citations).
- **NEW — depth defects surfaced**: 10 entity stubs + 7 partial-depth doctrinal concepts identified that no prior audit caught.

## Wiki-by-wiki state

| Wiki | W152 pages | W162 pages | Δ | Concepts | Standards (sans template) | Sources | Entities | Outbound cross-wiki refs (files) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| engineering-standards | 167 | 167 | 0 | 30 | 118 | 19 | — | **6** (was 3) |
| lng-projects | 24 | 26 | +2 | 12 | 9 | 5 | 0 | 6 (was 4) |
| maritime-law | 55 | 60 | +5 | 23 | 24 | 2 | 11 | 6 (was 4) |
| **Total** | **246** | **253** | **+7** | **65** | **151** | **26** | **11** | **18** |

**Observations:**

- Maritime-law remains the most active wiki — iter-33 added 5 of 7 net new pages.
- Engineering-standards bridge depth W152's binding defect is **resolved** (3 outbound files → 6; 4 link-instances → 6 outbound from eng-stds, with 13 total counting return edges).
- Concept↔standards parity remains structurally clean; iter-33 closed 2 of the 7 prior concept-only DEFER pages by elevating opa-90 and llmc-1996 to first-class doctrinal synthesis with standards-page companions already in place (the standards/opa-90.md and standards/llmc-1996.md pre-existed; new concepts/* are the synthesis layer).

## Cross-wiki edge density refresh

Bridge counts measured by file-instances grepping `../../../<other-wiki>/wiki/` markdown links, excluding `_template.md`. Link-instance count = total markdown links across all bridge files.

| Source wiki | Target wiki | Bridge files (W152 → W162) | Link-instances (W152 → W162) | Notes |
|---|---|---:|---:|---|
| engineering-standards | lng-projects | 2 → **4** | 2 → **4** | + asme-b31-3, iso-15156 |
| engineering-standards | maritime-law | 1 → **2** | 1 → **2** | + api-rp-571 |
| lng-projects | engineering-standards | 2 → **2** | 2 → **4** | return-edge thickening on lng-process-safety + igc-code |
| lng-projects | maritime-law | 3 → **3** | 7 → **7** | unchanged |
| maritime-law | engineering-standards | 1 → **2** | 1 → **2** | + marpol-73-78 return-edge |
| maritime-law | lng-projects | 3 → **3** | 9 → **8** | -1 (template excluded; previously over-counted) |
| **Totals** | | **12 → 16** | **22 → 27** | **12 bidirectional pairs (was 9)** |

The eng-stds↔* axes carry 12 link-instances (was 4); the lng↔maritime axis carries 15 (was 16, with one template-excluded correction). **Density disparity has narrowed from 73%/27% to 56%/44% — bridge-depth is no longer the dominant defect.**

## NEW: Depth-check assessment

Sibling-pattern averages (computed across all non-template, non-index pages of the same kind):

| Kind | n | Lines avg | Sections avg | 50% threshold (lines) | 50% threshold (sections) |
|---|---:|---:|---:|---:|---:|
| maritime-law concepts | 23 | 68.9 | 5.96 | 34.5 | 3.0 |
| maritime-law entities | 11 | 33.0 | 3.36 | 16.5 | 1.7 |
| maritime-law standards | 24 | 106.9 | 7.71 | 53.5 | 3.9 |
| lng-projects concepts | 12 | 57.8 | 5.75 | 28.9 | 2.9 |
| lng-projects standards | 9 | 142.6 | 7.78 | 71.3 | 3.9 |

### Page-by-page depth status

Status legend: **full** ≥ avg; **partial** 50-100% of avg on at least one axis; **stub** < 50% on both axes; **stub-by-cohort** = numerically above threshold but only because cohort itself is stub-dominated (n-1 stubs anchor the average). Flag = expansion candidate for iter-35+.

| File | Lines | Sections | Sibling avg (L / S) | Depth status | Flag for expansion? |
|---|---:|---:|---|---|---|
| **maritime-law/concepts** ||||||
| athens-convention-2002.md | 35 | 4 | 68.9 / 5.96 | partial | low (treaty stub, see standards page) |
| hns-convention-2010.md | 35 | 4 | 68.9 / 5.96 | partial | low |
| bunkers-convention-2001.md | 36 | 4 | 68.9 / 5.96 | partial | low |
| clc-1992.md | 36 | 4 | 68.9 / 5.96 | partial | medium — early-iter seed |
| environmental-liability.md | 43 | 3 | 68.9 / 5.96 | **stub-on-sections** | **YES P1** — 2026-04-07 seed; 3 sections vs avg 5.96 |
| flag-state-jurisdiction.md | 45 | 5 | 68.9 / 5.96 | partial | medium — 2026-05-02 doctrinal lean |
| general-average.md | 45 | 5 | 68.9 / 5.96 | partial | medium — 2026-05-02 doctrinal lean |
| salvage.md | 45 | 5 | 68.9 / 5.96 | partial | medium — 2026-05-02 doctrinal lean |
| limitation-of-liability.md | 46 | 5 | 68.9 / 5.96 | partial | medium |
| charterparties.md | 47 | 5 | 68.9 / 5.96 | partial | medium |
| port-state-control.md | 48 | 5 | 68.9 / 5.96 | partial | medium |
| marpol-73-78.md | 49 | 5 | 68.9 / 5.96 | partial | low |
| mlc-2006.md | 49 | 5 | 68.9 / 5.96 | partial | low |
| solas-1974.md | 60 | 5 | 68.9 / 5.96 | partial | low |
| ism-code.md | 62 | 5 | 68.9 / 5.96 | partial | low |
| stcw-convention.md | 87 | 7 | 68.9 / 5.96 | full | — |
| isps-code.md | 93 | 9 | 68.9 / 5.96 | full | — |
| rotterdam-rules.md | 96 | 9 | 68.9 / 5.96 | full | — |
| paris-mou.md | 114 | 10 | 68.9 / 5.96 | full | — |
| opa-90.md | 115 | 8 | 68.9 / 5.96 | full | — (iter-33 W161) |
| llmc-1996.md | 118 | 8 | 68.9 / 5.96 | full | — (iter-33 W161) |
| unclos-1982.md | 126 | 8 | 68.9 / 5.96 | full | — |
| hague-visby-rules.md | 131 | 9 | 68.9 / 5.96 | full | — |
| **maritime-law/entities** ||||||
| amoco-cadiz-1978.md | 29 | 3 | 33.0 / 3.36 | **stub-by-cohort** | **YES P2** — seed-migration stub (n-1 of cohort) |
| eurasian-dream-2002.md | 29 | 3 | 33.0 / 3.36 | stub-by-cohort | YES P2 |
| msc-flaminia-2012.md | 29 | 3 | 33.0 / 3.36 | stub-by-cohort | YES P2 |
| mv-erika-1999.md | 29 | 3 | 33.0 / 3.36 | stub-by-cohort | YES P2 |
| mv-ever-given-2021.md | 29 | 3 | 33.0 / 3.36 | stub-by-cohort | YES P2 |
| mv-prestige-2002.md | 29 | 3 | 33.0 / 3.36 | stub-by-cohort | YES P2 |
| mv-wakashio-2020.md | 29 | 3 | 33.0 / 3.36 | stub-by-cohort | YES P2 |
| sea-empress-1996.md | 29 | 3 | 33.0 / 3.36 | stub-by-cohort | YES P2 |
| torrey-canyon-1967.md | 29 | 3 | 33.0 / 3.36 | stub-by-cohort | YES P2 |
| deepwater-horizon-2010.md | 30 | 3 | 33.0 / 3.36 | stub-by-cohort | YES P2 |
| volcafe-2018.md | 61 | 7 | 33.0 / 3.36 | full | — (authored fresh; reference) |
| **lng-projects/concepts** ||||||
| lng-boil-off-gas-management.md | 38 | 4 | 57.8 / 5.75 | partial | medium |
| lng-liquefaction-processes.md | 39 | 4 | 57.8 / 5.75 | partial | medium |
| lng-storage-tanks.md | 40 | 4 | 57.8 / 5.75 | partial | medium |
| lng-marine-transfer-systems.md | 42 | 4 | 57.8 / 5.75 | partial | medium |
| lng-process-safety.md | 42 | 4 | 57.8 / 5.75 | partial | medium |
| lng-project-shapes.md | 42 | 4 | 57.8 / 5.75 | partial | low |
| lng-project-lifecycle.md | 43 | 4 | 57.8 / 5.75 | partial | low |
| lng-regulatory-framework.md | 61 | 4 | 57.8 / 5.75 | partial-on-sections | low |
| lng-vapor-handling.md | 79 | 9 | 57.8 / 5.75 | full | — |
| lng-composition-management.md | 83 | 10 | 57.8 / 5.75 | full | — |
| lng-cooldown-commissioning.md | 83 | 10 | 57.8 / 5.75 | full | — |
| lng-cargo-containment-systems.md | 89 | 8 | 57.8 / 5.75 | full | — |

### Depth-check summary

- **Hard stubs (< 50% on both axes)**: 0 once cohort effect is excluded — the absolute thresholds are too generous because half the cohorts have stub-dominated averages.
- **Effective stubs (cohort-corrected)**: **10 ship-incident entities** (all except volcafe-2018) at 29 lines / 3 sections — flagged P2 expansion target.
- **Partial-depth on sections (≤50% of section avg)**: environmental-liability (3 sections vs avg 5.96) — flagged P1.
- **Partial doctrinal (45-49 lines, 5 sections)**: 7 maritime-law concepts authored 2026-05-02 — Scope/Doctrine/Cases/Cross-Refs/Citation skeleton is doctrinally complete but section-shallow vs. the iter-33 W161 reference standard (opa-90 / llmc-1996 at 115-118 lines / 8 sections). Flagged P3 medium.
- **lng-projects concepts**: 7 of 12 sit at 38-43 lines / 4 sections — marginally below avg, but cohort is healthy with vapor-handling/composition-management/cooldown-commissioning/cargo-containment as the full-depth reference. Flagged medium for follow-up iters.

## iter-35 recommendation

**Priority 1 — Expand environmental-liability.md to full doctrinal depth** (1 file edit; 1 agent; ~25 min)

environmental-liability.md is the only maritime-law concept page with section-count below 50% threshold (3 vs avg 5.96). It's a 2026-04-07 seed and predates the doctrinal-synthesis pattern that opa-90/llmc-1996 now exemplify. Expand to ~115 lines / 8 sections following the opa-90 template: Scope, Doctrine (CLC strict liability + Bunker + HNS layers + OPA-90 unlimited carve-out), Compensation Architecture (CLC/IOPC/Bunker/HNS/OPA tiers), Enforcement Surface (criminal liability post-Erika; Préjudice écologique; ECJ jurisprudence), Cases (existing 6 + new Bouchard 65, Front Altair, Sanchi 2018), Standards-page Companions, Cross-References, Citation Source. Highest leverage of all iter-35 candidates because it's the connective doctrinal hub for 6 of the 10 entity-page expansions in P2.

**Priority 2 — Expand 10 ship-incident entity stubs to volcafe-pattern depth** (10 files; 1 batch agent or 3 parallel agents; ~60-90 min)

The seed-migrated 29-line / 3-section ship-incident entities (torrey-canyon-1967, amoco-cadiz-1978, sea-empress-1996, mv-erika-1999, mv-prestige-2002, deepwater-horizon-2010, msc-flaminia-2012, eurasian-dream-2002, mv-wakashio-2020, mv-ever-given-2021) should each grow to ~60 lines / 7 sections matching volcafe-2018: Vessel Particulars, Incident Narrative, Legal Proceedings (court/tribunal, ratio decidendi, citations), Doctrinal Significance, Regulatory Aftermath, Cross-References, Citation Source. Each entity has a known canonical case-law citation and a known regulatory follow-on (Torrey Canyon → IMO Civil Liability work; Amoco Cadiz → US 5th Circuit treble-damages; Erika → French Cour de cassation 2012). **Highly batchable**: schema-uniform across all 10, public sources extensive (admiralty case reporters, IMO records, EU Commission post-incident reviews). Recommended dispatch: 1 batch agent processing all 10 in sequence, OR 2-3 parallel agents partitioned by era (pre-1990 / 1990-2010 / post-2010).

**Priority 3 — Expand 4 of 7 partial-depth doctrinal concepts to opa-90 reference standard** (4 file edits; 1 agent; ~45 min)

The 2026-05-02 doctrinal concepts (charterparties, port-state-control, salvage, general-average, limitation-of-liability, flag-state-jurisdiction, environmental-liability) sit at 45-48 lines / 5 sections — doctrinally complete but section-shallow. Top 4 leverage candidates: **port-state-control** (concept-hub for 7 MoU standards-pages now in maritime-law/standards/), **limitation-of-liability** (anchor for llmc-1996 + CLC interaction), **general-average** (high modern-relevance: Ever Given, Suez incidents), **flag-state-jurisdiction** (UNCLOS interaction). Defer salvage + charterparties + (already P1) environmental-liability to iter-36+. Each expansion adds 2-3 sections (Jurisdictional Variants, Case Law, Comparative Notes) and grows the page to ~80-100 lines.

**Total iter-35 budget**: 15 file edits across 3 priorities; 3 sequential or 2-3 parallel agents; wall-clock 90-120 min. No new bridges, no new MoUs, no new wikis.

## Anti-recommendations

**Do NOT add a 4th wiki domain in iter-35.** Same rationale as W134/W143/W152 — depth-check has just exposed substantial in-wiki defects (10 entity stubs + 1 stub concept + 7 partial concepts). Spinning up a new wiki while existing pages are below depth threshold dilutes signal-to-content ratio.

**Do NOT thicken cross-wiki bridges in iter-35.** W157 lifted eng-stds depth from 4 → 13 link-instances; the 56%/44% density split is acceptable. Marginal value of bridge #13/#14 is far below marginal value of expanding a 29-line entity stub to 60 lines.

**Do NOT batch-deploy the remaining 2 regional MoUs (Vina del Mar, Abuja).** Same reason as W152 — Spanish/Portuguese and African regional source coverage is materially weaker than Paris/Tokyo/Caribbean/Indian-Ocean/Med/Black-Sea/Riyadh, and the 4-deep template-substitution chain has now extended to 7-deep with consistent quality. Adding deeper substitutions risks template drift and substandard pages. Defer to a future iter where dedicated source-discovery work precedes authoring.

**Do NOT promote the 10 ship-incident entities to a new sub-tier or split them across schemas.** Volcafe is the depth reference; same `entities/<event-slug>.md` schema with richer authoring. Don't fragment.

**Do NOT add the `revision:` field to maritime-law standards retroactively** (carry-forward from W143/W152). The `consolidated_edition` schema is intentional.

**Do NOT mass-expand all 7 partial-depth doctrinal concepts in one iter.** Iter-35 takes 4 highest-leverage concepts (P3); the remaining 3 (salvage, charterparties, environmental-liability — though environmental-liability is P1, separately prioritized) flow into iter-36+. Bulk authoring at this depth-tier risks generic templated prose vs. genuinely doctrinal synthesis.

## Audit-pattern improvement note — depth-check dimension formalization

iter-33's meta-finding (existence-based audits miss page-depth-stub patterns) is now formally codified as **audit dimension #4 alongside topology, parity, and density**. Going forward:

1. **Compute sibling-pattern averages** (lines + sections) per kind (concepts, standards, entities, sources) per wiki at audit time.
2. **Flag <50% threshold** on either axis as candidate "stub" — but escalate to **cohort-corrected stub** when the cohort itself is stub-dominated (e.g., 10 of 11 ship-incident entities at 29 lines pulls the average down to 33; the absolute threshold of 16.5 is meaningless — cohort-corrected status flags all 10 as expansion candidates against the volcafe reference).
3. **Three-bucket status**: full (≥ avg), partial (50-100% of avg on at least one axis), stub (< 50% on both axes OR cohort-corrected stub). Page age can be a tiebreaker — older seed-migration pages are more likely candidates than recently-authored intentionally-lean pages.
4. **Embed depth-check in the audit-template** as a fixed section between cross-wiki edge density and iter-N+1 recommendation. Future audits run depth-check on every wiki with > 5 pages of any kind.
5. **Migration to enforcement**: this audit-pattern dimension is currently a Level-0 prose check (per `.claude/rules/patterns.md`). When the depth-check produces consistent flagging across 2-3 audits, promote to Level-2 script: `scripts/enforcement/check-wiki-page-depth.py` taking `<wiki>/<kind>` and emitting flag list. Do NOT promote to Level-3 hook — this is a periodic-audit dimension, not a per-commit guard.

The depth-check dimension does NOT replace the existing topology/parity/density dimensions. All four run together at each cross-wiki audit cycle.

## Calc-citation-contract readiness (carry-forward)

Unchanged from W152:

| Wiki | Standards (sans template) | Calc-citation-ready |
|---|---:|---|
| engineering-standards | 118 | 118/118 |
| lng-projects | 9 | 9/9 |
| maritime-law | 24 | 24/24 (treaty-flavored schema) |

iter-35 priorities P1+P2+P3 all preserve calc-citation readiness — they touch concepts and entities, not standards-pages.
