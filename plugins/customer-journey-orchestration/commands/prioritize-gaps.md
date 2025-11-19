---
name: prioritize-gaps
description: Scores journey friction points, aligns owners, and builds remediation roadmap.
usage: /customer-journey-orchestration:prioritize-gaps --persona "IT Director" --scope onboarding --limit 10
---

# Command: prioritize-gaps

## Inputs
- **persona** – persona/segment for gap analysis.
- **scope** – journey stage or lifecycle slice.
- **limit** – optional cap on number of gaps to surface.
- **criteria** – optional weighting scheme (impact, effort, urgency, customer value).
- **dependencies** – optional notes about systems/teams involved.

### GTM Agents Pattern & Plan Checklist
> Mirrors GTM Agents orchestrator blueprint @puerto/plugins/orchestrator/README.md#112-325.

- **Pattern selection**: Gap prioritization generally runs **pipeline** (aggregation → scoring → owner mapping → roadmap → comms). If scoring + owner mapping can run in parallel (multiple pods), document a **diamond** segment with merge gate in the plan header.
- **Plan schema**: Save `.claude/plans/plan-<timestamp>.json` with persona/scope, task IDs, weighting criteria, parallel groups, dependency graph (ops, product, eng), error handling, and success metrics (gap closure %, CSAT uplift, time-to-fix).
- **Tool hooks**: Reference `docs/gtm-essentials.md` stack—Serena for instrumentation diffs, Context7 for VOC/support docs, Sequential Thinking for decision tree prompts, Playwright for QA on prototype fixes if required.
- **Guardrails**: Default retry limit = 2 for scoring/owner mapping failures; escalation path = Journey Ops Owner → CX Strategist → CCO/CS leadership.
- **Review**: Use `docs/usage-guide.md#orchestration-best-practices-puerto-parity` before execution to confirm facilitators, data sources, and deliverables.

## Workflow
1. **Gap Aggregation** – pull journey map findings, VOC insights, support tickets, and telemetry anomalies.
2. **Scoring Engine** – apply weighting (impact × frequency × effort × strategic fit) to rank opportunities.
3. **Owner Mapping** – assign accountable teams, supporting partners, and required approvals.
4. **Roadmap Packaging** – cluster into quick wins, strategic bets, and structural fixes with timelines.
5. **Communication Plan** – generate summary for executives + working teams with next steps.

## Outputs
- Prioritized gap list with scores, owners, and proposed actions.
- Portfolio view (quick wins vs strategic initiatives) with resource estimates.
- Governance-ready backlog entry for each initiative.
- Plan JSON entry stored/updated in `.claude/plans` for audit trail.

## Agent/Skill Invocations
- `journey-ops-owner` – coordinates resourcing + timelines.
- `journey-mapping` skill – ensures gap definitions align with map standards.
- `voice-of-customer` skill – keeps scoring grounded in customer evidence.

## GTM Agents Safeguards
- **Fallback agents**: document substitutes (e.g., CX Strategist covering Journey Ops Owner) when resource owners unavailable.
- **Escalation triggers**: if high-impact gaps remain unassigned after two checkpoints or portfolio balance violates guardrails, escalate to CX/Product leadership per GTM Agents rip-cord.
- **Plan maintenance**: update plan JSON/change log whenever scoring criteria, owners, or dependencies change to maintain GTM Agents audit parity.

---
