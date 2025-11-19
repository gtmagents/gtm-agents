---
name: identify-advocates
description: Scores customers for advocacy readiness and produces outreach roster.
usage: /customer-advocacy-orchestration:identify-advocates --goal "enterprise references" --segments "healthcare,finance" --limit 20
---

# Command: identify-advocates

## Inputs
- **goal** – advocacy need (references, case studies, speakers, advisory board).
- **segments** – optional list of industries, regions, or tiers to prioritize.
- **limit** – max number of candidates to surface.
- **exclusions** – optional filters (active escalations, NDA restrictions).
- **signals** – optional metrics to emphasize (product usage, NPS, expansion, community activity).

## Workflow
1. **Data Aggregation** – pull health scores, usage telemetry, NPS/CSAT, deal history, and community participation.
2. **Scoring Model** – apply readiness model (value delivered × relationship strength × risk factors).
3. **Opportunity Tagging** – classify advocates by potential program (reference call, webinar, story, council).
4. **Consent & Risk Review** – check existing permissions, legal constraints, and account escalations.
5. **Output Packaging** – generate roster with recommended outreach scripts and owners.

## Outputs
- Candidate list with score, fit notes, and suggested asks.
- Consent/compliance status per account.
- Outreach plan (owner, channel, timing) tied to CRM tasks.

## Agent/Skill Invocations
- `advocacy-strategist` – validates scoring and prioritization.
- `advocate-sourcing` skill – provides scoring framework + data templates.
- `reference-manager` – receives high-priority reference opportunities.

---
