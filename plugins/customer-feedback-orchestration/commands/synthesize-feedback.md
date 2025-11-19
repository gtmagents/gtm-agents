---
name: synthesize-feedback
description: Consolidates quantitative and qualitative signals into prioritized themes with opportunity sizing.
usage: /customer-feedback-orchestration:synthesize-feedback --window 60d --personas "admins,execs" --detail workshop
---

# Command: synthesize-feedback

## Inputs
- **window** – analysis horizon (30d, 60d, quarter) pulling data from surveys, support, usage, community.
- **personas** – optional filter for personas or segments to highlight.
- **detail** – summary | workshop controls depth of deliverables.
- **include-voice** – true/false to embed verbatim quotes.
- **impact-lens** – arr | adoption | satisfaction to drive prioritization lens.

### GTM Agents Pattern & Plan Checklist
> Mirrors GTM Agents orchestrator blueprint @puerto/plugins/orchestrator/README.md#112-325.

- **Pattern selection**: Feedback synthesis typically runs **pipeline** (aggregation → tagging → impact modeling → opportunity framing → narrative). If tagging + modeling can run in parallel, record a **diamond** block with merge gate in the plan header.
- **Plan schema**: Save `.claude/plans/plan-<timestamp>.json` capturing window, data feeds, dependency graph (CS, product, research, analytics), error handling, and success metrics (theme confidence, coverage %, time-to-synthesize).
- **Tool hooks**: Reference `docs/gtm-essentials.md` stack—Serena for taxonomy updates, Context7 for historic studies, Sequential Thinking for workshop prep, Playwright for dashboard QA when embedding outputs.
- **Guardrails**: Default retry limit = 2 for data pulls/tagging jobs; escalation ladder = Research Lead → CX Leadership → Exec sponsor.
- **Review**: Run `docs/usage-guide.md#orchestration-best-practices-puerto-parity` before workshops to confirm dependencies + deliverables.

## Workflow
1. **Data Aggregation** – collect structured/unstructured feedback from connected systems.
2. **Tagging & Clustering** – apply taxonomy, detect emerging topics, score severity + frequency.
3. **Impact Modeling** – quantify ARR, usage, or sentiment impact with supporting metrics.
4. **Opportunity Framing** – craft problem statements, desired outcomes, and proposed motions.
5. **Narrative Packaging** – produce decks/notes for PM, CS, marketing, and exec consumption.

## Outputs
- Theme matrix with impact, personas, confidence, and owner recommendations.
- Quote bank + evidence appendix tied to each theme.
- Action backlog seeds for `route-insights` command.
- Plan JSON entry stored/updated in `.claude/plans` for audit trail.

## Agent/Skill Invocations
- `cs-analyst` – leads data prep + scoring.
- `research-lead` – ensures insights align with study goals.
- `insight-synthesis` skill – provides framing templates and storytelling patterns.
- `survey-design` skill – highlights methodology caveats.

## GTM Agents Safeguards
- **Fallback agents**: document substitutes (e.g., CS Analyst covering Research Lead) when leads unavailable.
- **Escalation triggers**: if data completeness or confidence metrics miss thresholds twice, escalate via GTM Agents rip-cord and log remediation in plan JSON.
- **Plan maintenance**: update plan JSON/change log when data sources, personas, or impact lenses change to preserve audit history.

---
