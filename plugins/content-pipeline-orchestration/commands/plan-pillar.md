---
name: plan-pillar
description: Produces a content pillar blueprint with hero assets, derivatives, and distribution plan.
usage: /content-pipeline-orchestration:plan-pillar --theme "AI readiness" --window 8w --channels "blog,video,webinar"
---

# Command: plan-pillar

## Inputs
- **theme** – content pillar topic.
- **window** – program duration.
- **channels** – comma-separated roster (blog, video, webinar, social, email, enablement).
- **audiences** – optional persona/vertical list.
- **goals** – optional KPIs (pipeline, subscribers, product adoption).

### GTM Agents Pattern & Plan Checklist
> Derived from GTM Agents orchestrator blueprint @puerto/plugins/orchestrator/README.md#112-325.

- **Pattern selection**: Default to **pipeline** (brief → hero asset → derivatives → owners → distribution). Use **diamond** when creative pods and distribution prep can run in parallel; document the pattern in the plan header.
- **Plan schema**: Save `.claude/plans/plan-<timestamp>.json` with objective, asset stages, task IDs, parallel groups, dependency graph, error handling, and success criteria (e.g., MQL, pipeline, share of voice).
- **Tool hooks**: Reference `docs/gtm-essentials.md` stack (Serena for CMS/landing updates, Context7 for brand/legal docs, Sequential Thinking for retros, Playwright for QA of landing pages).
- **Guardrails**: Define retry strategy (default 2) and escalation ladder (Editorial Director → Creative Producer → Marketing Director) for missed approvals or QA issues.
- **Review**: Before execution, run the checklist in `docs/usage-guide.md#orchestration-best-practices-puerto-parity` to confirm agents, dependencies, deliverables.

## Workflow
1. **Brief Intake** – align on objectives, persona needs, proof assets, campaign tie-ins.
2. **Hero Asset Definition** – define flagship deliverables (ebook, webinar, video series) with requirements.
3. **Derivative Mapping** – outline derivative assets per channel with rough cadence.
4. **Resourcing & Owners** – assign writers, designers, reviewers, budgets, tooling.
5. **Distribution Hooks** – highlight promotion partners, paid support, enablement ties.

## Outputs
- Pillar blueprint table (asset, format, owner, due date, CTA, dependency).
- Creative brief package template per asset.
- Initial distribution + amplification notes.
- Plan JSON entry stored/updated in `.claude/plans` for audit trail.

## Agent/Skill Invocations
- `editorial-director` – leads strategy + calendar.
- `editorial-calendar` skill – enforces cadence + governance.
- `asset-tracking` skill – maps resources + dependencies.

## GTM Agents Safeguards
- **Fallback agents**: document substitutes (e.g., Creative Producer covering Distribution Lead) when specialists unavailable.
- **Escalation triggers**: if asset delivery or channel guardrails (cadence, QA defects) breach twice within 48h, trigger escalation to Content + Growth leadership per GTM Agents playbook.
- **Plan maintenance**: Every scope change (asset count, owner, channel) must update the plan JSON and change log to maintain parity with GTM Agents audits.

---
