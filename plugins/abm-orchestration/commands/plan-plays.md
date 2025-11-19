---
name: plan-plays
description: Produces an ABM playbook roadmap with offers, channels, and timelines aligned to tiers.
usage: /abm-orchestration:plan-plays --tiering "T1:10,T2:40" --window 6w --objectives pipeline
---

# Command: plan-plays

## Inputs
- **tiering** – map of tier counts (e.g., `T1:10,T2:40`).
- **window** – program duration (e.g., 6w, quarter).
- **objectives** – pipeline, expansion, strategic meetings, adoption.
- **channels** – optional list (ads, email, direct mail, exec events, social).
- **offers** – optional predefined offers to include.

### GTM Agents Pattern & Plan Checklist
> Derived from GTM Agents orchestrator model @puerto/plugins/orchestrator/README.md#112-325.

- **Pattern selection**: Start with a **diamond** pattern (strategy intake → parallel pod planning → consolidation) and switch to **pipeline** when play development must stay sequential. Record the chosen pattern in the plan header.
- **Plan schema**: Every run saves `.claude/plans/plan-<timestamp>.json` including objective, stages, parallel groups, agent assignments, context handoffs, error handling, and success criteria.
- **Tool hooks**: Reference `docs/gtm-essentials.md` tools explicitly (Serena for CRM/MAP patches, Context7 for platform docs, Sequential Thinking for retros, Playwright for QA on assets/landing pages).
- **Guardrails**: Define retry strategy (default 2 attempts) and escalation path (ABM Strategist → Sales Director) for any failed stage.
- **Review**: Before execution, run the checklist in `docs/usage-guide.md#orchestration-best-practices-puerto-parity` to confirm agents, dependencies, and deliverables.

## Workflow
1. **Strategy Alignment** – confirm goals, budget, team capacity, channel constraints.
2. **Play Library Selection** – choose plays per tier (executive experience, custom content, direct mail, workshops, ads).
3. **Timeline & Cadence** – schedule waves of outreach, follow-up, and standups.
4. **Asset & Owner Mapping** – identify required content, personalization, approvals, stakeholders.
5. **Measurement Plan** – define KPIs per play (engagement, meetings, pipeline) and reporting cadence.

## Outputs
- Playbook table (tier, play, channel, owner, CTA, assets, SLAs).
- Calendar/timeline highlighting waves, reviews, retros.
- Risk + dependency log (asset gaps, approval needs, data requirements).
- Plan JSON stored in `.claude/plans` with version history (update if owners/scope change).

## Agent/Skill Invocations
- `abm-strategist` – leads play selection + governance.
- `account-planner` – maps plays to specific accounts/personas.
- `personalization` skill – ensures messaging + assets are tailored.

## GTM Agents Safeguards
- **Fallback agents**: document substitutions (e.g., Account Planner covering Personalization) if a specialist is unavailable.
- **Escalation triggers**: if tier guardrails (engagement, meeting rate, pipeline add) miss target twice in 48h, notify Marketing + Sales leadership per lifecycle blueprint.
- **Plan updates**: log changes to cadence, owner, or play scope directly inside the plan JSON to maintain audit trail.

---
