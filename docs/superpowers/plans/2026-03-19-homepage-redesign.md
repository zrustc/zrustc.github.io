# Homepage Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild the personal site into a research-first English homepage with a dedicated publications page, updated resume download, and refreshed content from the latest resume and Scholar data.

**Architecture:** Keep the repo as a simple static website. Rewrite the legacy homepage into semantic HTML, add a separate `publications.html` archive page, and centralize styling/behavior in shared static assets under `Files/`. Add a small `unittest`-based regression suite so the redesign can be implemented with TDD despite the repo having no framework.

**Tech Stack:** Static HTML, CSS, minimal vanilla JavaScript, Python 3 `unittest`

---

## File Structure

### Final File Responsibilities

- `index.html`
  Homepage with hero, bio, research areas, selected work, concise experience, service/awards, and contact/metrics rail.
- `publications.html`
  Dedicated year-grouped publication archive page.
- `Files/site.css`
  Shared visual system, layout, responsive styles, and palette variables.
- `Files/site.js`
  Minimal interaction layer for mobile navigation, active section highlighting, and any light polish that survives without a framework.
- `Files/zhirui_20260319.pdf`
  Repo-local resume asset used by the download-first resume link.
- `tests/__init__.py`
  Makes the `tests` directory importable by `unittest`.
- `tests/test_site_content.py`
  Regression tests for required pages, key sections, local resume link, palette variables, and publication-year coverage.
- `_config.yml`
  Optional metadata cleanup to match the redesigned site title/description.

### Notes

- Keep `Files/me.jpg` and existing favicon assets unless a better local asset is intentionally substituted.
- Do not preserve the old `jemdoc.css` structure; treat it as legacy and stop linking it from the new homepage.

### Task 1: Add Regression Test Harness

**Files:**
- Create: `tests/__init__.py`
- Create: `tests/test_site_content.py`
- Test: `tests/test_site_content.py`

- [ ] **Step 1: Write the failing test**

```python
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]


def read_text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


class SiteStructureTests(unittest.TestCase):
    def test_homepage_links_to_publications_and_resume(self) -> None:
      html = read_text("index.html")
      self.assertIn('href="publications.html"', html)
      self.assertIn('href="Files/zhirui_20260319.pdf"', html)

    def test_homepage_contains_required_sections(self) -> None:
      html = read_text("index.html")
      for marker in ['id="hero"', 'id="research-areas"', 'id="selected-work"', 'id="experience"']:
        self.assertIn(marker, html)

    def test_publications_page_exists(self) -> None:
      self.assertTrue((ROOT / "publications.html").exists())

    def test_shared_assets_exist(self) -> None:
      self.assertTrue((ROOT / "Files/site.css").exists())
      self.assertTrue((ROOT / "Files/site.js").exists())


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_site_content -v`
Expected: FAIL because `publications.html`, `Files/site.css`, `Files/site.js`, and the new homepage section markers do not exist yet.

- [ ] **Step 3: Write minimal implementation**

```python
# tests/__init__.py
```

Create the empty package marker file so `python3 -m unittest tests.test_site_content -v` works consistently.

- [ ] **Step 4: Run test to verify it still fails for the right reasons**

Run: `python3 -m unittest tests.test_site_content -v`
Expected: FAIL only on missing pages/assets/markers, not on import errors.

- [ ] **Step 5: Commit**

```bash
git add tests/__init__.py tests/test_site_content.py
git commit -m "test: add static site regression harness"
```

### Task 2: Create Shared Assets And New Page Shells

**Files:**
- Create: `publications.html`
- Create: `Files/site.css`
- Create: `Files/site.js`
- Create: `Files/zhirui_20260319.pdf`
- Modify: `index.html`
- Modify: `_config.yml`
- Test: `tests/test_site_content.py`

- [ ] **Step 1: Extend the failing test for shared branding and palette**

```python
    def test_shared_palette_is_declared(self) -> None:
      css = read_text("Files/site.css")
      self.assertIn("--color-navy: #13294B;", css)
      self.assertIn("--color-coral: #E94A36;", css)
      self.assertIn("--color-mist: #EAF2FA;", css)
      self.assertIn("--color-paper: #F4F4F2;", css)

    def test_publications_page_has_title_and_year_groups(self) -> None:
      html = read_text("publications.html")
      self.assertIn("<title>Publications | Zhirui Zhang</title>", html)
      for year in ["2026", "2025", "2024", "2023"]:
        self.assertIn(f'data-year="{year}"', html)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_site_content -v`
Expected: FAIL because the new CSS variables, publications page title, and year groups do not exist yet.

- [ ] **Step 3: Write minimal implementation**

```html
<!-- index.html -->
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Zhirui Zhang</title>
  <link rel="stylesheet" href="Files/site.css">
</head>
<body>
  <main>
    <section id="hero"></section>
    <section id="research-areas"></section>
    <section id="selected-work"></section>
    <section id="experience"></section>
    <a href="publications.html">Publications</a>
    <a href="Files/zhirui_20260319.pdf">Resume</a>
  </main>
  <script src="Files/site.js"></script>
</body>
</html>
```

```html
<!-- publications.html -->
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Publications | Zhirui Zhang</title>
  <link rel="stylesheet" href="Files/site.css">
</head>
<body>
  <main>
    <section data-year="2026"></section>
    <section data-year="2025"></section>
    <section data-year="2024"></section>
    <section data-year="2023"></section>
  </main>
</body>
</html>
```

```css
/* Files/site.css */
:root {
  --color-navy: #13294B;
  --color-coral: #E94A36;
  --color-mist: #EAF2FA;
  --color-paper: #F4F4F2;
}
```

```js
// Files/site.js
document.documentElement.dataset.js = "enabled";
```

```bash
cp /Users/zhangzhirui/workspace_zzr/writing/resume_zhirui/zhirui_20260319.pdf Files/zhirui_20260319.pdf
```

Update `_config.yml` to align title/description with the new English site metadata.

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests.test_site_content -v`
Expected: PASS for the shared shell, page existence, palette declarations, and local resume asset link.

- [ ] **Step 5: Commit**

```bash
git add index.html publications.html Files/site.css Files/site.js Files/zhirui_20260319.pdf _config.yml
git commit -m "feat: add redesigned site shell and shared assets"
```

### Task 3: Implement Homepage Content And Research-First Narrative

**Files:**
- Modify: `index.html`
- Modify: `Files/site.css`
- Modify: `tests/test_site_content.py`
- Test: `tests/test_site_content.py`

- [ ] **Step 1: Extend the failing test for homepage content requirements**

```python
    def test_homepage_contains_key_content_blocks(self) -> None:
      html = read_text("index.html")
      for marker in [
        'id="bio"',
        'id="research-areas"',
        'id="selected-work"',
        'id="experience"',
        'id="service-awards"',
        'id="contact"',
      ]:
        self.assertIn(marker, html)
      self.assertIn("Google Scholar", html)
      self.assertIn("GitHub", html)
      self.assertIn("Cited by 2908", html)
      self.assertIn("h-index 25", html)
      self.assertIn("i10-index 38", html)
      self.assertIn("Deep Learning", html)
      self.assertIn("Large Language Model", html)
      self.assertIn("World Model", html)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_site_content -v`
Expected: FAIL because the homepage shell does not yet include the new narrative sections, metrics, and links.

- [ ] **Step 3: Write minimal implementation**

```html
<section id="hero" class="hero">
  <p class="eyebrow">Zhirui Zhang</p>
  <h1>Researcher-builder in LLM post-training, reasoning, multilingual, and translation systems.</h1>
  <p class="lede">Short English bio rewritten from the 2026-03-19 resume summary.</p>
</section>

<section id="bio"></section>
<section id="research-areas"></section>
<section id="selected-work"></section>
<section id="experience"></section>
<section id="service-awards"></section>
<section id="contact"></section>

<aside class="sidebar-metrics">
  <span>Cited by 2908</span>
  <span>h-index 25</span>
  <span>i10-index 38</span>
  <span>Deep Learning</span>
  <span>Large Language Model</span>
  <span>World Model</span>
  <a href="https://scholar.google.com/citations?user=C8Ylo7sAAAAJ&hl=en">Google Scholar</a>
  <a href="https://github.com/zrustc">GitHub</a>
</aside>
```

```css
.hero {
  background: linear-gradient(180deg, var(--color-mist), var(--color-paper));
}

.sidebar-metrics {
  border: 1px solid rgba(19, 41, 75, 0.16);
}
```

Populate the sections with the approved content strategy:

- concise English bio derived from the resume summary
- research areas centered on LLM post-training, reasoning, multilingual, multimodal, and translation
- selected recent papers
- concise timeline for IDEA Research, Huawei, StepFun, Tencent AI Lab, Alibaba DAMO Academy, and Microsoft Research
- academic service and selected awards
- contact links and resume entry

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests.test_site_content -v`
Expected: PASS, confirming the homepage now contains the required research-first sections and updated sidebar links/metrics.

- [ ] **Step 5: Commit**

```bash
git add index.html Files/site.css tests/test_site_content.py
git commit -m "feat: implement research-first homepage content"
```

### Task 4: Implement Publications Archive Page

**Files:**
- Modify: `publications.html`
- Modify: `Files/site.css`
- Modify: `tests/test_site_content.py`
- Test: `tests/test_site_content.py`

- [ ] **Step 1: Extend the failing test for publication coverage**

```python
    def test_publications_page_lists_recent_anchor_papers(self) -> None:
      html = read_text("publications.html")
      for title in [
        "SWE-AGI",
        "Is PRM Necessary?",
        "Safe Delta",
        "Simple o3",
        "Lost in the Source Language",
        "Document-Level Machine Translation with Large Language Models",
      ]:
        self.assertIn(title, html)

    def test_publications_page_contains_rich_entry_metadata(self) -> None:
      html = read_text("publications.html")
      self.assertIn("Z Zhang, H Zhang, H Fei", html)
      self.assertIn("arXiv preprint arXiv:2602.09447", html)
      self.assertIn('data-year="2026"', html)
      self.assertIn('href="https://arxiv.org/abs/2602.09447"', html)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_site_content -v`
Expected: FAIL because the publications page still contains empty year sections.

- [ ] **Step 3: Write minimal implementation**

```html
<section class="pub-year" data-year="2026">
  <h2>2026</h2>
  <article class="pub-entry">
    <h3>SWE-AGI: Benchmarking Specification-Driven Software Construction with MoonBit in the Era of Autonomous Agents</h3>
    <p>Z Zhang, H Zhang, H Fei, Z Bao, Y Chen, Z Lei, Z Liu, Y Sun, M Xiao, Z Ye, ...</p>
    <p>arXiv preprint arXiv:2602.09447</p>
    <a href="https://arxiv.org/abs/2602.09447">Paper</a>
  </article>
</section>

<section class="pub-year" data-year="2025">
  <h2>2025</h2>
  <article class="pub-entry">Is PRM Necessary? Problem-Solving RL Implicitly Induces PRM Capability in LLMs</article>
  <article class="pub-entry">Safe Delta: Consistently Preserving Safety when Fine-Tuning LLMs on Diverse Datasets</article>
  <article class="pub-entry">Simple o3: Towards Interleaved Vision-Language Reasoning</article>
</section>
```

Then finish the full archive with year-grouped entries for 2024, 2023, and earlier representative work, using Scholar as the source of truth for title, author, venue, and year metadata, and include resource links whenever the live or existing source material makes them available.

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests.test_site_content -v`
Expected: PASS, confirming recent anchor papers and year groups appear on the publications page.

- [ ] **Step 5: Commit**

```bash
git add publications.html Files/site.css tests/test_site_content.py
git commit -m "feat: add publications archive page"
```

### Task 5: Add Responsive Polish And Minimal Interaction

**Files:**
- Modify: `Files/site.css`
- Modify: `Files/site.js`
- Modify: `index.html`
- Modify: `publications.html`
- Modify: `tests/test_site_content.py`
- Test: `tests/test_site_content.py`

- [ ] **Step 1: Extend the failing test for responsive and interaction hooks**

```python
    def test_pages_include_shared_nav_and_mobile_toggle_hook(self) -> None:
      for path in ["index.html", "publications.html"]:
        html = read_text(path)
        self.assertIn('class="site-nav"', html)
        self.assertIn('data-nav-toggle', html)
        self.assertIn('src="Files/site.js"', html)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_site_content -v`
Expected: FAIL because the pages do not yet include the finalized shared nav and mobile toggle hook.

- [ ] **Step 3: Write minimal implementation**

```html
<button type="button" class="nav-toggle" data-nav-toggle aria-expanded="false">
  Menu
</button>
<nav class="site-nav"></nav>
```

```js
const toggle = document.querySelector("[data-nav-toggle]");
const nav = document.querySelector(".site-nav");

if (toggle && nav) {
  toggle.addEventListener("click", () => {
    const expanded = toggle.getAttribute("aria-expanded") === "true";
    toggle.setAttribute("aria-expanded", String(!expanded));
    nav.dataset.open = String(!expanded);
  });
}
```

```css
@media (max-width: 860px) {
  .site-layout {
    grid-template-columns: 1fr;
  }
}
```

Apply the final responsive polish:

- sticky or fixed top navigation in the approved navy tone
- two-column desktop layout collapsing to one column on mobile
- publication entries wrapping gracefully
- restrained hover and reveal states

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests.test_site_content -v`
Expected: PASS, confirming both pages use the shared nav and minimal JS hook.

- [ ] **Step 5: Commit**

```bash
git add index.html publications.html Files/site.css Files/site.js tests/test_site_content.py
git commit -m "feat: polish responsive navigation and interactions"
```

### Task 6: Final Verification And Metadata Cleanup

**Files:**
- Modify: `_config.yml`
- Modify: `README.md`
- Test: `tests/test_site_content.py`

- [ ] **Step 1: Write the failing test for final metadata expectations**

```python
    def test_homepage_title_matches_new_branding(self) -> None:
      html = read_text("index.html")
      self.assertIn("<title>Zhirui Zhang</title>", html)
```

- [ ] **Step 2: Run test to verify it fails only if branding drifted**

Run: `python3 -m unittest tests.test_site_content -v`
Expected: PASS if already satisfied; if so, keep the test as a regression guard and continue to the full suite run.

- [ ] **Step 3: Write minimal implementation**

```yaml
# _config.yml
title: Zhirui Zhang
description: Researcher-builder in LLM post-training, reasoning, multilingual, and translation systems.
```

```md
# README.md
Static personal site for Zhirui Zhang.
```

Keep README changes minimal and only update metadata/documentation if it clarifies the new site.

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests.test_site_content -v`
Expected: PASS

Run: `python3 -m unittest -v`
Expected: PASS for the full regression suite

- [ ] **Step 5: Commit**

```bash
git add _config.yml README.md tests/test_site_content.py
git commit -m "chore: finalize homepage redesign metadata"
```

## Verification Checklist

- Run: `python3 -m unittest -v`
- Expected: all site regression tests pass

- Run: `python3 -m http.server 8000`
- Expected: manual browser smoke test for `http://localhost:8000/index.html` and `http://localhost:8000/publications.html`

- Manually verify:
  - homepage hero leads with research identity
  - homepage links to Scholar, GitHub, publications, and local resume PDF
  - publications page includes recent 2024-2026 work and older representative years
  - palette reflects the approved navy/coral/mist/paper direction
  - mobile layout remains readable
