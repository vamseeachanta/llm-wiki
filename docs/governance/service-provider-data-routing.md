---
title: Service-provider data routing matrix
date: 2026-05-14
authority: this doc expands the one-line "Vendor PDFs" rule in llm-wiki/CLAUDE.md to a 6-row matrix
related:
  - workspace-hub#2482 (vendor-derivative deny-list)
  - workspace-hub/docs/governance/2026-05-14-service-provider-data-routing-and-bsee-ingest-design.md (design doc)
  - workspace-hub/docs/governance/vendor-pdf-inventory.md (off-repo inventory)
---

# Service-provider data routing matrix

This wiki publishes under MIT (code) + CC-BY-4.0 (content). Service-provider data enters the ecosystem through six different routes depending on document class and copyright surface. The matrix governs which path is correct.

## The matrix

| Document class | Examples | Route | Rationale |
|---|---|---|---|
| Vendor brochure / spec sheet / marketing PDF | Vessel LTRs, equipment data sheets, product brochures | **Off-repo**: private vendor mount (`/mnt/ace/vendor-pdfs/<vendor-slug>/`) | Copyright owned by vendor; not redistributable under CC-BY-4.0; per workspace-hub#2482 deny-list |
| SEC filings (10-K, 10-Q, 8-K, investor decks) | Public-company fleet descriptions, segment disclosures | **Public wiki**: entity page, paraphrased with page-citation to the filing | Public record under US securities law; factual disclosures not copyrightable; prose paraphrase under fair-use |
| Conference papers (SPE / OTC / IADC / OMAE) | DOI-stable technical disclosures | **Public wiki**: source page, DOI-grounded paraphrase | Conference-publication norms support fair-use paraphrase; mirrors the Papkov source-page precedent in drilling-engineering |
| Press releases / vendor marketing landing pages | Vendor service-line landing pages, press disclosures | **Public wiki**: URL-only bibliographic reference for facts disclosed; **off-repo** copy of the verbatim page (HTML snapshot) at private mount | PR/marketing prose is vendor-controlled; fact extraction allowed, prose copy is not |
| Public classification-society / regulator records | ABS / DNV / LR / BV / IACS class records, USCG vessel registry, IMO MODU records, BSEE OCS reports | **Public wiki**: entity/standards page directly | Class-society and regulator records are public factual data; US federal-regulator publications additionally fall under 17 U.S.C. § 105 (public-domain) |
| User's own annotated extracts | Engineering notes after reading a vendor brochure | **Off-repo**: alongside the source at the private mount | The notes are the user's, but the chain of custody must stay private so they don't accidentally land in a public-repo entity page |

## When you must choose a route

1. **Identify the document class** — match to one of the 6 rows above.
2. **Apply the route** — if the row says "off-repo", deposit at `/mnt/ace/vendor-pdfs/<vendor-slug>/` and add an entry to `workspace-hub/docs/governance/vendor-pdf-inventory.md`. Never check the asset into llm-wiki.
3. **If the row says "public wiki"** — write paraphrased content in the appropriate sub-wiki (entity / source / standards / concepts) with the citation noted in YAML frontmatter `sources:` field. Never transcribe vendor tables, drawings, marketing copy, or proprietary technical content verbatim.
4. **If the row says "hybrid"** (row 4) — URL-only reference goes in the wiki page that needs it; the verbatim HTML or PDF snapshot goes off-repo.

## Worked examples

- **Helix Energy Solutions Q4000 LTR brochure (vendor product PDF)** → row 1 → `/mnt/ace/vendor-pdfs/helix-esg/` (off-repo). Recorded in `workspace-hub/docs/governance/vendor-pdf-inventory.md` on 2026-05-14.
- **Helix Energy Solutions 10-K Well-Intervention segment description** → row 2 → cite paraphrased on a future `wikis/drilling-engineering/wiki/entities/helix-energy-solutions-fleet.md` page.
- **BSEE 2024 *Deepwater Riser Life Extension Perspectives and Process*** → row 5 → public-domain US federal regulator publication, ingest directly into `wikis/drilling-engineering/wiki/sources/` (no off-repo deposit). Done 2026-05-14.
- **Helix "Riser-Based Well Intervention" service-line landing page** → row 4 → URL-only reference allowed in any future entity-page that needs it; verbatim HTML snapshot kept off-repo at `/mnt/ace/vendor-pdfs/helix-esg/`.

## Anti-patterns

- **Never cite a vendor brochure as a source for a concept page**. Concept pages need textbook / DOI / public-manual grounding per the workspace-hub feedback memory `feedback_llm_wiki_concept_pages_need_public_references`. A single vendor brochure as sole source fails day-one lint.
- **Never transcribe vendor tables, dimensions, drawings, or marketing copy verbatim into the public wiki**, even paraphrased into prose if the paraphrase preserves the vendor's structuring choices (selection of which dimensions to report, etc.). Reach for public-record sources (10-K, class-society records, conference papers) when the same fact is needed.
- **Never bypass the matrix by routing a vendor-brochure-derived fact into a wiki sources/ page** under the rationale that "the brochure URL is publicly accessible". Public accessibility ≠ permission to redistribute under CC-BY-4.0.

## Promoting this rule to enforcement

This is currently a Level-0 prose rule per workspace-hub `.claude/rules/patterns.md` enforcement gradient. Promotion path if violations recur:

- **Level-1 micro-skill**: auto-load on llm-wiki edit-session entry.
- **Level-2 script**: pre-commit hook that scans `wikis/**/sources/*.md` for known vendor-brochure-URL patterns (`*helixesg.com/downloads/*`, `*halliburton.com/products/*`, etc.) and blocks the commit with a pointer to this matrix.
- **Level-3 hook**: stop-hook in workspace-hub `.claude/settings.json` that fires the same scan across all child repos before any push.
