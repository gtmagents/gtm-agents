---
name: versioning-dashboard
description: Dashboard pattern for tracking doc coverage across product versions,
  locales, and channels.
---

# Versioning Dashboard Skill

## When to Use
- Managing multiple product versions, editions, or deployment models.
- Coordinating deprecations, migrations, and long-term support documentation.
- Reporting readiness and gaps to leadership during launches.

## Framework
1. **Version Inventory** – list active versions, release dates, support windows, and owners.
2. **Artifact Coverage** – matrix of docs/tutorials/guides per version + locale + channel.
3. **Change Log Hooks** – tie version changes to release notes, migration guides, and alert cadence.
4. **Risk & Action Log** – highlight outdated assets, missing locales, or compliance needs.
5. **Reporting Layer** – KPIs (coverage %, SLA adherence, reader metrics) with filters for audience or product area.

## Templates
- Dashboard sheet with pivoted coverage views and status chips.
- Migration tracker linking deprecated features to comms + doc updates.
- Executive summary slide with version highlights and asks.

## Tips
- Integrate with source control metadata to auto-update coverage status.
- Highlight dependencies (SDKs, integrations) when versions shift.
- Pair with `plan-documentation-roadmap`, `publish-release-documentation`, and `update-api-reference` workflows.

---
