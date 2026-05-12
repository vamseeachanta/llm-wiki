---
title: "Tug Working-End Fendering"
tags: [tug-operations, fendering, port-operations, vessel-freeboard, hull-geometry, tug-design, harbour-towage]
sources:
  - linkedin-lloyds-maritime-institute-2026-tug-fender-height
added: 2026-05-12
last_updated: 2026-05-12
see_also:
  - concepts/lng-berth-operability.md
  - concepts/motions-rao.md
  - concepts/stability-in-waves.md
---

# Tug Working-End Fendering

## Scope

This page synthesises the design considerations for the **working-end fender** of a harbour or escort tug — the part of the tug that contacts the assisted vessel when pushing or transmitting line forces. It is the concept-side anchor for the [Lloyd's Maritime Institute (2026)](../sources/lloyds-maritime-institute-2026-tug-fender-height-discussion.md) training discussion prompt. It treats the engineering drivers and constraints at a synthesis level; it does **not** restate clauses, tables, or sizing formulae from PIANC, BSI, OCIMF, or class-society rules — those are deferred to the listed public references.

## Working-end definition by tug type

The "working end" is not the same end of the tug for all propulsion arrangements:

| Tug type | Typical working end | Why |
|---|---|---|
| Conventional (single- or twin-screw, forward-set wheelhouse) | Bow | Tug pushes with its bow fender and tows from the after-deck. |
| ASD (azimuth stern drive) / Z-drive | Often stern, sometimes bow | ASD tugs can operate stern-first or bow-first; staple/towing point and the corresponding working-end fender depend on the operating mode (direct-pulling, escort indirect, pushing). |
| Tractor (Voith Schneider, cycloidal) | Forward of amidships | Propulsion units sit under the forward half of the hull; the tow point is aft of the propulsion, and the fender face is forward. |

The post under [Lloyd's Maritime Institute (2026)](../sources/lloyds-maritime-institute-2026-tug-fender-height-discussion.md) refers generically to "the tug's working end" — in practice the height optimisation is a different exercise for each of the above arrangements.

## The freeboard-matching design driver

The dominant constraint on working-end fender height is the **freeboard band of the assisted-vessel population**. The fender face must make contact at a height that:

1. Distributes the push load over a meaningful contact patch on the assisted ship's side shell.
2. Does not contact above the vessel's freeing-port band, sheer line, or accommodation overhang.
3. Does not contact so low as to bear against the bulwark or under the rubbing strake on a low-freeboard vessel.

The freeboard span across the vessel mix in a deep-water harbour can be substantial:

| Assisted vessel state | Freeboard band (illustrative) |
|---|---|
| Tanker / bulker, laden | Lower freeboard; contact possible near or just above the boot top. |
| Container, laden | Mid freeboard. |
| Container / car carrier / RoRo, ballast | High freeboard; flare and overhang complicate contact geometry. |
| Cruise | Mid-to-high freeboard; large parallel side; topside flare aft. |
| LNG carrier, ballast (membrane or Moss) | High freeboard with limited parallel midbody. |

A tug serving a port with only one of these segments can target a narrower fender height; a tug serving a mixed-traffic port faces a wider design envelope — which is what motivates the discussion-prompt question on the source page.

## Hull-geometry considerations

The fender does not see a flat plate. Several aspects of the assisted-ship hull modify the effective contact:

- **Bow flare.** When pushing near the bow, the topside flares outward; the contact patch is on an inclined face rather than a vertical one, which biases the working-end fender contact toward the upper edge of the fender.
- **Parallel midbody.** The cleanest contact case; the height question reduces to matching the freeboard at the contact location.
- **Shoulder transitions.** Forward and after shoulders are curved; tug working-end fender face geometry that is too narrow can roll along the shoulder during a push manoeuvre, producing localised loads.
- **Stern overhang and quarter.** When pushing the quarter, the fender must avoid the stern flare and any sponsons.

## Fender face geometry

The fender face on the working end can take several forms, each with different contact behaviour:

- **Cylindrical / "bullnose" fender.** Rounded face, robust for off-axis contact.
- **Push-knee / shaped fender block.** Flat or slightly curved tall face matched to the typical contact height.
- **Wing or D-section fender.** Continuous horizontal section running across the working end.
- **Tube / pneumatic auxiliary fenders.** Sometimes carried inflatable / Yokohama-style auxiliary fenders for special vessels.
- **Stepped / multi-level arrangements.** Two or more vertically stacked faces of different heights — adopted on some modern designs to cover a wide freeboard band on the same tug.

The Lloyd's Maritime Institute post explicitly invites readers to share which arrangement they have seen perform well — confirming that the choice is not standardised across ports.

## Tug-stability constraint

A higher working-end fender enlarges the freeboard coverage but raises the **contact point** at which the push force acts on the tug. The pushing reaction couples into the tug's transverse stability:

- The fender contact line, applied through a high point on the tug, generates a roll-inducing moment when the push direction is not exactly normal.
- This moment must be carried by the tug's righting arm at the operating draft; on small or shallow-draft tugs this becomes a real limit.
- Class rules and tug-design practice cap the working-end fender height against tug stability accordingly.

This is why an arbitrary "as high as possible" fender is not the right answer to the prompt — height is bounded by tug stability as well as by assisted-ship contact geometry.

## Operational interface with vessel motion

Even with the right static fender height, the contact during a push is dynamic: the tug heaves, surges, and the assisted ship can roll and heave at low encounter frequencies. The tug working-end fender must absorb intermittent impacts as well as the steady push load — which is why fender-face material and stiffness, not only height, are part of the design. See [Motions and Response Amplitude Operators](motions-rao.md) and [Stability in Waves](stability-in-waves.md) for the motion side of the problem.

## Cross-References

- [LNG Berth Operability](lng-berth-operability.md) — operability framing for berthing, of which tug assistance is a contributor.
- [LNG Carrier Mooring](../entities/lng-carrier-mooring.md) — terminal-side counterpart to the tug-side fendering question.
- [Motions and Response Amplitude Operators](motions-rao.md) — vessel-motion context for dynamic fender contact.
- [Stability in Waves](stability-in-waves.md) — stability framing that bounds working-end fender height on the tug.

## Public references

The following are the public-citable anchors for the synthesis above. The LinkedIn trigger source is on the [Lloyd's Maritime Institute (2026)](../sources/lloyds-maritime-institute-2026-tug-fender-height-discussion.md) page and is **not** the anchor for any technical claim on this page.

- Hensen, H. (2003). *Tug Use in Port: A Practical Guide*, 2nd edition. The Nautical Institute, London. — Practitioner-standard reference covering tug types, working-end geometry, push and tow operations, and fender-arrangement considerations. (3rd edition published 2018.)
- PIANC MarCom Working Group 33 (2002). *Guidelines for the Design of Fender Systems*. PIANC, Brussels. — Engineering principles for fender selection, energy absorption, contact-area sizing, and material behaviour; the basis for most port-side fender design and the conceptual backdrop for tug-side fender selection.
- BS 6349-4:2014. *Maritime works — Part 4: Code of practice for design of fendering and mooring systems*. BSI, London. — UK code of practice covering fendering design at port and quay; provides the codified context for tug-fender interaction at the assisted-vessel side. (Named only; clauses not reproduced.)
- OCIMF (2018). *Mooring Equipment Guidelines (MEG4)*, 4th edition. Oil Companies International Marine Forum. — Industry guideline for tanker mooring including fender-face contact considerations at ship-shore interfaces. (Named only; clauses not reproduced.)
- ITS (International Tug, Salvage & OSV Convention) Proceedings — public conference papers from harbour-towage and escort-tug practitioners describing operating-mode-specific fender design choices. https://www.tugandosv.com/ .
