---
name: route-insights
description: Operationalizes feedback themes by assigning owners, communication plans, and tracking loops.
usage: /customer-feedback-orchestration:route-insights --themes file://themes.json --cadence monthly --channels "product,cs,marketing"
---

# Command: route-insights

## Inputs
- **themes** – JSON/CSV file or inline JSON containing prioritized themes from `synthesize-feedback`.
- **cadence** – meeting or reporting cadence (weekly, biweekly, monthly).
- **channels** – comma-separated functional audiences (product, cs, marketing, exec, community).
- **broadcast** – true/false toggle to auto-generate comms templates for customers.
- **tracking** – project tool identifier (asana, jira, notion) for action logging.

### GTM Agents Pattern & Plan Checklist
> Mirrors GTM Agents orchestrator blueprint @puerto/plugins/orchestrator/README.md#112-325.

- **Pattern selection**: Insight routing generally runs **pipeline** (theme intake → owner mapping → action serialization → communications → feedback loop). If action serialization + comms can run in parallel, document a **diamond** block with merge gate in the plan header.
- **Plan schema**: Save `.claude/plans/plan-<timestamp>.json` capturing theme set, DRIs, dependency graph (product, CS, marketing, exec), error handling, and success metrics (resolution rate, time-to-close, comms completion).
- **Tool hooks**: Reference `docs/gtm-essentials.md` stack—Serena for workflow automation diffs, Context7 for past retros + roadmap docs, Sequential Thinking for follow-up cadence, Playwright for portal/comms QA if needed.
- **Guardrails**: Default retry limit = 2 for task routing/comms failures; escalation ladder = Product Liaison → CX Leadership → Exec sponsor.
- **Review**: Run `docs/usage-guide.md#orchestration-best-practices-puerto-parity` before publishing to confirm dependencies, approvals, deliverables.

## Workflow
1. **Theme Intake** – validate scoring, persona coverage, and urgency tags.
2. **Owner Mapping** – assign DRIs per functional area, define success metrics, and set deadlines.
3. **Action Serialization** – create tasks/epics with references to supporting data and customer quotes.
4. **Communication Plan** – craft internal/external messaging, executive summaries, and customer follow-ups.
5. **Feedback Loop Setup** – configure progress dashboards, reminders, and close-the-loop alerts.

## Outputs
- Routing table (theme, owner, due date, metric, status).
- Internal + external comms templates referencing impact and next steps.
- Action tracker ready for import into chosen project tool.
- Plan JSON entry stored/updated in `.claude/plans` for audit trail.

## Agent/Skill Invocations
- `product-liaison` – ensures roadmap alignment and executive visibility.
- `cs-analyst` – verifies metrics + datasets tied to each action.
- `stakeholder-ops` skill – governs approvals, cadences, and comms.
- `insight-synthesis` skill – keeps narratives consistent with source data.

## GTM Agents Safeguards
- **Fallback agents**: document substitutes (e.g., CX Ops covering Product Liaison) when stakeholders unavailable.
- **Escalation triggers**: if SLAs for close-the-loop breaching twice or roadmap owners reject actions repeatedly, escalate via GTM Agents rip-cord and log remediation inside plan JSON.
- **Plan maintenance**: update plan JSON/change log when owners, cadences, or tracking tools change to maintain audit parity.

---
