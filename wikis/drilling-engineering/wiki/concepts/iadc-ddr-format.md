---
title: "IADC DDR — Daily Drilling Report Format"
tags: [iadc, ddr, daily-drilling-report, drilling-data, npt, rop, offset-data]
sources:
  - iadc-drilling-manual
added: 2026-05-13
last_updated: 2026-05-13
---

# IADC DDR — Daily Drilling Report Format

## Scope

The IADC Daily Drilling Report (DDR) is the standard reporting taxonomy for operational data from drilling operations — captured every 24 hours per well, per crew shift. The DDR data structure is the **canonical input format** for offset-well analysis and the data layer downstream applications (AI tender-evaluation agents, drilling-analytics dashboards, operator data warehouses) consume.

## Standard DDR sections

### Header

- Date, well name, AFE number, rig ID
- Reporting period (00:00-24:00, 06:00-06:00, etc. — operator convention)
- Tour breaks
- Personnel on board

### Depth and operations summary

- Depth at start of report period
- Depth at end of report period
- Footage drilled during period
- Casing depth, mud weight, BHA configuration

### Time breakdown (24-hour accounting)

Each 15-minute or 30-minute interval coded by activity:

- Drilling (rotary, sliding)
- Tripping (in, out)
- Reaming
- Connection
- Circulation
- Wireline operations
- Casing running
- Cementing
- Wait on cement / wait on weather / wait on equipment
- NPT subcategories — mechanical, formation, contractor, third-party

### NPT codes

Standard IADC NPT taxonomy:

- **N1** — mechanical (rig equipment)
- **N2** — formation-induced (washout, kick, lost circulation)
- **N3** — contractor (service-company failure)
- **N4** — third-party (weather, logistics, regulatory hold)
- **N5** — waiting on materials

### Mud data

- Weight in / weight out
- Funnel viscosity, PV, YP, gels
- Volumes pumped, returned, lost

### Cementing operations (when applicable)

- Cement type / class / volume / density
- Pumping rate, displacement
- Plug bumped (Y/N)

### BHA / Bit

- BHA components and depths
- Bit run number, hours, footage
- WOB, RPM, flow rate ranges

### Personnel and HSE

- Toolbox-talk topics
- Near-misses, first-aid events, HSE incidents

## Why this matters

The DDR data structure is the bridge between **single-well drilling operations** and **multi-well analytics**. AI tender-evaluation agents (per [Papkov (2026)](../sources/papkov-2026-drilling-tender-ai-agent.md)) ingest DDR records across many offset wells to build the empirical baseline against which new bids are scored. Operator data warehouses store DDR data going back decades; the structured taxonomy makes longitudinal analysis possible.

## Public references

- **IADC Drilling Manual** — DDR template and taxonomy
- **IADC** website — public DDR-format reference and code lists
- **Bourgoyne et al.** Ch. 11

## Cross-references

- [Well Plan](well-plan.md), [AFE](afe-authorization-for-expenditure.md), [Offset Well Analysis](offset-well-analysis.md), [Drilling Tender Evaluation](drilling-tender-evaluation.md), [BHA Design](bha-design.md), [Directional Drilling](directional-drilling.md)
- [IADC Dull Grading](iadc-dull-grading.md) — Phase 1; bit-dull-grade is a DDR data field
- Founding source: [Papkov (2026)](../sources/papkov-2026-drilling-tender-ai-agent.md)
