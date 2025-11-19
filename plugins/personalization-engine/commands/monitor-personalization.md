---
name: monitor-personalization
description: Audits personalization performance, governance compliance, and experiment results.
usage: /personalization-engine:monitor-personalization --initiative "PLG Onboarding" --window 14d --detail full
---

# Command: monitor-personalization

## Inputs
- **initiative** – personalization program or campaign to analyze.
- **window** – time frame (7d, 14d, 30d) for pulling metrics.
- **detail** – summary | full to control report depth.
- **dimension** – optional breakdown (profile, channel, cohort).
- **alert_threshold** – optional KPI threshold to trigger incident items.

### GTM Agents Pattern & Plan Checklist
> Mirrors GTM Agents orchestrator blueprint @puerto/plugins/orchestrator/README.md#112-325.

- **Pattern selection**: Monitoring usually runs **pipeline** (data aggregation → governance scan → experiment readout → issue detection → action plan). If governance + experiments review can run concurrently, capture a **diamond** block with merge gate in the plan header.
- **Plan schema**: Save `.claude/plans/plan-<timestamp>.json` capturing initiative, data feeds, dependency graph (data eng, privacy, experimentation), error handling, and success metrics (lift %, incident response time, consent adherence).
- **Tool hooks**: Reference `docs/gtm-essentials.md` stack—Serena for schema diffs, Context7 for governance/experiment SOPs, Sequential Thinking for retro cadence, Playwright for experience QA evidence.
- **Guardrails**: Default retry limit = 2 for failed data pulls or anomaly jobs; escalation ladder = Testing Lead → Personalization Architect → Data Privacy Lead.
- **Review**: Run `docs/usage-guide.md#orchestration-best-practices-puerto-parity` before distribution to ensure dependencies + approvals are logged.

## Workflow
1. **Data Aggregation** – pull engagement, conversion, and revenue impact by profile/channel plus decision tree health signals.
2. **Governance Scan** – verify consent flags, fallback rates, and rule change logs for compliance.
3. **Experiment Readout** – summarize live/completed tests with statistical confidence and recommended actions.
4. **Issue Detection** – flag anomalies (data freshness, variant suppression, performance dips) and suggest playbooks.
5. **Report Distribution** – publish recap with dashboards, backlog items, and owners.

## Outputs
- Performance dashboard snapshot segmented by profile/channel/variant.
- Governance checklist status with any violations or pending approvals.
- Experiment memo with next steps + rollout guidance.
- Plan JSON entry stored/updated in `.claude/plans` for audit trail.

## Agent/Skill Invocations
- `testing-lead` – interprets experiments and recommends rollouts.
- `personalization-architect` – validates experience integrity.
- `governance` skill – enforces policy checks and approvals.

## GTM Agents Safeguards
- **Fallback agents**: document substitutes (e.g., Governance covering Testing Lead) when leads unavailable.
- **Escalation triggers**: escalate if alert_threshold breached twice, consent violations appear, or anomaly alerts repeat; log remediation steps in plan JSON.
- **Plan maintenance**: update plan JSON/change log when metrics, thresholds, or monitoring cadences change to keep audits accurate.

---
