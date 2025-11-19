---
name: analyze-call
description: Breaks down a call recording/transcript into metrics, highlights, risks, and recommended actions.
usage: /sales-calls:analyze-call --recording "s3://calls/demo-456" --focus "exec alignment" --compare "top-performer"
---

# Command: analyze-call

## Inputs
- **recording** – required link or ID for the call.
- **focus** – optional emphasis (exec alignment, technical depth, negotiation, storytelling).
- **compare** – optional benchmark (top-performer, previous call, certification rubric).
- **clips** – true/false to generate highlight reels.
- **include-meddic** – true/false toggle to evaluate MEDDIC/BANT coverage.

## Workflow
1. **Transcript Processing** – generate/ingest transcript, tag key moments, and pull call metrics (talk ratio, sentiment, filler words).
2. **Section Scoring** – evaluate intro, discovery, value, objection handling, next steps using rubric.
3. **Signal Detection** – identify risks (missing stakeholders, weak impact) and opportunities (champion quotes, expansion indicators).
4. **Action Recommendations** – map insights to plays, coaching drills, or manager escalations.
5. **Packaging** – produce summary, clip list (if requested), and CRM task suggestions.

## Outputs
- Call analysis brief with scores, notable quotes, and next steps.
- Optional highlight reel references.
- MEDDIC/BANT coverage grid when enabled.

## Agent/Skill Invocations
- `deal-analyst` – interprets signals + coverage.
- `conversation-engineer` – critiques talk tracks and delivery.
- `call-strategist` – recommends storyline adjustments.
- `call-analysis-framework` skill – scoring rubric + output structure.
- `meddic-checklist` skill – ensures qualification completeness.

---
