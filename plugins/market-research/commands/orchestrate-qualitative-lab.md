---
name: orchestrate-qualitative-lab
description: Designs and manages qualitative research labs (interviews, focus groups, diary studies) end-to-end.
usage: /market-research:orchestrate-qualitative-lab --personas buyer,admin --sessions 12 --channels interview,focus-group --deliverable highlight-reel
---

# Command: orchestrate-qualitative-lab

## Inputs
- **personas** – comma-separated persona or segment list with optional tier tags.
- **sessions** – number of sessions/interviews/focus groups to run.
- **channels** – interview | focus-group | diary-study | community | hybrid.
- **deliverable** – highlight-reel | memo | board-pack | research-notebook.
- **incentive** – optional gift card or perk description to automate fulfillment guidance.

## Workflow
1. **Recruiting Plan** – build quota matrix, screeners, and outreach/incentive sequences.
2. **Instrument Design** – generate discussion guide, stimulus, and exercise facilitation tips.
3. **Scheduling & Logistics** – manage invites, reminders, recordings, consent, and backups.
4. **Moderation & QA** – support moderators with live notes, probing cues, and debrief capture.
5. **Synthesis & Packaging** – assemble highlight reels, quote libraries, and theme boards for the requested deliverable.

## Outputs
- Recruiting tracker with status, contact info, and incentive progress.
- Discussion guide packet + moderator coaching notes.
- Highlight reel / memo with themes, supporting quotes, and next-step recommendations.

## Agent/Skill Invocations
- `qualitative-field-lead` – owns recruiting, moderation, and synthesis.
- `insights-research-director` – ensures alignment with business goals.
- `participant-operations-hub` skill – tracks quotas, consent, incentives.
- `insights-repository-kit` skill – archives recordings, notes, and transcripts.

---
