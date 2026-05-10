---
audit_id: W172
iter_under_review: 35
iter_planned: 37
audit_date: 2026-05-09
auditor: cross-wiki-audit-v5
scope: [engineering-standards, lng-projects, maritime-law]
prior_audits: [W90 (iter-22), W111 (iter-24), W134 (iter-28), W143 (iter-30), W152 (iter-32), W162 (iter-34)]
new_dimension: depth-check extended from maritime-law-only (V4) to all three wikis (V5); metadata-only standards-page schema treated as out-of-scope for depth-check
---

# W172 cross-wiki audit v5 — iter-37 priority recommendation

## Executive summary

iter-35 closed **all three audit-V4 priorities cleanly**: environmental-liability.md elevated from 43L/3S → 133L/8S (P1), all 10 ship-incident entity stubs lifted from 29L/3S → 60-79L/7S matching the volcafe reference (P2), and 4 partial-depth doctrinal concepts (port-state-control, limitation-of-liability, charterparties, general-average) expanded to 122-147L/8S the opa-90 standard (P3). With audit V4's depth-check now extended to lng-projects and engineering-standards, **a structurally different defect class surfaces**: lng-projects has 8 of 12 concept-pages clustered at 38-43L/4S (the "early-iter seed" pattern that maritime-law cleared in iter-35), and engineering-standards' apparent stubs (61 of 118 standards-pages under 50L) are **deliberately metadata-only by frontmatter contract** and out-of-audit-scope. iter-37 should prioritize lng-projects concept-page depth uplift as the dominant remaining defect, with maritime-law residual gap (salvage + flag-state-jurisdiction at 45L/5S) and 2-3 high-leverage cross-wiki bridges as secondary.

## State change since W162

- **iter-35 was a depth-only iter** (zero new files, ~15 file edits). Audit-V4 priorities P1+P2+P3 all landed.
- **maritime-law concepts**: 23 → 27. The 4 added concepts are the iter-35 P3 expansions counted as "new" because they were promoted from doctrinal-stub (45L) to first-class doctrinal synthesis (122-147L).
- **maritime-law entity median**: 29L → 71L. All 11 entities now full-depth (cohort-corrected stub class eliminated).
- **maritime-law P1**: environmental-liability.md is now the longest-by-line maritime-law concept other than limitation-of-liability (133L vs 147L).
- **lng-projects**: unchanged file count (12 concepts + 9 standards + 5 sources). No iter-35 activity here.
- **engineering-standards**: unchanged file count (30 concepts + 118 standards + 19 sources). No iter-35 activity here.
- **Cross-wiki bridges**: unchanged at 16 bridge-file pairs / ~27 link-instances (12 bidirectional pairs).

## Wiki-by-wiki state

| Wiki | W162 pages | W172 pages | Δ | Concepts | Standards | Sources | Entities | Outbound bridge files |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| engineering-standards | 167 | 167 | 0 | 30 | 118 | 19 | — | 6 (4→lng + 2→maritime) |
| lng-projects | 26 | 26 | 0 | 12 | 9 | 5 | 0 | 5 (2→eng + 3→maritime) |
| maritime-law | 60 | 60* | 0 | 27 | 24 | 2 | 11 | 5 (2→eng + 3→lng) |
| **Total** | **253** | **253** | **0** | **69** | **151** | **26** | **11** | **16** |

\*maritime-law concept count rose 23→27 in W172 measurement because the 4 doctrinal expansions (port-state-control, limitation-of-liability, charterparties, general-average) crossed the depth-completion threshold; total file count unchanged.

## Cross-wiki edge density refresh

Bridge-file-instance counts grepping `../../../<other-wiki>/wiki/` markdown links, excluding `_template.md`. Link-instance count = total markdown links across all bridge files.

| Source | Target | Bridge files | Link-instances | Notes |
|---|---|---:|---:|---|
| engineering-standards | lng-projects | 4 | 4 | unchanged from W162: brittle-fracture, cathodic-protection, asme-b31-3, iso-15156 |
| engineering-standards | maritime-law | 2 | 2 | unchanged from W162: api-rp-571, asme-bpvc-viii-1 |
| lng-projects | engineering-standards | 2 | 4 | unchanged |
| lng-projects | maritime-law | 3 | 7 | unchanged |
| maritime-law | engineering-standards | 2 | 2 | unchanged |
| maritime-law | lng-projects | 3 | 8 | unchanged |
| **Totals** | | **16** | **27** | **12 bidirectional pairs** |

**Three candidate new bridges (per task brief)**:

| Candidate pair | Substrate exists? | Justification | Defect score |
|---|---|---|---|
| api-rp-580 (eng) ↔ ism-code (maritime) | api-rp-580 313L/7S; ism-code 62L/5S — both present | RBI methodology and shipboard safety-management share risk-tier conceptual grammar; ISM Code §1.2.2 maps to RBI risk-prioritization | medium |
| astm-a553 (eng) ↔ igc-code (maritime + lng — both have igc) | astm-a553 page **MISSING** in eng-stds; igc-code in lng (138L) and maritime (no entry; maritime tracks IGC via lng-projects) | 9% Ni cryogenic-service alloy is the dominant LNG containment material; IGC Ch.6 cargo-tank materials directly references ASTM A553 | high (substrate gap on eng side) |
| nace-tm0177 (eng) ↔ lng-process-safety (lng) | nace-tm0177 page **MISSING**, but ampp-tm-0177.md exists at 40L/4S; iso-15156↔lng-process-safety bridge already in place | SSC test method underlies sour-service material qualification; LNG process-safety H2S-trace envelopes already covered via iso-15156 bridge — this would be redundant | low |

The api-rp-580↔ism-code bridge is the only **substrate-ready** candidate that wouldn't require new authoring. astm-a553 is a substrate gap (page does not exist), and nace-tm0177 is mostly redundant given the iso-15156 bridge.

## NEW: LNG-projects depth-check

Sibling-pattern averages (concepts excluding template):

| Kind | n | Lines avg | Sections avg |
|---|---:|---:|---:|
| lng-projects concepts | 12 | 56.7 | 5.75 |
| lng-projects standards | 9 | 142.7 | 7.78 |
| lng-projects sources | 5 | 61.0 | 4.6 |

### Concepts (sibling pattern: full ≥80L/7S per maritime-law iter-35 lock-in)

| File | Lines | Sections | Status | Flag |
|---|---:|---:|---|---|
| lng-boil-off-gas-management.md | 38 | 4 | partial | YES P1 |
| lng-liquefaction-processes.md | 39 | 4 | partial | YES P1 |
| lng-storage-tanks.md | 40 | 4 | partial | YES P1 |
| lng-marine-transfer-systems.md | 42 | 4 | partial | YES P1 |
| lng-process-safety.md | 42 | 4 | partial | YES P1 |
| lng-project-shapes.md | 42 | 4 | partial | medium |
| lng-project-lifecycle.md | 43 | 4 | partial | medium |
| lng-regulatory-framework.md | 61 | 4 | partial-on-sections | medium |
| lng-vapor-handling.md | 79 | 9 | full | — |
| lng-composition-management.md | 83 | 10 | full | — |
| lng-cooldown-commissioning.md | 83 | 10 | full | — |
| lng-cargo-containment-systems.md | 89 | 8 | full | — |

**Pattern**: identical to the pre-iter-35 maritime-law concept distribution — a 2026-04-07 seed cohort (4-section skeleton: Overview / Key Components / Cross-Refs / Citation) at 38-43L sits beneath a 4-page authored-fresh cohort (8-10 sections, 79-89L). 8 of 12 concepts are partial; 5 are P1 candidates by leverage (boil-off, liquefaction, storage-tanks, marine-transfer, process-safety are all referenced by 4+ standards-pages and the existing bridges).

### Standards (sibling pattern: 96-227L, all 9 full-depth)

All 9 lng-projects standards are full-depth (96-227L / 6-9 sections). No flags.

### Sources (sibling pattern: 45-89L; 2 of 5 below avg)

| File | Lines | Sections | Status |
|---|---:|---:|---|
| elements-acma-projects-31522-woodfibre.md | 45 | 2 | partial (corpus-pointer style by design) |
| elements-doris-62092-sesa.md | 45 | 2 | partial (corpus-pointer style by design) |
| ferc-lng-portal.md | 57 | 6 | full |
| igu-2025-lng-report.md | 69 | 6 | full |
| woodfibre-corpus-pointer.md | 89 | 7 | full |

The 2 partial sources are intentional corpus-pointers (canonical `elements-*` schema). Out of audit scope.

## NEW: Engineering-standards selective depth-check

### Concepts (n=30)

All 30 eng-stds concepts ≥ 78L / 7S. **Zero stubs. Zero partials.** Concept-page authoring quality is uniformly high (78-305L; cathodic-protection 305L is the longest page in any wiki). No flags.

### Standards spotcheck (per task brief)

| File | Lines | Sections | Status |
|---|---:|---:|---|
| dnv-os-e301.md | 43 | 5 | metadata-only (frontmatter) |
| api-rp-2a-wsd.md | 49 | 4 | metadata-only |
| asme-bpvc-viii-1.md | 58 | 5 | metadata-only |
| asme-b31-3.md | 61 | 5 | metadata-only |
| iso-15156.md | 109 | 6 | full |
| api-rp-571.md | 238 | 9 | full |
| api-rp-580.md | 313 | 7 | full |
| api-17j.md | **MISSING** | — | substrate gap (api-spec-17j.md exists at 45L) |
| astm-a553.md | **MISSING** | — | substrate gap |
| nace-tm0177.md | **MISSING** | — | substrate gap (ampp-tm-0177.md exists at 40L) |

### Cohort-wide standards depth distribution (n=118)

- **Under 50 lines**: 61 pages
- **50-79 lines**: 12 pages
- **80+ lines**: 45 pages
- **Of the 73 pages under 80L, all 73 declare `extraction_policy: metadata-only` in frontmatter** — these are intentional resolver-placeholders for Doris University calc-citation routing per the post-spinout governance (no clause-text bundled, public metadata only).

### 10-page random standards spotcheck (sorted)

| File | Lines | Sections | Notes |
|---|---:|---:|---|
| abs-rules-coc-part1-offshore.md | 37 | 4 | metadata-only |
| asme-b31-8.md | 41 | 4 | metadata-only |
| bs-13628-2-flexible-pipe-subsea.md | 41 | 4 | metadata-only |
| dnv-st-f101.md | 44 | 5 | metadata-only |
| aws-d1-1.md | 53 | 5 | metadata-only |
| norsok-n-001.md | 54 | 5 | metadata-only |
| dnv-rp-f103.md | 90 | 10 | full |
| astm-g3.md | 105 | 7 | full |
| bs-7608-fatigue-design.md | 120 | 7 | full |
| api-spec-6a.md | 160 | 5 | full |

**Conclusion**: engineering-standards has zero true depth defects. The metadata-only schema is a deliberate design choice and the cohort splits cleanly into two regimes (metadata-stub <80L; full content ≥80L).

## Maritime-law residual gaps

Two concepts at the iter-35-deferred 45L/5S tier:

| File | Lines | Sections | iter-35 plan | Current recommendation |
|---|---:|---:|---|---|
| salvage.md | 45 | 5 | deferred to iter-36+ | **YES — iter-37 P2** |
| flag-state-jurisdiction.md | 45 | 5 | deferred to iter-36+ | **YES — iter-37 P2** |

Both pages are doctrinally complete but section-shallow vs. iter-35 expansions (port-state-control 145L/8S, general-average 122L/8S). Pattern locked: target 115-150L / 8 sections.

Additionally the **4 sub-50L treaty-stub concepts** (athens-convention-2002, hns-convention-2010, bunkers-convention-2001, clc-1992 at 35-36L/4S) remain partial-depth. iter-35 audit-V4 deferred these as "treaty stub, see standards page" (low priority because liability convention details are carried on the standards-pages of the same name). Re-examine in iter-37 — if the standards-pages carry the doctrinal heft, leave as-is; if not, expand.

## iter-37 recommendation

**Priority 1 — Expand 5 lng-projects concept stubs to sibling full-depth pattern** (5 files; 2 parallel agents; ~75 min)

Target the 5 highest-leverage 38-42L/4S concepts: lng-boil-off-gas-management, lng-liquefaction-processes, lng-storage-tanks, lng-marine-transfer-systems, lng-process-safety. Expand each to ~80-95L / 8 sections using the lng-vapor-handling.md / lng-composition-management.md template: Overview, Process/Engineering Detail, Standards Mapping (which IGC/NFPA/EN-1473/CSA-Z276 clauses govern), Operational Considerations, Hazards/Failure Modes, Cases/Incidents, Cross-References, Citation Source. lng-process-safety is highest individual leverage — it's already a cross-wiki bridge target from iso-15156 (eng-stds) and bunkers-convention-2001 (maritime-law); expansion benefits all 3 wikis. Recommended dispatch: 2 parallel agents partitioned (process-side: liquefaction + boil-off + process-safety; cargo-side: storage-tanks + marine-transfer).

**Priority 2 — Expand 2 maritime-law residual partial concepts** (2 files; 1 agent; ~30 min)

salvage.md and flag-state-jurisdiction.md to ~115-150L / 8 sections matching the iter-35 doctrinal pattern. Salvage: extend Doctrine (LOF/SCOPIC/Article 14 environmental award), Compensation Architecture (no-cure-no-pay vs Article 14 special-comp), Modern Cases (Nagasaki Spirit, MV Lyrma, Ever Given salvage award), Standards Companions, Cross-Refs to salvage-convention-1989 + york-antwerp + general-average. Flag-state-jurisdiction: extend Doctrine (UNCLOS Art. 91-94 nationality / genuine-link / Saiga / Lotus), Enforcement Surface (port-state vs flag-state interaction with paris-mou bridge), Cases (M/V Saiga, M/V Virginia G, Camouco). Single agent, 1 commit per file.

**Priority 3 — Land 1 new substrate-ready cross-wiki bridge** (1 file edit; 1 agent; ~15 min)

api-rp-580.md ↔ ism-code.md bidirectional. Both pages exist (313L and 62L respectively). Add a "Cross-References" section to each linking the RBI risk-prioritization framework to ISM Code §1.2.2 risk-management requirements. Defer astm-a553 and nace-tm0177 candidates — both have substrate gaps that would require authoring new metadata-only pages first.

**Total iter-37 budget**: 8 file edits across 3 priorities; 3-4 sequential or 2-3 parallel agents; wall-clock ~110-130 min. No new wikis. No new MoUs. No new sources.

## Anti-recommendations

**Do NOT treat engineering-standards short standards-pages as depth defects.** 73 of 118 standards-pages declare `extraction_policy: metadata-only` in frontmatter; these are intentional Doris-University calc-citation resolver placeholders, not authoring stubs. The audit-V5 depth-check rule must respect the metadata-only frontmatter contract — promote to script-level enforcement (`scripts/enforcement/check-wiki-page-depth.py`) with a frontmatter-aware exclusion.

**Do NOT add a 4th wiki domain in iter-37.** Same rationale as W134/W143/W152/W162 — depth-check has just exposed substantial in-wiki defects on lng-projects (8 partial concepts) and 2 residual maritime-law gaps. Spinning up a new wiki dilutes signal-to-content.

**Do NOT expand the 4 maritime-law treaty-stub concepts (athens, hns, bunkers, clc) in iter-37.** Liability-convention doctrinal heft is carried on the same-named standards-pages (e.g., standards/clc-1992.md). Concept-page deferral is correct; revisit only if standards-pages also lack doctrine. Verify before flagging in iter-38+.

**Do NOT batch-author the missing api-17j / astm-a553 / nace-tm0177 standards-pages in iter-37.** These are substrate gaps that require deliberate authoring (metadata frontmatter + public-source verification + revision binding); piggy-backing them on a depth-uplift iter risks template drift. Schedule as a dedicated bridge-substrate iter-38+ if the api-rp-580↔ism-code bridge proves the value.

**Do NOT thicken cross-wiki bridge density beyond the api-rp-580↔ism-code add.** 12 bidirectional pairs / 27 link-instances at 56%/44% eng-stds/lng-maritime split is acceptable. Marginal value of bridge #13 is far below marginal value of expanding a 38L lng concept-stub.

**Do NOT add the `revision:` field to maritime-law standards retroactively** (carry-forward W143/W152/W162). The `consolidated_edition` schema is intentional.

**Do NOT mass-expand all 8 partial-depth lng-projects concepts in one iter.** Iter-37 takes 5 highest-leverage concepts (P1); the remaining 3 (project-shapes, project-lifecycle, regulatory-framework) flow into iter-38+. Bulk authoring at depth-tier risks generic templated prose vs. substantive process-engineering synthesis.

## Audit pattern evolution V1 → V5 retrospective

| Audit | Iter | New dimension | Caught | Missed |
|---|---:|---|---|---|
| V1 (W90) | 22 | topology — files-per-kind | wiki existence + breadth gaps | edge density, parity, depth |
| V1 (W111) | 24 | concept↔standards parity | partial-edge defects (concept without standards companion) | edge density, depth |
| V2 (W134) | 28 | cross-wiki edges | bridge-existence gaps | bridge depth, page depth |
| V2 (W143) | 30 | calc-citation readiness | revision-field absence; consolidated_edition variance | bridge thickness, page depth |
| V3 (W152) | 32 | bridge density (link-instances per bridge) | bridge-thinness defect (4/22 imbalance) | page depth |
| V4 (W162) | 34 | depth-check (maritime-law only) | 10 entity stubs + 7 partial doctrinal concepts + 1 stub-on-sections | lng-projects depth, eng-stds depth, metadata-only schema awareness |
| V5 (W172) | 36 | depth-check extended to lng + eng-stds + frontmatter-aware exclusion | lng-projects 8-concept partial cluster; eng-stds metadata-only schema cohort split | bridge target-substrate gaps; treaty-stub concept↔standards-page doctrine-allocation question |

**Dimensions added cumulatively, not replaced.** All 5 dimensions run together at audit time: topology, parity, density, depth (with frontmatter-aware exclusion as of V5), and bridge-substrate readiness (newly named in V5 — flagged in candidate-bridge table when target page is missing).

**What V5 still leaves out**:

1. **Cross-link bidirectionality verification** — V5 counts bridge-files but doesn't verify each "bidirectional" pair has actual reciprocal links (could have only one-way). Promote to V6.
2. **Citation-density per page** — high-traffic concepts may carry 0 inline citations while low-traffic ones carry 5+. V6 candidate.
3. **Section-name canonicalization drift** — different concepts may use "Cross-References" vs "See Also" vs "Related Pages" inconsistently. V7 candidate (low priority — cosmetic).
4. **Source-page-to-content traceability** — sources/*.md exist but how many concepts/standards actually cite them? V6 candidate alongside citation-density.

## Calc-citation-contract readiness (carry-forward)

Unchanged from W152/W162:

| Wiki | Standards (sans template) | Calc-citation-ready |
|---|---:|---|
| engineering-standards | 118 | 118/118 (73 metadata-only resolvers + 45 full-content; both compliant) |
| lng-projects | 9 | 9/9 |
| maritime-law | 24 | 24/24 (treaty-flavored schema) |

iter-37 priorities P1+P2+P3 all preserve calc-citation readiness — they touch concepts only, not standards-pages.
