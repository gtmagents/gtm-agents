---
name: optimize-nurture
description: Builds a nurture optimization plan with insights, experiments, and remediation tasks.
usage: /lead-nurture-orchestration:optimize-nurture --window 30d --kpis "activation,pipeline" --segments "enterprise"
---

# Command: optimize-nurture

## Inputs
- **window** – reporting period (7d, 14d, 30d, quarter).
- **kpis** – comma-separated metrics (opens, clicks, conversion, pipeline, velocity, unsub).
- **segments** – optional audience filters.
- **experiments** – optional list of running tests to review.
- **alerts** – optional thresholds for escalations.

### GTM Agents Pattern & Plan Checklist
> Based on GTM Agents orchestrator blueprint @puerto/plugins/orchestrator/README.md#112-325.

- **Pattern selection**: Optimization usually runs **pipeline** (data → insights → experiments → action plan → governance). If insights and experiment analysis can proceed in parallel, log a **diamond** segment + merge gate.
- **Plan schema**: Update `.claude/plans/plan-<timestamp>.json` with data sources, query/metric owners, experiment IDs, remediation tasks, risk guardrails, error handling, and success targets (activation %, pipeline lift, unsub ceiling).
- **Tool hooks**: Reference `docs/gtm-essentials.md` (Serena for pipeline diffs + data pulls, Context7 for platform docs, Sequential Thinking for retrospection, Playwright for QA of revised assets).
- **Guardrails**: Define retry limit (default 2) for automation fixes; escalation ladder = Nurture Analytics Partner → Marketing Ops Partner → Revenue Operations if alerts breach thresholds.
- **Review**: Run `docs/usage-guide.md#orchestration-best-practices-puerto-parity` before sharing to ensure agent coverage + deliverables are complete.

## Workflow
1. **Data Consolidation** – MAP stats, CRM pipeline, product usage, SDR assist metrics.
2. **Insight Detection** – highlight stages with drop-offs, fatigue, or high unsub rates.
3. **Experiment Analysis** – summarize test results, significance, and rollout recommendations.
4. **Action Plan** – propose new tests, content refresh, audience refinements, or sequencing changes.
5. **Governance** – log owners, deadlines, and dependencies for each recommendation.

## Outputs
- Optimization brief (insights, impact, recommended action, owner, due date).
- Updated experiment tracker with verdicts and next tests.
- Alert + SLA tracker for segments needing fast intervention.
- Plan JSON entry stored/updated in `.claude/plans` for auditability.

## Agent/Skill Invocations
- `nurture-analytics-partner` – leads analysis.
- `nurture-testing` skill – validates experiment rigor.
- `lifecycle-cadence` skill – checks pacing vs fatigue thresholds.

## GTM Agents Safeguards
- **Fallback agents**: record substitutes (e.g., Lifecycle Cadence covering analytics) when primary owners unavailable.
- **Escalation triggers**: if activation/pipeline KPIs fall below guardrail for two consecutive windows, invoke lifecycle rip-cord and notify Marketing + Sales leadership.
- **Plan maintenance**: every optimization cycle must append results + changes to the plan JSON and status packets, matching GTM Agents audit expectations.

---
