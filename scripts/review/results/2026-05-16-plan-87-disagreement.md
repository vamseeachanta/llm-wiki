---
title: "Plan #87 review disagreement — Codex r2 MAJOR-5 vs Claude r1 MINOR-7"
plan: docs/plans/2026-05-16-issue-87-pe-phase-4-flow-assurance-choke-integrity.md
issue: 87
date: 2026-05-16
codex_verdict: MAJOR-5
claude_r1_verdict: MINOR-7
---

# Plan #87 Disagreement Summary — Codex r2 MAJOR-5 vs Claude r1 MINOR-7

> Per `feedback_codex_sustained_major_loop`: surface as consensus-vs-minority for user judgment; do NOT auto-cycle.

## Severity divergence

| Aspect | Claude r1 (2026-05-16) | Codex r2 (2026-05-16) |
|---|---|---|
| Overall verdict | MINOR-7 | MAJOR-5 |
| Vendor-IP guard | Adequate per Phase 3 precedent | NOT testable; silent-pass risk for production chemistry |
| Calc-citation contract | Relevance flagged | Half-activated; ambiguous-middle false-compliance trap |
| Multiphase-flow scope | Page-length bound sufficient | Deeper — formula-transcription drift risk |
| PE-vs-DE boundary | Explicit prose | Needs ENFORCEABLE test/gate |
| Vendor citation policy | Followed Phase 3 framing | Silent-failure due to policy conflict |
| Approval recommendation | Approve after MINOR fixes | DO NOT APPROVE; plan patches required |

## Where they agree

- Both flag multiphase-flow scope-control (Claude MINOR-7 ≈ Codex MAJOR-3)
- Both flag PE-vs-DE boundary as needing care (Claude MINOR-1 ≈ Codex MAJOR-4)
- Both run as single-author (Claude r1 only; Codex r2 only — no Gemini r3)

## Where Codex finds NEW defects Claude r1 missed (high-value per `feedback_cross_provider_review_payoff`)

1. **Vendor-IP guard testability** — Codex argues the Phase 3 vendor-archetype-framing precedent (Halliburton SmartWell / Schlumberger StimFRAC named-only) is qualitative; for production chemistry (Nalco / Champion-X / Halliburton MultiChem) the proprietary risk surface is much larger and needs enumerated deny-list patterns.
2. **Calc-citation contract half-activation** — Codex caught that wiki-side `citations:` frontmatter "even if no calc module consumes them" creates false-compliance with no executable enforcement. The actual contract specifies sidecar-per-calc-return and fail-closed at calc time.
3. **Vendor citation policy silent-failure** — Codex argues the policy conflict between "cite by name + general chemistry class only" and "vendor production-chemistry datasheets forbidden" needs an allowed/blocked example table to prevent silent leaks.

## What's actually load-bearing for the user's approval decision

Codex's MAJOR-5 verdict turns on a single judgment: **how much do you trust prose-only governance vs enforceable tests?**

Claude r1 said vendor-IP framing + Phase 3 precedent + plan-time prose is sufficient. Codex argues that for production chemistry (the most-proprietary topic in the wiki to date) prose-only governance has a silent-pass failure mode: implementers produce content that looks compliant at review-time but leaks proprietary detail at content-time.

The Phase 3 framing precedent IS testable (the existing `validate_governance_artifacts.py` scanner catches verbatim chunks), but Codex argues that for production chemistry the deny-list patterns are different (commercial product names, dosage ranges, performance curves) and not currently in the scanner. This is consistent with `feedback_skill_content_scanner_docs_tension` — scanners written for one content class can miss adjacent content classes.

## Three viable paths

1. **Apply Codex's 5 MAJOR patches as plan revisions** — add enforceable chemistry-IP deny rules + clarify calc-citation activation as either real-contract or doc-only metadata + bound multiphase formulas to prose + add cross-wiki boundary tests + add allowed/blocked vendor-citation example table. Re-review (r3, Codex or Gemini). Estimated 30-60 min plan rework + r3 round.

2. **Accept Codex as advisory and approve at Claude r1 MINOR severity** — user judgment that implementation-time vigilance is sufficient for the reversibility cost. Path of least resistance. Preserves Codex artifact as governance trail. Suitable if you trust your implementation discipline + the existing `validate_governance_artifacts.py` scanner's adequacy.

3. **Partial patches** — apply MAJOR-1 (vendor-IP testable deny-list) + MAJOR-5 (allowed/blocked example table) as plan revisions because they're the highest-leverage and lowest-cost. Defer MAJOR-2 (calc-citation contract clarification), MAJOR-3 (multiphase-flow formula-transcription test), MAJOR-4 (DE-page contamination scanner) to sub-issue-implementation-time. Re-review (r3) only if you want full coverage. Estimated 15-30 min plan rework.

## Provenance

- Codex full review: `scripts/review/results/2026-05-16-plan-87-codex.md` (full capture via direct `codex exec`)
- Claude r1 review: `scripts/review/results/2026-05-16-plan-87-claude.md` (full)
- Plan reviewed: `llm-wiki/docs/plans/2026-05-16-issue-87-pe-phase-4-flow-assurance-choke-integrity.md` (post-MINOR-2/MINOR-3 fix-up state at commit `1f32bc79`)
- Codex CLI session id: `019e3171-4904-7e82-980f-aa4b09e8a2b6`
