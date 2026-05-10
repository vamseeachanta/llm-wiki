---
title: "6 International Maritime Liability Conventions"
source_file: "maritime-liabilities.yaml"
sources:
  - knowledge/seeds/maritime-liabilities.yaml
added: 2026-04-07
last_updated: 2026-05-09
tags: [maritime-law, conventions, liability, compensation, international-law, source-page]
---

# 6 International Maritime Liability Conventions

Seed migration from `knowledge/seeds/maritime-liabilities.yaml`. Six instruments that together constitute the international and US-domestic surface for maritime liability and compensation: tanker-oil pollution, non-tanker bunker pollution, hazardous and noxious substances, passenger personal-injury, the global aggregate cap, and the US carve-out.

## Summary Table

| Convention | Year | Scope | Key Feature |
|-----------|------|-------|-------------|
| CLC | 1992 (Protocol) | Oil tanker spills | Strict liability, compulsory insurance, ~SDR 89.77M cap, IOPC-Funds layered |
| Bunkers Convention | 2001 | Bunker fuel spills | Non-tanker pollution liability; defers cap to LLMC |
| HNS Convention | 2010 (Protocol) | Hazardous and noxious substances | Tanker + non-tanker HNS; supplemental fund; not yet in force |
| Athens Convention | 2002 (Protocol) | Passenger death/injury | Compulsory insurance, EU Reg 392/2009 |
| LLMC | 1976 / 1996 Protocol / 2012 + 2018 Amendments | General maritime claims | Tonnage-banded SDR cap; cap-break under Article 4 |
| OPA 90 | 1990 | US navigable waters + EEZ | Strict liability, COFR financial-responsibility, §2704(c) cap-loss for gross negligence / regulatory violation |

## Pattern: Layered Liability Architecture

The six instruments form a **layered architecture**, not a flat list:

1. **Subject-matter regimes** (CLC for tanker oil, Bunkers for non-tanker oil, HNS for noxious substances, Athens for passenger personal-injury) carry their own scope, cap, and compulsory-insurance evidence (CLC blue card, Bunkers blue card, HNS blue card, Athens blue card).
2. **The aggregate ceiling** (LLMC 1996 Protocol with 2012 and 2018 Amendments) operates as the residual / outer cap on everything not channelled to a subject-matter regime, and in some opt-in jurisdictions on wreck removal under Nairobi WRC 2007.
3. **The US carve-out** (OPA 90) is the domestic substitute for the international layer in US navigable waters — broader cap-loss gateway, COFR financial-responsibility evidence, and OSLTF compensation fund replace the international CLC-Bunkers-IOPC architecture.
4. **The non-liability instruments that condition liability** (UNCLOS for jurisdiction, MARPOL for the underlying substantive standards, SOLAS / ISM / ISPS / MLC / STCW for the operational standards whose breach can drive cap-loss findings) are not in this list but are inseparable from it in practice.

## How to use this source

This source page is the **conventions-side index** for the maritime-law wiki. It is the entry point when you have a regime question (a treaty name, a year, a country's ratification status) and need to walk to:

- The **standards page** (`wiki/standards/<code-id>.md`) — public-metadata resolver for the instrument: adoption date, entry-into-force, consolidated-edition, and stable identifiers.
- The **concept page** (`wiki/concepts/<code-id>.md`) — practitioner-impact synthesis: what the instrument means for shipowners, P&I clubs, claimants, courts, and arbitrators.
- The **case index** at [`sources/maritime-law-cases.md`](./maritime-law-cases.md) — landmark casualties that have tested the instrument.

**Practitioner usage**: a research path on a candidate regime typically runs *summary table → standards page → concept page → cases that have tested the instrument*. Where multi-regime layering is in play (e.g. tanker spill engaging CLC plus collision claims engaging LLMC), the analytical path runs through both regime concept pages and into [`concepts/limitation-of-liability.md`](../concepts/limitation-of-liability.md) for the cross-regime layering doctrine.

## Coverage scope

**In scope**:
- The six core liability and compensation instruments enumerated above.
- The amendment / protocol structure that brings each instrument up to its current operating edition (CLC 1969 → 1976 Protocol → 1992 Protocol → 2000 limit increases; LLMC 1976 → 1996 Protocol → 2012 Amendments → 2018 Amendments; HNS 1996 → 2010 Protocol; Athens 1974 → 2002 Protocol).
- Domestic carve-outs that are recognized first-class regimes: OPA 90 in this source; EU Regulation 392/2009 (Athens-equivalent) is referenced inline in [`concepts/athens-convention-2002.md`](../concepts/athens-convention-2002.md) but not separately indexed.

**Not in scope** (deferred to future expansion):
- Operational instruments (SOLAS, MARPOL, MLC, STCW, COLREG, ISM, ISPS) — indexed separately under [`wiki/standards/`](../standards/) since they govern operational standards rather than liability quantum.
- The 1957 Brussels limitation convention — superseded by LLMC 1976 between states-parties; cited inline in [`concepts/llmc-1996.md`](../concepts/llmc-1996.md) for doctrinal-evolution context.
- Nuclear-liability conventions (1962 Brussels, 1971 Brussels) — separate regime, separate insurance market, deferred.
- Wreck-removal liability (Nairobi WRC 2007) — closely related to LLMC's Article 18(1) opt-in but indexed under operational instruments rather than this liability index.
- Salvage Convention 1989 — operates on the property-rescue surface rather than as a liability instrument; indexed separately.

## Cross-wiki citation guidance

Cite this source page when:

- A page in a sibling wiki (marine-engineering, naval-architecture, ocean-engineering, or insurance / commercial) needs a single canonical pointer to "the international maritime-liability convention surface" rather than to one specific instrument.
- A skill or rule needs to direct the reader to the conventions-index without enumerating each instrument.
- A page in a downstream commercial-practice context (charterparty drafting, P&I cover analysis, COFR/blue-card evidence) needs a unified entry point covering the international + US-domestic surfaces together.

**Do NOT cite this source** when the linking page is itself doctrinal-tier (concept or standards) and is *making* an instrument-specific argument — those pages should cite the standards page or concept page directly. The source page is for *navigation*, not for doctrine.

## Updates + maintenance

- **Source seed**: `knowledge/seeds/maritime-liabilities.yaml` (workspace-hub canonical seed, immutable).
- **Last seed migration**: 2026-04-07.
- **Last reviewer pass**: 2026-05-09 (W171 deepening pass — added "How to use" / "Coverage scope" / "Cross-wiki citation guidance" / this maintenance section).
- **Amendment-tracking notes**:
  - **CLC 1992** — limit increases adopted 2000, in force 1 November 2003 (cap raised to ~SDR 89.77M for the largest tankers); supplemental fund layer at IOPC Funds (1992 Fund + Supplementary Fund 2003).
  - **Bunkers Convention 2001** — in force 21 November 2008; aggregate ceiling defers to LLMC where the state-of-jurisdiction is an LLMC party.
  - **HNS Convention** — 1996 original never entered into force; 2010 Protocol designed to fix the financial-contribution mechanic; **not yet in force** as of 2026 — ratification trajectory tracked in IMO Legal Committee record.
  - **Athens Convention 2002** — Protocol in force 23 April 2014; EU Member States operationalize via Regulation 392/2009 since 31 December 2012.
  - **LLMC 1996 Protocol** — in force 13 May 2004; **2012 Amendments** in force 8 June 2015 (~51 % limit uplift); **2018 Amendments** subject to tacit-acceptance ratification trajectory.
  - **OPA 90** — Coast Guard 33 CFR Part 138 inflation-adjustment Final Rule cycle (most recent 2019); §2704 dollar values are CFR-current, not statute-text-current.
- **Expansion cadence**: New protocols, amendments, or limit increases are reflected by updating the relevant standards page (`wiki/standards/<code-id>.md`) and concept page (`wiki/concepts/<code-id>.md`) first; this index is updated when the seed YAML changes or when the layered-architecture overview needs a structural revision.
