---
name: optimize-referrals
description: Analyzes referral performance, fraud risk, and partner health to recommend improvements.
usage: /referral-program-orchestration:optimize-referrals --window 30d --detail full --dimensions "channel,partner-tier"
---

# Command: optimize-referrals

## Inputs
- **window** – analysis horizon (7d, 30d, 90d).
- **detail** – summary | full to control output length.
- **dimensions** – optional breakdowns (channel, persona, partner-tier, region).
- **experiments** – optional list of tests to evaluate.
- **alert_threshold** – optional KPI threshold for escalations.

### GTM Agents Pattern & Plan Checklist
> Mirrors GTM Agents orchestrator blueprint @puerto/plugins/orchestrator/README.md#112-325.

- **Pattern selection**: Optimization review typically runs **pipeline** (data refresh → diagnostics → risk review → partner health → action plan). If diagnostics + risk review can run concurrently, note a **diamond** block with merge gate in the plan header.
- **Plan schema**: Save `.claude/plans/plan-<timestamp>.json` capturing window, datasets, task IDs, dependency graph (BI, fraud, partner ops), error handling, and success metrics (conversion lift, fraud reduction, partner NPS).
- **Tool hooks**: Reference `docs/gtm-essentials.md` stack—Serena for schema diffs, Context7 for referral SOPs/partner comms, Sequential Thinking for retro cadence, Playwright for offer flows or portal QA.
- **Guardrails**: Default retry limit = 2 for failed data pulls or fraud model runs; escalation ladder = Referral Architect → Partner Ops → Exec sponsor.
- **Review**: Run `docs/usage-guide.md#orchestration-best-practices-puerto-parity` before distributing recommendations to confirm dependencies and approvals.

## Workflow
1. **Data Refresh** – pull referral submissions, conversions, payouts, fraud flags, and NPS per dimension.
2. **Performance Diagnostics** – inspect funnel (invites → referrals → pipeline → revenue) and incentive efficiency.
3. **Risk Review** – run fraud heuristics, identify suspicious cohorts, confirm compliance logs.
4. **Partner Health** – evaluate top/bottom partners, share-of-voice, and engagement levels.
5. **Playbook Output** – recommend experiments (incentive tweaks, messaging, partner enablement) with expected impact.

## Outputs
- Performance dashboard snapshot with annotated insights.
- Fraud/risk summary referencing `fraud-detection` skill outputs.
- Optimization backlog with owners, ETA, and projected lift.
- Plan JSON entry stored/updated in `.claude/plans` for audit trail.

## Agent/Skill Invocations
- `referral-architect` – prioritizes experiments + approvals.
- `lifecycle-ops` – implements tooling or messaging changes.
- `fraud-detection` skill – validates risk findings.
- `partner-ops` skill – coordinates partner communications.

## GTM Agents Safeguards
- **Fallback agents**: document substitutes (e.g., Lifecycle Ops covering Architect) when leads unavailable.
- **Escalation triggers**: if alert_threshold breached twice or fraud risk spikes, trigger GTM Agents rip-cord escalation and record actions in plan JSON.
- **Plan maintenance**: update plan JSON/change log whenever metrics, thresholds, or partner tiers change to maintain audit continuity.

---
