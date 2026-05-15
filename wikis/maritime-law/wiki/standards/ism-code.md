---
title: "ISM Code — International Safety Management Code"
slug: ism-code
tags: [ism, imo, safety-management, sms, solas-chapter-ix, mandatory-code, maritime-law, standards]
added: 2026-05-15
last_updated: 2026-05-15
domain: maritime-law
cross_links: []
--- standards-page extra fields (treaty-flavored; per maritime-law/CLAUDE.md schema) ---
code_id: ism-code
publisher: IMO
consolidated_edition: "ISM Code 2018 Consolidated Edition (IMO publication IB117E)"
amendment_status: "MSC continuous revision; recent: MSC.353(92) 2013 risk-assessment + audit cycle clarifications; MSC.476(102) 2019 Designated Person Ashore (DPA) competency"
instrument_type: code
jurisdiction: global (mandatory under SOLAS Ch. IX for SOLAS Contracting Governments)
effective_date: 1998-07-01
parent_instrument: "Made mandatory by SOLAS 1974 Chapter IX (added by 1994 Resolution MSC.99(73)); sister mandatory codes include ISPS Code, IGC Code, IBC Code, IGF Code"
sources:
  - https://www.imo.org/en/OurWork/HumanElement/Pages/ISMCode.aspx
extraction_policy: metadata-and-doctrinal-synthesis
raw_copy_allowed: false
public_url: https://www.imo.org/en/OurWork/HumanElement/Pages/ISMCode.aspx
publisher_catalog_url: https://www.imo.org/en/publications/Pages/Default.aspx
---

# ISM Code — Standards Routing Entry

## Scope

International Management Code for the Safe Operation of Ships and for Pollution Prevention — the IMO's mandatory framework requiring shipping companies and shipboard organisations to operate a documented **Safety Management System (SMS)**. Adopted by IMO Assembly Resolution A.741(18) (1993), made mandatory by SOLAS Chapter IX (added via Resolution MSC.99(73), 1994).

**Entry-into-force schedule (phased by ship type):**
- Phase 1 — 1 July 1998: passenger ships (incl. high-speed passenger craft), oil tankers, chemical tankers, gas carriers, bulk carriers, cargo high-speed craft ≥ 500 GT
- Phase 2 — 1 July 2002: other cargo ships and Mobile Offshore Drilling Units (MODUs) ≥ 500 GT

## Functional architecture

The Code is structured in **two parts**:

- **Part A — Implementation** (12 elements): general SMS objectives, company responsibilities, Designated Person Ashore (DPA) function, master's authority, resources & personnel, shipboard operations, emergency preparedness, reports/analysis of non-conformities, maintenance, documentation, company verification & review, certification & periodical verification.
- **Part B — Certification and Verification:** Document of Compliance (DOC) for the company + Safety Management Certificate (SMC) for each ship; flag-State or Recognized Organization audit cycle (initial → annual → renewal at 5-year intervals).

## Why this page is in `wiki/standards/`

ISM is a mandatory **code** (instrument_type=code) routed here per the maritime-law standards routing schema (sanctioned by [#15](https://github.com/vamseeachanta/llm-wiki/issues/15)), parallel to ISPS Code. The metadata-resolver companion to the concept page lets downstream tooling treat ISM as a citable instrument with stable `code_id` for the same calc-citation contract semantics used in engineering-standards wikis.

## Canonical concept treatment

Full structural treatment, doctrinal synthesis, case-law arc (Costa Concordia ISM/SMS failure cascade; *Erika* ISM-derived corporate liability), and ECDIS-era SMS evolution: [ISM Code (concept page)](../concepts/ism-code.md).

## Cross-references

- Parent treaty: [SOLAS 1974](solas-1974.md) — Chapter IX makes ISM mandatory
- Sister mandatory IMO codes: [ISPS Code](isps-code.md) (SOLAS Ch. XI-2), IGC Code (cross-wiki: [lng-projects/igc-code](../../../lng-projects/wiki/standards/igc-code.md))
- Crew-side companion treaty: [STCW Convention 1978/2010](stcw-convention.md) (competency framework feeding ISM personnel-resources element)
- Companion concepts: [Flag State Jurisdiction](../concepts/flag-state-jurisdiction.md) (DOC issuance authority), [Port State Control](../concepts/port-state-control.md) (PSC inspection of SMC), [Limitation of Liability](../concepts/limitation-of-liability.md) (ISM compliance affects break-of-limitation analyses)
- Landmark case: [[Costa Concordia 2012]](../entities/costa-concordia-2012.md) — ISM/SMS-failure cascade benchmark
