# llm-wiki — public OSS repo (MIT + CC-BY-4.0)

This repo is nested inside workspace-hub for navigation but is independently licensed and independently published to vamseeachanta/llm-wiki.

## Agent-context firewall
- Do NOT echo workspace-hub private memory, recruiter notes, project state, or vendor-derivative deny-lists into commits, PRs, or wiki content here.
- Treat all output as bound by MIT (code) or CC-BY-4.0 (content).
- Local `.claude/` is gitignored — its presence scopes the agent memory namespace away from workspace-hub.

## Service-provider data routing
Per spinout 2026-05-05 + 2026-05-14 governance: 6-row routing matrix covers vendor brochures (off-repo), SEC filings (public entity pages), conference papers (public source pages, DOI), vendor marketing pages (URL ref + off-repo snapshot), regulator/class records (public), user notes (off-repo). Full matrix + worked examples + anti-patterns: `docs/governance/service-provider-data-routing.md`. Vendor-derivative content NEVER lands in this repo.
