---
title: "Papkov (2026) — Drilling-Tender AI Agent Prototype (LinkedIn post)"
tags: [drilling-tender, rfp, afe, offset-well-analysis, ai-agent, procurement, drilling-engineering, practitioner-essay]
sources:
  - linkedin-papkov-2026-drilling-tender-ai-agent
added: 2026-05-13
last_updated: 2026-05-13
---

# Papkov (2026) — Drilling-Tender AI Agent Prototype

Raw URL: https://www.linkedin.com/posts/alex-papkov_drillingengineering-oilfieldtechnology-ai-share-7459348778580357120-_FWU

Author: Alex Papkov (practitioner account, 618 followers at time of capture). Format: LinkedIn post (technical problem-statement + AI-prototype announcement). Date observed: 2026-05-13.

## Relevance

The founding source for the `drilling-engineering/` wiki domain. Papkov identifies a practitioner-stated gap: operators — particularly independents — award drilling service contracts based on **incomplete technical evaluation**, because the existing procurement platforms (Arkestro, Enverus are named) handle pricing and workflow but cannot evaluate whether a bidder's claims are consistent with drilling technical requirements and the operator's own offset-well history. The post pitches an AI-agent prototype that closes the gap and solicits anonymized well plans, AFEs, and bid packages for pilot testing.

The post is significant for this wiki not as a primary source for drilling-engineering technical claims — it is not — but because it states the **data-quality dependency** that motivates the wiki's entire scope: AI-assisted drilling-tender evaluation requires a rigorous corpus of rig specs, drilling equipment specifications, well-plan / AFE template structure, offset-well analysis methodology, and tender-evaluation rubrics. This wiki is the data-quality layer for downstream agents of the kind Papkov describes.

## Key claims (as presented by the author)

- **Procurement-platform gap.** Arkestro and Enverus handle pricing optimization and workflow but cannot evaluate the technical consistency of a drilling-tender bid against the operator's drilling requirements and offset history.
- **Practitioner problem statement.** "Most operators — particularly independents — award drilling service contracts based on incomplete technical evaluation."
- **AI-agent prototype capability surface** (claimed; methodology not detailed in the post):
  1. Generates technically rigorous RFPs from well plans and AFEs.
  2. Evaluates bids against verifiable offset data.
  3. Flags inconsistencies in bidder submissions.
  4. Produces structured award recommendations with quantified uncertainty.
- **Operational dependencies named but not detailed.** Well plans, AFEs, offset wells, bid packages — these are the data artifacts the agent operates on. Each warrants its own concept page in this wiki.

## Limitations of this source

The post does not specify the prototype's algorithmic approach (no model architecture, no retrieval strategy, no rubric structure), does not benchmark against a baseline, does not quantify "rigorous" or "verifiable" in measurable terms, and does not specify the data schemas the agent ingests for well plans / AFEs / bid packages. The follow-up comment ("Come on now, people. Help me to help you.") suggests the project is at the data-acquisition stage — the prototype is a pitch for pilot partners rather than a published methodology. A skeptical reader should treat the post as a **problem statement and prototype announcement**, not as a methodology source.

## How this maps to the wiki

| Topic in post | Wiki location (planned / target) |
|---|---|
| Well plan | `concepts/well-plan.md` (planned) |
| AFE — Authorization For Expenditure | `concepts/afe-authorization-for-expenditure.md` (planned) |
| Offset-well analysis | `concepts/offset-well-analysis.md` (planned) |
| Drilling-tender RFP / bid evaluation | `concepts/drilling-tender-evaluation.md` (planned) |
| Rig technical requirements (the "drilling technical requirements" the post names) | `entities/` rig-class and individual-rig pages + `concepts/` rig-spec taxonomy (planned) |
| Procurement platforms (Arkestro, Enverus) | Out of scope — the AI-agent landscape, not drilling engineering proper |

## Use as a wiki source

Cite as the **founding motivation** for the drilling-engineering wiki domain and as a literature data point on AI applied to drilling-tender evaluation. Do **not** cite as a primary source for any technical claim about drilling rigs, well design, AFE construction, or offset-well methodology — defer those to the API specs (4F / 7K / 8C), IADC Drilling Manual, IOGP guidance, and the SPE peer-reviewed drilling literature when those source pages are written.

## Follow-on work seeded by this ingest

The four "data artifacts the agent operates on" (well plan, AFE, offset well, bid package) and the four claimed capabilities (generate RFP, evaluate bids, flag inconsistencies, quantify uncertainty) form a natural concept-page roadmap. The Seed Roadmap section of [overview.md](../overview.md) lists the standards and concept ingests anticipated as immediate next steps.
