---
name: define-handoff
description: Establishes marketing-to-sales routing design, SLAs, and enablement requirements.
usage: /sales-handoff-orchestration:define-handoff --segment enterprise --goal pipeline --response-sla 2h
---

# Command: define-handoff

## Inputs
- **segment** – target segment/persona (enterprise, mid-market, SMB, partner).
- **goal** – business target (pipeline, expansion, product activation, ABM campaign).
- **response-sla** – desired first-touch SLA (e.g., 2h, 1d).
- **capacity** – optional SDR/AE capacity notes to shape routing rules.
- **dependencies** – optional systems/content that must be ready (scoring, sequences, talk tracks).

### GTM Agents Pattern & Plan Checklist
> Derived from GTM Agents orchestrator blueprint @puerto/plugins/orchestrator/README.md#112-325.

- **Pattern selection**: Handoff design usually follows a **pipeline** (intake → routing → SLA modeling → enablement → approvals). If routing + enablement prep can run in parallel, log a **diamond** segment with merge gate.
- **Plan schema**: Save `.claude/plans/plan-<timestamp>.json` with objective, tasks, dependencies (data, tooling), context passing (scoring configs), error handling, and success metrics (SLA %, acceptance rate, conversion lift).
- **Tool hooks**: Reference `docs/gtm-essentials.md` stack—Serena for CRM/MAP script diffs, Context7 for platform docs, Sequential Thinking for review cadence, Playwright for QA of lead forms/sequences.
- **Guardrails**: Default retry limit = 2 for automation/build failures; escalation ladder = RevOps Director → Sales Manager → CRO.
- **Review**: Use `docs/usage-guide.md#orchestration-best-practices-puerto-parity` checklist before execution to confirm agents, dependencies, deliverables.

## Workflow
1. **Brief Intake** – confirm funnel stage definitions, qualification criteria, scoring thresholds.
2. **Routing Blueprint** – map lead ownership logic (account owner, round-robin, pod based) and required enrichment data.
3. **SLA Modeling** – calculate achievable response times vs capacity, flag risks, define escalation ladder.
4. **Enablement Requirements** – list assets, talk tracks, sequences, and dashboards each pod needs.
5. **Approval Packet** – consolidate documentation for RevOps + sales leadership sign-off.

## Outputs
- Handoff design doc (routing matrix, SLA tables, escalation tree).
- Data + tooling checklist (fields, integrations, automation flows) with owners.
- Enablement kit request list with due dates.
- Plan JSON entry stored/updated in `.claude/plans` for audit trail.

## Agent/Skill Invocations
- `revops-director` – leads routing/SLA design.
- `routing-logic` skill – enforces qualification + assignment best practices.
- `enablement-kit` skill – ensures supporting assets are ready.

## GTM Agents Safeguards
- **Fallback agents**: document substitutes (e.g., Sales Manager covering RevOps Director) when specialists unavailable.
- **Escalation triggers**: if SLA breaches or routing failures exceed guardrails twice in 48h, trigger escalation to Sales + Marketing leadership per GTM Agents rip-cord.
- **Plan maintenance**: update plan JSON whenever segments, routing logic, or enablement requirements change so audit trail mirrors GTM Agents standards.

---
