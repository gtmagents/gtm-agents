---
name: analyze-competitive-landscape
description: Produces competitive landscape brief with threat levels, differentiators, and recommended actions.
usage: /competitive-intelligence:analyze-competitive-landscape --scope enterprise-saas --audience exec --window 30d --format deck
---

# Command: analyze-competitive-landscape

## Inputs
- **scope** – product line, segment, or geo focus.
- **audience** – exec | product | sales | marketing.
- **window** – analysis timeframe (30d, 60d, quarter, custom).
- **format** – deck | memo | docset.
- **signals** – optional URLs/files to include (research, CRM stats, win/loss exports).

## Workflow
1. **Signal Aggregation** – pull intel from research feeds, CRM, sales notes, and market news.
2. **Threat Assessment** – evaluate competitor moves, assign severity/confidence, link to metrics.
3. **Differentiation Mapping** – highlight core strengths/weaknesses vs each rival.
4. **Action Planning** – recommend counter plays, investments, or messaging pivots per stakeholder.
5. **Executive Packaging** – format narrative, visuals, and action register for the requested format.

## Outputs
- Competitive brief (deck/memo) with threat levels, trends, and insights.
- Action register with owners, due dates, and success metrics.
- Appendix with referenced signals, quotes, and supporting data.

## Agent/Skill Invocations
- `market-insights-director` – leads synthesis + executive narrative.
- `battlecard-program-manager` – feeds differentiation + plays into the brief.
- `market-signal-tracker` skill – structures signals + metadata.
- `executive-briefing-kit` skill – enforces storytelling + action format.

---
