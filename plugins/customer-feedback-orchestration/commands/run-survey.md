---
name: run-survey
description: Launches customer surveys with sampling plans, question sets, and automation hooks.
usage: /customer-feedback-orchestration:run-survey --audience "admins" --goal adoption --channels "email,in-app" --deadline 2025-12-15
---

# Command: run-survey

## Inputs
- **audience** – persona or segment target (admins, champions, exec sponsors).
- **goal** – objective (adoption, roadmap validation, satisfaction, messaging test).
- **channels** – comma-separated distribution methods (email, in-app, community, CS-led).
- **deadline** – fielding end date or fixed duration.
- **incentive** – optional reward description or budget.
- **sample_size** – desired number of responses (numeric).

### GTM Agents Pattern & Plan Checklist
> Mirrors GTM Agents orchestrator blueprint @puerto/plugins/orchestrator/README.md#112-325.

- **Pattern selection**: Survey orchestration typically runs **pipeline** (brief → question design → sampling → monitoring → handoff). If question design + sampling prep run in parallel, note a **diamond** block with merge gate in the plan header.
- **Plan schema**: Save `.claude/plans/plan-<timestamp>.json` capturing audience, goals, sampling logic, dependency graph (legal, CS, research ops), error handling, and success metrics (response rate, completion %, demographic balance).
- **Tool hooks**: Reference `docs/gtm-essentials.md` stack—Serena for MAP automation diffs, Context7 for research SOPs + historic surveys, Sequential Thinking for pre/post-readouts, Playwright for survey QA.
- **Guardrails**: Default retry limit = 2 for distribution/QA failures; escalation ladder = Research Lead → Customer Marketing → Exec sponsor.
- **Review**: Run `docs/usage-guide.md#orchestration-best-practices-puerto-parity` before launch to confirm dependencies, approvals, deliverables.

## Workflow
1. **Brief Assembly** – capture goals, personas, hypotheses, and stakeholder approvals.
2. **Question Design** – generate question bank with logic, scales, and branching recommendations.
3. **Sampling & Distribution** – build target lists, dedupe suppression lists, schedule sends.
4. **Monitoring** – track response rates, data quality, and audience balance; trigger boosts if needed.
5. **Handoff** – package clean dataset + metadata for `synthesize-feedback` command.

## Outputs
- Survey plan (audience, sample, channels, incentive, timeline).
- Question set with logic map and translation/localization notes.
- Distribution checklist + automation steps for MAP/CS tooling.
- Plan JSON entry stored/updated in `.claude/plans` for audit trail.

## Agent/Skill Invocations
- `research-lead` – validates methodology and question quality.
- `cs-analyst` – ensures sampling + data integrity.
- `survey-design` skill – provides templates and guardrails.
- `stakeholder-ops` skill – outlines approvals + comms.

## GTM Agents Safeguards
- **Fallback agents**: document substitutes (e.g., CS Analyst covering Research Lead) when leads unavailable.
- **Escalation triggers**: if response rate misses guardrail twice or sampling bias detected, escalate via GTM Agents rip-cord and log corrective actions in plan JSON.
- **Plan maintenance**: update plan JSON/change log when audiences, question sets, or tooling stacks change to preserve audit parity.

---
