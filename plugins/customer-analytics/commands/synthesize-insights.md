---
name: synthesize-insights
description: Consolidates qualitative + quantitative customer signals into executive-ready briefs.
usage: /customer-analytics:synthesize-insights --theme "onboarding" --sources "interviews,surveys,community" --audience "product,marketing"
---

# Command: synthesize-insights

## Inputs
- **theme** – focus topic (onboarding, adoption, support, expansion, churn).
- **sources** – comma-separated inputs (interviews, surveys, community, NPS, usage).
- **audience** – target stakeholders (product, marketing, sales, cs, exec).
- **urgency** – normal | rush to tailor scope.
- **format** – deck | memo | digest.

## Workflow
1. **Signal Collection** – gather requested data + qualitative notes; dedupe/resample as needed.
2. **Coding & Tagging** – cluster observations into themes, sentiments, and impact level.
3. **Quantification** – add metrics per theme (occurrence, ARR impacted, retention delta).
4. **Recommendation Layer** – map insights to actions, owners, and next experiment ideas.
5. **Packaging & Distribution** – produce deck/memo/digest plus repository updates.

## Outputs
- Insight brief with themes, quotes, metrics, and action items.
- Repository updates with tags + links.
- Follow-up tracker for product/GTM owners.

## Agent/Skill Invocations
- `customer-insights-partner` – leads research synthesis.
- `segmentation-architect` – contextualizes insights by segment.
- `retention-analyst` – quantifies impact on retention metrics.
- `insight-repository` skill – maintains tagging + historical logs.
- `activation-map` skill – links insights to GTM actions.

---
