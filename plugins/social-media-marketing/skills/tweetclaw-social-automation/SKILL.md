---
name: tweetclaw-social-automation
description: Use when executing X/Twitter research, posting, reply, follower export, monitoring, or giveaway workflows through TweetClaw and Xquik.
license: Apache-2.0
compatibility: Claude Code, OpenClaw
metadata:
  author: gtmagents
  version: "1.0"
  category: marketing
---

# TweetClaw Social Automation Skill

## When to Use
- Running X/Twitter workflows where the agent can access TweetClaw or the `@xquik/tweetclaw` OpenClaw plugin.
- Searching tweets, searching tweet replies, exporting followers, or monitoring brand and competitor mentions.
- Drafting and approving post tweets, post tweet replies, giveaway draws, or creator outreach follow-ups.

## Framework
1. **Access Check** - confirm the agent has TweetClaw access, identify whether the run is API key mode or MPP read-only mode, and verify the target account or keyword set.
2. **Research Pass** - use read-only flows first: search tweets, search tweet replies, user lookup, follower research, and audience signal collection before proposing actions.
3. **Approval Gate** - present the exact post text, reply text, monitor scope, extraction scope, or giveaway rules before any visible or paid action.
4. **Execution Path** - run the approved TweetClaw action, capture returned IDs, links, or exported artifacts, and note any rate-limit or policy constraints.
5. **Reporting Loop** - summarize what happened, what changed, what to monitor next, and what follow-up asset or reply should be prepared.

## Templates
- **Launch Listening Brief** - keyword set, competitor handles, date window, top themes, top objections, reply opportunities.
- **Posting Approval Sheet** - account, final text, media list, CTA, approval owner, success metric.
- **Monitor Setup Sheet** - target handles or keywords, event types, alert priority, response owner, escalation path.
- **Giveaway Draw Checklist** - source tweet, eligibility rules, exclusion rules, draw window, exported entrant file, winner confirmation notes.

## Tips
- Use TweetClaw for concrete jobs users actually ask for: search tweets, search tweet replies, post tweets, post tweet replies, follower export, user lookup, media upload, media download, direct messages, monitor tweets, webhooks, and giveaway draws.
- MPP mode only covers 31 read-only endpoints. Posts, replies, follows, DMs, monitors, webhooks, uploads, and giveaway operations require API key mode.
- Keep writes approval-gated and scope-limited. Bulk follow, bulk DM, and spammy engagement loops are out of bounds.
- For launch and community work, start with conversation mining first, then move to replies or posts after approval.
- Record tweet URLs, user IDs, monitor IDs, exported files, and next actions so the marketing team can reuse the output.

---
