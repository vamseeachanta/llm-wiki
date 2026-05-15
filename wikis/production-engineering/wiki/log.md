# Wiki Log: Production Engineering

> Founded 2026-05-13 as the 10th llm-wiki domain. Founding-trigger anchor: scope-edge note on [drilling-engineering/concepts/artificial-lift-method-selection.md](../../drilling-engineering/wiki/concepts/artificial-lift-method-selection.md). This log records all ingests, structural changes, and lint passes for this wiki.

---

## [2026-05-14] ingest | PE Phase 1 sub-issue #64 — PCP (API Spec 11W + progressing-cavity-pumps + elastomer chemistry + heavy-oil application)
- Processed: API Spec 11W (PCP systems specification). Textbook synthesis from Brown 1980 *Technology of Artificial Lift Methods* Vol 2b, Lyons handbook artificial-lift section, SPE OnePetro PCP literature.
- Pages created: standards/api-spec-11w.md, concepts/progressing-cavity-pumps.md, concepts/pcp-elastomer-chemistry.md, concepts/pcp-heavy-oil-application.md.
- Pages updated: wiki/index.md (page_count 17 → 21; +3 Concepts rows, +1 Standards row).
- Closes: vamseeachanta/llm-wiki#64 (PE Phase 1 sub-issue, parent epic #61).
- Notes: Two configurations captured (surface-driven + ESPCP). Elastomer family framework (NBR / HNBR / FKM / EPDM) with fluid-compatibility logic + 4 failure-mode catalog (swelling / hardening / softening / chunking). Heavy-oil application chapter covers Western Canada, Venezuelan Faja, California (Kern River etc.), Colombia/Brazil. Cold-flow vs thermal (SAGD / CSI) distinguished. No vendor proprietary content transcribed.

## [2026-05-14] ingest | PE Phase 1 sub-issue #63 — gas lift (API RP 11V6 + RP 11V2 + Spec 11V1 + gas-lift concept cluster)
- Processed: API RP 11V6 (design), RP 11V2 (valve performance testing), Spec 11V1 (valve specification). Textbook synthesis from Takacs 2005 *Gas Lift Manual* (ISBN 0-87814-805-1), Brown 1977 *Technology of Artificial Lift Methods* Vol 1.
- Pages created: standards/api-rp-11v6.md, standards/api-rp-11v2.md, standards/api-spec-11v1.md, concepts/gas-lift-overview.md, concepts/gas-lift-valve-design.md, concepts/gas-lift-valve-spacing.md, concepts/gas-lift-troubleshooting.md.
- Pages updated: wiki/index.md (page_count 10 → 17; +4 Concepts rows, +3 Standards rows).
- Closes: vamseeachanta/llm-wiki#63 (PE Phase 1 sub-issue, parent epic #61).
- Notes: Continuous-flow vs intermittent modes captured. IPO vs PPO valve actuation + bellows vs spring force source distinguished. Brown-Camp graphical valve-spacing method named + modern computational methods (ValCalc / PerformLink / WellCare). Troubleshooting catalog: multipointing, heading, valve failures (stuck-open / stuck-closed / seat-leak), surface-pressure instability. No vendor/proprietary content transcribed.

## [2026-05-13] domain-founding | production-engineering wiki founded with artificial-lift-overview as founding concept anchor
- Processed: structural founding of 10th llm-wiki domain. Trigger event: scope-edge note on drilling-engineering's `artificial-lift-method-selection.md` explicitly anticipated this domain founding ("if/when a future production-engineering wiki domain is founded, this page should re-route there with rod-pump kept as the cross-link back to drilling-engineering"). User signal: "continue with next session candidates" in conversation following Phase 2 close-out 2026-05-13.
- Pages created: CLAUDE.md (schema), wiki/overview.md, wiki/index.md, wiki/log.md, concepts/artificial-lift-overview.md.
- Structural decisions: new top-level `wikis/production-engineering/` mirrors the established domain layout (acma-projects / asset-management / drilling-engineering / engineering / engineering-standards / lng-projects / marine-engineering / maritime-law / naval-architecture). Cross-wiki linkage declared in CLAUDE.md and overview.md: drilling-engineering (well-construction handover, founding-trigger anchor), naval-architecture (FPSO host platforms), marine-engineering (offshore-marine production operations), engineering-standards (API 11/14/17 series), asset-management (well-integrity-during-production overlap).
- V18 anti-rec #8 override: corpus-freeze cron-only mode broken under explicit user signal (the same explicit-signal logic that authorized drilling-engineering founding earlier same day). V19 audit (calendared 2026-06-09) should treat production-engineering as the 10th authorized domain, alongside drilling-engineering as the 9th.
- Notes: No external LinkedIn-post trigger like drilling-engineering's Papkov founding — the trigger is internal cross-wiki structural completeness (the scope-edge note that drilling-engineering deliberately left open). Founding concept anchor `artificial-lift-overview.md` is the production-engineering-side counterpart to drilling-engineering's `artificial-lift-method-selection.md`; together they form the bidirectional cross-link. Rod-pump deep coverage stays in drilling-engineering per API "drilling and well servicing" umbrella; production-engineering inherits the other 4 lift methods plus completions, stimulation, production operations, well-integrity-during-production. Seed roadmap (Phase 1-4) captured in overview.md as scope intent.

## [2026-05-14] ingest | PE Phase 1 sub-issue #62 — ESP (API RP 11S family + electric-submersible-pumps concepts) [INDEX/LOG FIXUP for log only]
- Processed: API RP 11S/11S1/11S2/11S4/11S7 + textbook synthesis from Takacs 2017 *Electrical Submersible Pumps Manual* (ISBN 978-0-12-814570-8), Brown 1980 *Technology of Artificial Lift Methods* Vol 2b, Lyons handbook.
- Pages created in commit `a4f981a6`: 5 standards (RP 11S/11S1/11S2/11S4/11S7) + 4 concepts (electric-submersible-pumps, esp-sizing, esp-failure-modes, esp-vendor-archetypes).
- Pages updated in commit `a4f981a6`: wiki/index.md (page_count 1 → 10). log.md was missed due to Edit-freshness window expiring (same pattern as DE Phase 2 fixups). This fixup adds the log entry.
- Closes vamseeachanta/llm-wiki#62 (auto-closed by Closes #62 trailer in commit a4f981a6).
- Notes: System-anatomy approach (motor → seal → intake → pump stages → head → cable → VFD), 6-step sizing workflow per RP 11S4, 5-category failure-mode catalog (cable/motor/pump/seal/gas-handling) with VFD telemetry signatures. Vendors named (Schlumberger REDA, Baker Hughes Centrilift, Borets) without proprietary content. Cross-link to drilling-engineering rod-pump cluster preserves the bidirectional cross-link.
