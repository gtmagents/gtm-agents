---
name: plan-loyalty
description: Produces loyalty program blueprint with tiers, benefits, and lifecycle triggers.
usage: /loyalty-lifecycle-orchestration:plan-loyalty --goal retention --tiers 3 --budget 50000
---

# Command: plan-loyalty

## Inputs
- **goal** – retention | expansion | engagement | advocacy.
- **tiers** – number of tiers or type (points-only, hybrid, missions).
- **budget** – monthly/quarterly reward pool.
- **personas** – optional comma-separated member segments.
- **constraints** – optional compliance or platform notes.

### GTM Agents Pattern & Plan Checklist
> Mirrors GTM Agents orchestrator blueprint @puerto/plugins/orchestrator/README.md#112-325.

- **Pattern selection**: Loyalty design generally follows a **diamond** (research ↔ modeling in parallel, converge into governance) or **pipeline** if run sequentially; document choice in the plan header.
- **Plan schema**: Save `.claude/plans/plan-<timestamp>.json` capturing tiers, benefit assumptions, financial guardrails, dependency graph (legal, finance, ops), error handling, and success criteria (retention, NRR, cost/point).
- **Tool hooks**: Reference `docs/gtm-essentials.md` stack—Serena for catalog/tier diffs, Context7 for compliance docs, Sequential Thinking for scenario modeling, Playwright for testing redemption flows.
- **Guardrails**: Default retry limit = 2 for data pulls or modeling errors; escalation ladder = Loyalty Strategist → Finance/Legal → Exec sponsor.
- **Review**: Run `docs/usage-guide.md#orchestration-best-practices-puerto-parity` before publishing to ensure dependencies, approvals, and deliverables are logged.

## Workflow
1. **Signal Review** – pull churn metrics, cohort revenue, product usage, and VOC insights.
2. **Tier & Benefit Design** – outline requirements per tier (earn rules, benefits, surprise moments).
3. **Lifecycle Mapping** – embed loyalty triggers into onboarding, adoption, upsell, and renewal stages.
4. **Economic Modeling** – estimate cost per point, breakage, and projected ROI.
5. **Governance Packet** – assign owners, cadences, and KPIs for launch.

## Outputs
- Program blueprint deck/table (tiers, requirements, benefits, KPIs).
- Lifecycle trigger matrix (event → loyalty action → channel → owner).
- Financial model summary (cost, expected lift, break-even timeline).
- Plan JSON entry stored/updated in `.claude/plans` for audit trail.

## Agent/Skill Invocations
- `loyalty-strategist` – leads architecture.
- `loyalty-modeling` skill – calculates economics and guardrails.
- `member-insights-analyst` – validates segment assumptions.

## GTM Agents Safeguards
- **Fallback agents**: document substitutes (e.g., loyalty-ops covering strategist) when key approvers unavailable.
- **Escalation triggers**: escalate if modeling shows negative ROI twice or compliance blockers arise; follow GTM Agents rip-cord path and log in plan JSON.
- **Plan maintenance**: update plan JSON/change log whenever tiers, budgets, or guardrails shift so audit reviewers see history.

---
