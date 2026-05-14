---
title: "Well Intervention Methods"
tags: [well-intervention, coiled-tubing, wireline, snubbing, hwu, workover]
sources:
  - api-rp-5c7
added: 2026-05-13
last_updated: 2026-05-13
---

# Well Intervention Methods

## Scope

Post-completion wellbore-access methods for production-well maintenance, repair, stimulation, or workover. The choice between methods is bid-evaluation-relevant; each has cost / time / risk trade-offs.

## The four primary methods

### Coiled tubing (CT)

- See [coiled-tubing-overview.md](coiled-tubing-overview.md)
- Live-well operations under pressure
- Fast trip times; continuous tubing
- Limited tensile capacity (rated by CT grade × wall thickness)

### Wireline / slickline

- See [wireline-overview.md](wireline-overview.md)
- Smaller-OD cable; lowest cost
- Limited to applications not requiring fluid circulation
- Live-well capable via pressure-control equipment

### Snubbing

- Hydraulic snubbing unit — pulls and pushes jointed pipe under wellbore pressure
- Used for live-well jointed-pipe operations (heavier than CT)
- Slower trip times than CT but higher tensile capacity

### Hydraulic Workover Unit (HWU)

- Larger snubbing-style unit; intermediate between snubbing and a drilling rig
- Used for major intervention requiring full workover-string deployment under pressure
- Higher capacity than snubbing; lower cost than mobilizing a drilling rig

## Selection matrix

| Driver | CT | Wireline | Snubbing | HWU |
|---|---|---|---|---|
| Cost / day | low-moderate | lowest | moderate | high |
| Tensile capacity | low | very low | high | very high |
| Circulation capable | yes | no | yes | yes |
| Live-well pressure | yes | yes (with PCE) | yes | yes |
| Tool conveyance | yes | yes | yes | yes |
| Speed | fast | fastest | slow | slow |

## Why this matters for tender evaluation

Operators tender well-intervention work as separate scopes from drilling. Bidder method selection (proposing CT when wireline would suffice, or proposing wireline when snubbing is needed) flags non-compliance. The [Papkov AI tender-evaluation agent](../sources/papkov-2026-drilling-tender-ai-agent.md) would evaluate method-vs-scope match.

## Public references

- **API RP 5C7** — [api-rp-5c7.md](../standards/api-rp-5c7.md)
- **Robello Samuel** *Drilling Engineering* — intervention chapter
- **Lyons handbook** — well-intervention section

## Cross-references

- [Coiled Tubing Overview](coiled-tubing-overview.md), [Wireline Overview](wireline-overview.md), [MWD/LWD Overview](mwd-lwd-overview.md)
