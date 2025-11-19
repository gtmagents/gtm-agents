---
name: post-launch-retro
description: Produces a retrospective plan summarizing launch performance, learnings, and follow-up actions.
usage: /product-launch-orchestration:post-launch-retro --product "AI Copilot" --window 30d --audience "exec"
---

# Command: post-launch-retro

## Inputs
- **product** – launch identifier.
- **window** – timeframe to evaluate (7d, 30d, quarter).
- **audience** – intended audience (exec, GTM, product, board).
- **kpis** – optional list of KPIs to spotlight.
- **feedback_sources** – optional sources (CS, community, partners, analysts).

## Workflow
1. **Data Snapshot** – gather product metrics, pipeline, revenue, adoption, support volume, sentiment.
2. **Workstream Review** – collect inputs from each owner (what worked, blockers, improvements).
3. **Customer/Market Feedback** – summarize quotes, reviews, analyst reactions, competitor moves.
4. **Action Plan** – prioritize follow-up work (bugs, roadmap updates, enablement refresh, marketing plays).
5. **Retro Meeting Facilitation** – propose agenda, facilitation plan, decision/owner logging.

## Outputs
- Retro deck/brief (objectives, KPIs, highlights, lowlights, actions).
- Consolidated feedback log + sentiment analysis.
- Action register with owners, due dates, and impact.

## Agent/Skill Invocations
- `launch-director` – runs retro and maintains decision/action logs.
- `enablement-captain` – contributes field feedback + follow-up training.
- `risk-playbooks` skill – ensures lessons learned feed future mitigation plans.

---
