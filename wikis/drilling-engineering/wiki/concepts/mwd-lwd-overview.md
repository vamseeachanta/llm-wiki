---
title: "MWD / LWD Overview"
tags: [mwd, lwd, measurement-while-drilling, logging-while-drilling, mud-pulse-telemetry, real-time]
sources:
  - api-rp-7l
added: 2026-05-13
last_updated: 2026-05-13
---

# MWD / LWD Overview

## Scope

MWD (Measurement While Drilling) and LWD (Logging While Drilling) — downhole instrumentation that measures directional / formation data **during** drilling, transmitting to surface via mud-pulse telemetry (or wired drill pipe in advanced rigs). Replaces or augments traditional wireline logging in many wells.

## MWD vs LWD distinction

- **MWD** — directional and drilling-mechanics measurements: inclination, azimuth, toolface, drilling-vibration, weight-on-bit, torque-on-bit
- **LWD** — formation-evaluation measurements: gamma ray, resistivity, density, neutron, sonic, image logs

In practice the two are integrated in modern BHAs — same tool string carries both.

## Mud-pulse telemetry

The standard transmission mechanism: a downhole modulator generates pressure pulses in the mud column that propagate to surface and are decoded at the standpipe. Bandwidth-limited (typically < 40 bps); critical real-time data is prioritized.

Higher-bandwidth alternatives:
- **Electromagnetic (EM) telemetry** — through-formation low-frequency RF; works in air / underbalanced drilling
- **Wired drill pipe (Intellipipe)** — multi-Mbps; specialty service; not standard

## Real-time vs memory data

- **Real-time** — transmitted via mud pulse, displayed at surface during drilling
- **Memory** — recorded in tool memory, dumped at surface after trip
- Memory data typically has higher resolution; real-time used for steering and drilling decisions

## Connection to AI tender evaluation

MWD/LWD data is the real-time drilling record. A [Papkov-style AI tender-evaluation agent](../sources/papkov-2026-drilling-tender-ai-agent.md) consuming offset-well data should ingest LWD logs and MWD drilling-mechanics records — the empirical record of how previous bidders' equipment performed in this formation. LWD-quality differences between bidders (resolution, sensor count) are bid-evaluation dimensions.

## Public references

- **API RP 7L** — [api-rp-7l.md](../standards/api-rp-7l.md)
- **Bourgoyne et al.** Ch. 9
- **Robello Samuel** *Drilling Engineering* — MWD/LWD chapter

## Cross-references

- [Wireline Overview](wireline-overview.md), [Coiled Tubing Overview](coiled-tubing-overview.md), [Formation Evaluation Basics](formation-evaluation-basics.md), [Well Intervention Methods](well-intervention-methods.md)
- Founding source: [Papkov (2026)](../sources/papkov-2026-drilling-tender-ai-agent.md)
