---
name: manage-production
description: Generates a production tracker with tasks, owners, feedback cycles, and QA steps.
usage: /content-pipeline-orchestration:manage-production --pillar "AI readiness" --assets "ebook,video,design kit"
---

# Command: manage-production

## Inputs
- **pillar** – reference pillar or campaign.
- **assets** – comma-separated asset types or names.
- **tools** – optional tools/platforms (Docs, Figma, Notion, CMS).
- **qa** – include QA/evidence plan (default true).
- **localization** – regions/languages requiring localization.

### GTM Agents Pattern & Plan Checklist
> Pulled from GTM Agents orchestrator blueprint @puerto/plugins/orchestrator/README.md#112-325.

- **Pattern selection**: Production typically runs **pipeline** (tasks → owners → feedback → QA → packaging). Use **diamond** when localization or QA evidence can run parallel; document choice in the plan header.
- **Plan schema**: Save or update `.claude/plans/plan-<timestamp>.json` with task IDs, asset references, tooling context, parallel groups, handoff requirements, error handling, and success criteria (on-time %, defect ceiling).
- **Tool hooks**: Reference `docs/gtm-essentials.md` stack (Serena for CMS automation patches, Context7 for brand/legal standards, Sequential Thinking for retros, Playwright for accessibility/QA screens).
- **Guardrails**: Default retry limit = 2 for failed QA; escalation ladder = Creative Producer → Editorial Director → Marketing Director.
- **Review**: Run `docs/usage-guide.md#orchestration-best-practices-puerto-parity` before execution to confirm agents, dependencies, deliverables.

## Workflow
1. **Task Breakdown** – create tasks per asset (draft, design, review, localization, QA).
2. **Owner Assignment** – map writers, designers, reviewers, approvers, and due dates.
3. **Feedback Loops** – schedule review checkpoints, consolidate feedback instructions.
4. **QA Checklist** – ensure brand, accessibility, legal, and technical requirements are validated.
5. **Asset Packaging** – outline final delivery steps (naming conventions, metadata, storage paths).

## Outputs
- Production tracker (task, owner, status, due date, dependencies, comments).
- QA/evidence log template.
- Asset handoff checklist with storage locations.
- Plan JSON entry stored/updated in `.claude/plans` for audit trail.

## Agent/Skill Invocations
- `creative-producer` – runs production board + QA.
- `asset-tracking` skill – ensures dependencies + metadata.
- `distribution-lead` – receives handoff package for publishing.

## GTM Agents Safeguards
- **Fallback agents**: document substitutes (e.g., Editorial Director covering Creative Producer) when specialists unavailable.
- **Escalation triggers**: if QA defects, brand issues, or missed deadlines breach guardrails twice in 48h, escalate to Content + Growth leadership per GTM Agents runbook.
- **Plan maintenance**: update plan JSON and change log whenever assets, owners, or QA scope shift so audit trail mirrors GTM Agents standards.

---
