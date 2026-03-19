# Homepage Follow-Up Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Refine the rebuilt site by shortening the homepage hero, surfacing multimodal explicitly, rebalancing homepage representative papers, expanding the publications archive, and adding a minimal first-party blog page.

**Architecture:** Keep the existing static-site architecture. Update shared navigation and styles in place, adjust homepage content structure in `index.html`, expand `publications.html` toward a fuller archive, and add a lightweight `blog.html` that shares the same visual system. Extend the existing `unittest` regression suite to lock each follow-up requirement before implementation.

**Tech Stack:** Static HTML, CSS, minimal vanilla JavaScript, Python 3 `unittest`

---

## File Structure

### Final File Responsibilities

- `index.html`
  Updated homepage hero, split representative papers section, and lightweight `Writing / Notes` entry block.
- `publications.html`
  Fuller year-grouped archive with stronger pre-2024 coverage.
- `blog.html`
  New minimal site-integrated blog landing page with placeholder entries.
- `Files/site.css`
  Shared styling updates for the new hero rhythm, blog page, and any layout adjustments.
- `Files/site.js`
  Shared nav behavior, unchanged in scope except if needed to support the additional nav item safely.
- `tests/test_site_content.py`
  Regression tests for hero copy, representative-paper structure, blog navigation, blog page existence, and fuller publications coverage.

### Notes

- Reuse the current shared visual system; do not do a second full redesign.
- Keep the blog intentionally lightweight in this pass.
- Keep the homepage blog section as an entry point rather than a feed.

### Task 1: Add Follow-Up Regression Coverage

**Files:**
- Modify: `tests/test_site_content.py`
- Test: `tests/test_site_content.py`

- [ ] **Step 1: Write the failing test**

```python
    def test_homepage_hero_uses_short_keyword_headline(self) -> None:
        html = read_text("index.html")
        self.assertIn("LLM Post-Training", html)
        self.assertIn("Multimodal", html)
        self.assertNotIn(
            "Researcher-builder in LLM post-training, reasoning, multilingual, and translation systems.",
            html,
        )

    def test_homepage_selected_work_has_influential_and_recent_groups(self) -> None:
        html = read_text("index.html")
        self.assertIn("Influential", html)
        self.assertIn("Recent", html)
        self.assertIn("Achieving Human Parity on Automatic Chinese to English News Translation", html)
        self.assertIn("Adaptive Nearest Neighbor Machine Translation", html)
        self.assertIn("SWE-AGI", html)

    def test_blog_navigation_and_page_exist(self) -> None:
        for path in ["index.html", "publications.html"]:
            html = read_text(path)
            self.assertIn('href="blog.html"', html)
            self.assertIn(">Blog<", html)
        blog = read_text("blog.html")
        self.assertIn("<title>Blog | Zhirui Zhang</title>", blog)
        self.assertIn('class="site-nav"', blog)
        self.assertIn("data-nav-toggle", blog)
        self.assertIn('src="Files/site.js"', blog)

    def test_publications_page_includes_more_older_work(self) -> None:
        html = read_text("publications.html")
        for year in ["2022", "2021", "2020", "2019", "2018"]:
            self.assertIn(f'data-year="{year}"', html)
        self.assertIn("Task-Oriented Dialogue System as Natural Language Generation", html)
        self.assertIn("Cross-lingual Pre-training Based Transfer for Zero-shot Neural Machine Translation", html)
        self.assertIn("Achieving Human Parity on Automatic Chinese to English News Translation", html)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_site_content -v`
Expected: FAIL because the current homepage still uses the longer hero sentence, does not split representative work into `Influential` and `Recent`, has no `blog.html`, and the publications archive does not yet include enough older translation-heavy work.

- [ ] **Step 3: Write minimal implementation**

```python
# No production changes yet.
# This task only updates the regression suite.
```

- [ ] **Step 4: Run test to verify it still fails for the right reasons**

Run: `python3 -m unittest tests.test_site_content -v`
Expected: FAIL only on the newly added follow-up requirements.

- [ ] **Step 5: Commit**

```bash
git add tests/test_site_content.py
git commit -m "test: add homepage follow-up regression coverage"
```

### Task 2: Shorten Hero And Add Multimodal Framing

**Files:**
- Modify: `index.html`
- Modify: `Files/site.css`
- Test: `tests/test_site_content.py`

- [ ] **Step 1: Keep the failing test in place and re-run it**

Run: `python3 -m unittest tests.test_site_content -v`
Expected: FAIL on hero-copy assertions before implementation.

- [ ] **Step 2: Write minimal implementation**

```html
<section id="hero" class="hero section-block">
  <div class="hero-copy">
    <p class="eyebrow">Zhirui Zhang</p>
    <h1>LLM Post-Training · Reasoning · Multilingual · Multimodal</h1>
    <p class="lede">
      Researcher and builder across large-model systems, translation, multimodal capability, and deployable intelligence.
    </p>
  </div>
</section>
```

```css
.hero h1 {
  max-width: 14ch;
  letter-spacing: -0.02em;
}
```

Adjust hero typography and spacing so the new line reads lighter and cleaner than the previous oversized sentence.

- [ ] **Step 3: Run test to verify it passes**

Run: `python3 -m unittest tests.test_site_content -v`
Expected: Hero-related assertions pass, while later follow-up requirements may still fail.

- [ ] **Step 4: Run a focused visual smoke check**

Run: `python3 -m http.server 8000`
Expected: `http://127.0.0.1:8000/index.html` loads for quick manual inspection of hero rhythm

- [ ] **Step 5: Commit**

```bash
git add index.html Files/site.css
git commit -m "feat: shorten homepage hero and add multimodal framing"
```

### Task 3: Rebalance Homepage Representative Work And Add Blog Entry Block

**Files:**
- Modify: `index.html`
- Modify: `Files/site.css`
- Test: `tests/test_site_content.py`

- [ ] **Step 1: Keep the representative-work and blog-entry tests failing**

Run: `python3 -m unittest tests.test_site_content -v`
Expected: FAIL on missing `Influential`/`Recent` grouping and missing homepage blog entry behavior.

- [ ] **Step 2: Write minimal implementation**

```html
<section id="selected-work" class="section-block">
  <p class="section-label">Selected Work</p>
  <h2>Representative Papers</h2>
  <div class="selected-work-grid">
    <div>
      <h3>Influential</h3>
      <ul class="paper-group">
        <li>Achieving Human Parity on Automatic Chinese to English News Translation</li>
        <li>Document-Level Machine Translation with Large Language Models</li>
        <li>Adaptive Nearest Neighbor Machine Translation</li>
      </ul>
    </div>
    <div>
      <h3>Recent</h3>
      <ul class="paper-group">
        <li>SWE-AGI</li>
        <li>Is PRM Necessary?</li>
        <li>Safe Delta</li>
      </ul>
    </div>
  </div>
</section>

<section id="writing-notes" class="section-block writing-notes">
  <p class="section-label">Writing / Notes</p>
  <h2>Occasional notes on models, translation, and building systems.</h2>
  <a class="secondary-link" href="blog.html">Visit Blog</a>
</section>
```

Finish the influential group with the approved translation-heavy representative set:

- Achieving Human Parity on Automatic Chinese to English News Translation
- Document-Level Machine Translation with Large Language Models
- Adaptive Nearest Neighbor Machine Translation
- Regularizing Neural Machine Translation by Target-bidirectional Agreement
- Incorporating BERT into Parallel Sequence Decoding with Adapters
- Simple and Scalable Nearest Neighbor Machine Translation

Finish the recent group with:

- SWE-AGI
- Is PRM Necessary?
- Safe Delta
- Simple o3
- Lost in the Source Language

- [ ] **Step 3: Run test to verify it passes**

Run: `python3 -m unittest tests.test_site_content -v`
Expected: Homepage representative-work assertions pass, while `blog.html` and fuller publication coverage may still fail.

- [ ] **Step 4: Run a focused visual smoke check**

Run: `python3 -m http.server 8000`
Expected: `http://127.0.0.1:8000/index.html` loads with balanced two-group paper block and understated blog entry area

- [ ] **Step 5: Commit**

```bash
git add index.html Files/site.css
git commit -m "feat: rebalance homepage representative work"
```

### Task 4: Expand Publications Archive Coverage

**Files:**
- Modify: `publications.html`
- Modify: `Files/site.css`
- Test: `tests/test_site_content.py`

- [ ] **Step 1: Re-run tests to keep publications follow-up assertions red**

Run: `python3 -m unittest tests.test_site_content -v`
Expected: FAIL on older-work coverage if not yet added.

- [ ] **Step 2: Write minimal implementation**

```html
<section class="pub-year-group section-block" data-year="2022">
  <p class="section-label">2022</p>
  <div class="pub-entry">
    <h2>Task-Oriented Dialogue System as Natural Language Generation</h2>
  </div>
</section>

<section class="pub-year-group section-block" data-year="2020">
  <p class="section-label">2020</p>
  <div class="pub-entry">
    <h2>Cross-lingual Pre-training Based Transfer for Zero-shot Neural Machine Translation</h2>
  </div>
</section>

<section class="pub-year-group section-block" data-year="2018">
  <p class="section-label">2018</p>
  <div class="pub-entry">
    <h2>Achieving Human Parity on Automatic Chinese to English News Translation</h2>
  </div>
</section>
```

Then extend the archive with materially fuller older coverage, explicitly adding visible year sections for 2022, 2021, 2020, 2019, and 2018.

Minimum coverage target:

- keep the current 2024-2026 material
- retain the current 2023 material
- add clearly visible older representative papers from at least 2022, 2021, 2020, 2019, and 2018

Minimum older-year anchors:

- 2022:
  - Task-Oriented Dialogue System as Natural Language Generation
- 2021:
  - Adaptive Nearest Neighbor Machine Translation
- 2020:
  - Cross-lingual Pre-training Based Transfer for Zero-shot Neural Machine Translation
- 2019:
  - Regularizing Neural Machine Translation by Target-bidirectional Agreement
- 2018:
  - Achieving Human Parity on Automatic Chinese to English News Translation

Preserve authors, venue/year metadata, and resource links where they are already available or easy to source.

- [ ] **Step 3: Run test to verify it passes**

Run: `python3 -m unittest tests.test_site_content -v`
Expected: Publications coverage assertions pass.

- [ ] **Step 4: Run a focused visual smoke check**

Run: `python3 -m http.server 8000`
Expected: `http://127.0.0.1:8000/publications.html` loads with fuller archive coverage and readable year-group structure

- [ ] **Step 5: Commit**

```bash
git add publications.html Files/site.css
git commit -m "feat: expand publications archive coverage"
```

### Task 5: Add Minimal Blog Page And Shared Navigation Entry

**Files:**
- Create: `blog.html`
- Modify: `index.html`
- Modify: `publications.html`
- Modify: `Files/site.css`
- Modify: `Files/site.js`
- Test: `tests/test_site_content.py`

- [ ] **Step 1: Re-run tests to keep blog assertions red**

Run: `python3 -m unittest tests.test_site_content -v`
Expected: FAIL on missing `blog.html` and missing shared `Blog` navigation entry.

- [ ] **Step 2: Write minimal implementation**

```html
<!-- blog.html -->
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Blog | Zhirui Zhang</title>
  <link rel="stylesheet" href="Files/site.css">
</head>
<body>
  <header class="site-header">...</header>
  <main class="page-shell publications-shell">
    <section class="section-block pub-hero">
      <p class="section-label">Blog</p>
      <h1 class="page-title">Writing / Notes</h1>
      <p class="lede">Notes on models, translation, systems, and research in progress.</p>
    </section>
  </main>
  <script src="Files/site.js"></script>
</body>
</html>
```

Add `Blog` to shared navigation in `index.html` and `publications.html`.

Complete the blog page with:

- shared nav
- one short intro
- 1-2 placeholder cards or a clean coming-soon structure
- styling integrated with the existing palette and card system

Only touch `Files/site.js` if the additional nav item requires a safe adjustment; otherwise keep JS scope minimal.

- [ ] **Step 3: Run test to verify it passes**

Run: `python3 -m unittest tests.test_site_content -v`
Expected: All follow-up tests pass.

- [ ] **Step 4: Run a final local static smoke test**

Run: `python3 -m http.server 8000`
Expected:
- `http://127.0.0.1:8000/index.html` returns 200
- `http://127.0.0.1:8000/publications.html` returns 200
- `http://127.0.0.1:8000/blog.html` returns 200

- [ ] **Step 5: Commit**

```bash
git add blog.html index.html publications.html Files/site.css Files/site.js
git commit -m "feat: add minimal blog page"
```

### Task 6: Final Verification

**Files:**
- Test: `tests/test_site_content.py`

- [ ] **Step 1: Run the targeted follow-up suite**

Run: `python3 -m unittest tests.test_site_content -v`
Expected: PASS

- [ ] **Step 2: Run the full suite**

Run: `python3 -m unittest -v`
Expected: PASS

- [ ] **Step 3: Manual spot check**

Run: `python3 -m http.server 8000`
Expected:
- homepage hero is shorter and lighter
- homepage representative papers are split into `Influential` and `Recent`
- homepage has a small `Writing / Notes` entry
- publications page feels materially fuller
- blog page exists and looks integrated

- [ ] **Step 4: Confirm clean git state**

Run: `git status --short`
Expected: empty output

- [ ] **Step 5: Commit**

```bash
# No new commit if already clean and all previous tasks committed.
```
