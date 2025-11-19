---
name: plan-calendar
description: Builds a cross-network social calendar with content pillars, approvals, and asset requirements.
usage: /social-scheduler-orchestration:plan-calendar --campaign "Q2 Product Story" --duration 6weeks --channels "linkedin,instagram,twitter"
---

# Command: plan-calendar

## Inputs
- **campaign** – program or theme anchoring the calendar.
- **duration** – timeframe (e.g., 4weeks) or number of posts.
- **channels** – comma-separated list of primary networks.
- **pillars** – optional list of content pillars or narrative arcs.
- **regions** – optional localization requirement.

## Workflow
1. **Brief Consolidation** – gather objectives, ICP, CTAs, paid alignment, and constraints.
2. **Pillar Mapping** – translate goals into recurring story arcs, formats, and hero assets.
3. **Scheduling Logic** – assign posting cadence per channel with timezone coverage and blackout dates.
4. **Asset Planning** – list creative requirements, copy notes, approvals, and localization tasks.
5. **Handoff Packet** – generate calendar view, owner assignments, and dependency tracker.

## Outputs
- Calendar spreadsheet/table with post date, channel, pillar, CTA, asset link, owner, approval status.
- Asset + localization brief with due dates.
- Risk log for collisions, bandwidth gaps, or compliance needs.

## Agent/Skill Invocations
- `social-program-manager` – leads brief intake and calendar strategy.
- `calendar-governance` skill – enforces cadence, coverage, and blackout rules.
- `asset-coordinator` – manages asset requirements + delivery timeline.

---
