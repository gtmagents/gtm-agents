---
name: run-retro
description: Facilitates structured retrospectives after renewal cycles to capture insights, update playbooks, and improve forecasting.
usage: /renewal-orchestration:run-retro --segment enterprise --window quarter --include-churn true
---

# Command: run-retro

## Inputs
- **segment** – optional filter (enterprise, growth, scale) for the retro scope.
- **window** – time range (month, quarter, rolling-90d).
- **include-churn** – true/false toggle to include churned accounts alongside renewals.
- **dimensions** – optional grouping (cs-owner, product, geo, persona).
- **depth** – summary | workshop (adds facilitation guides + templates).

### GTM Agents Pattern & Plan Checklist
> Derived from GTM Agents orchestrator blueprint @puerto/plugins/orchestrator/README.md#112-325.

- **Pattern selection**: Retros typically follow **pipeline** (data → analysis → insights → action planning → documentation). If insight synthesis + action planning can run in parallel (workshop mode), log a **diamond** segment with merge gate.
- **Plan schema**: Save `.claude/plans/plan-<timestamp>.json` with objective, scope, task IDs, parallel groups, dependencies (CS Ops, Product, Finance), error handling, and success metrics (closed-loop actions %, renewal uplift, blocker removal).
- **Tool hooks**: Reference `docs/gtm-essentials.md` stack—Serena for pulling historical plan diffs, Context7 for product/support notes, Sequential Thinking for facilitation prompts, Playwright for verifying embedded dashboards if used.
- **Guardrails**: Default retry limit = 2 for data pulls or workshop sync failures; escalation ladder = Renewal Director → CS Ops Partner → Exec Sponsor.
- **Review**: Use `docs/usage-guide.md#orchestration-best-practices-puerto-parity` before execution to confirm facilitation resources, dependencies, deliverables.

## Workflow
1. **Data Compilation** – aggregate deal outcomes, ARR deltas, health trends, product usage shifts, and qualitative notes.
2. **Pattern Analysis** – bucket learnings by reason codes, plays applied, executive involvement, and pricing.
3. **Insight Synthesis** – highlight leading indicators, blockers, and emerging opportunities.
4. **Action Planning** – assign remediation owners, timeline, and metrics for follow-up workstreams.
5. **Documentation** – publish retro deck + database entries for ongoing knowledge base.

## Outputs
- Retro report summarizing metrics, insights, and improvement themes.
- Action tracker with owners, due dates, and success criteria.
- Template slides + transcripts for sharing across CS, product, finance leadership.
- Plan JSON entry stored/updated in `.claude/plans` for audit trail.

## Agent/Skill Invocations
- `renewal-director` – sponsors session and finalizes recommendations.
- `cs-ops-partner` – compiles data and action tracker.
- `renewal-playbooks` skill – integrates learnings into new plays.
- `deal-desk` skill – informs pricing/process adjustments.

## GTM Agents Safeguards
- **Fallback agents**: document substitutes (e.g., Exec Sponsor covering Renewal Director) when facilitators unavailable.
- **Escalation triggers**: if critical blockers repeat across two retros or action items stall beyond SLA, escalate to CRO + Product leadership per GTM Agents rip-cord.
- **Plan maintenance**: update plan JSON/change log when retro scope, owners, or follow-up workstreams change to maintain GTM Agents audit parity.

---
