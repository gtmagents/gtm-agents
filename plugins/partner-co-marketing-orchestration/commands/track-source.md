---
name: track-source
description: Aligns attribution, dashboards, and ROI reporting for partner co-marketing campaigns.
usage: /partner-co-marketing-orchestration:track-source --campaign "AI Launch Tour" --window 30d --detail full
---

# Command: track-source

## Inputs
- **campaign** – joint campaign identifier matching briefs/assets.
- **window** – time range for analysis (7d, 30d, campaign duration).
- **detail** – summary | full report depth.
- **dimensions** – optional breakdowns (partner, channel, asset, region).
- **attribution_model** – optional override (first-touch, last-touch, multi-touch).

### GTM Agents Pattern & Plan Checklist
> Mirrors GTM Agents orchestrator blueprint @puerto/plugins/orchestrator/README.md#112-325.

- **Pattern selection**: Tracking/reporting usually runs **pipeline** (gather → normalize → attribute → insights → reporting). If normalization + attribution can run in parallel (separate partners), log a **diamond** segment with merge gate.
- **Plan schema**: Save `.claude/plans/plan-<timestamp>.json` with campaign, data sources, task IDs, dependency graph (CRM, MAP, analytics), error handling, and success metrics (attribution confidence, SLA adherence, partner satisfaction).
- **Tool hooks**: Reference `docs/gtm-essentials.md` stack—Serena for data model diffs, Context7 for partner taxonomy docs, Sequential Thinking for readout cadence, Playwright for dashboard QA if embedded.
- **Guardrails**: Default retry limit = 2 for failed data pulls or reconciliation mismatches; escalation ladder = Co-marketing Analytics Lead → RevOps/Finance partners → Exec sponsors.
- **Review**: Run `docs/usage-guide.md#orchestration-best-practices-puerto-parity` before execution to confirm agents, dependencies, deliverables.

## Workflow
1. **Data Gathering** – ingest analytics/CRM data from both partners using shared taxonomy + UTM parameters.
2. **Normalization** – reconcile schemas, currencies, and funnel stages; dedupe overlapping records.
3. **Attribution Calculation** – apply agreed model to allocate pipeline/revenue across partners + channels.
4. **Insight Generation** – highlight top-performing assets, audience segments, and drop-off points.
5. **Reporting Package** – produce dashboards, executive summary, and recommended optimizations.

## Outputs
- Attribution dashboard snapshot with partner/source breakdown.
- Revenue/pipeline contribution table vs targets.
- Optimization action list referencing asset or channel adjustments.
- Plan JSON entry stored/updated in `.claude/plans` for audit trail.

## Agent/Skill Invocations
- `co-marketing-analytics-lead` – validates data + insights.
- `attribution` skill – enforces methodology consistency.
- `partner-marketer` – receives recommendations for next sprint.

## GTM Agents Safeguards
- **Fallback agents**: note substitutes (e.g., Partner Marketer covering Analytics Lead) if specialists unavailable.
- **Escalation triggers**: if attribution accuracy drops below guardrails twice or partners dispute sourced pipeline, escalate to revenue/partner governance board per GTM Agents rip-cord.
- **Plan maintenance**: update plan JSON/change log when models, data sources, or reporting cadences change to maintain audit parity.

---
