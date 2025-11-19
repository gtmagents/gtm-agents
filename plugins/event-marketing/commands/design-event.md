---
name: design-event
description: Generates an event brief with objectives, audience, agenda, experience design, and KPIs.
usage: /event-marketing:design-event --type "executive dinner" --goal pipeline --region "US West"
---

# Command: design-event

## Inputs
- **type** – webinar, conference, dinner, field event, partner activation, etc.
- **goal** – pipeline, expansion, community, product adoption, etc.
- **region** – geography or segment.
- **budget** – optional amount.
- **timeline** – target month/date.

## Workflow
1. **Objective Mapping** – align event purpose with KPIs and attendee personas.
2. **Experience Blueprint** – recommend agenda, format, speakers, demos, activations.
3. **Content & Offer Plan** – define narratives, assets, giveaways, CTAs.
4. **Promotion Strategy** – outline invite journey, partner amplification, paid/organic mix.
5. **Measurement Plan** – specify registration targets, attendance, engagement SLAs, post-event routing.

## Outputs
- Event brief (objectives, agenda, deliverables, KPIs).
- Creative/messaging checklist.
- Promotion + follow-up plan outline.

## Agent/Skill Invocations
- `event-strategist` – leads strategy + alignment.
- `event-briefs` skill – provides standardized template + guardrails.
- `field-program-manager` – adds localization guidance if region-specific.

---
