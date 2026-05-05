> Git-tracked snapshot from Claude auto-memory. Captured: 2026-05-02
> Source: /home/vamsee/.claude/projects/-mnt-local-analysis-workspace-hub/memory/feedback_naive_secret_scan_false_positive_cascade.md

---
name: Naive secret-scan false-positive cascade
description: Agent-prompt regex `(api_key|token|secret|password)` matches benign prose; rely on hardened pre-commit hook for workspace-hub paths instead of duplicating naive scans
type: feedback
originSessionId: 73cbf578-6fb3-4436-9a95-06ed471cd8b1
---
When an agent prompt instructs subagents to grep changed files for secrets with a naive `(api[_-]?key|token|secret|password|...)` regex BEFORE staging/committing, this regex fires on:
- File **path** references like `scripts/security/secrets-scan.sh` (the literal word "secret" in a file path)
- LLM-output prose containing "tokens used" / "X tokens consumed"
- Library/dependency comments like `# Alternative password-hashing` (e.g. argon2-cffi in pyproject.toml)
- Discussions of GitHub auth scopes mentioning `GH_TOKEN` permission requirements

These false positives blocked S2's digitalmodel sweep and the nightly-batch-2 sweep on 2026-05-01.

**Why:** simple substring matching can't distinguish a credential VALUE from a credential-related TOPIC. Real secret values have structure (sk-XXXX, AKIA-prefixed AWS, ghp_-prefixed GitHub PATs, JWT-like Telegram bot tokens). Topic words are everywhere in security/auth-adjacent codebases.

**How to apply:** for **workspace-hub** repos and worktrees, the workspace-hub pre-commit hook (`.claude/hooks/check-skill-content.sh`) is the trusted gate — it has hardened patterns, `scanner-allow:<id>` marker support, and false-positive filtering. Don't duplicate a naive scan in subagent prompts; let `git commit` exercise the hook. For **non-workspace-hub sibling repos** that don't run the hardened scanner (e.g. aceengineer-admin), keep a defensive scan but tighten the regex to require structure (e.g. `(sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{36}|AKIA[0-9A-Z]{16}|[0-9]{8,}:[A-Za-z0-9_-]{30,})`).
