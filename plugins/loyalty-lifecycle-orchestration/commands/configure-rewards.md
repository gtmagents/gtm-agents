---
name: configure-rewards
description: Orchestrates reward catalog setup, fulfillment workflows, and QA before launch.
usage: /loyalty-lifecycle-orchestration:configure-rewards --program "Tiered Loyalty" --catalog drive://loyalty --launch-date 2026-01-15
---

# Command: configure-rewards

## Inputs
- **program** – reference name/ID for the loyalty initiative.
- **catalog** – storage location or doc with reward definitions.
- **launch-date** – target go-live date.
- **regions** – optional localization list for compliance and fulfillment.
- **approvers** – optional stakeholders (legal, finance, partner, ops).

### GTM Agents Pattern & Plan Checklist
> Mirrors GTM Agents orchestrator blueprint @puerto/plugins/orchestrator/README.md#112-325.

- **Pattern selection**: Reward configuration usually runs **pipeline** (catalog intake → fulfillment design → compliance QA → launch packet). If QA + compliance run in parallel, document a **diamond** block with merge gate in the plan header.
- **Plan schema**: Save `.claude/plans/plan-<timestamp>.json` capturing catalog source, fulfillment automations, dependency graph (legal, finance, ops, vendors), error handling, and success metrics (SLA, redemption accuracy, fraud rate).
- **Tool hooks**: Reference `docs/gtm-essentials.md` stack—Serena for catalog diffs, Context7 for compliance/billing SOPs, Sequential Thinking for QA retros, Playwright for redemption form testing.
- **Guardrails**: Default retry limit = 2 for failed catalog loads or QA runs; escalation ladder = Reward Ops → Finance/Legal → Exec sponsor.
- **Review**: Run `docs/usage-guide.md#orchestration-best-practices-puerto-parity` before launch to confirm dependencies + approvals.

## Workflow
1. **Catalog Intake** – load reward definitions (cost, eligibility, inventory) plus vendor details.
2. **Fulfillment Design** – define earning/redemption automations, notification flows, and SLA tracking.
3. **Compliance & Risk** – validate tax regulations, export controls, and fraud safeguards.
4. **QA Checklist** – run test transactions across tiers, currencies, devices, and failure scenarios.
5. **Launch Packet** – produce runbook, escalation plan, and monitoring dashboard references.

## Outputs
- Reward configuration checklist with owner + status.
- QA evidence (screenshots, logs, test cases) stored with catalog.
- Fulfillment runbook (SLA, webhook IDs, contact points) for ops + support teams.
- Plan JSON entry stored/updated in `.claude/plans` for audit trail.

## Agent/Skill Invocations
- `reward-operations` – leads fulfillment + QA steps.
- `loyalty-strategist` – approves benefit alignment with goals.
- `reward-ops` skill – enforces operational standards.
- `loyalty-modeling` skill – confirms economics after final catalog changes.

## GTM Agents Safeguards
- **Fallback agents**: document substitutes (e.g., Reward Ops covering Strategist) when approvers unavailable.
- **Escalation triggers**: escalate if QA fails twice or compliance issues surface; follow GTM Agents rip-cord and log remediation inside plan JSON.
- **Plan maintenance**: update plan JSON/change log whenever catalog, vendors, or launch dates shift for audit parity.

---
