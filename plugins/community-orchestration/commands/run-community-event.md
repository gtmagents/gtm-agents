---
name: run-community-event
description: Generates run of show, moderation plan, and follow-up tasks for community events or live sessions.
usage: /community-orchestration:run-community-event --event "Product AMA" --date 2025-12-05 --hosts "PM,CSM" --format livestream
---

# Command: run-community-event

## Inputs
- **event** – name or theme of the session.
- **date** – scheduled date/time (ISO or natural language).
- **hosts** – comma-separated speakers/moderators.
- **format** – webinar | livestream | roundtable | in-person | async.
- **audience** – optional persona/community segment.
- **goals** – optional KPIs (registrations, NPS, product adoption prompt).

### GTM Agents Pattern & Plan Checklist
> Mirrors GTM Agents orchestrator blueprint @puerto/plugins/orchestrator/README.md#112-325.

- **Pattern selection**: Live event orchestration generally runs **pipeline** (brief → run-of-show → moderation → promotion → follow-up). If moderation + promotion can run in parallel, document a **diamond** segment with merge gate in the plan header.
- **Plan schema**: Save `.claude/plans/plan-<timestamp>.json` capturing event details, task IDs, dependency graph (hosts, ops, tooling, accessibility), error handling, and success metrics (attendance, engagement rate, CSAT/NPS).
- **Tool hooks**: Reference `docs/gtm-essentials.md` stack—Serena for script/asset diffs, Context7 for event SOPs, Sequential Thinking for pre/post-mortem cadence, Playwright for registration/stream QA if needed.
- **Guardrails**: Default retry limit = 2 for tooling failures or host changes; escalation ladder = Community Lead → Marketing/CS leadership → Exec sponsor.
- **Review**: Run `docs/usage-guide.md#orchestration-best-practices-puerto-parity` before execution to confirm owners, dependencies, deliverables.

## Workflow
1. **Brief Assembly** – capture objectives, audience, and success metrics; pull relevant insights/content.
2. **Run of Show** – outline agenda, time stamps, speaker prompts, engagement moments, and CTAs.
3. **Moderation & Ops** – assign backstage roles, chat moderation guidelines, accessibility needs, and failovers.
4. **Promotion & Reminders** – auto-generate promo copy, schedule reminders, and update community calendar.
5. **Follow-up Plan** – create recap checklist (recording, notes, action items, support cases) and measurement hooks.

## Outputs
- Event runbook (agenda, host responsibilities, tech setup, contingency plan).
- Moderation worksheet with escalation triggers and response templates.
- Follow-up task list tied to owners and due dates.
- Plan JSON entry stored/updated in `.claude/plans` for audit trail.

## Agent/Skill Invocations
- `community-lead` – approves agenda + goals.
- `community-moderator` – executes moderation plan.
- `community-ops` skill – ensures tooling + workflows are ready.
- `escalation` skill – provides incident handling guidance.

## GTM Agents Safeguards
- **Fallback agents**: document substitutes (e.g., Moderator covering Community Lead) when hosts unavailable.
- **Escalation triggers**: if incidents breach guardrails (e.g., harassment, platform failure) escalate immediately per GTM Agents rip-cord; log remediation in plan JSON.
- **Plan maintenance**: update plan JSON/change log when hosts, formats, or tooling stack change so audit trail mirrors GTM Agents procedures.

---
