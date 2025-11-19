---
name: run-market-landscape-study
description: End-to-end secondary and primary research sprint covering market size, trends, and competitor mapping.
usage: /market-research:run-market-landscape-study --scope "AI Sales Tech" --regions na,emea --horizon 3y --format deck
---

# Command: run-market-landscape-study

## Inputs
- **scope** – product category, segment, or thesis to analyze.
- **regions** – comma-separated regions or markets.
- **horizon** – timeframe for projections (1y, 3y, 5y).
- **format** – deck | memo | dashboard.
- **sources** – optional URLs, analyst reports, internal docs to ingest.

## Workflow
1. **Scoping** – confirm hypotheses, KPIs, and stakeholder decisions.
2. **Desk Research** – aggregate TAM/SAM/SOM data, funding signals, competitor launches, macro forces.
3. **Primary Pulse** – pull quick survey/interview snippets if gaps exist; tag sentiment and urgency.
4. **Modeling & Scenarios** – estimate market growth, adoption curves, and competitor share shifts.
5. **Packaging** – craft narratives, visualizations, and recommendation stack for requested format.

## Outputs
- Market landscape deck/memo with size, trends, competitor matrix.
- Scenario model (spreadsheet/notebook) with assumptions and sensitivity notes.
- Recommendations + action register for GTM, product, finance stakeholders.

## Agent/Skill Invocations
- `insights-research-director` – overall orchestration and exec packaging.
- `quant-insights-architect` – builds models and validates data sources.
- `research-brief-blueprint` skill – keeps scope/methodology aligned.
- `insights-repository-kit` skill – archives findings + sources.
- `market-scenario-modeler` skill – stress-tests assumptions and packages models.

---
