---
name: orchestrate-renewal-play
description: Coordinates cross-functional renewal motions with timelines, stakeholder tasks, and escalation paths.
usage: /renewal-orchestration:orchestrate-renewal-play --account "ACME Corp" --tier strategic --risk red --play "exec-save"
---

# Command: orchestrate-renewal-play

## Inputs
- **account** – required account name or ID.
- **tier** – strategic | growth | scale segments.
- **risk** – green | yellow | red (sets default cadence + oversight).
- **play** – playbook identifier (exec-save, value-realization, pricing-refresh, adoption-accelerator).
- **deadline** – renewal date or milestone to anchor the plan.

### GTM Agents Pattern & Plan Checklist
> Mirrors GTM Agents orchestrator blueprint @puerto/plugins/orchestrator/README.md#112-325.

- **Pattern selection**: Renewal plays generally run **pipeline** (context → customization → tasks → enablement → governance). If enablement + task orchestration can run in parallel, log a **diamond** segment with merge gate.
- **Plan schema**: Save `.claude/plans/plan-<timestamp>.json` capturing objective, risk tier, task IDs, parallel groups, dependency graph (exec sponsor, product, finance), error handling, and success metrics (renewal %, expansion, churn risk reduction).
- **Tool hooks**: Reference `docs/gtm-essentials.md` stack—Serena for contract/CRM diffs, Context7 for product/legal docs, Sequential Thinking for retrospection, Playwright for portal/usage QA when required.
- **Guardrails**: Default retry limit = 2 for missed checkpoints; escalation path = CSM → Renewal Director → CRO/Exec Sponsor, aligned with `escalation-framework` skill.
- **Review**: Run `docs/usage-guide.md#orchestration-best-practices-puerto-parity` checklist before execution to confirm agents, dependencies, deliverables.

## Workflow
1. **Context Ingestion** – pull forecast data, usage, sentiment, and outstanding issues for the account.
2. **Play Customization** – tailor messaging, milestones, and proof points to persona stack + risk level.
3. **Task Orchestration** – generate workback plan with owners (CSM, AE, exec sponsor, product, finance).
4. **Enablement Package** – attach decks, ROI analyses, roadmap updates, and FAQ docs.
5. **Governance & Tracking** – log actions in CRM/project tools, set status checkpoints, and escalation triggers.

## Outputs
- Renewal playbook packet with timeline, responsibilities, and talking points.
- Task and escalation list ready for import into CRM/project tools.
- Status tracker with checkpoints mapped to `escalation-framework` requirements.
- Plan JSON entry stored/updated in `.claude/plans` for audit trail.

## Agent/Skill Invocations
- `cs-ops-partner` – ensures workflows + automations match governance rules.
- `exec-sponsor` – reviews strategic motions and commits resources.
- `renewal-playbooks` skill – provides templates and messaging blocks.
- `deal-desk` skill – aligns commercial terms + approvals.

## GTM Agents Safeguards
- **Fallback agents**: document substitutes (e.g., Renewal Director covering Exec Sponsor) if stakeholders unavailable.
- **Escalation triggers**: if risk tier remains red after two checkpoints or milestones slip twice, escalate to CRO and Product/Finance partners per GTM Agents rip-cord.
- **Plan maintenance**: update plan JSON/change log whenever play selection, stakeholders, or escalation paths change, keeping audit parity with GTM Agents procedures.

---
