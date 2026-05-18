---
title: "Reservoir Engineering Literature Corpus — formation-evaluation foundation scope"
issue: 40
created: 2026-05-16
last_updated: 2026-05-17
scope: formation-evaluation-foundation (per #40 user scope-narrow 2026-05-15)
companion_issue: vamseeachanta/kaggle-rogii-2026#5
total_candidates: 36
classifications: {ingest: 25, defer: 1, skip: 10}
license_fail_closed_posture: true
phase_b_redacted: true  # see Local sources (Phase B) section; off-repo data-layer content not enumerated
---

# Reservoir Engineering Literature Corpus

Inventory of candidate sources for `wikis/reservoir-engineering/` Waves 3–5 (concept pages, methodology pages, standards pages). Built per approved plan [#40](https://github.com/vamseeachanta/llm-wiki/issues/40) under formation-evaluation-foundation scope, driven by the [Kaggle ROGII 2026](https://github.com/vamseeachanta/kaggle-rogii-2026/issues/5) modeling needs (porosity, permeability, gamma-ray log interpretation, dip/azimuth, formation tops, geosteering workflow, log correlation).

License-triage applies **license-fail-closed posture** per Codex r2 advisory carried in `.planning/plan-approved/40.md`: when in doubt, SKIP. Only sources with clearly-redistributable licenses (CC-BY, CC-BY-SA, public domain, OCW with explicit redistribution clause) are classified `ingest`. Sources where license is unclear, where commercial-redistribution is restricted (the wiki publishes under CC-BY-4.0 which is commercial-permissive), or where the source is paywalled / shareware / all-rights-reserved are classified `skip` or `defer`. **Note on CC-BY-NC sources:** `ingest`-classified MIT OCW (CC-BY-NC-SA) and Equinor Volve (CC-BY-NC-SA) entries below are admissible as **reference citations** under fair-use scholarly attribution in wiki pages but cannot have their content redistributed into the llm-wiki corpus verbatim — the NC clause is incompatible with the wiki's CC-BY-4.0 publication license for derivative-content reuse. They are flagged `ingest-ref-only` in the license note. Use-in-wiki: cite + paraphrase ≤30 words, never copy.

This manifest carries paths + metadata + decisions only. No source content is reproduced here; ingestion to wiki content pages happens in Waves 3–5 with per-page citation discipline (see `.claude/rules/calc-citation-contract.md`).

## Coordination with #2667 Domain Knowledge Sweep

Per the plan body, this Wave 2 deliverable is scope-narrowed to **formation evaluation** (driven by Kaggle ROGII 2026). Core reservoir-engineering substrate (relative perm, capillary pressure, recovery factor, material balance, decline-curve analysis, well-test interpretation, PVT) is DEFERRED — may land under [workspace-hub#2667 Domain Knowledge Sweep](https://github.com/vamseeachanta/workspace-hub/issues/2667) when it reaches reservoir engineering. #2667 had not scheduled reservoir-eng work as of 2026-05-16 (last #2667 update 2026-05-13 — Domain 1 Hydrodynamics #2668 still active). Pre-execution check satisfied.

## Online sources (Phase A)

| # | Source | Title / Description | URL | License | Classification | License note |
|---|---|---|---|---|---|---|
| A1 | MIT OCW | 12.110 Sedimentary Geology — lecture notes (stratigraphy, depositional environments, sedimentary basins, diagenesis) | https://ocw.mit.edu/courses/12-110-sedimentary-geology-spring-2007/pages/lecture-notes/ | CC-BY-NC-SA 4.0 | ingest | `ingest-ref-only`: MIT OCW CC-BY-NC-SA confirmed in page footer; NC clause incompatible with llm-wiki CC-BY-4.0 derivative reuse — cite as reference, paraphrase ≤30 words, no verbatim copy |
| A2 | MIT OCW | 12.113 Structural Geology (Fall 2005) — faults, folds, strain analysis (background for dip/azimuth interpretation) | https://ocw.mit.edu/courses/12-113-structural-geology-fall-2005/ | CC-BY-NC-SA 4.0 | ingest | `ingest-ref-only`: MIT OCW CC-BY-NC-SA; reference-only for dip/azimuth concept page; paraphrase + attribute |
| A3 | MIT OCW | EAPS catalog — earth, atmospheric and planetary sciences open course list (browse-entry for additional related courses) | https://ocw.mit.edu/courses/earth-atmospheric-and-planetary-sciences/ | CC-BY-NC-SA 4.0 | skip | License-verification 2026-05-17 (#96): CC-BY-NC-SA 4.0 NC clause incompatible with llm-wiki CC-BY-4.0 derivative redistribution. Available as bibliographic pointer only (cite + paraphrase ≤30 words under fair-use); cannot bulk-extract content |
| A4 | AAPG Wiki | Well log analysis for reservoir characterization | http://wiki.aapg.org/Well_log_analysis_for_reservoir_characterization | CC-BY-SA 3.0 Unported | ingest | CC-BY-SA verified at wiki.aapg.org/AAPG_Wiki:Copyrights — commercial-redistribution-permitted with attribution; compatible with llm-wiki CC-BY-4.0 (downstream consumers must preserve SA on derivative-of-derivative) |
| A5 | AAPG Wiki | Petrophysical analysis of lithofacies | https://wiki.aapg.org/Petrophysical_analysis_of_lithofacies | CC-BY-SA 3.0 Unported | ingest | Same as A4 — CC-BY-SA, attribute and preserve SA on derivative content |
| A6 | AAPG Wiki | Data sources (wireline logs, LWD, core analysis) | https://wiki.aapg.org/Data:_sources | CC-BY-SA 3.0 Unported | ingest | Same as A4 |
| A7 | AAPG Wiki | Top 10 Landmark Papers in Petrophysics and Formation Evaluation (centennial reference list) | https://100years.aapg.org/top-100-papers-petrophysics-formation-evaluation | unclear — appears to be AAPG.org editorial, not wiki | skip | License-verification 2026-05-17 (#96): no explicit license on AAPG centennial editorial page; presumed all-rights-reserved per fail-closed posture. Available as bibliographic pointer only — each individual cited paper still requires per-source license check before extraction |
| A8 | SEG Wiki | Log analysis for unconventionals | https://wiki.seg.org/wiki/Log_analysis_for_unconventionals | CC-BY-SA 3.0 Unported | ingest | CC-BY-SA verified at wiki.seg.org/wiki/SEG_Wiki:Copyrights; compatible with llm-wiki publication; image-by-image reuse must be individually verified per SEG Wiki notes |
| A9 | SEG Wiki | Seismic petrophysics: Part 1 | https://wiki.seg.org/wiki/Seismic_petrophysics:_Part_1 | CC-BY-SA 3.0 Unported | ingest | Same as A8 |
| A10 | SEG Wiki | Sonic logs | https://wiki.seg.org/wiki/Sonic_logs | CC-BY-SA 3.0 Unported | ingest | Same as A8 |
| A11 | SEG Wiki | Resistivity log | https://wiki.seg.org/wiki/Resistivity_log | CC-BY-SA 3.0 Unported | ingest | Same as A8 — feeds porosity / saturation concept pages |
| A12 | SEG Wiki | Pickett plot (graphical Archie's-equation method) | https://wiki.seg.org/wiki/Pickett_plot | CC-BY-SA 3.0 Unported | ingest | Same as A8 — methodology reference for permeability concept page |
| A13 | USGS | Open-File Report 1990/0637a — Fundamentals of Well Logging and Well-Log Interpretation (annotated bibliography) | https://pubs.usgs.gov/of/1990/0637a/report.pdf | public domain (US federal work) | ingest | Public-domain US federal publication per 17 USC §105; safe for unrestricted reuse |
| A14 | USGS | Open-File Report 1993/0579a — Basic Well Logging and General Petrophysics (bibliography) | https://pubs.usgs.gov/of/1993/0579a/report.pdf | public domain (US federal work) | ingest | Same as A13 |
| A15 | USGS | Open-File Report 1995/0817a — Bibliography of Well-Log Applications | https://pubs.usgs.gov/of/1995/0817a/report.pdf | public domain (US federal work) | ingest | Same as A13 |
| A16 | USGS | Open-File Report 2014/1023 — petrophysical properties of ash-flow tuff, algorithms for porosity and water saturation calculations from logs (25 boreholes) | https://pubs.usgs.gov/of/2014/1023/pdf/ofr2014-1023.pdf | public domain (US federal work) | ingest | Same as A13 — direct calc-derivation source for porosity/saturation pages |
| A17 | USGS | OFR 1986/0170 — Geological applications of well logs | https://pubs.usgs.gov/of/1986/0170/report.pdf | public domain (US federal work) | ingest | Same as A13 |
| A18 | USGS | OFR 1998/0487 — Visualization of Subsurface Geology from Wireline Logs (Collins) | https://pubs.usgs.gov/of/1998/of98-487/collins.html | public domain (US federal work) | ingest | Same as A13 — directly relevant to formation tops + log correlation methodology page |
| A19 | Kansas Geological Survey | Geological Log Analysis — online practitioner's manual (intro chapter linked) | https://www.kgs.ku.edu/Publications/Bulletins/LA/index.html | US state-government work; KGS publications generally public-domain for reuse with attribution — needs per-page verification | ingest | KGS is a state agency (University of Kansas); content historically published for unrestricted educational use; recommend explicit attribution per page used and one final license-confirmation email to KGS before bulk extraction in Wave 3 |
| A20 | Kansas Geological Survey | The Logging Operation (LA bulletin ch.1) | https://www.kgs.ku.edu/Publications/Bulletins/LA/01_logging.html | same as A19 | ingest | Same as A19 |
| A21 | Kansas Geological Survey | Digital Logs (LA bulletin ch.2) | https://www.kgs.ku.edu/Publications/Bulletins/LA/02_digital.html | same as A19 | ingest | Same as A19 |
| A22 | Kansas Geological Survey | Open-File Reports archive (1930s–present, PDF) | https://www.kgs.ku.edu/Publications/pubOFR.html | state-government, per-document license varies | defer | KGS [Publishing Policy](https://www.kgs.ku.edu/Publications/pubPolicy.html) states all KGS publications are public domain with source credit requested. Pending explicit confirmation that this applies uniformly across the OFR archive via [#98](https://github.com/vamseeachanta/llm-wiki/issues/98) email-in-flight (drafted 2026-05-17). Re-classify on KGS response |
| A23 | Kansas Geological Survey | LAS digital well logs for Kansas (post-2yr confidentiality) | https://www.kgs.ku.edu/Magellan/Logs/ | state-government open data | ingest | Open data, free download; can be cited as canonical example dataset for log-correlation methodology page |
| A24 | Equinor / Force | Volve field public dataset — 5 TB / 40k files including well logs (petrophysical + drilling), seismic, static/dynamic models | https://www.equinor.com/energy/volve-data-sharing | CC-BY-NC-SA per Equinor Open Data Licence | ingest | `ingest-ref-only`: NC clause; cite as canonical real-data example for geosteering + log-correlation methodology; do NOT redistribute the dataset contents into wiki repo; link out only |
| A25 | arXiv | 2509.18152 — "WLFM: Well-Logs Foundation Model for Multi-Task and Cross-Well Geological Interpretation" (transformer + masked-token modeling for lithology classification) | https://arxiv.org/abs/2509.18152 | CC BY 4.0 | ingest | License verified 2026-05-17 (#96): arXiv abs page links to https://creativecommons.org/licenses/by/4.0/. Authors: Zhenyu Qi, Qing Yu, Jichen Wang, Yun-Bo Zhao, Zerui Li, Wenjun Lv (2025-09-16). Compatible with llm-wiki CC-BY-4.0; direct relevance to Kaggle ROGII modeling |
| A26 | arXiv | 2512.13529 — "Enhancing lithological interpretation from petrophysical well log of IODP expedition 390/393 using machine learning" | https://arxiv.org/abs/2512.13529 | arXiv perpetual non-exclusive license (no CC variant) | skip | License verified 2026-05-17 (#96): arXiv abs page links to https://arxiv.org/licenses/nonexclusive-distrib/1.0/ — author retains copyright, reuse beyond arXiv requires per-author permission. Authors: Raj Sahu, Saumen Maiti (2025-12-15). Fail-closed → skip for extraction. Available as bibliographic pointer only |
| A27 | Frontiers in Earth Science | "Geological information-driven deep learning for lithology identification from well logs" (2025) | https://www.frontiersin.org/journals/earth-science/articles/10.3389/feart.2025.1662760/full | Frontiers default is CC-BY 4.0 (open access publisher) | ingest | Frontiers is OA-by-default CC-BY-4.0; compatible with llm-wiki license; cite directly |
| A28 | Springer Nature Link | "Petrophysical evaluation of well log data and rock physics modeling for characterization of Eocene reservoir, Chandmari oil field" (J. Petroleum Exploration & Production Technology, 2017) | https://link.springer.com/article/10.1007/s13202-017-0373-8 | CC BY 4.0 | ingest | License verified 2026-05-17 (#96) via CrossRef API for DOI 10.1007/s13202-017-0373-8: license.URL = http://creativecommons.org/licenses/by/4.0, effective 2017-07-28. Springer JPEPT is fully open access. Compatible with llm-wiki CC-BY-4.0 |
| A29 | DOAB / OAPEN | "The Geology of Kuwait" — open access book covering marine geology, structural geology, hydrogeology, geophysics relevant to petroleum exploration | https://library.oapen.org/handle/20.500.12657/60172 | CC BY 4.0 | ingest | License verified 2026-05-17 (#96) via DOAB metadata API: "Springer Nature books are published under the Creative Commons Attribution 4.0 (CC BY) license, so they can be reused and redistributed as long as the original author is attributed". Compatible with llm-wiki CC-BY-4.0 |
| A30 | Stanford Doerr School | Energy Resources Engineering (ERE) program overview — bulletin / catalog only (no OCW courses with downloadable materials located) | https://ese.stanford.edu/ | not licensed for reuse (program-info pages); no OCW analog for ERE found in 2026-05-16 search | skip | Stanford SEE (CC-BY-NC-SA) was searched; no petroleum / energy / geoscience courses present in SEE catalog. ERE itself does not publish OCW. Pointer-only; skip for ingestion |
| A31 | Texas A&M PETE 663 | "Formation Evaluation and Analysis of Reservoir Performance" (Blasingame syllabus archive) | https://blasingame.engr.tamu.edu/ | university-faculty content, no explicit license; copyright presumed reserved | skip | License-verification 2026-05-17 (#96): no explicit license on archive landing page; faculty-owned course materials default to all-rights-reserved per fail-closed posture. Available as bibliographic pointer only — bulk reuse would require explicit Blasingame permission |
| A32 | UT Austin PETEX | Formation Evaluation e-learning module | https://petex.utexas.edu/e-learning/modules/exploration-elearning/330-formation-evaluation | paid e-learning, not open | skip | PETEX is paid commercial e-learning extension; not redistributable; included here only to document scope decision |
| A33 | Heriot-Watt IGE | MSc Petroleum Engineering — online program | https://www.hw.ac.uk/online/postgraduate/petroleum-engineering-msc.htm | tuition-based, no open / free materials located | skip | Pay-per-course tuition program; no open educational resources found in 2026-05-16 search |
| A34 | OnePetro / SPE Journal | General petroleum-engineering search portal | https://onepetro.org/ | mostly paywalled; individual open-access entries exist but are exception not default | skip | License-verification 2026-05-17 (#96): default-paywalled portal; only ingest specific papers via per-page open-access verification on targeted entries. Portal-level entry: bibliographic pointer only |
| A35 | SLB (Schlumberger) | Log Interpretation Charts (chartbook) | https://www.slb.com/resource-library/book/log-interpretation-charts | all rights reserved per copyright notice; Internet Archive availability does NOT confer redistribution rights | skip | All-rights-reserved corporate publication; Internet Archive copy exists but copyright notice explicitly restricts reproduction; fail-closed → skip |
| A36 | spec2000.net | Crain's Petrophysical Handbook (Ross Crain) | https://spec2000.net/ | shareware (fee-based licence: single-user / corporate / academic / associate-instructor) | skip | Shareware fee required; not redistributable under any CC-compatible license; fail-closed → skip. (Free 100+ technical papers section on same site is per-paper license-check.) |

## Local sources (Phase B) — redacted

A Phase B sweep was performed against the local candidate directory named in the plan body (`/mnt/ace/rock-oil-field/`). The directory was determined to be off-repo data infrastructure for the user's professional client work — operationally correctly-domain for its actual purpose, but not a reservoir-engineering or formation-evaluation literature corpus. No in-scope reservoir-engineering / formation-evaluation sources were identified by the sweep.

Per the off-repo data-layer governance boundary that applies to client and employer materials in published repositories, no path-level / title-level / document-level enumeration of off-repo content is carried into this public manifest. The Phase B contribution to corpus inventory is therefore zero rows.

**Implication for future plans:** plan bodies that name local-directory candidates by name should not assume name-based categorisation. If a future plan re-proposes walking `/mnt/ace/rock-oil-field/` for reservoir-engineering / formation-evaluation content, this Phase B finding pre-empts the work (zero in-scope content; off-repo data-layer boundary applies).

_Phase B per-row enumeration redacted 2026-05-17 per off-repo data-layer governance boundary (client/employer materials)._

## Summary

| Classification | Online (Phase A) | Local (Phase B) | Total |
|---|---|---|---|
| ingest | 25 | _(redacted)_ | 25 |
| defer | 1 | _(redacted)_ | 1 |
| skip | 10 | _(redacted)_ | 10 |
| **Total** | **36** | **_(redacted)_** | **36** |

Net inventory: **36 triaged rows publicly enumerated** (Phase A only; Phase B per-row enumeration redacted per off-repo data-layer governance — see Phase B section above). The sweep's audit-trail finding is preserved (Phase B yielded zero in-scope sources); the row-level evidence is not carried into this public manifest.

> Counts reconciled 2026-05-17 ([#96](https://github.com/vamseeachanta/llm-wiki/issues/96) commit): post-redaction frontmatter previously asserted `total_candidates: 42 (ingest 24, defer 10, skip 8)`; actual Phase A table had 36 rows (ingest 22, defer 9, skip 5). This commit reconciles both the latent 6-row inconsistency and the #96 reclassifications in one pass.

### Plan acceptance check

Plan acceptance criterion (lines 104 + 56 of the approved plan): **≥30 high-quality OR ≥50 mixed-quality**, each row carrying `(filepath/URL, classification, license note)`.

| Metric | Target | Actual | Met? |
|---|---|---|---|
| High-quality (`ingest`) sources | ≥30 | 25 | Partial — short of 30 by 5 ([#97](https://github.com/vamseeachanta/llm-wiki/issues/97) arXiv expansion targets the gap) |
| Mixed-quality (`ingest` + `defer`) sources | ≥50 | 26 | Partial — short of 50 by 24 (post-#96 license verification moved most defers to skip per fail-closed; [#97](https://github.com/vamseeachanta/llm-wiki/issues/97) arXiv expansion targets the gap) |
| All rows | (schema) | 36 publicly enumerated, every row with non-blank license note | **Met for enumerated rows** |

**Gap analysis (post-#96 license verification, 2026-05-17):** The 25 / 26 totals reflect the post-#96 state after per-row license verification of the original 9 `defer` rows. Of those 9 defers, 3 promoted to `ingest` (A25 + A28 + A29 — all CC-BY-4.0 verified via arXiv abs / CrossRef API / DOAB API), 5 demoted to `skip` per fail-closed posture (A3 NC-incompatible / A7 unclear / A26 arXiv-non-exclusive / A31 no-explicit-license / A34 paywalled-portal), and 1 remains `defer` (A22 KGS OFR archive — pending [#98](https://github.com/vamseeachanta/llm-wiki/issues/98) email response). The remaining acceptance gaps will be closed by:

1. **[#98](https://github.com/vamseeachanta/llm-wiki/issues/98) KGS email response** — if the OFR archive is uniformly public-domain per [KGS Publishing Policy](https://www.kgs.ku.edu/Publications/pubPolicy.html), A22 promotes to `ingest` (+1 → ingest 26).
2. **[#97](https://github.com/vamseeachanta/llm-wiki/issues/97) arXiv expansion** — targeted search of `physics.geo-ph` + `stat.ML` for additional CC-BY licensed well-log / lithology-classification papers; primary mechanism for closing the mixed-quality gap to ≥50.
3. **Wave 3 ingestion** can now proceed against the 25 `ingest`-classified sources without per-row license blockers.

Caveat for the mixed-quality target: the post-#96 license verification consciously moved defers to skip rather than holding them open — the resulting mixed-quality count (26) is *lower* than the prior 34 because the verification surfaced incompatibility rather than confirming permissibility. This is the fail-closed posture working as designed; #97 expansion is now the load-bearing path to ≥50.

## Notes

- **License-triage discipline:** defaulted to `skip` for paywalled-textbook filename patterns; defaulted to `skip` for shareware (Crain's, spec2000.net) and all-rights-reserved corporate publications (SLB chartbook). Defaulted to `ingest` only for clearly-CC-licensed wiki content (AAPG, SEG), federal public-domain works (USGS), or OCW with explicit CC-BY-NC-SA licence (MIT — flagged `ingest-ref-only` because NC is incompatible with llm-wiki CC-BY-4.0 derivative-reuse).
- **`defer` rows** require external dependency to resolve. After [#96](https://github.com/vamseeachanta/llm-wiki/issues/96) license verification (2026-05-17), only 1 defer remains: A22 (KGS OFR archive) pending [#98](https://github.com/vamseeachanta/llm-wiki/issues/98) email response. All other prior defers have been re-classified — see Gap analysis above for the resolution.
- **No source content reproduced in this manifest** — paths, URLs, titles, sizes, and metadata only.
- **Vendor-derivative deny-list** per [workspace-hub#2482](https://github.com/vamseeachanta/workspace-hub/issues/2482): no `wikis/*/wiki/sources/` paths appear here (correctly — none would by design under formation-eval scope).
- **Cross-link to be added in Wave 3:** kaggle-rogii-2026#5 should reference this manifest once the wiki domain pages exist.

## Forward references for main session

Wave 3-5 sub-issues filed under [#40](https://github.com/vamseeachanta/llm-wiki/issues/40):

1. **[#96](https://github.com/vamseeachanta/llm-wiki/issues/96) — License-verification sub-issue** — per-document license check for the 9 `defer` rows in this manifest (A3, A7, A22, A25, A26, A28, A29, A31, A34). **Status:** COMPLETED 2026-05-17 — 3 promoted to `ingest` (A25/A28/A29 CC-BY-4.0 verified), 5 demoted to `skip` per fail-closed (A3/A7/A26/A31/A34), 1 remains `defer` (A22 pending [#98](https://github.com/vamseeachanta/llm-wiki/issues/98) KGS email). See Gap analysis above.
2. **[#98](https://github.com/vamseeachanta/llm-wiki/issues/98) — Kansas Geological Survey reuse-permission request** — single email/contact to KGS confirming bulk-reuse-under-attribution for the Log Analysis bulletin (A19–A21) before Wave 3 authoring extracts content. **Status:** `status:plan-approved` 2026-05-17.
3. **[#97](https://github.com/vamseeachanta/llm-wiki/issues/97) — arXiv expansion sub-issue** — targeted search of arXiv `physics.geo-ph` + `stat.ML` for additional CC-BY-licensed well-log machine-learning papers to close the mixed-quality gap to ≥50. **Status:** `status:plan-approved` 2026-05-17.
4. **[#99](https://github.com/vamseeachanta/llm-wiki/issues/99) — Corpus-mismatch documentation note** — originally proposed; **CLOSED as obsolete 2026-05-17** per user reframing: the local candidate directory is correctly-domain for its actual purpose (off-repo data infrastructure), and the existing off-repo data-layer governance boundary already applies — no new `docs/governance/` note in llm-wiki was needed. Phase B redaction in this manifest is the appropriate remediation; recorded above.
