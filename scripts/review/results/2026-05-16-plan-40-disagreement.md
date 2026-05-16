---
title: "Plan #40 review disagreement — Codex r2 BLOCKER vs Claude r1 MINOR"
plan: docs/plans/2026-05-15-issue-40-reservoir-engineering-literature.md
issue: 40
date: 2026-05-16
codex_verdict: BLOCKER
claude_r1_verdict: MINOR
---

# Plan #40 Disagreement Summary — Codex r2 BLOCKER vs Claude r1 MINOR

> Per `feedback_codex_sustained_major_loop`: surface as consensus-vs-minority for user judgment; do NOT auto-cycle.

## Severity divergence

| Aspect | Claude r1 (2026-05-15) | Codex r2 (2026-05-16) |
|---|---|---|
| Overall verdict | MINOR | BLOCKER |
| License triage | Not flagged as defect class | Defect: NOT fail-closed for mixed-corpus founding |
| Founding-event rollback | Not addressed | Defect: no rollback / taint-response story |
| State-drift (label vs frontmatter vs marker) | MINOR — noted but resolvable | BLOCKER — execution self-approves narrow scope |
| 5-wave PR strategy from May 7 issue comment | Not caught | Defect: plan-vs-prior-comment divergence |
| Standards anchor enumeration | Adequate at high level | Defect: too generic; should enumerate at plan-time |
| Recommendation | Approve after MINOR fixes | DO NOT APPROVE; user judgment required |

## Where they agree

- Both flag the scope-narrow-vs-issue-body tension
- Both note the state-drift between GH label, plan frontmatter, and marker file
- Both run as single-author (Claude r1 only; Codex r2 only) — no Gemini r3 run

## Where Codex finds NEW defects Claude r1 missed

Per `feedback_cross_provider_review_payoff`, these are the high-value findings:

1. **License-fail-closed-by-construction** — Codex argues the deny-list workflow must be safe-by-construction, not operator-vigilance-dependent. Material risk surface for a 30K-PDF corpus → public CC-BY-4.0 repo with perpetual reversibility cost.
2. **Founding-event rollback procedure** — Codex argues a plan founding the 11th wiki domain in a public repo must specify post-publication taint-response steps (revert, downstream-archive notification, fork-cleanup).
3. **Wave-PR strategy state divergence** — Codex caught that 5-wave landing strategy in May 7 comment is silently dropped from canonical plan. Should be explicitly killed or explicitly retained.

## What's actually load-bearing for the user's approval decision

The Codex BLOCKER is driven mostly by **risk-management defects** (license fail-closed-by-construction, founding-event rollback) rather than **correctness defects** (does the plan describe-the-right-thing-to-do). Claude r1's MINOR verdict assumes risk-management defects are resolvable during implementation; Codex's BLOCKER verdict assumes they need plan-time fixes because once content lands in a public repo the cost of getting it wrong is high.

The user-decision lens is: **how much do you trust operator-vigilance during implementation vs how much do you want plan-time safe-by-construction guarantees?** For a founding event in a public CC-BY-4.0 repo, the Codex-side argument has merit. For a researcher-driven exploratory ingest where you'll be the implementer, the Claude-side argument has merit.

## Three viable paths (compatible with Codex's recommendation)

1. **Apply Codex defects as MAJOR plan revisions** — rewrite plan with fail-closed license workflow + rollback procedure + explicit 5-wave dispatch decision + specific standards-anchor enumeration; re-review (r3, Codex or Gemini); then user approval. Estimated 1-2 sessions of plan rework.

2. **Accept Codex findings as informative-only and approve at Claude r1 MINOR severity** — write the missing `.planning/plan-approved/40.md` marker, leave plan as-is. User judgment that the implementation-time mitigations are sufficient for the reversibility cost. Path of least resistance; preserves Codex artifacts as advisory.

3. **Narrow scope further to corpus-manifest-only** — defer wiki-domain founding to a separate later plan; current scope becomes Step 1 (sweep + bookmark) only. Reduces reversibility cost dramatically (no published wiki pages, just an internal manifest). User-prompt-listed path (3) from the earlier surface.

## Provenance

- Codex full review: `scripts/review/results/2026-05-16-plan-40-codex.md` (partial-capture; ENV-MISMATCH banner)
- Claude r1 review: `workspace-hub/scripts/review/results/2026-05-15-plan-40-claude.md` (full)
- Plan reviewed: `llm-wiki/docs/plans/2026-05-15-issue-40-reservoir-engineering-literature.md`
