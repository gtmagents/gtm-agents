---
name: define-profiles
description: Produces audience profile schemas, data sources, and activation requirements for personalization programs.
usage: /personalization-engine:define-profiles --initiative "PLG Onboarding" --channels "web,in-app,email"
---

# Command: define-profiles

## Inputs
- **initiative** – program or campaign name anchoring the personalization effort.
- **channels** – comma-separated channels to activate (web, in-app, email, ads, sales).
- **metrics** – optional KPIs (activation rate, pipeline $, retention).
- **constraints** – optional compliance, consent, or tooling notes.
- **timeline** – optional delivery window.

### GTM Agents Pattern & Plan Checklist
> Mirrors GTM Agents orchestrator blueprint @puerto/plugins/orchestrator/README.md#112-325.

- **Pattern selection**: Profile definition typically runs **diamond** (objective intake ↔ attribute inventory in parallel, reconverging into activation/governance) or **pipeline** when sequential; document pattern choice in plan header.
- **Plan schema**: Save `.claude/plans/plan-<timestamp>.json` capturing initiative, data sources, dependency graph (data eng, legal, privacy), error handling, and success metrics (attribute coverage %, consent integrity, activation lift).
- **Tool hooks**: Reference `docs/gtm-essentials.md` stack—Serena for schema diffs, Context7 for privacy/compliance docs, Sequential Thinking for governance reviews, Playwright for consent/opt-in flow QA if needed.
- **Guardrails**: Default retry limit = 2 for data pulls or consent checks; escalation ladder = Personalization Architect → Data Privacy Lead → Exec sponsor.
- **Review**: Run `docs/usage-guide.md#orchestration-best-practices-puerto-parity` before finalizing to confirm dependencies + approvals.

## Workflow
1. **Objective Intake** – clarify business goals, target personas, lifecycle stages.
2. **Attribute Inventory** – list required fields, source systems, refresh cadence, and consent rules.
3. **Profile Definition** – outline segments, eligibility logic, scoring, decay windows.
4. **Activation Mapping** – document downstream systems, API/webhook needs, fallback states.
5. **Governance Plan** – assign owners, QA cadences, and change management checkpoints.

## Outputs
- Profile schema deck/table (attributes, types, source, SLA, privacy notes).
- Eligibility + suppression logic doc for each profile.
- Activation checklist linking profiles to channels and tooling.
- Plan JSON entry stored/updated in `.claude/plans` for audit trail.

## Agent/Skill Invocations
- `personalization-architect` – leads objectives + profile design.
- `customer-data-engineer` – validates data feasibility.
- `decision-trees` skill – ensures logic structures align with downstream rules.

## GTM Agents Safeguards
- **Fallback agents**: document substitutes (e.g., Customer Data Engineer covering Architect) when leads unavailable.
- **Escalation triggers**: escalate if consent/compliance blockers occur twice or attribute coverage misses SLA; log remediation in plan JSON.
- **Plan maintenance**: update plan JSON/change log when attributes, data sources, or governance cadences change.

---
