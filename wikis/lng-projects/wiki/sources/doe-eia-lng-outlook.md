---
title: "DOE / EIA LNG Outlook + Henry Hub"
slug: doe-eia-lng-outlook
domain: lng-projects
added: 2026-05-09
last_updated: 2026-05-09
sources:
  - "https://www.eia.gov/dnav/ng/ng_move_lng_a_EPL0_o_d_a.htm — EIA US LNG export-import movements"
  - "https://www.eia.gov/outlooks/steo/ — EIA Short-Term Energy Outlook (STEO)"
  - "https://www.eia.gov/outlooks/aeo/ — EIA Annual Energy Outlook (AEO)"
  - "https://www.energy.gov/fecm/ — DOE Office of Fossil Energy and Carbon Management (export authorizations)"
ingested: 2026-05-09
tags:
  - doe
  - eia
  - lng-export
  - henry-hub-pricing
  - short-term-energy-outlook
  - annual-energy-outlook
  - source-document
  - us-statistics
---

# DOE / EIA LNG Outlook + Henry Hub

> Metadata-first source page for US Department of Energy (DOE/FECM) and US Energy Information Administration (EIA) LNG-export statistics, Henry Hub pricing data, and the Short-Term and Annual Energy Outlooks. Companion to FERC for the US-regulatory dimension and to IGU/GIIGNL for the global-industry dimension.

## Source overview

The Energy Information Administration (EIA) publishes free, ungated US energy-statistics data including monthly LNG export and import volumes by destination, Henry Hub spot and futures price history, and forward outlooks (Short-Term Energy Outlook / STEO, monthly; Annual Energy Outlook / AEO, annual). Sister agency DOE/FECM (Office of Fossil Energy and Carbon Management, https://www.energy.gov/fecm/) issues the Natural Gas Act §3 export authorizations distinct from FERC's facility-siting authorizations. The EIA LNG export movements landing page (https://www.eia.gov/dnav/ng/ng_move_lng_a_EPL0_o_d_a.htm) is the canonical numeric series. STEO is monthly and forward-looking; AEO is annual and long-horizon. All EIA data is in the public domain (US government work).

## How to use this source

Cite EIA/DOE when a wiki page makes a **US-export-volume, Henry Hub price, or US-LNG-outlook claim**. EIA is authoritative for US-side trade flows, monthly destination breakdowns, capacity utilization at US terminals, and forward export forecasts. Henry Hub is the US gas-price benchmark and the contractual reference for most US-LNG offtake contracts; cite EIA's Henry Hub series rather than commercial price-reporting agencies (Platts, Argus) when the citation is in a public-facing wiki page. Use STEO for short-horizon forecasts (≤24 months); use AEO for long-horizon (≤30 years, scenario-based). Citation form: `(EIA, Natural Gas Monthly, [date])` or `(EIA STEO YYYY-MM)` or `(EIA AEO YYYY)`. **Do not** reproduce EIA tables or charts verbatim; cite the series page or report by URL + retrieval date.

## Coverage scope

**In scope**:
- US LNG export volumes by month and by destination country (EIA Natural Gas Monthly, dnav LNG movements series).
- US LNG import volumes (residual; mostly LNG re-exports and small Caribbean flows post-2016 export pivot).
- Henry Hub spot and futures price history (daily/weekly/monthly).
- Short-Term Energy Outlook (STEO) — monthly forward forecasts on US production, exports, prices.
- Annual Energy Outlook (AEO) — annual long-horizon scenario projections.
- DOE/FECM export-authorization metadata (FTA vs. non-FTA distinction; authorization volumes per terminal).

**Not in scope** (defer to other sources):
- Per-project facility-siting docket detail — defer to [`ferc-lng-portal`](ferc-lng-portal.md).
- Global trade flows beyond US-side counterparties — defer to [`igu-2025-lng-report`](igu-2025-lng-report.md) / [`igu-2024-lng-report`](igu-2024-lng-report.md).
- Importer-side receiving-terminal data and spot-market analytics — defer to [`giignl-annual-report`](giignl-annual-report.md).
- Vessel-side, cargo-containment, or marine-transfer technical detail — defer to concept pages.
- Regional benchmarks (TTF, JKM) — EIA reports US-centric prices; international benchmarks are commercial.

## Cross-wiki citation guidance

Cite EIA/DOE when:

- A concept or standards page makes a US export-volume, US capacity-utilization, or Henry Hub price claim.
- A page references US-LNG-export forward outlook (FID-supported export growth, expected 2030 capacity).
- A page distinguishes FTA vs. non-FTA export authorizations or references DOE/FECM authorization order numbers.
- A sibling wiki cites US gas-price assumptions for design-economic context (e.g., FSRU charter-rate sensitivity to Henry Hub).

Prefer FERC ([`ferc-lng-portal`](ferc-lng-portal.md)) when the claim is per-project siting or facility-design; prefer IGU/GIIGNL when the claim is global or non-US.

**Do NOT** cite EIA for non-US data; EIA's international-energy series (e.g., International Energy Statistics) is derived from third-party sources and is weaker than IGU/GIIGNL for global LNG framing.

## Updates + maintenance

- **EIA cadence**: Natural Gas Monthly (monthly, ~6-week lag); STEO (monthly, mid-month release); AEO (annual, typically Q1).
- **DOE/FECM cadence**: Export authorizations issued per project; aggregate authorization status published periodically.
- **Henry Hub series**: Daily updates from EIA; settlement series sourced from NYMEX/CME.
- **Refresh trigger**: STEO citations should be refreshed monthly for "current outlook" claims; AEO annually. Volume and price data citations should record retrieval date because EIA backfills and revises prior months in subsequent releases.
- **URL stability**: EIA dnav landing-page URLs are stable; AEO and STEO landing pages are stable; specific report-edition PDFs are versioned by year.

## Cross-references

- [`sources/ferc-lng-portal`](ferc-lng-portal.md) — sibling US-regulatory companion (facility-siting + per-docket detail; FERC's siting authority complements DOE/FECM's export authority).
- [`sources/igu-2025-lng-report`](igu-2025-lng-report.md) — global all-tier companion; cite for global context around US-export claims.
- [`sources/igu-2024-lng-report`](igu-2024-lng-report.md) — prior-year IGU edition.
- [`sources/giignl-annual-report`](giignl-annual-report.md) — importer-side companion; cite for destination-side context on US export flows.
- Concept pages that should cite this source: [`concepts/lng-project-shapes`](../concepts/lng-project-shapes.md), [`concepts/lng-project-lifecycle`](../concepts/lng-project-lifecycle.md), [`concepts/lng-regulatory-framework`](../concepts/lng-regulatory-framework.md), [`concepts/lng-liquefaction-processes`](../concepts/lng-liquefaction-processes.md).
- Standards pages: [`standards/ferc-18-cfr-153`](../standards/ferc-18-cfr-153.md), [`standards/phmsa-49-cfr-193`](../standards/phmsa-49-cfr-193.md).
