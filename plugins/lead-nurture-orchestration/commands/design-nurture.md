---
name: design-nurture
description: Produces a multi-stage nurture journey blueprint with segmentation, triggers, and content plan.
usage: /lead-nurture-orchestration:design-nurture --goal pipeline --segments "mid-market,enterprise" --length 6
---

# Command: design-nurture

## Inputs
- **goal** – pipeline, expansion, adoption, education, reactivation.
- **segments** – comma-separated audiences.
- **length** – desired number of steps/stages.
- **channels** – optional list (email, in-app, ads, SDR assist).
- **constraints** – optional compliance/brand limitations.

### GTM Agents Pattern & Plan Checklist
> Derived from GTM Agents orchestrator blueprint @puerto/plugins/orchestrator/README.md#112-325.

- **Pattern selection**: Most nurture builds follow a **pipeline** (brief → architecture → content → branching → measurement). Switch to **diamond** when content mapping and personalization work can run in parallel. Document the pattern in the plan header.
- **Plan schema**: Save `.claude/plans/plan-<timestamp>.json` with objective, stages, task IDs, parallel groups, context passing (e.g., audience segments), error handling, and success criteria (activation, SQL lift, etc.).
- **Tool hooks**: Reference `docs/gtm-essentials.md` (Serena for MAP/CRM automation patches, Context7 for platform docs, Sequential Thinking for retros, Playwright for landing/in-app QA).
- **Guardrails**: Set retry limits (default 2) and escalation flow (Nurture Architect → Marketing Ops Lead → RevOps) if automation validation fails.
- **Review**: Use `docs/usage-guide.md#orchestration-best-practices-puerto-parity` checklist before execution to confirm agents, dependencies, deliverables.

## Workflow
1. **Brief Alignment** – confirm ICP, lifecycle stage, KPIs, and signal availability.
2. **Stage Architecture** – define entry criteria, triggers, and suppression per segment.
3. **Content Mapping** – outline assets, offers, personalization tokens per touch.
4. **Branching & Fail-safes** – specify conditional logic, fallback steps, exit rules.
5. **Measurement Plan** – KPIs per stage, alerting, retro cadence, experiment backlog.

## Outputs
- Journey table (step, trigger, channel, asset, CTA, owner).
- Mermaid-style diagram or pseudo-code for automation teams.
- Asset + data requirements list with due dates and owners.
- Plan JSON entry stored/updated in `.claude/plans` for audit trail.

## Agent/Skill Invocations
- `nurture-architect` – leads design.
- `lifecycle-cadence` skill – validates pacing + suppression.
- `personalization-logic` skill – ensures tailored content blocks.

## GTM Agents Safeguards
- **Fallback agents**: note substitutions (e.g., Marketing Ops Partner covering Personalization) if a specialist is unavailable.
- **Escalation triggers**: if guardrails (drop-off %, unsubscribe, latency) breach twice within 48h, escalate per lifecycle rip-cord (Marketing Director + Sales Director).
- **Plan maintenance**: When segments, owners, or branching logic change, update the saved plan and reference change log in status packets.

---
