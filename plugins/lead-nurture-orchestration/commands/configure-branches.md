---
name: configure-branches
description: Generates implementation instructions for nurture branching logic, personalization rules, and automations.
usage: /lead-nurture-orchestration:configure-branches --journey "MM Onboarding" --platform marketo --qa true
---

# Command: configure-branches

## Inputs
- **journey** – reference name or existing blueprint ID.
- **platform** – MAP/CRM platform (Marketo, HubSpot, Braze, Iterable, Pardot, Customer.io, SF Automations).
- **qa** – include QA + evidence steps (default true).
- **assets** – optional asset list to wire.
- **webhooks** – optional external integrations to include.

### GTM Agents Pattern & Plan Checklist
> Lifted from GTM Agents orchestrator practices @puerto/plugins/orchestrator/README.md#112-325.

- **Pattern selection**: Most branching config is a **pipeline** continuation of design-nurture. If QA + personalization can run parallel, explicitly log a **diamond** segment and define merge points.
- **Plan schema**: Update `.claude/plans/plan-<timestamp>.json` (or create if standalone) with branch IDs, step references, tokens, webhook payloads, QA scenarios, and error handling. Note dependencies (assets, webhooks) and success criteria (activation %, latency).
- **Tool hooks**: Use `docs/gtm-essentials.md` stack—Serena for MAP diffs, Context7 for platform docs, Sequential Thinking for post-flight retro, Playwright for landing/app QA.
- **Guardrails**: Default retry limit = 2 per failed automation. Escalate Marketing Ops Partner → Nurture Architect → RevOps if QA evidence fails or compliance issues appear.
- **Review**: Run `docs/usage-guide.md#orchestration-best-practices-puerto-parity` before publishing to ensure agents, dependencies, and deliverables are confirmed.

## Workflow
1. **Blueprint Sync** – pull journey diagram, triggers, suppression, personalization tokens.
2. **Branch Mapping** – translate logic into platform-specific steps (smart lists, decision splits, wait steps, webhook calls).
3. **Personalization Wiring** – define tokens, dynamic content blocks, conditional logic.
4. **QA & Evidence** – build test plan (seed profiles, edge cases, fallback paths) with screenshots/logs.
5. **Documentation** – produce build guide, change log, rollback plan.

## Outputs
- Implementation checklist with step-by-step instructions.
- QA/evidence matrix (test profile, scenario, expected result, status).
- Change log template + rollback notes.
- Plan JSON entry stored/updated in `.claude/plans` for traceability.

## Agent/Skill Invocations
- `marketing-ops-partner` – executes platform build.
- `personalization-logic` skill – ensures conditional content is accurate.
- `nurture-testing` skill – enforces QA rigor.

## GTM Agents Safeguards
- **Fallback agents**: document substitutes (e.g., Marketing Ops Partner covering testing) if specialists unavailable.
- **Escalation triggers**: if unsubscribe/spam complaints or latency guardrails breach twice in 48h, trigger lifecycle rip-cord and notify Marketing + Sales leadership.
- **Plan maintenance**: each branching change requires updating plan JSON + change log; reference in status packets to keep audit trail aligned with GTM Agents standards.

---
