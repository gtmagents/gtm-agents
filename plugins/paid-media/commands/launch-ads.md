---
name: launch-ads
description: Produces platform-specific build instructions, QA steps, and tracking requirements for new paid campaigns.
usage: /paid-media:launch-ads --campaign "AI launch" --platforms "LinkedIn,Meta" --qa true
---

# Command: launch-ads

## Inputs
- **campaign** – reference name or brief ID.
- **platforms** – comma-separated platforms to build in.
- **qa** – include full QA + evidence log (default true).
- **assets** – optional asset filenames/URLs.
- **utm_template** – custom tracking template if needed.

## Workflow
1. **Brief Sync** – pull targeting, budgets, bids, flight dates.
2. **Platform Mapping** – convert targeting + creative into platform-specific objects (campaign/ad set/ad group).
3. **Build Checklist** – steps for naming, audiences, placements, bidding, daily caps, exclusions, tracking pixels.
4. **QA Matrix** – links, policy compliance, creative previews, tracking tests, custom conversions.
5. **Launch Plan** – pre-flight approvals, go-live time, monitoring windows, escalation contacts.

## Outputs
- Platform build guide with copy-paste configs.
- QA checklist and evidence log template.
- Launch runbook including monitoring tasks + owner assignments.

## Agent/Skill Invocations
- `channel-operator` – handles builds + QA evidence.
- `creative-variants` skill – verifies asset specs.
- `data-orchestrator` (from marketing automation) or `budget-optimization` skill – ensures budgets + pacing guardrails (optional cross-plugin reference).

---
