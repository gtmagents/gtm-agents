---
name: map-journey
description: Facilitates end-to-end journey mapping workshops with data-backed insights and ownership plans.
usage: /customer-journey-orchestration:map-journey --persona "IT Director" --scope "onboarding" --horizon 6months
---

# Command: map-journey

## Inputs
- **persona** – target persona or segment.
- **scope** – journey slice (awareness, onboarding, adoption, renewal, expansion).
- **horizon** – time window to analyze (e.g., 6months, lifecycle).
- **data_sources** – optional list of VOC/telemetry sources to emphasize.
- **facilitators** – optional list of stakeholders joining workshops.

### GTM Agents Pattern & Plan Checklist
> Based on GTM Agents orchestrator blueprint @puerto/plugins/orchestrator/README.md#112-325.

- **Pattern selection**: Journey mapping typically runs **pipeline** (discovery → workshop → evidence → gaps → synthesis). If workshop activities can split (e.g., persona + channel subgroups), log a **diamond** segment with merge gate in the plan header.
- **Plan schema**: Save `.claude/plans/plan-<timestamp>.json` capturing persona, scope, task IDs, parallel groups, dependency graph (research, CX ops, product), error handling, and success metrics (gap closure %, NPS uplift, time-to-resolution).
- **Tool hooks**: Reference `docs/gtm-essentials.md` stack—Serena for instrumentation diffs, Context7 for VOC/support docs, Sequential Thinking for facilitation prompts, Playwright for QA on journey prototypes if needed.
- **Guardrails**: Default retry limit = 2 for evidence gaps or facilitation blockers; escalation ladder = CX Strategist → Journey Ops Owner → CCO/CS leadership.
- **Review**: Run `docs/usage-guide.md#orchestration-best-practices-puerto-parity` before execution to confirm facilitators, dependencies, and deliverables.

## Workflow
1. **Discovery Packet** – compile research, telemetry, and existing maps for the selected persona/scope.
2. **Workshop Flow** – guide stakeholders through stage definition, touchpoint inventory, emotion mapping, and ownership assignment.
3. **Evidence Layer** – inject VOC quotes, product metrics, and support data to ground decisions.
4. **Gap Logging** – capture friction points, root causes, and potential solutions.
5. **Synthesis** – produce journey blueprint, highlight quick wins, and queue items for prioritization.

## Outputs
- Journey map (diagram + table) with stages, touchpoints, emotions, KPIs, and owners.
- Gap log referencing supporting data and potential solutions.
- Stakeholder recap with action items and next steps.
- Plan JSON entry stored/updated in `.claude/plans` for audit trail.

## Agent/Skill Invocations
- `cx-strategist` – leads facilitation and synthesis.
- `journey-mapping` skill – provides templates/checklists.
- `research-lead` – injects VOC evidence.

## GTM Agents Safeguards
- **Fallback agents**: document substitutes (e.g., Journey Ops Owner covering CX Strategist) when facilitators unavailable.
- **Escalation triggers**: if critical gaps lack owners after two checkpoints or evidence quality falls below guardrails, escalate to CX + Product leadership per GTM Agents rip-cord.
- **Plan maintenance**: update plan JSON/change log when scope, facilitators, or data sources change to keep audit alignment with GTM Agents procedures.

---
