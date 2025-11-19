---
name: build-battlecard-suite
description: Creates updated battlecards, objection handling, and enablement assets for target competitors.
usage: /competitive-intelligence:build-battlecard-suite --competitors alpha,beta --audience sales,cs --format deck --refresh-cadence monthly
---

# Command: build-battlecard-suite

## Inputs
- **competitors** – comma-separated competitor list.
- **audience** – sales | cs | marketing | exec | product (multi-select via comma list).
- **format** – deck | docset | notion | pdf.
- **refresh-cadence** – monthly | quarterly | on-demand.
- **data-links** – optional references (win/loss notes, recordings, research PDFs).

## Workflow
1. **Intel Consolidation** – gather latest insights from CRM, call libraries, research hubs, and product notes.
2. **Narrative Refresh** – update positioning, traps, landmines, differentiation, and value proof.
3. **Play Development** – define talk tracks, objection handling, traps, and recommended assets.
4. **Packaging** – format deliverables per audience + format, including quick reference tables.
5. **Distribution & Feedback** – publish to enablement channels, capture usage + improvement requests.

## Outputs
- Battlecard pack per competitor (PDF/deck/Notion) with messaging + plays.
- Objection handling sheet + competitive talk track scripts.
- Update log + adoption plan with owners.

## Agent/Skill Invocations
- `battlecard-program-manager` – curates content + manages adoption plan.
- `market-insights-director` – validates differentiation + threat framing.
- `battlecard-library` skill – enforces battlecard structure + metadata.
- `executive-briefing-kit` skill – prepares exec-friendly highlights when audience includes leadership.

---
