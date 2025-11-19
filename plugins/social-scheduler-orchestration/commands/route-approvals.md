---
name: route-approvals
description: Coordinates legal, brand, partner, and regional approvals for scheduled social content.
usage: /social-scheduler-orchestration:route-approvals --calendar "Q2 Product Story" --mode async --stakeholders "legal,brand,regional"
---

# Command: route-approvals

## Inputs
- **calendar** – reference name or ID of the calendar produced by `plan-calendar`.
- **mode** – live | async review workflow.
- **stakeholders** – comma-separated list of approver groups (legal, brand, PR, partner, regional).
- **deadline** – due date/time for approvals to be completed.
- **notes** – optional context or risk flags requiring special review.

## Workflow
1. **Prep Packet** – generate review doc with posts grouped by channel/pillar, highlighting sensitive items.
2. **Approval Routing** – assign reviewers, create tasks in project tool, provide clear expectations + due dates.
3. **Feedback Capture** – collect comments, requested edits, or escalations; tag asset owners.
4. **Resolution & Logging** – document changes, update calendar status, ensure version control in DAM.
5. **Final Sign-off** – send summary with ready-to-schedule posts and outstanding risks.

## Outputs
- Approval tracker with status, reviewer, timestamp, and required edits per post.
- Consolidated feedback log + action items for asset owners.
- Sign-off summary sent to publishing team and stakeholders.

## Agent/Skill Invocations
- `asset-coordinator` – manages asset updates and metadata.
- `brand-guardrails` skill – enforces brand/legal rules before sign-off.
- `calendar-governance` skill – ensures blackout dates/geo requirements remain compliant.

---
