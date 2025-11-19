---
name: experiment-design-kit
description: Toolkit for structuring hypotheses, variants, guardrails, and measurement
  plans.
---

# Experiment Design Kit Skill

## When to Use
- Translating raw ideas into testable hypotheses with clear success metrics.
- Ensuring experiment briefs include guardrails, instrumentation, and rollout details.
- Coaching pods on best practices for multi-variant or multi-surface tests.

## Framework
1. **Problem Framing** – define user problem, business impact, and north-star metric.
2. **Hypothesis Structure** – "If we do X for Y persona, we expect Z change" with assumptions.
3. **Measurement Plan** – primary metric, guardrails, min detectable effect, power calc.
4. **Variant Strategy** – control definition, variant catalog, targeting, and exclusion rules.
5. **Operational Plan** – owners, timeline, dependencies, QA/rollback steps.

## Templates
- Experiment brief (context, hypothesis, design, metrics, launch checklist).
- Guardrail register with thresholds + alerting rules.
- Variant matrix for surfaces, messaging, and states.
- **GTM Agents Growth Backlog Board** – capture idea → sizing → prioritization scoring (ICE/RICE) @puerto/README.md#183-212.
- **Weekly Experiment Packet** – includes KPI guardrails, qualitative notes, and next bets for Marketing Director + Sales Director.
- **Rollback Playbook** – pre-built checklist tied to lifecycle-mapping rip-cord procedures.

## Tips
- Pressure-test hypotheses with counter-metrics to avoid local optima.
- Document data constraints early to avoid rework during build.
- Pair with `guardrail-scorecard` to ensure sign-off before launch.
- Apply GTM Agents cadence: Monday backlog groom, Wednesday build review, Friday learnings sync.
- Require KPI guardrails per stage (activation, engagement, monetization) before authorizing build.
- If a test risks Sales velocity, include Sales Director in approval routing per GTM Agents governance.

## GTM Agents Experiment Operating Model
1. **Backlog Intake** – ideas flow from GTM pods; Growth Marketer tags theme, objective, expected impact.
2. **Prioritization** – score with RICE + qualitative "strategic fit" modifier; surface top 3 bets weekly.
3. **Design & Instrumentation** – reference Serena/Context7 to patch code + confirm documentation.
4. **Launch & Monitor** – use guardrail-scorecard to watch leading indicators (churn, complaints, latency).
5. **Learning Loop** – run Sequential Thinking retro; document hypothesis, result, decision, follow-up in backlog card.

## KPI Guardrails (GTM Agents Reference)
- Activation rate change must stay within ±3% of baseline for Tier-1 segments.
- Revenue per visitor cannot drop more than 2% for more than 48h.
- Support tickets tied to experiment variant must remain <5% of total volume.

## Weekly Experiment Packet Outline
```
Week Ending: <Date>

1. Portfolio Snapshot – tests live, status, KPI trend (guardrail vs actual)
2. Key Wins – hypothesis, uplift, next action (ship, iterate, expand)
3. Guardrail Alerts – what tripped, mitigation taken (rollback? scope adjust?)
4. Pipeline Impact – SQLs, ARR influenced, notable customer anecdotes
5. Upcoming Launches – dependencies, owners, open questions
```

Share packet with Growth, Marketing Director, Sales Director, and RevOps to mirror GTM Agents's cross-functional communication rhythm.

---
