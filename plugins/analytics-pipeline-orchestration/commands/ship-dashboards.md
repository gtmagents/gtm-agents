---
name: ship-dashboards
description: Creates a dashboard launch plan with visualization specs, enablement steps, and monitoring.
usage: /analytics-pipeline-orchestration:ship-dashboards --use_case "pipeline velocity" --tool looker --audience "exec,sales"
---

# Command: ship-dashboards

## Inputs
- **use_case** – dashboard or report purpose.
- **tool** – BI platform (Looker, Tableau, Mode, Sigma, PowerBI).
- **audience** – comma-separated audiences.
- **access** – optional role-based access requirements.
- **alerts** – optional alert thresholds or anomaly rules.

### GTM Agents Pattern & Plan Checklist
> Based on GTM Agents orchestrator blueprint @puerto/plugins/orchestrator/README.md#112-325.

- **Pattern selection**: Dashboard launches typically run **pipeline** (requirements → visualization → publishing → enablement → monitoring). If publishing + enablement can proceed in parallel, log a **diamond** segment and merge gate.
- **Plan schema**: Save `.claude/plans/plan-<timestamp>.json` with objective, visualization stages, task IDs, parallel groups, dependency graph (models, permissions), error handling, and success metrics (adoption %, freshness, alert SLA).
- **Tool hooks**: Reference `docs/gtm-essentials.md` stack—Serena for repo/LookML diffs, Context7 for BI platform docs, Sequential Thinking for rollout retros, Playwright for UI QA of embedded dashboards.
- **Guardrails**: Default retry limit = 2 for failed publishes/alerts; escalation path = BI Publisher → Analytics Modeling Lead → RevOps/Exec sponsor.
- **Review**: Use `docs/usage-guide.md#orchestration-best-practices-puerto-parity` before execution to confirm agents, dependencies, deliverables.

## Workflow
1. **Requirement Review** – confirm metrics, filters, drill paths, narrative structure.
2. **Visualization Spec** – define layout, chart types, color systems, accessibility notes.
3. **Publishing Steps** – build dashboards, set permissions, schedule refreshes, configure alerts.
4. **Enablement & Rollout** – plan walkthroughs, documentation, office hours, feedback channels.
5. **Monitoring** – track usage analytics, data freshness, dashboard performance, enhancement backlog.

## Outputs
- Dashboard spec (wireframe, chart list, metrics dictionary).
- Enablement kit (loom/video, doc, FAQ, adoption plan).
- Monitoring + enhancement tracker.
- Plan JSON entry stored/updated in `.claude/plans` for audit trail.

## Agent/Skill Invocations
- `bi-publisher` – leads visualization + enablement.
- `visualization-patterns` skill – enforces design best practices.
- `quality-gates` skill – ensures data + refresh checks.

## GTM Agents Safeguards
- **Fallback agents**: document substitutes (e.g., Analytics Data Strategist covering BI Publisher) when specialists unavailable.
- **Escalation triggers**: if adoption, freshness, or alert guardrails breach twice in 48h, escalate to Analytics + GTM leadership and trigger rollback plan.
- **Plan maintenance**: update plan JSON/change log whenever visual specs, access rules, or monitoring hooks change to maintain GTM Agents-grade auditability.

---
