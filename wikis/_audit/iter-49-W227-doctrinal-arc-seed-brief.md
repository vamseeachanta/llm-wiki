---
audit_id: W227
iter_seed: 49
target_iter_for_arc_open: 50
brief_date: 2026-05-10
auditor: doctrinal-arc-seed-brief
parent_audit: W220 (iter-48 cross-wiki audit v11)
scope: [marine-insurance, offshore-decommissioning]
type: candidate-arc-scoping
status: user-decision-needed
---

# W227 doctrinal-arc seed brief — marine-insurance vs offshore-decommissioning

## Executive summary

W220 V11 declared corpus saturation at 322 pages and instructed iter-49+ to pivot from substrate-fill to (a) depth-expansion of high-traffic pages and (b) seeding a NEW doctrinal arc. This brief scopes the two candidate arcs flagged in V11 P3 — **marine-insurance** and **offshore-decommissioning** — across substrate availability, cross-wiki bridge potential, doctrinal coherence, practitioner relevance, and build cost. Both arcs are genuinely new (verified absent from the existing 322-page corpus), but they differ materially on bridge density and substrate availability; this brief recommends **seeding marine-insurance at full scope in iter-50** and **deferring offshore-decommissioning to iter-52+** pending further substrate-fill on the engineering side.

## Marine-insurance arc

### Scope

Marine-insurance is the doctrinal complement to maritime-law: maritime-law sets the liability ceiling (LLMC 1996, CLC 1992, Athens 2002) and the compulsory-insurance triggers (CLC Article VII, Bunkers Article 7, Nairobi WRC Article 12, Athens Article 4bis), and marine-insurance is the market that supplies the certificates of financial responsibility, prices the war-risk premium, structures the P&I mutuality, and underwrites hull-and-machinery + cargo. The arc covers the contractual + market layer that sits underneath the convention layer.

### Ties to existing wikis

- **maritime-law**: 6 concept pages currently reference insurance incidentally — clc-1992, bunkers-convention-2001, nairobi-wrc-2007, athens-convention-2002, hague-visby-rules, environmental-liability. Each becomes a bidirectional bridge target.
- **maritime-law/entities**: 8 of the 24 incident entities (mv-prestige-2002, mv-erika-1999, deepwater-horizon-2010, mv-wakashio-2020, x-press-pearl-2021, fso-safer-2023, front-altair-2019, sanchi-2018) have documented P&I + hull recoveries; each entity gets a 1-2 sentence insurance addendum.
- **lng-projects**: JWC listed-area pricing intersects with LNG voyage routing (Strait of Hormuz, Bab-el-Mandeb, Black Sea); a single JWC-bulletins source page bridges to lng-projects.

### Sub-doctrines (arc skeleton)

1. P&I clubs structure (mutuality, calls, releases, IG Group pooling)
2. Lloyd's syndicate model (Names, corporate capital, Lloyd's Act 1982, Reconstruction & Renewal)
3. Hull-and-machinery vs liability vs war-risk distinction (clauses, exclusions, ITC-Hulls, IHC 2003)
4. International Group (IG) of P&I Clubs — pooling agreement, reinsurance contract, group excess
5. JWC (Joint War Committee) listed-area model, pricing, withdrawal mechanics
6. Compulsory-insurance enforcement (blue cards, certificates of financial responsibility)
7. P&I rule-changes 2018-2024 (sanctions, cyber, pandemic, climate, decarbonization)

### Initial substrate (~10 standards-equivalent pages)

Standards-page slugs (treated as `wiki/standards/<slug>.md` under a new `marine-insurance/wiki/standards/` tree):

1. itc-hulls-1983 (Institute Time Clauses — Hulls)
2. ihc-2003 (International Hull Clauses)
3. ig-pooling-agreement (IG of P&I Clubs pooling agreement, current revision)
4. jwc-listed-areas-bulletin (JWC bulletin format + listed-areas list)
5. lloyds-act-1982 (statutory frame for Lloyd's market)
6. p-and-i-rule-book-template (skeleton of a typical P&I rule book — based on UK Club / Britannia / American Club rulesets)
7. mia-1906 (UK Marine Insurance Act 1906 — still the doctrinal anchor for hull + cargo)
8. iua-clauses (International Underwriting Association cargo clauses A/B/C)
9. cofr-opa-90 (Certificate of Financial Responsibility under OPA-90 — bridges to maritime-law/concepts/opa-90)
10. blue-card-template (CLC/Bunkers/HNS/WRC blue-card structure)

### Initial concept-page substrate (~10 concept-pages)

Concept-page slugs under `marine-insurance/wiki/concepts/`:

1. p-and-i-club-mutuality
2. lloyds-syndicate-model
3. hull-machinery-vs-liability
4. war-risk-insurance
5. cargo-insurance
6. compulsory-insurance-triggers
7. reinsurance-and-retrocession
8. financial-responsibility-certificates
9. salvage-and-scopic-financing (bridges to maritime-law/concepts/salvage)
10. limitation-and-insurance-interaction (bridges to maritime-law/concepts/limitation-of-liability)

### Source-page candidates (~5-7 source pages)

- IG of P&I Clubs annual review (publicly downloadable, CC-attribution clean)
- Individual P&I club annual reports — UK Club, Gard, Britannia, American Club, Steamship Mutual (5 club reports; public)
- Lloyd's market data — Lloyd's annual report + Lloyd's market bulletin index
- JWC bulletins index (public via Lloyd's Market Association)
- IUMI (International Union of Marine Insurance) annual statistics
- BIMCO / Intertanko clause libraries (public reference)

## Offshore-decommissioning arc

### Scope

Offshore-decommissioning is the lifecycle-phase complement to engineering-standards: where engineering-standards covers design, construction, operation, and inspection, decommissioning covers post-production cessation — well plug-and-abandonment (P&A), subsea-system retrieval, jacket removal vs rig-to-reef, FPSO disposal, environmental remediation. The doctrinal anchors are OSPAR Decision 98/3 (North-East Atlantic), BSEE/USCG decommissioning rules (US OCS), and the IMO Guidelines on Removal (1989, IMO Resolution A.672(16)).

### Ties to existing wikis

- **engineering-standards**: ties to API RP 17 series (subsea), DNV-OS-C401 (hull-integrity), and a NEW DNV-OS-F211 (decommissioning) page that does not yet exist. Decommissioning extends the lifecycle of each design standard from "as-designed" through "abandoned."
- **maritime-law**: ties to UNCLOS Article 60(3) (removal obligation) — already covered in maritime-law/concepts/unclos-1982 — and to the IMO 1989 Removal Guidelines.
- **lng-projects**: minimal direct tie; LNG decommissioning is rare (export terminals typically converted, not removed).

### Sub-doctrines (arc skeleton)

1. Well plug-and-abandonment (P&A) — temporary, suspended, permanent
2. Subsea-system retrieval (manifolds, jumpers, flowlines, umbilicals)
3. Jacket removal — full removal vs partial removal vs rig-to-reef
4. FPSO disposal — green recycling vs sinking-in-place permits
5. Pipeline decommissioning — removal vs leave-in-place vs trench-and-bury
6. Environmental remediation — drill-cuttings piles, sediment, hydrocarbon residuals
7. Post-decommissioning monitoring (long-tail liability)

### Initial substrate (~10 standards-equivalent pages)

Standards-page slugs under `offshore-decommissioning/wiki/standards/`:

1. ospar-decision-98-3 (OSPAR 1998 Decision on disposal of disused offshore installations — the North Sea anchor)
2. imo-resolution-a-672-16 (IMO 1989 Removal Guidelines)
3. bsee-30-cfr-250-subpart-q (US OCS decommissioning regulations)
4. uk-ompr-2009 (UK Offshore Marine Petroleum Regulations / Energy Act 2008)
5. norway-pma-decommissioning (Norwegian Petroleum Management Act + decom guidelines)
6. dnv-os-f211 (DNV-OS-F211 — decommissioning planning, not currently in corpus)
7. api-rp-17-decom (API RP 17 series subsea-decom relevant subset)
8. iogp-report-584 (IOGP decommissioning report — publicly downloadable)
9. og21-decom-strategy (Norwegian OG21 decommissioning strategy)
10. nogepa-industry-standards (Netherlands NL decommissioning standard 2.5/2.6)

### Initial concept-page substrate (~10 concept-pages)

Concept-page slugs under `offshore-decommissioning/wiki/concepts/`:

1. well-plug-and-abandonment
2. subsea-system-retrieval
3. jacket-removal-vs-rig-to-reef
4. fpso-disposal
5. pipeline-decommissioning
6. environmental-remediation-decom
7. post-decom-monitoring
8. comparative-assessment-decom (the OSPAR-mandated multi-criteria decision framework)
9. cessation-of-production
10. decommissioning-cost-estimation

### Source-page candidates (~5-7 source pages)

- BSEE Notice-to-Lessees (NTL) bulletins index (public)
- OSPAR decisions + recommendations index (public)
- OG21 decommissioning report (Norwegian, public)
- IOGP report 584 + 463 (decommissioning + cost-estimation; public)
- Brent Decommissioning programme — Shell public dossier (CC-attribution clean — verify)
- Gulf of Mexico structures-removal database (BSEE, public)
- Wood Mackenzie / Westwood public-release decommissioning briefings (selective; license-check)

## Comparison + recommendation

| Dimension | Marine-insurance | Offshore-decommissioning |
|---|---|---|
| Cross-wiki bridge potential | **High** — 6 maritime-law concepts + 8 entities + 1 lng-projects bridge = 15 immediate bridges | Medium — 1 maritime-law concept (unclos-1982) + 1 NEW eng-stds page (DNV-OS-F211) + speculative API-RP-17 ties |
| Substrate availability | **High** — IG/Lloyd's/IUMI/club annual reports + JWC bulletins are publicly downloadable, CC-attribution clean | Medium — OSPAR + BSEE + IOGP reports are public, but DNV-OS-F211 is vendor-derivative (deny-listed per spinout governance); API-RP-17 series is API-licensed |
| Doctrinal coherence | **High** — MIA-1906 is a 120-year doctrinal trunk; P&I + Lloyd's + JWC are well-bounded sub-doctrines | High — OSPAR 98/3 + IMO 1989 + BSEE Subpart Q form a tri-jurisdiction trunk; sub-doctrines are well-bounded |
| Practitioner relevance | **High** — every shipowner, charterer, cargo interest, financier touches marine-insurance daily; aceengineer client base intersects | High — narrower — only operators in late-life production touch decommissioning, but those that do face $50M-$500M per-asset spend |
| Build cost estimate | ~25 pages × 1 iter = **1 iter at full scope** (10 standards + 10 concepts + 5 sources) | ~25 pages × 1.5 iter = **1.5 iter at full scope** (substrate harder to source CC-clean; vendor-derivative risk on DNV/API) |
| Vendor-derivative risk | **Low** — MIA-1906 is statute, IG/Lloyd's/clubs publish for marketing reasons, JWC is public | **Medium-high** — DNV-OS-F211 is paywalled; API RP 17 is API-licensed; OSPAR + BSEE + IOGP are clean but limited |
| Audit-trail / citation contract fit | **High** — insurance clauses are explicitly cited per case (calc-citation-contract pattern fits) | Medium — decommissioning citations are typically regulatory, not engineering-numeric; citation contract fits but with a different shape |

## Recommendation

**USER DECISION NEEDED.** The recommended primary path:

1. **iter-50: seed marine-insurance at full scope** — build the 10 + 10 + 5-7 substrate (~25-27 pages) in a single iter, leveraging the high cross-wiki bridge density (15 immediate bridges into maritime-law) to accelerate corpus integration. Marine-insurance has lower vendor-derivative risk, higher substrate availability, and stronger doctrinal coherence around the MIA-1906 trunk.
2. **iter-52+: defer offshore-decommissioning** — surface 2-3 substrate-fill iters first to land DNV-OS-F211 (or its public substitutes — IOGP 584, OG21, OSPAR 98/3) BEFORE attempting the full arc. The vendor-derivative issue around DNV/API is real and a premature seed will collide with the spinout governance deny-list (per llm-wiki/CLAUDE.md and project_llm_wiki_spunout memory).

**Alternative paths the user may prefer:**

- **A. Both arcs at reduced scope** — 5 + 5 + 3 substrate per arc, two arcs in parallel over iter-50 + iter-51. Trade-off: less cross-wiki bridge density per arc, more parallel-write coordination cost.
- **B. Defer both** — continue depth-expansion (iter-49 P2 pilot on api-rp-571 + environmental-liability + mechanical-fatigue) for 2-3 more iters to push average-page-depth from V11's measurement before opening any new arc.
- **C. Seed offshore-decommissioning first** — counter to the recommendation above; only justified if the user wants to drive the eng-stds expansion in advance of the eng-stds substrate-fill backlog being fully closed.

## Anti-recommendations

1. **Do NOT seed both arcs at full scope simultaneously.** ~50-page parallel write across two new top-level wiki trees breaches the per-iter sustainable-cadence ceiling V11 already flagged (V11 finding 5 — corpus has crossed absorption threshold). Expected outcome: cross-arc bridge confusion + sustained MAJOR cross-review findings.
2. **Do NOT conflate marine-insurance with maritime-law.** Marine-insurance gets its own top-level wiki (`wikis/marine-insurance/`), not a subdir under maritime-law. Doctrinal distinction: maritime-law is convention + statute + tort + contract layer; marine-insurance is contract + market layer. Conflating produces a 100+ page maritime-law wiki that double-counts every CLC/Bunkers/Nairobi page and fails the "one doctrine per wiki" principle.
3. **Do NOT seed offshore-decommissioning before DNV-OS-F211 substrate is sourced from a CC-clean alternative.** The spinout governance deny-list (vendor PDFs at private-vendor-mount, never in this repo) means a literal DNV-OS-F211 page citing the paywalled spec content is non-compliant. The clean substitute path is OSPAR 98/3 + IOGP 584 + OG21 first, with DNV-OS-F211 as a metadata-only stub citing publisher.
4. **Do NOT bake P&I club rule-changes into individual club pages.** Use the `p-and-i-rule-book-template` concept page as the lensed view; individual clubs become entity pages (or sources), not standards pages. The clubs are not standards-issuing bodies — they are mutual-insurance vehicles applying a common rule template.
5. **Do NOT cite Lloyd's, IG, JWC, or BSEE bulletins from a vendor-derivative deny-list page.** Per `.claude/rules/calc-citation-contract.md`, source pages cite the standards/concepts page; do not chain citations through `wiki/sources/`. Marine-insurance has high source-page density and could easily slip into double-citing.

## Hand-off

This brief is `status: user-decision-needed`. Awaiting user selection among (recommended, A, B, C) before iter-50 plan-phase opens. No commits. No writes outside `_audit/`.
