---
title: "Marine Engineering Code and Results Links"
added: 2026-05-11
last_updated: 2026-05-11
type: reference-index
tags: [marine-engineering, implementation, results, public-safe]
sources:
  - ../../cross-links-tier1.md
  - ../../../docs/reports/2026-05-11-tier1-ecosystem-link-map.md
---

# Marine Engineering Code and Results Links

This page makes the marine/offshore wiki operational by linking concepts to public-safe implementation, demo, and result surfaces. It deliberately avoids raw solver models, client simulations, standards text, and private project archives.

## Implementation anchors

| Topic | Authoritative public-safe target | Use in wiki |
|---|---|---|
| Digital model routing | [digitalmodel](https://github.com/vamseeachanta/digitalmodel) `docs/maps/digitalmodel-operator-map.md` | Start here before linking a concept to code. |
| Marine engineering domain docs | [digitalmodel](https://github.com/vamseeachanta/digitalmodel) `docs/domains/marine-engineering/` | General marine/offshore workflows and proof points. |
| OrcaFlex workflows | [digitalmodel](https://github.com/vamseeachanta/digitalmodel) `docs/domains/orcaflex/` | Dynamic analysis, model setup, post-processing. |
| OrcaWave workflows | [digitalmodel](https://github.com/vamseeachanta/digitalmodel) `docs/domains/orcawave/` | Diffraction/radiation analysis and hydrodynamic coefficients. |
| Hydrodynamics | [digitalmodel](https://github.com/vamseeachanta/digitalmodel) `docs/domains/hydrodynamics/` | RAOs, added mass, damping, solver comparisons. |
| GTM demo runner | [digitalmodel](https://github.com/vamseeachanta/digitalmodel) `examples/demos/gtm/README.md` | Public-safe examples that connect methods to rendered outputs. |

## Result/demo anchors

| Result family | Candidate target | Public-safety rule |
|---|---|---|
| Freespan/VIV | [digitalmodel](https://github.com/vamseeachanta/digitalmodel) `examples/demos/gtm/output/` and [aceengineer-website](https://github.com/vamseeachanta/aceengineer-website) `content/demos/freespan.html` | Link only validated demo outputs. |
| Mudmat installation | [digitalmodel](https://github.com/vamseeachanta/digitalmodel) `examples/demos/gtm/output/` and [aceengineer-website](https://github.com/vamseeachanta/aceengineer-website) `content/demos/mudmat.html` | No client vessel/site data. |
| Shallow-water pipelay | [digitalmodel](https://github.com/vamseeachanta/digitalmodel) `examples/demos/gtm/output/` and [aceengineer-website](https://github.com/vamseeachanta/aceengineer-website) `content/demos/pipelay.html` | Public synthetic case only. |
| Rigid/flexible jumper installation | [digitalmodel](https://github.com/vamseeachanta/digitalmodel) `examples/demos/gtm/output/` and [aceengineer-website](https://github.com/vamseeachanta/aceengineer-website) `content/demos/jumper-installation.html` | Public synthetic case only. |
| On-bottom stability | [aceengineer-website](https://github.com/vamseeachanta/aceengineer-website) `content/case-studies/pipeline-on-bottom-stability-assessment.html` | Link public case study; do not embed private calculations. |

## Link-back targets

Update or cross-reference this page from marine-engineering portal/index pages whenever a concept page needs an implementation or result pointer. Use repository-relative paths for branch-sensitive artifacts until the target exists on the public default branch.
