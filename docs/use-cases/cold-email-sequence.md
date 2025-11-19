# Use Case: Build a 5-Touch Cold Email Sequence

## Overview

**Problem:** You need to reach out to cold prospects but writing personalized email sequences takes hours per prospect.

**Solution:** Use the `email-marketing` plugin to create a complete 5-email sequence in under 5 minutes.

**Time Saved:** ~2 hours per sequence (from 2.5 hours to 30 minutes including customization)

**ROI:** At $75/hour, that's $150 saved per sequence

---

## Who This Is For

- Sales Development Reps (SDRs)
- Account Executives
- Business Development Reps (BDRs)
- Founders doing outreach
- Marketing teams running cold campaigns

---

## What You'll Get

✅ 5 personalized emails with subject lines  
✅ Optimal send timing (days between emails)  
✅ Personalization tokens  
✅ A/B test variations  
✅ Follow-up triggers  
✅ Breakup email template

---

## Prerequisites

- [ ] Claude Code installed
- [ ] GTM Agents marketplace added
- [ ] `email-marketing` plugin installed
- [ ] Target persona defined
- [ ] Value proposition clear

---

## Step-by-Step Instructions

### Step 1: Define Your Target (2 minutes)

Be specific about who you're reaching:

**Example Target:**
```
Role: VP of Sales
Company: B2B SaaS, Series A, 50-200 employees
Pain Point: Manual prospecting slowing down team
Goal: Book a 30-minute demo
```

### Step 2: Run the Sequence Builder (1 minute)

1. Open Claude Code
2. Run:
   ```
   /email-marketing:design-campaign
   ```
3. Describe your sequence:

**Example Prompt:**
```
Create a 5-email cold outreach sequence for VP of Sales at 
Series A B2B SaaS companies (50-200 employees).

Pain point: Their sales team is wasting time on manual prospecting
Solution: Our AI-powered prospecting tool saves 15 hours/week
Goal: Book a 30-minute demo
Tone: Professional but conversational, data-driven
```

### Step 3: Review the Sequence (2 minutes)

You'll get a complete sequence like this:

---

**EMAIL 1: Introduction (Day 0)**

**Subject:** Quick question about {{company}}'s sales process

**Body:**
```
Hi {{first_name}},

I noticed {{company}} recently raised Series A and is scaling 
your sales team. Congrats!

Quick question: How much time does your team spend on manual 
prospecting each week?

Most VPs of Sales we work with tell us their reps spend 15-20 
hours/week researching leads and building lists. That's nearly 
half their time not actually selling.

We've helped companies like [Customer 1] and [Customer 2] cut 
prospecting time by 80% using AI automation.

Worth a quick 15-minute conversation?

Best,
{{your_name}}

P.S. Here's a 2-minute video showing how it works: [link]
```

**Send timing:** Immediately after lead is qualified

---

**EMAIL 2: Value Proof (Day 3)**

**Subject:** How [Customer Name] saved 60 hours/week

**Body:**
```
{{first_name}},

Not sure if you saw my email from Tuesday, but wanted to share 
a quick case study that might be relevant.

[Customer Name] (similar size to {{company}}) was facing the 
same challenge - their 5 SDRs were spending 15 hours/week each 
on manual prospecting.

After implementing our solution:
• 75 hours/week saved across the team
• 3x more qualified leads generated
• 40% increase in meetings booked
• ROI in first month

Their VP of Sales said: "We got our SDRs back to actually 
selling instead of being researchers."

Want to see if we could deliver similar results for {{company}}?

Happy to do a quick 15-min screen share.

Best,
{{your_name}}
```

**Send timing:** 3 days after Email 1 if no response

---

**EMAIL 3: Different Angle (Day 7)**

**Subject:** {{first_name}}, thought you'd find this interesting

**Body:**
```
Hi {{first_name}},

I know you're busy, so I'll keep this brief.

I put together a quick analysis of {{company}}'s market based 
on your recent job postings and funding announcement.

Looks like you're hiring 3 new SDRs this quarter. At $75K 
salary each, that's $225K in new headcount.

What if you could get the same output with 2 SDRs instead of 3 
by automating their prospecting? That's $75K saved, plus faster 
time-to-productivity.

Here's a 1-page ROI calculator I built for companies your size: 
[link]

Worth exploring?

Best,
{{your_name}}
```

**Send timing:** 7 days after Email 1 if no response

---

**EMAIL 4: Social Proof (Day 10)**

**Subject:** 47 B2B SaaS companies are using this

**Body:**
```
{{first_name}},

Quick update: We just hit a milestone - 47 B2B SaaS companies 
(including 12 in your space) are now using our platform.

The common thread? They all had the same problem you might be 
facing:
- Sales team spending too much time on research
- Inconsistent lead quality
- Slow ramp time for new reps

Average results after 90 days:
• 18 hours/week saved per rep
• 2.5x more qualified leads
• 35% faster ramp for new hires

I'm not sure if this is a priority for {{company}} right now, 
but if it is, I'd love to show you how companies like 
[Competitor 1] and [Competitor 2] are using it.

15 minutes this week?

Best,
{{your_name}}
```

**Send timing:** 10 days after Email 1 if no response

---

**EMAIL 5: Breakup (Day 14)**

**Subject:** Should I close your file?

**Body:**
```
{{first_name}},

I've reached out a few times about helping {{company}} automate 
prospecting and save your team 15+ hours/week.

Haven't heard back, so I'm assuming either:
a) Not a priority right now
b) Wrong timing
c) I'm reaching the wrong person

No worries if it's not a fit! I'll close your file unless I 
hear otherwise.

If I am barking up the wrong tree, who should I talk to about 
sales productivity and automation?

Either way, best of luck scaling the team!

Best,
{{your_name}}

P.S. If timing changes, here's our calendar: [link]
```

**Send timing:** 14 days after Email 1 if no response

---

### Step 4: Customize and Personalize (10-15 minutes)

Add your specific details:

**Replace placeholders:**
- {{company}} → Prospect's company name
- {{first_name}} → Prospect's first name
- {{your_name}} → Your name
- [Customer 1], [Customer 2] → Real customer names
- [link] → Actual links

**Add personalization:**
- Recent funding news
- Job postings
- LinkedIn activity
- Company growth signals
- Mutual connections

**Customize for persona:**
- Adjust pain points
- Change metrics
- Update case studies
- Modify tone

### Step 5: Load into Your Email Tool (5 minutes)

**For Outreach.io / SalesLoft:**
1. Create new sequence
2. Copy each email
3. Set send delays (Day 0, 3, 7, 10, 14)
4. Add personalization tokens
5. Enable tracking

**For HubSpot:**
1. Create workflow
2. Add emails as workflow steps
3. Set delays between steps
4. Add enrollment triggers
5. Activate workflow

**For Mailchimp / SendGrid:**
1. Create automation
2. Add emails to sequence
3. Set trigger conditions
4. Configure timing
5. Test and launch

---

## Email Sequence Best Practices

### Subject Lines

**Do:**
- Keep under 50 characters
- Personalize with {{company}} or {{first_name}}
- Ask questions
- Create curiosity
- Use numbers/data

**Don't:**
- Use all caps
- Overuse exclamation points!!!
- Make false promises
- Use spammy words (free, guaranteed, act now)

### Email Body

**Do:**
- Keep under 150 words
- One clear CTA per email
- Use short paragraphs (2-3 lines max)
- Include social proof
- Make it about them, not you

**Don't:**
- Write long paragraphs
- Include multiple CTAs
- Use jargon or buzzwords
- Talk only about your product
- Forget to proofread

### Timing

**Best send times:**
- Tuesday-Thursday
- 8-10 AM or 2-4 PM (recipient's timezone)
- Avoid Mondays and Fridays
- Avoid end of month/quarter

**Sequence spacing:**
- Email 1-2: 2-3 days
- Email 2-3: 3-4 days
- Email 3-4: 3-4 days
- Email 4-5: 4-5 days

---

## A/B Testing Your Sequence

### What to Test

**Subject Lines:**
```
Version A: "Quick question about {{company}}'s sales process"
Version B: "{{first_name}}, 2-minute question"
Version C: "Noticed {{company}} is hiring SDRs"
```

**Opening Lines:**
```
Version A: "I noticed {{company}} recently raised Series A..."
Version B: "Quick question: how much time does your team spend..."
Version C: "Congrats on the Series A! I wanted to reach out because..."
```

**CTAs:**
```
Version A: "Worth a quick 15-minute conversation?"
Version B: "Can I show you a quick demo?"
Version C: "Want to see how this works?"
```

### How to Test

1. Split your list 50/50
2. Test one variable at a time
3. Send to at least 50 people per variation
4. Measure: open rate, reply rate, meeting rate
5. Implement winner, test next variable

---

## Measuring Success

### Key Metrics

**Open Rate:**
- Target: 40-60%
- Improve with: Better subject lines, send timing

**Reply Rate:**
- Target: 5-15%
- Improve with: Better personalization, value prop

**Meeting Booked Rate:**
- Target: 2-5%
- Improve with: Clearer CTA, stronger social proof

**Sequence Completion Rate:**
- Target: 80%+ reach Email 5
- Track: How many prospects see all emails

### Tracking Template

```
Sequence: VP of Sales - Series A SaaS
Sent: 100 prospects

Email 1: 
- Sent: 100
- Opened: 52 (52%)
- Replied: 8 (8%)
- Meetings: 3

Email 2:
- Sent: 92 (8 replied, removed from sequence)
- Opened: 41 (45%)
- Replied: 5 (5%)
- Meetings: 2

Email 3:
- Sent: 87
- Opened: 35 (40%)
- Replied: 4 (5%)
- Meetings: 1

Email 4:
- Sent: 83
- Opened: 28 (34%)
- Replied: 3 (4%)
- Meetings: 1

Email 5:
- Sent: 80
- Opened: 22 (28%)
- Replied: 2 (3%)
- Meetings: 0

Total Results:
- Meetings booked: 7 (7%)
- Total replies: 22 (22%)
- Positive replies: 12 (12%)
```

---

## Common Mistakes to Avoid

### ❌ Too Product-Focused

**Bad:**
```
Our platform has 47 features including AI-powered lead scoring,
automated email sequences, CRM integration, and advanced analytics...
```

**Good:**
```
We help sales teams save 15 hours/week on prospecting so they can
focus on actually selling.
```

### ❌ No Personalization

**Bad:**
```
Hi there,

I wanted to reach out to companies in your industry...
```

**Good:**
```
Hi Sarah,

I noticed Acme Corp just raised Series A and is hiring 3 new SDRs...
```

### ❌ Weak CTA

**Bad:**
```
Let me know if you'd like to learn more.
```

**Good:**
```
Worth a 15-minute call this Thursday at 2pm?
```

### ❌ Too Long

**Bad:**
8 paragraphs, 400 words, multiple CTAs

**Good:**
3-4 short paragraphs, 100-150 words, one clear CTA

---

## Advanced Techniques

### Trigger-Based Sequences

Start sequence based on:
- Job change
- Funding announcement
- New hire posting
- Product launch
- Competitor mention

### Multi-Channel Approach

Combine email with:
- LinkedIn connection request (Day 1)
- LinkedIn message (Day 5)
- Phone call (Day 8)
- LinkedIn comment on their post (ongoing)

### Video Personalization

Add personalized videos:
- Email 1: Quick intro video
- Email 3: Screen share of their website
- Email 5: Personal message

Tools: Loom, Vidyard, BombBomb

---

## Real User Example

> "I used to spend 2-3 hours writing each cold email sequence, and they all sounded the same. Now I generate a sequence in 5 minutes, customize it for 10-15 minutes, and my reply rates have doubled because the emails are more thoughtful and personalized."
>
> — Jessica L., SDR at TechStart

**Jessica's Results:**
- **Before:** 2.5 hours per sequence, 3% reply rate
- **After:** 30 minutes per sequence, 7% reply rate
- **Time saved:** 2 hours per sequence × 10 sequences/month = 20 hours/month
- **Value:** $1,500/month saved
- **Business impact:** 2.3x more meetings booked

---

## Related Use Cases

- [Generate Qualified Leads](lead-generation-workflow.md)
- [Sales Call Preparation](sales-call-prep.md)
- [LinkedIn Outreach Sequence](linkedin-outreach.md)
- [Re-engagement Campaign](re-engagement-campaign.md)

---

## Resources

- [Email Marketing Plugin Documentation](../plugin-reference.md#email-marketing)
- [Cold Email Templates](../../templates/email-templates.md)
- [Email Copywriting Guide](../business-skills.md#email-copywriting)
- [A/B Testing Framework](../business-skills.md#ab-testing)

---

**Questions?** [Ask in GitHub Discussions](https://github.com/gtmagents/gtm-agents/discussions)

**Found this helpful?** [Support the project ☕](https://buymeacoffee.com/gtmagents)
