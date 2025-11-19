---
name: design-campaign
description: Creates full-funnel email campaign plans with assets, segmentation, and cadences.
usage: /email-marketing:design-campaign --goal launch --audience startups --touches 5
---

# Command: design-campaign

## Inputs
- **goal** – conversion objective (launch, nurture, upsell, retention).
- **audience** – persona, lifecycle stage, or segment key.
- **touches** – number of emails in the sequence.
- **offers** – optional incentives, resources, or events to feature.

## Workflow
1. **Brief Intake** – parse goal + audience to determine messaging pillars.
2. **Audience & Personalization** – recommend segmentation logic, merge fields, dynamic modules.
3. **Touch Matrix** – draft touch-by-touch objectives, subject lines, preview text, CTA focus, content notes.
4. **Asset Checklist** – list creative needs (copy blocks, graphics, landing pages, tracking URLs).
5. **Measurement Plan** – specify KPIs per touch, success thresholds, and experiment ideas.

## Outputs
- Campaign overview (goal, target, primary offer, KPI table).
- HTML-ready copy briefs with personalization notes.
- QA checklist covering links, tracking, accessibility, and compliance.

## Agent/Skill Invocations
- `email-strategist` – requirements gathering and KPI translation.
- `drip-campaigns` skill – ensures best-practice cadence and pacing.
- `segmentation` skill – validates filters and suppression logic.

---
