---
title: "BS 7910 — Flaw Assessment in Metallic Structures"
slug: bs-7910-flaw-assessment
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
tags:
  - bsi
  - standards
  - flaw-assessment
  - fitness-for-service
  - fatigue
  - fracture
  - ffs
  - metadata-only
sources:
  - /mnt/local-analysis/workspace-hub/llm-wiki/wikis/engineering-standards/wiki/sources/og-standards-bsi.md
  - /mnt/ace/O&G-Standards/_catalog.json
code_id: bs-7910
publisher: BSI
publisher_full: "British Standards Institution"
revision: "2013 (with Amendment 1, 2015)"
jurisdiction: UK / international
extraction_policy: metadata-only
raw_copy_allowed: false
bs_doc_number: "BS 7910"
ledger_id: BS-7910
---

# BS 7910 — Guide to Methods for Assessing the Acceptability of Flaws in Metallic Structures

**code_id:** `bs-7910` &nbsp;·&nbsp; **publisher:** BSI (British Standards Institution) &nbsp;·&nbsp; **revision:** 2013 (with Amendment 1, 2015) — latest edition present in catalog.

> Bounded metadata page. Vendor PDFs do not enter this repo per spinout 2026-05-05 governance — only publisher facts (titles, document IDs, revision years, on-disk paths) are recorded here. Cite the publisher edition for normative use.

## Scope

BS 7910 is BSI's flagship guide for **engineering critical assessment (ECA)** and **fitness-for-service (FFS)** evaluation of crack-like and non-crack-like flaws in metallic structures and weldments. It provides methods to determine whether a known or postulated flaw is acceptable for continued service under static, cyclic, and elevated-temperature loading.

The guide covers:

- **Failure Assessment Diagram (FAD) methodology** at three levels of analytical conservatism — **Level 1** (simplified, conservative; for screening and limited input data), **Level 2** (general-purpose, the workhorse for most assessments; further subdivided into 2A default and 2B material-specific options), and **Level 3** (advanced, ductile-tearing aware; uses J-integral / R-curve / constraint-modified inputs).
- **Planar (crack-like) flaws** — surface, embedded, and through-thickness cracks in plates, pipes, pressure vessels, and welded joints; recharacterisation rules; interaction and re-categorisation criteria.
- **Non-planar flaws** — volumetric defects (porosity, slag, lack of fusion treated as planar where appropriate) and shape-imperfection assessments (misalignment, weld profile).
- **Fatigue crack growth** — Paris-law integration of stress-intensity-factor ranges with sequence and threshold effects; coupling to S-N approaches in [[bs-7608]].
- **Leak-before-break (LBB)** — demonstration that a through-wall flaw will be detected by leakage before catastrophic rupture; pressure-vessel and pipework applications.
- **Residual stress treatment** — tabulated as-welded and post-weld-heat-treated residual-stress profiles for a wide range of weld geometries; combined with primary stress in the FAD ordinate.
- **Creep and creep-fatigue** — high-temperature crack initiation and growth assessment for plant operating in the creep regime.

### Comparison with API 579-1 / ASME FFS-1

BS 7910 and [[api-579-1-asme-ffs-1]] are the two dominant fitness-for-service codes in global engineering practice. They are **broadly aligned in technical philosophy** (FAD-based two-criteria fracture assessment, residual-stress superposition, fatigue-crack-growth integration) but **diverge in scope, structure, and method options**:

| Dimension | BS 7910 (2013) | API 579-1/ASME FFS-1 (2021) |
|---|---|---|
| Primary surface | Crack-like flaws + fatigue/creep | Full FFS suite — corrosion (Pt 4/5), pitting (6), HIC (7), distortion (8), creep (10), fire (11), brittle (3), cracks (9) |
| FAD levels | 1 / 2A / 2B / 3 (BS-specific labelling) | Levels 1 / 2 / 3 in Part 9 (cracks); option-based per part |
| Reference-stress / J | BS 7910 ref-stress library + J-from-FAD options | API 579 Annex 9F ref-stress; J via FAD or direct |
| Residual-stress profiles | Annex Q (as-welded, PWHT) | Annex 9D — overlaps but with different parametrisations |
| Constraint correction | Annex N (T-stress / Q-parameter aware) | Annex 9F constraint adjustment |
| LBB | Clause 9 + Annex T | Part 9 LBB procedure |
| Creep | Annex T (creep crack growth) | Part 10 (broader creep FFS) |
| Industry default | Offshore O&G, EU/UK fabrications, R6-aligned | Refining/petrochem, US-led pressure vessels |

The two codes generally produce **comparable end results** when applied to the same flaw with consistent inputs, but practitioners must not mix-and-match annexes across codes — residual-stress profiles, reference-stress solutions, and FAD curves are **internally calibrated** within each code.

## Edition history

| Edition | Year | Catalog file | parent_root |
|---|---|---|---|
| 1999 (with Amendment 1) | 1999 — `Guide on methods for assessing the acceptability of flaws in fusion welded structures` | `BSI/BS_7910_with_Amendment_1_(1999)_Guide_on_methods_for_assessing_the_acceptability_of_flaws_in_fusion_welded_structures.pdf` | `/mnt/ace/O&G-Standards/BSI` |
| 2005 (with Amendment 1) | 2005 — title broadens to `… flaws in metallic structures` (drops the "fusion welded" restriction) | `BSI/BS_7910_with_Amendment_1_(2005)_Guide_to_methods_for_assessing_the_acceptability_of_flaws_in_metallic_structures.pdf` | `/mnt/ace/O&G-Standards/BSI` |
| 2005 (unlocked variant) | 2005 — same edition, alternate file (unlocked PDF) | `BSI/BS_7910-_unlocked_with_Amendment_1_(2005)_Guide_to_methods_for_assessing_the_acceptability_of_flaws_in_metallic_structures.pdf` | `/mnt/ace/O&G-Standards/BSI` |
| 2013 | 2013 — major revision; introduces revised FAD options, updated residual-stress profiles, expanded creep clause | `BSI/BS_7910-2013.pdf` | `/mnt/ace/O&G-Standards/BSI` |
| 2013 (file variant) | 2013 — second on-disk copy with different `content_hash` (likely larger paginated/scanned variant; 72.8 MB vs 13.7 MB) | `BSI/BS_7910-2013_1.pdf` | `/mnt/ace/O&G-Standards/BSI` |

The BS 7910:2013 edition has been further updated by **Amendment 1 (2015)** in the publisher catalog (not present in the local mirror — verify via BSI Knowledge before normative citation). A successor edition is anticipated; consult the BSI catalog for current status.

Notable lineage notes:

- The **1999** edition was titled "*… flaws in fusion welded structures*"; the **2005** edition broadened scope to all metallic structures (welded or not), reflecting wider FFS adoption beyond weld inspection.
- BS 7910 superseded **PD 6493** (the legacy BSI flaw-assessment Published Document) when it was first issued in 1999.

## Key annexes

The 2013 edition's normative annex set is the working surface for most calc modules:

- **Annex A — Failure Assessment Diagram (FAD).** Defines the Level 1, 2A, 2B, and 3 FAD curves; ordinate K<sub>r</sub> (or √δ<sub>r</sub>), abscissa L<sub>r</sub>; cut-off L<sub>r</sub><sup>max</sup>. The default Option 2A curve is geometry- and material-independent; Option 2B uses material-specific stress-strain data.
- **Annex K — Residual stresses.** Tabulated as-welded and post-weld-heat-treated residual-stress distributions for plate butt welds, T-butt welds, set-on / set-in nozzles, pipe seam and girth welds, and repair welds. The membrane-plus-bending decomposition feeds the FAD primary+secondary stress sum.
- **Annex M — Fatigue crack growth.** Paris-law constants for ferritic and austenitic steels, aluminium alloys; threshold ΔK<sub>th</sub>; environmental modifiers (air, marine, freely-corroding seawater, cathodically-protected); R-ratio handling; integration procedure.
- **Annex N — Probabilistic FAD / reliability.** Monte Carlo and FORM/SORM treatment of uncertain inputs; partial-safety-factor calibration; complements the deterministic FAD for risk-based inspection (RBI) workflows.
- **Annex J — Creep crack initiation and growth.** C\* parameter framework; high-temperature reference-stress solutions; coupling to creep-fatigue interaction.
- **Annex T — Leak-before-break.** Through-wall-flaw stability assessment; leakage-rate prediction; safety-margin requirements for LBB-licensed components.

> Annex letters are normative within BS 7910:2013 and stable between Amendment 1 (2015) revisions; verify against the publisher edition for normative work.

## Cross-references

- [[api-579-1-asme-ffs-1]] — parallel US FFS standard; broadly aligned but with code-specific FAD calibration, residual-stress profiles, and reference-stress libraries. Do not mix annexes across codes.
- [astm-e399](astm-e399.md) — plane-strain fracture toughness K<sub>Ic</sub> (linear-elastic input to BS 7910 Level 1/2 FAD).
- [astm-e1820](astm-e1820.md) — J-integral and CTOD δ measurement (elastic-plastic toughness input to BS 7910 Level 2/3 and Annex A Option 3).
- [astm-e1921](astm-e1921.md) — Master Curve methodology for ferritic steel reference temperature T<sub>0</sub> (toughness-vs-temperature input for ductile-to-brittle transition assessments).
- [[bs-7448]] — UK companion fracture-mechanics toughness test methods (K<sub>Ic</sub>, CTOD, J, R-curves) feeding BS 7910 input data.
- [[bs-7608]] — UK fatigue design and assessment of steel structures; BS 7910 Annex M references BS 7608 for S-N approaches and is cross-cited for fatigue endurance.
- [[dnv-rp-c210]] — DNV recommended practice for probabilistic fatigue, complements BS 7910 Annex N for offshore structural reliability.
- [[api-1104]] — pipeline girth-weld code; **Annex A** (Alternative Acceptance Standards for Girth Welds) is the ECA route for pipeline construction welds and is methodologically aligned with BS 7910 Level 2.
- **R6** — the UK nuclear-industry sibling code (EDF Energy / formerly British Energy / CEGB). BS 7910 and R6 share the FAD framework; R6 retains additional nuclear-specific provisions (constraint-modified FAD, secondary-stress treatment for thermal transients) and is typically cited in parallel for nuclear safety cases.

## Sources

- [og-standards-bsi](../sources/og-standards-bsi.md) — BSI publisher catalog page summarising the 80-document BSI slice of `/mnt/ace/O&G-Standards/`, including all five on-disk BS 7910 edition variants.
- Catalog source: `/mnt/ace/O&G-Standards/_catalog.json` (catalog version 1.0.0, generated 2025-12-25).
- Publisher: BSI Knowledge — https://knowledge.bsigroup.com/ (search `BS 7910`).
- Calc-citation contract: `.claude/rules/calc-citation-contract.md` (workspace-hub) — governs how downstream digitalmodel calc modules emit `Citation` instances against this page.

## Notes

- This page is **metadata-only**; no clause text, figure, or table content is reproduced from the BS 7910 PDFs. All technical descriptions above are paraphrased general engineering knowledge.
- For normative ECA work, cite the BSI-published edition directly (BS 7910:2013+A1:2015 or the current edition at time of citation).
- Cross-check against R6 when assessing pressure-retaining components in nuclear safety cases; BS 7910 alone is not a sufficient nuclear citation.
