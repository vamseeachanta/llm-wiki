---
title: "Production SCADA Architecture"
tags: [scada, rtu, plc, hmi, opc-ua, modbus, iec-61850, dnp3, hart, isa-95, production-data-integration, surface-handover-boundary]
added: 2026-05-16
last_updated: 2026-05-16
---

# Production SCADA Architecture

## Scope

Production SCADA (Supervisory Control And Data Acquisition) is the data-and-control architectural overlay that spans the entire [Surface Handover Boundary](surface-handover-boundary.md) envelope — from wellhead instrumentation, through the production and test manifolds, through the choke skid, to the separator-inlet conditioning. It carries operating data from the field instruments to the operator-facing HMI consoles, to the historian for trending and analytics (per [Production Data Historian Patterns](production-data-historian-patterns.md)), and to the downstream control-and-decisioning systems that interface with reservoir-management, allocation, and regulatory reporting.

This page covers SCADA topology (RTU / PLC / HMI / OPC server / historian), the [ISA-95](../standards/isa-95.md) manufacturing-control hierarchy (Level 0-4 mapping), the RTU-vs-PLC distinction, the named-only treatment of fieldbus protocols (Modbus, OPC-UA, IEC 61850, DNP3, HART), and the **explicit cybersecurity scope-edge** (IEC 62443 and adjacent cybersecurity standards are OUT OF SCOPE for this wiki). It does not transcribe protocol internals, vendor-proprietary address-space schemas, or platform-specific implementation details.

**Vendor-confidentiality posture:** SCADA + historian content carries the heaviest vendor-IP-risk profile in Phase 5 of the production-engineering wiki. This page provides concept-level and architectural framing only. Vendor-specific SCADA platform internals, proprietary control-logic implementations, namespace schemas, communication-protocol implementation details, and proprietary historian-archive internals are all explicitly out of scope. Vendor product families are cited by name and general capability only — no proprietary content reproduced.

## SCADA topology

A production SCADA system organises around a layered architecture that connects field instrumentation to operator-facing control and to enterprise-level data systems:

### Level 0 — Process and field

The lowest layer: the physical process and the field instrumentation that senses it. For production engineering, this includes:

- **Sensing instrumentation** — pressure transmitters, temperature transmitters, flow meters, level transmitters, position transducers on valves and chokes, sand detectors, vibration sensors, downhole gauges where installed
- **Actuating instrumentation** — choke actuators, valve actuators, ESD solenoids, chemical-injection pumps, gas-lift compressor controls
- **Local protective devices** — pressure-relief valves, rupture discs, mechanical safety interlocks (not part of SCADA but coordinated with it)

Field instruments communicate with the next layer via fieldbus protocols (HART, Modbus, Foundation Fieldbus, Profibus, IEC 61850, OPC-UA — named only here, internals out of scope).

### Level 1 — Basic control (RTU / PLC)

The Remote Terminal Unit (RTU) and Programmable Logic Controller (PLC) layer. These devices acquire data from field instrumentation, execute local control logic, and communicate upstream to the supervisory layer:

- **Remote Terminal Unit (RTU)** — historically optimised for **remote / distributed / lower-loop-rate** applications (wellpad telemetry, pipeline gathering, water-injection well monitoring). Strengths: low power consumption, ruggedised packaging, long-haul-communication-protocol support (DNP3, IEC 60870-5), often solar-powered for unattended remote sites
- **Programmable Logic Controller (PLC)** — historically optimised for **central / process / higher-loop-rate** applications (production platform, compression facility, processing plant). Strengths: high-speed scan, deterministic execution for safety-critical loops, broad I/O-module ecosystem, programming via IEC 61131-3 language family
- **Modern convergence** — the RTU vs PLC distinction has blurred in modern hardware. Many modern devices are marketed as "RTU/PLC" or as "edge controllers" and provide both feature sets. The distinction is now more a deployment-pattern choice than a hardware-class choice
- **Safety PLC (SIS)** — a dedicated safety-instrumented-system PLC running the SAFE-chart-derived ESD logic per [API RP 14C](../standards/api-rp-14c.md) (with optional IEC 61511 safety-integrity-level enrichment). Architecturally separate from the basic-control PLC for independence per IEC 61511

### Level 2 — Supervisory (HMI / SCADA host)

The supervisory layer: the operator-facing console, the SCADA host server(s), the OPC server, and the alarm-and-event management. This is where the SCADA-architecture descriptor formally applies:

- **Human-Machine Interface (HMI)** — the operator-facing graphical display showing process state (pressure / temperature / flow trends; valve states; alarm conditions). Modern HMIs run on workstation-class hardware with redundant servers
- **SCADA host** — server software that aggregates the field data, executes higher-level control logic, drives the HMI displays, and feeds the upstream historian and enterprise systems
- **OPC server** — middleware that abstracts the device-specific fieldbus protocols into a unified data-access interface (per OPC Foundation standards: OPC Classic for legacy installations, OPC-UA for modern installations)
- **Alarm and event management** — alarm prioritisation, suppression, escalation, and audit-trail capture per the ISA 18.2 alarm-management methodology

### Level 3 — Operations management (MES)

The Manufacturing Execution System (MES) layer in ISA-95 framing: production-scheduling, dispatch-decisioning, batch-management. In upstream production-engineering, this layer is typically thinner than in process-manufacturing industries; key elements include:

- **Production-scheduling integration** — connecting the SCADA system to the well-test scheduler, the allocation system, and the maintenance-management system
- **Historian feed** — see [Production Data Historian Patterns](production-data-historian-patterns.md). The historian is structurally Level 3 (it spans Level 2 and Level 4 interfaces)
- **Workflow integration** — connecting operational events (alarms, ESDs, equipment-state transitions) to the operations-management workflow (work-order generation, intervention scheduling)

### Level 4 — Enterprise (business systems)

The business-systems layer: enterprise resource planning, financial systems, regulatory-reporting interfaces, allocation-accounting systems. Production data from the historian feeds [Federal Production Reporting](federal-production-reporting.md), [State Production Reporting](state-production-reporting.md), [Gas Flaring Rules](gas-flaring-rules.md), [Custody Transfer Overview](custody-transfer-overview.md), and downstream-tie-in interfaces at this layer.

## ISA-95 manufacturing-control hierarchy

The [ISA-95](../standards/isa-95.md) standard (Enterprise-Control System Integration; published as the IEC 62264 joint standard internationally) provides the canonical framework for the Level 0-4 hierarchy described above. ISA-95 was developed by the International Society of Automation as a vendor-neutral framework for integrating enterprise business systems with manufacturing-control systems, and is widely adopted across upstream oil-and-gas operations as the conceptual scaffolding for SCADA architecture.

The framework's value to production engineering is the **vendor-neutral abstraction** it provides: an ISA-95-compliant architecture can integrate SCADA platforms from different vendors at different facility tiers, integrate field instrumentation from arbitrary manufacturers, and integrate the SCADA layer with enterprise systems through structured interface definitions. ISA-95 does not prescribe specific protocols, vendor platforms, or implementation choices; it provides the conceptual layering and the data-model framework that operators populate with vendor-specific implementations.

## Field-bus protocols (named only)

Production SCADA installations carry data over a small set of widely-deployed protocols. This page names each protocol and notes its dominant use case; protocol internals (frame formats, address-space schemas, message-encoding internals) are out of scope. Operators consult the protocol-specification documents from the relevant publishing body for implementation detail.

- **HART** — Highway Addressable Remote Transducer. Hybrid 4-20 mA analog + digital communication; legacy-dominant field-instrumentation interface. Maintained by FieldComm Group
- **Modbus** — Open serial / TCP protocol for industrial communication. Originally serial (Modbus RTU); TCP/IP variant (Modbus TCP) dominant in modern installations. Maintained by Modbus Organization
- **OPC-UA** — OPC Unified Architecture. Modern vendor-neutral interoperability standard for industrial automation; published by OPC Foundation. Used as the dominant SCADA-to-MES and SCADA-to-historian interface in modern installations
- **IEC 61850** — Communication Networks for Power Utility Automation. Originally a utility-substation standard; increasingly applied to offshore platform electrical SCADA where electrical-system integration is a load-bearing scope. Published by IEC
- **DNP3** — Distributed Network Protocol. Utility-SCADA-adjacent; widely deployed in pipeline gathering, water-injection-well telemetry, and other distributed-remote-site applications. Open standard maintained by DNP Users Group
- **Foundation Fieldbus** — Multi-drop digital field-instrumentation bus; deployed in process-control installations as an alternative to HART. Maintained by FieldComm Group
- **Profibus** — Process Field Bus; widely deployed in European-pedigree installations. Maintained by PI (Profibus & Profinet International)

### Protocol-citation discipline

This wiki names protocols and notes their general role only. NO transcription of frame formats, NO transcription of address-space schemas, NO transcription of message-encoding internals, NO transcription of proprietary vendor extensions to base protocols. Operators consult the publishing-body specifications directly for implementation. Protocol internals are software-implementation IP that lives outside this wiki's scope.

## RTU vs PLC distinction

The historical RTU vs PLC distinction reflected hardware-architecture and deployment-pattern differences:

| Axis | RTU (historical) | PLC (historical) |
|---|---|---|
| **Deployment** | Remote unattended sites | Centralised attended facilities |
| **Power** | Solar / battery / low-grid | Plant-grade AC |
| **Scan rate** | Seconds-to-minutes (event-driven) | Milliseconds-to-tens-of-ms (deterministic) |
| **Communication** | Long-haul (DNP3, IEC 60870, radio, cellular) | Industrial-LAN (Ethernet, Profibus, Modbus TCP) |
| **Packaging** | Ruggedised, sealed, wide-temperature | DIN-rail, climate-controlled enclosure |
| **Programming** | Vendor-specific configuration | IEC 61131-3 language family |

Modern hardware blurs the distinction: "edge controller" or "RTU/PLC" devices provide both feature sets. The distinction has become more about **deployment pattern** than about **hardware class**. The architectural decision an operator faces is which deployment pattern fits the asset (centralised platform vs distributed wellpads), not which hardware class to procure.

## Cybersecurity scope-edge (OUT OF SCOPE)

**Cybersecurity for industrial control systems is OUT OF SCOPE for this wiki phase per Phase 5 epic.**

Cybersecurity is its own discipline with vendor-neutral standards coverage that warrants a dedicated wiki domain or phase, not a subsection on a SCADA-architecture page:

- **IEC 62443** (also published as ISA/IEC 62443) — Industrial Automation and Control Systems Security; the dominant international cybersecurity standards-suite for ICS environments
- **NIST SP 800-82** — Guide to Industrial Control Systems Security; the dominant US-side reference framework
- **API STD 1164** — Pipeline SCADA Security; the pipeline-industry-specific cybersecurity standard
- **TSA Pipeline Security Guidelines** — US Transportation Security Administration pipeline cybersecurity guidance, applicable to pipeline SCADA but adjacent to production-side SCADA

The defensible reasoning for the scope-edge: cybersecurity engineering operates on different threat models (adversarial / intentional vs operational / accidental), different assurance frameworks (risk-based security assessment vs reliability-based safety assessment), different specialist disciplines (security engineering vs control engineering), and different regulatory regimes than the operational SCADA discipline. Compressing cybersecurity into a SCADA-architecture page would either misrepresent the scope or fail to do it justice.

Operators needing cybersecurity coverage should consult the relevant primary sources directly (IEC 62443 family, NIST SP 800-82, API STD 1164, and the increasingly active OT-cybersecurity vendor and consulting ecosystem). This wiki notes the scope-edge here and on adjacent pages (per [30 CFR 250](../standards/30-cfr-250.md) Adjacent federal frameworks section) and reserves cybersecurity for a future dedicated treatment.

## SCADA and historian vendor-citation discipline

SCADA platform vendors, historian-system vendors, RTU/PLC vendors, and SCADA-adjacent software vendors are cited at name + general capability level only. The table below establishes the allowed-vs-blocked enforcement contract; this is the testable equivalent of the production-engineering wiki's standing vendor-IP discipline and mirrors the precedent in [Flow Assurance](flow-assurance.md), [Choke Sand Erosion](choke-sand-erosion.md), and [Custody Transfer Overview](custody-transfer-overview.md).

### SCADA / DCS platform vendors

| Vendor | Allowed citation | Blocked citation |
|---|---|---|
| **OSIsoft PI / AVEVA PI System** | "PI System — practitioner-dominant operational-historian / SCADA-adjacent data infrastructure platform; deployed across upstream and midstream operators" | Proprietary PI tag-naming convention schemas, PI namespace-and-asset-framework internals, archive-file binary layout, compression-algorithm internals, AF SDK internals |
| **AVEVA Process Optimization (formerly Wonderware)** | "AVEVA SCADA / system-platform family — broad-coverage SCADA platform across process and manufacturing industries" | Wonderware HMI tag-script internals, proprietary system-platform schema |
| **Honeywell Experion PKS** | "Experion PKS distributed-control-system / SCADA family — dominant in topside-platform and gas-processing applications" | Experion server internals, proprietary control-block libraries, Honeywell-specific ESD-logic implementation |
| **Emerson DeltaV** | "DeltaV DCS family — broad deployment in offshore production-platform and onshore gas-processing applications" | DeltaV configuration-and-engineering-tool internals, proprietary control-block libraries |
| **Schneider EcoStruxure (formerly Foxboro / Modicon)** | "EcoStruxure DCS / SCADA family — broad deployment across utility and process applications" | Modicon PLC firmware internals, Foxboro I/A Series proprietary protocols |
| **Rockwell PlantPAx** | "PlantPAx DCS family based on the ControlLogix PLC architecture — broad deployment in onshore production applications" | ControlLogix firmware internals, RSLogix engineering-tool internals, AOI library internals |
| **Yokogawa CENTUM VP** | "CENTUM VP DCS family — broad deployment in process-industry applications including LNG, refining, and offshore production" | CENTUM controller firmware internals, FCS proprietary protocols |
| **Siemens SIMATIC PCS 7** | "SIMATIC PCS 7 DCS family — broad deployment in European-pedigree process operations" | SIMATIC controller firmware internals, STEP 7 / TIA Portal engineering-tool internals |
| **ABB Ability System 800xA** | "System 800xA DCS family — broad deployment in process operations" | 800xA controller firmware internals, Control Builder engineering-tool internals |

### Historian and time-series platforms

| Vendor | Allowed citation | Blocked citation |
|---|---|---|
| **AVEVA PI System (Historian role)** | "PI Historian — practitioner-dominant operational-historian for upstream-and-midstream operating data" | Archive-file binary layout, swinging-door compression algorithm internals, AF asset-framework schema |
| **Honeywell Uniformance PHD** | "Uniformance PHD historian — Honeywell-ecosystem operational historian" | PHD storage internals, proprietary compression-algorithm internals |
| **Aspen InfoPlus.21** | "InfoPlus.21 historian — Aspen-ecosystem operational historian; common in refining and gas-processing operations" | IP.21 storage internals, proprietary compression internals |
| **GE Proficy Historian (now Emerson)** | "Proficy Historian — broad operational-historian deployment" | Proficy storage internals, proprietary compression internals |
| **AVEVA Historian (formerly Wonderware Historian)** | "AVEVA Historian — Wonderware-ecosystem operational historian" | Historian storage internals, proprietary tag-and-namespace schema |

### RTU / PLC / Edge controller vendors

| Vendor | Allowed citation | Blocked citation |
|---|---|---|
| **Schneider Electric** | "Schneider PLC and RTU portfolio (Modicon-pedigree, EcoStruxure-branded); broad deployment across upstream telemetry and platform-control" | Modicon controller firmware internals, proprietary configuration-tool schemas |
| **Allen-Bradley (Rockwell Automation)** | "Allen-Bradley CompactLogix / ControlLogix PLC portfolio; dominant in onshore production wellpad telemetry and platform-control" | ControlLogix firmware internals, AOI library schemas |
| **Siemens** | "Siemens SIMATIC PLC portfolio (S7-1500, S7-1200); broad European-pedigree deployment" | SIMATIC firmware internals, STEP 7 / TIA engineering-tool internals |
| **ABB** | "ABB AC500 / Symphony Plus PLC and DCS-controller portfolio; broad deployment in process applications" | AC500 firmware internals, Symphony Plus controller internals |
| **Emerson** | "Emerson FloBoss / ROC RTU portfolio for wellpad gas-measurement telemetry; broad deployment in gas-gathering operations" | FloBoss firmware internals, ROC configuration-tool schemas, AGA-compute-algorithm internals |
| **Honeywell** | "Honeywell SCADAPack RTU portfolio (acquired ex-Schneider); broad upstream telemetry deployment" | SCADAPack firmware internals, configuration-tool schemas |
| **Yokogawa** | "Yokogawa STARDOM / ProSafe-RS controller portfolio; safety and basic-process-control" | STARDOM firmware internals, ProSafe-RS safety-controller internals |
| **GE Intelligent Platforms (now Emerson)** | "GE PACSystems controller portfolio; legacy and ongoing deployment in process applications" | PACSystems firmware internals |

The vendor-citation discipline is the **testable enforcement contract** equivalent to the production-chemistry-deny-list precedent established in Phase 4 ([Corrosion Management](corrosion-management.md), [Choke Sand Erosion](choke-sand-erosion.md)). Any text that crosses from the Allowed column to the Blocked column should be removed and re-cited from a public protocol-specification or standards-body document instead. The table is intentionally comprehensive enough (9 + 5 + 8 = 22 vendor entries) to make the discipline operationally visible to reviewers.

## Cross-domain interactions

- **Production accounting** — SCADA data feeds well-test reconciliation, allocation arithmetic, and custody-transfer measurement closure. See [Production Allocation](production-allocation.md), [Well Test and Reconciliation](well-test-and-reconciliation.md), [GOR and Water-Cut Tracking](gor-and-water-cut-tracking.md), [Custody Transfer Overview](custody-transfer-overview.md), [Flow-Measurement Uncertainty](flow-measurement-uncertainty.md).
- **Regulatory reporting** — historian data feeds federal and state reporting platforms. See [Federal Production Reporting](federal-production-reporting.md), [State Production Reporting](state-production-reporting.md), [Gas Flaring Rules](gas-flaring-rules.md), [Production Allowable Rates](production-allowable-rates.md), [30 CFR 250](../standards/30-cfr-250.md).
- **Well integrity during production** — historian data feeds integrity-monitoring trending and APB/SCP diagnostics. See [Well Integrity During Production](well-integrity-during-production.md), [Integrity Monitoring](integrity-monitoring.md), [Intervention Triggers](intervention-triggers.md), [Corrosion Management](corrosion-management.md).
- **Choke management** — choke-position telemetry and choke-discharge instrumentation are SCADA-acquired. See [Choke Management](choke-management.md), [Choke Skid and Separator Inlet](choke-skid-and-separator-inlet.md), [Choke Types](choke-types.md), [Multiphase Choke Modeling](multiphase-choke-modeling.md), [Choke Sand Erosion](choke-sand-erosion.md).
- **Flow assurance** — SCADA-acquired pressure/temperature trends feed flow-assurance surveillance (hydrate-formation risk, scale-deposition trending). See [Flow Assurance](flow-assurance.md), [Hydrate Management](hydrate-management.md), [Erosional Velocity](erosional-velocity.md).
- **API RP 14C** — Safety PLC architecture aligns with the SAFE-chart methodology. See [API RP 14C](../standards/api-rp-14c.md).
- **Multi-zone completions** — zone-level SCADA tagging relates to multi-zone surface tie-in and to intelligent-completion data. See [Multi-Zone Completions](multi-zone-completions.md), [Intelligent-Well Completions](intelligent-well-completions.md).
- **Surface handover boundary** — SCADA spans the entire envelope. See [Surface Handover Boundary](surface-handover-boundary.md), [Manifold Tie-In](manifold-tie-in.md).
- **Production data historian patterns** — the data-discipline counterpart to this page. See [Production Data Historian Patterns](production-data-historian-patterns.md).
- **Naval-architecture (FPSO)** — FPSO topsides SCADA scope crosses into surface-facility-engineering on the host vessel; cross-reference only.

## Cross-references

- [Surface Handover Boundary](surface-handover-boundary.md), [Manifold Tie-In](manifold-tie-in.md), [Choke Skid and Separator Inlet](choke-skid-and-separator-inlet.md), [Production Data Historian Patterns](production-data-historian-patterns.md)
- [ISA-95](../standards/isa-95.md), [API RP 14C](../standards/api-rp-14c.md), [API Spec 14A](../standards/api-spec-14a.md), [30 CFR 250](../standards/30-cfr-250.md)
- [Production Allocation](production-allocation.md), [Well Test and Reconciliation](well-test-and-reconciliation.md), [GOR and Water-Cut Tracking](gor-and-water-cut-tracking.md), [Custody Transfer Overview](custody-transfer-overview.md), [Flow-Measurement Uncertainty](flow-measurement-uncertainty.md)
- [Federal Production Reporting](federal-production-reporting.md), [State Production Reporting](state-production-reporting.md), [Gas Flaring Rules](gas-flaring-rules.md), [Production Allowable Rates](production-allowable-rates.md)
- [Choke Management](choke-management.md), [Choke Types](choke-types.md), [Multiphase Choke Modeling](multiphase-choke-modeling.md), [Choke Sand Erosion](choke-sand-erosion.md), [Erosional Velocity](erosional-velocity.md)
- [Flow Assurance](flow-assurance.md), [Hydrate Management](hydrate-management.md)
- [Well Integrity During Production](well-integrity-during-production.md), [Integrity Monitoring](integrity-monitoring.md), [Intervention Triggers](intervention-triggers.md), [Corrosion Management](corrosion-management.md)
- [Multi-Zone Completions](multi-zone-completions.md), [Intelligent-Well Completions](intelligent-well-completions.md)

## Standards anchors

- [ISA-95](../standards/isa-95.md) — Enterprise-Control System Integration (Level 0-4 hierarchy framework)
- **ISA-88** — Batch Control (adjacent reference for batch-orientated process operations)
- **IEC 61131-3** — Programmable Controllers, Part 3: Programming Languages (PLC programming language family)
- **IEC 61511** — Functional Safety: Safety Instrumented Systems for the Process Industry (SIS architecture; pairs with [API RP 14C](../standards/api-rp-14c.md))
- **IEC 61508** — Functional Safety of Electrical/Electronic/Programmable Electronic Safety-related Systems (foundational functional-safety standard)
- **ISA 18.2** — Management of Alarm Systems for the Process Industries (alarm-management methodology)
- **OPC Foundation** — OPC Classic and OPC-UA specifications (public protocol framework)
- **Modbus Organization** — Modbus protocol specifications (open standard)
- **IEC 61850** — Communication Networks for Power Utility Automation (offshore-platform-electrical adjacency)
- **IEC 60870-5** — Telecontrol Equipment and Systems, Part 5: Transmission Protocols (DNP3 adjacency)
- **FieldComm Group** — HART and Foundation Fieldbus specifications
- **API STD 1164** — Pipeline SCADA Security (cybersecurity scope-edge reference; OUT OF SCOPE)
- **IEC 62443 / ISA/IEC 62443** — Industrial Automation and Control Systems Security (cybersecurity scope-edge reference; OUT OF SCOPE)
- **NIST SP 800-82** — Guide to Industrial Control Systems Security (cybersecurity scope-edge reference; OUT OF SCOPE)

## Public references

- **Boyer, S. A.** — *SCADA: Supervisory Control and Data Acquisition*, 4th ed., ISA 2010 (ISBN 978-1-936007-09-7). The practitioner-canonical SCADA textbook; covers RTU/PLC architecture, HMI design, communication-protocol selection, and SCADA-system commissioning.
- **Bailey, D. & Wright, E.** — *Practical SCADA for Industry*, Newnes 2003 (ISBN 978-0-7506-5805-8). Practitioner-oriented SCADA-systems reference.
- **Krutz, R. L.** — *Securing SCADA Systems*, Wiley 2005 (ISBN 978-0-7645-9787-9). Cybersecurity-side reference; cited as the boundary-discipline reference — cybersecurity is OUT OF SCOPE for this wiki phase, this reference belongs to the future dedicated cybersecurity coverage.
- **ISA — International Society of Automation** — ISA-95, ISA-88, ISA-18.2 standards publications; isa.org. The publishing body for the standards-suite that frames the SCADA architecture covered here.
- **OPC Foundation** — OPC Classic and OPC-UA specifications; opcfoundation.org. The public protocol-specification source.
- **Modbus Organization** — Modbus specifications; modbus.org. The public protocol-specification source.
- **FieldComm Group** — HART and Foundation Fieldbus specifications; fieldcommgroup.org.
- **IEC** — IEC 61850, IEC 61131-3, IEC 61511, IEC 61508 standards publications; iec.ch.
- **SPE OnePetro production-SCADA literature** — practitioner corpus on upstream SCADA architecture, wellpad telemetry retrofits, historian-integration projects, and edge-controller adoption.
