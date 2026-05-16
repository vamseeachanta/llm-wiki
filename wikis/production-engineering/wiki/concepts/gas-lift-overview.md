---
title: "Gas Lift Overview"
tags: [gas-lift, artificial-lift, continuous-flow, intermittent, valve-spacing, unloading]
sources:
  - api-rp-11v6
  - api-spec-11v1
added: 2026-05-14
last_updated: 2026-05-16
---

# Gas Lift Overview

## Scope

Gas lift uses high-pressure gas injected down the annulus, entering production tubing through gas-lift valves at controlled depths, to reduce the fluid column density. Reservoir pressure then lifts the lighter column to surface. **No moving downhole parts** — the valves themselves are the only mechanical elements, and they have long mean-time-to-failure compared with rod-string or ESP systems.

## Operating principle

1. High-pressure gas enters the casing-tubing annulus from surface compressor
2. Gas pressurizes annulus; tubing-fluid column is lighter
3. Gas-lift valves in side-pocket mandrels along the tubing string open in sequence (top to bottom) during **unloading**, then settle to a single operating valve in continuous-flow mode
4. Gas enters the tubing through the operating valve and mixes with produced fluid
5. The aerated column has lower bulk density → reservoir pressure pushes the column to surface

## Two operating modes

### Continuous-flow

- Steady gas injection through the operating valve
- Common for moderate-rate wells (200-10,000+ bbl/d)
- Operating valve at the deepest depth where the gas-pressure budget allows

### Intermittent

- Gas slug injected periodically; lifts a fluid slug; cycle repeats
- For low-rate wells (< 500 bbl/d) where continuous-flow can't sustain stable lift
- Cycle time per well typically 10-90 minutes

## Strengths and weaknesses

| Strength | Weakness |
|---|---|
| No moving downhole parts | Requires high-pressure gas source + surface compression |
| Excellent gas-handling tolerance (intake gas is a non-issue) | Lower efficiency at very-low rate |
| Works in deviated and horizontal wells | Gas-lift valve workovers when valves fail (less frequent than ESP) |
| Long mean-time-to-failure | Multipointing / heading instabilities require diagnosis |
| Depth effectively unlimited (subject to gas-pressure budget) | Operationally more sensitive than rod-pump for unstable wells |

## Multi-zone gas-lift — independent zonal injection vs commingled lift-gas distribution

When a gas-lifted well has a multi-zone or selective completion architecture (see [Multi-Zone Completions](multi-zone-completions.md)), the gas-lift design must be tuned to the zonal-isolation arrangement. Two structurally distinct architectures emerge:

### Commingled lift-gas distribution

In a commingled multi-zone completion, all zones produce into a common production stream and the gas-lift system services the aggregate flow. The operating-valve depth is set against the IPR of the aggregated multi-zone inflow; per-zone gas-lift tuning is not possible. Strengths: lowest first cost, simplest operation. Weaknesses: when one zone develops different fluid properties (water cut, GOR, gradient) the gas-lift design optimized for the original aggregate IPR may become poorly tuned.

### Independent zonal gas-lift injection

In selective completions with downhole flow control (see [Downhole Flow Control](downhole-flow-control.md)), each zone may have its own gas-lift mandrel and operating valve, allowing gas-injection rate and depth to be tuned per zone. This is most common in:

- **Stacked-pay reservoirs** with distinct fluid types per zone, where shared gas-lift design would be a poor compromise.
- **Smart-completion architectures** ([Intelligent-Well Completions](intelligent-well-completions.md)) where remotely-actuated ICVs can be combined with zone-by-zone gas-lift tuning to enable closed-loop reservoir management.

Operational discipline:

- Per-zone unloading sequences are more complex than single-zone unloading; the order of valve openings across zones must be planned to avoid surface-equipment overload.
- Crossflow risk on shut-in is elevated (gas can flow from a higher-pressure zone's annulus to a lower-pressure zone's tubing); shut-in procedures must include zone-isolation steps.
- Multi-zone gas-lift wells benefit disproportionately from downhole monitoring (per-zone PT gauges) because surface measurement alone cannot resolve per-zone gas-lift performance.

| Aspect | Commingled lift-gas | Independent zonal injection |
|---|---|---|
| First cost | Lowest | Higher (per-zone valves, mandrels, control hardware) |
| Reservoir-management granularity | Aggregate only | Per-zone |
| Surveillance requirement | Surface-only sufficient | Downhole monitoring strongly recommended |
| Best fit | Compatible-zone stacked completions | Heterogeneous-zone or smart completions |

See [Multi-Zone Completions](multi-zone-completions.md) for the full architectural overview.

## IPR coupling — perforation strategy interaction

Gas-lift design depends on the **IPR curve** (inflow-performance relationship) of the producing interval — kickoff procedure, operating-valve depth, and gas-injection rate are all set against the IPR shape. When IPR is dominated by **perforation skin**, gas-lift design is effectively sized to the perforation policy upstream of completion:

- A well with high perforation skin (low shot density, OBP without acid cleanup, short EHL relative to damage radius) presents a stiff IPR — gas lift has to fight a steep pressure drawdown for low rate gain.
- Re-perforation as a workover intervention can transform an under-performing gas-lift well's economics; modelling the post-re-perforation IPR drives the workover business case.
- Re-orienting an existing gas-lift design after a re-perforation campaign typically means re-spacing valves to take advantage of the new IPR — Brown-Camp re-design from the new operating envelope.

See [Perforation Strategy](perforation-strategy.md) for the shot-density / phasing / EHL framework that sets the IPR floor.

## Hydrate formation in marginal injection-gas dehydration

Gas-lift operations depend on a high-pressure injection-gas stream delivered down the annulus. When the injection-gas dehydration is **marginal** (the gas-export dehydration system is operating off-target, or the injection-gas slipstream is taken upstream of the dehydration train), residual water in the injection gas can drive hydrate formation in two operationally-distinct locations:

- **Inside the gas-lift valves** — the valve body and orifice operate at a pressure-drop point that produces Joule-Thomson cooling of the injection gas as it expands from annulus pressure to tubing pressure. The combination of cooling at the orifice and any residual free water in the injection gas can produce hydrate at the valve, plugging the orifice and disabling the valve. The plug typically clears once injection is stopped and the well warms up, but the operational disruption is significant.
- **In the tubing immediately above the gas-lift mandrel** — once injection gas mixes into the tubing column, cooler tubing temperature above the operating-valve depth can drive hydrate formation if free water is present in either the produced fluid or the injection gas.

Mitigation strategies overlap with the broader hydrate-management toolkit (see [Hydrate Management](hydrate-management.md)): improve injection-gas dehydration (raise glycol-contactor or molecular-sieve performance to keep injection-gas water content below the no-hydrate threshold across the operating temperature range), or apply methanol or MEG injection at the injection-gas distribution point.

Cross-link: see [Flow Assurance](flow-assurance.md) for the integrated thermal-hydraulic-chemical envelope and [Hydrate Management](hydrate-management.md) for the THI / LDHI prevention framework.

## Choke coordination on injection-gas side

Gas-lifted wells operate two distinct choke surfaces simultaneously: the production choke on the wellhead (controlling produced-fluid rate to the separator per [Choke Management](choke-management.md)) and the gas-injection choke on the surface-compressor discharge line (controlling lift-gas injection rate to the casing-tubing annulus). The two chokes must be coordinated:

- **Steady-state operating point** — gas-injection rate sets the operating valve depth's pressure-budget envelope; produced-fluid rate is then a function of the IPR / TPR / production-choke intersection. Both chokes are tuned together against the well's gas-lift performance curve.
- **Bean-up coordination** — during well startup the gas-injection choke must be opened to establish unloading flow before the production choke is opened to send produced fluid through the separator. Coordinated bean-up sequencing avoids unloading-instability (heading) and avoids transient surface-equipment overload.
- **ESD interlock** — on facility ESD per [API RP 14C](../standards/api-rp-14c.md), both the production choke and the gas-injection choke participate in the coordinated shutdown sequence. The gas-injection valve closes to stop lift-gas supply; the production choke biases toward closure; the SSV closes; tree valves close.
- **Multi-zone gas-lift wells** — for independent zonal gas-lift injection (see the Multi-zone gas-lift section above), each zone's gas-injection choke must be coordinated with the production choke and with the other zones' injection chokes; multi-zone surface-control logic becomes a coordinated multi-axis control problem.

See [Choke Management](choke-management.md) for the production-choke operational discipline router and [Choke Types](choke-types.md) for the architecture-family framework that informs gas-injection choke selection (typically severe-service cage chokes given the high differential pressure across the surface-compressor-to-annulus piping).

## Cross-references

- [Gas Lift Valve Design](gas-lift-valve-design.md), [Gas Lift Valve Spacing](gas-lift-valve-spacing.md), [Gas Lift Troubleshooting](gas-lift-troubleshooting.md)
- [Artificial Lift Overview](artificial-lift-overview.md)
- [Perforation Strategy](perforation-strategy.md) — IPR coupling
- [Multi-Zone Completions](multi-zone-completions.md), [Downhole Flow Control](downhole-flow-control.md), [Intelligent-Well Completions](intelligent-well-completions.md) — multi-zone gas-lift coupling
- [Flow Assurance](flow-assurance.md), [Hydrate Management](hydrate-management.md) — injection-gas dehydration / hydrate-formation coupling
- [Choke Management](choke-management.md), [Choke Types](choke-types.md), [API RP 14C](../standards/api-rp-14c.md) — production-choke and injection-choke coordination, ESD interlocking
- [API RP 11V6](../standards/api-rp-11v6.md), [API RP 11V2](../standards/api-rp-11v2.md), [API Spec 11V1](../standards/api-spec-11v1.md)
- Drilling-engineering cross-link: [Artificial-Lift Method Selection](../../../drilling-engineering/wiki/concepts/artificial-lift-method-selection.md)

## Public references

- **Takacs, Gabor** — *Gas Lift Manual*, PennWell 2005 (ISBN 0-87814-805-1)
- **Brown, Kermit E.** — *The Technology of Artificial Lift Methods*, Vol 1 PennWell 1977
- **API RP 11V6** — design reference
- **SPE OnePetro gas-lift literature**
