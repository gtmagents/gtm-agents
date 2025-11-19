---
name: run-launch
description: Creates launch execution runbook covering timeline, comms, instrumentation, and go/no-go gates.
usage: /product-launch-orchestration:run-launch --product "AI Copilot" --window 14d --channels "email,press,webinars"
---

# Command: run-launch

## Inputs
- **product** – launch identifier.
- **window** – time horizon for execution (e.g., 14d, 30d).
- **channels** – comma-separated channels/workstreams.
- **dependencies** – optional gating items (feature flag, pricing, legal approval).
- **alerts** – optional monitoring thresholds (error rate, adoption, PR sentiment).

### GTM Agents Pattern & Plan Checklist
> Inspired by GTM Agents orchestrator guidance @puerto/plugins/orchestrator/README.md#112-325.

- **Pattern selection**: Start with **pipeline** (timeline → comms → instrumentation → gates → command center). Use **diamond** when channel workstreams can run in parallel; note selection in plan header.
- **Plan schema**: Save `.claude/plans/plan-<timestamp>.json` with objective, stages, parallel groups, agent assignments, context passing (e.g., feature readiness), error handling, and success criteria (launch KPIs).
- **Tool hooks**: Reference `docs/gtm-essentials.md` (Serena for doc/code patches, Context7 for platform docs, Sequential Thinking for retros, Playwright for pre-launch QA).
- **Guardrails**: Define retry strategy (default 2 attempts) and escalation ladder (Launch Director → Product Marketing Lead → CSO) for failed gates.
- **Review**: Run `docs/usage-guide.md#orchestration-best-practices-puerto-parity` checklist before execution to confirm agents, dependencies, and deliverables.

## Workflow
1. **Timeline Build** – map critical path (code freeze, press embargo, enablement, GA) with owners.
2. **Communication Plan** – outline internal + external comms (press, blog, email, social, CS updates).
3. **Instrumentation & Monitoring** – confirm telemetry, dashboards, alerting, and logging.
4. **Go/No-Go Gates** – document readiness checklist, fallback plans, rollback triggers, decision authority.
5. **Launch-Day Command Center** – schedule standups, escalation tree, backlog triage process.

## Outputs
- Launch execution runbook (timeline, tasks, owners, dependencies).
- Go/no-go checklist + approval matrix.
- Monitoring plan with dashboard links and alert thresholds.
- Plan JSON entry stored/updated in `.claude/plans` for audit trail.

## Agent/Skill Invocations
- `launch-director` – orchestrates execution + governance.
- `workstream-lead` – ensures deliverables per channel.
- `war-room-ops` skill – defines command center rituals.

## GTM Agents Safeguards
- **Fallback agents**: document substitutions (e.g., Workstream Lead covering enablement) when specialists unavailable.
- **Escalation triggers**: if launch KPIs (error rate, adoption, sentiment) breach guardrails twice within 24h, execute rollback path and notify Exec Sponsor per war-room ops skill.
- **Plan maintenance**: revise plan JSON whenever dependencies, owners, or gates change; log updates in status packets.

---
