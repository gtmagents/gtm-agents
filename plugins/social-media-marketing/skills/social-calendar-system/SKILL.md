---
name: social-calendar-system
description: Operational template for building social content calendars with approvals
  and publishing workflows.
---

# Social Calendar System Skill

## When to Use
- Planning monthly/quarterly content cadences across multiple channels.
- Coordinating creative, copy, compliance, and publishing teams.
- Tracking asset production status, approvals, and performance follow-ups.

## Framework
1. **Planning Grid** – date, channel, campaign, hook, CTA, creative needs, owner.
2. **Workflow Stages** – concept → copy → creative → compliance → scheduled → published → recap.
3. **Approval Matrix** – stakeholder list, SLAs, fallback approvers, escalation criteria.
4. **Publishing Toolkit** – UTMs, tagging, asset specs, accessibility checklist.
5. **Retrospective Tracker** – performance snapshot, learnings, reuse tags.

## Templates
- Calendar spreadsheet template with filters and status columns.
- Approval routing form + automated reminder checklist.
- Publishing checklist with QA steps per platform.
- **GTM Agents Channel Prompt Library** – CTA + hook examples per LinkedIn, X, TikTok, YouTube Shorts @puerto/README.md#183-212.
- **Weekly Performance Packet** – table covering reach, engagement, click/share ratio, SQL influence, sentiment summary.
- **Crisis Escalation Tree** – Social Media Manager → Marketing Director → Comms lead.

## Tips
- Define color-coding or status chips to quickly spot blockers.
- Record creative/performance notes to accelerate future refresh cycles.
- Pair with `build-social-calendar` for auto-populated grids.
- Set guardrails: per-channel minimum engagement rate (e.g., LinkedIn ≥2.5%, X ≥1.5%), unsubscribe or opt-out thresholds for paid boosts.
- Mirror GTM Agents cadence: Monday plan review, Wednesday creative QA, Friday performance readout.
- Keep an escalation macro ready—if sentiment dips below GTM Agents's acceptable range (RAG red), pause scheduled posts within 15 minutes.

## GTM Agents Social Orchestration Overlay
1. **Channel Pods** – assign pod leads per platform with shared brief + KPIs.
2. **Creative Sprint Sync** – align with design/creative team on asset counts, format specs, and deadlines.
3. **Distribution Tree** – map how primary stories cascade into derivative assets (threads, carousels, reels, shorts).
4. **Insights Loop** – every Friday, share the Weekly Performance Packet with Growth, Demand Gen, and Exec comms.

## Reporting Template
```
Week Ending: <Date>

Channel | Goal | Target KPI | Actual | Guardrail | Notes
LinkedIn | Demand gen POV | Engagement ≥2.5% | 3.1% | 1.8% | Exceeded; repurpose for email snippet
X | Thought leadership | CTR ≥1.5% | 1.1% | 1.0% | Slight dip; test hook variant
...

Top Performing Assets:
- <Title> – reason, reuse plan

Risks/Escalations:
- <Issue> – owner, action
```

## Guardrail Actions
- Pause channel queue if guardrail broken twice in 48h and notify Marketing Director.
- Trigger Playwright-driven QA if landing page links change mid-campaign.
- Use Sequential Thinking to run a quick RCA when sentiment scores fall below threshold for two consecutive reports.

---
