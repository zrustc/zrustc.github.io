# AI and the God Model English Blog Design

## Goal

Publish a professional English translation of the Chinese essay `../ai-and-god/AI-与上帝模型：大模型的能力边界在哪？.md` as a standalone in-site article page and link to it from `blog.html`.

## Approved Direction

Use the minimal static-site approach:

- create one standalone HTML article page inside the current site
- keep the existing shared header, navigation, stylesheet, and script
- add one real blog entry card on `blog.html` that links to the new article page

The user approved this direction by choosing option A on 2026-03-20.

## Constraints

- Preserve the existing visual language of the site
- Keep the article translation professional and technically precise rather than literal
- Do not introduce a markdown build pipeline or JavaScript rendering dependency
- Do not add math rendering libraries; equations should remain readable with plain HTML

## Page Structure

### New Article Page

Create `blog-ai-and-god-boundary.html` with:

- shared site header and navigation
- article hero with title, status, date, and short deck
- single-column essay body
- section headings matching the source argument structure
- equation blocks formatted as readable preformatted text
- bibliography with outbound links

### Blog Landing Page

Update `blog.html` so the first card becomes a real entry for the new essay with:

- status label
- English title
- short abstract
- direct link to the standalone article page

## Styling

Reuse current layout classes where possible and add only the article-specific styles needed for:

- readable long-form width and spacing
- metadata row
- equation block treatment
- bibliography spacing

## Verification

Add or update tests to confirm:

- `blog.html` links to `blog-ai-and-god-boundary.html`
- the new article page exists
- the article page includes the expected title, shared navigation, and shared script
