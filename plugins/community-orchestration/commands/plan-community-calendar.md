---
name: plan-community-calendar
description: Builds a rolling community programming calendar with themes, formats, and owners.
usage: /community-orchestration:plan-community-calendar --window 8weeks --channels "forum,events,slack" --themes "product,customer-stories"
---

# Command: plan-community-calendar

## Inputs
- **window** – planning horizon (e.g., 8weeks, quarter).
- **channels** – comma-separated community surfaces (forum, Slack, Discord, events, webinar, newsletter).
- **themes** – optional list of focus themes or series.
- **audiences** – optional persona/segment filters.
- **dependencies** – optional notes on launches, campaigns, or partner tie-ins.

### GTM Agents Pattern & Plan Checklist
> Mirrors GTM Agents orchestrator blueprint @puerto/plugins/orchestrator/README.md#112-325.

- **Pattern selection**: Community calendar planning typically runs **pipeline** (signals → themes → programming → resources → publishing). If programming segments (e.g., events vs async drops) run in parallel, capture a **diamond** segment with merge gate in the plan header.
- **Plan schema**: Save `.claude/plans/plan-<timestamp>.json` capturing window, channels, task IDs, dependency graph (hosts, moderators, asset teams), error handling, and success metrics (attendance, engagement %, advocacy contributions).
- **Tool hooks**: Reference `docs/gtm-essentials.md` stack—Serena for asset/promo diffs, Context7 for playbooks/guidelines, Sequential Thinking for governance/check-in cadence, Playwright for testing community microsites or forms if needed.
- **Guardrails**: Default retry limit = 2 for resource shortages or tooling failures; escalation ladder = Community Lead → Marketing/CS leadership → Exec sponsor.
- **Review**: Run `docs/usage-guide.md#orchestration-best-practices-puerto-parity` before execution to confirm owners, dependencies, deliverables.

## Workflow
1. **Signal Review** – pull engagement data, VOC insights, and upcoming GTM milestones.
2. **Theme Mapping** – align themes to goals (activation, adoption, advocacy) and persona interests.
3. **Programming Mix** – schedule events, AMAs, content drops, and spotlights with owners + formats.
4. **Resource Checklist** – detail required assets, hosts, moderators, and promo timelines.
5. **Publishing Packet** – output calendar plus reminders/automation hooks for each touch.

## Outputs
- Calendar table (date, theme, channel, format, owner, CTA, dependencies).
- Asset + promotion checklist with due dates.
- Risk log flagging capacity or approval gaps.
- Plan JSON entry stored/updated in `.claude/plans` for audit trail.

## Agent/Skill Invocations
- `community-lead` – sets strategy and approvals.
- `community-ops` skill – ensures workflows and tooling readiness.
- `community-analyst` – provides data context for theme prioritization.

## GTM Agents Safeguards
- **Fallback agents**: document substitutes (e.g., Community Ops covering Community Lead) when decision-makers unavailable.
- **Escalation triggers**: if capacity gaps or moderation risks appear twice in planning reviews, escalate to cross-functional steering committee per GTM Agents rip-cord.
- **Plan maintenance**: update plan JSON/change log when themes, channels, or dependencies change so audit trail matches GTM Agents standards.

---
