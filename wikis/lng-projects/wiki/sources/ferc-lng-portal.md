---
title: "FERC LNG Portal + eLibrary"
slug: ferc-lng-portal
domain: lng-projects
added: 2026-05-09
last_updated: 2026-05-09
sources:
  - https://www.ferc.gov/natural-gas/lng
ingested: 2026-05-09
tags: ["ferc", "lng-projects", "regulatory-docket", "public-information", "terminal-list", "us-regulation"]
---

# FERC LNG Portal + eLibrary

> Metadata-first source page for the US Federal Energy Regulatory Commission's authoritative LNG-project information portal and the eLibrary docket-search system. Public-URL pointers only — no FERC docket text or filing content is reproduced in this wiki.

## Summary

FERC's LNG portal (https://www.ferc.gov/natural-gas/lng) and the companion eLibrary docket-search system (https://elibrary.ferc.gov/eLibrary/search) together form the authoritative free public access surface for US LNG project information. The portal publishes the working list of US LNG terminals — existing, FERC-approved, and proposed — with status and basic siting information. eLibrary holds the per-project dockets keyed by docket number (CP-series for siting/construction certificates, e.g. `CP25-XXX`, `CP26-XXX`), and surfaces every public filing in a docket: applicant Resource Reports, FERC environmental and safety review documents, public comments, agency consultations, project status updates, and the ultimate Order issuing or denying authorization. For US-jurisdiction LNG-project work, this is the primary regulatory record.

## Why this is foundational for the wiki

FERC dockets are the most-detailed authoritative source for any US LNG project. The thirteen Resource Reports (siting through engineering design and reliability — see `standards/ferc-18-cfr-153.md`) are part of the public docket and contain the engineering, environmental, and operations basis-of-design that downstream concept and entity pages may cite. Engineering studies, environmental impact statements (EISs and EAs under NEPA), third-party reviews, and vendor specifications surface in the docket over the project lifecycle from pre-filing through post-construction monitoring. For US-LNG project work the wiki cites FERC dockets the way standards pages cite catalog edition history — as the canonical pointer-of-record. Concept pages on US-LNG topics (siting, vapor-cloud exclusion, marine waterway suitability, sendout capacity certifications) without a FERC-docket citation are at risk of being weakly grounded relative to peers that do cite.

## Portal structure

- **LNG terminal list page**: https://www.ferc.gov/industries-data/natural-gas/lng — existing, FERC-approved, and proposed terminals with status and high-level siting metadata.
- **eLibrary search**: https://elibrary.ferc.gov/eLibrary/search — per-docket document search by accession number, docket number, or full-text query across all FERC filings.
- **Project filings**: per-docket Resource Reports 1–13 plus applicant supplemental engineering submittals and FERC environmental/safety review documents.
- **Order issued page**: FERC Orders and Notices for project authorizations, amendments, extensions of time, and conditions-of-approval compliance filings.
- **NEPA review documents**: Environmental Impact Statements (EISs) and Environmental Assessments (EAs) published per project under FERC's NEPA-lead authority.

## Major LNG project dockets (representative)

| Project | Docket # | Status |
|---------|----------|--------|
| Sabine Pass | CP08-77, CP14-12 | Operating since 2016 |
| Cove Point | CP13-113 | Operating since 2018 |
| Plaquemines | CP19-46, CP21-490 | Operating since 2024 |
| Commonwealth | CP21-110 | Authorized 2022, financing-dependent |
| Driftwood | CP17-117 | Authorized 2019 |
| Port Arthur | CP15-490 | Authorized + under-construction |

Docket numbers are FERC-assigned identifiers; resolve them via eLibrary search.

## Citation usage

When concept or entity pages cite specific US LNG project facts (export capacity, FID date, liquefaction technology, vendor selection, conditions of FERC approval), they should cite the FERC docket by accession or docket-and-order pair, e.g. `FERC Docket CP19-46-000, Order issued 2022-02-17`. Pages **must not** reproduce docket text, applicant filings, or FERC review-document content beyond a pointer-and-scope reference; the eLibrary URL plus docket/order identifier is sufficient. Where concept pages summarize FERC review findings, summarize from the public Order text or the EIS executive summary, not from applicant Resource Reports (which contain proprietary engineering data filed under public-record terms but are still the applicant's authored content).

## Cross-references

Bidirectional cross-links to standards pages and adjacent regulatory sources:

- [`standards/ferc-18-cfr-153.md`](../standards/ferc-18-cfr-153.md) — the regulation governing how LNG-import/export-terminal siting and construction dockets are filed (Resource Report structure, pre-filing process, application content).
- [`standards/phmsa-49-cfr-193.md`](../standards/phmsa-49-cfr-193.md) — companion safety regulation for onshore LNG facilities; PHMSA and FERC dockets are co-referenced because PHMSA's siting and operations rules are incorporated into FERC's facility-safety review.
- [`standards/nfpa-59a.md`](../standards/nfpa-59a.md) — Standard for the Production, Storage, and Handling of LNG, incorporated by reference into PHMSA 49 CFR 193 and thus into FERC's facility-safety review.
- DOE/FECM (https://www.energy.gov/fecm/) — separate from FERC siting jurisdiction: DOE's Office of Fossil Energy and Carbon Management issues the LNG **export authorization** for non-FTA destinations under Natural Gas Act §3, while FERC issues the **facility-siting and construction authorization** under NGA §3 for the physical terminal. Both authorizations are required for any export terminal.
