---
name: launch-program
description: Orchestrates referral program launch tasks, tooling, and communications.
usage: /referral-program-orchestration:launch-program --program "Customer Advocates" --launch-date 2025-12-10 --channels "email,in-app"
---

# Command: launch-program

## Inputs
- **program** – name/ID of referral initiative.
- **launch-date** – target go-live date.
- **channels** – comma-separated launch/promotion channels.
- **segments** – optional list of participant personas.
- **approvers** – optional stakeholders for gating steps.

### GTM Agents Pattern & Plan Checklist
> Mirrors GTM Agents orchestrator blueprint @puerto/plugins/orchestrator/README.md#112-325.

- **Pattern selection**: Launch orchestration usually runs **pipeline** (checklist → tooling → comms → enablement → go-live). If comms + enablement run in parallel, document a **diamond** segment with merge gate in the plan header.
- **Plan schema**: Save `.claude/plans/plan-<timestamp>.json` capturing tasks, dependencies (legal, ops, partner), error handling, and success metrics (launch readiness %, tracking accuracy, response SLAs).
- **Tool hooks**: Reference `docs/gtm-essentials.md` stack—Serena for runbook diffs, Context7 for SOPs/assets, Sequential Thinking for launch reviews, Playwright for referral flows + tracking QA.
- **Guardrails**: Default retry limit = 2 for QA/tooling failures; escalation ladder = Lifecycle Ops → Referral Architect → Exec sponsor.
- **Review**: Run `docs/usage-guide.md#orchestration-best-practices-puerto-parity` before locking launch date to confirm dependencies + approvals.

## Workflow
1. **Checklist Creation** – pull design charter, list tasks (tooling, creative, legal, finance) with owners.
2. **Tooling & QA** – coordinate lifecycle ops to finalize forms, tracking, reward fulfillment, and MAP workflows.
3. **Communications** – auto-generate launch emails, in-app prompts, partner kits, and support scripts.
4. **Training & Enablement** – schedule sessions for sales/CS, publish FAQs, and update help center entries.
5. **Go-live & Monitoring** – run day-of checklist, confirm tracking, enable dashboards, and log outcomes.

## Outputs
- Launch runbook with tasks, owners, due dates, and status.
- Comms kit (emails, social posts, landing pages) packaged for GTM teams.
- Monitoring plan linking dashboards, alerts, and incident response steps.
- Plan JSON entry stored/updated in `.claude/plans` for audit trail.

## Agent/Skill Invocations
- `lifecycle-ops` – drives tooling + QA.
- `partner-manager` – coordinates partner enablement and post-launch support.
- `partner-ops` skill – ensures partner workflows and approvals are documented.

## GTM Agents Safeguards
- **Fallback agents**: document substitutes (e.g., Partner Manager covering Lifecycle Ops) when leads unavailable.
- **Escalation triggers**: escalate if tooling QA fails twice or compliance approvals slip; follow GTM Agents rip-cord, log remediation in plan JSON.
- **Plan maintenance**: update plan JSON/change log when tasks, owners, or channels change to keep audit-ready history.

---
