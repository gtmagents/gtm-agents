---
name: segment-customers
description: Generates customer segmentation models, scoring logic, and activation briefs.
usage: /customer-analytics:segment-customers --goal "upsell" --inputs usage,firmographic --method hybrid --segments 5
---

# Command: segment-customers

## Inputs
- **goal** – business goal (upsell, retention, adoption, marketing efficiency).
- **inputs** – comma-separated data sources (usage, firmographic, revenue, support, survey).
- **method** – rules | clustering | hybrid.
- **segments** – target number of segments/personas to output.
- **activation** – optional channel focus (sales, cs, marketing, product).

## Workflow
1. **Data Profiling** – evaluate selected inputs, quality, and coverage.
2. **Segmentation Design** – run clustering/heuristics, score stability, and interpretability.
3. **Scoring Logic** – define rules/weights for RevOps/data teams to implement.
4. **Persona Packaging** – craft segment personas with value props, risks, and KPIs.
5. **Activation Plan** – map segments to GTM plays, reporting, and refresh cadence.

## Outputs
- Segmentation matrix (definition, criteria, size, key metrics).
- Scoring workbook/API spec with weights and thresholds.
- Activation brief aligning segments to plays/channels.

## Agent/Skill Invocations
- `segmentation-architect` – leads modeling + documentation.
- `retention-analyst` – supplies usage/retention signals.
- `customer-insights-partner` – injects qualitative proof.
- `segmentation-framework` skill – provides templates + guardrails.
- `activation-map` skill – links segments to GTM workflows.

---
