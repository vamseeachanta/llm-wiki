---
title: "Mud System Equipment"
tags: [mud-system, shale-shaker, desander, desilter, mud-cleaner, centrifuge, degasser, mud-pit]
sources:
  - api-spec-13a
added: 2026-05-13
last_updated: 2026-05-13
---

# Mud System Equipment

## Scope

The surface equipment that conditions returning mud — removes drilled solids, gas, and contaminants — before recirculation to the mud pump and back down the well. The "solids-control system" is the engineering term; equipment choices and configuration drive mud-property maintenance and operating cost.

## Equipment train (in flow order from well to suction)

1. **Possum belly / flow-line** — gravity collection from the flow line entering the rig
2. **Shale shaker** — first solids removal stage; vibrating screen removes large cuttings (typically API 80-200 mesh)
3. **Degasser** — vacuum or atmospheric chamber removing entrained gas (after well-control kick or naturally-gassy mud)
4. **Desander** — 4-12" hydrocyclones removing sand-sized solids (44-74 microns)
5. **Desilter** — 4" hydrocyclones removing silt-sized solids (~10-44 microns)
6. **Mud cleaner** — desilter cones discharged onto fine shaker screen; recovers weighted barite
7. **Centrifuge** — separates fine solids (< 10 microns) from mud; primary tool for mud-weight control on weighted systems
8. **Active mud pits** — suction pit, mixing pit, reserve pit; provide volume buffering and mud-treatment workspace

## Sizing drivers

- **Total flow rate** through the system (mud-pump output)
- **Drilling rate of penetration** (cutting generation rate)
- **Hole-size and section length** (total cutting volume)
- **Mud-weight retention requirement** (weighted-mud systems need centrifuge)

## API Spec 13C — adjacent reference

API Spec 13C covers shale-shaker screen designations (API mesh number, conductance, area). Cross-referenced from [api-spec-13a.md](../standards/api-spec-13a.md) but not separately ingested.

## Public references

- **API Spec 13A** — material context
- **API Spec 13C** — shale-shaker screen designations (not separately ingested)
- **Caenn et al.** 2017 — solids-control equipment chapter
- **ASME / API SHALE-SHAKER handbook** — public practitioner reference

## Cross-references

- [Drilling-Fluid Types](drilling-fluid-types.md), [Mud Properties](mud-properties.md), [ECD and Pressure Management](ecd-and-pressure-management.md), [Hole Cleaning](hole-cleaning.md)
- [API Spec 7K](../standards/api-spec-7k.md) — mud-pump (driving the system)
