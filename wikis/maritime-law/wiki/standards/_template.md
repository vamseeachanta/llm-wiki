<!--
  Template: maritime-law/wiki/standards/<code-id>.md
  --------------------------------------------------
  Use this template when authoring a NEW standards-page in the maritime-law
  wiki. Maritime-law instruments are TREATY-FLAVORED — they do not follow
  the linear publisher-revision regime of engineering standards. Frontmatter
  and body diverge accordingly (see W111 audit divergences from the
  lng-projects sibling template).

  AUTHORING RULES (non-negotiable):
    1. Public OSS repo (MIT + CC-BY-4.0). Treat all output as CC-BY-4.0 for
       prose and metadata only. Do NOT copy convention text, annexes,
       clauses, tables, or vendor/IMO-paywalled passages into the page.
       Cite the publisher catalog or the consolidated edition record.
    2. Frontmatter required fields: title, tags, added, last_updated, domain,
       code_id, publisher, instrument_type. `consolidated_edition` is required
       when the instrument has one (most IMO conventions do); `revision` is
       OMITTED — treaties amend by protocol/resolution, not by linear
       revision.
    3. `instrument_type` controlled vocabulary:
          - treaty                  (e.g. UNCLOS 1982)
          - protocol                (e.g. MARPOL Protocol of 1978)
          - code                    (e.g. ISM Code, IGC Code, Polar Code)
          - regulation              (e.g. EU MRV, USCG NVIC)
          - mou                     (e.g. Paris MoU on Port State Control)
          - private-codification    (e.g. CMI York-Antwerp Rules, BIMCO clauses)
          - case-law                (only when the page IS a doctrinal case
                                     digest used as a citable instrument)
    4. `amendment_status` records the most-recent IMO MEPC/MSC/Assembly
       resolution number (or analogue for non-IMO bodies). This is the
       maritime-law analogue of "edition pinning" but lives at resolution
       granularity, not edition granularity.
    5. Filename = lowercase-slug of code_id (e.g. `unclos-1982.md`,
       `marpol-73-78.md`, `mlc-2006.md`, `solas-1974.md`). Replace this
       file's name when copying.
    6. Bidirectional cross-references: any concepts/* or cases/* page you
       link MUST gain a return link in its own "Cross-references" section.
    7. Keep this template body as `_<author: ...>_` italic placeholders so
       future authors fill in the blanks. Do NOT pre-fill with a real
       instrument.

  CALC-CITATION CONTRACT (downgraded for maritime-law):
    Maritime-law citations are doctrinal — courts cite Articles, not
    numeric constants. This page's resolver role is to back DOCTRINAL
    citations (case-law, treaty-interpretation memoranda, compliance
    matrices), NOT numeric Citation instances under
    .claude/rules/calc-citation-contract.md. Engineering-standards Annexes
    that DO carry numeric constants (e.g. MARPOL Annex VI sulphur-cap
    figures consumed by emissions calcs) should be cited via the
    engineering-standards wiki page that mirrors the technical Annex, not
    via this maritime-law page.
-->

---
title: "<CODE-ID> — <Short instrument title>"
slug: <code-id-lowercase>
tags: ["<publisher-lowercase>", "standards", "maritime-law", "<instrument-type>"]
added: YYYY-MM-DD
last_updated: YYYY-MM-DD
domain: maritime-law
# --- maritime-law standards-page extra fields (treaty-flavored) ---
code_id: <code-id-lowercase>                  # e.g. unclos-1982, marpol-73-78, mlc-2006, solas-1974
publisher: <Publisher>                         # e.g. UN, IMO, ILO, CMI, BIMCO, USCG, EMSA
instrument_type: <treaty|protocol|code|regulation|mou|private-codification|case-law>
consolidated_edition: "<Consolidated YYYY>"   # e.g. "MARPOL Consolidated 2022"; omit if N/A
amendment_status: "<latest IMO/UN resolution>" # e.g. "MEPC.328(76)", "MSC.521(106)", "A.1155(32)"
jurisdiction: <global|flag-state|port-state|EU|US|regional-mou>
effective_date: YYYY-MM-DD                     # in-force date
# parent_instrument: <code-id-of-parent>       # optional, e.g. solas-1974 for igc-code
# supersedes: ["<prior-code-id>"]              # optional
# verified_on: YYYY-MM-DD                      # optional, when frontmatter last reconciled with publisher
sources:
  - <link-to-maritime-law-sources-page-or-future-promotion>
extraction_policy: metadata-and-doctrinal-synthesis
raw_copy_allowed: false
---

# <CODE-ID> — <Short instrument title>

## Scope

_<author: 1–2 paragraphs describing what the instrument covers and which
maritime-law regime it governs. Pick from: liability / pollution /
safety-of-life / labour / carriage-of-goods / collision / salvage /
limitation / port-state-control / flag-state / dispute-resolution. Bound
the page as metadata + doctrinal synthesis; do not paraphrase Article
text or reproduce Annex tables. End with the consolidated edition the
page is pinned to and the amendment-status resolution.>_

## Adoption + entry-into-force

_<author: capture the treaty timeline:
  - Adoption date and forum (e.g. "Adopted at IMO Diplomatic Conference,
    London, 17 Feb 1978")
  - Adoption resolution number (e.g. IMO Resolution A.NNN(NN))
  - Entry-into-force date and the threshold that triggered it
    (e.g. "in force 2 Oct 1983, on ratification by 15 States representing
    not less than 50% of world merchant shipping tonnage")
  - Current ratification count and tonnage coverage if publicly known
  - For non-treaty instruments (codes, MoUs, private codifications):
    record the equivalent adoption/effective-date facts and the
    governing-body resolution.>_

## Amendment history

_<author: chronological table of amendment protocols and resolutions.
This replaces the engineering-standards "Edition history" — treaties
do not have linear editions, they accrete amendments. List the
material amendments only; full administrative tweaks belong on the
publisher's own page. Cite each row to its IMO/UN resolution number.>_

| Amendment / protocol | Year adopted | Year in force | Summary |
|----------------------|--------------|----------------|---------|
| _<e.g. Protocol of 1978>_       | YYYY | YYYY | _<one-line scope>_ |
| _<e.g. Annex VI, MEPC.176(58)>_ | YYYY | YYYY | _<one-line scope>_ |
| _<e.g. MEPC.328(76)>_           | YYYY | YYYY | _<one-line scope>_ |
| _<...>_                          | YYYY | YYYY | _<...>_ |

## Key Articles / Annexes / Regulations

_<author: bullet outline of the most-cited Articles, Annexes, Parts,
or Regulations. Title-only — no clause text. The shape varies by
instrument:
  - Treaties → Articles (e.g. UNCLOS Art. 87, Art. 211)
  - IMO conventions with Annexes → Annexes (e.g. MARPOL Annex I–VI)
  - Codes → Chapters / Regulations (e.g. ISM Code Part A, IGC Code Ch. 5)
  - Private codifications → Rules (e.g. York-Antwerp Rule VI)
Aim for 5–12 bullets.>_

- _<e.g. Article 87 — Freedom of the high seas>_
- _<e.g. Annex I — Regulations for the prevention of pollution by oil>_
- _<e.g. Regulation 13 — NOx emissions>_
- _<...>_

## Case law citing this instrument

_<author: list 3–5 representative cases that interpret or apply this
instrument. Provide neutral citation, jurisdiction, and a one-line
holding. If the maritime-law/wiki/cases/ directory carries a digest
page for the case, cross-link it; if not, list the case here as a
future-cases-page stub. Prefer canonical leading cases over recent
or jurisdiction-narrow ones unless the instrument is itself recent.>_

- _<e.g. The "Erika" — Cour de cassation (FR), 2012 — confirmed pollution
  liability under MARPOL/CLC framework>_ ([[cases/erika-2012]](../cases/erika-2012.md))
- _<e.g. M/V "Saiga" (No. 2) — ITLOS, 1999 — UNCLOS bunkering and hot
  pursuit>_
- _<e.g. The "Prestige" — multiple jurisdictions, 2002–2018 — CLC/Fund
  Convention compensation>_
- _<...>_

## Cross-references

_<author: bidirectional links. Any concepts/* or cases/* page linked
here MUST get a return link in its own Cross-references section.>_

**Parent instrument** _(if this page is a code or annex under a parent treaty)_
- _<e.g. [[solas-1974]](./solas-1974.md) — IGC Code is mandatory under SOLAS Ch. VII>_

**Sibling protocols + amendments** _(other instruments in the same family)_
- _<e.g. [[marpol-73-78]](./marpol-73-78.md) and its six Annexes>_
- _<e.g. CLC 1969 / CLC 1992 / Fund Convention 1992 / Supplementary Fund 2003>_

**Implementing-regulation national codes**
- _<e.g. US: 33 CFR / 46 CFR sections implementing this instrument>_
- _<e.g. EU: Directive 2005/35/EC (ship-source pollution) — MARPOL implementation>_
- _<e.g. UK: Merchant Shipping Act 1995, Part VI>_

**maritime-law concepts** _(populate as concepts/* pages land)_
- _<e.g. [[liability-channeling]](../concepts/liability-channeling.md)>_
- _<e.g. [[port-state-control]](../concepts/port-state-control.md)>_
- _<e.g. [[flag-state-jurisdiction]](../concepts/flag-state-jurisdiction.md)>_

**maritime-law cases** _(see "Case law citing this instrument" above; mirror those links here for index hygiene)_

**Cross-wiki (engineering-standards)** _(only when a technical Annex carries numeric constants used by calcs)_
- _<e.g. MARPOL Annex VI Reg. 14 sulphur-cap figures → engineering-standards page on emissions limits>_
- _<e.g. SOLAS Ch. II-1 subdivision/damage-stability → engineering-standards page on ship stability>_

**Cross-wiki (lng-projects)** _(when the instrument governs LNG carriage or terminals)_
- _<e.g. [[igc-code]](../../../lng-projects/wiki/standards/igc-code.md) — gas-carrier construction under SOLAS Ch. VII>_

## Sources

_<author: link the maritime-law sources/ catalog page summarizing the
publisher catalog or the consolidated-edition record. If no sources/
page exists yet, file a future-promotion stub here and create the
sources/ page when the IMO/UN/ILO catalog ingest reaches this
instrument.>_

- _<e.g. [[maritime-law-sources-marpol]](../sources/<slug>.md) — sources/* catalog summary>_
- Publisher catalog: _<public_url>_
- Consolidated edition record: _<publisher catalog entry for `consolidated_edition`>_
- Latest amendment resolution: _<IMO Documents portal entry for `amendment_status`>_
