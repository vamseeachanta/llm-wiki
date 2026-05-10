---
title: "ISM Code — International Safety Management Code"
code_id: ism-code
publisher: IMO
consolidated_edition: "2018 (consolidated; rides on the SOLAS Ch. IX amendment chain)"
embedded_in: solas-1974
tags: [maritime-law, standards-tier, imo, ism, safety-management]
added: 2026-05-02
last_updated: 2026-05-09
sources:
  - maritime-liability-conventions
cross_links:
  - ./solas-1974.md
  - ./port-state-control.md
  - ./flag-state-jurisdiction.md
---

# ISM Code — International Safety Management Code

## Scope

The International Safety Management (ISM) Code is the IMO standard for the safe management and operation of ships and for pollution prevention. It is **not a free-standing convention**: ISM is given legal force by SOLAS Chapter IX, which makes the Code mandatory for most commercial vessels. **Entry into force**: 1 July 1998 (passenger ships, oil/chemical/gas tankers, bulk carriers, high-speed craft of 500 GT and above on international voyages); 1 July 2002 (other cargo ships and mobile offshore drilling units of 500 GT and above).

## Structure

- **Part A — Implementation**
  - **Element 1 — General** (objectives, definitions, application). Establishes the ISM objectives: safety at sea, prevention of human injury or loss of life, avoidance of damage to the environment and to property.
  - **Element 2 — Safety and environmental-protection policy.** The Company is required to establish, document, and implement an SEP policy at the corporate level, signed by top management and visibly cascaded to ship-level personnel.
  - **Element 3 — Company responsibilities and authority.** Defines "the Company" — the registered owner or any other organization or person (such as the bareboat charterer) who has assumed responsibility for operation. Identifying *which* legal entity is the Company is itself a recurring legal question, particularly in tonnage-tax and bareboat-charter structures.
  - **Element 4 — Designated Person(s) Ashore (DPA).** The DPA must have direct access to the highest level of management; the DPA is the bridge between shipboard personnel and shore-based decision-makers when ordinary chain-of-command escalation is insufficient. DPA accountability is the load-bearing institutional design of the ISM Code.
  - **Element 5 — Master's responsibility and authority.** The Master's overriding authority and discretion to take any decision necessary for safety and pollution prevention is preserved by the SMS, not subordinated to it. This is the legal-doctrine bridge to the historical [Master's Authority](./master-authority.md) tradition.
  - **Element 6 — Resources and personnel.** Manning, qualification, familiarisation, training, and language requirements; couples to the [STCW Convention](./stcw-1978.md) competency framework.
  - **Element 7 — Shipboard operations.** Procedures, plans, and instructions for key shipboard operations including navigation, cargo handling, mooring, machinery operation, and emergency response — the SMS surface where most port-state-control non-conformities originate.
  - **Element 8 — Emergency preparedness.** Programmes for drills, exercises, and identification of credible shipboard emergencies; expected to integrate with shore-side emergency response.
  - **Element 9 — Reports and analysis of non-conformities, accidents, and hazardous occurrences.** The corrective-action loop. The internal reporting culture this element establishes is the canonical leading indicator of SMS health and the locus of the "paper SMS vs. living SMS" distinction examined in repeated casualty investigations.
  - **Element 10 — Maintenance of ship and equipment.** Planned maintenance system (PMS), critical-equipment identification, and recordkeeping; the most-frequently-audited element in IACS UR Z17 audits.
  - **Element 11 — Documentation.** Document control: how the SMS itself is maintained, revised, and made available aboard.
  - **Element 12 — Company verification, review, and evaluation.** Internal audit programme, management review at the company level, and continual-improvement loop closure.
  - **Element 13 — Certification, verification, and control.** Cross-references the Part B issuance and verification mechanisms.
- **Part B — Certification and verification**
  - Document of Compliance (DOC) for the company
  - Safety Management Certificate (SMC) for the ship
  - Interim certification, audit, and form provisions

## Key Mechanisms

- **Safety Management System (SMS)** — the documented set of company and shipboard procedures required by Part A; subject to internal and external audit.
- **Designated Person Ashore (DPA)** — required link between company top management and shipboard personnel, with direct access to the highest level of management.
- **Document of Compliance (DOC)** issued to the company, **Safety Management Certificate (SMC)** issued to the ship — both required for trading.
- **Major non-conformity** — finding that requires immediate corrective action and may lead to suspension of certificates, port-state detention, or both.
- **Embedded-in-SOLAS coupling** — ISM amendments propagate via the SOLAS Chapter IX amendment chain, not via a stand-alone amendment procedure.

## DPA accountability framework

The Designated Person Ashore is the institutional pivot of the ISM Code. The DPA's required attributes and authorities — and their typical failure modes — are:

| Attribute | Requirement | Typical failure mode |
|---|---|---|
| Direct access to top management | Must report to highest level of management on ship-related safety matters; no intermediate filtering of escalation | Reporting channel routed through commercial / chartering management, diluting the safety-channel directness |
| Authority commensurate with responsibility | Sufficient organisational authority to ensure resources are made available for safety and pollution prevention | DPA designated but without budget or hiring authority — title without power |
| Continuous availability | Must be reachable by ship at all times, with deputy / alternate when primary is unavailable | Time-zone or vacation gaps where the SMS escalation channel is effectively offline |
| Independence from commercial pressure | Should not be in a role where charterparty or commercial-performance metrics override safety judgement | DPA role assigned as a part-time duty to a commercial manager whose KPIs reward turnaround speed |
| Adequate qualifications and training | Knowledge of relevant codes, the SMS, and the ships' technical envelope | Pro-forma DPA letter on file with no documented training or audit experience |

The DPA is not a regulator; the DPA is the institutional answer to the question "who has the authority and the channel to halt unsafe operation, regardless of commercial pressure?"

## Cybersecurity addendum integration

IMO MSC Resolution 428(98) (adopted 2017) and the supporting MSC-FAL.1/Circ.3 guidance require that cyber risks be addressed within the existing SMS framework, with full implementation expected from the first DOC annual verification after 1 January 2021. This integration is delivery-by-existing-mechanism rather than a new standalone code:

- Cyber-risk identification is folded into Element 1 (objectives) and Element 7 (shipboard operations) of the SMS.
- Cyber-incident response is folded into Element 8 (emergency preparedness).
- Cyber non-conformities and hazardous occurrences flow through Element 9 reporting.
- The DPA's accountability scope expands to include cyber-risk escalation.

For vessels with significant industrial-control / OT footprint — gas carriers, FPSOs, MODUs, cruise ships, large container ships — the cyber-SMS scope reaches into territory better served by formal risk-based methodology. This is the substantive content of the existing API RP 580 / RP 581 cross-wiki bridge (see below): the SMS records the management envelope; the engineering substrate (RBI for pressure equipment; IEC 62443 / NIST CSF for OT cyber) supplies what the SMS records.

## Case-law and casualty application

The ISM Code's audit-trail value is illustrated by the way major casualty investigations have repeatedly reached into the SMS to diagnose institutional failure rather than only crew error. Four reference cases — none restated here as primary source, all summarised at synthesis depth:

- **Costa Concordia (2012).** The Italian cruise-ship grounding investigation found shortcomings in the operator's SMS implementation around master-discretion procedures, voyage-planning deviations, and emergency-response training. Costa Concordia is cited in post-2012 ISM commentary as the case where Element 5 (Master's overriding authority) and Element 8 (emergency preparedness) collide: the SMS preserved the master's discretion, but the casualty showed that discretionary deviation outside SMS-sanctioned voyage planning was treated as routine. Auditors increasingly treat normalisation-of-deviation patterns in voyage logs as Element 9 / Element 12 audit findings.
- **Sewol (2014).** The South Korean RoRo-ferry capsizing produced criminal convictions against the operating company's senior management. Investigation findings spanning cargo-securing failures, ballast-water mismanagement, master-replacement-without-familiarisation, and corporate cost-cutting on stability assessments are now textbook examples of Elements 3, 5, 6, 7, and 10 failures cascading through a paper-only SMS. Sewol is cited as the case where SMS documentation existed but was not the actual operating practice — the canonical "SMS on the shelf" failure mode.
- **Wakashio (2020).** The Japanese-flagged bulk carrier grounded on the reef at Pointe d'Esny, Mauritius, with subsequent oil pollution. ISM findings centred on Element 7 (navigation procedures: deviation from passage plan to obtain mobile-phone signal proximate to coast), Element 8 (emergency preparedness in a sensitive coastal area), and Element 9 (whether crew concerns about the deviation were escalated). See `../entities/mv-wakashio-2020.md` for the entity-level case record.
- **Marine Electric (1983, historical).** The pre-ISM US-flag bulk carrier sinking off Virginia is the historical antecedent often cited in ISM-Code preamble teaching — the loss of 31 of 34 crew was traced to systematic falsification of inspection records and acceptance of a vessel known to be unfit for sea. The US Coast Guard reforms that followed Marine Electric prefigured the institutional logic that ISM later codified at IMO scale: there must be a documented, auditable system, and there must be accountable persons whose job is to make the system real.

## Cross-References

- **Parent convention**: [SOLAS 1974](./solas-1974.md) — Chapter IX is the legal anchor.
- **Standards-page metadata**: [standards/solas-1974](../standards/solas-1974.md) — parent convention metadata resolver; [standards/marpol-73-78](../standards/marpol-73-78.md) — sibling IMO instrument referenced by ISM Part A pollution-prevention objectives.
- **Companion conventions**: [STCW 1978](./stcw-1978.md) — the seafarer competency framework that supplies Element 6's manning-and-qualification substrate; [MLC 2006](./mlc-2006.md) — labour-rights regime whose hours-of-rest and crew-welfare provisions interact with Element 6 manning adequacy and Element 9 incident-reporting culture.
- **Doctrine pages**: [Port-State Control](./port-state-control.md), [Flag-State Jurisdiction](./flag-state-jurisdiction.md), [Master's Authority](./master-authority.md).
- **Cases**: see `../entities/mv-prestige-2002.md` and `../entities/mv-wakashio-2020.md` for ISM-implementation discussion.

## Major non-conformity vs. observation — audit-finding spectrum

ISM audit findings sit on a graded scale; the categorisation discipline matters because consequences (DOC suspension, port-state detention, insurance covenant impact) cascade differently:

| Finding class | Definition (synthesis) | Typical operator response window | Downstream consequence |
|---|---|---|---|
| Major non-conformity | An identifiable deviation that poses a serious threat to safety of personnel or ship, or a serious risk to the environment, that requires immediate corrective action; or where an objective evidence of lack of effective and systematic implementation of an ISM Code requirement is demonstrated | Immediate (often before ship sails) | DOC / SMC suspension; PSC detention; insurance / charterparty consequences |
| Non-conformity | Observed situation where objective evidence indicates the non-fulfilment of a specified requirement | Defined corrective-action window (typically 90 days) | Documented in audit record; recurrence escalates to major |
| Observation | A statement of fact made during a safety-management audit and substantiated by objective evidence | No mandatory close-out timeline | Trended over audit cycles; cluster patterns trigger management review |

The discipline that distinguishes a major non-conformity from a non-conformity is itself a leading indicator of audit-organisation health: an audit programme that systematically downgrades majors to non-conformities under commercial pressure is itself an Element 12 (verification, review, evaluation) failure.

## Cross-wiki bridges

- [API RP 580 — Risk-Based Inspection](../../../engineering-standards/wiki/standards/api-rp-580.md)
  (engineering-standards) — **bidirectional bridge**: ISM Code Part A's
  Safety Management System (SMS) imposes a risk-assessment obligation on
  operators (§1.2.2.2 — "establish safeguards against all identified
  risks"; §7 — shipboard-operations plans addressing safety-critical
  activities) but specifies no numeric methodology. For vessels carrying
  fixed pressure equipment within API RP 580's scope (FPSOs, gas
  carriers, MODUs, process-module-equipped offshore units), the RBI
  programme — qualitative POF × COF risk matrix per RP 580, optionally
  refined to quantitative damage-factor scoring per [API RP 581
  (engineering-standards)](../../../engineering-standards/wiki/standards/api-rp-581.md)
  — is the engineering-substrate that supplies the technical content
  the SMS records. Class-society implementation guidance (IACS UR Z17
  on ISM auditing, plus DNV / ABS / LR / BV / ClassNK class rules)
  treats the RP 580 / RP 581 stack as the conventional risk-assessment
  methodology for SMS pressure-equipment scope. The treaty regime
  delegates the engineering content; the SMS document records the
  management-system envelope around it.

## Citation Source

- IMO ISM Code portal: https://www.imo.org/en/OurWork/HumanElement/Pages/ISMCode.aspx
- Local corpus: `/mnt/ace/acma-codes/IMO/ISM/` (reference only — no extraction per #2482).
