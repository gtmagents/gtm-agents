---
name: review-call
description: Generates annotated call reviews with scores, coaching moments, and follow-up actions.
usage: /sales-coaching:review-call --recording "s3://calls/deal-123" --focus "negotiation" --audience "manager,rep"
---

# Command: review-call

## Inputs
- **recording** – link or ID for the call/video to analyze.
- **focus** – optional tags (discovery, negotiation, demo, pricing, exec alignment).
- **audience** – recipients for the summary (rep, manager, enablement).
- **compare-to** – optional benchmark (top-performer, last week, certification rubric).
- **clips** – true/false toggle to auto-create highlight clips.

## Workflow
1. **Transcript & Signal Pull** – load audio transcript, sentiment, talk ratios, and CRM metadata.
2. **Section Scoring** – evaluate intro, discovery, value storyline, objection handling, closing motions.
3. **Coach Moments** – flag standout moments and improvement areas with suggested phrasing.
4. **Clip Production** – (optional) create short clips for enablement + peer share.
5. **Action Plan** – recommend drills, assets, or follow-up assignments.

## Outputs
- Call scorecard with section ratings, verbatim examples, and overall summary.
- Highlight reel links if clips requested.
- Coaching action list aligned to the active coaching plan.

## Agent/Skill Invocations
- `call-analyst` – performs tagging/scoring.
- `performance-coach` – translates findings into actions.
- `enablement-partner` – routes clips/assets into LMS.
- `call-highlights` skill – manages clip templates + storage.
- `coaching-framework` skill – ties insights to competency rubric.

---
