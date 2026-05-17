---
title: "ISA-95 — Enterprise-Control System Integration"
code_id: isa-95
publisher: "International Society of Automation (ISA) + IEC 62264 joint"
revision: "Multi-part standard. Part 1 ANSI/ISA-95.00.01-2025 (IEC 62264-1 Mod); Part 2 ANSI/ISA-95.00.02-2018; Part 3 ANSI/ISA-95.00.03-2013 (IEC 62264-3 Mod); Part 4 ANSI/ISA-95.00.04-2018; Part 5 ANSI/ISA-95.00.05-2018; Part 6 ANSI/ISA-95.00.06-2014; Part 7 ANSI/ISA-95.00.07-2017; Part 8 ANSI/ISA-95.00.08-2020. Verified against ISA standards catalog (isa.org) 2026-05-16. Confidence: HIGH. Operators should pin to specific part-and-revision in project specifications."
jurisdiction: international
tags: [isa-standard, iec-standard, enterprise-control, manufacturing-operations-management, level-hierarchy, scada-architecture, mes-integration]
sources:
  - isa-95
added: 2026-05-16
last_updated: 2026-05-16
---

# ISA-95 — Enterprise-Control System Integration

## Scope

ISA-95 (formally ANSI/ISA-95, also published internationally as the IEC 62264 joint standard) is the practitioner-canonical multi-part framework for **integrating enterprise business systems with manufacturing operations and control systems**. It provides a vendor-neutral conceptual scaffolding — terminology, functional hierarchy, data-flow models, and activity-decomposition framework — for the integration that connects manufacturing-execution and supervisory-control systems to the broader enterprise.

For upstream oil-and-gas operations, ISA-95 is the conceptual anchor for production SCADA architecture (see [Production SCADA Architecture](production-scada-architecture.md)), for production-data integration (see [Production Data Historian Patterns](production-data-historian-patterns.md)), and for the broader operational-data flow from field instrumentation to allocation, regulatory reporting, and business decisioning. Its value is the **vendor-neutral abstraction** it provides: an ISA-95-compliant architecture can integrate SCADA platforms from different vendors at different tiers without being captive to a single vendor's namespace and data-model conventions.

This page is the **standards anchor** for the Level 0-4 control hierarchy that the production-SCADA-architecture and production-data-historian-patterns concept pages reference. The standard is paywalled and multi-part; this page summarises structural intent and cross-links to the publishers without transcribing standard text.

## Why operators read it

- **Vendor-neutral conceptual framework** — operators specifying SCADA-architecture, MES-integration, and historian-architecture projects use ISA-95 as the integration-reference framework that decouples the project from any single vendor's product architecture
- **Multi-vendor integration** — modern upstream operators run multi-vendor SCADA, historian, and enterprise estates (e.g. one platform vendor for the topside DCS, a different vendor for the historian, a third for the MES layer). ISA-95 provides the data-model and interface-decomposition framework that operationalises the integration
- **Mergers and acquisitions integration** — when operators acquire assets with different SCADA estates, ISA-95-aligned architecture eases the integration of the acquired assets into the acquirer's data-and-control infrastructure
- **Documentation and engineering communication** — ISA-95 terminology is widely-understood across operator, integrator, and vendor practitioner communities, making it the lingua franca for engineering specification, RFP/RFQ documents, and architecture review

## Multi-part structure (structural overview, paraphrased)

ISA-95 is organised into multiple parts, each addressing a specific aspect of enterprise-control integration. The high-level part structure (verify-at-publish-time against the publisher for current revision and supplementary parts):

- **Part 1 — Models and Terminology** — establishes the functional hierarchy (Level 0-4), the equipment hierarchy, the personnel/material/equipment/process-segment data models, and the canonical terminology used across the rest of the standard
- **Part 2 — Object Model Attributes** — populates the Part 1 data models with attribute definitions used for integration message construction
- **Part 3 — Activity Models of Manufacturing Operations Management** — decomposes the manufacturing-operations-management activities (Level 3 in the hierarchy) into a structured activity model; the basis for MES-system-and-function specification
- **Part 4 — Object Models and Attributes for Manufacturing Operations Management Integration** — extends Part 2's data-model framework into the MES-integration scope
- **Part 5 — Business-to-Manufacturing Transactions** — defines the transaction-level integration between enterprise (Level 4) and manufacturing (Level 3) systems
- **Part 6 — Messaging Service Model** — addresses the messaging-infrastructure level of business-to-manufacturing integration
- **Part 7 — Alias Service Model** (ANSI/ISA-95.00.07-2017) — defines an alias service for identifier mapping across the integration domains addressed by the standard
- **Part 8 — Information Exchange Profiles** (ANSI/ISA-95.00.08-2020) — defines information-exchange profiles for the Level 3 / Level 4 transactions, building on Parts 2, 4, and 5

Per-part revisions are independently published; operators citing ISA-95 in a specification document should pin to the specific part-and-revision applicable to the project. Per-part revisions verified 2026-05-16 against isa.org standards catalog (see frontmatter `revision` field for current per-part publication metadata). The 2025 revision of Part 1 (ANSI/ISA-95.00.01-2025) is the most consequential recent change, addressing specific functions in the enterprise and tightening the boundary framing between enterprise and manufacturing-and-control domains; the structural Level 0-4 hierarchy and Personnel / Material / Equipment / Process-segment data-model entities described elsewhere on this page survive the 2025 revision unchanged.

## The Level 0-4 control hierarchy

The single most-cited element of ISA-95 is the **5-level functional hierarchy** that maps the layered architecture from the physical process to enterprise business systems. The hierarchy is the conceptual backbone of [Production SCADA Architecture](production-scada-architecture.md):

- **Level 0 — Physical Process** — the actual physical process being controlled. For production engineering, this is the producing wells, the manifold-and-choke-and-separator-inlet envelope, the surface piping, and the rotating equipment
- **Level 1 — Basic Control** — sensing, actuation, and basic-loop control. Field instrumentation (pressure transmitters, temperature transmitters, flow meters), final-control elements (control valves, choke actuators, ESD solenoids), and the basic-control layer (RTUs, PLCs, DCS controllers) that closes individual loops
- **Level 2 — Supervisory Control** — process-level monitoring, supervisory control, alarm management, and operator-facing interface. SCADA hosts, HMI consoles, OPC servers, alarm-and-event managers
- **Level 3 — Manufacturing Operations Management (MES)** — production-scheduling, dispatch-decisioning, batch-management, performance analysis, and operational-data management. The historian sits structurally at the Level 2-3 boundary; the MES layer is thinner in upstream production-engineering than in process-manufacturing industries but covers production-scheduling integration, well-test scheduling, allocation-system integration, and workflow-management
- **Level 4 — Business Planning and Logistics (ERP)** — enterprise resource planning, financial systems, regulatory-reporting interfaces, allocation-accounting systems. Production data flows from the historian to this layer for federal and state reporting (per [30 CFR 250](30-cfr-250.md), [Federal Production Reporting](../concepts/federal-production-reporting.md), [State Production Reporting](../concepts/state-production-reporting.md)), custody-transfer-derived royalty calculation (per [Custody Transfer Overview](../concepts/custody-transfer-overview.md)), and allocation-accounting closure

The hierarchy is **conceptual, not prescriptive** — a real-world architecture may collapse adjacent layers, span multiple layers in one product, or distribute a single layer across multiple products. The value of the hierarchy is the shared vocabulary and the integration-interface conceptual framework, not a mandate for specific software architecture.

## Functional data model framework

ISA-95 Part 1 establishes a small number of canonical data-model entities that recur across the standard:

- **Personnel** — people involved in operations, with skills, training, and qualification metadata
- **Material** — physical inputs and outputs (raw materials, intermediates, finished products); for production engineering, applies to chemicals consumed, produced fluid handled, and waste-stream management
- **Equipment** — physical equipment items with capabilities, capacity, and operational state
- **Process segments** — defined units of operational work (e.g. "produce a batch of crude oil") with required personnel, material, equipment, and parameter resources
- **Operations definitions** — engineering specifications for how process segments are performed
- **Operations capabilities** — what an operating site is capable of producing, at what rate, with what resources

For upstream-production operations, the most operationally-significant entities are **equipment** (well, wellhead, separator, meter station — each instance with its capability and operational-state metadata) and **process segments** (allocation period, well-test event, intervention event — each consuming a defined resource bundle). The standard provides the data-model framing; the operator-side mapping into a specific SCADA-and-MES-and-ERP estate is operator-and-integrator work.

## Relevance to production SCADA architecture

The ISA-95 framework is the structural reference for the SCADA-architecture concept page in this wiki. Specifically:

- **Level 0-4 hierarchy** — the layering pattern described in [Production SCADA Architecture](production-scada-architecture.md) is the ISA-95 functional hierarchy applied to upstream production
- **Vendor-neutral integration** — the SCADA-architecture page's vendor-citation discipline (vendor platforms cited by name only, internals out of scope) is the operationalisation of ISA-95's vendor-neutral integration philosophy: the framework is the standard, the vendor-platform implementations are interchangeable per the standard's interface definitions
- **Historian placement** — the historian's structural placement at the Level 2-3 boundary, described in [Production Data Historian Patterns](production-data-historian-patterns.md), comes directly from the ISA-95 hierarchy
- **Enterprise-reporting integration** — the data flow from the historian to regulatory-reporting systems (per [Federal Production Reporting](../concepts/federal-production-reporting.md), [State Production Reporting](../concepts/state-production-reporting.md)) is a Level 3 → Level 4 integration in ISA-95 framing

## Adjacent standards

- **ISA-88** — Batch Control (adjacent ISA standard; orchestrates batch-process operations; applicable to batch-oriented upstream operations like batch-chemical-treatment programs)
- **IEC 62264** — the IEC counterpart to ISA-95, jointly published; international operators dominantly cite the IEC number rather than the ISA number
- **ISA 18.2** — Management of Alarm Systems for the Process Industries (alarm-management methodology consumed by the Level 2 supervisory-control layer)
- **IEC 61131-3** — Programmable Controllers, Part 3: Programming Languages (PLC programming language family; populates the Level 1 basic-control layer)
- **IEC 61511 / IEC 61508** — functional-safety standards for the safety-instrumented-system (SIS) layer; complementary to ISA-95's basic-control framing
- **OPC-UA** (OPC Foundation) — modern interoperability protocol family; the dominant Level 2 ↔ Level 3 integration interface
- **IEC 62443 / ISA/IEC 62443** — cybersecurity for industrial automation and control systems; **OUT OF SCOPE** for this wiki phase per scope-edge framing

## Concept-page references

- [Production SCADA Architecture](../concepts/production-scada-architecture.md) — Level 0-4 hierarchy applied to upstream production-engineering
- [Production Data Historian Patterns](../concepts/production-data-historian-patterns.md) — historian placement in the hierarchy
- [Surface Handover Boundary](../concepts/surface-handover-boundary.md) — the in-scope envelope the SCADA architecture covers
- [Manifold Tie-In](../concepts/manifold-tie-in.md), [Choke Skid and Separator Inlet](../concepts/choke-skid-and-separator-inlet.md) — Level 0-1 physical hardware in the envelope

## Cross-references

- **Cross-domain into engineering-standards** — ISA-95's functional-safety adjacency (IEC 61508 / IEC 61511) and alarm-management adjacency (ISA 18.2) live in engineering-standards
- **Vendor-archetype framing** — DCS, SCADA, historian, MES, and ERP vendors implement ISA-95-aligned architecture across their product portfolios. The vendor table at [Production SCADA Architecture](../concepts/production-scada-architecture.md) covers the dominant vendor archetypes at name-and-capability level only; no proprietary implementation internals reproduced

## Public references

- **ANSI/ISA — International Society of Automation** — official publication pages for ANSI/ISA-95 parts (isa.org). The publishing-body source.
- **IEC — International Electrotechnical Commission** — official publication pages for IEC 62264 parts (iec.ch). The international counterpart publication.
- **Scholten, B.** — *The Road to Integration: A Guide to Applying the ISA-95 Standard in Manufacturing*, ISA 2007 (ISBN 978-0-979-50190-1). Practitioner-oriented application guide for ISA-95 integration projects.
- **Brandl, D.** — *Design Patterns for Flexible Manufacturing*, ISA 2007 (ISBN 978-0-979-50191-8). Patterns-based reference for applying ISA-95 in real-world MES-and-integration architectures.
- **Boyer, S. A.** — *SCADA: Supervisory Control and Data Acquisition*, 4th ed., ISA 2010 (ISBN 978-1-936007-09-7). SCADA textbook that frames ISA-95 alongside other SCADA-architecture references.
- **Williams, T. J.** — The Purdue Reference Model for CIM (Computer-Integrated Manufacturing), 1989 — the foundational hierarchical-model work from which ISA-95's Level 0-4 hierarchy descends. The Purdue Enterprise Reference Architecture (PERA) is the academic precedent for the ISA-95 framework.
- **MESA International** — the Manufacturing Enterprise Solutions Association; practitioner community around MES and the ISA-95 framework (mesa.org).

## Notes

- ISA-95 is a multi-part standard with per-part revision dates. The `revision` frontmatter field carries the verified per-part publication metadata as of 2026-05-16 — the operator specifying ISA-95 in a project document should pin to the specific part and revision (e.g. "ANSI/ISA-95.00.01-2025" for Part 1, with similar specificity for other parts). Different parts have been revised on different schedules; Part 1's 2025 revision is the most recent.
- ISA-95 and IEC 62264 are **the same standard** with different publication numbers; ISA is the originating body, IEC publishes the same content as IEC 62264 for international adoption. Different operator and integrator communities use the two numbers interchangeably.
- The Level 0-4 hierarchy descends from the Purdue Reference Model for CIM (Williams 1989); the ISA-95 framing is the modern operationalised version of the Purdue conceptual framework.
- The standard is paywalled. This wiki paraphrases the structural intent and references the standard for operators who already have a licensed copy. No verbatim text reproduced.
- ISA-95 itself is **vendor-neutral and protocol-agnostic** — it does not prescribe specific protocols (OPC-UA, Modbus, etc.) or vendor platforms (PI System, Experion, etc.). Operators populate the framework with operator-and-integrator-chosen implementations. The framework's value is the abstraction, not a specific technology mandate.
- The MES (Level 3) layer is **thinner in upstream production-engineering** than in process-manufacturing industries (refining, petrochemicals, pharmaceuticals). Many upstream operators run a Level 2 (SCADA + historian) → Level 4 (ERP and reporting) architecture with minimal explicit Level 3 MES infrastructure — production-scheduling and workflow-management activities are distributed across the Level 2 and Level 4 layers rather than centralised in a dedicated MES product. The framework still applies; it is just realised differently.
