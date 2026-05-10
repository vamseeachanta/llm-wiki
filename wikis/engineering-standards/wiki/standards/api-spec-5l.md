---
title: "API SPEC 5L — Line Pipe (bounded summary)"
tags: ["api", "standards", "line-pipe", "specification", "metadata-only"]
added: 2026-05-02
last_updated: 2026-05-09
domain: engineering-standards
code_id: api-spec-5l
publisher: API
revision: "44e-2007"
revision_source: /mnt/ace/O&G-Standards/API/Specifications/
publisher_current_edition: "46e-2018 (with addenda through 2024)"
methodology_status: "stale-as-of-publisher-cycle"
verified_on: 2026-05-02
public_url: https://www.api.org/products-and-services/standards
sources:
  - /mnt/ace/O&G-Standards/API/Specifications/API_SPEC_5L_44th_Ed_(2007)_Line_Pipe.pdf
extraction_policy: metadata-only
raw_copy_allowed: false
---

# API SPEC 5L — Line Pipe (bounded summary)

## Scope

API Specification 5L establishes manufacturing requirements, dimensions, mechanical and chemical properties, hydrostatic-test requirements, marking, and supplementary inspection options for steel line pipe used in pipeline transportation systems for the oil and gas industry. It covers seamless and welded line pipe (longitudinally welded by SAW, HFW/ERW, or laser-welding processes; helically welded by SAW) for transmission and gathering of hydrocarbons, water, and steam. The specification harmonises substantially with ISO 3183 (*Petroleum and natural gas industries — Steel pipe for pipeline transportation systems*); the two documents are technically equivalent for most grades and product specification levels and are published as a joint API/ISO document on the modern cycle. The standard is the foundational specification consumed by pipeline-transportation design codes (ASME B31.4 for liquids and B31.8 for gas) and by U.S. DOT pipeline-safety regulations under 49 CFR Parts 192 and 195.

## Revision history

- **1928 origin** — API 5L first issued as the U.S. industry standard for line pipe, marking the start of API's role in pipeline-material specification.
- **Long lineage through the 20th century** — the specification evolved alongside the growth of long-distance transmission pipelines in North America; the modern grade-designation system (Grade B, X42, X52, ..., X80) hardened into the form used today.
- **42nd Edition (2000)** — significant restructuring to align with the emerging two-product-specification-level (PSL 1 / PSL 2) framework that distinguishes basic line pipe (PSL 1) from higher-quality line pipe with stricter Charpy-V impact, chemical-composition, and yield-to-tensile-ratio requirements (PSL 2).
- **44th Edition (2007)** — On-disk reference revision (`/mnt/ace/O&G-Standards/API/Specifications/API_SPEC_5L_44th_Ed_(2007)_Line_Pipe.pdf`); first edition published jointly with ISO 3183 as a fully harmonised API/ISO document.
- **45th Edition (2012)** — incremental update covering sour-service requirements, supplementary requirement specifications (SR family), and updated Charpy-V impact requirements for low-temperature service.
- **46th Edition (2018, with addenda through 2024)** — currently active publisher edition; users emitting calc citations against current projects should re-pin to the publisher's currently active edition. The on-disk 44th Edition lags by approximately 17 years.

## Key sections

API 5L is structured around two product specification levels and a graded family of strength designations:

- **PSL 1 (Product Specification Level 1)** — basic line pipe with the standard manufacturing, chemical-composition, and mechanical-property requirements; suitable for moderate-service transmission and gathering applications.
- **PSL 2 (Product Specification Level 2)** — higher-quality line pipe with tighter chemistry caps (carbon equivalent, sulfur, phosphorus), mandatory Charpy-V impact testing at specified test temperatures, controlled yield-to-tensile ratio, and stricter NDE; required by most modern transmission-pipeline owner specifications.
- **Grade designations** — by minimum specified yield strength: **Grade B** (≈241 MPa / 35 ksi), **X42, X46, X52, X56, X60, X65, X70, X80** (yield strength ksi-equivalent in the X-number; X42 is 42 ksi minimum specified yield, X80 is 80 ksi minimum specified yield). Higher-strength grades (X90, X100, X120) are addressed in the modern editions and in supplementary requirement specifications, used selectively on long-distance high-pressure transmission pipelines for wall-thickness and weight reduction.
- **Sour-service supplementary requirement** — Annex H / SR sour-service framework links to NACE / AMPP MR0175 (ISO 15156) for hydrogen-sulfide-resistant materials in sour-hydrocarbon service.
- **Supplementary requirements (SR family)** — fracture-arrest, ductile-fracture-arrest, low-temperature impact, hydrogen-induced cracking, sulfide-stress-cracking, and other owner-elected supplementary requirements activated by the purchase order.

The specification covers dimensions (outside diameter, wall thickness, length, straightness), tolerances, weldability requirements, hydrostatic-test requirements, NDE (ultrasonic / radiographic / magnetic-particle / liquid-penetrant requirements by product type and PSL level), marking, and inspection / acceptance procedures.

## Practitioner application

In practice, API 5L is the cited basis for:

- **Line-pipe procurement** — the mill-test certificate and Manufacturer's Quality Plan are written to API 5L; PSL 2 with named supplementary requirements is the typical specification baseline for modern transmission projects.
- **Hoop-stress and longitudinal-stress allowables** — pipeline design codes (ASME B31.4 and B31.8) consume the API 5L Specified Minimum Yield Strength (SMYS) directly in the hoop-stress design equation `S_h = (P × D) / (2 × t)` capped against `F × E × T × SMYS` (design factor F, longitudinal-joint factor E, temperature derating factor T).
- **Welding qualification basis** — line-pipe welding is qualified to API 1104 (Welding of Pipelines and Related Facilities), which keys to the API 5L base-metal specification.
- **Sour-service material selection** — when the line pipe is in sour-hydrocarbon service, the API 5L Annex H / SR framework cross-links to AMPP MR0175 (formerly NACE MR0175) for HIC-resistant, SSC-resistant material qualification.
- **In-service assessment** — fitness-for-service evaluations (API 579-1 / ASME FFS-1) and integrity-management programmes (API 1160 for liquids, ASME B31.8S for gas) reference back to the as-built API 5L specification when assessing remaining strength after corrosion or mechanical damage.

## Industry adoption

- **U.S. DOT pipeline-safety regulations** — 49 CFR Part 192 (gas pipelines) and Part 195 (liquid pipelines) reference API 5L (or ISO 3183, given the harmonisation) as the acceptable line-pipe specification basis for newly constructed transmission and gathering pipelines.
- **ASME B31.4 / B31.8** — the design codes consume API 5L SMYS values directly in the hoop-stress design equation; pipeline operators and EPC contractors specify API 5L PSL 2 grades on essentially all new transmission construction.
- **International acceptance** — via the API/ISO 3183 harmonisation, API 5L is effectively the global reference specification for line pipe; national regulators in Canada (CSA Z662 for oil-and-gas pipeline systems), Australia (AS 2885), and Europe (EN 1594 with supplementary CEN/EN 10208 for low-pressure line pipe) reference API 5L equivalents or the ISO 3183 substrate.
- **Offshore and subsea pipelines** — DNV-ST-F101 (Submarine Pipeline Systems) and ISO 13628 / API 17 series for subsea systems likewise specify line pipe to API 5L (with supplementary requirements) as the underlying material specification, with DNV adding offshore-specific supplementary requirements.

## Why this page exists

Resolver target for digitalmodel `Citation` instances per `.claude/rules/calc-citation-contract.md`. Contains no clause text, no chemistry / strength bands, and no dimensional tables from the source. Downstream callers wire line-pipe SMYS values, grade-to-yield correspondence, and PSL-level-driven supplementary requirements through this page rather than parsing the source PDF. The on-disk 44th Edition (2007) lags the publisher's currently active 46th Edition (2018, with addenda through 2024) by approximately 17 years; calc callers MUST treat the on-disk artifact as **stale-as-of-publisher-cycle** and re-pin to the current edition before emitting design-pressure or design-stress citations.

## Where to find the full text

- Raw PDF: `/mnt/ace/O&G-Standards/API/Specifications/API_SPEC_5L_44th_Ed_(2007)_Line_Pipe.pdf` (read-only, vendor-derivative; do not copy into git per #2482)
- Publisher catalog: https://www.api.org/products-and-services/standards
- Internal callers: `digitalmodel/src/digitalmodel/` pipeline-design and assessment modules resolving line-pipe SMYS by grade

## Cross-references

- [api-rp-1111](api-rp-1111.md) — offshore hydrocarbon pipelines, LSD companion design code
- [asme-b31-4](asme-b31-4.md) — liquid-pipeline transportation design code consuming API 5L SMYS
- [asme-b31-8](asme-b31-8.md) — gas-pipeline transportation design code consuming API 5L SMYS
- [ampp-mr-0175-pt1](ampp-mr-0175-pt1.md) — sour-service material selection (cross-linked from API 5L Annex H)
- [api-1104](api-1104.md) — welding-qualification companion for API 5L line pipe
- [Calc citation contract](../../../../../.claude/rules/calc-citation-contract.md)
