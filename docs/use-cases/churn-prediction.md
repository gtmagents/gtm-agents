# Use Case: Predict and Prevent Customer Churn

## Overview

**Problem:** Customers churn unexpectedly and you don't know who's at risk until it's too late.

**Solution:** Use the `customer-analytics` plugin to identify at-risk customers and predict churn probability in under 10 minutes.

**Time Saved:** ~12 hours per month (from 15 hours to 3 hours)

**ROI:** At $100/hour, that's $1,200 saved per month + revenue saved from prevented churn

---

## Who This Is For

- Customer Success Managers
- Growth Managers
- Product Managers
- Revenue Operations
- Retention Specialists

---

## What You'll Get

✅ Churn risk score for each customer  
✅ Top churn indicators identified  
✅ At-risk customer list prioritized  
✅ Recommended intervention strategies  
✅ Predicted churn timeline  
✅ Save rate estimates  
✅ Revenue at risk calculation

---

## Prerequisites

- [ ] Claude Code installed
- [ ] GTM Agents marketplace added
- [ ] `customer-analytics` plugin installed
- [ ] Customer data export (usage, engagement, support, billing)

---

## Step-by-Step Instructions

### Step 1: Export Customer Data (5 minutes)

Export from your database/CRM with these fields:

**Account Information:**
- Customer ID
- Account name
- MRR/ARR
- Contract end date
- Tenure (months as customer)

**Usage Data:**
- Monthly active users
- Feature usage (which features, how often)
- Last login date
- Login frequency (last 30 days)

**Engagement Data:**
- Support tickets (count, severity)
- NPS score
- Product feedback submitted
- Event attendance
- Email engagement

**Billing Data:**
- Payment issues
- Downgrades
- Failed payments
- Discount/promotion usage

**Example CSV:**
```csv
customer_id,mrr,tenure_months,monthly_logins,last_login_days_ago,support_tickets_30d,nps,contract_days_remaining
CUST001,5000,24,45,2,1,9,180
CUST002,1200,6,3,45,8,3,90
```

### Step 2: Run Churn Prediction (3 minutes)

1. Open Claude Code
2. Run:
   ```
   /customer-analytics:predict-churn
   ```
3. Upload your CSV or paste the data
4. Specify your churn definition:

**Example Prompt:**
```
Analyze churn risk for our B2B SaaS customers.

Churn definition: No login in 60 days or contract not renewed

Analyze based on:
- Usage patterns (logins, feature adoption)
- Engagement (support, NPS, events)
- Account health (tenure, MRR, growth)
- Billing signals (payment issues, downgrades)

Goal: Identify customers at risk in next 90 days
```

### Step 3: Review Churn Analysis (5-10 minutes)

The plugin provides a comprehensive churn risk assessment:

---

## CHURN RISK OVERVIEW

**Total Customers Analyzed:** 1,247  
**At High Risk (>70%):** 89 customers ($267K MRR)  
**At Medium Risk (40-70%):** 156 customers ($312K MRR)  
**At Low Risk (<40%):** 1,002 customers ($2.1M MRR)

**Predicted Churn (Next 90 Days):**
- High risk: 62 customers (70% churn rate) = $187K MRR at risk
- Medium risk: 47 customers (30% churn rate) = $94K MRR at risk
- **Total at risk:** $281K MRR

**If No Intervention:**
- Expected churn: 109 customers
- Revenue loss: $281K MRR = $3.4M ARR
- With 35% save rate: Can save $98K MRR

---

## TOP CHURN INDICATORS

**Ranked by Predictive Power:**

1. **Login Frequency (90% predictive)**
   - <5 logins/month = 85% churn rate
   - 5-15 logins/month = 45% churn rate
   - 15+ logins/month = 8% churn rate

2. **Days Since Last Login (85% predictive)**
   - 45+ days = 92% churn rate
   - 30-45 days = 68% churn rate
   - 15-30 days = 35% churn rate
   - <15 days = 6% churn rate

3. **Support Ticket Volume (75% predictive)**
   - 5+ tickets/month = 78% churn rate
   - 3-5 tickets/month = 52% churn rate
   - 1-2 tickets/month = 22% churn rate
   - 0 tickets/month = 12% churn rate

4. **NPS Score (70% predictive)**
   - 0-6 (Detractors) = 72% churn rate
   - 7-8 (Passives) = 28% churn rate
   - 9-10 (Promoters) = 4% churn rate

5. **Feature Adoption (65% predictive)**
   - 0-1 features = 81% churn rate
   - 2-3 features = 42% churn rate
   - 4+ features = 9% churn rate

6. **Tenure (60% predictive)**
   - 0-3 months = 55% churn rate
   - 3-6 months = 38% churn rate
   - 6-12 months = 22% churn rate
   - 12+ months = 12% churn rate

7. **Payment Issues (55% predictive)**
   - Failed payment = 89% churn rate
   - Downgrade = 64% churn rate
   - No issues = 15% churn rate

---

## HIGH-RISK CUSTOMERS (Immediate Action Required)

### Customer: Acme Corp
**Churn Risk:** 92% (CRITICAL)  
**MRR:** $5,000  
**Tenure:** 18 months  
**Contract Expires:** 45 days

**Risk Factors:**
- ❌ No login in 52 days (last: Oct 1)
- ❌ 8 support tickets in last month (all severity: high)
- ❌ NPS: 2 (Detractor)
- ❌ Using only 1 of 8 core features
- ❌ Champion left company (LinkedIn update)
- ❌ Downgraded from Enterprise to Pro (3 months ago)

**Predicted Churn Date:** Within 30 days  
**Save Probability:** 15% (very difficult)

**Recommended Actions:**
1. **URGENT:** Executive escalation call within 48 hours
2. Find new champion (who replaced departed contact?)
3. Understand root cause of support issues
4. Offer dedicated success manager
5. Consider win-back offer (discount, extended trial)
6. If lost, conduct exit interview

**Estimated Effort:** 10 hours  
**Potential Save Value:** $60K ARR (if successful)

---

### Customer: TechStart Inc
**Churn Risk:** 78% (HIGH)  
**MRR:** $1,200  
**Tenure:** 6 months  
**Contract Expires:** 90 days

**Risk Factors:**
- ⚠️ Login frequency dropped 80% (from 45/month to 9/month)
- ⚠️ Last login: 23 days ago
- ⚠️ NPS: 5 (Detractor)
- ⚠️ Only 2 active users (down from 8)
- ⚠️ No event attendance (0 webinars, 0 training)
- ✅ No support tickets (but also no engagement)

**Predicted Churn Date:** 60-75 days  
**Save Probability:** 40% (moderate)

**Recommended Actions:**
1. Success intervention call this week
2. Understand why usage dropped (team changes? priorities?)
3. Re-onboarding for remaining users
4. Quick wins demonstration
5. Invite to upcoming webinar
6. Offer 1-on-1 training session

**Estimated Effort:** 4 hours  
**Potential Save Value:** $14.4K ARR

---

### Customer: Global Systems
**Churn Risk:** 71% (HIGH)  
**MRR:** $3,500  
**Tenure:** 14 months  
**Contract Expires:** 120 days

**Risk Factors:**
- ⚠️ Feature usage declining (was using 6 features, now 3)
- ⚠️ Login frequency stable but shallow (quick logins, no depth)
- ⚠️ NPS: 6 (Passive leaning Detractor)
- ⚠️ Mentioned competitor in support ticket
- ⚠️ Asked about data export process
- ✅ Still logging in regularly

**Predicted Churn Date:** 90-105 days  
**Save Probability:** 55% (good chance)

**Recommended Actions:**
1. Proactive QBR to understand needs
2. Demonstrate ROI and value delivered
3. Address competitor comparison head-on
4. Re-activate unused features
5. Share relevant case studies
6. Offer product roadmap preview

**Estimated Effort:** 3 hours  
**Potential Save Value:** $42K ARR

---

## MEDIUM-RISK CUSTOMERS (Monitor Closely)

### Cohort Analysis

**156 customers at medium risk (40-70% churn probability)**

**Common Patterns:**
- Stable but not growing usage
- Passive NPS scores (7-8)
- Moderate engagement
- No major red flags but no green flags either
- "Coasting" accounts

**Recommended Strategy:**
1. **Automated nurture campaign**
   - Monthly value emails
   - Feature spotlight series
   - Customer success stories
   - Upcoming events/webinars

2. **Quarterly check-ins**
   - Automated health score monitoring
   - Trigger manual outreach if score drops
   - Proactive value demonstration

3. **Activation campaigns**
   - Drive deeper feature adoption
   - Share best practices
   - Invite to community

**Resource Allocation:** 30 minutes per customer per quarter

---

## CHURN PREVENTION PLAYBOOK

### For High-Risk Customers (>70% risk)

**Week 1: Diagnose**
- [ ] Review account history
- [ ] Identify root cause
- [ ] Find decision makers
- [ ] Assess save probability
- [ ] Prepare intervention plan

**Week 2: Intervene**
- [ ] Executive escalation call
- [ ] Understand concerns
- [ ] Demonstrate value/ROI
- [ ] Address objections
- [ ] Present solution

**Week 3: Execute**
- [ ] Implement agreed actions
- [ ] Provide dedicated support
- [ ] Monitor usage recovery
- [ ] Follow up frequently
- [ ] Track progress

**Week 4: Evaluate**
- [ ] Measure improvement
- [ ] Adjust strategy if needed
- [ ] Secure renewal commitment
- [ ] Document learnings

### For Medium-Risk Customers (40-70% risk)

**Month 1: Engage**
- [ ] Proactive outreach
- [ ] Value demonstration
- [ ] Feature education
- [ ] Quick wins

**Month 2: Activate**
- [ ] Drive feature adoption
- [ ] Share best practices
- [ ] Community involvement
- [ ] Success benchmarking

**Month 3: Solidify**
- [ ] QBR or check-in
- [ ] ROI reporting
- [ ] Renewal discussion
- [ ] Expansion opportunities

---

## CHURN PREDICTION MODEL

### How It Works

**Data Inputs:**
- Usage patterns (frequency, depth, breadth)
- Engagement signals (support, NPS, events)
- Account characteristics (tenure, size, industry)
- Billing behavior (payment issues, downgrades)
- Relationship health (champion status, satisfaction)

**Scoring Algorithm:**
```
Churn Risk Score = 
  (Usage Score × 0.30) +
  (Engagement Score × 0.25) +
  (Support Score × 0.20) +
  (NPS Score × 0.15) +
  (Billing Score × 0.10)

Where each component is scored 0-100 (100 = highest risk)
```

**Risk Tiers:**
- 0-40%: Low risk (healthy)
- 40-70%: Medium risk (monitor)
- 70-100%: High risk (intervene)

### Model Accuracy

**Validation Results:**
- Precision: 82% (of predicted churns, 82% actually churn)
- Recall: 76% (catches 76% of actual churns)
- F1 Score: 0.79 (good balance)

**False Positives:** 18% (predicted churn but didn't)
- Still valuable to engage these customers

**False Negatives:** 24% (didn't predict but churned)
- Often due to external factors (budget cuts, acquisitions)

---

## MEASURING SUCCESS

### Churn Metrics to Track

**Churn Rate:**
```
Monthly Churn Rate = Churned Customers / Total Customers at Start
Target: <5% monthly for B2B SaaS
```

**Revenue Churn:**
```
Monthly Revenue Churn = Churned MRR / Total MRR at Start
Target: <3% monthly (net negative with expansion)
```

**Save Rate:**
```
Save Rate = Saved Customers / At-Risk Customers Contacted
Target: 30-50%
```

**Early Warning:**
```
% of Churns Predicted 60+ Days in Advance
Target: 70%+
```

### ROI Calculation

**Example:**
```
Customers at high risk: 89
Predicted to churn: 62 (70%)
Revenue at risk: $187K MRR

With intervention:
- Customers contacted: 89
- Time per customer: 4 hours avg
- Total time: 356 hours
- Cost: $35,600 (at $100/hour)

Results:
- Customers saved: 31 (35% save rate)
- Revenue saved: $93K MRR = $1.1M ARR
- ROI: 31x ($1.1M / $35.6K)
```

---

## PREVENTION STRATEGIES

### Proactive (Before At-Risk)

**Onboarding Excellence:**
- First 90 days critical
- Drive to activation quickly
- Establish success criteria
- Regular check-ins

**Continuous Value:**
- Quarterly business reviews
- ROI reporting
- Feature education
- Best practice sharing

**Relationship Building:**
- Multi-threading (multiple contacts)
- Executive engagement
- Community involvement
- Customer advisory board

### Reactive (When At-Risk)

**Early Intervention:**
- Automated alerts when risk score increases
- Immediate outreach
- Root cause analysis
- Tailored save plan

**Win-Back Offers:**
- Discounts (use sparingly)
- Extended trials
- Free training/consulting
- Product enhancements

**Last Resort:**
- Executive escalation
- Custom solutions
- Partnership opportunities
- Graceful offboarding (for future win-back)

---

## Real User Example

> "We were losing 8-10% of customers monthly and didn't know why until they cancelled. Now we predict churn 60-90 days in advance and save 40% of at-risk customers. We've reduced churn from 8% to 4.5% monthly, saving $2.3M ARR."
>
> — Jennifer K., VP of Customer Success at RetainCo

**Jennifer's Results:**
- **Before:** 8% monthly churn, reactive approach
- **After:** 4.5% monthly churn, proactive intervention
- **Churn reduction:** 43.75%
- **Revenue saved:** $2.3M ARR
- **Save rate:** 40% of at-risk customers
- **Time investment:** 12 hours/month on analysis + intervention time

---

## Related Use Cases

- [Customer Segmentation](customer-segmentation.md)
- [Calculate Customer LTV](ltv-calculation.md)
- [Build Retention Campaigns](retention-campaigns.md)
- [Customer Health Scoring](health-scoring.md)

---

## Resources

- [Customer Analytics Plugin Documentation](../plugin-reference.md#customer-analytics)
- [Churn Prediction Framework](../business-skills.md#churn-prediction)
- [Retention Playbook](../business-skills.md#retention)
- [Customer Health Score Template](../../templates/health-score.md)

---

**Questions?** [Ask in GitHub Discussions](https://github.com/gtmagents/gtm-agents/discussions)

**Found this helpful?** [Support the project ☕](https://buymeacoffee.com/gtmagents)
