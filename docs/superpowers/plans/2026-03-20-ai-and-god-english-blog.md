# AI and the God Model English Blog Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish a standalone English article page for the AI-and-God essay and link it from the site blog landing page.

**Architecture:** Keep the site fully static. Add one hand-authored article HTML page, extend shared CSS only where the long-form article needs dedicated presentation, and update `blog.html` plus tests so the new page is part of the site instead of an external artifact.

**Tech Stack:** Static HTML, shared CSS/JS, Python `unittest`

---

### Task 1: Add failing coverage for the new article integration

**Files:**
- Modify: `tests/test_site_content.py`
- Test: `tests/test_site_content.py`

- [ ] **Step 1: Write the failing test**

Add assertions that:
- `blog.html` links to `blog-ai-and-god-boundary.html`
- `blog-ai-and-god-boundary.html` exists
- the new page contains the expected title, shared nav hook, and shared script

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m unittest tests.test_site_content.SiteStructureTests.test_blog_page_links_to_real_article`
Expected: FAIL because the article file and link do not exist yet

- [ ] **Step 3: Write minimal implementation**

Create the article page and update the blog landing page so the test target exists.

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m unittest tests.test_site_content.SiteStructureTests.test_blog_page_links_to_real_article`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add tests/test_site_content.py blog.html blog-ai-and-god-boundary.html Files/site.css
git commit -m "feat: publish english ai-and-god blog article"
```

### Task 2: Publish the translated article with long-form styling

**Files:**
- Create: `blog-ai-and-god-boundary.html`
- Modify: `Files/site.css`
- Modify: `blog.html`
- Test: `tests/test_site_content.py`

- [ ] **Step 1: Write the failing test**

Ensure the test checks for real article metadata and title text rather than only file existence.

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m unittest tests.test_site_content.SiteStructureTests.test_blog_page_links_to_real_article`
Expected: FAIL until the exact article content is present

- [ ] **Step 3: Write minimal implementation**

Add:
- the professional English translation
- article metadata and bibliography
- minimal article-specific CSS for long-form readability

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m unittest tests.test_site_content.SiteStructureTests.test_blog_page_links_to_real_article`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add tests/test_site_content.py blog.html blog-ai-and-god-boundary.html Files/site.css
git commit -m "style: add long-form blog article presentation"
```

### Task 3: Full-site verification

**Files:**
- Verify: `tests/test_site_content.py`
- Verify: `blog.html`
- Verify: `blog-ai-and-god-boundary.html`
- Verify: `Files/site.css`

- [ ] **Step 1: Run the focused test file**

Run: `python -m unittest tests.test_site_content -v`
Expected: PASS

- [ ] **Step 2: Re-read against the spec**

Check `docs/superpowers/specs/2026-03-20-ai-and-god-english-blog-design.md` and verify that the page is standalone, linked from `blog.html`, and translated professionally.

- [ ] **Step 3: Inspect the final diff**

Run: `git diff -- blog.html blog-ai-and-god-boundary.html Files/site.css tests/test_site_content.py`
Expected: Only the intended article, blog entry, style, and test changes appear

- [ ] **Step 4: Commit**

```bash
git add docs/superpowers/specs/2026-03-20-ai-and-god-english-blog-design.md docs/superpowers/plans/2026-03-20-ai-and-god-english-blog.md tests/test_site_content.py blog.html blog-ai-and-god-boundary.html Files/site.css
git commit -m "docs: record english blog article plan"
```
