# OSS engineering-tool watchlist — 2026-05-16

## Run metadata
- Date: 2026-05-16
- Schema version: `oss-tool-watchlist-report/v1`
- Roadmap anchor: https://github.com/vamseeachanta/llm-wiki/issues/13
- Public-safety note: public-safe metadata-only report; no raw/private/vendor/client content.
- Data sources: committed `data/oss_tool_watchlist.json`, optional fixture observations, optional prior state, and `data/oss_tool_issue_map.json` only.

## Tools checked and signal sources
| Tool | Signal strategy | Source URL | Docs URL | Tier-1 links | Wiki target |
|---|---|---|---|---|---|
| MoorDyn | github_release | https://api.github.com/repos/FloatingArrayDesign/MoorDyn/releases/latest | https://moordyn.readthedocs.io/ | https://github.com/vamseeachanta/digitalmodel | `wikis/engineering/wiki/entities/moordyn-tool.md` |
| MoorPy | github_release | https://api.github.com/repos/NREL/MoorPy/releases/latest | https://moorpy.readthedocs.io/ | https://github.com/vamseeachanta/digitalmodel | `wikis/engineering/wiki/entities/moorpy-tool.md` |
| OpenFAST | github_release | https://api.github.com/repos/OpenFAST/openfast/releases/latest | https://openfast.readthedocs.io/ | https://github.com/vamseeachanta/digitalmodel | `wikis/engineering/wiki/entities/openfast-tool.md` |
| Capytaine | github_release | https://api.github.com/repos/capytaine/capytaine/releases/latest | https://capytaine.org/ | https://github.com/vamseeachanta/digitalmodel | `wikis/engineering/wiki/entities/capytaine-tool.md` |
| HAMS | latest_commit_marker | https://api.github.com/repos/YingyiLiu/HAMS/commits?per_page=1 | https://github.com/YingyiLiu/HAMS | https://github.com/vamseeachanta/digitalmodel | `wikis/engineering/wiki/entities/hams-tool.md` |
| WEC-Sim | github_release | https://api.github.com/repos/WEC-Sim/WEC-Sim/releases/latest | https://wec-sim.github.io/WEC-Sim/ | https://github.com/vamseeachanta/digitalmodel | `wikis/engineering/wiki/entities/wec-sim-tool.md` |
| OPM Flow | github_release | https://api.github.com/repos/OPM/opm-simulators/releases/latest | https://opm-project.org/ | https://github.com/vamseeachanta/worldenergydata, https://github.com/vamseeachanta/digitalmodel | `wikis/engineering/wiki/entities/opm-flow-tool.md` |
| OpenFOAM | github_release | https://api.github.com/repos/OpenFOAM/OpenFOAM-dev/releases/latest | https://www.openfoam.com/documentation/ | https://github.com/vamseeachanta/digitalmodel | `wikis/engineering/wiki/entities/openfoam-cfd.md` |
| Gmsh | docs_or_release_page_marker | https://gmsh.info/ | https://gmsh.info/doc/texinfo/gmsh.html | https://github.com/vamseeachanta/digitalmodel, https://github.com/vamseeachanta/assetutilities | `wikis/engineering/wiki/entities/gmsh-tool.md` |
| FreeCAD | github_release | https://api.github.com/repos/FreeCAD/FreeCAD/releases/latest | https://wiki.freecad.org/ | https://github.com/vamseeachanta/digitalmodel, https://github.com/vamseeachanta/assetutilities | `wikis/engineering/wiki/entities/freecad-tool.md` |
| ParaView | docs_or_download_page_marker | https://www.paraview.org/download/ | https://docs.paraview.org/ | https://github.com/vamseeachanta/digitalmodel, https://github.com/vamseeachanta/assetutilities | `wikis/engineering/wiki/entities/paraview-tool.md` |
| PyVista | github_release | https://api.github.com/repos/pyvista/pyvista/releases/latest | https://docs.pyvista.org/ | https://github.com/vamseeachanta/digitalmodel, https://github.com/vamseeachanta/assetutilities | `wikis/engineering/wiki/entities/pyvista-tool.md` |
| BEMRosetta | github_release | https://api.github.com/repos/BEMRosetta/BEMRosetta/releases/latest | https://github.com/BEMRosetta/BEMRosetta | https://github.com/vamseeachanta/digitalmodel | `wikis/engineering/wiki/entities/bemrosetta-tool.md` |

## Detected changes
| Tool | Signal type | Observed | Previous | Confidence | Why it matters |
|---|---|---|---|---|---|
| MoorDyn | candidate_page_missing | baseline-unverified | baseline-unverified | medium | Open mooring dynamics reference for comparing OrcaFlex-style workflows and testing public mooring examples. |
| MoorPy | candidate_page_missing | baseline-unverified | baseline-unverified | medium | Useful public Python reference for mooring statics, line-property examples, and validation fixtures. |
| OpenFAST | candidate_page_missing | baseline-unverified | baseline-unverified | medium | Provides public coupled-simulation context that can inform digitalmodel examples and solver-comparison docs. |
| Capytaine | candidate_page_missing | baseline-unverified | baseline-unverified | medium | Open hydrodynamics solver useful for public solver-benchmark and coefficient-contract thinking. |
| HAMS | candidate_page_missing | baseline-unverified | baseline-unverified | low | Public BEM reference useful for benchmark comparisons when release cadence is sparse. |
| WEC-Sim | candidate_page_missing | baseline-unverified | baseline-unverified | medium | Useful public examples for hydrodynamics-driven simulation and report-generation workflows. |
| OPM Flow | candidate_page_missing | baseline-unverified | baseline-unverified | medium | Connects public reservoir-simulation concepts to worldenergydata and engineering code development. |
| OpenFOAM | no_change | baseline-unverified | baseline-unverified | medium | OpenFOAM is a public CFD anchor for code-development workflows and cross-machine solver readiness. |
| Gmsh | candidate_page_missing | baseline-unverified | baseline-unverified | medium | Gmsh is core to geometry-to-solver pipelines and mesh-quality validation. |
| FreeCAD | candidate_page_missing | baseline-unverified | baseline-unverified | medium | FreeCAD enables public, scriptable CAD workflows for geometry generation and solver input preparation. |
| ParaView | candidate_page_missing | baseline-unverified | baseline-unverified | medium | ParaView is a public visualization anchor for CFD and simulation result inspection. |
| PyVista | candidate_page_missing | baseline-unverified | baseline-unverified | medium | PyVista supports code-generated 3D inspection, documentation images, and solver result visualization. |
| BEMRosetta | no_change | baseline-unverified | baseline-unverified | medium | BEMRosetta bridges hydrodynamic coefficient formats relevant to OrcaWave/AQWA/OrcaFlex workflows. |

## Candidate wiki updates
| Tool | Candidate action | Affected paths | Rationale |
|---|---|---|---|
| MoorDyn | create_initial_seed_page | `wikis/engineering/wiki/entities/moordyn-tool.md`, `wikis/engineering/wiki/concepts/mooring-dynamics.md` | Tool is watchlisted but the candidate wiki target does not exist. |
| MoorPy | create_initial_seed_page | `wikis/engineering/wiki/entities/moorpy-tool.md`, `wikis/engineering/wiki/concepts/mooring-analysis.md` | Tool is watchlisted but the candidate wiki target does not exist. |
| OpenFAST | create_initial_seed_page | `wikis/engineering/wiki/entities/openfast-tool.md`, `wikis/engineering/wiki/concepts/offshore-wind-dynamics.md` | Tool is watchlisted but the candidate wiki target does not exist. |
| Capytaine | create_initial_seed_page | `wikis/engineering/wiki/entities/capytaine-tool.md`, `wikis/engineering/wiki/entities/diffraction-analysis-system.md` | Tool is watchlisted but the candidate wiki target does not exist. |
| HAMS | create_initial_seed_page | `wikis/engineering/wiki/entities/hams-tool.md`, `wikis/engineering/wiki/entities/diffraction-analysis-system.md` | Tool is watchlisted but the candidate wiki target does not exist. |
| WEC-Sim | create_initial_seed_page | `wikis/engineering/wiki/entities/wec-sim-tool.md`, `wikis/engineering/wiki/concepts/wave-energy-converters.md` | Tool is watchlisted but the candidate wiki target does not exist. |
| OPM Flow | create_initial_seed_page | `wikis/engineering/wiki/entities/opm-flow-tool.md`, `wikis/engineering/wiki/concepts/reservoir-simulation.md` | Tool is watchlisted but the candidate wiki target does not exist. |
| OpenFOAM | no_action | `wikis/engineering/wiki/entities/openfoam-cfd.md`, `wikis/engineering/wiki/concepts/cfd-pipeline.md` | No actionable public signal change detected. |
| Gmsh | create_initial_seed_page | `wikis/engineering/wiki/entities/gmsh-tool.md`, `wikis/engineering/wiki/concepts/mesh-generation.md` | Tool is watchlisted but the candidate wiki target does not exist. |
| FreeCAD | create_initial_seed_page | `wikis/engineering/wiki/entities/freecad-tool.md`, `wikis/engineering/wiki/concepts/cad-automation.md` | Tool is watchlisted but the candidate wiki target does not exist. |
| ParaView | create_initial_seed_page | `wikis/engineering/wiki/entities/paraview-tool.md`, `wikis/engineering/wiki/concepts/scientific-visualization.md` | Tool is watchlisted but the candidate wiki target does not exist. |
| PyVista | create_initial_seed_page | `wikis/engineering/wiki/entities/pyvista-tool.md`, `wikis/engineering/wiki/concepts/scientific-visualization.md` | Tool is watchlisted but the candidate wiki target does not exist. |
| BEMRosetta | no_action | `wikis/engineering/wiki/entities/bemrosetta-tool.md`, `wikis/engineering/wiki/entities/diffraction-analysis-system.md` | No actionable public signal change detected. |

## Duplicate/open-issue routing
| Tool | Route action | Issue | Route reason |
|---|---|---|---|
| MoorDyn | reuse-existing-issue | [#79](https://github.com/vamseeachanta/llm-wiki/issues/79) | Issue #79 owns the weekly OSS engineering-tool watchlist lane and should receive MoorDyn signal deltas until split into a dedicated child issue. |
| MoorPy | comment-on-roadmap | [#13](https://github.com/vamseeachanta/llm-wiki/issues/13) | Initial seed-page candidates should be batched through the roadmap anchor before opening duplicate per-tool issues. |
| OpenFAST | comment-on-roadmap | [#13](https://github.com/vamseeachanta/llm-wiki/issues/13) | Initial seed-page candidates should be batched through the roadmap anchor before opening duplicate per-tool issues. |
| Capytaine | comment-on-roadmap | [#13](https://github.com/vamseeachanta/llm-wiki/issues/13) | Initial seed-page candidates should be batched through the roadmap anchor before opening duplicate per-tool issues. |
| HAMS | comment-on-roadmap | [#13](https://github.com/vamseeachanta/llm-wiki/issues/13) | Initial seed-page candidates should be batched through the roadmap anchor before opening duplicate per-tool issues. |
| WEC-Sim | comment-on-roadmap | [#13](https://github.com/vamseeachanta/llm-wiki/issues/13) | Initial seed-page candidates should be batched through the roadmap anchor before opening duplicate per-tool issues. |
| OPM Flow | comment-on-roadmap | [#13](https://github.com/vamseeachanta/llm-wiki/issues/13) | Initial seed-page candidates should be batched through the roadmap anchor before opening duplicate per-tool issues. |
| OpenFOAM | comment-on-roadmap | [#13](https://github.com/vamseeachanta/llm-wiki/issues/13) | Weekly OSS watchlist findings are deduplicated through the roadmap anchor unless a specific open issue owns the tool lane. |
| Gmsh | comment-on-roadmap | [#13](https://github.com/vamseeachanta/llm-wiki/issues/13) | Initial seed-page candidates should be batched through the roadmap anchor before opening duplicate per-tool issues. |
| FreeCAD | comment-on-roadmap | [#13](https://github.com/vamseeachanta/llm-wiki/issues/13) | Initial seed-page candidates should be batched through the roadmap anchor before opening duplicate per-tool issues. |
| ParaView | comment-on-roadmap | [#13](https://github.com/vamseeachanta/llm-wiki/issues/13) | Initial seed-page candidates should be batched through the roadmap anchor before opening duplicate per-tool issues. |
| PyVista | comment-on-roadmap | [#13](https://github.com/vamseeachanta/llm-wiki/issues/13) | Initial seed-page candidates should be batched through the roadmap anchor before opening duplicate per-tool issues. |
| BEMRosetta | comment-on-roadmap | [#13](https://github.com/vamseeachanta/llm-wiki/issues/13) | Weekly OSS watchlist findings are deduplicated through the roadmap anchor unless a specific open issue owns the tool lane. |

## Blocked/manual-review items
No blocked or manual-review items.

## Validation evidence
- `uv run pytest tests/test_oss_tool_watchlist.py tests/test_oss_tool_watchlist_artifacts.py -q`
- `uv run python scripts/llm_wiki_oss_tool_watchlist.py --date 2026-05-16 --write`
- `uv run python scripts/validate_oss_tool_watchlist.py data/oss_tool_watchlist.json docs/reports/2026-05-16-oss-engineering-tool-watchlist.md`

## Public-safety guardrail
This artifact is public-safe: it contains public URLs, repo-relative paths, normalized signal metadata, and GitHub issue links only. It does not copy upstream docs, source code, release-note bodies, unprocessed upstream response bodies, secrets, cookies, headers, or private paths.
