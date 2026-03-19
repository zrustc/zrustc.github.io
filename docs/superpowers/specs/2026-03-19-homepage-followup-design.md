# Homepage Follow-Up Design

**Date:** 2026-03-19

## Summary

This follow-up design refines the newly rebuilt personal site in four areas:

- shorten the homepage hero headline
- explicitly include multimodal work in the top-level framing
- strengthen homepage representative papers with more translation-heavy influential work
- expand `publications.html` toward a fuller academic archive
- add a minimal first-party `blog.html` page as a future writing entry point

## Why This Follow-Up Exists

The first redesign successfully modernized the site, but the current homepage still has several issues:

- the hero headline is visually too long and heavy
- multimodal work is not visible enough in the top-level identity
- homepage representative papers skew too much toward recent work
- translation-related influential work is underrepresented
- the publications page feels more like a partial curated archive than a fuller academic record
- there is not yet a first-party blog entry point

## Goals

- Replace the long hero sentence with shorter keyword-like framing
- Explicitly surface multimodal capability building in the homepage identity
- Rebalance homepage representative work so it reflects both long-term translation depth and recent LLM work
- Expand `publications.html` with more complete year-grouped coverage, especially before 2024
- Add a minimal but real `blog.html` page that can grow later
- Add a light homepage `Writing / Notes` entry section without competing with the research narrative

## Non-Goals

- Do not build a full CMS or article engine
- Do not add search, tags, RSS, or markdown rendering for blog posts in this pass
- Do not turn the homepage into a content-heavy portal
- Do not redesign the entire visual system again

## Homepage Changes

### Hero

Replace the current main hero line with:

`LLM Post-Training · Reasoning · Multilingual · Multimodal`

Replace the current hero sub-line with a shorter supporting sentence along the lines of:

`Researcher and builder across large-model systems, translation, multimodal capability, and deployable intelligence.`

Requirements:

- main line must remain short and keyword-like
- hero should feel visually lighter than the current version
- multimodal must be explicit in the top layer

### Representative Papers On Homepage

The homepage paper block should be restructured into two groups:

- `Influential`
- `Recent`

#### Influential

This group should include stronger translation-centered representative work and high-signal papers such as:

- Achieving Human Parity on Automatic Chinese to English News Translation
- Document-Level Machine Translation with Large Language Models
- Adaptive Nearest Neighbor Machine Translation
- Regularizing Neural Machine Translation by Target-bidirectional Agreement
- Incorporating BERT into Parallel Sequence Decoding with Adapters
- Simple and Scalable Nearest Neighbor Machine Translation

Optional substitutions if layout pressure requires a swap:

- Cross-lingual Pre-training Based Transfer for Zero-shot Neural Machine Translation
- Rethinking Translation Memory Augmented Neural Machine Translation

#### Recent

This group should retain recent work such as:

- SWE-AGI
- Is PRM Necessary?
- Safe Delta
- Simple o3
- Lost in the Source Language

Requirements:

- homepage representative work must visibly preserve the translation research line
- the section should feel more balanced between influence and recency
- the visual structure should remain concise enough for a homepage

### Homepage Blog Entry

Add a small homepage section near the lower part of the page:

- section label: `Writing / Notes` or similar
- one short sentence describing future writing
- one clear link to `blog.html`

Requirements:

- the section should be understated
- it should act as an entry point, not a dominant homepage block

## Publications Page Changes

`publications.html` should move closer to a fuller academic archive.

Requirements:

- keep year-grouped layout
- preserve the cleaner modern presentation
- add more older important papers, especially in MT, NMT, speech translation, and dialogue
- cover the broader publication history better than the current version

The page does not need to include every single possible entry from Scholar if layout or effort becomes unreasonable, but it must no longer feel like only a partial recent selection.

Implementation may use the old homepage publication list and Scholar data together, with Scholar remaining the source of truth for metadata formatting when conflicts arise.

## Blog Page Changes

Create a minimal `blog.html`.

Requirements:

- include shared site navigation
- include page title and short intro
- include a short description such as writing about models, translation, systems, or research notes
- include 1-2 placeholder post cards or a clearly designed coming-soon structure
- be visually integrated with the rest of the site

This page is a framework for future growth, not a full publishing system.

## Navigation Changes

Add `Blog` to shared navigation.

Requirements:

- visible on homepage and publications page
- links to `blog.html`
- mobile navigation continues to work

## Acceptance Criteria

This follow-up is ready when:

- homepage hero is shorter and includes multimodal explicitly
- homepage representative work is split into `Influential` and `Recent`
- translation-related influential work is clearly present
- publications page is materially more complete than the current version
- `blog.html` exists as a minimal integrated page
- homepage includes a lightweight blog entry section
