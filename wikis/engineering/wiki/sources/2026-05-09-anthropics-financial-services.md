---
title: "Claude for Financial Services — managed-agent reference patterns (anthropics/financial-services)"
tags: [managed-agents, multi-agent-orchestration, plugin-architecture, anthropic, agent-handoff, leaf-worker-subagents]
sources:
  - https://github.com/anthropics/financial-services
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering
---

# Source: Claude for Financial Services — managed-agent reference patterns

**Repository:** [github.com/anthropics/financial-services](https://github.com/anthropics/financial-services)
**License:** Apache-2.0
**Observed pushed_at:** 2026-05-09T11:28:47Z (re-fetched at write time via `gh api repos/anthropics/financial-services --jq '.pushed_at'`)
**Domain framing:** finance-vertical (investment banking, equity research, private equity, wealth management) — content out of scope for this wiki. **Methodology framing:** managed-agent and plugin architecture — the actual reason this source is captured.

## Relevance

This wiki's domain spine is offshore/marine engineering, not finance. The financial-services repo is captured here because its **agent architecture is domain-agnostic methodology** — a concrete reference implementation of multi-agent orchestration patterns that downstream agent code in workspace-hub, digitalmodel, and adjacent repos can pattern-match against. The finance content (Pitch Agent, GL Reconciler, KYC Screener and the like) is incidental; the structural lessons are the load-bearing artifact.

## Key teachings

- **Managed-agent cookbook structure.** Each agent ships as a directory under `managed-agent-cookbooks/<slug>/` containing an `agent.yaml` (orchestrator definition), one or more `subagents/*.yaml` (leaf workers, depth-1), and a `steering-examples.json` (handoff event examples). The structure is uniform across agents, which makes the orchestrator-worker boundary readable at a glance.
- **`callable_agents` research-preview pattern.** The orchestrator delegates to leaf workers via a depth-1 callable-agents mechanism — not arbitrary recursion. This caps blast radius and keeps debugging tractable.
- **`handoff_request` events as the cross-agent control plane.** Inter-agent control flows through a steering-event protocol; `scripts/orchestrate.py` ships as a reference event-loop implementation that consumers can read instead of reinventing.
- **Dual-surface principle.** The same source tree compiles to both a Cowork plugin (`plugins/agent-plugins/<slug>/`) and a Managed Agent template (`managed-agent-cookbooks/<slug>/`). Both reference the same system prompts and skills — one source, two deployment targets.
- **Self-contained agent plugins.** Each agent plugin under `plugins/agent-plugins/<slug>/` bundles a synced copy of the vertical-plugin skills it uses. Installing one plugin is enough; the bundle handles the rest.
- **Vertical-plugin decoupling.** Skills, slash commands, and connectors live in `plugins/vertical-plugins/<vertical>/` and can be installed independently of the end-to-end agents. Lets users adopt `/comps` or `/dcf` without the full Pitch Agent.
- **Partner-built plugin pattern.** `plugins/partner-built/lseg/` and `plugins/partner-built/spglobal/` demonstrate how third parties extend the marketplace alongside Anthropic-authored content — a template for ecosystem extension.

## How this maps to existing wiki structure

- [`concepts/agent-delegation`](../concepts/agent-delegation.md) — base pattern this source extends; `callable_agents` is the concrete API-surface name and the depth-1 constraint is the operational detail.
- [`concepts/orchestrator-worker-separation`](../concepts/orchestrator-worker-separation.md) — `agent.yaml` (orchestrator) plus `subagents/*.yaml` (workers) is a concrete instantiation of the pattern.
- [`concepts/multi-agent-parity`](../concepts/multi-agent-parity.md) — the dual-surface principle is parity through shared source rather than parity through duplicated maintenance.
- [`sources/agent-equivalence-architecture-doc`](agent-equivalence-architecture-doc.md) — closest peer source in this wiki; this entry extends it with managed-agent specifics (cookbook layout, steering events).

## Use as a wiki source

Cite this page when:

- A new managed-agent or plugin-architecture wiki page is authored and needs an external reference implementation to ground the patterns it describes.
- A workspace-hub agent design wants to point at concrete cookbook structure rather than re-derive the convention.
- Cross-link from any future `concepts/managed-agent-orchestration.md` page (currently a deferred gap).

## License and provenance

- License: Apache-2.0 per the repository's `LICENSE` file (verified via GitHub MCP).
- All teachings synthesized from the repository's public README and managed-agent cookbook documentation. No verbatim README content reproduced; methodology described in own words per the wiki's firewall discipline.
