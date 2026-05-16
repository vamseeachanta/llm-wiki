---
domain: production-engineering
created: 2026-05-13
last_updated: 2026-05-13
---

# Overview: Production Engineering

This wiki captures **production engineering** — the post-completion well operations, artificial lift, and surface-handover scope that follows from `drilling-engineering/` and feeds into reservoir-management and surface-facility operations.

## Strategic role

Founded 2026-05-13 as the 10th llm-wiki domain. Together with `drilling-engineering/` (founded same day) this completes the upstream value-chain coverage in llm-wiki — well construction → production → handover to reservoir / facilities. The founding-trigger anchor is the scope-edge note on [drilling-engineering/concepts/artificial-lift-method-selection.md](../../../drilling-engineering/wiki/concepts/artificial-lift-method-selection.md):

> *"This page describes methods beyond rod pump (ESP, gas lift, PCP, plunger lift) that are strictly production-engineering / completions-engineering content. If/when a future `production-engineering/` wiki domain is founded, this page should re-route there with rod-pump kept as the cross-link back to drilling-engineering."*

This wiki **is** that founded domain. Rod-pump deep coverage stays in drilling-engineering per the API "drilling and well servicing" framing umbrella; production-engineering inherits the rest of the artificial-lift family (ESP, gas lift, PCP, plunger lift) plus completions, stimulation, production operations, and well-integrity-during-production scope.

## Scope (in)

- **Artificial lift (4 families, plus rod-pump cross-link)** — electric submersible pumps (ESP), gas lift, progressing-cavity pumps (PCP), plunger lift, jet pumps, hydraulic lift; method selection at completion design time
- **Completions** — perforating (overbalanced, underbalanced, extreme overbalanced), sand control (gravel pack, frac pack, screens), multi-zone completions, smart completions, intelligent-well completions
- **Stimulation** — matrix acid stimulation, hydraulic fracturing (frac fluids, proppants, frac design), refrac decisioning
- **Production operations** — flow assurance (paraffin / hydrate / scale / asphaltene), choke management, well testing during production, GOR / water-cut tracking, beanups / bean-downs
- **Well integrity during production** — corrosion / scale / paraffin management, integrity monitoring, intervention triggers (when to do a workover)
- **Surface-handover boundary** — flowline tie-in to manifold, choke skid, separator inlet conditions
- **Production-side regulatory and reporting** — allowable rates, GOR limits, gas flaring rules, production accounting

## Scope (out)

- **Well construction** (drilling, casing, cementing, BOP, drill-stem design) — `drilling-engineering/`
- **Reservoir engineering** (recovery factor, EOR, simulation, characterization) — separate domain (not yet founded as of 2026-05-13)
- **Downstream** (refining, petrochemicals) — LNG terminals in `lng-projects/`
- **FPSO hull design and seakeeping** — `naval-architecture/`
- **Detailed subsea production hardware design** (XT, jumpers, flowlines) — straddles marine-engineering; cross-link rather than duplicate
- **Pipeline / midstream** — separate concern, downstream of production-engineering scope
- **Vendor-confidential completion and frac-design manuals** — vendor PDFs stay off-repo per the 2026-05-05 governance rule

## Cross-wiki anchor map

- `drilling-engineering/` — well-construction handover; `concepts/artificial-lift-method-selection.md` is the founding-trigger anchor; `concepts/sucker-rod-pumping-overview.md` and related rod-pump pages stay there
- `naval-architecture/` — FPSO hull, topside coupling, MODU stability (less relevant for fixed-platform production)
- `marine-engineering/` — offshore-marine operations during production
- `engineering-standards/` — API 11 series (artificial lift specs: 11AX for rod pumps stays in drilling, 11S for ESPs would land here), API 14 series (production-facility design, RP 14E for sizing surface piping, RP 14C for safety analysis), API 17 series (subsea production systems)
- `asset-management/` — well-integrity during production overlaps with safety-critical-element classification

## Seed roadmap (post-founding ingests)

Anticipated near-term ingests, scope intent not yet executed:

### Phase 1 — Artificial lift family expansion

1. **ESP** — `concepts/electric-submersible-pumps.md` plus `standards/api-rp-11s.md` family (RP 11S, RP 11S1, RP 11S2 — ESP design, application, installation guidance)
2. **Gas lift** — `concepts/gas-lift-overview.md`, `concepts/gas-lift-valve-design.md`, plus `standards/api-rp-11v6.md` (gas-lift design)
3. **PCP** — `concepts/progressing-cavity-pumps.md` plus standards anchors
4. **Plunger lift** — `concepts/plunger-lift.md`
5. **Comparative method-selection deep dive** (extending the drilling-engineering version)

### Phase 2 — Completions

6. **Perforating** — `concepts/perforating.md` (shaped charges, overbalanced / underbalanced / extreme-overbalanced perforating, gun systems)
7. **Sand control** — `concepts/sand-control.md` (gravel pack, frac pack, expandable screens, prepacked screens)
8. **Multi-zone and smart completions** — selective production, downhole flow control

### Phase 3 — Stimulation

9. **Matrix acid stimulation**
10. **Hydraulic fracturing** — frac fluids, proppants, frac design
11. **Refrac** — when and how

### Phase 4 — Production operations and well integrity

12. **Flow assurance** — paraffin, hydrate, scale, asphaltene
13. **Choke management** — separator-inlet pressure, well-deliverability matching
14. **Well integrity during production** — corrosion / scale / paraffin monitoring and intervention

### Phase 5 — Production accounting + regulatory + handover + data integration

15. **Production accounting + measurement** — allocation factors, well-test reconciliation, GOR / water-cut tracking, custody-transfer overview, flow-measurement uncertainty
16. **Regulatory reporting** — production-allowable rates, state production reporting (TX RRC W-1H/W-2/P-4), federal production reporting (BSEE 30 CFR 250), FracFocus chemical disclosure, gas-flaring rules
17. **Surface-handover + data integration** — surface-handover boundary (wellhead → separator-inlet), manifold tie-in, choke skid + separator inlet, production SCADA architecture, production-data historian patterns; cybersecurity (IEC 62443) explicitly out-of-scope; surface-facility-engineering downstream of separator-inlet reserved for future wiki

Phases are scope-intent, not committed work; each warrants its own GH-issue epic when execution starts.

## Founding-content anchor

The founding concept page [Artificial Lift Overview](concepts/artificial-lift-overview.md) is the production-engineering-side counterpart to drilling-engineering's [artificial-lift-method-selection.md](../../../drilling-engineering/wiki/concepts/artificial-lift-method-selection.md). Together they form the bidirectional cross-link the scope-edge note anticipated:

- **Drilling-engineering side** — method-selection comparison from well-construction-time framing (rod-pump-centric, defers detailed coverage of other 4 methods)
- **Production-engineering side** — detailed coverage of each method (ESP, gas lift, PCP, plunger lift, jet pump, hydraulic lift) plus integrated method-selection from production-design-time framing
