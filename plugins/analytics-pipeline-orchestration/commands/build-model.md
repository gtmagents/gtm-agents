---
name: build-model
description: Generates a modeling plan detailing transforms, tests, and deployment schedule for analytics use cases.
usage: /analytics-pipeline-orchestration:build-model --use_case "pipeline velocity" --stack "dbt" --refresh daily
---

# Command: build-model

## Inputs
- **use_case** – name of metric or dashboard relying on the model.
- **stack** – modeling tool (dbt, LookML, Metrics Layer, SQL Runner, Python jobs).
- **refresh** – cadence (hourly, daily, weekly) or cron.
- **dependencies** – optional upstream tables or APIs.
- **tests** – optional list of validations to enforce.

### GTM Agents Pattern & Plan Checklist
> Mirrors GTM Agents orchestrator blueprint @puerto/plugins/orchestrator/README.md#112-325.

- **Pattern selection**: Modeling often runs **pipeline** (spec → blueprint → testing → deployment → docs). If testing + deployment prep can parallelize, log a **diamond** segment with merge gate.
- **Plan schema**: Save `.claude/plans/plan-<timestamp>.json` with objective, data lineage, task IDs, parallel groups, dependency matrix, error handling, and success metrics (freshness %, defect ceiling, SLA adherence).
- **Tool hooks**: Reference `docs/gtm-essentials.md` stack—Serena for repo diffs/dbt patches, Context7 for platform docs, Sequential Thinking for review cadences, Playwright for UI validations tied to modeled data.
- **Guardrails**: Default retry limit = 2 for failed tests/deployments; escalation path = Analytics Modeling Lead → Data Engineering Lead → RevOps.
- **Review**: Run `docs/usage-guide.md#orchestration-best-practices-puerto-parity` before execution to confirm agents, dependencies, deliverables.

## Workflow
1. **Spec Alignment** – review event/tracking plan, KPI definitions, stakeholders.
2. **Model Blueprint** – outline staging, intermediate, mart layers, join keys, surrogate IDs.
3. **Testing Strategy** – define schema, freshness, unique, accepted value, and custom tests.
4. **Deployment Plan** – schedule jobs, resource configs, backfill strategy, rollback steps.
5. **Documentation & Handoff** – update dbt docs / catalog, change log, owner assignments.

## Outputs
- Modeling spec (diagram, SQL pseudocode, dependencies).
- Test plan + configuration snippets.
- Deployment checklist with monitoring hooks and rollback instructions.
- Plan JSON entry stored/updated in `.claude/plans` for audit trail.

## Agent/Skill Invocations
- `analytics-modeling-lead` – architects model + tests.
- `quality-gates` skill – ensures validation coverage.
- `instrumentation` skill – confirms data contracts stay intact.

## GTM Agents Safeguards
- **Fallback agents**: document substitutes (e.g., BI Publisher covering modeling reviews) when specialists unavailable.
- **Escalation triggers**: if freshness, defect, or SLA guardrails breach twice within 24h, escalate to Data + RevOps leadership per GTM Agents runbook and consider rollback.
- **Plan maintenance**: update plan JSON whenever dependencies, owners, or deployment cadence changes, keeping audit alignment with GTM Agents standards.

---
