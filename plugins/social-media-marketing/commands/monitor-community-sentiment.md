---
name: monitor-community-sentiment
description: Produces sentiment dashboard, risk alerts, and advocacy opportunities across social + community channels.
usage: /social-media-marketing:monitor-community-sentiment --window 14d --channels twitter,linkedin,community --alert-threshold high
---

# Command: monitor-community-sentiment

## Inputs
- **window** – lookback window (7d | 14d | 30d | custom).
- **channels** – comma-separated list (twitter, linkedin, instagram, tiktok, reddit, community, discord, slack).
- **alert-threshold** – low | medium | high (controls sensitivity and escalation path).
- **topics** – optional keywords or product lines to prioritize.
- **export** – dashboard | memo | csv (default dashboard).

## Workflow
1. **Data Aggregation** – pull social listening feeds, community platform exports, and support tags.
2. **Sentiment & Theme Analysis** – classify mentions by sentiment, topic, influencer tier, and severity.
3. **Risk & Opportunity Detection** – flag negative surges, competitor narratives, or advocate spikes.
4. **Action Routing** – generate follow-up tasks for comms, support, product, or community teams.
5. **Reporting Package** – compile dashboard/memo with highlights, risks, and recommended actions.

## Outputs
- Sentiment dashboard snapshot with charts and insight callouts.
- Escalation list with owners, due dates, and response guidance.
- Advocate/opportunity tracker for campaign activation.

## Agent/Skill Invocations
- `community-insights-lead` – leads listening + analysis.
- `social-strategy-director` – reviews risks + executive updates.
- `community-sentiment-dashboard` skill – structures reporting outputs.
- `community-advocacy-toolkit` skill – (optional) seeds advocate activation follow-ups.

---
