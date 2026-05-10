---
title: "HNS Convention 2010 — Hazardous and Noxious Substances"
tags: [maritime-law, convention, liability, compensation]
sources:
  - ../sources/maritime-liability-conventions.md
added: 2026-04-07
last_updated: 2026-05-10
---

# HNS Convention 2010 — Hazardous and Noxious Substances

## Summary

| Property | Value |
|----------|-------|
| Scope | HNS spills (chemicals, LNG, LPG, persistent + non-persistent oil cargoes, packaged dangerous goods) |
| Key Feature | Two-tier compensation modelled on CLC: shipowner strict liability + HNS Fund |
| Status | **Not yet in force** — 2010 Protocol awaiting the 12-state ratification threshold (5 of 12 as of 2026) |
| Reference | IMO LEG/CONF.17/10 (2010 Protocol consolidating 1996 Convention) |
| Standards-resolver | [standards/hns-convention-2010](../standards/hns-convention-2010.md) |

## Details

The HNS Convention extends the CLC-style civil-liability + dedicated-fund architecture from persistent oil cargoes to the much broader category of hazardous and noxious substances carried by sea. It channels strict liability to the registered shipowner up to a tonnage-indexed cap, requires compulsory insurance evidenced by an HNS Certificate, and superimposes a second-tier HNS Fund financed by levies on cargo receivers. Unlike [clc-1992](./clc-1992.md), which has been in force since 1996, the HNS regime is **not yet operational**: the original 1996 Convention failed to attract sufficient ratifications (largely because of disputes over packaged-goods reporting and LNG receiver attribution), and the 2010 Protocol — drafted to fix those defects — is itself still short of the 12-state activation threshold.

This entry was migrated from `knowledge/seeds/maritime-liabilities.yaml` and has since been deepened with article-level doctrinal notes, named-incident counterfactuals, and a multi-criteria comparison against the parallel regimes under [clc-1992](./clc-1992.md), [bunkers-convention-2001](./bunkers-convention-2001.md), and [opa-90](./opa-90.md). Because the regime is not in force, the analysis is necessarily counterfactual — "what an HNS-applicable incident would have looked like" — anchored to the working CLC framework as the operative analogue.

## Three-Tier Compensation Architecture (Planned)

When (and if) the 2010 Protocol enters force, the HNS regime will operate as a layered compensation stack closely modelled on the CLC + IOPC Fund architecture, with one important difference: the HNS Fund is internally split into **general** and **separate accounts** to keep oil, LNG, LPG, and other-HNS cargo classes from cross-subsidizing one another.

| Tier | Instrument | Liable / paying party | Cap (per incident, 2010 Protocol) | Trigger |
|------|------------|------------------------|-----------------------------------|---------|
| 1 | HNS Convention | Registered shipowner | 10M SDR (under 2,000 GT) → 100M SDR ceiling, tonnage-scaled | Strict, channeled |
| 2 | HNS Fund (general account) | Receivers of bulk HNS in contracting states | 250M SDR aggregate (incl. tier 1) | Tier 1 inadequate; non-LNG / non-LPG / non-persistent-oil HNS |
| 2′ | HNS Fund (separate accounts) | Per-cargo-class receivers (oil / LNG / LPG) | Same 250M SDR aggregate envelope, ring-fenced by cargo class | Tier 1 inadequate; cargo-class-specific incident |
| 3 | (No Supplementary Fund) | — | — | HNS does not yet have a third-tier supplementary protocol analogous to the [clc-1992](./clc-1992.md) 2003 Supplementary Fund |

The separate-accounts mechanism is the single most distinctive structural feature of HNS: under the 1996 Convention LNG and LPG receivers objected to general-account pooling on the grounds that gas-cargo casualties were rare but catastrophic and would unfairly burden routine chemical-cargo receivers. The 2010 Protocol's separate-accounts compromise — one for oil, one for LNG, one for LPG, with the residual general account covering everything else — is what unlocked the renewed ratification push.

### Interaction with adjacent funds

A particular HNS-cargo casualty does not draw on the [clc-1992](./clc-1992.md) IOPC Fund: the two regimes are mutually exclusive by Article 4 of HNS, which excludes "pollution damage" already governed by CLC (i.e., persistent oil cargo from a tanker). HNS therefore fills three distinct gaps that CLC + Bunkers leave open:

- **Chemical / non-oil cargo from any vessel** — neither CLC (oil only) nor [bunkers-convention-2001](./bunkers-convention-2001.md) (bunker fuel only) reaches a styrene, DVB, or sulphuric-acid spill from a chemical tanker.
- **LNG / LPG cargo casualties** — covered by HNS separate accounts; fall entirely outside CLC and Bunkers.
- **Packaged dangerous goods (IMDG Code cargo)** in containers — covered by HNS as packaged HNS; outside both CLC and Bunkers; this is the [msc-flaminia-2012](../entities/msc-flaminia-2012.md) gap.

## Article-by-Article Doctrinal Notes

The following are doctrinal-synthesis summaries — convention text is not reproduced. Refer to the IMO LEG depositary publication for the operative wording of the 2010 Protocol.

- **Article 1 (Definitions — what counts as HNS)** — defines HNS by reference to a layered list of IMO instruments: bulk liquid HNS by reference to the IBC Code Chapter 17 list (chemicals carried by chemical tankers), bulk liquefied gases by reference to the IGC Code Chapter 19 list, packaged dangerous goods by reference to the IMDG Code, solid bulk by reference to the IMSBC Code's MHB (Materials Hazardous only in Bulk) entries, and persistent + non-persistent oil cargoes by reference to MARPOL Annex I. This referential-list architecture is the principal source of administrative complexity and the reason the 1996 Convention struggled with reporting compliance.
- **Article 3 (Strict liability and channeling)** — strict liability is channeled exclusively to the registered shipowner, with defences narrower than the corresponding [clc-1992](./clc-1992.md) Article III defences: HNS expressly does not exempt the shipowner where the damage results from the hazardous nature of the cargo itself even if the shipper failed to disclose, **unless** the shipper's failure to disclose was the proximate cause and the shipowner had no actual or constructive knowledge. This shifted-disclosure-burden rule is one of the principal commercial concerns flagged by P&I clubs.
- **Article 7 (Compulsory insurance and HNS Certificate)** — vessels carrying HNS in any quantity (no minimum tonnage threshold like CLC's 2,000-tonne floor) must maintain insurance up to the Article 9 cap, evidenced by a state-issued HNS Certificate. This is administratively heavier than CLC because it applies to nearly the entire merchant fleet — every container ship carrying IMDG cargo, every chemical tanker, every gas carrier.
- **Article 9 (Limitation gateway)** — shipowner may limit liability to the tonnage-indexed HNS cap unless the spill resulted from the shipowner's "personal act or omission, committed with the intent to cause such damage, or recklessly and with knowledge that such damage would probably result." Identical wording to [clc-1992](./clc-1992.md) Article V — same high break-of-limitation bar.
- **Article 12 (HNS Fund operation)** — HNS Fund is constituted as a separate legal person, financed by post-incident levies on receivers of HNS in contracting states above per-cargo-class thresholds, and pays compensation when (a) the shipowner is exempt under Article 7, (b) the shipowner is unable to meet liability, or (c) the damage exceeds the Article 9 cap. The internal general-account / separate-accounts split (oil, LNG, LPG, residual) determines which receivers contribute for which incident class.
- **Article 18 (Time-bar)** — claims against the shipowner extinguish three years from date of damage / six years from date of incident, whichever is earlier; HNS Fund claims have parallel limits. Consistent with the [clc-1992](./clc-1992.md) Article VIII regime.

## Why the Convention Is Not Yet in Force

The 2010 Protocol enters into force 18 months after the 12th state has both deposited its instrument of accession and reported the previous calendar year's HNS receivers above specified thresholds. As of 2026 only **5 states** have completed both steps — Norway, the United Kingdom, Canada (signed, ratification advancing), the Netherlands, and South Africa — leaving the regime well short of activation.

The structural reasons for slow uptake reveal where the doctrinal arc remains contested:

- **Major flag states are absent**. The United States is committed to the parallel [opa-90](./opa-90.md) framework and shows no domestic appetite for ratifying a competing international regime. Japan, China, South Korea, Singapore, Panama, and Liberia — collectively most of the world's tanker tonnage and the most important open-registry flags — have not advanced ratification. Without their participation the HNS Fund's contribution base would be too narrow to credibly support the 250M SDR aggregate cap.
- **Receiver-side reporting compliance**. Contracting states must annually report receipts of HNS by their domestic receivers, broken down by cargo class. The 1996 Convention foundered on the practical impossibility of identifying all receivers of packaged HNS (every importer of containerized IMDG cargo). The 2010 Protocol limits packaged-goods reporting but the residual administrative burden remains a barrier for smaller maritime states.
- **Separate-accounts politics**. LNG receivers, in particular, have lobbied flag states to hold ratification pending clarification of the LNG separate-account contribution mechanism. Until LNG-importing states (Japan, Korea, China, India, Spain) commit, the LNG separate account would be financially fragile.
- **Insurance-market response uncertainty**. P&I clubs have prepared model HNS Certificate wording but have not yet committed to issuance pricing in the absence of a clear entry-into-force date. The chicken-and-egg dynamic — flag states wait for insurance pricing, insurers wait for flag-state demand — has slowed momentum.

The current realistic estimate (per IMO LEG progress reports through 2024) is that the regime would enter force in the late-2020s at earliest, contingent on at least two more major-tonnage flag states ratifying and on the LNG-importer bloc resolving the separate-account question.

## Worked Examples — Counterfactual Named Incidents

Because the regime is not yet operational, the doctrinal-synthesis examples are necessarily **counterfactuals**: incidents to which HNS *would* have applied had it been in force, paired with the regime that actually governed the response. This counterfactual mode is itself the core teaching device for HNS — practitioners reason from the gap between the "as-handled" disposition and the "as-HNS-would-have-handled" disposition.

### MSC Flaminia (2012) — packaged-goods gap that HNS would close

The [msc-flaminia-2012](../entities/msc-flaminia-2012.md) container-ship fire in the mid-Atlantic involved divinylbenzene (DVB) cargo in containers that auto-polymerized exothermically and triggered a multi-day cargo-hold fire with three crew fatalities and substantial hull damage. Under the regime as it stood in 2012, [clc-1992](./clc-1992.md) did not apply (no persistent oil cargo from a tanker), [bunkers-convention-2001](./bunkers-convention-2001.md) did not apply to the cargo loss (only to bunker spillage, which was secondary), and the resulting disposition fell under English [llmc-1996](./llmc-1996.md) limitation proceedings combined with bilateral commercial litigation between the carrier and cargo interests. **Had HNS been in force**, the DVB cargo and the surrounding packaged IMDG containers would have triggered Article 1 packaged-HNS coverage; the shipowner would have faced strict liability under Article 3 up to the tonnage-indexed cap; the HNS Fund general account would have addressed claims exceeding the cap; and the litigation matrix would have been substantially compressed. Flaminia is the canonical illustration of the packaged-goods gap.

### Sanchi (2018) — borderline-cargo classification

The [sanchi-2018](../entities/sanchi-2018.md) collision off Shanghai involved an Iranian tanker carrying ~136,000 tonnes of natural-gas condensate that burned for a week before sinking, with total loss of 32 crew. Condensate sits at the doctrinal boundary: it is classified by MARPOL Annex I as a non-persistent oil cargo but behaves operationally more like an HNS bulk-liquid hazard (high volatility, vapour-cloud explosion risk, near-complete burn-off rather than persistent slick). The actual response was handled under [clc-1992](./clc-1992.md) tier-1 channeling because condensate falls within the "oil" definition of Article I. **Under HNS**, condensate would arguably have routed through the oil separate account of the HNS Fund rather than through the IOPC Fund — preserving CLC-equivalent shipowner liability but shifting the second-tier compensation pool. Sanchi therefore illustrates not a gap-filling scenario (CLC did apply) but a **regime-allocation** question: which fund pays second-tier claims when the cargo is borderline?

### Stolt-Nielsen Bow Pioneer (1989) — pre-HNS chemical tanker baseline

The Bow Pioneer chemical-tanker casualty in 1989 (a Stolt-Nielsen vessel, sulphuric-acid release in port) is the canonical pre-HNS chemical-tanker example. At the time no international convention reached chemical-tanker cargo claims at all — neither CLC (oil only), nor LLMC (general limitation but not a dedicated chemical-spill regime), nor any predecessor to HNS. Recovery proceeded entirely under domestic tort and contractual claims against the shipowner and the cargo interest. The 1996 HNS Convention was drafted in part in direct response to this gap, and the Bow Pioneer incident is routinely cited in IMO LEG preparatory documents as the proof-of-need for HNS. **Under HNS in force**, this incident would have produced a clean Article 3 strict-liability claim against the shipowner up to the Article 9 cap with HNS Fund tier-2 backstop — precisely the architecture the regime is designed to deliver.

## HNS vs CLC vs Bunkers vs OPA-90 — Multi-Criteria Comparison

The four regimes form a layered cargo-coverage map, with HNS designed to fill the chemicals + gas + packaged-goods gap that CLC and Bunkers do not reach.

| Criterion | HNS 2010 (planned) | [clc-1992](./clc-1992.md) | [bunkers-convention-2001](./bunkers-convention-2001.md) | [opa-90](./opa-90.md) (US-only) |
|-----------|---------------------|---------------------------|---------------------------------------------------------|---------------------------------|
| Cargo class covered | Bulk + packaged HNS (chemicals, LNG, LPG, oil, MHB solids, IMDG packaged) | Persistent oil cargo from tankers only | Bunker fuel only (any vessel) | Oil discharge into US navigable waters (cargo or bunker) |
| Vessel scope | Any vessel carrying HNS | Tankers carrying persistent oil cargo in bulk | Any sea-going vessel | Any vessel in US waters / EEZ |
| Liability standard | Strict, channeled to registered shipowner | Strict, channeled to registered shipowner | Strict, joint among shipowner / bareboat charterer / manager / operator | Strict, joint-and-several across responsible parties |
| Cap (per incident) | 100M SDR tier-1 ceiling; 250M SDR tier-1+2 aggregate | 89.77M SDR tier-1; 203M SDR tier-1+2; 750M SDR with Supplementary Fund | LLMC-indexed (no dedicated cap) | Statutory dollar cap; forfeit on gross negligence |
| Compulsory insurance | Yes — HNS Certificate, no tonnage threshold | Yes — Blue Card, ≥ 2,000 tonnes oil cargo | Yes — Blue Card, ≥ 1,000 GT | Yes — US COFR |
| Second-tier fund | HNS Fund (general + separate accounts) | 1992 IOPC Fund + 2003 Supplementary Fund | None — limitation governed by [llmc-1996](./llmc-1996.md) | Domestic Oil Spill Liability Trust Fund |
| Forum | Contracting-state courts where damage occurred | Contracting-state courts where damage occurred (Articles IX/XI) | Contracting-state courts where damage occurred | US federal courts |
| In force | **No** (5 of 12 ratifications) | Yes (1996) | Yes (2008) | Yes (1990) |

The matrix shows why HNS is structurally important even while not yet in force: it is the only regime in the layered map that addresses chemical-tanker, gas-carrier, and packaged-IMDG-container cargo casualties as a coherent civil-liability + compensation-fund architecture.

## What Changes When HNS Enters Force

For each principal stakeholder class, entry into force is a structural rather than incremental change. The "before / after" map below tracks where exposure shifts.

- **Shipowners and operators** — must carry an HNS Certificate for every voyage involving HNS cargo, on every vessel (no tonnage threshold). For container operators this is administratively heavy: every laden container voyage is potentially HNS-covered because IMDG cargo is endemic. P&I clubs are expected to issue HNS Blue Cards alongside existing CLC and Bunkers Blue Cards, and the certification stack at the dock will grow to three certificates for any vessel carrying both bunkers and HNS-eligible cargo.
- **P&I clubs (International Group)** — face restructured cover: the existing pooling and reinsurance architecture will need to absorb the HNS Article 9 cap exposure on top of the existing CLC and Bunkers exposures. Pricing models drafted by the International Group's subcommittees in 2018-2024 anticipate a modest premium uplift but a significant operational uplift in certificate issuance volume. The most exposed clubs are those concentrated in chemical-tanker and LNG/LPG-carrier classes.
- **Cargo receivers** — face a new contribution obligation. Bulk receivers above per-cargo-class thresholds (oil, LNG, LPG, other-HNS) will be levied post-incident to fund tier-2 payouts. This is the primary reason ratification has stalled in importer states with concentrated LNG/LPG receiver bases.
- **Coastal states** — gain a much wider compensation tool. Pre-HNS, a chemical-tanker casualty leaves coastal states with only domestic tort + LLMC limitation; post-HNS, they have CLC-equivalent shipowner strict liability + a dedicated Fund. This is the principal political case for ratification in coastal states with heavy chemical-tanker traffic (Mediterranean, Baltic, Singapore Strait, English Channel).
- **IMO LEG and the prospective HNS Fund administrators** — gain operational mandate; the IOPC Fund secretariat in London is widely expected to administer the HNS Fund as a second concurrent fund, sharing infrastructure with the 1992 IOPC Fund.
- **Insurance-market reinsurers** — face a new aggregate-cap exposure roughly comparable in scale to the existing CLC + Supplementary Fund exposure, but with a different cargo-mix profile (gas-carrier catastrophic-tail risk as the dominant feature).

## Cases Testing This Convention

(Counterfactual until in force — see [Worked Examples](#worked-examples--counterfactual-named-incidents) above.)

[msc-flaminia-2012](../entities/msc-flaminia-2012.md), [sanchi-2018](../entities/sanchi-2018.md).

## Cross-References

- **Sibling concept**: [clc-1992](./clc-1992.md) — HNS modelled on CLC's two-tier structure (shipowner strict liability + dedicated fund); the working analogue against which the not-yet-in-force HNS regime is taught.
- **Standards-page companions (metadata resolvers)**:
  - [standards/hns-convention-2010](../standards/hns-convention-2010.md) — paired metadata-resolver page (publisher, consolidated-edition, certificate machinery, ratification tracker).
  - [standards/clc-1992](../standards/clc-1992.md) — sibling civil-liability instrument for persistent oil cargo (the explicit Article 4 carve-out).
  - [standards/bunkers-convention-2001](../standards/bunkers-convention-2001.md) — bunker-fuel civil-liability counterpart (HNS does not reach bunker-only casualties).
  - [standards/marpol-73-78](../standards/marpol-73-78.md) — Annex II (chemical tankers) and Annex III (Harmful Substances Carried by Sea in Packaged Form) are the operational counterparts to HNS's civil-liability layer; HNS's Article 1 cargo definitions cross-reference MARPOL Annex I.
  - [standards/llmc-1996](../standards/llmc-1996.md) — general limitation regime that currently governs HNS-style casualties in the absence of HNS entry-into-force.
  - [standards/opa-90](../standards/opa-90.md) — US-domestic civil-liability regime for oil; the US is not expected to ratify HNS.
- **Concept companions**:
  - [concepts/clc-1992](./clc-1992.md) — the working-regime model HNS replicates.
  - [concepts/bunkers-convention-2001](./bunkers-convention-2001.md) — adjacent civil-liability regime in the layered map.
  - [concepts/opa-90](./opa-90.md) — parallel US regime explaining one of the principal ratification holdouts.
  - [concepts/marpol-73-78](./marpol-73-78.md) — operational pollution-prevention layer that HNS's civil-liability layer presupposes.
  - [concepts/llmc-1996](./llmc-1996.md) — fallback general-limitation regime.
  - [concepts/environmental-liability](./environmental-liability.md) — overarching concept under which HNS sits as the chemicals + gas + packaged-cargo specialization.
  - [concepts/limitation-of-liability](./limitation-of-liability.md) — Article 9 limitation gateway in its broader context.
  - [concepts/flag-state-jurisdiction](./flag-state-jurisdiction.md) — the certification chain underpinning Article 7 compulsory insurance.
- **Related entities (counterfactual incidents)**:
  - [entities/msc-flaminia-2012](../entities/msc-flaminia-2012.md) — packaged-IMDG container fire; canonical HNS-gap counterfactual.
  - [entities/sanchi-2018](../entities/sanchi-2018.md) — borderline condensate-cargo classification; regime-allocation question between CLC and HNS.
  - [entities/mv-erika-1999](../entities/mv-erika-1999.md), [entities/mv-prestige-2002](../entities/mv-prestige-2002.md) — CLC-regime baselines for comparison.
- **Source**: [Maritime Liability Conventions](../sources/maritime-liability-conventions.md).
- **Related cases index**: [Maritime Law Cases](../sources/maritime-law-cases.md).
