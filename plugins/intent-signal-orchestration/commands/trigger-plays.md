---
name: trigger-plays
description: Launches multi-channel plays based on live signals with safeguards, SLA tracking, and measurement hooks.
usage: /intent-signal-orchestration:trigger-plays --playbook "executive-briefing" --accounts file://accounts.csv --channels "sales,ads,email"
---

# Command: trigger-plays

## Inputs
- **playbook** – required identifier referencing a predefined program (executive-briefing, surge-outreach, nurture-reset).
- **accounts** – CSV/JSON path or comma list of account IDs to activate.
- **channels** – comma-separated list (sales, ads, email, web, events).
- **signals** – optional signal filters or thresholds.
- **suppress** – true/false to enforce global suppression logic before triggering.

### GTM Agents Pattern & Plan Checklist
> Mirrors GTM Agents orchestrator blueprint @puerto/plugins/orchestrator/README.md#112-325.

- **Pattern selection**: Activation typically runs **pipeline** (eligibility → play assembly → channel execution → telemetry → monitoring). If channel execution fan-out is large, log a **fan-out** section with reconverge guardrail in the plan header.
- **Plan schema**: Save `.claude/plans/plan-<timestamp>.json` capturing playbook, account set, dependency graph (automation, sales, marketing), error handling, and success metrics (SLA adherence, reply/conversion lift, suppression integrity).
- **Tool hooks**: Reference `docs/gtm-essentials.md` stack—Serena for playbook diffs, Context7 for SOPs/runbooks, Sequential Thinking for go/no-go reviews, Playwright for landing page or form QA.
- **Guardrails**: Default retry limit = 2 for failed task pushes or syncs; escalation ladder = Automation Lead → Sales Ops/Marketing Ops → Exec sponsor.
- **Review**: Run `docs/usage-guide.md#orchestration-best-practices-puerto-parity` before triggering to confirm dependencies, approvals, and suppression compliance.

## Workflow
1. **Eligibility Check** – confirm each account meets signal thresholds and is not suppressed.
2. **Play Assembly** – map approved accounts to playbook actions, cadences, and owners.
3. **Channel Execution** – push tasks to CRM/engagement tools, sync audiences to ads, and schedule nurture branches.
4. **Telemetry Setup** – attach UTM parameters, experiment IDs, and success metrics per channel.
5. **Monitoring & Escalation** – track SLA adherence, bouncebacks, or conflicts; notify owners when intervention is needed.

## Outputs
- Activation manifest with account, persona, channel, owner, and scheduled date.
- SLA dashboard snapshot plus webhook notifications for go-live.
- Post-play measurement brief template for RevOps + GTM leads.
- Plan JSON entry stored/updated in `.claude/plans` for audit trail.

## Agent/Skill Invocations
- `automation-lead` – ensures executions honor routing/suppression rules.
- `sales-liaison` – coordinates rep-owned steps.
- `outbound-plays` skill – provides channel-specific messaging + cadences.
- `suppression-logic` skill – runs compliance + conflict checks.

## GTM Agents Safeguards
- **Fallback agents**: document substitutes (e.g., Sales Liaison covering Automation Lead) when leads unavailable.
- **Escalation triggers**: if SLA breaches occur twice or suppression conflicts trigger, execute GTM Agents rip-cord, halt plays, and log remediation in plan JSON.
- **Plan maintenance**: update plan JSON/change log when playbooks, account lists, or channel mix change to preserve audit traceability.

---
