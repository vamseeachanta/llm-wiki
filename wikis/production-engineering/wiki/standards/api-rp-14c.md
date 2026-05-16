---
title: "API RP 14C — Analysis, Design, Installation, and Testing of Safety Systems for Offshore Production Facilities"
code_id: api-rp-14c
publisher: American Petroleum Institute
revision: "8th edition, 2017 (Errata 1, 2018)"
jurisdiction: international
tags: [recommended-practice, api, safety-system, offshore, esd, sssv, choke-coordination, production-facility]
sources:
  - api-rp-14c
added: 2026-05-16
last_updated: 2026-05-16
---

# API RP 14C — Analysis, Design, Installation, and Testing of Safety Systems for Offshore Production Facilities

## Scope

API RP 14C is the practitioner-canonical recommended practice for **safety-system analysis, design, installation, and testing** on offshore oil and gas production facilities. The standard provides a structured methodology — built around the Safety Analysis Table (SAT) and Safety Analysis Function Evaluation (SAFE) chart — for identifying credible undesirable events on each process component, selecting the protective devices that defend against those events, and verifying that the resulting safety-system architecture meets the protective intent.

The 8th-edition (2017) title uses "Production Facilities" — distinct from older 6th/7th-edition phrasing ("Production Platforms") which the industry sometimes still echoes informally. The 2017 revision and its 2018 Errata 1 are the currently-active reference. The methodology has been the dominant offshore-safety-system framework since the 1970s and is incorporated by reference into US OCS regulations under 30 CFR 250 Subpart H.

This page is the **standards anchor** for choke-coordinated ESD logic and surface safety valve (SSV) coverage in the production-engineering wiki. Choke management cannot be discussed in isolation from the ESD interlocks that close around it; RP 14C defines that envelope.

## Why operators read it

- **Regulatory mandate** — incorporated by reference into US OCS regulations under 30 CFR 250 Subpart H. Comparable references exist in North Sea NORSOK, UK HSE, Australian NOPSEMA, and Brazilian ANP regimes.
- **Safety-system design basis** — operators specifying production-facility safety systems in completion-design AFEs, topsides front-end engineering and design (FEED) packages, and brownfield-modification AFEs cite RP 14C as the methodology basis.
- **Audit trail** — post-incident reviews of well-control or process-safety events use SAFE-chart records as first-line documentary evidence that protective devices were correctly specified and verified.
- **Choke-ESD coordination** — choke valves, surface safety valves, subsurface safety valves, wing valves, and master valves form a coordinated barrier hierarchy that RP 14C structures explicitly. Choke management decisions interact with the ESD logic that closes around the choke on overpressure, underpressure, or process-trip detection.

## Methodology (structural overview, paraphrased)

The exact section labels, threshold values, and SAT/SAFE-chart layouts have evolved across editions and are not transcribed here (paywalled standard); the structural intent is stable across the 6th, 7th, and 8th editions:

- **Safety Analysis Table (SAT)** — a per-component tabular analysis identifying credible undesirable events (overpressure, underpressure, flow-direction-reversal, leak, vessel-rupture, fire, etc.) and the primary and secondary protective devices that defend against each event. Components covered include separators, treaters, compressors, pumps, headers, pipelines, fired vessels, and the wellhead-and-choke section that connects them to the producing wells.
- **Safety Analysis Function Evaluation (SAFE) chart** — a matrix mapping protective devices to the events they detect, the components they protect, and the shutdown actions they initiate. The SAFE chart is the auditable artefact that demonstrates the safety system is internally consistent.
- **Shutdown hierarchy** — the standard structures shutdown actions in a layered hierarchy from local component isolation through process-section ESD through full-facility ESD through abandon-platform. Choke valves participate in the lowest layers (component-level flow control during process upsets) and the ESD valves around them participate in the higher layers (process-section and facility shutdown).
- **Acceptance testing** — periodic function testing of each protective device, with records demonstrating that each SAFE-chart entry has been verified within its specified test interval. The standard does not prescribe a single test interval but ties test frequency to device class and consequence severity.

## Choke and surface-safety-valve coverage

The wellhead-and-choke section of an offshore production facility is one of the most safety-critical components covered by RP 14C, sitting at the boundary between the producing well (subsurface safety valve envelope) and the topside process (separator and downstream-equipment envelope):

- **Surface safety valve (SSV)** — the primary topside well-control barrier, located on the production wing of the Christmas tree (subsea) or the production wing of the wellhead (surface). RP 14C requires SSVs to fail-safe-close on loss of control signal, overpressure detection downstream, and ESD actuation. The SSV is conceptually the topside counterpart to the subsurface safety valve covered by [API Spec 14A](api-spec-14a.md).
- **Choke valve as control element, not safety barrier** — the production choke is a flow-control device, not a safety barrier per RP 14C taxonomy. Its job is matching well deliverability to downstream process capacity, not isolating the well on emergency. The SSV (upstream of the choke) and the wing/master valves (further upstream on the tree) provide the safety barriers; the choke provides the operating-point control.
- **Coordinated ESD logic** — on facility ESD, the closure sequence is structured to avoid creating new hazards. Typical sequence: production choke biases toward closure first (reducing flow), SSV closes (isolating the topside from the well), wing valve closes (additional well-isolation), master valve closes (final tree-level isolation), and the subsurface safety valve closes (downhole well-isolation). RP 14C structures the logic that determines this sequence and the time gates between each step.
- **High/low pressure shutdown (PSHL) on the choke discharge** — RP 14C specifies PSHL sensors on the choke discharge line that initiate ESD on either overpressure (downstream blockage) or underpressure (loss of well or flow-line rupture). The PSHL setpoints relative to the operating envelope of the choke are part of the SAT/SAFE-chart design.

## Subsea production application

For subsea-tree applications, RP 14C principles apply at the host-facility level (FPSO, fixed platform, semi-submersible, spar) but interact with the subsea-production-control-system architecture covered by the **API RP 17F** standard (subsea production control systems) at the umbilical-to-host boundary. The handoff is:

- **Subsea-tree SSV and choke** — controlled via subsea production-control-system architecture (electric-hydraulic multiplex or all-electric), with host-facility ESD signals communicated via the umbilical.
- **Topside choke (often present in addition to the subsea choke)** — covered directly under RP 14C as a topside-process component.
- **Coordinated subsea-and-topside ESD** — both choke valves and both SSV layers (subsea-tree-SSV and topside-SSV) participate in a coordinated shutdown sequence designed at the host-facility integrated-control-and-safety-system (ICSS) level.

## Adjacent standards

- **API Spec 14A** — subsurface safety valve equipment specification (downhole well-isolation barrier, complementary to RP 14C's topside-and-wellhead scope). See [API Spec 14A](api-spec-14a.md).
- **API RP 17F** — subsea production control systems (defines the subsea-to-host architecture that carries RP 14C-derived ESD signals to subsea-tree SSVs and chokes).
- **API RP 14E** — Design and Installation of Offshore Production Platform Piping Systems (referenced for the erosional-velocity criterion that bounds choke discharge piping sizing and influences choke-selection economics). Cross-link to engineering-standards.
- **ISO 10417** — Petroleum and natural gas industries — Subsurface safety valve systems — Design, installation, operation, and redress (complementary international counterpart to API Spec 14A).
- **IEC 61508 / IEC 61511** — functional-safety standards (safety integrity level, SIL, methodology) that increasingly inform the protective-instrumented-system (PIS) layer of facility safety architecture; the SAFE chart can be enriched with SIL classifications per IEC 61511.
- **NACE MR0175 / ISO 15156** — sour-service material requirements applicable to choke trim, SSV trim, and tree-component metallurgy.

## Concept-page references

- [Choke Management](../concepts/choke-management.md) — router for choke-management coverage in the production-engineering wiki
- [Choke Types](../concepts/choke-types.md) — fixed-bore, adjustable, cage, and multistage choke architectures
- [Multiphase Choke Modeling](../concepts/multiphase-choke-modeling.md) — Sachdeva, Perkins, Ashford-Pierce framework
- [Choke Sand Erosion](../concepts/choke-sand-erosion.md) — erosion-rated choke selection under sand-laden duty

## Cross-references

- **Drilling-engineering** — [Casing Program Design](../../../drilling-engineering/wiki/concepts/casing-program-design.md) (production-casing burst rating sets the upper bound on the wellhead-and-choke section's design pressure that RP 14C analyses).
- **Vendor-archetype framing** — choke and SSV manufacturers (Master Flo, Mokveld, Cameron, Emerson, Baker Hughes, Schlumberger, and specialty independents) qualify equipment for RP 14C-compliant installations. Vendor-specific actuation hardware, choke-trim proprietary geometries, and ESD-controller proprietary firmware are concept-level only in this wiki — no proprietary content reproduced.

## Public references

- **API** — official publication page for API RP 14C (8th edition 2017, Errata 1 2018; current edition retrievable from api.org).
- **Arnold, K. & Stewart, M.** — *Surface Production Operations*, Volume 1 (Design of Oil Handling Systems and Facilities), 3rd ed., Gulf Professional Publishing (Elsevier), ISBN 978-0-7506-7853-7. Surface-facility safety-system chapters contextualise the engineering practice that RP 14C formalises.
- **Lyons, W. C. (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, Elsevier (ISBN 978-0-7506-7785-1). Production-operations chapters cover wellhead safety-system architecture.
- **SPE OnePetro safety-system literature** — extensive corpus on SAFE-chart methodology, SSV reliability, choke-coordinated ESD design, and offshore-platform safety-system retrofits.
- **30 CFR 250 Subpart H** (US BSEE offshore safety regulations) — incorporates RP 14C by reference and serves as the regulatory driver behind RP 14C adoption in US OCS operations.

## Notes

- API RP 14C has been issued in multiple editions since the 1970s. The 8th edition (2017) with Errata 1 (2018) is the currently-active reference; operators specifying safety-system designs in AFE / scope-of-work documents should pin to a specific edition.
- The 8th-edition title nomenclature change from "Offshore Production Platforms" (6th/7th editions) to "Offshore Production Facilities" reflects the modern scope expansion to cover FPSOs, semisubmersibles, spars, and other production-facility classes beyond fixed platforms.
- API RP 14C is paywalled. This wiki paraphrases the structural intent and references the standard for operators who already have a licensed copy. No verbatim text reproduced.
- The methodology is increasingly augmented by IEC 61511-based safety-integrity-level (SIL) analysis, which adds a probabilistic-failure-rate dimension to the deterministic SAT/SAFE-chart structure. Modern facility designs typically present both an RP 14C SAFE chart and an IEC 61511 SIL assignment in the same safety-design package.
