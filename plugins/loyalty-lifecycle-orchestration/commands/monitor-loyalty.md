---
name: monitor-loyalty
description: Evaluates loyalty program performance, member health, and experiment impact.
usage: /loyalty-lifecycle-orchestration:monitor-loyalty --window 30d --detail full --dimensions "tier,region"
---

# Command: monitor-loyalty

## Inputs
- **window** – time range (7d, 30d, quarter) for analysis.
- **detail** – summary | full report depth.
- **dimensions** – optional breakdowns (tier, cohort, region, channel).
- **experiments** – optional list of campaigns/tests to review.
- **alert_threshold** – optional KPI threshold for escalations.

### GTM Agents Pattern & Plan Checklist
> Mirrors GTM Agents orchestrator blueprint @puerto/plugins/orchestrator/README.md#112-325.

- **Pattern selection**: Monitoring typically runs **pipeline** (data → diagnostics → experiments → action plan). If diagnostics and experiment review can run in parallel, document a **diamond** segment with merge gate in the plan header.
- **Plan schema**: Save `.claude/plans/plan-<timestamp>.json` capturing window, feeds, task IDs, dependency graph (BI, CRM, experimentation), error handling, and success metrics (retention, liability, engagement lift, alert remediation time).
- **Tool hooks**: Reference `docs/gtm-essentials.md` stack—Serena for metric definition diffs, Context7 for SOPs/dashboards, Sequential Thinking for retro cadence, Playwright for verifying embedded dashboards.
- **Guardrails**: Default retry limit = 2 for failed data pulls or chart renders; escalation ladder = Member Insights Analyst → Loyalty Strategist → Exec sponsor.
- **Review**: Run `docs/usage-guide.md#orchestration-best-practices-puerto-parity` before distributing outputs to ensure dependencies + approvals captured.

## Workflow
1. **Data Pull** – collect enrollment, engagement, redemption, CSAT, and revenue metrics by selected window.
2. **Health Diagnostics** – evaluate tier mix, churn risk, point liability, and reward breakage.
3. **Member Insights** – surface segments needing nudges, upgrade opportunities, or win-back plays.
4. **Experiment Review** – summarize test results with lift, guardrails, and recommendations.
5. **Action Plan** – produce prioritized backlog (journey tweaks, rewards refresh, messaging updates).

## Outputs
- Dashboard snapshot with KPI trends and drilldowns.
- Risk/Opportunity list referencing data points and owners.
- Experiment readouts plus next-test suggestions.
- Plan JSON entry stored/updated in `.claude/plans` for audit trail.

## Agent/Skill Invocations
- `member-insights-analyst` – owns analysis + insights.
- `loyalty-strategist` – validates roadmap adjustments.
- `member-insights` skill – ensures segmentation + reporting standards.

## GTM Agents Safeguards
- **Fallback agents**: document substitutes (e.g., Loyalty Strategist covering Analyst) when analysts unavailable.
- **Escalation triggers**: if alert_threshold is breached twice or liability spikes, trigger GTM Agents rip-cord escalation and record remediation in plan JSON.
- **Plan maintenance**: update plan JSON/change log when metrics, thresholds, or tooling stack shift to keep audit history accurate.

---
