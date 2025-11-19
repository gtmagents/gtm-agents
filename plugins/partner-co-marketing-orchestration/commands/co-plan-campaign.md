---
name: co-plan-campaign
description: Builds a joint marketing brief with objectives, audiences, assets, and responsibilities across partners.
usage: /partner-co-marketing-orchestration:co-plan-campaign --campaign "AI Launch Tour" --partners "Acme,Northwind" --window 8weeks
---

# Command: co-plan-campaign

## Inputs
- **campaign** – name of the joint initiative.
- **partners** – comma-separated partner org names.
- **window** – planning horizon or launch window.
- **objectives** – optional KPIs (pipeline, signups, ARR, adoption).
- **audiences** – optional personas or regions.

### GTM Agents Pattern & Plan Checklist
> Based on GTM Agents orchestrator blueprint @puerto/plugins/orchestrator/README.md#112-325.

- **Pattern selection**: Co-planning typically follows a **pipeline** (intake → messaging → channel → assets → governance). If channel and asset workstreams can run in parallel, log a **diamond** segment with merge gate in the plan header.
- **Plan schema**: Save `.claude/plans/plan-<timestamp>.json` capturing objectives, partner roles, task IDs, dependencies (legal/compliance, asset repos, data sharing), error handling, and success metrics (pipeline, sourced revenue, lead targets).
- **Tool hooks**: Reference `docs/gtm-essentials.md` stack—Serena for asset template diffs, Context7 for partner/brand guidelines, Sequential Thinking for steering committee checkpoints, Playwright for QA of landing pages/microsites.
- **Guardrails**: Default retry limit = 2 for approval delays or dependency blockers; escalation ladder = Partner Marketer → Partner Ops Lead → Exec Sponsors across companies.
- **Review**: Run `docs/usage-guide.md#orchestration-best-practices-puerto-parity` before execution to confirm owners, dependencies, deliverables.

## Workflow
1. **Brief Intake** – capture each partner's goals, offers, ICP, and available assets.
2. **Messaging & Offer** – align on key narrative, value props, and differentiation.
3. **Channel Plan** – map owned, shared, and paid channels with cadence + owners.
4. **Asset Requirements** – detail creative needs, content formats, localization, and compliance.
5. **Governance Packet** – document approvals, brand guidelines, legal checkpoints, and comms plan.

## Outputs
- Joint campaign brief (objectives, audience, narrative, KPIs, timeline).
- Asset + channel tracker with partner assignments and due dates.
- Risk + dependency log for cross-org coordination.
- Plan JSON entry stored/updated in `.claude/plans` for audit trail.

## Agent/Skill Invocations
- `partner-marketer` – leads agenda and stakeholder alignment.
- `co-branding` skill – enforces visual + messaging standards.
- `asset-manager` – tracks deliverables and approval workflow.

## GTM Agents Safeguards
- **Fallback agents**: note substitutes (e.g., Partner Ops covering Partner Marketer) when stakeholders unavailable.
- **Escalation triggers**: if approvals or legal checkpoints miss SLA twice or partners deviate from guardrails, escalate to governance council per GTM Agents rip-cord.
- **Plan maintenance**: update plan JSON/change log whenever objectives, owners, or compliance requirements change to keep audit parity.

---
