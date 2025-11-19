# Use Case: Weekly Pipeline Health Check

## Overview

**Problem:** You need to review pipeline health but manually analyzing deals, stages, and risks takes hours every week.

**Solution:** Use the `sales-pipeline` plugin to automatically audit your pipeline and identify risks in under 10 minutes.

**Time Saved:** ~3 hours per week (from 4 hours to 1 hour)

**ROI:** At $100/hour, that's $300 saved per week or $15,600 per year

---

## Who This Is For

- Sales Managers
- Revenue Operations
- VP of Sales
- Account Executives
- Sales Directors

---

## What You'll Get

✅ Pipeline health score (0-100)  
✅ Deal risk analysis by stage  
✅ Stalled deal identification  
✅ Coverage ratio calculations  
✅ Velocity metrics  
✅ Recommended actions  
✅ Forecast accuracy assessment

---

## Prerequisites

- [ ] Claude Code installed
- [ ] GTM Agents marketplace added
- [ ] `sales-pipeline` plugin installed
- [ ] Access to your CRM data (Salesforce, HubSpot, etc.)

---

## Step-by-Step Instructions

### Step 1: Export Your Pipeline Data (2 minutes)

Export from your CRM with these fields:
- Deal name
- Stage
- Amount
- Close date
- Last activity date
- Owner
- Created date
- Probability

**Salesforce:** Reports → Create Report → Opportunities  
**HubSpot:** Deals → Export → All deals

Save as CSV file.

### Step 2: Run Pipeline Audit (3 minutes)

1. Open Claude Code
2. Run:
   ```
   /sales-pipeline:audit-pipeline
   ```
3. Upload your CSV or paste the data
4. Specify your sales cycle length (e.g., "90 days")

### Step 3: Review Health Metrics (5 minutes)

The plugin analyzes and provides:

**Overall Health Score:**
```
Pipeline Health: 72/100

✅ Strong Areas:
- Good stage distribution
- Healthy deal velocity in early stages
- Adequate pipeline coverage (3.2x quota)

⚠️ Areas of Concern:
- 15 deals stalled >30 days
- Low conversion rate in demo stage (18% vs 35% target)
- 8 deals at risk of slipping this quarter
```

**Stage Analysis:**
```
Discovery: 45 deals, $2.3M
- Healthy velocity (avg 12 days)
- Good qualification rate

Demo: 22 deals, $1.8M
⚠️ Conversion issue: 18% (target: 35%)
- 8 deals stalled >14 days
- Recommend: Re-engage with value proposition

Proposal: 12 deals, $980K
✅ Strong stage
- Good velocity (avg 8 days)
- High win rate (62%)

Negotiation: 6 deals, $540K
⚠️ 3 deals at risk
- Legal review taking >21 days
- Recommend: Expedite legal process
```

**At-Risk Deals:**
```
High Risk (Action Required):
1. Acme Corp - $120K - Stalled 45 days in Demo
   → No activity since 10/15
   → Champion left company
   → Action: Find new champion or disqualify

2. TechStart Inc - $85K - Close date passed
   → Slipped 2 quarters
   → Budget concerns
   → Action: Requalify or move to nurture

Medium Risk (Monitor):
3. Global Systems - $200K - Slow legal review
   → In negotiation 28 days
   → Legal taking longer than usual
   → Action: Executive alignment call
```

### Step 4: Take Action (Ongoing)

Based on the audit, take these actions:

**Immediate (This Week):**
- [ ] Re-engage stalled deals
- [ ] Disqualify dead deals
- [ ] Escalate at-risk deals
- [ ] Coach reps on low-converting stages

**Short-term (This Month):**
- [ ] Improve demo-to-proposal conversion
- [ ] Streamline legal review process
- [ ] Add more top-of-funnel deals
- [ ] Update forecasts

---

## Key Metrics Explained

### Pipeline Coverage Ratio
**Formula:** Total Pipeline Value ÷ Quota  
**Target:** 3-5x for most B2B sales  
**Example:** $3M pipeline ÷ $1M quota = 3x coverage

### Deal Velocity
**Formula:** Average days in each stage  
**Target:** Varies by stage and sales cycle  
**Example:** Discovery: 10-15 days, Demo: 7-10 days

### Conversion Rates
**Formula:** Deals moved to next stage ÷ Total deals in stage  
**Target:** Varies by stage  
**Example:** Demo → Proposal: 30-40%

### Stalled Deals
**Definition:** No activity in >14 days (or your threshold)  
**Action:** Re-engage or disqualify

---

## Pipeline Health Checklist

### Weekly Review
- [ ] Overall health score >70
- [ ] No deals stalled >30 days
- [ ] Pipeline coverage >3x quota
- [ ] Stage conversion rates on target
- [ ] At-risk deals have action plans

### Monthly Review
- [ ] Velocity trends improving
- [ ] Win rates by stage stable or improving
- [ ] Forecast accuracy >85%
- [ ] Rep performance consistent
- [ ] Pipeline generation on track

### Quarterly Review
- [ ] Sales cycle length decreasing
- [ ] Average deal size increasing
- [ ] Win rate improving
- [ ] Pipeline quality improving
- [ ] Forecast accuracy >90%

---

## Common Issues & Solutions

### Issue: Low Pipeline Coverage (<3x)

**Symptoms:**
- Not enough deals to hit quota
- Reps scrambling at end of quarter
- Inconsistent results

**Solutions:**
1. Increase prospecting activity
2. Improve lead quality
3. Expand target market
4. Add more reps

**Command:**
```
/sales-prospecting:generate-leads "Generate 200 leads matching our ICP"
```

### Issue: Deals Stalling in Demo Stage

**Symptoms:**
- Low demo-to-proposal conversion
- Deals sitting in demo >14 days
- Reps can't get next meeting

**Solutions:**
1. Improve demo quality
2. Better discovery questions
3. Stronger value proposition
4. Multi-threading (engage multiple stakeholders)

**Command:**
```
/sales-enablement:build-playbook "Demo best practices"
```

### Issue: Long Sales Cycle

**Symptoms:**
- Deals taking >90 days (or your target)
- Slow movement through stages
- Low velocity

**Solutions:**
1. Better qualification (BANT/MEDDIC)
2. Executive sponsorship earlier
3. Streamline approval processes
4. Create urgency

**Command:**
```
/sales-calls:prepare-call "Executive alignment call for [deal name]"
```

### Issue: Inaccurate Forecasts

**Symptoms:**
- Forecast vs actual >15% variance
- Deals slipping unexpectedly
- Overly optimistic reps

**Solutions:**
1. Stricter qualification criteria
2. Better deal inspection
3. Regular pipeline reviews
4. Data-driven forecasting

**Command:**
```
/sales-pipeline:forecast-coverage "Calculate forecast for Q1"
```

---

## Advanced Analysis

### Cohort Analysis

Track deals by cohort (month created):

```
October Cohort (45 deals):
- 12 closed-won (27%)
- 8 closed-lost (18%)
- 25 still open (55%)
- Avg time to close: 67 days

November Cohort (52 deals):
- 8 closed-won (15%)
- 5 closed-lost (10%)
- 39 still open (75%)
- Avg time to close: 45 days (in progress)
```

### Rep Performance

Compare reps:

```
Top Performer (Sarah):
- Pipeline: $1.2M (4x quota)
- Win rate: 42%
- Avg deal size: $95K
- Velocity: 58 days

Needs Coaching (Mike):
- Pipeline: $650K (2.1x quota)
- Win rate: 18%
- Avg deal size: $62K
- Velocity: 89 days
```

### Stage-by-Stage Conversion

```
Discovery → Demo: 45%
Demo → Proposal: 32%
Proposal → Negotiation: 68%
Negotiation → Closed-Won: 75%

Overall Win Rate: 22%
```

---

## Integration with Other Workflows

### After Pipeline Audit:

**If coverage is low:**
```
/sales-prospecting:generate-leads
```

**If deals are stalled:**
```
/sales-calls:prepare-call "Re-engagement call for [deal]"
/email-marketing:design-campaign "Re-engagement sequence"
```

**If conversion is low:**
```
/sales-enablement:build-playbook "Improve demo conversion"
/sales-coaching:review-call "Analyze recent demo calls"
```

**If forecast is off:**
```
/sales-operations:design-territories "Rebalance territories"
```

---

## Real User Example

> "Our weekly pipeline reviews used to take 4 hours - pulling reports, analyzing in Excel, creating slides for leadership. Now I run the audit in 10 minutes and spend the rest of the time actually coaching my team on the issues we find."
>
> — David R., VP of Sales at GrowthCo

**David's Results:**
- **Before:** 4 hours/week on pipeline analysis
- **After:** 1 hour/week
- **Time saved:** 3 hours/week = 156 hours/year
- **Value:** $15,600/year (at $100/hour)
- **Business impact:** 
  - Forecast accuracy improved from 72% to 91%
  - Average deal velocity decreased from 87 to 64 days
  - Win rate increased from 19% to 27%

---

## Pipeline Health Scoring

### How the Score is Calculated

**Coverage (30 points):**
- 5x+ quota: 30 points
- 4-5x quota: 25 points
- 3-4x quota: 20 points
- 2-3x quota: 10 points
- <2x quota: 0 points

**Velocity (25 points):**
- Faster than target: 25 points
- At target: 20 points
- 10-20% slower: 15 points
- >20% slower: 5 points

**Conversion Rates (25 points):**
- All stages on target: 25 points
- 1 stage below target: 20 points
- 2 stages below target: 10 points
- 3+ stages below target: 0 points

**Deal Health (20 points):**
- No stalled deals: 20 points
- 1-5 stalled: 15 points
- 6-10 stalled: 10 points
- 11+ stalled: 0 points

**Total: 100 points**

---

## Best Practices

### Run Weekly
Make this a Monday morning ritual:
1. Export fresh data from CRM
2. Run pipeline audit
3. Identify top 3 actions
4. Share with team
5. Track progress

### Focus on Trends
Don't just look at point-in-time:
- Is health score improving?
- Are velocity trends positive?
- Are conversion rates stable?

### Take Action
Analysis without action is wasted:
- Assign owners to at-risk deals
- Set deadlines for re-engagement
- Track action completion

### Share Insights
Make it visible:
- Weekly team email
- Dashboard in CRM
- Leadership updates
- Rep coaching sessions

---

## Related Use Cases

- [Generate Qualified Leads](lead-generation-workflow.md)
- [Build Email Re-engagement Sequence](cold-email-sequence.md)
- [Sales Call Preparation](sales-call-prep.md)
- [Forecast Your Quarter](quarterly-forecast.md)

---

## Resources

- [Sales Pipeline Plugin Documentation](../plugin-reference.md#sales-pipeline)
- [Pipeline Management Best Practices](../business-skills.md#pipeline-management)
- [CRM Integration Guide](../integrations.md#crm)
- [Forecasting Framework](../business-skills.md#forecasting)

---

**Questions?** [Ask in GitHub Discussions](https://github.com/gtmagents/gtm-agents/discussions)

**Found this helpful?** [Support the project ☕](https://buymeacoffee.com/gtmagents)
