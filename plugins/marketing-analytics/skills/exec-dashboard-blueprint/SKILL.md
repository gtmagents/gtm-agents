---
name: exec-dashboard-blueprint
description: Layout and storytelling guide for marketing analytics executive dashboards.
---

# Executive Dashboard Blueprint Skill

## When to Use
- Preparing ELT/board-ready snapshots of marketing performance.
- Standardizing dashboard layout across BI, RevOps, and marketing teams.
- Packaging insights from `/marketing-analytics` commands into clear narratives.

## Framework
1. **Story Arc** – headline → KPI spine → risks/opps → actions.
2. **KPI Tiles** – awareness, demand, pipeline, revenue, efficiency metrics with traffic lights.
3. **Drill Cards** – channel, campaign, and audience breakouts linking to deeper views.
4. **Insight Callouts** – annotate anomalies, root causes, and required decisions.
5. **Action Register** – owners, due dates, and follow-ups surfaced alongside metrics.

## Templates
- 3-slide deck structure (headline, KPIs, actions).
- Dashboard wireframe with recommended chart types + layout.
- Annotation checklist ensuring context + next steps accompany data.
- **GTM Agents KPI Guardrail Sheet** – baseline vs target vs alert ranges for reach, pipeline, win rate, CAC payback @puerto/README.md#214-241.
- **Measurement Spec** – metric definitions, filters, refresh cadence, owner column.
- **Weekly Exec Packet** – combines dashboard screenshots, narrative summary, decision log (mirrors GTM Agents Data Analyst deliverable).

## Tips
- Limit each dashboard view to one primary objective to avoid overload.
- Embed links back to commands (`produce-campaign-report`, `monitor-channel-pacing`) for drilldowns.
- Archive monthly snapshots for trend storytelling.
- Adopt GTM Agents cadence: Monday data QA, Tuesday ELT preview, Thursday exec meeting, Friday retro + action register updates.
- Highlight which KPIs are within guardrail, trending to alert, or breaching (RAG) so leadership can react quickly.
- Pair with `docs/gtm-essentials.md` tools: Context7 for latest GA4 docs, Serena for patching data models, Sequential Thinking for retro facilitation.

## GTM Agents Dashboard Governance Overlay
1. **Data QA Loop** – run freshness + anomaly checks before distributing (log results in audit trail).
2. **Narrative Structure** – use Story Arc to link KPI shifts to drivers and required decisions.
3. **Action Register** – every dashboard delivery must include owner, due date, and status for prescribed actions.
4. **Escalation** – if guardrail breach persists >2 weeks, escalate to Chief Product Officer / Sales Director per GTM Agents governance.

## KPI Guardrails (GTM Agents Reference)
- Awareness (reach/impressions) ±8% window before alerting; >12% triggers campaign review.
- Pipeline add ≥3x quota per quarter; warn at 2.5x.
- Win rate ≥25% for in-quarter commit; escalate if <20%.
- CAC payback ≤14 months; escalate if >16 months.

## Weekly Exec Packet Outline
```
1. Headline + KPI spine (traffic lights per guardrail)
2. Insights & Drivers – 3 bullets tying KPI movement to channels/programs
3. Required Decisions – what leadership must approve/block
4. Action Register – owner, due date, status
5. Appendix – detailed drill cards + methodology
```

## Tool Hooks
- **Context7** – fetch current platform docs (GA4, Salesforce) referenced in measurement specs.
- **Serena** – update BI repo SQL notebooks or dbt models safely.
- **Sequential Thinking** – facilitate monthly retros and architecture of dashboard iterations.
- **Playwright** – capture dashboard screenshots or verify embedded web components before distribution.

---
