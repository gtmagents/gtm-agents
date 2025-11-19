---
name: synthesize-voc-insights
description: Turn multi-channel VoC signals into quantified insights, impact sizing, and exec-ready narratives.
usage: /voice-of-customer:synthesize-voc-insights --window quarter --drivers onboarding,ai --audience exec,product --format deck
---

# Command: synthesize-voc-insights

## Inputs
- **window** – time range to cover (month, quarter, half, custom dates).
- **drivers** – comma-separated themes or drivers to emphasize (pricing, onboarding, integrations, reliability, AI, services).
- **audience** – exec | product | cs | marketing | sales | board (comma list allowed).
- **format** – deck | memo | workspace | dashboard.
- **evidence-links** – optional list of folders, dashboards, or note docs to ingest.

## Workflow
1. **Signal Harvest** – pull all tagged feedback, interviews, surveys, support logs, community posts within the window.
2. **Taxonomy Alignment** – ensure tags match latest taxonomy; resolve duplicates and anomalies.
3. **Quantification & Modeling** – attach ARR/churn/adoption metrics to each driver and calculate impact range.
4. **Story Synthesis** – craft storyline with quotes, data viz, confidence levels, and recommendations per audience.
5. **Packaging & Distribution** – format into requested output, add action register, and log follow-ups.

## Outputs
- Insight brief (deck/memo) with top drivers, opportunity sizing, and confidence.
- Supporting appendix with quotes, data tables, and method notes.
- Action register with owners, due dates, and measurement approach.

## Agent/Skill Invocations
- `customer-insights-lab-analyst` – leads modeling and storyline.
- `voc-program-director` – approves narrative + ensures governance compliance.
- `signal-correlation-workbench` skill – links telemetry to qualitative data.
- `executive-briefing-kit` skill (from competitive-intelligence) automatically included when exec/board audience requested.

---
