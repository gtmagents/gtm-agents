---
name: build-sequence
description: Generate personalized, multi-touch outbound sequences across email, phone, and social.
usage: /sales-prospecting:build-sequence --industry "SaaS" --persona "VP Sales" --length 5 --personalization high
---

# Build Sequence Command

Create channel-mixed outreach cadences tailored to a given persona, industry, and ICP stage.

## Command Syntax
```bash
/sales-prospecting:build-sequence \
  --industry "<segment>" \
  --persona "<role>" \
  --length <touches> \
  --personalization <low|medium|high> \
  --channels "email,linkedin,phone"
```

### Parameters
- `--industry`: Industry vertical for context and proof points.
- `--persona`: Buyer role or title.
- `--length`: Number of touches (default 5).
- `--personalization`: Depth of personalization (low/medium/high).
- `--channels`: Ordered list of channels to include.
- `--intent-level`: cold|warm|hot (affects tone and CTA).
- `--assets`: Optional resources (case studies, reports) to embed.

## Workflow
1. **Persona Calibration** – pull pain points, goals, language cues.
2. **Narrative Arc** – map touches to curiosity → value → proof → urgency → ask.
3. **Channel Assignment** – rotate channels per touch with rationale.
4. **Copy Drafting** – craft subject lines, body copy, social scripts, call guides.
5. **Instrumentation** – specify success metrics and A/B test ideas.

## Output
- Tabular sequence plan with send day, channel, message summary, CTA.
- Full copy deck per touch (email body, LI message, call opener, voicemail script).
- Personalization tokens (e.g., {recent_funding}, {tech_stack}).
- Test backlog (subject line variants, CTA swaps, timing experiments).

## Best Practices
- Front-load personalization; escalate urgency over time.
- Keep mobile-friendly line lengths and single CTA.
- Align send windows with persona working hours and time zones.
- Log replies and auto-stop sequences on positive intent.

---
