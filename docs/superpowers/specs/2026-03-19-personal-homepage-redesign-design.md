# Personal Homepage Redesign Design

**Date:** 2026-03-19

## Summary

Redesign the existing static personal website into a more polished English-language academic homepage with a dedicated publications page. The new site should reflect the latest information from `resume_zhirui/zhirui_20260319.tex` and the current public Google Scholar profile for Zhirui Zhang. The presentation should be research-first, academically credible, and visually more distinctive, with restrained geek-oriented interface details rather than flashy effects.

## Goals

- Replace the old single-file, legacy-style homepage with a more intentional and modern static site.
- Rewrite the homepage content in English based on the latest resume and current Scholar profile rather than preserving the old wording.
- Present Zhirui Zhang primarily as a long-horizon researcher-builder across LLM post-training, reasoning, multilingual, and translation.
- Keep the homepage concise and high-signal while moving the broader publication archive to a separate publications page.
- Improve typography, layout, spacing, and visual hierarchy so the site feels more premium and current.
- Add a light geek layer through layout structure, metadata chips, metrics, subtle grids, and technical micro-labels.
- Preserve simple static-site hosting compatibility for GitHub Pages or equivalent static hosting.

## Non-Goals

- Do not build a complex client-side application or introduce a framework migration unless strictly needed.
- Do not create a separate long-form experience page.
- Do not make the site terminal-heavy, neon-heavy, or visually noisy.
- Do not attempt to mirror the entire Google Scholar experience on-site.
- Do not make the homepage a literal translation of the previous site or the Chinese resume.

## Source Material

### Required Sources

- Local resume source: `resume_zhirui/zhirui_20260319.tex`
- Public Google Scholar profile: `https://scholar.google.com/citations?user=C8Ylo7sAAAAJ&hl=en`

### Key Data To Incorporate

- Latest short professional narrative derived from the resume summary
- Updated career timeline, including:
  - IDEA Research
  - Huawei
  - StepFun
  - Tencent AI Lab
  - Alibaba DAMO Academy
  - Microsoft Research
- Representative recent publications from 2024-2026
- Scholar metrics currently visible on the public profile:
  - Citations: 2908
  - h-index: 25
  - i10-index: 38
- Public research tags currently visible on Scholar:
  - Deep Learning
  - Large Language Model
  - World Model

## Chosen Product Direction

The chosen direction is:

- Research-first
- Multi-page
- Homepage plus publications page
- Resume remains download-first
- Experience remains concise
- Broader publication archive belongs on the publications page

## Information Architecture

### Page 1: Homepage

The homepage is the narrative front page. It should answer:

- Who is Zhirui Zhang?
- What research areas define his current profile?
- What recent work best represents him?
- Where can visitors go next for papers, resume, and external profiles?

The homepage should include:

1. Hero section
2. Short rewritten bio
3. Research focus areas
4. Selected publications or selected recent works
5. Concise experience timeline
6. Academic service and selected awards
7. Contact and quick links

### Page 2: Publications

The publications page is the durable archive. It should contain the broader paper list grouped by year, with cleaner formatting and better scanability than the existing homepage.

The publications page should include:

- Intro header with quick links back to home, Scholar, and resume
- Publication list grouped by year
- Entries with title, authors, venue, and year
- Optional resource links when available, such as PDF or code

### Resume Access

Resume should not become its own rich HTML page. The homepage should instead expose a prominent resume download/view link. If hosting requires an intermediate file page, it should remain minimal.

## Content Strategy

### Homepage Narrative

The homepage should lead with research identity first and current role second.

The core framing should position Zhirui Zhang as:

- A researcher-builder working on LLM post-training
- A contributor to reasoning models and production-facing model capabilities
- A researcher with sustained depth in multilingual, translation, and multimodal systems
- Someone whose work spans both frontier model research and product deployment

### Bio Rewrite

The new English bio should be rewritten from the latest resume rather than translated mechanically. It should emphasize:

- LLM post-training
- Reasoning models
- Multilingual and multimodal capability building
- Production and deployment experience
- Strong publication record

The tone should be professional, compact, and current.

### Experience Section

Experience should remain concise on the homepage. Each role should use:

- Organization
- Location if useful
- Date range
- One-line or short two-line summary

Long impact bullets from the resume should not be fully copied onto the homepage.

### Publications Strategy

Homepage publications should be curated and selective, biased toward:

- Recent papers
- Papers aligned with the current research identity
- High-signal work across LLMs, reasoning, multilingual capability, and translation

The publications page should then carry the broader archive, including recent 2024-2026 papers and earlier representative work.

## Visual Design Direction

### Core Style

The site should feel like:

- A modern academic monograph
- Clean and editorial
- Slightly research-lab flavored
- Distinctive without being loud

### Color Direction

The palette should be inspired by the reference site `https://liyuanlucasliu.github.io/`, but adapted to fit this site’s calmer tone.

Primary palette:

- Deep navy: `#13294B`
- Coral accent: `#E94A36`
- Pale blue section tone: `#EAF2FA`
- Warm light-gray section tone: `#F4F4F2`

Recommended usage:

- Navy for top navigation, structural accents, labels, and high-contrast UI anchors
- Coral for links, buttons, highlights, and active states
- Pale blue for hero or major highlight sections
- Warm light-gray for reading blocks and alternating section backgrounds

### Typography

Typography should prioritize readability and editorial polish.

Rules:

- Headings may use a more expressive serif or semi-serif direction
- Body copy should use a clean, readable sans-serif
- Monospace should be used sparingly for technical labels, chips, metrics, and small metadata accents

### Geek Layer

The geek flavor should come from:

- Metric chips
- Publication tags
- Structural dividers
- Subtle grid or instrumentation-like details
- Small technical labels

It should not come from:

- Heavy terminal imitation
- Neon cyberpunk styling
- Dense code windows
- Over-animated backgrounds

### Motion

Motion should be restrained:

- Gentle section reveal
- Hover elevation or highlight
- Possibly light background drift or texture movement

Avoid animation that distracts from reading.

## Layout Design

### Homepage Layout

Desktop layout should be reading-first with a strong two-column rhythm:

- Main column for narrative content
- Secondary rail or sidebar for metrics, links, and quick facts

Mobile layout should collapse cleanly into a single-column sequence without losing hierarchy.

### Publications Layout

The publications page should favor scanability over novelty:

- Clear year separators
- Consistent entry rhythm
- Compact metadata styling
- Better whitespace than the existing page

## Technical Direction

The site should remain a static site that can be served directly from the repository.

Implementation should likely:

- Replace or substantially rewrite the current `index.html`
- Add a dedicated publications page
- Update or replace the old CSS approach
- Continue using local static assets where appropriate

There is no requirement to retain the old `jemdoc` visual structure.

## Page-Level Requirements

### Homepage Must Include

- Name and English primary identity
- Current focus statement
- Short bio
- Research areas
- Selected recent work
- Concise experience
- Academic service and/or awards
- Contact links
- Google Scholar link
- GitHub link
- Resume link
- Updated Scholar metrics

### Publications Page Must Include

- Fuller publication archive grouped by year
- Recent 2024-2026 papers included
- Older major papers retained
- Clear title-first formatting
- Optional paper resource links where available

## Responsiveness

The design must work well on:

- Desktop
- Tablet
- Mobile

Special care should be taken with:

- Navigation collapse
- Sidebar behavior
- Publication entry wrapping
- Long paper titles

## Tone And Copy Principles

- English-only primary presentation
- Professional and current
- More mature than the old homepage
- More selective and intentional than a CV dump
- More polished and readable than a raw paper list

## Out Of Scope For This Redesign

- Blog overhaul
- Dynamic search system
- Auto-sync with Scholar
- Dark mode unless it falls out cheaply from the chosen style system
- Complex filtering UI for publications

## Acceptance Criteria

The redesign is ready for planning when:

- The homepage and publications page structure are fully defined
- Visual direction is specific enough to implement without guessing
- Content boundaries are clear between homepage and publications
- Resume behavior is clear as download-first
- Latest resume and Scholar data requirements are explicitly represented
- The design remains implementable as a static website in this repository

## Implementation Notes For Planning

- Existing assets such as profile image and favicon may be reused if still appropriate
- The old site content should be treated as legacy source material, not as a structure to preserve
- The planner should decide the minimal file structure needed to implement the redesign cleanly
