---
title: "Kick Detection"
tags: [kick, pit-gain, flow-show, drill-break, well-control, early-warning]
sources:
  - api-rp-53
added: 2026-05-13
last_updated: 2026-05-13
---

# Kick Detection

## Scope

The early-warning signatures of formation-fluid influx (a "kick") into the wellbore. Early detection is the most-leveraged operational variable in well control — a small kick caught immediately is a routine event; an undetected kick that migrates to surface is a blowout.

## Primary detection signatures

### Flow-show / pit gain

Most reliable. Active mud pit volume increases without operator-initiated addition — the volume increase is formation fluid pushing mud out of the well into the pits. Modern rigs alarm on pit-volume gain > 5-10 bbl.

### Drilling break

Sudden increase in rate of penetration (ROP) suggesting the bit has entered a higher-pressure, lower-strength formation. Drilling break itself isn't a kick — but it's the warning to monitor for pit gain.

### Flow with pumps off

When mud pumps are off (e.g., during a connection), any continuing return flow from the well = kick. Routine "flow check" at every connection is procedure-mandated.

### Mud-gas log

Continuous gas chromatograph on the return mud line. Gas spikes signal gas-bearing formation; combined with other signs, confirms a kick.

### Pump-pressure / SPP changes

Standpipe pressure (SPP) decrease at constant pump rate suggests lighter formation fluid lifting the column ahead of the pumps. Slower-developing signal.

## Detection latency

- **Routine pit-gain alarm** — detects 5-10 bbl gain (most kicks caught here)
- **Drilling break + flow-check** — depends on driller vigilance; 1-3 minute lag
- **Mud-gas log** — depends on lag time (cuttings transport up the annulus); 10-30 minutes for a deep well

## After detection

Kick detection triggers immediate **shut-in procedures** — see [shut-in-procedures.md](shut-in-procedures.md). Once shut in, [well-control methods](well-control-methods.md) determine how to kill the kick.

## Public references

- **API RP 53** — [api-rp-53.md](../standards/api-rp-53.md)
- **IADC WellCAP curriculum**
- **Bourgoyne et al.** Ch. 4

## Cross-references

- [Shut-In Procedures](shut-in-procedures.md), [Well-Control Methods](well-control-methods.md), [BOP Stack Overview](bop-stack-overview.md)
