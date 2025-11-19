---
name: define-events
description: Produces instrumentation specification with events, properties, owners, and QA steps.
usage: /analytics-pipeline-orchestration:define-events --use_case "pipeline velocity" --sources "product,crm" --tools "Segment,dbt"
---

# Command: define-events

## Inputs
- **use_case** – business question or KPI the events support.
- **sources** – data sources involved (product, web, CRM, MAP, billing).
- **tools** – instrumentation stack (CDP, product analytics, warehouse, dbt).
- **constraints** – optional legal/compliance requirements.
- **timeline** – optional delivery date.

### GTM Agents Pattern & Plan Checklist
> Mirrors GTM Agents orchestrator blueprint @puerto/plugins/orchestrator/README.md#112-325.

- **Pattern selection**: Instrumentation typically runs **pipeline** (requirements → catalog → governance → QA → change mgmt). If governance + QA can run parallel, log a **diamond** segment with merge gate in the plan header.
- **Plan schema**: Save `.claude/plans/plan-<timestamp>.json` capturing objective, data sources, task IDs, dependencies, context passing (schemas, privacy notes), error handling, and success metrics (coverage %, defect ceiling).
- **Tool hooks**: Reference `docs/gtm-essentials.md` stack (Serena for repo diffs, Context7 for platform/legal docs, Sequential Thinking for review flows, Playwright for front-end event QA when applicable).
- **Guardrails**: Default retry limit = 2 for QA failures; escalation ladder = Analytics Data Strategist → Data Engineering Lead → RevOps.
- **Review**: Run `docs/usage-guide.md#orchestration-best-practices-puerto-parity` before execution to confirm agents, dependencies, deliverables.

## Workflow
1. **Requirement Gathering** – clarify KPIs, dimensions, and downstream consumers.
2. **Event Cataloging** – list events, payloads, properties, IDs, sampling rate, ownership.
3. **Governance Mapping** – document naming conventions, consent handling, retention policies.
4. **QA Plan** – outline testing methods (unit tests, replay, observability dashboards).
5. **Change Management** – define review/approval steps, rollout plan, and version control.

## Outputs
- Instrumentation spec (event name, description, properties, source, owner, status).
- Tracking plan (CSV/JSON/YAML) aligned with CDP or analytics tool requirements.
- QA checklist + evidence plan (logs, dashboards, sample payloads).
- Plan JSON entry stored/updated in `.claude/plans` for audit trail.

## Agent/Skill Invocations
- `analytics-data-strategist` – leads requirements + governance.
- `instrumentation` skill – enforces schema + consent rules.
- `quality-gates` skill – defines QA expectations.

## GTM Agents Safeguards
- **Fallback agents**: document substitutes (e.g., BI Publisher covering QA) if specialists unavailable.
- **Escalation triggers**: if instrumentation defects or compliance blockers breach guardrails twice in 48h, escalate to Data + Legal leadership, triggering GTM Agents-style rip-cord.
- **Plan maintenance**: update plan JSON/change log whenever events, schemas, or governance rules change to keep analytics audit-ready.

---
