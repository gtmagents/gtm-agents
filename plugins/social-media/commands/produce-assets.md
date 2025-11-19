---
name: produce-assets
description: Generates social-first asset briefs and copy variations for a given campaign or content pillar.
usage: /social-media:produce-assets --campaign "AI launch" --platforms "LinkedIn,TikTok" --variants 3
---

# Command: produce-assets

## Inputs
- **campaign** – name or description of the initiative.
- **platforms** – comma-separated list (e.g., LinkedIn, X, TikTok, Instagram).
- **variants** – number of creative variations per platform.
- **assets_available** – optional list of existing raw assets (video, blog, research) to reference.

## Workflow
1. **Signal Review** – pull hooks, proof points, and CTAs from the campaign brief or assets.
2. **Platform Mapping** – tailor narrative approach, tone, and format to each platform’s norms.
3. **Creative Specs** – outline duration, dimensions, editing cues, overlays, captions, hashtags, tracking links.
4. **Variant Generation** – produce requested number of copy/visual options (A/B/C) per platform.
5. **QA** – ensure accessibility (alt text, subtitles), compliance, and brand voice alignment.

## Outputs
- Copy deck with hooks, captions, CTA variants, and metadata tags.
- Asset spec sheet (dimensions, duration, editing guidance, motion suggestions).
- Shot list/storyboard for video-heavy platforms (Reels, TikTok, YouTube Shorts).

## Agent/Skill Invocations
- `content-producer` – leads creative development.
- `platform-frameworks` skill – enforces per-channel requirements.
- `trend-research` skill – infuses current memes/audio/visual cues.

---
