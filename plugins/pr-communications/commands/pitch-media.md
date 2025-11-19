---
name: pitch-media
description: Produces personalized media outreach plan with journalist targets, pitch copy, and follow-up cadence.
usage: /pr-communications:pitch-media --story "AI launch" --region US --tier "top" --embargo 2025-01-08T09:00:00Z
---

# Command: pitch-media

## Inputs
- **story** – topic or angle for pitching.
- **region** – target geography.
- **tier** – outlet tier (top, trade, regional) to shape messaging.
- **embargo** – ISO date/time for embargo (optional).
- **assets** – optional links to press kit, product pages, executive bios.

## Workflow
1. **Beat Matching** – surface relevant journalists/bloggers with background notes and prior coverage.
2. **Pitch Development** – craft customizable pitch email + subject line + bulletproof CTA.
3. **Sequencing** – define outreach order (exclusive, embargoed, broad) with timing and follow-up plan.
4. **Enablement** – produce briefing doc and attachments references.
5. **Tracking Plan** – set up CRM sheet or Airtable with response logging, deadlines, and sentiment.

## Outputs
- Media target table (name, outlet, angle, contact info, notes).
- Pitch templates for initial email + follow-up.
- Outreach tracker with dates, status, owner.

## Agent/Skill Invocations
- `media-relations-lead` – manages journalist relationships.
- `media-database` skill – powers list research + hygiene.
- `communications-director` – reviews messaging alignment.

---
