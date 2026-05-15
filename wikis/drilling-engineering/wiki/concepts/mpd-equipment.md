---
title: "MPD Equipment"
tags: [mpd, rcd, rotating-control-device, choke-manifold, back-pressure-pump, automated-choke]
sources:
  - api-rp-92m
added: 2026-05-14
last_updated: 2026-05-14
---

# MPD Equipment

## Scope

The surface and near-surface equipment required for Managed Pressure Drilling operations beyond conventional drilling-rig infrastructure. The rotating control device (RCD) is the load-bearing primary element; the choke manifold + back-pressure pump + control system form the integrated MPD package.

## Rotating Control Device (RCD)

- Sits above the BOP stack; provides a sealed annular barrier around the drill string while it rotates
- **Dual seal** — primary + secondary elastomeric sealing elements
- **Bearing assembly** — supports the drill-string passing through under rotation
- **Compatible with conventional BOP** — installed on top; BOP remains primary well-control
- Operates at low to moderate working pressure (typically up to 1,500 psi for surface RCD; higher for deepwater RCD)

## Choke manifold

- High-pressure choke skid in the returns flow line
- Single or dual chokes (redundant)
- **Automated chokes** — position-controlled by MPD control system in real time
- Pressure transducers + flow meters provide feedback for closed-loop control

## Back-pressure pump

- Small high-pressure pump that injects fluid into the returns line to maintain BHP during pipe connections
- **Critical during connections** — when the rig mud pump is ramped down for a connection, the back-pressure pump replaces the friction-pressure contribution that the mud pump was providing
- Sized at ~10-30% of mud-pump rate
- Connection events become BHP-stable rather than BHP-cycling

## Control system

- Closed-loop PLC or specialty controller
- Inputs: pressure transducers (standpipe, choke, returns), flow meters, mud-pump rate, RCD bearing temperature
- Outputs: choke position commands, back-pressure pump rate commands, alarms
- Modern systems: real-time BHP estimation + adjustment within sub-second response time

## Vendors named in industry

(Vendor identity informational; no proprietary content transcribed)

- Weatherford Secure Drilling
- Halliburton GeoBalance
- Schlumberger DRILTRONICS / @balance
- Beyond Energy MPD systems

## Cross-references

- [Managed Pressure Drilling](managed-pressure-drilling.md), [Dual-Gradient Drilling](dual-gradient-drilling.md), [Underbalanced Drilling](underbalanced-drilling.md), [UBD Fluid Types](ubd-fluid-types.md)
- [API RP 92M](../standards/api-rp-92m.md)
- Phase 2 cross-ref: [BOP Stack Overview](bop-stack-overview.md) — MPD RCD is installed above the BOP; BOP remains primary well-control

## Public references

- **API RP 92M**
- **Rehm et al.** *Managed Pressure Drilling* (2008)
- **IADC UBO/MPD Committee** publications
