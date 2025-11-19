---
name: manage-production
description: Builds a production plan with tasks, owners, deadlines, and QA checkpoints for creative assets.
usage: /design-creative:manage-production --campaign "Platform Launch" --assets "hero,landing,email" --deadline 2025-12-10 --tools asana
---

# Command: manage-production

## Inputs
- **campaign** – campaign/initiative name.
- **assets** – comma-separated list (hero, landing, email, video, motion, print).
- **deadline** – launch or delivery date.
- **tools** – optional project tool reference (asana, jira, notion).
- **localization** – true/false for translation workflows.

## Workflow
1. **Inventory & Dependencies** – parse asset list, required formats, and upstream inputs.
2. **Timeline Builder** – create workback schedule with draft/review/polish milestones.
3. **Resource Allocation** – assign designers, writers, motion, QA owners, approvers.
4. **Workflow Automation** – generate task board with statuses, labels, and SLAs.
5. **QA + Handoff** – embed QA checklists, localization steps, and delivery instructions.

## Outputs
- Production workback plan (Gantt/table) with owners + due dates.
- Task board template for import into project tools.
- QA & localization checklist linked per asset.

## Agent/Skill Invocations
- `design-ops-lead` – orchestrates workflow + assignments.
- `creative-director` – sets review gates.
- `brand-strategist` – ensures messaging alignment.
- `production-playbook` skill – provides workflow + template library.
- `creative-qa-checklist` skill – adds QA steps (accessibility, localization, devices).

---
