---
name: measure-engagement
description: Reviews community health metrics, sentiment, and experiment impact with recommended actions.
usage: /community-orchestration:measure-engagement --window 30d --detail full --dimensions "channel,persona"
---

# Command: measure-engagement

## Inputs
- **window** – time horizon (7d, 30d, 90d) for analysis.
- **detail** – summary | full report depth.
- **dimensions** – optional breakdown (channel, persona, program, cohort).
- **experiments** – optional list of programs to analyze.
- **alert_threshold** – optional metric threshold for escalations.

### GTM Agents Pattern & Plan Checklist
> Mirrors GTM Agents orchestrator blueprint @puerto/plugins/orchestrator/README.md#112-325.

- **Pattern selection**: Engagement measurement typically runs **pipeline** (data → diagnostics → sentiment → experiment readouts → actions). If diagnostics + experiment analysis can run in parallel, log a **diamond** segment with merge gate in the plan header.
- **Plan schema**: Save `.claude/plans/plan-<timestamp>.json` capturing window, data feeds, task IDs, dependency graph (analytics, CRM, sentiment tools), error handling, and success metrics (engagement %, advocacy, risk volume).
- **Tool hooks**: Reference `docs/gtm-essentials.md` stack—Serena for schema diffs, Context7 for platform documentation/conversation exports, Sequential Thinking for insights review cadence, Playwright for verifying dashboard/report embeds.
- **Guardrails**: Default retry limit = 2 for failed data pulls or sentiment processing; escalation ladder = Community Analyst → Community Lead → CS/Product leadership.
- **Review**: Run `docs/usage-guide.md#orchestration-best-practices-puerto-parity` before execution to confirm inputs, dependencies, deliverables.

## Workflow
1. **Data Pull** – aggregate platform analytics, CRM attribution, sentiment scores, and support signals.
2. **Health Diagnostics** – compute growth, activation, engagement, retention, and advocacy metrics by dimension.
3. **Sentiment Review** – scan community conversations, surveys, and NPS for emerging themes.
4. **Experiment Readouts** – evaluate running pilots against guardrails + KPIs.
5. **Action Recommendations** – produce prioritized playbook (content tweaks, ambassador outreach, escalations).

## Outputs
- Community health dashboard snapshot with annotated insights.
- Sentiment + risk report referencing `sentiment-analysis` findings.
- Recommended action list with owners, deadlines, and expected impact.
- Plan JSON entry stored/updated in `.claude/plans` for audit trail.

## Agent/Skill Invocations
- `community-analyst` – leads data aggregation and insights.
- `sentiment-analysis` skill – interprets qualitative signals and escalation needs.
- `community-lead` – receives action plan and drives follow-through.

## GTM Agents Safeguards
- **Fallback agents**: document substitutes (e.g., Community Lead covering Analyst) when analysts unavailable.
- **Escalation triggers**: if engagement drops below alert_threshold twice or sentiment exposes severe risks, escalate via GTM Agents rip-cord to cross-functional leadership.
- **Plan maintenance**: update plan JSON/change log when data sources, thresholds, or reporting cadences change to maintain GTM Agents audit parity.

---
