# Use Case: Design and Launch an A/B Test in 10 Minutes

## Overview

**Problem:** You want to run growth experiments but designing statistically valid A/B tests requires expertise and takes hours.

**Solution:** Use the `growth-experiments` plugin to design, calculate sample sizes, and launch A/B tests in under 10 minutes.

**Time Saved:** ~6 hours per experiment (from 8 hours to 2 hours including setup)

**ROI:** At $125/hour, that's $750 saved per experiment

---

## Who This Is For

- Growth Managers
- Product Managers
- Marketing Managers
- Data Analysts
- Conversion Rate Optimizers

---

## What You'll Get

✅ Hypothesis framework  
✅ Sample size calculation  
✅ Test duration estimate  
✅ Success metrics defined  
✅ Statistical significance thresholds  
✅ Implementation checklist  
✅ Analysis framework

---

## Prerequisites

- [ ] Claude Code installed
- [ ] GTM Agents marketplace added
- [ ] `growth-experiments` plugin installed
- [ ] Baseline metrics available
- [ ] Testing tool access (Optimizely, VWO, Google Optimize, etc.)

---

## Step-by-Step Instructions

### Step 1: Define What You Want to Test (2 minutes)

Be specific about the change you want to test:

**Examples:**
- "New homepage hero section"
- "Pricing page layout"
- "Email subject line"
- "Onboarding flow"
- "CTA button color and copy"

### Step 2: Run Experiment Designer (3 minutes)

1. Open Claude Code
2. Run:
   ```
   /growth-experiments:design-experiment
   ```
3. Describe your experiment:

**Example Prompt:**
```
I want to test a new pricing page layout.

Current situation:
- Page: /pricing
- Current conversion rate: 3.2%
- Monthly visitors: 10,000
- Goal: Increase trial signups

Proposed change:
- Simplify from 4 plans to 3 plans
- Add comparison table
- Highlight "most popular" plan
- Add customer logos

Expected impact: 15-20% increase in conversions
```

### Step 3: Review Experiment Design (5 minutes)

The plugin generates a complete experiment plan:

---

## EXPERIMENT DESIGN

### Hypothesis

**Format:** If [change], then [outcome], because [reasoning]

**Your Hypothesis:**
```
If we simplify the pricing page from 4 plans to 3 and add social proof,
then trial signup conversion will increase by 15-20%,
because users will have less decision paralysis and more trust signals.
```

### Variables

**Independent Variable (what you're changing):**
- Pricing page layout
- Number of plans (4 → 3)
- Addition of comparison table
- Addition of customer logos

**Dependent Variable (what you're measuring):**
- Primary: Trial signup conversion rate
- Secondary: Time on page, scroll depth, plan selection distribution

**Control Variables (keep constant):**
- Traffic source
- Device type
- Time of day
- Pricing amounts
- Trial length

### Success Metrics

**Primary Metric:**
- Trial signup conversion rate
- Current baseline: 3.2%
- Target: 3.7% (15% relative increase)
- Minimum detectable effect: 0.4% (12.5% relative increase)

**Secondary Metrics:**
- Time on page (expect increase)
- Scroll depth (expect increase to comparison table)
- Plan distribution (expect shift to "most popular")
- Bounce rate (expect decrease)

**Guardrail Metrics (must not degrade):**
- Page load time (<3 seconds)
- Mobile conversion rate (maintain parity)
- Paid plan selection rate (maintain or improve)

---

## SAMPLE SIZE CALCULATION

**Inputs:**
- Baseline conversion rate: 3.2%
- Minimum detectable effect: 15% relative (0.48% absolute)
- Statistical power: 80%
- Significance level: 95% (α = 0.05)
- Two-tailed test

**Required Sample Size:**
- **Per variation: 16,250 visitors**
- **Total needed: 32,500 visitors**

**Timeline:**
- Monthly traffic: 10,000 visitors
- 50/50 split: 5,000 per variation per month
- **Test duration: 3.25 months (13 weeks)**

**Recommendation:**
- Run for minimum 4 months to account for:
  - Weekly seasonality
  - Monthly billing cycles
  - Holidays/anomalies
  - Buffer for statistical confidence

---

## TEST SETUP

### Traffic Allocation

**Option 1: Conservative (Recommended)**
```
Control (current page): 50%
Variation (new page): 50%
```

**Option 2: Aggressive**
```
Control: 10%
Variation: 90%
(Use if very confident in variation)
```

**Option 3: Gradual Rollout**
```
Week 1-2: 50/50
Week 3-4: 25/75 (if variation winning)
Week 5+: 10/90 or full rollout
```

### Randomization

**User-level randomization:**
- Assign users to variation on first visit
- Persist assignment via cookie/localStorage
- Duration: 90 days

**Avoid:**
- Session-level randomization (inconsistent experience)
- Page-level randomization (sample ratio mismatch)

### Segmentation

**Segment by:**
- Traffic source (organic, paid, direct, referral)
- Device type (desktop, mobile, tablet)
- New vs returning visitors
- Geography (if relevant)

**Why:** Understand if effect varies by segment

---

## IMPLEMENTATION CHECKLIST

### Pre-Launch (Week Before)

- [ ] Build variation page
- [ ] QA on all devices/browsers
- [ ] Set up tracking (events, goals)
- [ ] Configure testing tool
- [ ] Test randomization logic
- [ ] Verify data collection
- [ ] Document experiment in tracker
- [ ] Get stakeholder approval

### Launch Day

- [ ] Enable experiment at low traffic (10%)
- [ ] Monitor for 24 hours
- [ ] Check sample ratio (should be 50/50)
- [ ] Verify data flowing correctly
- [ ] Check for errors/bugs
- [ ] Ramp to full traffic if all good

### During Test

- [ ] Daily: Check sample ratio
- [ ] Daily: Monitor guardrail metrics
- [ ] Weekly: Review preliminary results
- [ ] Weekly: Check for anomalies
- [ ] Monthly: Segment analysis
- [ ] Document learnings

### Post-Test

- [ ] Reach statistical significance
- [ ] Analyze results by segment
- [ ] Calculate confidence intervals
- [ ] Document learnings
- [ ] Share results with team
- [ ] Implement winner (or iterate)

---

## ANALYSIS FRAMEWORK

### Statistical Significance

**When to call the test:**

**Winner declared if:**
- p-value < 0.05 (95% confidence)
- Reached minimum sample size
- Ran for minimum duration
- No sample ratio mismatch
- Guardrails not violated

**Example Results:**

```
Control: 3.2% conversion (520/16,250)
Variation: 3.8% conversion (617/16,250)

Absolute lift: +0.6%
Relative lift: +18.75%
p-value: 0.023 (statistically significant!)
95% CI: [+0.08%, +1.12%]

Conclusion: Variation wins! 
Expected annual impact: +600 trials = +$180K ARR
```

### Segment Analysis

Break down results by key segments:

**By Traffic Source:**
```
Organic:
- Control: 3.5% | Variation: 4.2% (+20%)
- Significant: Yes

Paid:
- Control: 2.8% | Variation: 3.1% (+11%)
- Significant: No (underpowered)

Direct:
- Control: 4.1% | Variation: 4.8% (+17%)
- Significant: Yes
```

**By Device:**
```
Desktop:
- Control: 3.8% | Variation: 4.5% (+18%)
- Significant: Yes

Mobile:
- Control: 2.4% | Variation: 2.5% (+4%)
- Significant: No

Insight: Variation works great on desktop, 
minimal impact on mobile. Consider mobile-specific test.
```

---

## COMMON EXPERIMENT TYPES

### Landing Page Tests

**What to test:**
- Hero headline and subheadline
- CTA button copy and color
- Social proof placement
- Form length
- Images vs videos
- Trust badges

**Example:**
```
Hypothesis: Adding customer logos above the fold will increase 
conversions by 10% because it builds immediate trust.

Test: Control (no logos) vs Variation (6 customer logos)
Duration: 4 weeks
Sample size: 5,000 per variation
```

### Pricing Tests

**What to test:**
- Number of plans
- Plan positioning
- Price anchoring
- Billing frequency (monthly vs annual)
- Feature bundling
- Free trial length

**Example:**
```
Hypothesis: Highlighting annual billing with "Save 20%" badge 
will increase annual plan selection by 25%.

Test: Control (equal emphasis) vs Variation (annual highlighted)
Duration: 8 weeks (2 billing cycles)
Sample size: 2,000 per variation
```

### Email Tests

**What to test:**
- Subject lines
- Sender name
- Preview text
- Email length
- CTA placement
- Personalization

**Example:**
```
Hypothesis: Personalized subject lines with first name will 
increase open rates by 15%.

Test: "Your trial expires soon" vs "[Name], your trial expires soon"
Duration: 1 week
Sample size: 10,000 per variation
```

### Onboarding Tests

**What to test:**
- Number of steps
- Required vs optional fields
- Progress indicators
- Tooltips and help text
- Welcome emails
- Activation checklist

**Example:**
```
Hypothesis: Reducing signup form from 8 fields to 4 will 
increase completion rate by 30%.

Test: Control (8 fields) vs Variation (4 fields)
Duration: 6 weeks
Sample size: 1,500 per variation
```

---

## SAMPLE SIZE CALCULATOR

### Quick Reference Table

**For conversion rate tests (95% confidence, 80% power):**

| Baseline Rate | Minimum Detectable Effect | Sample Size Per Variation |
|---------------|---------------------------|---------------------------|
| 1% | 20% relative (0.2% absolute) | 39,000 |
| 2% | 20% relative (0.4% absolute) | 19,000 |
| 5% | 20% relative (1% absolute) | 7,400 |
| 10% | 20% relative (2% absolute) | 3,600 |
| 20% | 20% relative (4% absolute) | 1,700 |

**For smaller effects (10% relative lift):**

| Baseline Rate | 10% Relative Lift | Sample Size Per Variation |
|---------------|-------------------|---------------------------|
| 2% | 0.2% absolute | 77,000 |
| 5% | 0.5% absolute | 30,000 |
| 10% | 1% absolute | 14,500 |

### When You Need More Power

**Increase sample size if:**
- Testing small changes (5-10% expected lift)
- High variance in metric
- Multiple variations (A/B/C/D test)
- Segmented analysis planned
- Risk-averse organization

---

## AVOIDING COMMON MISTAKES

### ❌ Peeking Too Early

**Problem:** Checking results daily and stopping when "significant"

**Why it's wrong:** Increases false positive rate

**Solution:** 
- Define sample size upfront
- Don't stop early unless overwhelming evidence
- Use sequential testing if you must peek

### ❌ Not Running Long Enough

**Problem:** Stopping after 1 week because "significant"

**Why it's wrong:** Weekly seasonality, novelty effects

**Solution:**
- Run for at least 2 full business cycles
- Minimum 2 weeks, ideally 4+ weeks
- Account for monthly patterns

### ❌ Sample Ratio Mismatch

**Problem:** 60/40 split instead of 50/50

**Why it's wrong:** Indicates tracking issues

**Solution:**
- Monitor daily
- Investigate immediately if >2% off
- Don't trust results if SRM present

### ❌ Multiple Testing

**Problem:** Testing 10 variations simultaneously

**Why it's wrong:** Increases false positive rate

**Solution:**
- Limit to 2-4 variations max
- Adjust significance threshold (Bonferroni correction)
- Or run sequential tests

### ❌ Ignoring Guardrails

**Problem:** Conversion up 20% but revenue down 10%

**Why it's wrong:** Optimizing wrong metric

**Solution:**
- Define guardrail metrics upfront
- Monitor throughout test
- Don't ship if guardrails violated

---

## EXPERIMENT VELOCITY

### Building an Experimentation Culture

**Week 1-4: Foundation**
- Set up testing infrastructure
- Train team on methodology
- Run first 2-3 tests
- Document learnings

**Month 2-3: Acceleration**
- Run 4-6 tests per month
- Build experiment backlog
- Create testing playbook
- Share wins widely

**Month 4+: Scale**
- Run 8-12 tests per month
- Automated reporting
- Cross-functional experiments
- Continuous optimization

### Experiment Prioritization (ICE Framework)

**Score each experiment:**

**Impact (1-10):** How much will this move the needle?
**Confidence (1-10):** How sure are you it will work?
**Ease (1-10):** How easy is it to implement?

**ICE Score = (Impact + Confidence + Ease) / 3**

**Example:**
```
Experiment: Simplify pricing page
Impact: 8 (could increase conversions 15%)
Confidence: 7 (similar tests worked before)
Ease: 6 (requires design + dev work)
ICE Score: 7.0 (HIGH PRIORITY)

Experiment: Change button color
Impact: 3 (minor impact expected)
Confidence: 5 (mixed evidence)
Ease: 10 (5-minute change)
ICE Score: 6.0 (MEDIUM PRIORITY)
```

---

## Real User Example

> "We used to spend 2 days designing each experiment - calculating sample sizes in Excel, debating methodology, second-guessing ourselves. Now we design experiments in 10 minutes with confidence. We've gone from 2 tests per quarter to 8 tests per month. Our conversion rate has improved 40% in 6 months."
>
> — Marcus T., Head of Growth at ConvertCo

**Marcus's Results:**
- **Before:** 8 experiments per year, 2 days per design
- **After:** 96 experiments per year, 2 hours per design
- **Time saved:** 6 hours × 96 = 576 hours/year
- **Value:** $72,000 saved
- **Business impact:** 40% conversion rate improvement = $2.4M additional ARR

---

## Related Use Cases

- [Customer Segmentation](customer-segmentation.md)
- [Conversion Rate Optimization](cro-audit.md)
- [Landing Page Optimization](landing-page-optimization.md)
- [Email A/B Testing](email-ab-testing.md)

---

## Resources

- [Growth Experiments Plugin Documentation](../plugin-reference.md#growth-experiments)
- [A/B Testing Framework](../business-skills.md#ab-testing)
- [Statistical Significance Calculator](../../templates/sample-size-calculator.md)
- [Experiment Tracker Template](../../templates/experiment-tracker.md)

---

**Questions?** [Ask in GitHub Discussions](https://github.com/gtmagents/gtm-agents/discussions)

**Found this helpful?** [Support the project ☕](https://buymeacoffee.com/gtmagents)
