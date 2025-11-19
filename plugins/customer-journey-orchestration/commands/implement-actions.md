---
name: implement-actions
description: Converts prioritized journey initiatives into coordinated execution plans with measurement.
usage: /customer-journey-orchestration:implement-actions --initiative "Onboarding Refresh" --timeline 60d --owners "marketing,product"
---

# Command: implement-actions

## Inputs
- **initiative** – name of the prioritized journey program.
- **timeline** – duration or deadline (e.g., 60d, 2026-01-15).
- **owners** – comma-separated list of accountable teams.
- **budget** – optional resource or dollar allocation.
- **kpis** – optional key metrics to monitor.

### GTM Agents Pattern & Plan Checklist
> Mirrors GTM Agents orchestrator blueprint @puerto/plugins/orchestrator/README.md#112-325.

- **Pattern selection**: Implementation runs **pipeline** (plan → workstreams → change mgmt → measurement → governance). If workstreams can execute in parallel, document a **diamond** segment with merge gate in the plan header.
- **Plan schema**: Save `.claude/plans/plan-<timestamp>.json` capturing initiative, timeline, task IDs, parallel groups, dependency graph (marketing, product, ops, enablement), error handling, and success metrics (KPI targets, VOC improvements).
- **Tool hooks**: Reference `docs/gtm-essentials.md` stack—Serena for instrumentation/config diffs, Context7 for SOPs, Sequential Thinking for retros, Playwright for experience QA if required.
- **Guardrails**: Default retry limit = 2 for blocked workstreams; escalation ladder = Journey Ops Owner → CX Strategist → CCO/Product leadership.
- **Review**: Run `docs/usage-guide.md#orchestration-best-practices-puerto-parity` before execution to confirm owners, dependencies, deliverables.

## Workflow
1. **Plan Assembly** – pull prioritized gap details, define scope, deliverables, and success metrics.
2. **Workstream Breakdown** – create task tree (content, product, ops, enablement) with owners + dependencies.
3. **Change Management** – map approvals, communications, enablement, and risk mitigation steps.
4. **Measurement Setup** – configure instrumentation, dashboards, VOC checkpoints, and cadence of reviews.
5. **Launch + Governance** – track execution status, surface blockers, and log outcomes for future journey reviews.

## Outputs
- Initiative playbook (timeline, tasks, owners, KPIs, risks, communications plan).
- Dashboard + tracker links for ongoing monitoring.
- Post-implementation recap capturing results and learnings.
- Plan JSON entry stored/updated in `.claude/plans` for audit trail.

## Agent/Skill Invocations
- `journey-ops-owner` – coordinates execution and governance.
- `governance` skill – ensures approvals + documentation.
- `voice-of-customer` skill – keeps measurement tied to customer feedback loops.

## GTM Agents Safeguards
- **Fallback agents**: document substitutes (e.g., CX Strategist covering Journey Ops Owner) if leads unavailable.
- **Escalation triggers**: if KPIs miss guardrails twice or blockers persist beyond SLA, escalate to CX/Product leadership per GTM Agents rip-cord.
- **Plan maintenance**: update plan JSON/change log whenever scope, owners, or measurement cadences change to maintain GTM Agents audit parity.

---
