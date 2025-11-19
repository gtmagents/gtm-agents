---
name: run-call-review
description: Facilitates manager-led call reviews with scorecards, clips, and follow-up assignments.
usage: /sales-calls:run-call-review --team "Enterprise AEs" --window week --focus negotiation --participants 5
---

# Command: run-call-review

## Inputs
- **team** – group or cohort to review (team, pod, region).
- **window** – time horizon for call selection (week, 2w, month).
- **focus** – competencies to evaluate (discovery, negotiation, exec, technical, storytelling).
- **participants** – number of calls/reps to highlight.
- **format** – live | async to choose facilitation style.

## Workflow
1. **Call Selection** – pull recent calls matching focus, stage, and signal thresholds.
2. **Scorecard Prep** – auto-fill rubric sections, metrics, and suggested clips.
3. **Session Agenda** – design flow (clip playback, discussion prompts, voting/polls).
4. **Action Logging** – capture feedback, commitments, and assignments per rep.
5. **Follow-up Package** – send recap with recordings, notes, and drills.

## Outputs
- Call review deck/agenda with clip timestamps.
- Scorecard PDFs/links for each participant.
- Recap + assignment tracker for managers and reps.

## Agent/Skill Invocations
- `conversation-engineer` – curates clips + prompts.
- `deal-analyst` – surfaces insights + metrics.
- `call-strategist` – aligns learnings to upcoming calls.
- `call-review-kit` skill – provides agenda + worksheet templates.
- `reinforcement-drills` skill – attaches follow-up assignments.

---
