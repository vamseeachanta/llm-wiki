---
audit_id: W180
iter_under_review: 37
iter_planned: 39
audit_date: 2026-05-09
auditor: cross-wiki-audit-v6
scope: [engineering-standards, lng-projects, maritime-law]
prior_audits: [W90 (iter-22), W111 (iter-24), W134 (iter-28), W143 (iter-30), W152 (iter-32), W162 (iter-34), W172 (iter-36)]
new_dimensions:
  - publisher-rename detection (NACE→AMPP precedent generalized to SSPC, SAE, ASNT, BS/BSI, DIN VDE, corporate-renames)
  - cross-wiki naming-consistency (slug + frontmatter + cross_links/see_also field discipline)
---

# W180 cross-wiki audit v6 — iter-39 priority recommendation

## Executive summary

iter-37 closed all three audit-V5 priorities cleanly: 5 lng-projects partial-depth concept-pages lifted to full sibling-depth (W176+W177), 3 high-leverage eng-stds metadata-only resolvers (asme-bpvc-viii-1, asme-b31-3, dnv-os-e301 plus iso-19901-7, api-rp-2a-wsd) expanded into doctrinal synthesis, and the api-rp-580↔ism-code bridge landed bidirectionally (W178). iter-37 also added 1 new substrate-fill page (api-17j short-slug, W179) and verified the NACE→AMPP rename clean (13 mentions, 0 stale). With three wikis now at depth-saturation on entities (maritime 12/12), concept-pages (lng 12/12, maritime 17/27 ≥80L), and resolver-coverage, **the next-defect class is no longer depth — it is naming-consistency drift across wikis**: maritime-law has zero `revision:` field on standards (uses `consolidated_edition` instead), eng-stds carries 9 `legacy_code_id` mappings while lng/maritime carry zero, and cross_links vs see_also field usage splits cleanly per-wiki (eng=cross_links only; lng+maritime=mixed). iter-39 should prioritize substrate canonicalization (publisher-rename audit + naming-discipline scripted enforcement) over content authoring; with 7 bidirectional cross-wiki bridges already in place and all three wikis at depth-floor, the marginal value of a 14th content authoring wave is below the marginal value of locking schema discipline before the corpus crosses 300+ pages.

## State change since W172

- **iter-37 was a depth-completion + tactical-cleanup iter** (1 new file, ~14 file edits): W173 closed 2 maritime-law residual concept stubs (salvage 45→103L, flag-state 45→88L); W174 closed 3 lng-projects partial concepts; W175 closed 3 eng-stds resolver expansions; W176+W177 closed remaining 5 lng-projects partial concepts (now 12/12 at full depth); W178 added 2 borderline eng-stds expansions + RBI↔ISM bridge; W179 created api-17j canonical short-slug + verified NACE→AMPP cleanliness.
- **lng-projects depth-saturation reached**: 12/12 concepts ≥79L (up from 4/12 in W172).
- **maritime-law concept-page depth**: 17/27 concepts now ≥80L (up from 11/27 in W172). 4 treaty-stub concepts (athens, hns, bunkers, clc) and 4 mid-depth concepts (marpol, mlc, solas, ism) remain below 80L — see roadmap §6.
- **eng-stds**: 1 file added (api-17j), 5 standards-pages expanded from metadata-only stubs into full doctrinal synthesis.
- **Cross-wiki bridges**: 7 bidirectional pairs (was 6); 18 outbound bridge files; ~30 link-instances (api-rp-580↔ism-code added bidirectionally).
- **Sources**: lng-projects 5→7 sources (giignl-annual-report, igu-2024-lng-report added); eng-stds and maritime-law unchanged at 19 and 2.
- **Maritime-law entities**: 11→12 (x-press-pearl-2021 added).

## Wiki-by-wiki state

| Wiki | W172 pages | W180 pages | Δ | Concepts | Standards | Sources | Entities | Outbound bridge files |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| engineering-standards | 167 | 169 | +2 | 30 | 119 | 19 | — | 7 (4→lng + 3→maritime) |
| lng-projects | 26 | 30 | +4 | 12 | 10 | 7 | 0 | 5 (2→eng + 3→maritime) |
| maritime-law | 60 | 67 | +7 | 27 | 25 | 2 | 12 | 6 (3→eng + 3→lng) |
| **Total** | **253** | **266** | **+13** | **69** | **154** | **28** | **12** | **18** |

Page-count growth +13 is small relative to file-edit count (~14) because iter-37 was depth-uplift, not new-page authoring.

## Cross-wiki edge density refresh — 7 pairs post-iter-37

| Source | Target | Bridge files | Link-instances | Notes |
|---|---|---:|---:|---|
| engineering-standards | lng-projects | 4 | 4 | unchanged W172 baseline |
| engineering-standards | maritime-law | 3 | 4 | **+1 (api-rp-580→ism-code, W178)** |
| lng-projects | engineering-standards | 2 | 4 | unchanged |
| lng-projects | maritime-law | 3 | 7 | unchanged |
| maritime-law | engineering-standards | 3 | 3 | **+1 (ism-code→api-rp-580, W178 return-link)** |
| maritime-law | lng-projects | 3 | 8 | unchanged (template excluded) |
| **Totals** | | **18** | **30** | **7 bidirectional pairs** |

**3-5 candidate bridges for iter-39 (substrate-readiness ranked)**:

| Candidate pair | Substrate-ready? | Justification | Defect score |
|---|---|---|---|
| asme-b31-3 (eng) ↔ ibc-code (lng-projects) | Y — both at full depth (142L + W148-anchored) | LNG cargo-piping below 0°C maps to B31.3 §304 / Appendix M (low-temperature service); ibc-code Ch.6 references ASTM A553 + ASME B31.3 directly | medium-high |
| api-rp-571 (eng) ↔ lng-process-safety (lng) | Y — 238L + 107L | Damage-mechanism catalogue § 4.5 (cryogenic embrittlement) and § 5 (process-side erosion-corrosion) directly applicable to LNG plant integrity-management | medium |
| paris-mou (maritime) ↔ api-rp-580 (eng) | Y — 114L + 336L (RBI bridge already exists via ism-code) | PSC inspection regime = port-side risk-based-inspection sister of RBI; Paris MoU detention-risk algorithm is RBI applied to vessels | medium (potential redundancy w/ ism-code bridge) |
| stcw-convention (maritime) ↔ ferc-lng-portal (lng-source) | N — source-page is corpus-pointer style | LNG-vessel crew certification = STCW endorsement under STCW V/1-2 IGF Code training; bridge target-side is lng-regulatory-framework concept already linked to maritime | low (use lng-regulatory-framework, not a source-page) |
| salvage-convention-1989 (maritime) ↔ lng-marine-transfer-systems (lng) | Y — 124L + 118L | LNG transfer ESD-1/ESD-2 incidents → salvage-of-LNG-cargo legal regime (no historical pure cargo-loss case yet, but doctrinal substrate worth bridging) | low (theoretical bridge; defer until incident provides citation hook) |

iter-39 should land **2 bridges** (asme-b31-3↔ibc-code as P-bridge-1, api-rp-571↔lng-process-safety as P-bridge-2). Both targets exist at full depth; both add asymmetric value to the eng→lng axis (currently 4 link-instances, lowest density of the 6 directional pairs).

## NEW: Publisher-rename detection

Audit-pattern V6 generalizes the W175/W179 NACE→AMPP precedent to a class: **any publisher-rename event must trigger a `legacy_code_id` + `legacy_publisher` frontmatter field on every affected standards-page**. Scan results:

| Rename event | Year | Affected pages | Status | Findings |
|---|---:|---:|---|---|
| **NACE → AMPP** | 2021 | 7 pages (ampp-tm-0177, ampp-tm-0284, ampp-sp0775, ampp-mr-0175-1995, ampp-mr-0175-pt1/pt2/pt3) + 1 (nace-34103 retained NACE prefix as published-imprint convention) | **CLEAN** (W179) | All 7 AMPP-prefix pages carry `legacy_code_id` + `legacy_publisher: "NACE International"`. nace-34103 carries `publisher: AMPP (formerly NACE)` and `legacy_code_id: nace-publication-34103`. 13 cross-wiki mentions audited 0 stale. |
| **SSPC → AMPP** | 2021 | 0 pages currently | **N/A — not yet ingested** | SSPC paint/coating standards (SP-1 through SP-15, PA-1 through PA-15) merged into AMPP at the same 2021 NACE/SSPC consolidation. Zero SSPC-prefix or AMPP-coatings standards-pages exist. **Open substrate gap** — coating-systems concept (added iter-22 W101) has 0-citation forward-references to SSPC. |
| **DNV-OS-F101 → DNV-ST-F101** | 2021 | 1 page (dnv-st-f101.md) | **CLEAN** | Carries `legacy_code_id: dnv-os-f101`. No DNV-OS-F101 stale wikilinks found. |
| **DNV GL → DNV** | 2021 | 12 DNV-prefix pages | **PARTIAL** | DNV GL (the merged 2013-2021 entity) reverted to DNV in 2021. Spot-check shows `publisher: DNV` everywhere — no `legacy_publisher: "DNV GL"` field carried, but no stale "DNV GL" wikilinks either. **Recommendation**: `legacy_publisher: "DNV GL (2013-2021); Det Norske Veritas (pre-2013)"` would document corporate provenance without changing routing. Low priority — the publisher-name change had no slug consequence. |
| **SAE → SAE International** | 2006 (pre-history of repo) | 0 pages | **N/A — not yet ingested** | 0 SAE-prefix pages exist. SAE J-series (esp. J1739 FMEA, J3088 cybersecurity) are candidate substrate gaps if/when automotive-adjacent oilfield electronics get authored. |
| **ASNT (no rename)** | — | 0 pages | **N/A** | ASNT (American Society for Nondestructive Testing) has not renamed; SNT-TC-1A and CP-189 NDT-personnel-qualification standards remain ASNT-published. **Open substrate gap** — fracture-toughness-measurement and related NDT-adjacent concepts have 0 ASNT references. |
| **BS / BSI** | — | 10 BS-prefix pages | **DRIFT-FLAG** | BSI (British Standards Institution) is the publisher; "BS" is the document-prefix. All 10 pages carry `publisher: BSI` + `publisher_full: "British Standards Institution"`. **Naming inconsistency**: bs-7608-fatigue-design and bs-7910-flaw-assessment use BS-document-prefix for the slug; bs-13628-2-flexible-pipe-subsea and bs-13533-drill-through-equipment are British editions of ISO drafts (ISO 13628-2, ISO 13533) — `publisher_catalog_url` points to ISO. **Open question**: should these be renamed to iso-13628-2 / iso-13533 with `legacy_code_id: bs-13628-2`? Currently no `legacy_code_id` on any BS-prefix page. |
| **DIN VDE (no rename)** | — | 0 pages | **N/A** | 0 DIN-prefix pages. German electrical/process safety codes (DIN VDE 0185, DIN EN 50554) candidate substrate for future ingest. |
| **Petroleum Equipment Institute (PEI)** | (no rename) | 0 pages | **N/A** | 0 pages. Not relevant unless retail/storage tank standards needed. |
| **IHS Markit → S&P Global** | 2022 | 0 pages | **N/A** | IHS is a publisher/aggregator, not a standards body. No direct ingest. |
| **ABS (no rename)** | — | 8 pages | **CLEAN** | ABS (American Bureau of Shipping) has not renamed. All 8 pages carry `publisher: ABS` + `publisher_full: "American Bureau of Shipping"`. No legacy fields needed. |
| **NORSOK → Standards Norway** | 2003 (pre-history) | 6 NORSOK pages | **CLEAN** | All 6 carry `publisher: "Standards Norway"` + `publisher_full: "Standards Norway (NORSOK)"` + `legacy_publisher: "NORSOK Steering Committee"`. norsok-d-sr-022 carries the legacy field; spot-check confirms convention. |

**Audit-pattern V6 finding**: the NACE→AMPP convention (legacy_code_id + legacy_publisher) is consistently applied where renames occurred (NACE/AMPP, NORSOK/SN, DNV-OS→DNV-ST), but **not retroactively applied to corporate-rebrands without slug consequence** (DNV GL → DNV). Recommend treating retro-application as cosmetic (low priority), but **mandatory at any publisher-rename event going forward**.

**Open substrate gaps surfaced by V6**: SSPC coating standards (high — coating-systems concept lacks resolver), ASNT NDT-personnel standards (low-medium), SAE J-series (out of scope until automotive-adjacent ingest).

## NEW: Cross-wiki naming-consistency

Three axes audited.

### Axis 1 — Slug conventions

| Wiki | Pattern | Examples | Drift-flag |
|---|---|---|---|
| maritime-law | lowercase-hyphenated; treaty-prefix or convention-name + year | clc-1992, opa-90, marpol-73-78, solas-1974, hns-convention-2010 | **clean** — pattern locked |
| lng-projects | lowercase-hyphenated; lng-* prefix for concepts; ferc-* / igc-code for standards | lng-process-safety, ferc-18-cfr-153, igc-code, ibc-code | **clean** — pattern locked |
| engineering-standards | lowercase-hyphenated; publisher + doc-type + number — but **3 sub-patterns coexist for API**: api-rp-NNN (RP), api-spec-NNN (spec), api-std-NNN (std), and api-NNN (short-slug for in-service codes) | api-rp-580, api-spec-6a, api-std-579, api-510, api-17j (W179 short-slug) + api-spec-17j (long-form pair) | **DRIFT** |

**eng-stds API slug drift**: 28 API pages split across 4 sub-patterns:
- 14 `api-rp-*` (recommended practices, e.g., api-rp-580)
- 6 `api-spec-*` (specifications, e.g., api-spec-6a)
- 3 `api-std-*` (standards, e.g., api-std-579)
- 5 `api-NNN` short-slug (in-service: api-510, api-570, api-653, api-17e, api-17j)

The W179 decision (api-17j short-slug paired with api-spec-17j long-form) **doubled one document** but locked a convention pattern. iter-39 should not retroactively migrate; current state is internally consistent if interpreted as: "API in-service codes use short-slug; API committee documents (RP/Spec/Std) use prefix-form".

**BS slug drift** (per V6 publisher-rename §): bs-13628-2 etc. are ISO mirrors with BS-imprint — slug-vs-publisher_catalog mismatch surfaced; documented in publisher-rename §, not duplicated here.

### Axis 2 — Frontmatter-field discipline

| Field | eng-stds | lng-projects | maritime-law | Variance |
|---|:---:|:---:|:---:|---|
| `code_id` | 119/119 | 10/10 | 25/25 | **clean** |
| `publisher` | 119/119 | 10/10 | 25/25 | **clean** |
| `revision` | 119/119 | 10/10 | 0/25 | **divergence: maritime uses `consolidated_edition` instead** |
| `consolidated_edition` | 0 | 0 | 25/25 | **divergence: maritime-only schema** |
| `legacy_code_id` | 9 pages | 0 | 0 | **eng-stds-only** (NORSOK, AMPP, DNV-ST-F101) |
| `legacy_publisher` | 9 pages | 0 | 0 | **eng-stds-only** |
| `extraction_policy: metadata-only` | 119/119 | spot-check (some) | spot-check (some) | **eng-stds locked; lng+maritime ad-hoc** |
| `raw_copy_allowed` | 119/119 | spot-check | spot-check | same |

**Carry-forward W143/W152/W162/W172**: maritime-law `consolidated_edition` schema is intentional (treaty editions don't follow ISO/API revision-numbering). **DO NOT migrate**. iter-39 should not touch maritime-law frontmatter except to add `revision:` as an alias-field IF calc-citation routing demands a single field — currently the citation-resolver supports either, so no action.

**Recommendation**: promote `extraction_policy: metadata-only` + `raw_copy_allowed: false` to a wiki-level rule for lng-projects + maritime-law standards-pages. eng-stds enforces 119/119; lng+maritime are spot-check ad-hoc. This is a low-effort cleanup (~10 min) but high audit-clarity payoff.

### Axis 3 — `cross_links` vs `see_also` field usage

| Wiki | `cross_links` | `see_also` | Pattern |
|---|---:|---:|---|
| engineering-standards | 9 files | 0 files | **uses cross_links exclusively** |
| lng-projects | 13 files | 8 files | **mixed** |
| maritime-law | 30 files | 4 files | **predominantly cross_links** |

**Drift surface**: lng-projects splits its 21 cross-reference-using pages between two field names. Schema is silent on which field name is canonical (engineering-standards CLAUDE.md line 87 documents `cross_links` as the optional field). **Recommendation**: canonicalize on `cross_links` repo-wide; migrate 12 `see_also` instances (8 lng + 4 maritime) to `cross_links`. ~15 min single-agent task.

### Cross-wiki naming canonicalization actions for iter-39

1. **Migrate 12 `see_also` → `cross_links`** (8 lng + 4 maritime; ~15 min)
2. **Add `extraction_policy: metadata-only` + `raw_copy_allowed: false`** to lng-projects standards (10 pages) + maritime-law standards (25 pages) where missing (~10 min)
3. **Add `legacy_publisher: "DNV GL (2013-2021); Det Norske Veritas (pre-2013)"`** to all 12 DNV-prefix pages (cosmetic, low priority — defer to iter-40)
4. **Resolve BS-vs-ISO slug ambiguity for 4 bs-1362x / bs-1353x pages** (substantive — needs publisher-catalog-cross-check; defer to iter-40 unless decision is made now)

## Engineering-standards depth-completion roadmap — resolver vs full-synthesis

Per V5 W172: 73 of 118 standards-pages declared `extraction_policy: metadata-only`. Post-iter-37: **all 119 pages declare metadata-only** (api-17j added with same frontmatter). Depth distribution:

| Bucket | Pages | Note |
|---|---:|---|
| <50 lines | 58 | pure resolver (publisher + revision + URL) |
| 50-79 lines | 11 | resolver + brief context (Why this page exists / Bounded summary) |
| 80-149 lines | 30 | resolver + doctrinal synthesis (W175/W178 expansion targets) |
| 150+ lines | 20 | full doctrinal synthesis (api-rp-580 at 336L is longest) |

**High-citation-density resolver candidates for iter-39 expansion** (short-page + concept-citation count):

| Page | Lines | Inbound concept refs | Recommendation |
|---|---:|---:|---|
| asme-bpvc-viii-2.md | 42 | 5 | **EXPAND** — Division 2 alternative rules carry FFS-related design-by-analysis content; 5 concept refs is the highest density on the under-50L cohort |
| dnv-rp-b401.md | 42 | 4 | **EXPAND** — cathodic-protection design recommended-practice; cathodic-protection concept (305L, longest in any wiki) currently links to thinner version |
| asme-bpvc-ix.md | 42 | 4 | **EXPAND** — welding qualifications; welding-procedures concept links here |
| ampp-tm-0177.md | 40 | 4 | **defer** — already covered in W175 audit; full doctrine carried via iso-15156 + ampp-mr-0175-pt1 |

**iter-39 P-resolver-1**: expand asme-bpvc-viii-2 + dnv-rp-b401 + asme-bpvc-ix from ~42L to ~90L doctrinal-synthesis tier. ~45 min single agent.

## Source-page coverage refresh

| Wiki | Sources count | Gap analysis |
|---|---:|---|
| engineering-standards | 19 | 9 og-standards-* + 5 doris-* + 1 elements-* + 4 minor. Solid coverage; corpus-pointer style. |
| lng-projects | 7 | +2 since W172 (giignl-annual-report, igu-2024-lng-report). **Gap**: SIGTTO LNG bunkering / OCIMF LNG-handling guidance not yet sourced; both are publisher-page candidates. |
| maritime-law | 2 | maritime-law-cases + maritime-liability-conventions. **Gap**: IMO-circulars source-page (per project memory aces-#4 substrate), CMI conference-papers source-page. |

**iter-39 source-add candidates** (low priority — content is already deep enough that absent source-page is documentation-debt, not retrieval-blocker):

- maritime-law: imo-circulars-source.md (~30 min)
- maritime-law: cmi-conference-papers.md (~30 min)
- lng-projects: sigtto-lng-bunkering.md (~30 min)

## iter-39 recommendation

**Top-3 priorities (substrate over content)**:

**Priority 1 — Naming-consistency canonicalization sweep** (~25 min, 1 agent)
- Migrate 12 `see_also` → `cross_links` (8 lng + 4 maritime)
- Add `extraction_policy: metadata-only` + `raw_copy_allowed: false` to all lng-projects + maritime-law standards-pages where missing (~35 page edits, mostly frontmatter-additive)
- Land schema-discipline as substrate before next content wave. **Highest leverage** because it locks frontmatter-grammar before the corpus crosses 300+ pages.

**Priority 2 — Publisher-rename audit + 1 substrate-gap fill** (~45 min, 1 agent)
- Add `legacy_publisher` field to 12 DNV-prefix pages (cosmetic, ~5 min — but bundle with substrate work)
- Author 1 SSPC→AMPP coatings resolver: ampp-sspc-sp-1.md (or ampp-sp-1) as a metadata-only resolver to close the coating-systems concept's 0-citation forward-reference. Demonstrates V6 publisher-rename pattern in action.

**Priority 3 — 2 substrate-ready cross-wiki bridges + 3 high-citation resolver expansions** (~75 min, 2 parallel agents)
- Bridge 1: asme-b31-3 ↔ ibc-code (eng↔lng axis low-density boost)
- Bridge 2: api-rp-571 ↔ lng-process-safety (eng↔lng axis low-density boost)
- Resolver expansions: asme-bpvc-viii-2 (5-ref), dnv-rp-b401 (4-ref), asme-bpvc-ix (4-ref) from ~42L to ~90L doctrinal-synthesis tier

**Total iter-39 budget**: ~145 min wall-clock; 3-4 sequential or 2-3 parallel agents; ~50 file edits (mostly frontmatter); 1 new file (ampp-sspc-sp-1). No new wikis. No new MoUs. No new entities. Substrate-discipline iter, not content iter.

## Anti-recommendations

**Do NOT migrate maritime-law `consolidated_edition` to `revision`.** Carry-forward W143/W152/W162/W172 — treaty-edition versioning is structurally different from ISO/API revision-numbering. The citation-resolver handles either field. Migration risks breaking 25 maritime-law standards-pages for cosmetic uniformity.

**Do NOT expand the 4 maritime-law treaty-stub concepts** (athens-convention-2002, hns-convention-2010, bunkers-convention-2001, clc-1992 at 35-36L). W172 carry-forward: doctrinal heft is on the standards-pages of the same name. Verify before flagging in audit V7.

**Do NOT batch-migrate `see_also` → `cross_links` without first confirming citation-resolver doesn't break.** The frontmatter parser is permissive but downstream `wiki_search` (#2400) may have schema assumptions. Run a 1-page migration + verify before sweeping all 12.

**Do NOT add a 4th wiki domain in iter-39.** Same rationale as W134/W143/W152/W162/W172 — substrate canonicalization is unfinished; 3 wikis is enough.

**Do NOT retroactively migrate api-rp-* slugs to the api-NNN short-slug pattern.** W179 locked the pattern: short-slug for in-service codes (510/570/653/17e/17j); prefix-form for committee documents (rp/spec/std). Migration breaks 14+ existing wikilinks.

**Do NOT batch-author the missing astm-a553 / nace-tm0177 substrate-gap pages flagged in W172.** ampp-tm-0177 already covers the NACE-TM-0177 use-case via legacy_code_id; astm-a553 remains a real gap but is a single-page authoring task, not iter-driver.

**Do NOT thicken cross-wiki bridges past the 2 candidates in P3.** 7 bidirectional pairs / 30 link-instances approaches the natural ceiling; marginal value of bridge #9 is below marginal value of resolver expansion or substrate canonicalization.

## Audit pattern V1 → V6 retrospective

| Audit | Iter | New dimension | Caught | Missed (closed in later audit) |
|---|---:|---|---|---|
| V1 (W90) | 22 | topology — files-per-kind | wiki existence + breadth | edge density, parity, depth, schema discipline |
| V1 (W111) | 24 | concept↔standards parity | partial-edge defects | edge density, depth |
| V2 (W134) | 28 | cross-wiki edges | bridge-existence gaps | bridge depth, page depth, schema |
| V2 (W143) | 30 | calc-citation readiness | revision-field absence; consolidated_edition variance | bridge thickness, page depth |
| V3 (W152) | 32 | bridge density (link-instances per bridge) | bridge-thinness defect (4/22 imbalance) | page depth, schema discipline |
| V4 (W162) | 34 | depth-check (maritime-law only) | 10 entity stubs + 7 partial doctrinal concepts | lng-projects depth, eng-stds depth, metadata-only schema, naming drift |
| V5 (W172) | 36 | depth-check extended to lng + eng-stds + metadata-only frontmatter awareness | lng-projects 8-concept partial cluster; eng-stds metadata-only schema cohort split; bridge-substrate gaps | publisher-rename detection, naming-consistency drift |
| V6 (W180) | 38 | publisher-rename detection + cross-wiki naming-consistency | NACE→AMPP clean; SSPC substrate gap (coating-systems concept); BS-vs-ISO slug ambiguity (4 pages); DNV GL legacy_publisher absence; see_also vs cross_links drift (12 pages); revision vs consolidated_edition divergence (intentional carry-forward) | citation-density per page (V7 candidate); section-name canonicalization (V7); source-page-to-content traceability (V7); bidirectional-link verification (V7) |

**Dimensions added cumulatively**, not replaced. All 6 dimensions run together at audit time: topology, parity, density, depth (frontmatter-aware), bridge-substrate readiness, **publisher-rename-detection (V6)**, **naming-consistency (V6)**.

**What V6 still leaves out** (V7 candidate list):

1. **Bidirectional-link verification** (V5-deferred) — 7 "bidirectional" pairs need actual reciprocal-link check, not file-presence inference. Promote to V7.
2. **Citation-density per page** — high-traffic concepts may carry 0 inline citations. Particularly relevant as legacy_code_id-bearing pages need provenance citations. V7 candidate.
3. **Section-name canonicalization drift** — Cross-References vs See Also vs Related Pages inconsistency across pages. V7 candidate (low priority — cosmetic).
4. **Source-page-to-content traceability** — sources/*.md exist but how many concepts/standards actually cite them? V7 candidate.
5. **Frontmatter-schema validator script** — promote V6 axis-2 findings to a Level-2 enforcement script per `.claude/rules/patterns.md` Enforcement Gradient.

## Calc-citation-contract readiness (carry-forward)

Unchanged from W152/W162/W172:

| Wiki | Standards | Calc-citation-ready |
|---|---:|---|
| engineering-standards | 119 | 119/119 (all metadata-only frontmatter; resolver-or-doctrinal both compliant) |
| lng-projects | 10 | 10/10 |
| maritime-law | 25 | 25/25 (consolidated_edition schema) |

iter-39 priorities P1+P2+P3 all preserve calc-citation readiness — P1 adds frontmatter fields without removing any; P2 adds 1 metadata-only resolver-page; P3 expands existing pages without changing their frontmatter contracts.
