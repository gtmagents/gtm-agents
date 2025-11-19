---
name: analyze-sequences
description: Evaluates live or completed email sequences, highlighting performance, deliverability, and experiment results.
usage: /email-sequence-orchestration:analyze-sequences --sequence "Expansion Play" --window 14d --detail full
---

# Command: analyze-sequences

## Inputs
- **sequence** – program name or ID to analyze.
- **window** – time horizon (7d, 14d, 30d, custom date range).
- **detail** – summary | full to control verbosity.
- **segment** – optional audience filter (persona, tier, region).
- **compare_to** – optional baseline sequence or control group.

## Workflow
1. **Data Pull** – collect MAP + CRM metrics (deliverability, engagement, pipeline impact) within specified window.
2. **Health Diagnostics** – evaluate KPI attainment, drop-off points, inbox placement, and fatigue risk.
3. **Experiment Readout** – summarize running/closed tests with confidence intervals and recommended actions.
4. **Insights & Actions** – generate prioritized playbook (optimize cadence, refresh content, escalate issues).
5. **Handoff** – prepare recap doc plus suggested backlog updates for architect + ops teams.

## Outputs
- Performance dashboard snapshot with KPIs by touch, persona, mailbox provider.
- Deliverability + QA alert summary referencing `deliverability-lead` incident logs.
- Experiment insights memo (winners, next tests, rollout guidance).

## Agent/Skill Invocations
- `experiment-analyst` – interprets tests and recommends next experiments.
- `deliverability-lead` – correlates reputation signals with performance dips.
- `cadence-design` skill – flags pacing issues causing fatigue.

---
