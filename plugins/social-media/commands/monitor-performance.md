---
name: monitor-performance
description: Aggregates channel analytics, benchmarks, and insights to optimize social programs.
usage: /social-media:monitor-performance --window 14d --channels "LinkedIn,X,Instagram"
---

# Command: monitor-performance

## Inputs
- **window** – reporting timeframe (7d, 14d, 30d).
- **channels** – platforms to include.
- **goals** – optional priorities (reach, engagement, traffic, pipeline, community growth).
- **benchmarks** – optional historical or industry comparison notes.

## Workflow
1. **Data Intake** – gather metrics (impressions, engagement rate, CTR, follower delta, saves/shares, referral traffic).
2. **Quality Checks** – normalize naming, remove paid boosts if needed, align attribution windows.
3. **Insight Generation** – highlight top/worst posts, creative themes, time-of-day patterns, audience growth.
4. **Action Plan** – recommend experiments (hooks, formats, creators, spend shifts) aligned to goals.
5. **Escalations** – flag brand risk or sentiment trends that require response plans.

## Outputs
- Dashboard-ready summary (tables + charts) per channel.
- Narrative analysis with insights + recommended actions.
- Experiment backlog prioritized by impact and effort.

## Agent/Skill Invocations
- `social-strategist` – validates alignment with GTM goals.
- `trend-research` skill – contextualizes data with culture/moment insights.
- `community-engagement` skill – surfaces community/programming implications.

---
