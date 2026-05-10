---
title: "Galvanic Corrosion"
slug: galvanic-corrosion
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
tags:
  - galvanic
  - dissimilar-metals
  - area-ratio
  - galvanic-series
  - corrosion
  - offshore
sources:
  - ../standards/api-rp-571.md
  - ../standards/dnv-rp-b401.md
---

# Galvanic Corrosion

> Concept anchor for the dissimilar-metal-couple damage mechanism. Bidirectional with [api-rp-571](../standards/api-rp-571.md) (mechanism catalogue) and [dnv-rp-b401](../standards/dnv-rp-b401.md) (the protective application of the same physics — sacrificial-anode CP). Cross-references [cathodic-protection](cathodic-protection.md), [sour-service-materials](sour-service-materials.md), [damage-mechanism-screening](damage-mechanism-screening.md), [corrosion-rate-measurement](corrosion-rate-measurement.md), and [pitting-and-crevice-corrosion](pitting-and-crevice-corrosion.md).

## What is galvanic corrosion?

Galvanic corrosion is the **accelerated corrosion of the more-anodic metal** in an electrically-connected couple of dissimilar metals exposed to the same conductive electrolyte. The driver is the open-circuit potential difference between the two metals on the **galvanic series** for the operating electrolyte; the rate is then modulated by the **area ratio** of cathode to anode in the resulting electrochemical cell.

In a galvanic couple:

- The **cathodic** (more-noble) metal is **protected** — its corrosion rate falls below what it would be in isolation.
- The **anodic** (less-noble) metal corrodes **faster** than it would in isolation, because it must carry the cathodic current of both itself and its noble partner.

Galvanic corrosion is the same physics that runs sacrificial-anode cathodic protection in reverse: in CP the engineer deliberately couples a sacrificial anode to a structure to protect the structure; in unwanted galvanic corrosion the same coupling has occurred by mistake or unavoidable design constraint, with the wrong member consumed.

## Three drivers (all required)

Galvanic attack requires **all three** of the following simultaneously — break any one and the cell collapses:

1. **Potential difference** greater than roughly **50 mV** between the two metals on the galvanic series for the specific electrolyte at the operating temperature. Below ~50 mV the cell current is small enough that ordinary corrosion of each metal in isolation dominates.
2. **Electrical continuity** between the two metals — direct metal-to-metal contact, a bolted/welded joint, or a shared structural path that carries DC current. Insulating gaskets, dielectric flange kits, and isolating sleeves break this leg.
3. **Electrolyte continuity** — both metals wetted by the same conductive solution (seawater, soil, fresh water, condensate, produced water, process fluid). A dry interface or a non-conducting fluid breaks the cell. Intermittent wetting (splash-zone, condensate films, deicing-salt aerosol) is sufficient to sustain attack.

## Galvanic series in seawater

The galvanic series ranks alloys by their measured open-circuit potential against a common reference electrode in a defined electrolyte. The seawater series (Ag/AgCl reference) is the offshore-engineering baseline; the order is **electrolyte-specific** and changes meaningfully in soil, fresh water, sour brines, or hot process condensate.

| Material | Position |
|----------|----------|
| Magnesium / Mg-alloys | Anode end (sacrificial) |
| Zinc | Anode (sacrificial) |
| Aluminum + Al-alloys (active) | Anode |
| Mild steel / cast iron | Anode |
| Lead / tin | Mid |
| Brass | Mid |
| Copper / Cu-alloys | Cathode-side mid |
| Stainless 304 / 316 (passive) | Cathode |
| Titanium | Cathode |
| Graphite | Most cathodic |

Two practical caveats:

- **Active vs. passive stainless** — 304/316 sit on the cathodic side **when the passive film is intact**. In a deaerated crevice, stagnant chloride pocket, or sour brine the same alloy can shift active and become an anode in its own couple — the same mechanism that drives [pitting-and-crevice-corrosion](pitting-and-crevice-corrosion.md) feeds back into the galvanic ranking.
- **Aluminum** is amphoteric and shifts position substantially with pH and chloride activity; the Al-Zn-In sacrificial-anode alloys exploit this by holding aluminum reliably active in seawater.

## Area-ratio rule

Galvanic-cell current is fixed by the cathodic-reaction kinetics on the cathodic surface. That current is then concentrated onto the anodic surface — so the anodic-current-density (the actual driver of metal loss) scales with **cathode area / anode area**.

The controlling design rule:

- **Small anode + large cathode = catastrophic** anodic attack (high anodic current density, deep wall loss in months).
- **Large anode + small cathode = mild** attack (low anodic current density, anode loss spread thin).

Two engineering corollaries follow:

1. **Maximize anode area, minimize cathode area** in any unavoidable galvanic couple.
2. **Coat the cathode, never the anode.** Coating the anode concentrates the same cell current on the few defect sites in the coating and produces the worst-case small-anode/large-cathode geometry locally. Coating the cathode reduces total cell current and is the safe direction.

This is also why a single carbon-steel bolt in a stainless-steel flange ring fails fast, while a single stainless bolt in a carbon-steel flange ring is tolerable — the area ratio is reversed.

## Where galvanic corrosion bites in O&G

| Scenario | Mechanism |
|----------|-----------|
| Carbon-steel piping with stainless-steel valves | CS becomes the anode and accelerates near the connection; localized wall-loss within a few pipe diameters of the valve |
| Aluminum-bronze with stainless-steel bolts | Bronze becomes the anode; bolt-hole bosses lose section preferentially |
| Copper-clad heat-exchanger tubes in a steel shell | Tubesheet and tubes nominally isolated by gasket; if isolation is compromised, galvanic cell forms between Cu tubes and CS tubesheet/shell |
| Titanium tubes in a carbon-steel tubesheet | Ti is highly cathodic — CS tubesheet attacks rapidly at the tube-to-tubesheet joint; classic seawater-cooler failure mode |
| Steel rebar in marine concrete with CRA welded inserts | Rebar accelerates in the vicinity of the CRA insert; cracking and spalling around the insert |
| Subsea hot-tap into a steel pipeline with an Inconel manifold | Steel pipeline is the anode adjacent to an Inconel cathode; localized pipeline-wall loss at the tap |

These scenarios are all variations of the same theme: an unavoidable join between a structural carbon-steel substrate and a corrosion-resistant fitting, with seawater or produced fluid completing the cell. The mitigation menu below is then chosen against the constraints of each case.

## Mitigation

The mitigation hierarchy follows the three-driver model — break any leg of the cell:

- **Dielectric isolation** — isolating gaskets, dielectric flange kits, insulating sleeves and washers, non-conductive bushings, and isolating spool pieces. Breaks **electrical continuity** while leaving the joint mechanically intact. Verified by isolation-resistance testing on commissioning and periodically thereafter.
- **Area-ratio reversal** — design with a **small cathode, large anode**. Use CRA only where indispensable (e.g. trim of a carbon-steel valve), keep CRA surface area minimized, and oversize the carbon-steel side so the local anodic current density stays low.
- **Coating discipline** — **coat the cathode, never the anode**. If both sides must be coated, coat both fully; never asymmetrically.
- **Cathodic protection** — couple the most-anodic structural metal to a still-more-anodic sacrificial anode (Al-Zn-In, Zn, Mg) so the structure is driven cathodic relative to its galvanic neighbours and the cell current is supplied by the deliberately-sized anode. This is the protective inversion of the same physics — see [cathodic-protection](cathodic-protection.md) and [dnv-rp-b401](../standards/dnv-rp-b401.md).
- **Material substitution** — use the **same alloy throughout** where economically feasible (e.g. all-316 trim in a small instrument-tubing run; all-CRA bolting on a CRA flange). Eliminates the potential difference entirely.
- **Lining and barrier liners** — internal weld-overlay or clad layer on the carbon-steel side of an unavoidable couple removes electrolyte contact at the anode surface.

Selection is constrained by service temperature, mechanical loading, the availability of a power supply (for ICCP), and inspection access — no single mitigation works everywhere.

## Standards

- [api-rp-571](../standards/api-rp-571.md) — *Damage Mechanisms Affecting Fixed Equipment in the Refining Industry.* Mechanism catalogue; galvanic corrosion is covered as a discrete damage mechanism with affected materials, critical factors, and inspection guidance. Anchor reference for refinery and downstream-plant screening.
- [dnv-rp-b401](../standards/dnv-rp-b401.md) — *Cathodic Protection Design.* The protective application of the same physics — anode-area sizing, alloy capacity, and zone current densities for offshore galvanic-anode systems. Cross-referenced from this page because every CP design is also an explicit galvanic-corrosion design (the engineer chooses which metal corrodes).

- [nace-34103](../standards/nace-34103.md) — *AMPP / NACE Publication 34103: Refinery Crude Unit Practical Damage Mechanisms.* Refinery-side mechanism reference that catalogues galvanic-corrosion scenarios alongside naphthenic-acid and HCl/Cl-corrosion at crude-unit dissimilar-metal joints (CRA trim in CS pipework, Inconel weld overlays in CS shells); complements the offshore-CRA-couple framing in API-RP-571.

Adjacent standards (flagged for future ingest as the corpus grows):

- **ASTM G71** — *Standard Guide for Conducting and Evaluating Galvanic Corrosion Tests in Electrolytes.* Couple-test protocol for ranking candidate material pairs in a project-specific electrolyte.
- **ASTM G82** — *Standard Guide for Development and Use of a Galvanic Series for Predicting Galvanic Corrosion Performance.* Classification framework for translating galvanic-couple test results into engineering rankings.
- **ISO 12473** — *General principles of cathodic protection in seawater.* International parallel to DNV-RP-B401 for marine galvanic-anode CP.

## Related concepts

- [cathodic-protection](cathodic-protection.md) — sacrificial-anode CP is the protective application of the same galvanic-cell physics; a galvanic-corrosion design and a CP design are mirror images of each other.
- [sour-service-materials](sour-service-materials.md) — galvanic interactions in H2S-containing service are complicated by the active-vs-passive shift of stainless and Ni-base alloys; the seawater galvanic series is not a safe proxy for sour brine.
- [damage-mechanism-screening](damage-mechanism-screening.md) — galvanic corrosion is one of the screened mechanisms in API-RP-571 walk-throughs; presence of dissimilar-metal joints in wetted service is the trigger.
- [corrosion-rate-measurement](corrosion-rate-measurement.md) — anode-loss rate is the operational metric that confirms a galvanic-corrosion design is performing as expected; departure from the design budget is the early-warning signal.
- [pitting-and-crevice-corrosion](pitting-and-crevice-corrosion.md) — galvanic effects amplify pitting on the anodic side of a couple, because the anodic surface carries the entire cell's cathodic current density and any local passive-film breakdown sees a much higher driving voltage than it would in isolation.

## Source materials

- [og-standards-api](../sources/og-standards-api.md) — parent source page for the API slice of the local catalog; anchors the API-RP-571 mechanism-catalogue reference used in this concept.
- [og-standards-dnv](../sources/og-standards-dnv.md) — parent source page for the DNV slice; anchors the DNV-RP-B401 CP-design reference used in this concept.
