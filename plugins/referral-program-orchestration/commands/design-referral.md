---
name: design-referral
description: Produces referral program blueprint with incentives, rules, and governance.
usage: /referral-program-orchestration:design-referral --goal "pipeline" --audience "customers" --budget 25000
---

# Command: design-referral

## Inputs
- **goal** – primary objective (signups, pipeline, revenue, expansion).
- **audience** – target participants (customers, partners, employees, influencers).
- **budget** – incentive budget cap or range.
- **regions** – optional list of geo restrictions/compliance considerations.
- **timeline** – planned launch window.

### GTM Agents Pattern & Plan Checklist
> Mirrors GTM Agents orchestrator blueprint @puerto/plugins/orchestrator/README.md#112-325.

- **Pattern selection**: Referral design typically uses a **diamond** (context ↔ mechanic modeling, converge into governance) or **pipeline**; document choice in the plan header.
- **Plan schema**: Save `.claude/plans/plan-<timestamp>.json` capturing goals, incentives, dependency graph (legal, finance, ops, partner), error handling, and success criteria (pipeline, CAC, fraud rates).
- **Tool hooks**: Reference `docs/gtm-essentials.md` stack—Serena for charter diffs, Context7 for compliance + incentive benchmarks, Sequential Thinking for trade-off analysis, Playwright for prototype referral journeys.
- **Guardrails**: Default retry limit = 2 for modeling or policy failures; escalation ladder = Referral Architect → Legal/Finance → Exec sponsor.
- **Review**: Run `docs/usage-guide.md#orchestration-best-practices-puerto-parity` before sign-off to confirm dependencies, approvals, deliverables.

## Workflow
1. **Context Gathering** – pull GTM targets, persona insights, legal/finance constraints.
2. **Mechanic Selection** – evaluate one-sided vs two-sided incentives, tiering, and cadence.
3. **Rules & Safeguards** – define eligibility, referral caps, fraud checks, and compliance requirements.
4. **Enablement Plan** – list assets, messaging, training, and tooling needed for launch.
5. **Measurement Framework** – connect KPIs to dashboards and define review cadence.

## Outputs
- Referral program charter (objective, mechanics, incentives, rules, KPIs).
- Stakeholder alignment deck outlining responsibilities and approvals.
- Risk log highlighting compliance/legal considerations.
- Plan JSON entry stored/updated in `.claude/plans` for audit trail.

## Agent/Skill Invocations
- `referral-architect` – leads program design and governance.
- `incentive-design` skill – structures payouts and thresholds.
- `fraud-detection` skill – recommends safeguards.

## GTM Agents Safeguards
- **Fallback agents**: document substitutes (e.g., Partner Ops covering Referral Architect) when decision-makers unavailable.
- **Escalation triggers**: if compliance blockers or budget overruns appear twice, trigger GTM Agents rip-cord escalation and log remediation in plan JSON.
- **Plan maintenance**: update plan JSON/change log whenever incentives, eligibility rules, or governance cadences change.

---
