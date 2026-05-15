---
title: "Managed Pressure Drilling (MPD)"
tags: [mpd, managed-pressure-drilling, rcd, closed-loop, narrow-window, cbhp]
sources:
  - api-rp-92m
added: 2026-05-14
last_updated: 2026-05-14
---

# Managed Pressure Drilling (MPD)

## Scope

Managed Pressure Drilling is an adaptive closed-loop drilling method that maintains precise bottomhole pressure (BHP) within a narrow tolerance using a rotating control device (RCD) + surface-choke manifold + back-pressure pump. MPD enables drilling wells where the pore-pressure-to-fracture-pressure window is too narrow for conventional overbalanced drilling — typical deepwater, HPHT, and depleted-reservoir applications.

## IADC 4-category classification (per API RP 92M)

### 1. Constant Bottomhole Pressure (CBHP)

Most common MPD variant. Surface back-pressure pump + choke maintain BHP at a fixed setpoint (e.g., pore pressure + 50-100 psi). Adjusts in real time to mud-pump rate variation, connection events, and trip operations.

### 2. Pressurized Mud Cap Drilling (PMCD)

For severe-lost-circulation zones (vugs, fractured carbonates). A pressurized mud cap sits above a sacrificial-fluid column; drilling proceeds with continuous loss but contained at surface pressure. Common in Middle East carbonate plays.

### 3. Dual Gradient

Two distinct fluid gradients — heavier mud below seafloor, seawater (or lighter fluid) above. Enables drilling deepwater wells where conventional single-gradient riser drilling exceeds fracture pressure at shallow casing shoes. See [Dual-Gradient Drilling](dual-gradient-drilling.md).

### 4. Returns Flow Control

Basic closed-loop without active BHP setpoint. Surface monitors flow returns; alerts on kick / loss but doesn't actively maintain BHP. Intermediate complexity between conventional and full CBHP.

## Operational sequence

1. Set up RCD at top of drill string above the wellhead
2. Configure choke manifold + back-pressure pump
3. Start circulation; choke maintains target BHP
4. As mud-pump rate changes (drilling, connecting), choke adjusts in real time
5. Connection events: ramp pump down → close choke → back-pressure pump maintains BHP across connection → reopen choke → ramp pump up

## Cross-references

- [MPD Equipment](mpd-equipment.md), [Dual-Gradient Drilling](dual-gradient-drilling.md), [Underbalanced Drilling](underbalanced-drilling.md), [UBD Fluid Types](ubd-fluid-types.md)
- [API RP 92M](../standards/api-rp-92m.md)
- Phase 2: [Well-Control Methods](well-control-methods.md), [ECD and Pressure Management](ecd-and-pressure-management.md), [BOP Stack Overview](bop-stack-overview.md)

## Public references

- **API RP 92M** — [api-rp-92m.md](../standards/api-rp-92m.md)
- **Rehm et al.** *Managed Pressure Drilling*, Gulf Publishing 2008 (ISBN 978-1-933762-24-1)
- **IADC UBO/MPD Committee** publications + classifications
- **SPE / IADC MPD Conference & Exhibition** OnePetro paper library
