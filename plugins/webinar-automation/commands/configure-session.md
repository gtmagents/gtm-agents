---
name: configure-session
description: Produces step-by-step webinar platform setup instructions with reminders, integrations, and QA gates.
usage: /webinar-automation:configure-session --platform on24 --session "AI Launch" --speakers "CPO,PMM"
---

# Command: configure-session

## Inputs
- **platform** – webinar platform (Zoom, ON24, Demio, Livestorm, etc.).
- **session** – title or identifier.
- **speakers** – comma-separated speaker list.
- **assets** – optional slide/video/demo asset links.
- **integrations** – optional systems to sync (MAP, CRM, Slack, etc.).

## Workflow
1. **Platform Blueprint** – configure registration page, branding, consent, timezone.
2. **Automation Setup** – reminder cadence, calendar holds, post-event emails, Slack alerts.
3. **Engagement Modules** – polls, Q&A, resources, CTA buttons, breakout rooms.
4. **Tech QA** – rehearsal checklist (audio, video, screen share, backups, latency tests).
5. **Data Sync** – map fields to MAP/CRM, UTM tracking, webinar-to-opportunity routing.

## Outputs
- Platform configuration checklist tailored to chosen vendor.
- Reminder & automation schedule with copy snippets.
- QA plan and rehearsal agenda.

## Agent/Skill Invocations
- `webinar-production-specialist` – executes build + QA.
- `registration-ops` skill – ensures data capture + consent compliance.
- `webinar-design` skill – validates attendee experience modules.

---
