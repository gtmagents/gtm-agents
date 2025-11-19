---
name: plan-calendar
description: Builds a 4-week cross-channel social calendar aligned to launch or evergreen goals.
usage: /social-media:plan-calendar --goal product-launch --duration 4w --channels "LinkedIn,TikTok"
---

# Command: plan-calendar

## Inputs
- **goal** – e.g., product-launch, category-education, community-growth.
- **duration** – time window in weeks.
- **channels** – comma-delimited platforms.
- **pillars** – optional content themes or campaigns to prioritize.

## Workflow
1. **Brief Parsing** – identify KPIs, audience segments, compliance or legal constraints.
2. **Channel Allocation** – suggest posting cadence per platform based on goal.
3. **Content Matrix** – for each slot provide format, hook, CTA, asset guidance.
4. **Experiment Slots** – insert test ideas (hook types, CTAs, creators, boosts).
5. **Collab Requirements** – highlight cross-functional needs (design, video, product, legal).

## Outputs
- Calendar table (date, channel, objective, format, CTA, owner, asset status).
- KPI alignment summary and measurement plan.
- Experiment backlog + success thresholds.

## Agent/Skill Invocations
- `social-strategist` – ensures calendar ladders up to GTM goals.
- `platform-frameworks` skill – applies channel-specific best practices.
- `trend-research` skill – surfaces cultural moments or audio/meme opportunities.

---
