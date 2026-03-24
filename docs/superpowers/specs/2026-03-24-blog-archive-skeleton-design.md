# Blog Archive Skeleton Design

## Goal

Refactor `blog.html` from a minimal landing page into a reusable in-site blog archive skeleton, while keeping the site static and lightweight.

The archive should support future posts without requiring another structural redesign, but should not introduce filtering, search, pagination, or a content pipeline at this stage.

## Scope

### In Scope

- turn `blog.html` into a formal archive page
- preserve the current standalone article page `blog-ai-and-god-boundary.html`
- represent archive metadata using four dimensions:
  - `Year`
  - `Format`
  - `Topic`
  - `Count`
- present posts as article cards grouped by year
- keep the implementation static and hand-authored
- add tests that assert the archive structure and first post metadata

### Out of Scope

- archive filters
- search
- pagination
- multiple article migration
- markdown/MDX pipeline
- content management system
- auto-generated metadata

## Approved Direction

The user approved a “Formal Archive” direction with:

- article cards as the main archive unit
- a dedicated archive metadata area
- a reusable skeleton optimized for future additions

The user explicitly chose:

- visual direction: `article cards + archive metadata`
- metadata dimensions: `Year / Format / Topic / Count`

## Information Architecture

`blog.html` becomes a two-zone archive page:

### 1. Archive Meta

A stable summary rail that aggregates archive-level information.

It displays:

- `Year`
- `Format`
- `Topic`
- `Count`

This section is descriptive, not interactive. It communicates the shape of the archive, not a filtering system.

### 2. Archive List

A year-grouped list of article cards.

Current state:

- one year group: `2026`
- one article card: `AI and the God Model`

Future state:

- additional posts are added by repeating the same card structure inside the corresponding year group
- the archive metadata rail is updated as counts and tags evolve

## Metadata Rules

The four metadata dimensions are intentionally distinct:

### Year

- single value
- publication year
- used for archive grouping and archive summary

Example:

- `2026`

### Format

- single value
- describes the content type of a post
- should remain a primary type, not a multi-tag field

Initial examples:

- `Essay`
- `Note`
- `Translation`
- `Reading`
- `Project`

Current article:

- `Essay`

### Topic

- multi-tag field
- recommended range: 1 to 3 tags per post
- describes subject matter, not content type

Initial examples:

- `Models`
- `Reasoning`
- `Systems`
- `Translation`
- `Multimodal`
- `Evaluation`

Current article:

- `Models`
- `Reasoning`
- `Systems`

### Count

- archive-level summary only
- not stored as a post-level tag
- expresses the current archive footprint

Current examples:

- `1 post`
- `1 essay`
- `3 topics`

## Card Structure

Each archive card should expose a fixed set of fields so future additions stay consistent:

- title
- one-sentence abstract
- format
- topic tags
- publication date
- article link

Current card instance:

- title: `AI and the God Model`
- abstract: one-sentence summary of the essay
- format: `Essay`
- topics: `Models`, `Reasoning`, `Systems`
- date: `March 20, 2026`
- link target: `blog-ai-and-god-boundary.html`

## Visual Design

The page should remain aligned with the existing site language:

- same header and navigation
- same typography family and general palette
- article cards remain the primary visual unit
- archive metadata uses a quieter supporting treatment
- layout should feel more formal than the current two-card placeholder page, but not like a dashboard

Recommended layout:

- left column: archive metadata
- right column: year-grouped article cards

On smaller screens:

- stack metadata above the archive list

## Implementation Boundaries

### Files Expected to Change

- `blog.html`
- `Files/site.css`
- `tests/test_site_content.py`

### Files Expected to Stay As-Is

- `blog-ai-and-god-boundary.html` content
- existing homepage and publications structure

## Testing

Tests should assert:

- `blog.html` contains a dedicated archive metadata section
- `blog.html` contains a year-grouped archive list
- `blog.html` includes the approved metadata values for the current post and archive summary
- the article card still links to `blog-ai-and-god-boundary.html`
- shared navigation and script hooks remain present

## Success Criteria

This work is successful if:

- the blog page reads as a real archive instead of a placeholder
- the archive metadata dimensions are visible and clearly separated by purpose
- the first article is represented through the reusable archive card structure
- adding a second or third post later only requires copying the card pattern and updating archive summary values
- the site remains static, lightweight, and test-covered
