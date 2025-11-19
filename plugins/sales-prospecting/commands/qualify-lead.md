---
name: qualify-lead
description: Evaluate prospect fit and intent to determine next-best action for sales teams.
usage: /sales-prospecting:qualify-lead --company "Acme" --persona "VP Revenue" --signals intent.json
---

# Qualify Lead Command

Score leads against ICP, intent signals, and buying triggers to decide whether to route, recycle, or nurture.

## Command Syntax
```bash
/sales-prospecting:qualify-lead \
  --company "<name>" \
  --persona "<title>" \
  --firmographics firmo.json \
  --technographics tech.json \
  --signals intent.json \
  --threshold 75
```

### Parameters
- `--company`: Account name or domain.
- `--persona`: Primary buyer role under evaluation.
- `--firmographics`: JSON/CSV input of company attributes.
- `--technographics`: Technology stack details.
- `--signals`: Intent data (product usage, web visits, 3rd-party intent).
- `--threshold`: Minimum composite score to pass to sales (default 70).
- `--stage`: Lead stage (MQL, PQL, recycled) to influence scoring weights.

## Workflow
1. **Data Normalization** – clean and map firmographic, technographic, and behavior fields.
2. **Fit Scoring** – apply weighted ICP model (industry, size, geography, use case, tech stack compatibility).
3. **Intent Scoring** – incorporate behavioral data (content engagement, trials, intent providers, product telemetry).
4. **Timing Assessment** – evaluate trigger events (funding, hires, tech churn) plus buying cycle alignment.
5. **Recommendation Engine** – produce route/recycle/nurture guidance with rationale, next steps, and owner.

## Output Schema
```json
{
  "company": "Acme Corp",
  "fit_score": 82,
  "intent_score": 76,
  "composite_score": 79,
  "decision": "route-to-ae",
  "urgency": "high",
  "rationale": [
    "ICP match: SaaS, 200 employees, US",
    "High technographic overlap",
    "Recent product trial and pricing page visits"
  ],
  "next_steps": [
    "Assign to AE Sarah Lee",
    "Send enterprise case study",
    "Schedule discovery call within 48h"
  ]
}
```

## Best Practices
- Keep scoring models transparent so SDRs/RevOps can adjust weights.
- Blend qualitative notes (call transcripts) with quantitative data.
- Auto-sync outcomes to CRM and track model drift monthly.
- Use different thresholds for inbound vs outbound vs product-led leads.

---
