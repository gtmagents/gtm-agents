---
name: forecast-renewals
description: Builds segmented renewal forecasts with health signals, variance commentary, and executive-ready views.
usage: /renewal-orchestration:forecast-renewals --window 90d --segment enterprise --detail full
---

# Command: forecast-renewals

## Inputs
- **window** – time horizon (30d, 60d, 90d, quarter) to include in the forecast.
- **segment** – optional filters (enterprise, midmarket, smb, region, vertical).
- **detail** – summary | full (controls depth of commentary and tables).
- **include-expansion** – true/false toggle to incorporate upsell scenarios.
- **confidence-threshold** – percentage for highlighting low-confidence projections.

### GTM Agents Pattern & Plan Checklist
> Based on GTM Agents orchestrator blueprint @puerto/plugins/orchestrator/README.md#112-325.

- **Pattern selection**: Forecast builds usually run **pipeline** (data → segmentation → scenarios → commentary → packaging). If segmentation + scenario modeling can parallelize, note a **diamond** segment and merge gate in the plan header.
- **Plan schema**: Save `.claude/plans/plan-<timestamp>.json` capturing objective, filters, task IDs, parallel groups, dependency graph (CS Ops, Finance, Product), error handling, and success metrics (forecast accuracy, coverage %, confidence spread).
- **Tool hooks**: Reference `docs/gtm-essentials.md` stack—Serena for data model diffs, Context7 for product/support doc pulls, Sequential Thinking for scenario retros, Playwright for dashboard QA if embedded.
- **Guardrails**: Default retry limit = 2 for failed data pulls or scenario jobs; escalation ladder = CS Ops Partner → Renewal Director → Finance lead.
- **Review**: Run `docs/usage-guide.md#orchestration-best-practices-puerto-parity` checklist before execution to confirm agents, dependencies, deliverables.

## Workflow
1. **Data Pull** – combine ARR, contract terms, product usage, CS health, support tickets, and sentiment data.
2. **Segmentation** – bucket accounts by tier, segment, and renewal phase; calculate coverage ratios.
3. **Scenario Modeling** – run base, upside, downside scenarios with expansion overlays.
4. **Variance Commentary** – note drivers (product adoption, exec engagement, risk flags) per segment.
5. **Package Deliverables** – produce dashboards + slides for CS leadership and finance.

## Outputs
- Renewal forecast table with ARR, NRR, churn %, and confidence per segment.
- Commentary deck with drivers, blockers, and next steps.
- Data extract for RevOps/finance to ingest into planning tools.
- Plan JSON entry stored/updated in `.claude/plans` for audit trail.

## Agent/Skill Invocations
- `renewal-director` – validates scenario assumptions and narratives.
- `cs-ops-partner` – ensures data integrity + automation hooks.
- `renewal-playbooks` skill – maps forecast insights to plays.

## GTM Agents Safeguards
- **Fallback agents**: document substitutes (e.g., Exec Sponsor covering Renewal Director commentary) when specialists unavailable.
- **Escalation triggers**: if accuracy or confidence guardrails fall below thresholds twice in a row, escalate to Renewal Director + Finance leadership per GTM Agents rip-cord.
- **Plan maintenance**: update plan JSON/change log whenever segments, scenario assumptions, or deliverables change to maintain GTM Agents audit parity.

---
