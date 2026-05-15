---
title: "ESP Vendor Archetypes"
tags: [esp, vendor, schlumberger-reda, baker-hughes-centrilift, borets, wood-group-esp]
sources:
  - api-rp-11s
added: 2026-05-14
last_updated: 2026-05-14
---

# ESP Vendor Archetypes

## Scope

The major ESP-system vendors operating globally as of mid-2020s. Vendor identity matters operationally because ESP-system component compatibility (motor / seal / pump / cable / VFD) is dominantly within-vendor; cross-vendor mixing is rare and adds qualification complexity.

## Major vendors

### Schlumberger REDA

Historically the dominant vendor (REDA = Russian Electric Dynamics Associates, original brand founded 1928; acquired by Schlumberger 1998 / now SLB). Strong global service footprint. Branded ESP-system + monitoring (e.g., InTouch).

### Baker Hughes Centrilift

Long-standing #2 globally; merged Centrilift acquisitions with their own ESP line. Acquired Wood Group ESP in 2017 (consolidating the #3 player). Dual-line offering covers low-cost commodity through HPHT specialty.

### Borets

Russian / Eurasian ESP manufacturer; significant share in Russia, CIS, Latin America. Lower-cost-per-stage than Schlumberger/Baker Hughes; competing for price-sensitive operators.

### Wood Group ESP (acquired by Baker Hughes 2017)

Pre-acquisition Wood Group ESP was the #3 global player. Now integrated into Baker Hughes Centrilift product line.

### Specialty vendors

- **Halliburton** — limited ESP presence (their artificial-lift focus is more on rod pump + gas lift)
- **NOV / Robbins & Myers** — small footprint
- **Regional vendors** — China-based (Shengli, etc.) for domestic market

## Operational implications of vendor selection

- **Service footprint** — does the vendor have service-center coverage in the operating region? Drives mean-time-to-restore on workover
- **Component compatibility** — mixing vendor parts during workover is technically possible but voids most vendor warranties + complicates failure-attribution
- **VFD and monitoring stack** — surface VFD + telemetry-software-stack is vendor-specific; switching vendors means operator IT changes
- **Spec sheet documentation** — vendor catalog completeness varies; some are exhaustively documented (Schlumberger REDA), others are sparser

## Public references

- **Takacs 2017** ESP Manual — vendor-neutral methodology references
- **Vendor catalog pages** — operators consume directly from vendor IR / product pages (not republished into this CC-BY-4.0 wiki per the vendor-marketing deny-list)
- **SPE OnePetro vendor papers** — published vendor case-study papers are citable as primary sources

## Cross-references

- [Electric Submersible Pumps](electric-submersible-pumps.md), [ESP Sizing](esp-sizing.md), [ESP Failure Modes](esp-failure-modes.md)
- [Artificial Lift Overview](artificial-lift-overview.md)
