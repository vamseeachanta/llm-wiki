---
title: "ISPS Code — International Ship and Port Facility Security Code"
slug: isps-code
tags: [isps, maritime-security, post-911, solas-xi-2, port-facility-security-officer, ship-security-officer, cyber, sso, pfso, cso, maritime-law, standards, code]
added: 2026-05-09
last_updated: 2026-05-09
domain: maritime-law
# --- standards-page extra fields (per maritime-law/CLAUDE.md schema) ---
code_id: isps-code
publisher: IMO
consolidated_edition: "As adopted 2002 with 2014 amendments (cybersecurity)"
amendment_status: "MSC.94(72) 2002 adoption; MSC.428(98) 2017 cyber risk management interpretation"
instrument_type: code
jurisdiction: "global (mandatory under SOLAS XI-2)"
effective_date: 2004-07-01
parent_instrument: "SOLAS XI-2 (Special Measures to Enhance Maritime Security)"
sources:
  - https://www.imo.org/en/OurWork/Security/Pages/SOLAS-XI-2%20ISPS%20Code.aspx
extraction_policy: metadata-and-doctrinal-synthesis
raw_copy_allowed: false
---

# ISPS Code — International Ship and Port Facility Security Code

## Scope

Mandatory IMO Code (Part A) plus recommendations (Part B) for ship and port-facility security. Adopted post-9/11 to address the vulnerability of maritime transport to terrorism. Applies to: passenger ships, cargo ships of 500 GT and above on international voyages, mobile offshore drilling units (MODUs), and the port facilities serving them. The ISPS Code is not a treaty in itself — it operates under the **SOLAS Chapter XI-2** mandate ("Special Measures to Enhance Maritime Security"), which makes Part A binding on contracting governments.

This page is a metadata-and-doctrinal-synthesis resolver for `code_id: isps-code`. It is the citation target when a maritime-law concept page or downstream sibling calc cites ISPS by Part, Section, or Security Level. It is the standards-page companion to the existing [`concepts/ism-code.md`](../concepts/ism-code.md) sibling — ISM (SOLAS Ch. IX) and ISPS (SOLAS Ch. XI-2) are adjacent but distinct mandates: ISM governs **safety** management; ISPS governs **security** management.

## Adoption and entry-into-force

- **Adopted:** London, 2002-12-12, by the IMO Diplomatic Conference on Maritime Security (the "December 2002 SOLAS Conference"), via Resolution MSC.94(72) and the simultaneous adoption of new SOLAS Chapter XI-2.
- **Entry-into-force:** 2004-07-01 — a deliberately compressed 19-month implementation window reflecting the post-9/11 political urgency.
- **Coverage:** 160+ flag states and approximately 10,000+ port facilities certified under the regime as of 2024.
- **Parent mandate:** SOLAS Chapter XI-2 ("Special Measures to Enhance Maritime Security") — see the parent standards page at [[solas-1974]](./solas-1974.md).

## Three security levels

ISPS operates on a layered security-level framework set by the contracting government's **Designated Authority**; ships and port facilities must implement the protective measures appropriate to the level in force:

- **Security Level 1** (normal): the minimum appropriate protective measures shall be maintained at all times.
- **Security Level 2** (heightened): additional appropriate protective measures shall be maintained for a period of time as a result of heightened risk of a security incident.
- **Security Level 3** (exceptional): further specific protective measures shall be maintained for a limited period of time when a security incident is probable or imminent, although it may not be possible to identify the specific target.

Security-level changes are communicated by the Designated Authority to ships entitled to fly its flag and to port facilities operating in its territory.

## Key roles

- **CSO (Company Security Officer):** shore-based; responsible for company-wide ship security across the fleet. Accountable to senior management; oversees Ship Security Assessments and Ship Security Plans.
- **SSO (Ship Security Officer):** ship-board; accountable to the Master and to the CSO. Implements and maintains the approved Ship Security Plan (SSP) onboard; conducts security drills and reports security incidents.
- **PFSO (Port Facility Security Officer):** port-side; responsible for the development, implementation, and maintenance of the approved Port Facility Security Plan (PFSP).
- **Designated Authority:** the contracting government's competent authority for ISPS implementation — for example the **United States Coast Guard (USCG)** in the US (under 33 CFR 101–105) and the **Maritime and Coastguard Agency (MCA)** in the UK (under SI 2004/1495).

## Mandatory documents

- **Ship Security Plan (SSP):** approved by the flag-state administration (or by a Recognized Security Organization on its behalf); carried onboard. The SSP is a confidential document and is not open to inspection by port-state control beyond verification of existence and approval.
- **Port Facility Security Plan (PFSP):** approved by the Designated Authority; held at the port facility.
- **International Ship Security Certificate (ISSC):** issued post flag-state audit; renewable on a 5-year cycle with intermediate verification. The ISSC is the operational evidence verified by port-state control under SOLAS XI-2 Reg. 9.
- **Continuous Synopsis Record (CSR):** an onboard document recording the ship's history including ownership, registry, classification society, ISSC issuance, and security-related history. Mandated by SOLAS XI-1 Reg. 5 in the same 2002 reform package.

## Cybersecurity addendum

Per IMO Resolution **MSC.428(98)** (2017), maritime cyber-risk management is interpreted as forming part of the safety-management system (SMS) under the **ISM Code** and is also relevant to the security-management regime under the **ISPS Code**. The implementation deadline for shipping operators was the first annual verification of the company's Document of Compliance after **2021-01-01**.

The **NIST Cybersecurity Framework v1.1** has been widely adopted as the de-facto baseline for ISPS-cyber and ISM-cyber implementation, primarily through the *Guidelines on Cyber Security Onboard Ships* maintained by the **Joint Industry Cyber Risk Working Group** (BIMCO, CLIA, ICS, INTERCARGO, INTERTANKO, OCIMF, WSC, and others).

## Notable application

- **9/11 attacks 2001-09-11** — the proximate driver for ISPS Code adoption; the December 2002 SOLAS Conference was convened in direct response.
- **Mumbai 2008-11-26** — the terrorist attack on the Taj Hotel and other Mumbai targets was preceded by maritime infiltration via small boat, which drove a global tightening of ISPS port-facility security audit and small-craft monitoring expectations.
- **NotPetya 2017-06-27** — non-targeted destructive malware caused multi-week disruption to A.P. Moller-Maersk's IT systems and to ~80 affected ports, providing the political momentum behind the MSC.428(98) cybersecurity interpretation later that year.

## Cross-references

**Companion / sibling pages in maritime-law**

- [[ism-code]](../concepts/ism-code.md) — sibling SOLAS Ch. IX child (safety-management); ISPS sits adjacent under Ch. XI-2 (security-management). The two regimes are deliberately complementary: same audit cadence, distinct scope.
- [[solas-1974]](./solas-1974.md) — parent instrument; SOLAS Ch. XI-2 is the binding-mandate hook for ISPS.
- [[unclos-1982]](./unclos-1982.md) — UNCLOS Article 211(2) and Part XII source authority for flag-state security regulation that ISPS operationalizes.
- [[port-state-control]](../concepts/port-state-control.md) — the PSC regime verifies ISSC and security-related operational requirements under SOLAS XI-2 Reg. 9.

**Implementing national regulations**

- **US:** 33 CFR Parts 101–105 (USCG) implement ISPS for US-registered ships and US port facilities, including the Maritime Transportation Security Act (MTSA) overlay.
- **UK:** Statutory Instrument 2004/1495 — *The Ship and Port Facility (Security) Regulations 2004* (MCA) implements ISPS in UK law.
- **EU:** Regulation (EC) No 725/2004 on enhancing ship and port facility security; Directive 2005/65/EC on enhancing port security (the wider port-area overlay, beyond ISPS port facilities).

**Industry guidance (cybersecurity)**

- *Guidelines on Cyber Security Onboard Ships* — Joint Industry Cyber Risk Working Group (BIMCO, CLIA, ICS, INTERCARGO, INTERTANKO, OCIMF, WSC).
- **NIST Cybersecurity Framework v1.1** — widely adopted as ISPS-cyber and ISM-cyber implementation baseline.
- **IMO MSC-FAL.1/Circ.3/Rev.2** — *Guidelines on Maritime Cyber Risk Management* (companion guidance to MSC.428(98)).

## Sources

- IMO ISPS Code portal: <https://www.imo.org/en/OurWork/Security/Pages/SOLAS-XI-2%20ISPS%20Code.aspx>
- IMO Maritime Safety Committee Resolution MSC.94(72) (2002) — adoption of the ISPS Code.
- IMO Resolution MSC.428(98) (2017) — *Maritime Cyber Risk Management in Safety Management Systems*.
- IMO MSC-FAL.1/Circ.3/Rev.2 — *Guidelines on Maritime Cyber Risk Management*.
- [[solas-1974]](./solas-1974.md) — parent standards page.
- [[ism-code]](../concepts/ism-code.md) — sibling concept page (safety-management regime).
- [Calc citation contract](../../../../.claude/rules/calc-citation-contract.md) — downstream calcs citing a specific ISPS Part or Section should resolve `code_id: isps-code` against this page.
