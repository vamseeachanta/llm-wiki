---
title: "10 Landmark Maritime Law Cases (1967-2021)"
source_file: "maritime-law-cases.yaml"
sources:
  - knowledge/seeds/maritime-law-cases.yaml
added: 2026-04-07
last_updated: 2026-05-09
tags: [maritime-law, cases, oil-spill, liability, precedent, source-page]
---

# 10 Landmark Maritime Law Cases (1967-2021)

Seed migration from `knowledge/seeds/maritime-law-cases.yaml`. Ten cases spanning foundational pollution liability (Torrey Canyon, 1967) through modern container ship and bulk carrier incidents (Wakashio 2020, Ever Given 2021). Each entry surfaces (i) the operational casualty, (ii) the litigation outcome, and (iii) the doctrinal precedent.

## Summary Table

| Case | Year | Location | Spill Volume | Key Legal Precedent |
|------|------|----------|-------------|---------------------|
| Torrey Canyon | 1967 | UK | 119,000 t | Triggered CLC 1969 / IOPC Funds |
| Amoco Cadiz | 1978 | France | 223,000 t | $85M trans-boundary damages, US 7th Circuit |
| Sea Empress | 1996 | Wales | 72,000 t | Port authority criminal liability |
| Erika | 1999 | France | 20,000 t | Corporate criminal liability (Total SA) |
| Prestige | 2002 | Spain | 77,000 t | Flag-state liability limits, EU 3rd safety package |
| Eurasian Dream | 2002 | UK | N/A | Carrier identity under Hague-Visby |
| Deepwater Horizon | 2010 | US | ~780,000 m³ | Gross negligence cap-loss, OPA 90 unlimited |
| MSC Flaminia | 2012 | US/Germany | N/A | Shipper dangerous cargo liability |
| Wakashio | 2020 | Mauritius | 1,000 t | MARPOL + crew welfare + reef damage |
| Ever Given | 2021 | Egypt | N/A | Canal blockage, general average, salvage award |

## Pattern: Evolution of Liability

1. **1967–1978 — Strict liability and compensation funds.** The Torrey Canyon (1967) prompted CLC 1969 and the Fund Convention 1971; Amoco Cadiz (1978) demonstrated that even with the CLC framework, claims against US-resident parents could yield trans-boundary damages above the international cap.
2. **1996–2002 — Corporate and port-authority criminal liability.** Sea Empress (1996) imposed criminal liability on Milford Haven Port Authority; Erika (1999) extended criminal pollution liability up the contractual chain to the charterer (Total SA, French Cour de cassation 2012).
3. **2010 onwards — Unlimited gross-negligence liability.** Deepwater Horizon (2010) operationalized OPA 90 §2704(c) cap-loss against an oil major and produced aggregate exposure of ~US$65 billion; MSC Flaminia (2012) extended dangerous-cargo-shipper liability under Hague-Visby Rule IV(6).
4. **2020s — Multi-defendant apportionment and reef-damage doctrine.** Wakashio (2020) brought MARPOL Annex I liability, crew-welfare prosecutions, and coral-reef ecosystem-damage claims into a single coordinated proceeding; Ever Given (2021) folded a Suez detention claim, salvage award, and a multi-jurisdictional limitation-fund constitution into a single global litigation.

## How to use this source

This source is the **case-side index** for the maritime-law wiki. It is the entry point when you have a casualty (a name, a year, a flag, or a spill volume) and need to walk to:

- The **entity page** (`wiki/entities/<case-slug>-<year>.md`) — operational facts of the casualty, including parties, dates, vessel particulars, and the litigation timeline.
- The **concept page** (`wiki/concepts/<doctrine>.md`) — the doctrinal synthesis the case helped establish or test.
- The **standards page** (`wiki/standards/<convention>.md`) — the convention or domestic statute the case interprets.

**Practitioner usage**: a research path on a candidate casualty typically runs *summary table → entity page → concept page(s) for the doctrines tested → standards page for the controlling instrument*. The summary table is the index, not the destination.

## Coverage scope

**In scope**:
- Major pollution casualties (Torrey Canyon, Amoco Cadiz, Sea Empress, Erika, Prestige, Deepwater Horizon, Wakashio).
- Container-ship and bulk-carrier incidents that produced doctrinal precedent (MSC Flaminia, Ever Given).
- Cases that tested core liability conventions (CLC 1969/1992, Hague-Visby Rules, OPA 90, LLMC 1996, MARPOL 73/78, Salvage 1989).
- Cases through 2021.

**Not in scope** (deferred to future expansion):
- Pre-1967 historical cases (Lex Rhodia, Oléron, mediaeval admiralty); see [`concepts/general-average.md`](../concepts/general-average.md) for the doctrinal trail.
- Salvage and wreck-removal arbitrations published only by the Lloyd's Salvage Arbitration Branch (Tojo Maru, Nagasaki Spirit, Stena Polaris); cited inline in [`concepts/salvage.md`](../concepts/salvage.md) but not separately indexed here.
- LLMC limitation-of-liability cap-break cases (The Marion, The Western Neptune, The Bowbelle); cited inline in [`concepts/llmc-1996.md`](../concepts/llmc-1996.md).
- ITLOS prompt-release jurisprudence (M/V Saiga 1+2, Camouco, Monte Confurco, Grand Prince, Volga); cited inline in [`concepts/flag-state-jurisdiction.md`](../concepts/flag-state-jurisdiction.md).
- Post-2021 casualties (X-Press Pearl 2021, FSO Safer 2023, MV Genco Picardy 2024, MV Dali / Francis Scott Key Bridge 2024) — pending entity-page authorship.

## Cross-wiki citation guidance

Cite this source page when:

- A page in a sibling wiki (marine-engineering, naval-architecture, ocean-engineering) references a maritime casualty for engineering-causation or design-lesson purposes and the maritime-law context is incidental rather than primary. Example: a fatigue-failure analysis citing Erika's hull-girder failure should link here for the legal-context companion.
- A skill or rule needs a single canonical maritime-law-cases pointer rather than a list of individual entity pages.
- A standards-tier page (in `wiki/standards/`) needs to direct the reader to "the cases that have tested this instrument" without enumerating each.

**Do NOT cite this source** when the linking page is itself doctrinal-tier (concept or standards) and is *making* a case-specific argument — those pages should cite the entity page directly.

## Updates + maintenance

- **Source seed**: `knowledge/seeds/maritime-law-cases.yaml` (workspace-hub canonical seed, immutable).
- **Last seed migration**: 2026-04-07.
- **Last reviewer pass**: 2026-05-09 (W171 deepening pass — added "How to use" / "Coverage scope" / "Cross-wiki citation guidance" / this maintenance section).
- **Expansion cadence**: New entity pages added under `wiki/entities/` are referenced inline from this index. The summary table is updated only when a new case enters the canonical-seed list (i.e. promoted from the in-flight backlog to the durable corpus).
- **Backlog candidates** (next seed-update window): X-Press Pearl 2021 (Sri Lanka, plastic-pellet pollution), FSO Safer 2023 (Yemen, abandoned-tanker preventive-salvage), MV Dali 2024 (Baltimore, Francis Scott Key Bridge allision and OPA 90 / state-law layered claims).
