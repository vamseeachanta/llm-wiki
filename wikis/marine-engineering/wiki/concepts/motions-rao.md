---
title: "Motions and Response Amplitude Operators"
tags: [motions, rao, seakeeping, hydrodynamics, operability]
sources:
  - committed-public-wiki-metadata
added: 2026-05-06
last_updated: 2026-05-06
---

# Motions and Response Amplitude Operators

Motions and response amplitude operators (RAOs) describe how a vessel or floating offshore unit responds to regular waves across frequency, heading, and degree of freedom. They are a practical bridge between hydrodynamic analysis, seakeeping, operability checks, mooring response, and riser or transfer-system interface loads.

## Engineering Use

RAOs are commonly used to:

- screen heave, roll, pitch, surge, sway, and yaw response across wave headings
- convert wave spectra into motion response spectra for operability or fatigue studies
- compare diffraction/radiation solvers and time-domain model inputs
- feed berth, transfer, riser, and station-keeping checks where motion limits govern usability

## Public-Wiki Boundary

This page gives a navigation-level description only. It does not reproduce ITTC procedure text, class-society formulas, solver manuals, coefficient tables, or vendor examples.

## Relationship to Existing Pages

The current public wiki already has related coverage in:

- [Seakeeping and 6-DOF Ship Dynamics](../../../engineering/wiki/concepts/seakeeping-6dof.md)
- [Hydrodynamic Analysis](../../../engineering/wiki/concepts/hydrodynamic-analysis.md)
- [AQWA Solver](../../../engineering/wiki/entities/aqwa-solver.md)
- [OrcaWave Solver](../../../engineering/wiki/entities/orcawave-solver.md)
- [OrcaFlex Solver](../../../engineering/wiki/entities/orcaflex-solver.md)
- [LNG Berth Operability](lng-berth-operability.md)
- [LNG Transfer System Envelope](lng-transfer-system-envelope.md)

## Practical Checks

When using RAO data in a marine-engineering workflow, keep these checks explicit:

1. degree-of-freedom convention and sign convention
2. frequency unit and ordering
3. heading convention
4. displacement, center of gravity, and waterline basis
5. rotational unit convention
6. whether the downstream workflow expects amplitude, phase, real/imaginary components, or response spectra
