---
name: coordinate-channels
description: Align scheduling, messaging, and trafficking across all campaign channels.
usage: /campaign-orchestration:coordinate-channels --campaign "Q1 Launch" --channels "email,social,paid,events"
---

# Coordinate Channels Command

## Purpose
Provide a unified execution plan for cross-channel campaigns, detailing cadences, owners, specs, and QA checkpoints.

## Syntax
```bash
/campaign-orchestration:coordinate-channels \
  --campaign "<name>" \
  --channels "email,social,paid,events" \
  --start "2025-01-10" \
  --end "2025-02-28"
```

### Parameters
- `--campaign`: Campaign name or ID.
- `--channels`: Comma-delimited list of channels to orchestrate.
- `--start` / `--end`: Run dates for calendar generation.
- `--budget`: Optional channel budget map (JSON or CSV).
- `--offers`: Asset bundle or offer IDs to align messaging.
- `--tracking`: UTM/taxonomy style guide reference.

## Output Package
- Master channel calendar (table + ICS export) with send dates, owners, statuses.
- Channel-specific checklists (assets required, approvals, QA steps, trafficking notes).
- Risk log (dependencies, blockers, mitigations).
- Reporting expectations (metrics per channel, refresh cadence).

## Best Practices
- Sequence channels for storytelling (teaser -> announcement -> nurture).
- Lock copy deadlines at least 5 business days before launch.
- Share QA sign-off path (creative, legal, ops) to avoid delays.
- Maintain single source of truth for UTMs and tracking scripts.

---
