# Segmentation Matrix

## Tier Definitions
| Tier | Description | Criteria | Engagement Strategy |
| :--- | :--- | :--- | :--- |
| **VIP** | High-value accounts/contacts. | - ARR > $50k<br>- C-Level title<br>- High intent score | - 1:1 Personalization<br>- Direct rep outreach<br>- Exclusive invites |
| **Core** | Standard target audience. | - ICP Match<br>- Director/Manager title<br>- Active in last 30 days | - Segmented nurture<br>- Role-based content<br>- Weekly cadence |
| **Dormant** | Previously engaged, now quiet. | - No activity > 90 days<br>- Valid email | - Re-engagement campaign<br>- "Break up" email<br>- Low frequency (Monthly) |
| **Suppressed** | Do not contact. | - Unsubscribed<br>- Hard Bounce<br>- Competitor domain | - Exclude from all sends |

## Logic Examples (JSON)
### VIP Segment
```json
{
  "AND": [
    {"field": "annual_revenue", "operator": "gt", "value": 50000},
    {"field": "title", "operator": "contains", "value": ["C-Level", "VP"]},
    {"field": "intent_score", "operator": "gt", "value": 80}
  ]
}
```

### Re-engagement Candidate
```json
{
  "AND": [
    {"field": "last_activity_date", "operator": "lt", "value": "now-90d"},
    {"field": "email_status", "operator": "eq", "value": "valid"},
    {"NOT": [
      {"field": "unsubscribed", "operator": "eq", "value": true}
    ]}
  ]
}
```
