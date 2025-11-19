---
name: monitor-sla
description: Tracks MQL→SQL SLA performance, raises alerts, and recommends corrective actions.
usage: /sales-handoff-orchestration:monitor-sla --segment enterprise --window 7d --threshold 85
---

# Command: monitor-sla

## Inputs
- **segment** – filter for program/team to analyze.
- **window** – time period (24h, 7d, 30d) for metrics.
- **threshold** – SLA compliance target percentage.
- **notify** – optional channel or email for alert delivery.
- **dimensions** – optional breakdowns (owner, geo, campaign).

### GTM Agents Pattern & Plan Checklist
> Mirrors GTM Agents orchestrator blueprint @puerto/plugins/orchestrator/README.md#112-325.

- **Pattern selection**: SLA monitoring usually follows a **pipeline** (aggregation → calculation → diagnostics → actions → alerts). If diagnostics + recommendations can run in parallel, log a **diamond** segment and merge gate.
- **Plan schema**: Save `.claude/plans/plan-<timestamp>.json` with objective, data sources, task IDs, dependencies (dashboards, alert channels), error handling, and success metrics (SLA %, response time, queue depth).
- **Tool hooks**: Reference `docs/gtm-essentials.md` stack—Serena for CRM automation diffs, Context7 for MAP/CRM field docs, Sequential Thinking for retro cadence, Playwright for form QA when routing fixes require front-end checks.
- **Guardrails**: Default retry limit = 2 for failed data pulls/alerts; escalation ladder = RevOps Director → Sales Manager → CRO.
- **Review**: Run `docs/usage-guide.md#orchestration-best-practices-puerto-parity` before execution to confirm agents, dependencies, deliverables.

## Workflow
1. **Data Aggregation** – pull MAP/CRM timestamps (MQL created, accepted, touched) plus routing metadata.
2. **SLA Calculation** – compute response time, acceptance time, conversion rates vs targets.
3. **Drill-down Diagnostics** – highlight segments, owners, or campaigns below threshold.
4. **Action Recommendations** – prescribe playbooks (re-prioritize queues, add enablement, adjust routing rules).
5. **Alert Packaging** – send summary + deep dive dashboards to notify channels.

## Outputs
- SLA dashboard snapshot with compliance %, aging pipeline, at-risk cohorts.
- Recommendation list with owners and due dates.
- Optional incident ticket for severe breaches.
- Plan JSON entry stored/updated in `.claude/plans` for audit trail.

## Agent/Skill Invocations
- `revops-director` – reviews systemic issues and approves remediation.
- `sla-tracking` skill – ensures methodology + thresholds are standardized.
- `routing-logic` skill – recommends rule adjustments causing delays.

## GTM Agents Safeguards
- **Fallback agents**: document substitutes (e.g., Sales Manager covering RevOps Director) when specialists unavailable.
- **Escalation triggers**: if SLA compliance stays below threshold for two consecutive windows, trigger escalation to Sales + Marketing leadership and open an incident per GTM Agents rip-cord.
- **Plan maintenance**: update plan JSON/change log whenever thresholds, alert channels, or remediation playbooks change.

---
