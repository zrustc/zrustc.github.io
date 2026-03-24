# Blog Archive Skeleton Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn `blog.html` into a reusable archive page with archive metadata and year-grouped article cards while preserving the current standalone article page.

**Architecture:** Keep the site fully static. Rework `blog.html` into a two-zone archive layout, extend `Files/site.css` with archive-specific presentation classes, and strengthen `tests/test_site_content.py` so the archive structure is asserted directly. The article page remains the content endpoint; the archive page becomes the navigational index.

**Tech Stack:** Static HTML, shared CSS, shared site JS, Python `unittest`

---

### Task 1: Add failing coverage for archive structure

**Files:**
- Modify: `tests/test_site_content.py`
- Test: `tests/test_site_content.py`

- [ ] **Step 1: Write the failing test**

Add a focused archive test that asserts:
- `blog.html` contains a dedicated archive metadata section
- `blog.html` contains a year-grouped archive list for `2026`
- the archive includes `Essay`, `Models`, `Reasoning`, `Systems`, and `1 post`
- the article card still links to `blog-ai-and-god-boundary.html`

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_site_content.SiteStructureTests.test_blog_archive_exposes_metadata_and_year_group -v`
Expected: FAIL because the current `blog.html` is still a minimal placeholder layout

- [ ] **Step 3: Write minimal implementation**

Update `blog.html` just enough to expose the new archive structure and metadata markers.

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests.test_site_content.SiteStructureTests.test_blog_archive_exposes_metadata_and_year_group -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add tests/test_site_content.py blog.html
git commit -m "feat: add blog archive skeleton structure"
```

### Task 2: Add archive-specific presentation styles

**Files:**
- Modify: `Files/site.css`
- Modify: `blog.html`
- Test: `tests/test_site_content.py`

- [ ] **Step 1: Write the failing test**

Strengthen the archive test so it also checks for the final archive fields rendered in the card and summary layout.

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_site_content.SiteStructureTests.test_blog_archive_exposes_metadata_and_year_group -v`
Expected: FAIL until the final archive content is fully represented

- [ ] **Step 3: Write minimal implementation**

Add archive layout and card styles in `Files/site.css` and finish the archive markup in `blog.html`:
- left metadata rail
- right year-grouped list
- article card metadata row and topic tags

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests.test_site_content.SiteStructureTests.test_blog_archive_exposes_metadata_and_year_group -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add Files/site.css blog.html tests/test_site_content.py
git commit -m "style: add formal blog archive presentation"
```

### Task 3: Full verification

**Files:**
- Verify: `blog.html`
- Verify: `Files/site.css`
- Verify: `tests/test_site_content.py`
- Reference: `docs/superpowers/specs/2026-03-24-blog-archive-skeleton-design.md`

- [ ] **Step 1: Run the full site test suite**

Run: `python3 -m unittest tests.test_site_content -v`
Expected: PASS

- [ ] **Step 2: Verify implementation against the spec**

Check:
- archive meta exists and is descriptive, not interactive
- archive list is grouped under `2026`
- the existing article remains the first card
- no filtering, search, or pagination was introduced

- [ ] **Step 3: Inspect final diff**

Run: `git diff -- blog.html Files/site.css tests/test_site_content.py docs/superpowers/specs/2026-03-24-blog-archive-skeleton-design.md docs/superpowers/plans/2026-03-24-blog-archive-skeleton.md`
Expected: Only archive structure, styling, test, and planning changes appear

- [ ] **Step 4: Commit**

```bash
git add blog.html Files/site.css tests/test_site_content.py docs/superpowers/specs/2026-03-24-blog-archive-skeleton-design.md docs/superpowers/plans/2026-03-24-blog-archive-skeleton.md
git commit -m "docs: record blog archive skeleton plan"
```
