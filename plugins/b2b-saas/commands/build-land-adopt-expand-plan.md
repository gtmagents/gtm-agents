---
name: build-land-adopt-expand-plan
description: Creates a phased land/adopt/expand action plan for strategic B2B SaaS accounts.
usage: /b2b-saas:build-land-adopt-expand-plan --account "Nimbus Corp" --stage adopt --horizon 2quarters --audience exec
---

# Command: build-land-adopt-expand-plan

## Inputs
- **account** – target customer name/ID.
- **stage** – land | adopt | expand | full; controls milestone focus.
- **horizon** – timeframe (quarter, 2quarters, year, custom).
- **audience** – exec | account-team | cs | async.
- **signals** – optional CSV/JSON with telemetry or program notes.

## Workflow
1. **Signal Review** – synthesize telemetry, value metrics, and stakeholder landscape.
2. **Milestone Mapping** – lay out success criteria, owners, and checkpoints per phase.
3. **Play Selection** – recommend adoption campaigns, exec plays, and expansion bets.
4. **Risk/Dependency Logging** – flag gaps, requests, and required approvals.
5. **Packaging** – generate presentation/memo plus tracker for follow-ups.

## Outputs
- Land/adopt/expand roadmap with timelines, KPIs, and owners.
- Risk + dependency register for leadership visibility.
- Action tracker synced to CRM/CSM tools for execution.

## Agent/Skill Invocations
- `land-adopt-expand-director` – orchestrates motion design + governance.
- `industry-strategist` – calibrates narrative + proof by vertical.
- `land-adopt-expand-blueprint` skill – enforces milestone structure.
- `usage-to-value-map` skill – injects telemetry-driven proof points.

---
