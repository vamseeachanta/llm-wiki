---
audit_id: W152
iter_under_review: 31
iter_planned: 33
audit_date: 2026-05-09
auditor: cross-wiki-audit-v3
scope: [engineering-standards, lng-projects, maritime-law]
prior_audits: [W90 (iter-22 → eng-std saturation), W111 (iter-24 → maritime-law pickup), W134 (iter-28 → bridges/back-links/parity), W143 (iter-30 → first eng-std bridges + 3 maritime concepts)]
---

# W152 cross-wiki audit v3 — iter-33 priority recommendation

## Executive summary

W143's three priorities all landed in iter-31 (W148 first 3 eng-standards outbound bridges + W149/W150/W151 Hague-Visby/Paris MoU/Rotterdam concept companions), so the substrate is now a **fully-connected 3-wiki graph** for the first time — every ordered-pair has at least one bridge edge, and engineering-standards is no longer a topology sink. Iter-32 is in flight on the regional-MoU spine (W153 Indian Ocean MoU) plus lng concept gap-fill (W154 vapor handling + W155 composition management) plus maritime entity #156 (Volcafe, post-Rotterdam carrier-liability case). The next bottleneck has shifted from **graph topology** (closed) to **bridge depth** — the eng-std↔maritime and eng-std↔lng axes still each carry exactly 1-2 bridge link-instances vs. lng↔maritime at 16 — so iter-33 should focus on (a) thickening eng-std's two thin axes via 3 more bridge pairs, (b) batch-deploying 3 of the 5 remaining regional MoUs (Mediterranean + Black Sea + Riyadh) since template-substitution proved repeatable across Tokyo + Caribbean + Indian-Ocean, and (c) authoring 2-3 high-leverage maritime-law concept companions (Salvage Convention 1989 doctrinal synthesis already exists in concepts/salvage.md per W134, but OPA 90 + LLMC 1996 are real gaps as concepts).

## State change since W143

- **engineering-standards**: 170 → 167 measured pages (concept count steady at 30; standards 118; sources 19). The W143-reported 170 may have included transient files; current grep yields 167 non-index/log/template `.md` under the wiki tree. Cross-wiki edges 0 → **3 outbound** (brittle-fracture, cathodic-protection, asme-bpvc-viii-1). Engineering-standards is no longer a sink.
- **lng-projects**: 26 → 24 net pages on the audit's stricter count (10 concepts + 9 standards + 5 sources, excluding `_template.md`); +2 concepts authored iter-30 (`lng-cargo-containment-systems`, `lng-cooldown-commissioning`). Cross-wiki outbound files 4 → **4** (no net new bridges this iter — but link-instance density up: lng→maritime now 7 instances).
- **maritime-law**: 54 → 55 measured pages (23 concepts + 20 standards + 2 sources + 10 entities). +1 standard `caribbean-mou` + `nairobi-wrc-2007` (iter-30) and 3 concepts in iter-31 (`hague-visby-rules`, `paris-mou`, `rotterdam-rules`). Cross-wiki outbound files 4 → 4, with the addition of solas-1974→asme-bpvc-viii-1 the FIRST outbound to engineering-standards.
- **Cross-wiki bridges**: from 6 bidirectional pairs (W143) to **9 bidirectional pairs** (3 new on the eng-std axes). Graph is now fully connected.

## Wiki-by-wiki state

| Wiki | W143 pages | W152 pages | Δ | Concepts | Standards (sans template) | Sources | Entities | Outbound cross-wiki refs (files) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| engineering-standards | 170 | 167 | -3* | 30 | 118 | 19 | — | **3** |
| lng-projects | 26 | 24 | -2* | 10 | 9 | 5 | 0 | 4 |
| maritime-law | 54 | 55 | +1 | 23 | 20 | 2 | 10 | 4 |
| **Total** | **250** | **246** | **-4*** | **63** | **147** | **26** | **10** | **11** |

*The negative deltas reflect this audit's stricter counting (excluding `index.md`, `log.md`, `overview.md`, `_template.md`). W143's 250 figure included some of those. Real authoring activity since W143: **+5 net pages** (2 lng concepts + 2 maritime standards + 3 maritime concepts; iter-32 in-flight adds another 4-5 once W153/W154/W155/W156 land).

**Observations:**

- Maritime-law is still the hottest wiki — iter-29/30/31 all touched it. Concept↔standards parity is now near-complete: standards-only stems with no concept synthesis are `salvage-convention-1989`, `york-antwerp-rules`, `caribbean-mou`, `nairobi-wrc-2007`, `tokyo-mou` (5 — all DEFER per W134 synthesis-page reasoning OR regional-MoU pattern); concept-only stems with no standards page are the 7 doctrinal-synthesis concepts confirmed DEFER in W134 (`charterparties`, `environmental-liability`, `flag-state-jurisdiction`, `general-average`, `limitation-of-liability`, `port-state-control`, `salvage`). **Genuine actionable parity gaps: 0 concept-side, 0 standards-side** (all remaining mismatches are intentional architectural choices).
- Engineering-standards has crossed the topology threshold (3 outbound bridges) but bridge **depth** is now the limiting factor: 4 link-instances total across the eng-std↔* axes vs. 16 across the lng↔maritime axis. Disparity is structural — eng-std covers 118 standards but only 3 of them link cross-wiki.
- Sources gap on maritime-law unchanged: 2 sources / 55 pages = 3.6%. Treaty-text-as-source remains structural.
- Entity count is static at 10 (maritime-law); iter-32 W156 (Volcafe) will bump to 11.

## Cross-wiki edge density

Bridge counts measured by file-instances grepping `../../../<other-wiki>/wiki/` markdown links, excluding `_template.md`. Link-instance count = total markdown links across all bridge files.

| Source wiki | Target wiki | Bridge files | Link-instances | Bidirectional pairs | Notes |
|---|---|---:|---:|---:|---|
| engineering-standards | lng-projects | 2 | 2 | 2 | brittle-fracture↔lng-process-safety; cathodic-protection↔igc-code |
| engineering-standards | maritime-law | 1 | 1 | 1 | asme-bpvc-viii-1↔solas-1974 |
| lng-projects | engineering-standards | 2 | 2 | (mirror) | bidirectional with above |
| lng-projects | maritime-law | 3 | 7 | 6 | igc↔solas/marpol/hns; ibc↔solas/marpol/hns; lng-regulatory-framework→solas |
| maritime-law | engineering-standards | 1 | 1 | (mirror) | bidirectional with above |
| maritime-law | lng-projects | 3 | 9 | (mirror) | mirror of lng↔maritime |
| **Totals** | | **12** | **22** | **9 pairs** | **All 3 wiki-pairs connected** |

The 3-wiki graph is now fully connected for the first time. But density disparity is severe: lng↔maritime carries 16 link-instances (73% of total) across 6 pairs; eng-std↔* carries 6 link-instances across 3 pairs. **The next bridge-layer defect is depth, not topology**.

## iter-33 recommendation

**Priority 1 — Thicken eng-standards bridge depth: 3 more cross-wiki pairs (~6 file-edits)**

Three high-confidence next-bridges, in priority order, all anchored on existing standards-pages already authored on both sides:

1. `engineering-standards/standards/asme-b31-3.md` ↔ `lng-projects/standards/igc-code.md` — Process-piping pressure-vessel design code; IGC Ch.5 cargo-process piping defers to B31.3 for non-cargo-tank piping. B31.3 is an eng-std spine page; bridging it pulls the whole B31 family into LNG-process traceability.
2. `engineering-standards/standards/iso-15156.md` ↔ `lng-projects/concepts/lng-process-safety.md` — Sour-service materials (NACE MR0175); LNG inlet-gas processing routinely encounters H₂S and CO₂ before liquefaction, and material selection for amine-treatment + acid-gas-removal units cites ISO 15156. ISO 15156 is the 4th-most-cited eng-std stem (25 citations).
3. `engineering-standards/standards/api-rp-571.md` ↔ `maritime-law/standards/marpol-73-78.md` — Damage-mechanism reference (corrosion under insulation, microbial corrosion, atmospheric corrosion) drives bunker-tank and ballast-tank integrity-management programs that MARPOL Annex I/II audit. The bridge formalizes the connection between damage-mechanism failure and pollution-prevention regime; api-rp-571 is the most-cited eng-std stem (49 citations).

These three plus return edges = ~6 file-edits and lift eng-std bridge depth from 4 link-instances to ~10 across both axes. **Estimated agent count: 1 (single edit-only agent, ~30 min wall-clock).**

**Priority 2 — Batch-deploy 3 regional MoUs (Mediterranean + Black Sea + Riyadh)**

W143 confirmed Tokyo MoU and Caribbean MoU were both successful sibling-template substitutions from Paris MoU; iter-32 W153 Indian Ocean MoU is the 4th and validates the 4-substitution-deep pattern. After iter-32 lands, 5 regional MoUs remain (Mediterranean, Black Sea, Riyadh, Vina del Mar, West/Central Africa). The first 3 share the highest topical overlap with already-authored MoU pages: Mediterranean MoU (1997, EU-adjacent, structurally near Paris MoU), Black Sea MoU (2000, regional cooperation pattern), Riyadh MoU (Gulf states, 2004, IMO-aligned PSC framework). Vina del Mar (Latin America, 1992) and West/Central Africa (Abuja MoU, 1999) have more bespoke detention-rate methodologies and weaker English-language source coverage — they belong in a follow-up wave.

Batch-deploy readiness: **HIGH for Med + Black Sea + Riyadh**. Template-substitution from Paris MoU has now run 4 times cleanly; member-state list, secretariat city, performance-list cycle, and inspection regime are all schema-stable. Each MoU = ~150-line template-substitution + 1 return-link in concepts/port-state-control.md. **Estimated agent count: 1 batch agent or 3 parallel agents (parallelizable since file sets disjoint), ~30-45 min wall-clock.**

**Priority 3 — 2 maritime-law concept-page authorings: OPA 90 + LLMC 1996 doctrinal synthesis**

The user-question's enumeration (Salvage Convention 1989, OPA 90, York-Antwerp Rules, LLMC 1996, Tokyo MoU, Caribbean MoU, Nairobi WRC 2007) lists 7 standards-only stems, but 5 of those are intentional DEFER per W134:
- `salvage-convention-1989` — concepts/salvage.md is the synthesis page (back-link sufficient)
- `york-antwerp-rules` — concepts/general-average.md is the synthesis page (back-link sufficient)
- `tokyo-mou` / `caribbean-mou` — both subsumed under concepts/port-state-control.md synthesis
- `nairobi-wrc-2007` — wreck-removal is a narrow operational treaty; concepts/environmental-liability.md and concepts/limitation-of-liability.md jointly cover the doctrinal scope

That leaves **2 genuine high-leverage gaps**: `opa-90` (US-domestic statutory regime distinct from CLC, requires standalone synthesis covering polluter-pays, OSLTF, EPA implementation, post-Exxon Valdez political economy) and `llmc-1996` (global-shipowner-liability cap regime, distinct from CLC's oil-specific cap, with active 2012 amendment uplifts and case-law on package-limitation breach). Both are Tier-1 IMO/US instruments that warrant doctrinal synthesis beyond the standards/* metadata page. **Estimated agent count: 1 (single concept-authoring agent, ~30 min wall-clock).**

### Total iter-33 budget

- ~6 cross-wiki bridge edits + 3 new MoU pages + 2 new maritime concept pages + return-link sweeps
- 1 sequential agent for priority 1, 1 batch agent for priority 2, 1 sequential agent for priority 3 (all parallelizable since file sets disjoint)
- Wall-clock estimate: 60-90 minutes
- No new-wiki pivot

## Anti-recommendations

**Do NOT pivot to a new wiki domain in iter-33.** Engineering-standards bridge depth is still the dominant defect (4 link-instances vs. 16 on the established axis). Adding a 4th wiki before fixing this leaves the substrate in a degraded 4-node graph with one fully-connected pair, two thin pairs, and three new disconnected pairs to seed. Same W134/W143 rationale, weaker urgency now that topology is closed but still binding.

**Do NOT promote any eng-standards entity to a new sub-tier.** The W143 finding stands — all 15 highest-cited eng-standards already exist as first-class standards pages with full calc-citation frontmatter. Sub-15 stems do exist, but reviewing the next 15 (`api-std-650`, `astm-e399`, `nace-sp0472`, etc.) shows they're all already first-class pages too. There is no entity→standards promotion gap in eng-standards. Re-validating iter-31 W143's NO-PROMOTION ruling.

**Do NOT author standards-companion pages for the 7 maritime-law synthesis concepts.** Same as W134 + W143: synthesis pages should not split. Reopening would fragment doctrine.

**Do NOT batch all 5 remaining regional MoUs in one shot.** Vina del Mar and Abuja (West/Central Africa) MoUs have weaker English-language source coverage and bespoke methodology choices that don't sibling-substitute cleanly from Paris/Tokyo/Caribbean/Indian-Ocean. Restrict iter-33 batch to the 3 high-overlap MoUs (Med + Black Sea + Riyadh).

**Do NOT add new lng-projects concept pages in iter-33.** The user-question candidates (cargo-tank stripping/draining, offloading-arms, bunkering, LNG-as-fuel safety-management, aging/quality-degradation) are real gaps but not high-leverage iter-33 priorities. After iter-32 lands W154 vapor handling + W155 composition management, the lng-projects concept count will be 12, with full topical-skeleton coverage of the 8-page W5-C foundation. Bunkering and LNG-as-fuel are large enough to warrant their own iteration, and offloading-arms is operational-equipment depth that should follow a deliberate user request rather than autonomous gap-fill.

**Do NOT add the `revision:` field to maritime-law standards retroactively.** W143 already ruled this out; the `consolidated_edition` + `effective_date` schema is intentional and the calc-citation-contract should be amended (not the standards pages). Re-validating.

## Regional-MoU batch deployment readiness

**Assessment: READY for Mediterranean + Black Sea + Riyadh as a 3-MoU batch.**

| Readiness criterion | Status | Evidence |
|---|---|---|
| Template-substitution proven N times | YES (4×) | Paris MoU → Tokyo (iter-28) → Caribbean (iter-30) → Indian Ocean (iter-32 in flight) |
| Schema stability | YES | 4 substitutions had no schema drift; instrument_type=mou + member-state list + secretariat-city + NIR-cycle all stable |
| English-language source coverage | YES for Med/Black Sea/Riyadh | Memoranda public on respective secretariat sites; IMO MSC.4/Circ documentation; PSC committee reports |
| Topical overlap with existing MoUs | HIGH | All 3 follow Paris MoU institutional template (memorandum + secretariat + annual-meeting + performance-list); minor variations in detention-rate methodology |
| Risk of duplicate doctrinal synthesis | LOW | All 3 fold into existing concepts/port-state-control.md as return-links; no new concept authoring required |
| Disjoint file sets | YES | 3 new standards/*.md + 1 modify of port-state-control.md (sequential return-link); parallelizable across 3 agents |

**Recommended dispatch pattern**: 1 batch agent processing all 3 in sequence (mediterranean → black-sea → riyadh), authoring 3 new standards/*.md + appending 3 return-links to concepts/port-state-control.md in one pass. Or 3 parallel agents partitioned by MoU, with concepts/port-state-control.md serialized to one of the 3 (the others' return-links handled in a final main-session sweep).

**Vina del Mar + Abuja DEFER to iter-34+** pending source-discovery work (Spanish/Portuguese language sources for Vina del Mar; African shipowners' association regional reports for Abuja). Not a 4th-iteration template-substitution.

## Calc-citation-contract readiness (carry-forward)

Unchanged from W143:

| Wiki | Standards (sans template) | Calc-citation-ready |
|---|---:|---|
| engineering-standards | 118 | 118/118 — at ceiling |
| lng-projects | 9 | 9/9 — at ceiling |
| maritime-law | 20 | 20/20 (treaty-flavored schema; intentionally schema-divergent) |

The corollary: iter-33 priorities 1+2+3 all preserve the calc-citation-contract readiness — bridge edits and new MoU pages don't touch frontmatter resolvability. Only the still-open contract-amendment task (recognize treaty-flavored `consolidated_edition` + `effective_date` as a valid `revision`-equivalent) remains as cross-cutting follow-on, separate from cross-wiki audit scope.
