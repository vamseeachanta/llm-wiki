---
title: "Lower Marine Riser Package (LMRP)"
tags: [lmrp, emergency-disconnect, eds, hydraulic-pod, mux-pod, subsea-bop]
sources:
  - api-spec-16f
  - api-spec-16a
added: 2026-05-14
last_updated: 2026-05-14
---

# Lower Marine Riser Package (LMRP)

## Scope

The LMRP is the upper portion of the subsea BOP stack — it carries the upper annular preventer, the hydraulic / MUX control pods that operate the lower BOP stack, and the disconnect plane where the riser can be detached from the wellhead-mounted lower stack during emergency operations. **LMRP design IS the load-bearing element for emergency-disconnect-sequence (EDS) reliability**.

## LMRP components

1. **Upper annular preventer** — top of LMRP; can seal around drill string before disconnect
2. **Riser connector** — top connection to the riser stack-up
3. **Hydraulic / MUX control pods** — dual-redundant pods that operate the lower BOP via piped hydraulic lines down through the disconnect plane
4. **Choke / kill / booster line stubs** — interface with the auxiliary lines from the riser
5. **Wellhead connector (BOP-side)** — bottom connection that latches onto the lower BOP stack via the disconnect plane

## Emergency disconnect sequence (EDS)

When the vessel must abandon location urgently (e.g., dynamic-positioning failure, hurricane, fire):

1. **Close pipe rams** — seals around drill string in the lower BOP
2. **Shear pipe** — if drill pipe must be cut to allow disconnect (blind-shear rams)
3. **Vent LMRP hydraulics** — releases the connector that holds LMRP to lower stack
4. **Lift riser** — vessel moves off station; riser comes up with LMRP attached
5. **Hang LMRP** — riser + LMRP either reeled onto the rig or moored off; lower BOP stays on wellhead sealing the well

The EDS sequence is timed in **seconds** for fast-developing emergencies. Modern MUX systems can complete a full EDS in 30-60 seconds from trigger.

## Dual-redundant pods

The two control pods (typically Pod A + Pod B) provide redundancy — if one fails or is contaminated, the other operates the same hydraulic functions independently. Both pods sit in the LMRP and disconnect with it; the lower BOP retains its accumulator capacity to hold rams closed without external pod support for a documented duration (per API Spec 16D).

## Public references

- **API Spec 16A** — [api-spec-16a.md](../standards/api-spec-16a.md). BOP-stack including LMRP.
- **API Spec 16D** — [api-spec-16d.md](../standards/api-spec-16d.md). Control systems.
- **API Spec 16F** — [api-spec-16f.md](../standards/api-spec-16f.md). Riser-side interface.
- **API RP 16Q** — [api-rp-16q.md](../standards/api-rp-16q.md). EDS framework.

## Cross-references

- [Marine Drilling Riser Overview](marine-drilling-riser-overview.md), [Riser Tensioning](riser-tensioning.md), [Subsea Wellhead](subsea-wellhead.md), [Subsea BOP Stack Architecture](subsea-bop-stack-architecture.md)
- Phase 2 cross-refs: [BOP Stack Overview](bop-stack-overview.md), [BOP Control Systems](bop-control-systems.md)
