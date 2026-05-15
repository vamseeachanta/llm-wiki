---
title: "Issue #73 plan — Production Engineering Phase 2 corpus build-out (completions)"
issue: 73
status: plan-review
created: 2026-05-15
last_updated: 2026-05-15
public_safety: API/SPE standards anchors + original concept authoring; NO vendor-confidential completion/frac manuals
---

# Issue #73 Plan — PE Phase 2 (Completions)

## Gate status

- GitHub issue: [vamseeachanta/llm-wiki#73](https://github.com/vamseeachanta/llm-wiki/issues/73) (created 2026-05-15)
- Local plan status: `draft`
- Implementation status: not started; awaiting adversarial review + user approval.
- Predecessor: [Phase 1 epic #61](https://github.com/vamseeachanta/llm-wiki/issues/61), closed 2026-05-15T04:13:47Z, 27 pages across 5 sub-issues.

## Resource intelligence

Sources consulted:

1. **PE overview** (`wikis/production-engineering/wiki/overview.md` lines 47-60) — Phase 2 scope: perforating (shaped charges, overbalanced / underbalanced / EOB, gun systems); sand control (gravel pack, frac pack, expandable screens, prepacked screens); multi-zone & smart completions (selective production, downhole flow control, intelligent-well).
2. **PE Phase 1 epic body** (#61) — pattern reference: 5 sub-issues, each owning 1 method family, each landing ≥1 standards page + ≥1 concept page. Phase 1 sub-issues #62-#66 used `research+ingest(production-engineering):` commit prefix.
3. **Drilling-engineering Phase 1 close-out** ([#49](https://github.com/vamseeachanta/llm-wiki/issues/49)) — established the founding-event commit pattern + cross-domain anchor map.
4. **engineering-standards wiki** — check whether API RP 19B (perforating), API RP 19SC (sand control), etc. are already standards-pages there. If yes, Phase 2 concept pages link to them; if no, Phase 2 lands them.
5. **Calc citation contract** `.claude/rules/calc-citation-contract.md` — applies if completion-design formulas appear (e.g., perforation skin, frac-pack proppant pack permeability).

**Gaps identified:**

- No `wikis/production-engineering/wiki/concepts/perforating.md` exists.
- No `wikis/production-engineering/wiki/concepts/sand-control.md` exists.
- No `wikis/production-engineering/wiki/concepts/multi-zone-completions.md` exists.
- No `wikis/production-engineering/wiki/concepts/smart-completions.md` exists.
- API RP 19B standards-page (verified-real). RP 19SC and RP 19WC are **not** published standalone API standards per Claude r1 review; revised slate uses API RP 90 (sand-control-adjacent), SPE Monograph 9 (sand control), ISO 14998 (smart completion cite-only), SPE 35545 (Gao 1996 smart-completion historical). Existence in `engineering-standards/` TBD for each; verify before Phase 2 execution.

## Public-safety boundary

**Allowed:**

- API / SPE / ISO recommended-practices ingest at the standards-page level (`code_id`, `publisher`, `revision` per #2471 frontmatter; no full-text reproduction).
- Original concept authoring referencing standards + textbooks + open-source field studies.
- Cross-links into `drilling-engineering/` casing-design cluster + Phase 1 artificial-lift cluster.
- Reference to public state-RRC frac-completion registries (Texas RRC W-2, Pennsylvania DEP, Colorado COGCC).

**Forbidden:**

- Vendor-confidential frac-design / completion-design manuals (Halliburton, Schlumberger, Baker Hughes proprietary docs).
- Verbatim copying of API/SPE paragraphs >30 words (paraphrase + cite; standards are paywalled and content-licensed).
- Citation of pages under `wikis/*/wiki/sources/` per [#2482](https://github.com/vamseeachanta/workspace-hub/issues/2482) deny-list.

## Deliverable

Phase 2 corpus expansion adding 3 sub-issues each landing concept page(s) + ≥1 standards page, growing `wikis/production-engineering/wiki/` from post-Phase-1 ~28 pages to ~35-40 pages total. Bidirectional cross-links established between Phase 1 (artificial lift) and Phase 2 (completions).

## Artifact map

| Artifact | Path |
|---|---|
| This plan | `llm-wiki/docs/plans/2026-05-15-issue-73-pe-phase-2-completions.md` |
| Sub-issue 1 (perforating) — new | created during execution; title `research+ingest(production-engineering): perforating — API RP 19B + shaped-charge mechanics + gun systems` |
| Sub-issue 2 (sand control) — new | created during execution; title `research+ingest(production-engineering): sand control — gravel pack + frac pack + screen technologies` |
| Sub-issue 3 (multi-zone & smart) — new | created during execution; title `research+ingest(production-engineering): multi-zone & smart completions — selective production + downhole flow control` |
| Concept pages (≥4) | `wikis/production-engineering/wiki/concepts/{perforating,sand-control,multi-zone-completions,smart-completions}.md` |
| Standards pages (as needed) | `wikis/production-engineering/wiki/standards/{api-rp-19b,api-rp-19sc,api-rp-19wc}.md` OR cross-link to `engineering-standards/` if pre-existing |
| Wiki index update | `wikis/production-engineering/wiki/index.md` (page_count bump, last_updated, table rows for new pages) |
| Wiki log entries | `wikis/production-engineering/wiki/log.md` (one entry per sub-issue) |
| Phase 1 reverse cross-links | `wikis/production-engineering/wiki/concepts/{electric-submersible-pumps,gas-lift-overview,progressing-cavity-pumps}.md` — add Phase 2 forward-references at appropriate sections (Claude r1 review MINOR-4 fix: reverse links must be explicit Files-to-Change, not implicit) |
| Plan review — Claude | `scripts/review/results/2026-05-15-plan-73-claude.md` |
| Plan review — Codex | `scripts/review/results/2026-05-15-plan-73-codex.md` |

## Sub-issue scope breakdown

### Sub-issue 1 — Perforating

**Pages to create:**

- `concepts/perforating.md` — shaped-charge mechanics, overbalanced / underbalanced / extreme-overbalanced perforating, gun systems (TCP / wireline-conveyed / coiled-tubing-conveyed), perforation strategy (shot density, phasing, EHD, EHL).
- `standards/api-rp-19b.md` (if not in `engineering-standards/`) — recommended practice for evaluation of well perforators.

**Cross-links to install:**

- Phase 1 `concepts/electric-submersible-pumps.md` — perforation density affects ESP inflow-performance shape.
- Phase 1 `concepts/gas-lift-overview.md` — perforation strategy affects gas-lift IPR coupling.
- `drilling-engineering/concepts/casing-program-design.md` — perforation policy must respect casing burst rating.

**Acceptance:** sub-issue closed only when both pages land, cross-links bidirectional, `index.md` updated, `log.md` entry exists.

### Sub-issue 2 — Sand control

**Pages to create:**

- `concepts/sand-control.md` — gravel pack (cased-hole, open-hole, high-rate water-pack), frac pack, expandable screens (Halliburton/Weatherford archetypes — concept-only, no proprietary detail), prepacked screens.
- `standards/api-rp-90.md` (annular casing pressure — adjacent control) AND/OR reference to **SPE Monograph 9** (Sand Control, license-clear authoritative reference) cited at the concept-page level. **Note (Claude r1 review):** API RP 19SC is NOT a published standalone API standard; sand-control standards are scattered. Plan execution must use these alternatives.

**Cross-links:**

- Phase 1 `concepts/electric-submersible-pumps.md` — sand-laden production accelerates ESP wear.
- Future Phase 3 `concepts/hydraulic-fracturing.md` — frac pack is the Phase-2/Phase-3 boundary topic (mention in both, primary home in sand-control page).

**Acceptance:** sub-issue closed when concept page lands + standards/SPE reference page lands + cross-links + index/log update.

### Sub-issue 3 — Multi-zone & smart completions

**Pages to create:**

- `concepts/multi-zone-completions.md` — selective production strategies, dual-string completions, sliding-sleeve technology, isolation packers.
- `concepts/smart-completions.md` — intelligent-well technology, downhole flow control, surface-controlled subsurface safety valves (SCSSVs) as part of integrated smart-completion package, downhole fiber-optic monitoring. **Reference: ISO 14998** (intelligent-well completion architecture, cite-only) and **SPE 35545** (Gao 1996 historical smart-completion ref). **Note (Claude r1 review):** API RP 19WC is NOT a published API standard; ISO 14998 is the closest licensable standard surface.

**Cross-links:**

- All Phase 1 artificial-lift method pages — multi-zone affects lift method selection per zone.
- Future Phase 4 `concepts/flow-assurance.md` — smart completions enable proactive flow-assurance intervention.

**Acceptance:** sub-issue closed when both pages land + cross-links + index/log update.

## Sequencing

Recommended order: **Sub-issue 1 (perforating) → Sub-issue 2 (sand control) → Sub-issue 3 (multi-zone & smart)**. Reason: perforating decisions cascade into sand control (sand-prevention starts at perforation design); sand control decisions cascade into multi-zone packer selection. Each sub-issue is plan-and-execute as its own gate; this epic plan covers the slate.

## TDD test list (governance/safety tests)

| Test | What it verifies |
|---|---|
| `tests/test_completion_artifacts.py` | new pages pass existing schema check (frontmatter, required sections) |
| `tests/test_governance_artifacts.py` | no >30-word verbatim chunks from API standards (license-paywall compliance) |
| `tests/test_scan_source_families_safe.py` | new pages don't reference vendor-confidential PDFs |
| `scripts/llm_wiki_strengthening_scorecard.py` re-run | `content_pages()` count reflects new pages |

No runtime calc to reproduce — content-authoring scope. **Reproduction proofs: N/A — content-authoring scope.**

## Acceptance criteria

- [ ] 3 sub-issues created under this epic with title prefix `research+ingest(production-engineering):` matching Phase 1 pattern
- [ ] ≥4 concept pages landed under `wikis/production-engineering/concepts/`
- [ ] ≥1 standards page per sub-issue (or cross-link justified if standard already in `engineering-standards/`)
- [ ] `wiki/index.md` page_count reflects new pages (post-Phase-1 ~28 → post-Phase-2 target ≥35)
- [ ] `wiki/log.md` carries one entry per ingest (3 entries minimum)
- [ ] Bidirectional cross-links between Phase 1 artificial-lift pages and Phase 2 completion pages
- [ ] `tests/test_completion_artifacts.py` + `tests/test_governance_artifacts.py` pass
- [ ] Plan + adversarial review artifacts posted to `scripts/review/results/2026-05-15-plan-73-*.md`

## Risks and open questions

- **Risk:** Vendor-archetype mentions in concept pages may drift into proprietary detail. Mitigation: enforce concept-only abstraction; cite vendor name as "Vendor archetype: <name>" without describing proprietary internals.
- **Risk:** API standards are paywalled; we can cite `code_id` + `publisher` + `revision` but cannot reproduce content. Need a fallback for technical depth on perforation skin calculation, etc. — likely SPE Monograph 16 (Well Cementing) and SPE Monograph 17 (Reservoir Stimulation) as license-clear references; verify their license terms before citation.
- **Risk:** PE Phase 1 cross-links may need updating to reference new Phase 2 pages — adds ~5-10 cross-link edits to existing files.
- **Open:** Should sub-issue sequencing be wave-parallel or strictly sequential? Sequential is safer (smaller diff per commit) but slower; wave-parallel risks `feedback_multi_agent_commit_serialization` if more than one runs at once.
- **Open:** Is `engineering-standards/` the canonical home for API RP 19B, or does it live in `production-engineering/standards/`? Surface in adversarial review.

## Complexity: T2

**T2** — 3 sub-issues, ≥4 new pages, multi-week scope (1-2 sub-issues per session), no runtime test surface, but requires careful cross-link discipline and license-aware authoring. Each individual sub-issue is T2 in its own right; the epic is T2-aggregate.

## Adversarial review summary

**Round 1 — 2026-05-15** (single-author Claude fallback per [[feedback_permission_gate_blocks_cross_review]])

| Provider | Verdict | Key findings |
|---|---|---|
| Claude | MINOR | (1) API RP 19SC and RP 19WC likely don't exist as standalone API standards — replace with API RP 90 / SPE Monograph 9 (sand control) and ISO 14998 / SPE 35545 (smart completion). (2) Sub-issue 1 (perforating) scope is large (5 topic clusters); accept ~500-line concept page or split. (3) Cross-link plan assumes Phase 1 page names — verify by `ls wikis/production-engineering/wiki/concepts/` before installing. (4) Phase 1 reverse-cross-link edits not in Files-to-Change — add them explicitly. |
| Codex | — | not run this round (T2 scope warrants Codex; deferred to user direction) |

**Overall result:** approval-ready after API standards verification (high-priority MINOR-1) and Phase 1 reverse-cross-link Files-to-Change addition (MINOR-4). Review artifact: [scripts/review/results/2026-05-15-plan-73-claude.md](../../../scripts/review/results/2026-05-15-plan-73-claude.md).
