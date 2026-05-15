---
title: "Gas Lift Valve Spacing"
tags: [gas-lift, valve-spacing, kickoff, unloading, brown-camp, depth-design]
sources:
  - api-rp-11v6
added: 2026-05-14
last_updated: 2026-05-14
---

# Gas Lift Valve Spacing

## Scope

The engineering calculation that determines at what depth each gas-lift valve sits in the tubing string. Spacing must allow staged unloading from surface to the deepest operating valve — each higher valve unloads a tubing-volume slug, lifting the kill-fluid column off the next-lower valve so that gas can transfer to a deeper injection point.

## Kickoff sequence (unloading)

1. Well is killed with brine before installing gas-lift; tubing is full of dead fluid (kill-weight density)
2. Gas injection starts at full surface pressure
3. **Top valve** opens first (its opening pressure is the lowest by design)
4. Gas enters tubing through top valve; aerates the fluid column above
5. Fluid level drops below top valve; gas continues to enter
6. Pressure at next valve down drops below its opening threshold → **second valve** opens
7. Sequence cascades down the string until the **operating valve** at design depth is reached
8. Top and intermediate valves close as their operating pressures are no longer met
9. Continuous-flow lift begins from the operating valve only

## Brown-Camp method

The classic graphical spacing method named after Brown and Camp. Pressures plotted vs depth: kill-fluid gradient line, injection-gas pressure line, design tubing-pressure line. Valve depths are placed where these lines intersect with appropriate design margins.

## Modern computer methods

Spacing is now computed numerically by commercial software (Halliburton ValCalc, Schlumberger PerformLink, Weatherford WellCare). Output: a depth-versus-valve-pressure table for the wireline crew installing the valves.

## Design factors

- **Tubing fluid gradient** — water cut sets bulk density
- **Reservoir productivity** — sets the operating-valve depth target
- **Available surface injection pressure** — typically 700-1,400 psi for older wells, up to 3,000+ psi for modern HPHT
- **Bellows-charge temperature correction** — bellows pressure shifts with downhole temperature
- **Unloading safety margins** — typically 25-50 psi between successive valve opening pressures

## Cross-references

- [Gas Lift Overview](gas-lift-overview.md), [Gas Lift Valve Design](gas-lift-valve-design.md), [Gas Lift Troubleshooting](gas-lift-troubleshooting.md)
- [API RP 11V6](../standards/api-rp-11v6.md)

## Public references

- **Brown, Kermit E.** *Technology of Artificial Lift Methods*, Vol 1 (1977) — valve-spacing methodology origin
- **Takacs 2005** *Gas Lift Manual* — modern computational treatment
- **API RP 11V6** — design framework
