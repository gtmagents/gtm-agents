---
name: lifecycle-mapping
description: Use when designing automation programs aligned to lifecycle stages, SLAs,
  and GTM objectives.
---

# Lifecycle Mapping Frameworks Skill

## When to Use
- Blueprinting onboarding, expansion, renewal, or churn-prevention journeys.
- Aligning automation programs with account stages, ICP tiers, or health scores.
- Auditing existing programs for gaps or over-saturation.

## Framework
1. **Stage Definition** – awareness, activation, adoption, expansion, advocacy (customize per business).
2. **Signal Library** – activation events, product usage milestones, score thresholds, purchase behaviors.
3. **Touch Architecture** – how many touches per stage, channel mix, personal vs automated.
4. **SLA Matrix** – entry/exit criteria, owner, response time, success metrics.
5. **Experiment Layer** – embed test slots to iterate hooks, cadences, or offers per stage.

## Templates
- Lifecycle heat map (stage vs metric vs automation coverage).
- SLA worksheet (stage, trigger, owner, time-to-response, fallback).
- Journey backlog board (ideas, prioritized, building, live, measuring).
- **GTM Agents Campaign Planning Checklist** – captures marketing director playbook @puerto/README.md#183-212.
- **KPI Guardrails Sheet** – track reach, engagement, SQL impact, CAC payback with min/max thresholds.
- **Status Packet Template** – weekly single-slide update mirroring GTM Agents project-manager format @puerto/TEAM-STRUCTURE.md#193-204.

## Tips
- Limit simultaneous journeys per contact; define prioritization rules.
- Include manual checkpoints (CSM/AE) for high-touch segments.
- Document every assumption so experiments can deliberately challenge them.
- Lock KPIs before build starts and refuse scope creep until metrics + owners are confirmed.
- Borrow GTM Agents's cadence: **Plan → Build → QA → Launch → Inspect** so reporting lines know when to approve or intervene.
- Pair every automation change with a "rip-cord" procedure the Sales Director or Ops Lead can trigger if leading indicators degrade.

## GTM Agents Campaign Blueprint (Adopted)
Use this five-stage blueprint when large GTM initiatives require orchestration across demand gen, lifecycle, and RevOps teams:

1. **Stage 1 – Briefing & Alignment**
   - Confirm objective, ICP, offer, timeline, and budget.
   - Capture cross-functional stakeholders (Marketing Director, Sales Director, RevOps Lead) and escalation paths.
2. **Stage 2 – Architecture**
   - Map lifecycle stages to channels + automations.
   - Define entry/exit criteria, personalization logic, and compliance constraints.
   - Assign data availability checks (Serena) + documentation pulls (Context7) if needed.
3. **Stage 3 – Build & QA**
   - Break work into swimlanes (journey build, content, data, QA) and track in backlog.
   - Require Playwright or similar browser QA for every externally facing experience.
4. **Stage 4 – Launch & Monitor**
   - Set Day 0/Day 7 KPI guardrails (e.g., form conversion ≥ 4%, unsubscribe ≤ 0.4%).
   - Route anomalies to the Operations Lead with a rollback procedure.
5. **Stage 5 – Inspect & Iterate**
   - Use Sequential Thinking to run structured retros (what worked, what failed, hypotheses for next wave).
   - Feed learnings back into lifecycle heat map + SLA matrix.

## Status Reporting Template
```
Campaign: <Name>
Week Ending: <Date>

1. Highlights (wins, blockers, escalations)
2. KPI Snapshot (target vs actual vs guardrail)
3. Journey Coverage (stage, channel, live %)
4. Next 5 Actions (owner, due date)
5. Risks & Decisions Needed (include GTM Agents-style RAG)
```

Use this template to sync with Sales Director, Partnership Manager, and Project Manager counterparts each week.

---
