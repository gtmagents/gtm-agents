---
name: build-social-calendar
description: Generates detailed social content calendar with briefs, approvals, and publishing workflow.
usage: /social-media-marketing:build-social-calendar --month "Jan 2026" --channels linkedin,instagram,tiktok --cadence daily --theme "AI Launch"
---

# Command: build-social-calendar

## Inputs
- **month** – month or date range for planning.
- **channels** – comma-separated list of target platforms.
- **cadence** – daily | 3x/week | weekly | custom.
- **theme** – optional campaign or narrative focus.
- **approvers** – optional comma-separated stakeholders for routing.

## Workflow
1. **Brief Intake** – gather campaign context, themes, assets, and guardrails.
2. **Content Grid** – map publish rhythm per channel with hooks, CTAs, and creative notes.
3. **Production Checklist** – assign owners, due dates, and asset requirements.
4. **Approval Routing** – integrate compliance/brand reviewers and track status.
5. **Publishing Package** – finalize copy, creative references, and tagging instructions.

## Outputs
- Calendar spreadsheet/table with channel, date, concept, CTA, owner, status.
- Asset + production checklist for creative + video teams.
- Approval + publishing tracker with deadlines and links.

## Agent/Skill Invocations
- `social-strategy-director` – sets priorities + reviews final plan.
- `campaign-optimization-manager` – identifies content refresh needs + experiments.
- `social-calendar-system` skill – enforces template + workflow steps.
- `creative-iteration-playbook` skill – guides creative briefs and testing cadence.

---
