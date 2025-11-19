---
name: analyze-performance
description: Consolidates webinar performance data, diagnoses drop-offs, and recommends optimizations.
usage: /webinar-automation:analyze-performance --window 30d --kpis "pipeline,attendance" --segments "enterprise,mid-market"
---

# Command: analyze-performance

## Inputs
- **window** – reporting range (7d, 30d, quarter).
- **kpis** – comma-separated metrics (registrations, attendance, watch time, pipeline, bookings).
- **segments** – optional persona/industry tiers.
- **experiments** – optional list of running tests to include.
- **source_data** – optional warehouse/BI query references.

## Workflow
1. **Data Consolidation** – merge platform stats, MAP data, CRM outcomes, survey results.
2. **Quality Checks** – ensure dedupe, UTM alignment, consistent stage definitions.
3. **Insight Generation** – highlight top-performing sessions, drop-off points, engagement drivers.
4. **Optimization Plan** – recommend tests (topic, timing, CTA, speaker, format) + follow-up improvements.
5. **Action Tracking** – assign owners + deadlines for recommended changes.

## Outputs
- Performance summary table with KPI deltas vs targets.
- Insight brief + prioritized actions.
- Experiment backlog updates + measurement plan.

## Agent/Skill Invocations
- `webinar-engagement-analyst` – leads analysis.
- `engagement-analytics` skill – provides measurement templates + diagnostics.
- `webinar-program-architect` – ensures insights feed back into strategy.

---
