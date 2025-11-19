---
name: follow-up-impact
description: Builds post-event follow-up plan plus impact report framework.
usage: /event-marketing:follow-up-impact --event "Summit" --window 30d --kpis "pipeline,expansion"
---

# Command: follow-up-impact

## Inputs
- **event** – event identifier.
- **window** – measurement horizon (7d/30d/quarter).
- **kpis** – comma-separated metrics (pipeline, bookings, success metrics, NPS, meetings).
- **segments** – optional segmentation (persona, region, tier).
- **playbooks** – optional reference to follow-up sequences.

## Workflow
1. **Attendee Data Prep** – consolidate registrations, attendance, engagement, notes.
2. **Routing & Follow-up** – recommend SDR/CS outreach tiers, nurture sequences, partner touchpoints.
3. **Measurement Framework** – map KPIs to data sources, dashboards, attribution rules.
4. **Insight Summary** – capture qualitative feedback, booth conversations, survey highlights.
5. **Retro Plan** – schedule retro, assign action items, document learnings.

## Outputs
- Follow-up matrix (segment → owner → action → deadline).
- KPI dashboard spec + SQL/Looker queries.
- Retro template pre-filled with event context.

## Agent/Skill Invocations
- `field-program-manager` – coordinates regional follow-up.
- `program-ops` skill – enforces routing/automation standards.
- `field-playbooks` skill – suggests nurture/cadence templates.

---
