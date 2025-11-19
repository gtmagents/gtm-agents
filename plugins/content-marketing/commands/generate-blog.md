---
name: generate-blog
description: Produce SEO-optimized blog drafts aligned with brand messaging and target keywords.
usage: /content-marketing:generate-blog --topic "AI in GTM" --persona "CMO" --keyword "ai marketing strategy"
---

# Generate Blog Command

## Purpose
Create long-form blog content that balances SEO intent, persona pain points, and GTM storytelling.

## Syntax
```bash
/content-marketing:generate-blog \
  --topic "<working title>" \
  --persona "<target role>" \
  --keyword "<primary keyword>" \
  --length 1200 \
  --tone "authoritative"
```

### Parameters
- `--topic`: Core subject or angle for the post.
- `--persona`: Reader profile (CMO, Demand Gen Lead, Founder).
- `--keyword`: Primary keyword to optimize for.
- `--length`: Target word count (default 1200).
- `--tone`: voice (authoritative, conversational, visionary).
- `--cta`: Desired call-to-action (demo, download, subscribe).

## Output Package
- SEO brief (H1/H2 structure, keyword usage, meta data).
- Draft article in Markdown with intro → body → CTA.
- Pull quotes, tweet thread, LinkedIn caption suggestions.
- Repurposing ideas (podcast segment, newsletter blurb, short video script).

## Best Practices
- Map subheadings to buyer journey stages.
- Include statistics or quotes every ~300 words for credibility.
- Add internal/external links (3 each minimum).
- End with CTA tied to campaign objective.

---
