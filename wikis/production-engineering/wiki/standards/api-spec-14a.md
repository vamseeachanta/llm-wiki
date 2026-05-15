---
title: "API Spec 14A — Subsurface Safety Valve Equipment"
code_id: api-spec-14a
publisher: American Petroleum Institute
revision: "12th edition (2015) — to be verified at next ingest pass against current edition tracked on api.org"
jurisdiction: international
tags: [specification, api, subsurface-safety-valve, sssv, well-control, completions, smart-completion-envelope]
sources:
  - api-spec-14a
added: 2026-05-15
last_updated: 2026-05-15
---

# API Spec 14A — Subsurface Safety Valve Equipment

## Scope

API Spec 14A is the canonical specification for **subsurface safety valve (SSSV)** equipment installed in the production tubing of oil and gas wells. The standard defines design, manufacturing, functional, and performance-test requirements for the downhole safety valves that close the production conduit on loss of surface control — the last automatic well-isolation barrier between produced fluids and the surface environment.

This page is the **standards anchor** for SSSV-related coverage in the production-engineering wiki. SSSV envelope specifications are directly relevant to multi-zone and smart-completion architectures because intelligent-completion control lines, downhole-monitoring cables, and remotely-actuated flow-control hardware all share the production tubing with the SSSV and must integrate with the safety-valve closure envelope.

## Why operators read it

- **Regulatory mandate** — subsurface safety valves are required in offshore and many onshore jurisdictions (US OCS regulations under 30 CFR 250, North Sea NORSOK, UK HSE, Australian NOPSEMA, Brazilian ANP). Spec 14A is the universally-referenced compliance benchmark.
- **Vendor qualification basis** — operators specifying SSSV hardware in completion-design AFEs typically write acceptance against Spec 14A class (e.g. "Class 2 surface-controlled subsurface safety valve, Spec 14A current edition").
- **Smart-completion design envelope** — multi-zone and smart-completion architectures must demonstrate that downhole hydraulic and electric control lines, sensor cables, and chemical-injection lines do not compromise the SSSV closure mechanism. Spec 14A defines the integrity envelope that smart-completion designs must respect.
- **Litigation and incident audit trail** — when post-incident reviews follow well-control events, SSSV qualification records (Spec 14A class, manufacturing certification, acceptance-test data) are first-line documentary evidence.

## Valve-class structure (high level)

The standard distinguishes valve classes by **actuation method** and **service envelope**. The exact class labels and concrete numerical thresholds have evolved across editions and are not transcribed here (paywalled standard); the structural intent is stable:

- **Surface-controlled subsurface safety valve (SCSSV)** — held open by hydraulic pressure supplied via a control line from surface; loss of control-line pressure causes closure (fail-safe-closed). The dominant modern architecture.
- **Subsurface-controlled subsurface safety valve (SSCSV)** — actuated by direct sensing of tubing flow rate or pressure differential; closes when flow exceeds a velocity threshold (sometimes called "storm choke"). Lower-cost legacy class with narrower applications today.
- **Tubing-retrievable vs wireline-retrievable** — orthogonal axis: a tubing-retrievable SCSSV is integral to the production tubing string and requires pulling tubing for replacement; a wireline-retrievable SCSSV sits in a side-pocket-style nipple and can be replaced via slickline. Each architecture has trade-offs in reliability, OPEX, and smart-completion compatibility.
- **Service-environment categories** — the standard defines categories accommodating sour service (per NACE MR0175 / ISO 15156), HPHT service, sand-laden flow, and deep-set high-back-pressure applications.

## Functional requirements (paraphrased structural intent)

The standard imposes the following operational categories of requirement:

- **Closure performance** — the valve must close against defined flowing conditions within a defined time when the actuation signal is removed (control-line pressure bled, flow-velocity threshold exceeded). The closure envelope considers gas, oil, multiphase, and sand-laden service.
- **Pressure-integrity** — the valve must hold downstream pressure with no leak path through the closure mechanism, body, or control-line interface.
- **Endurance and reliability** — the valve must demonstrate a defined number of open-close cycles without functional degradation, with cycle counts scaled to the expected service profile.
- **Material compatibility** — body, internals, seals, and trim materials must be qualified for the design service envelope (sour service, chloride content, temperature).
- **Marking, documentation, traceability** — each valve carries a permanent serial number; manufacturing records (heat-lot certifications, qualification-test data, witnessed-acceptance results) form the documentary qualification basis.

## Multi-zone and smart-completion coupling

In multi-zone completions ([Multi-Zone Completions](../concepts/multi-zone-completions.md)), each producing zone may interact with the SSSV envelope in distinct ways:

- **Single SSSV above all zones** — the standard architecture: one SSSV at the top of the production interval isolates the entire commingled or selectively-produced flow stream. Closure isolates all zones simultaneously.
- **Zone-isolation packers below the SSSV** — packers that segment the production interval do **not** themselves provide barrier-class isolation against tubing fluid; only the SSSV provides automatic surface-loss-of-control closure.
- **Flow-control hardware below the SSSV** — inflow-control valves (ICVs), sliding sleeves, and downhole chokes are reservoir-management hardware, not safety-barrier hardware. They do not substitute for the SSSV.

In smart-completion architectures ([Intelligent-Well Completions](../concepts/intelligent-well-completions.md)), the SSSV must integrate with:

- **Hydraulic control lines for ICV actuation** — the smart-completion control-line bundle must not compromise the SSSV control-line integrity or its emergency-closure response.
- **Electric power and signal cables** for downhole gauges and monitoring sensors (DTS / DAS / PT) — cable routing past the SSSV body must not impair closure performance.
- **Chemical-injection lines** for downhole inhibitor, demulsifier, or scale-treatment delivery — the injection-line penetration must respect the SSSV pressure-integrity envelope.

The control-line packaging ("control-line bundle" or "encapsulated tubing-encapsulated conductor") that carries hydraulic, electrical, and chemical lines past the SSSV is a smart-completion-design discipline in its own right and is the dominant first-cost adder over a conventional completion.

## Subsea control-system anchor

For subsea-tree applications, the SSSV control line connects through the production-tree control system to the surface host (FPSO, platform, or shore-control facility) under the **API RP 17F** subsea-production-control-system standard. The handoff between Spec 14A (downhole equipment) and RP 17F (control-system architecture) is at the wellhead penetrator. See [API RP 17F discussion in the Multi-Zone Completions page](../concepts/multi-zone-completions.md) for the integration boundary.

## Concept-page references

- [Multi-Zone Completions](../concepts/multi-zone-completions.md) — router for multi-zone architectures and SSSV envelope
- [Selective Production](../concepts/selective-production.md) — zonal-isolation packers and sliding-sleeve hardware
- [Downhole Flow Control](../concepts/downhole-flow-control.md) — ICV / ICD / AICD families
- [Intelligent-Well Completions](../concepts/intelligent-well-completions.md) — smart-completion architecture and control-line integration

## Cross-references

- **Adjacent standards** — **ISO 28781** (subsurface barrier valves and related equipment, providing complementary downhole-barrier coverage); **API RP 17F** (subsea production control systems, defining the surface-to-downhole hydraulic and electric control-line architecture for subsea smart completions); **NACE MR0175 / ISO 15156** (sour-service material requirements applicable to SSSV trim, body, and seal metallurgy).
- **Drilling-engineering** — [Casing Program Design](../../../drilling-engineering/wiki/concepts/casing-program-design.md) (production-tubing burst rating sets the upper bound on SSSV body design pressure).
- **Vendor-archetype framing** — SSSV manufacturers (Halliburton, Schlumberger, Baker Hughes, Weatherford, and specialty independents such as Tejas Research & Engineering) qualify equipment to Spec 14A. Vendor-specific actuation hardware, wireline-retrievable lock-mandrel proprietary geometries, and smart-completion control-bundle proprietary architectures are concept-level only in this wiki — no proprietary content reproduced.

## Public references

- **API** — official publication page for API Spec 14A (current edition retrievable from api.org).
- **Bellarby, J.** — *Well Completion Design*, Elsevier (Developments in Petroleum Science 56), ISBN 978-0-444-53210-7. SSSV chapter covers the engineering-design context that Spec 14A formalises.
- **Lyons, W. C. (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, Elsevier (ISBN 978-0-7506-7785-1). Production-completion chapters cover SSSV placement and operational practice.
- **SPE OnePetro SSSV literature** — extensive corpus on SSSV reliability, slam-closure analysis, control-line integrity, and integration with smart-completion architectures.
- **30 CFR 250 Subpart H** (US BSEE offshore safety regulations) — references SSSV requirements and serves as the regulatory driver behind Spec 14A adoption in US OCS operations.

## Notes

- API Spec 14A revisions have been issued multiple times since the 1970s. Operators specifying SSSV equipment in AFE / scope-of-work documents should always pin to a specific edition.
- The standard's evolution has tracked the maturation of smart-completion technology and the increasing complexity of downhole control-line bundles required for multi-zone reservoir management.
- API Spec 14A is paywalled. This wiki paraphrases the structural intent and references the standard for operators who already have a licensed copy. No verbatim text reproduced.
- The companion downhole-barrier-valve standard **ISO 28781** addresses subsurface barrier valves and related equipment beyond the SSSV scope per se; multi-zone completion designers should review both standards for the complete downhole-barrier picture. ISO 28781 is also paywalled and is referenced here at the structural level only.
