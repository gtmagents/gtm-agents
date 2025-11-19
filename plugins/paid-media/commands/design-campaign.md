---
name: design-campaign
description: Builds a paid media campaign plan across channels with targeting, creative, budget, and experiment structure.
usage: /paid-media:design-campaign --goal pipeline --budget 50000 --channels "LinkedIn,Meta,Google"
---

# Command: design-campaign

## Inputs
- **goal** – pipeline, revenue, awareness, lead gen, PLG activation, etc.
- **budget** – total spend available.
- **channels** – comma-separated list of platforms.
- **audiences** – optional persona or account segments.
- **timeline** – flight dates or campaign length.

## Workflow
1. **Brief Analysis** – clarify KPIs, attribution, constraints.
2. **Audience & Offer Mapping** – align personas/offers to channels and creative formats.
3. **Channel Plan** – allocate spend by channel/ad set, define bidding/optimization events.
4. **Creative & Experiment Plan** – propose hooks, asset needs, tests per channel.
5. **Measurement** – specify tracking setup, dashboards, guardrail metrics, post-launch review cadence.

## Outputs
- Campaign plan deck/table with budgets, targeting, messaging.
- Creative brief + asset checklist.
- Experiment backlog + KPI targets.

## Agent/Skill Invocations
- `media-strategist` – leads planning.
- `campaign-architecture` skill – enforces funnel/channel best practices.
- `creative-variants` skill – recommends asset variations.

---
