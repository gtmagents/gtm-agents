# Use Case: Segment Your Customer Base in 15 Minutes

## Overview

**Problem:** You need to understand your customers better but manual segmentation analysis takes days and requires SQL skills.

**Solution:** Use the `customer-analytics` plugin to automatically segment your customer base and identify high-value cohorts in under 15 minutes.

**Time Saved:** ~16 hours (from 2 days to 15 minutes)

**ROI:** At $100/hour, that's $1,600 saved per segmentation analysis

---

## Who This Is For

- Growth Managers
- Product Managers
- Marketing Managers
- Data Analysts
- Customer Success Leaders

---

## What You'll Get

✅ Customer segments with clear characteristics  
✅ Behavioral patterns by segment  
✅ Revenue contribution by segment  
✅ Engagement metrics by segment  
✅ Recommended actions for each segment  
✅ Segment size and growth trends  
✅ Activation and retention rates

---

## Prerequisites

- [ ] Claude Code installed
- [ ] GTM Agents marketplace added
- [ ] `customer-analytics` plugin installed
- [ ] Customer data export (CSV from your database/CRM)

---

## Step-by-Step Instructions

### Step 1: Export Your Customer Data (5 minutes)

Export from your database/CRM with these fields:

**Required:**
- Customer ID
- Signup date
- Total revenue (lifetime)
- Last activity date
- Plan/tier

**Optional (for better segmentation):**
- Monthly active usage
- Feature usage data
- Support tickets
- NPS score
- Company size
- Industry

**Example CSV:**
```csv
customer_id,signup_date,revenue,last_active,plan,monthly_usage,company_size
CUST001,2024-01-15,12000,2024-11-15,Enterprise,450,500
CUST002,2024-03-20,2400,2024-11-10,Pro,120,50
```

### Step 2: Run Customer Segmentation (5 minutes)

1. Open Claude Code
2. Run:
   ```
   /customer-analytics:segment-customers
   ```
3. Upload your CSV or paste the data
4. Specify segmentation approach:

**Example Prompt:**
```
Segment our B2B SaaS customers based on:
- Revenue (LTV)
- Engagement (monthly usage)
- Tenure (how long they've been customers)
- Plan tier

Goal: Identify high-value segments for targeted campaigns
```

### Step 3: Review Segment Analysis (5 minutes)

The plugin identifies segments and provides insights:

---

## SEGMENT 1: Champions (High Value, High Engagement)

**Size:** 145 customers (12% of base)  
**Revenue:** $1.2M ARR (45% of total revenue)  
**Avg LTV:** $8,275  
**Retention:** 98%

**Characteristics:**
- Enterprise plan customers
- 300+ monthly active users
- Using 5+ core features
- Been customers 12+ months
- High NPS (9-10)

**Behavioral Patterns:**
- Log in daily
- Use advanced features
- Attend webinars
- Refer new customers
- Engage with support proactively

**Recommended Actions:**
1. **Upsell/Cross-sell:** They're ready for premium features
2. **Advocacy:** Ask for case studies, testimonials, referrals
3. **Executive engagement:** QBRs, advisory board invitations
4. **Early access:** Beta test new features
5. **Community:** Invite to exclusive user groups

**Revenue Opportunity:** $240K (20% upsell potential)

---

## SEGMENT 2: Rising Stars (Medium Value, High Engagement)

**Size:** 320 customers (26% of base)  
**Revenue:** $640K ARR (24% of total revenue)  
**Avg LTV:** $2,000  
**Retention:** 92%

**Characteristics:**
- Pro plan customers
- 100-300 monthly active users
- Using 3-4 core features
- Been customers 6-12 months
- Good NPS (7-8)

**Behavioral Patterns:**
- Log in 3-4x per week
- Growing usage month-over-month
- Asking about advanced features
- Expanding team size
- Positive support interactions

**Recommended Actions:**
1. **Upgrade campaign:** Show value of Enterprise features
2. **Education:** Advanced feature webinars
3. **Success stories:** Share how similar companies scaled
4. **Usage optimization:** Help them get more value
5. **Expansion:** Identify additional use cases

**Revenue Opportunity:** $192K (30% upgrade potential)

---

## SEGMENT 3: Steady Users (Medium Value, Medium Engagement)

**Size:** 450 customers (37% of base)  
**Revenue:** $540K ARR (20% of total revenue)  
**Avg LTV:** $1,200  
**Retention:** 85%

**Characteristics:**
- Pro plan customers
- 50-100 monthly active users
- Using 2-3 core features
- Been customers 3-12 months
- Neutral NPS (6-7)

**Behavioral Patterns:**
- Log in 1-2x per week
- Stable usage (not growing)
- Limited feature adoption
- Minimal support engagement
- Renew but don't expand

**Recommended Actions:**
1. **Activation:** Drive deeper feature adoption
2. **Education:** Use case webinars and tutorials
3. **Check-ins:** Quarterly success reviews
4. **Feedback:** Understand barriers to growth
5. **Community:** Connect with power users

**Revenue Opportunity:** $108K (20% expansion potential)

---

## SEGMENT 4: At Risk (Low Value, Low Engagement)

**Size:** 210 customers (17% of base)  
**Revenue:** $210K ARR (8% of total revenue)  
**Avg LTV:** $1,000  
**Retention:** 65%

**Characteristics:**
- Starter/Pro plan customers
- <50 monthly active users
- Using 1-2 basic features only
- Been customers 1-6 months
- Low NPS (0-6)

**Behavioral Patterns:**
- Log in <1x per week
- Declining usage
- Support tickets about "how to" basics
- Not attending events
- Considering alternatives

**Recommended Actions:**
1. **Win-back campaign:** Re-engagement email sequence
2. **Success intervention:** Dedicated onboarding call
3. **Value demonstration:** Show ROI and quick wins
4. **Feedback collection:** Exit surveys, interviews
5. **Retention offers:** Discounts, extended trials

**Churn Risk:** $136K ARR (65% likely to churn)

---

## SEGMENT 5: New Customers (Unknown Potential)

**Size:** 95 customers (8% of base)  
**Revenue:** $76K ARR (3% of total revenue)  
**Avg LTV:** $800  
**Retention:** N/A (too new)

**Characteristics:**
- All plan tiers
- Varied usage levels
- Been customers <3 months
- Still in onboarding
- No NPS data yet

**Behavioral Patterns:**
- Exploring features
- High support engagement
- Learning curve
- Usage patterns forming
- Activation in progress

**Recommended Actions:**
1. **Onboarding excellence:** White-glove first 90 days
2. **Quick wins:** Help them see value fast
3. **Education:** Comprehensive training program
4. **Monitoring:** Track activation metrics closely
5. **Segmentation:** Move to appropriate segment after 90 days

**Potential:** $95K ARR (if 80% activate successfully)

---

### Step 4: Take Action on Insights (Ongoing)

Based on segmentation, launch targeted initiatives:

**This Week:**
- [ ] Create Champions advocacy program
- [ ] Launch Rising Stars upgrade campaign
- [ ] Design At Risk win-back sequence
- [ ] Improve New Customer onboarding

**This Month:**
- [ ] Build segment-specific email campaigns
- [ ] Create targeted content for each segment
- [ ] Set up automated segment tracking
- [ ] Train team on segment strategies

**This Quarter:**
- [ ] Measure segment movement (upgrades/downgrades)
- [ ] Calculate segment-specific LTV
- [ ] Optimize product for each segment
- [ ] Refine segmentation criteria

---

## Segmentation Frameworks

### RFM Analysis (Recency, Frequency, Monetary)

**Recency:** When did they last engage?
- Recent (0-30 days): Active
- Moderate (31-90 days): Declining
- Distant (90+ days): At risk

**Frequency:** How often do they engage?
- High (daily): Power users
- Medium (weekly): Regular users
- Low (monthly or less): Casual users

**Monetary:** How much revenue?
- High (top 20%): Champions
- Medium (middle 60%): Core
- Low (bottom 20%): Small accounts

### Behavioral Segmentation

**By Feature Usage:**
- Power users (5+ features)
- Core users (3-4 features)
- Basic users (1-2 features)
- Non-users (signed up, not using)

**By Growth Trajectory:**
- Expanding (usage increasing)
- Stable (usage flat)
- Declining (usage decreasing)
- Churned (no activity 90+ days)

### Value-Based Segmentation

**By LTV:**
- Whales (top 10%, $10K+ LTV)
- Dolphins (next 30%, $3K-10K LTV)
- Minnows (bottom 60%, <$3K LTV)

**By Potential:**
- High potential (small now, growing fast)
- Medium potential (stable, some growth)
- Low potential (maxed out, not growing)

---

## Segment-Specific Strategies

### Champions Strategy

**Goal:** Maximize advocacy and retention

**Tactics:**
- Executive QBRs
- Advisory board membership
- Beta program access
- Case study creation
- Referral incentives
- Premium support
- Exclusive events

**KPIs:**
- Retention rate: 98%+
- NPS: 9-10
- Referrals: 2+ per year
- Expansion: 20%+ annually

### Rising Stars Strategy

**Goal:** Accelerate to Champions

**Tactics:**
- Upgrade campaigns
- Advanced training
- Success benchmarking
- Feature recommendations
- Expansion planning
- ROI reporting

**KPIs:**
- Upgrade rate: 30%+
- Usage growth: 15%+ MoM
- Feature adoption: +2 features
- NPS improvement: +1 point

### At Risk Strategy

**Goal:** Prevent churn, re-engage

**Tactics:**
- Win-back emails
- Success intervention calls
- Value demonstration
- Discount offers
- Feedback surveys
- Competitive analysis

**KPIs:**
- Save rate: 35%+
- Usage recovery: 50%+
- NPS improvement: +2 points
- Churn reduction: -20%

---

## Advanced Analysis

### Cohort Analysis by Segment

Track how segments evolve over time:

```
January Cohort (100 customers):
Month 1: 80% New, 20% Rising Stars
Month 3: 50% Rising Stars, 30% Steady, 15% At Risk, 5% Champions
Month 6: 40% Champions, 35% Rising Stars, 20% Steady, 5% Churned
Month 12: 50% Champions, 30% Rising Stars, 15% Steady, 5% Churned
```

### Segment Migration

Track movement between segments:

```
Q3 → Q4 Segment Changes:
- 45 Rising Stars → Champions (upgrade success!)
- 30 Steady → Rising Stars (activation working)
- 25 At Risk → Steady (win-back success)
- 15 Steady → At Risk (need intervention)
- 20 At Risk → Churned (lost customers)
```

### Revenue Concentration

Understand revenue distribution:

```
Top 20% of customers = 70% of revenue (Champions + Rising Stars)
Middle 60% of customers = 25% of revenue (Steady Users)
Bottom 20% of customers = 5% of revenue (At Risk + New)
```

---

## Integration with Other Workflows

### After Segmentation:

**For Champions:**
```
/customer-marketing:activate-advocacy "Create case study program"
/account-management:plan-qbr "Schedule executive reviews"
```

**For Rising Stars:**
```
/email-marketing:design-campaign "Upgrade campaign for Pro users"
/customer-success:launch-adoption-program "Advanced feature training"
```

**For At Risk:**
```
/email-marketing:design-campaign "Win-back sequence"
/customer-success:build-success-plan "Intervention strategy"
```

**For New Customers:**
```
/customer-success:design-lifecycle-journey "Onboarding optimization"
/growth-experiments:design-experiment "Test activation tactics"
```

---

## Real User Example

> "We had 1,200 customers but treated them all the same. After segmenting, we realized 150 Champions drove 50% of our revenue. We created a VIP program for them and saw retention jump from 85% to 98%. Meanwhile, our At Risk segment got targeted win-back campaigns that saved $200K in ARR."
>
> — Lisa M., Head of Growth at DataCo

**Lisa's Results:**
- **Before:** One-size-fits-all approach, 85% retention
- **After:** Segment-specific strategies, 92% overall retention
- **Champions retention:** 85% → 98%
- **At Risk save rate:** 0% → 35%
- **Revenue impact:** +$450K ARR saved/expanded
- **Time saved:** 16 hours per analysis

---

## Segmentation Best Practices

### Start Simple
Begin with 3-5 segments:
- High value, high engagement
- High value, low engagement
- Low value, high engagement
- Low value, low engagement
- New customers

### Use Multiple Dimensions
Don't segment on just one variable:
- Revenue + Engagement + Tenure
- Plan + Usage + Growth
- Industry + Size + Behavior

### Make It Actionable
Each segment should have:
- Clear definition
- Distinct characteristics
- Specific strategies
- Measurable goals

### Update Regularly
- Re-segment monthly or quarterly
- Track segment migration
- Refine criteria based on learnings
- Adjust strategies as segments evolve

### Automate Tracking
- Set up dashboards
- Create alerts for segment changes
- Automate segment-specific campaigns
- Monitor KPIs by segment

---

## Common Pitfalls to Avoid

### ❌ Too Many Segments
**Problem:** 20 micro-segments are impossible to manage

**Solution:** Start with 5 segments, add more only if needed

### ❌ Static Segmentation
**Problem:** Segments defined once, never updated

**Solution:** Re-segment quarterly, track migration

### ❌ No Clear Actions
**Problem:** Interesting insights but no strategy

**Solution:** Define specific tactics for each segment

### ❌ Ignoring Small Segments
**Problem:** Focus only on Champions, ignore At Risk

**Solution:** Every segment needs a strategy (even if it's "let churn")

---

## Related Use Cases

- [Predict Customer Churn](churn-prediction.md)
- [Calculate Customer LTV](ltv-calculation.md)
- [Design Growth Experiments](ab-test-design.md)
- [Build Retention Campaigns](retention-campaigns.md)

---

## Resources

- [Customer Analytics Plugin Documentation](../plugin-reference.md#customer-analytics)
- [Segmentation Framework](../business-skills.md#customer-segmentation)
- [RFM Analysis Guide](../business-skills.md#rfm-analysis)
- [Cohort Analysis Template](../../templates/cohort-analysis.md)

---

**Questions?** [Ask in GitHub Discussions](https://github.com/gtmagents/gtm-agents/discussions)

**Found this helpful?** [Support the project ☕](https://buymeacoffee.com/gtmagents)
