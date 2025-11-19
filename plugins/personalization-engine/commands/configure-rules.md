---
name: configure-rules
description: Deploys decision logic, content variants, and delivery rules across personalization channels.
usage: /personalization-engine:configure-rules --initiative "PLG Onboarding" --environment staging --channels "web,in-app"
---

# Command: configure-rules

## Inputs
- **initiative** – reference to the personalization effort from `define-profiles`.
- **environment** – staging | production to govern deployment steps.
- **channels** – comma-separated list of activation surfaces.
- **change_type** – net-new, update, rollback.
- **approvers** – optional stakeholders for governance sign-off.

### GTM Agents Pattern & Plan Checklist
> Mirrors GTM Agents orchestrator blueprint @puerto/plugins/orchestrator/README.md#112-325.

- **Pattern selection**: Rule configuration generally runs **pipeline** (pre-flight → decision build → variant mapping → QA → deployment). If decision build + variant prep happen in parallel, note a **diamond** block with merge gate in the plan header.
- **Plan schema**: Save `.claude/plans/plan-<timestamp>.json` capturing initiative, environments, dependency graph (data eng, creative, QA, governance), error handling, and success metrics (latency, personalization lift, incident count).
- **Tool hooks**: Reference `docs/gtm-essentials.md` stack—Serena for rule diffing, Context7 for platform SOPs, Sequential Thinking for go/no-go reviews, Playwright for simulation/QA evidence capture.
- **Guardrails**: Default retry limit = 2 for deployment/QA failures; escalation ladder = Personalization Architect → Data Privacy Lead → Exec sponsor.
- **Review**: Run `docs/usage-guide.md#orchestration-best-practices-puerto-parity` before deployment to confirm dependencies + approvals.

## Workflow
1. **Pre-flight Review** – validate profiles, data freshness, consent status, and experiment dependencies.
2. **Decision Flow Build** – configure rules, weights, or model endpoints in MAP/CDP/product tooling.
3. **Variant Mapping** – link each rule outcome to content assets, CTAs, and fallback experiences.
4. **QA & Simulation** – run synthetic traffic through decision trees, capture screenshots/logs.
5. **Deployment & Logging** – push changes via API/CLI, note version metadata, set up monitoring hooks.

## Outputs
- Deployment runbook with rule IDs, version numbers, and rollback plan.
- QA evidence (simulation results, screenshots, payload logs).
- Governance log including approvers, timestamps, and linked experiments.
- Plan JSON entry stored/updated in `.claude/plans` for audit trail.

## Agent/Skill Invocations
- `customer-data-engineer` – ensures data pipelines and environments are ready.
- `personalization-architect` – verifies experience logic + content mapping.
- `content-variants` skill – tracks asset requirements + approvals.
- `governance` skill – enforces change controls and compliance steps.

## GTM Agents Safeguards
- **Fallback agents**: document substitutes (e.g., governance lead covering architect) when owners unavailable.
- **Escalation triggers**: if QA fails twice, latency spikes, or privacy gate blocks deployment, trigger GTM Agents rip-cord and log remediation in plan JSON.
- **Plan maintenance**: update plan JSON/change log when rule sets, environments, or deployment windows change so reviewers can trace history.

---
