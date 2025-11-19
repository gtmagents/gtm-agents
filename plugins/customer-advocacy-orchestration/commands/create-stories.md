---
name: create-stories
description: Produces advocacy content briefs, interview scripts, and distribution plans.
usage: /customer-advocacy-orchestration:create-stories --persona "CIO" --format "case-study" --count 3
---

# Command: create-stories

## Inputs
- **persona** – primary audience for the story.
- **format** – case-study | video | webinar | blog | social.
- **count** – number of stories or assets to produce.
- **customers** – optional list of advocate IDs to focus on.
- **channels** – optional distribution channels.

## Workflow
1. **Brief Assembly** – fetch advocate insights, product data, KPIs, and compliance notes.
2. **Narrative Framework** – outline hero, challenge, solution, outcomes, and supporting proof.
3. **Interview Kit** – generate question sets, scheduling plan, and consent requirements.
4. **Production Plan** – define tasks for writing, design, video, localization, and approvals.
5. **Distribution Checklist** – map assets to enablement hubs, campaigns, and launch timelines.

## Outputs
- Story brief + outline with key messages and proof.
- Interview script and logistics checklist.
- Production tracker with owners, status, and due dates.
- Distribution plan tied to marketing channels and KPIs.

## Agent/Skill Invocations
- `story-producer` – leads interview + production tasks.
- `storytelling` skill – provides narrative framework and templates.
- `reference-manager` – coordinates advocate communications.

---
