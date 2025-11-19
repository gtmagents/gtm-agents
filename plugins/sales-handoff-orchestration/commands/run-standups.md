---
name: run-standups
description: Facilitates daily MQL→SQL standups with shared metrics, blockers, and follow-up actions.
usage: /sales-handoff-orchestration:run-standups --segment enterprise --hosts "revops,sales" --mode async
---

# Command: run-standups

## Inputs
- **segment** – pipeline segment or program focus for the standup.
- **hosts** – comma-separated facilitators (revops, marketing, sales, cs).
- **mode** – live | async to determine meeting vs async summary.
- **interval** – default daily; override for weekly/bi-weekly.
- **notes** – optional agenda additions or urgent topics.

### GTM Agents Pattern & Plan Checklist
> Based on GTM Agents orchestrator blueprint @puerto/plugins/orchestrator/README.md#112-325.

- **Pattern selection**: Standups typically run **pipeline** (data prep → agenda → discussion → broadcast → accountability). If discussion capture + broadcast can run in parallel (async mode), document a **diamond** segment with merge gate in the plan header.
- **Plan schema**: Save `.claude/plans/plan-<timestamp>.json` capturing objective, schedule, task IDs, dependencies (dashboards, channels), error handling, and success metrics (response SLAs, blocker resolution %, queue depth).
- **Tool hooks**: Reference `docs/gtm-essentials.md` stack—Serena for CRM report diffs, Context7 for platform docs, Sequential Thinking for retro notes, Playwright for verifying embedded dashboard links if needed.
- **Guardrails**: Default retry limit = 2 for data fetch/broadcast failures; escalation ladder = Lifecycle Coordinator → Sales Manager → RevOps Director.
- **Review**: Run `docs/usage-guide.md#orchestration-best-practices-puerto-parity` before execution to confirm hosts, dependencies, deliverables.

## Workflow
1. **Data Prep** – pull latest routing stats (volume, conversion, SLA, backlog) filtered by segment.
2. **Agenda Builder** – auto-generate talking points: wins, blockers, experiments, escalations.
3. **Discussion Capture** – log owner + next action per issue, reference enablement resources.
4. **Broadcast** – send recap to shared channel/email with dashboards and follow-up tasks.
5. **Accountability Tracking** – sync action items into RevOps tracker for follow-up in next standup.

## Outputs
- Standup agenda doc (metrics snapshot, topics, owners).
- Action log with due dates and linked dashboards.
- Optional async update message for teams that cannot attend live.
- Plan JSON entry stored/updated in `.claude/plans` for audit trail.

## Agent/Skill Invocations
- `lifecycle-coordinator` – surfaces queue status + blockers.
- `sales-manager` – adds coaching notes + follow-up expectations.
- `enablement-kit` skill – links relevant scripts, talk tracks, or collateral.

## GTM Agents Safeguards
- **Fallback agents**: document substitutes (e.g., RevOps Director covering Lifecycle Coordinator) when specialists unavailable.
- **Escalation triggers**: if blockers remain unresolved for two standups or SLAs keep missing, escalate to Sales + Marketing leadership per GTM Agents rip-cord playbook.
- **Plan maintenance**: update plan JSON/change log whenever cadence, hosts, or tooling links change to maintain GTM Agents-grade auditability.

---
