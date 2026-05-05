# Archived Skill: `personal-tax-filing-packet`

Original path: `/home/vamsee/.hermes/skills/business_admin/personal-tax-filing-packet`
Archived into: `/home/vamsee/.hermes/skills/.archive/umbrella-2026-04-29/business_admin/personal-tax-filing-packet`
Consolidation date: 2026-04-29

---

---
name: personal-tax-filing-packet
version: "1.0.0"
category: business_admin
description: "Assemble a ready-to-file personal federal tax packet from existing repo artifacts: computation draft, filing checklist, entry guide, and optimization review."
type: workflow
tags: [tax, personal-tax, 1040, freetaxusa, filing-packet]
scripts_exempt: true
---

# Personal Tax Filing Packet

## Trigger Conditions
Use when the user wants to prepare or finalize a personal federal tax filing and there is already a workspace/repo with draft tax materials.

Common requests:
- "let us prepare the filing for personal taxes"
- "review my personal tax package"
- "what is ready for filing?"
- "summarize the return and next steps"

## Goal
Produce a concise filing-ready package by locating and reconciling the existing source artifacts instead of recomputing the entire return from scratch.

## Recommended Inputs to Look For
Search under likely tax paths such as:
- `_finance/tax/<YEAR>/personal/`
- `_finance/tax/<YEAR>/`

Priority files:
1. `tax-computation-<YEAR>-draft.yaml`
2. `freetaxusa-entry-guide.yaml`
3. `<YEAR>-filing-checklist.yaml`
4. `<YEAR>-filing-notes.txt`
5. `<YEAR>-tax-optimization-review.yaml`
6. supporting PDFs such as W-2 / 1099s / prior-year return

## Workflow

### Phase 1 — Recover existing filing artifacts
Use `search_files` first. Do not assume filenames are exact.

Look for:
- `*personal*`
- `*freetaxusa*`
- `*filing-checklist*`
- `*tax-computation*`
- `*optimization*`
- relevant PDFs in the tax-year directory

### Phase 2 — Read the canonical sources
Read, at minimum:
1. draft computation YAML
2. filing checklist YAML
3. filing notes / entry guide
4. optimization review YAML if present

Treat the computation YAML as the numeric source of truth unless a later checklist explicitly supersedes it.

### Phase 3 — Extract the filing package
Summarize these sections:
1. Filing identity
   - filing status
   - tax year
   - state filing note
   - dependents
2. Documents needed at desk
3. Expected return outputs
   - AGI
   - taxable income
   - total tax
   - withholding/payments
   - balance due
   - estimated penalty if stated
4. Forms expected
5. Open items / uncertainties
6. Filing method and review checkpoints
7. Payment actions and optional estimated tax recommendations

### Phase 4 — Cross-check for completeness
Compare the checklist, entry guide, and optimization review for:
- open items marked immaterial
- whether any tax-saving opportunities remain
- whether filing is described as ready
- whether there are unresolved items that materially change tax

If only immaterial uncertainties remain, say the package is effectively ready to file.

### Phase 5 — Save a consolidated packet
Write a simple text summary in the same personal tax directory, e.g.:
- `<YEAR>-filling-packet-summary.txt`
- preferably `<YEAR>-filing-packet-summary.txt`

Include:
- key numbers
- source files used
- outstanding items
- filing recommendation

## Output Style
Keep the user-facing result concise and decision-oriented:
1. confirm readiness level
2. list exact files reviewed
3. show bottom-line numbers
4. list open items and whether they are material
5. recommend next filing action
6. offer 2-3 concrete next-step options

## Important Notes
- Do not recompute tax manually if a vetted computation file already exists; synthesize first.
- Use the optimization review to avoid re-litigating already-closed deduction/credit ideas.
- Distinguish clearly between material blockers and low-impact uncertainties (for example small unknown ESPP basis).
- If current-year state is Texas, explicitly note no state income tax return.

## Deliverables
Minimum deliverables:
- user-facing filing summary
- saved consolidated packet summary file in the repo

Optional follow-ons:
- one-page exact-entry sheet
- line-by-line 1099-B lot entry checklist
- post-filing checklist
- next-year estimated tax schedule
- Claude/Chrome handoff prompt for interactive filing
- future GitHub follow-up issues for archive + estimated-tax cadence

## Experiential Additions

### If tax software blocks browser automation
If FreeTaxUSA or another tax site shows CAPTCHA / bot-detection and cannot be automated:
1. stop trying to drive the live site from the agent browser
2. explicitly state that filing must continue in the user's local browser
3. pivot to a human-in-the-loop workflow:
   - prepare a compact exact-entry sheet
   - prepare a Claude handoff prompt for a local Chrome/extension workflow
   - have the local Claude session guide the user screen by screen
4. do not attempt to bypass the CAPTCHA or security gate

A reusable deliverable is:
- `claude-tax-handover-prompt.md`

That prompt should include:
- source-of-truth file paths
- taxpayer facts
- expected final numbers
- explicit instruction not to submit without user approval
- a screen-by-screen checklist for FreeTaxUSA

### Session closeout and future tracking
When the return is prepared but not yet filed, create durable follow-up artifacts so the session can be resumed cleanly:
1. a saved filing-packet summary text file
2. a session exit note with current status, expected numbers, and open items
3. GitHub follow-up issues for:
   - next-year estimated tax payments
   - post-filing archive / payment confirmation capture
   - year-end tax strategy review

This is especially useful when filing must be completed manually in another environment.
