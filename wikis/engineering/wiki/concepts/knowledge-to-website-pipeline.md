---
title: "Knowledge-to-Website Content Pipeline"
tags: [content-pipeline, publishing, knowledge-management, static-site]
sources:
  - knowledge-to-website-pipeline
added: 2026-04-08
last_updated: 2026-05-10
---

# Knowledge-to-Website Content Pipeline

> Convert repo-resident engineering knowledge into client-facing web content.

## Purpose

Engineering knowledge accumulated in a versioned repository (wiki pages, methodology
docs, structured skills, parametric reports) carries client value when surfaced as
public web pages. The pipeline is the deterministic path from `git`-tracked source
to a published site, with normalization, review, and deploy stages that preserve
provenance and avoid silent drift.

## Pipeline Stages

```
Source (repo) -> Normalize -> Stage -> Review -> Publish
```

1. **Normalize** — Convert raw markdown to web-ready content: navigation (TOC,
   breadcrumbs), cross-links, author attribution, contact CTAs, SEO metadata.
2. **Stage** — Build a static-site artifact with branded theme; embed interactive
   elements (e.g., Plotly charts) where the source artifact supports it.
3. **Review** — Human or scripted check that nothing private leaked (vendor PDFs,
   internal memory, recruiter notes, customer data).
4. **Publish** — Deploy to the public surface; commit deploy provenance back into
   the repo.

## Content Inventory Pattern

| Content Type | Source location | Readiness |
|---|---|---|
| Wiki pages (multi-domain) | `wikis/<domain>/wiki/` | Raw markdown |
| Engineering skills | `.claude/skills/` (filtered) | Structured YAML + markdown |
| Methodology documents | `docs/methodology/` | Ready for publication |
| Parametric demo reports | reports skill output | Branded HTML+PDF |

## Service Pages from Skills

Each engineering skill becomes a service description page:

```
.claude/skills/marine-offshore/orcaflex/modeling/SKILL.md
    -> /services/orcaflex-modeling/
       Title: "OrcaFlex Marine Dynamic Analysis"
       Content: scope, methodology, deliverables, contact
```

A few hundred skills can generate ~100 service pages spanning OrcaFlex modeling,
mooring design, riser analysis, FEA, cathodic protection, fitness-for-service,
hydrodynamics, VIV, signal processing, and risk assessment.

## Methodology as Marketing

Published methodology documents do double duty:
1. **Technical credibility** — demonstrates rigorous engineering practice.
2. **Client education** — explains why the firm's review process catches what
   others miss.

## Daily Automation

A scheduled job (cron / GitHub Actions) executes nightly:

1. Diff `wikis/`, `docs/methodology/`, `.claude/skills/` against the last
   published baseline.
2. Regenerate the site from normalized sources.
3. Commit and deploy.
4. Log changed pages and any normalization warnings.

## Implementation Options

- **Static-site generator** (Hugo, MkDocs Material) — fast, version-controlled,
  cheap to host. Recommended for engineering-doc surfaces.
- **API-driven** — a backend renders pages on demand from the repo. Always
  current, higher operating cost.
- **CMS** — convert markdown into WordPress / Ghost. Easier for non-technical
  editors, but disconnects content from version control.

## Success Metrics

| Metric | Notional Target | Measurement |
|---|---|---|
| Pages published | 100+ | Site page count |
| Skills converted | 50+ | Skills → service pages |
| Methodology docs published | 5+ | `docs/methodology/` counted |
| Daily build success | >=90% | Cron job log |
| Search ranking (target keywords) | Top 10 | Search Console |

## Related Concepts

- [JSONL Knowledge Stores](jsonl-knowledge-stores.md) — JSONL as a normalized
  knowledge source feeding the pipeline.

## See Also

- `wikis/engineering/raw/papers/knowledge-to-website-pipeline.md` — original
  internal proposal (raw paper) preserved as the source of this concept page.
