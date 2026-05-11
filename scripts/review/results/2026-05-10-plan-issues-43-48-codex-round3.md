# Codex Adversarial Re-Review — llm-wiki issues 43-48 plan batch (round 3)

Round 3 found one remaining MAJOR: exact TOUCHED paths were still placeholders; later corrected.

Verdict: MAJOR

**Findings**

MAJOR: Validation commands are still not exact executable issue-specific commands.  
All six plans still use placeholders:

```bash
TOUCHED='docs/governance/<target-artifact>.md docs/plans/<this-plan>.md'
```

This does not fully close the prior finding that validation commands must be concrete enough for issue-specific execution, not placeholder-based. Each plan already knows both paths, so each should spell out the exact `TOUCHED` value, for example for #43:

```bash
TOUCHED='docs/governance/sesa-extraction-clearance-checklist.md docs/plans/2026-05-10-issue-43-sesa-extraction-clearance-checklist.md'
grep -RInE 'BEGIN (RSA|OPENSSH|PRIVATE) KEY|password[[:space:]]*=|secret[[:space:]]*=|api[_-]?key[[:space:]]*=|social security|SSN|bank account' $TOUCHED
```

Apply the same concrete substitution for #44-#48.

**Closed Prior Findings**

The secret/PII scan no longer includes impossible no-match patterns for allowed boundary mentions like `/mnt/ace`.

Bare parent issue references are now repo-qualified and include titles.

#47 and #48 now explicitly prohibit copying approval-bound private artifacts, branch contents, ledgers, registries, summaries, aliases, or artifact paths unless separately cleared.

#47 and #48 branch/SHA provenance is repo-qualified.

**Public Safety / Approval Gate**

The plans remain public-safe in substance: they describe metadata boundaries and governance artifacts, not raw extraction or private content promotion. They also remain implementation-blocked until explicit user approval and `status:plan-approved`.

**Required Fix**

Replace the placeholder `TOUCHED` commands in all six plans with exact file paths. After that, I would expect this to move to APPROVE unless the concrete commands introduce new issues.
