---
name: manage-production
description: Produces production plan with vendor checklist, run-of-show, and contingency matrix.
usage: /event-marketing:manage-production --event "Summit" --format hybrid --attendees 500
---

# Command: manage-production

## Inputs
- **event** – name or identifier.
- **format** – virtual, in-person, hybrid.
- **attendees** – expected size.
- **location** – optional venue/city/platform.
- **vendors** – optional known vendors to include.

## Workflow
1. **Requirements Intake** – gather AV, staging, streaming, accessibility, branding needs.
2. **Vendor Plan** – suggest vendor categories, RFP questions, contract reminders.
3. **Run-of-Show** – build detailed schedule with cues, speakers, technical notes.
4. **Operational Checklist** – staffing, registration, signage, swag, catering, shipments.
5. **Risk & Contingency** – highlight failure points (tech, weather, travel) with backup plans.

## Outputs
- Production plan doc with responsibilities + deadlines.
- Run-of-show table and cue sheets.
- Risk matrix and escalation contacts.

## Agent/Skill Invocations
- `event-producer` – owns production plan.
- `program-ops` skill – enforces ops standards.
- `event-briefs` skill – ensures documentation completeness.

---
