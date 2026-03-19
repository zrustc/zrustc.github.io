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
        self.assertIn("NeurIPS 2025 · 2025", html)

    def test_publications_page_contains_rich_entry_metadata(self) -> None:
        html = read_text("publications.html")
        self.assertIn("Z Zhang, H Zhang, H Fei", html)
        self.assertIn("arXiv preprint arXiv:2602.09447", html)
        self.assertIn('data-year="2026"', html)
        self.assertIn('href="https://arxiv.org/abs/2602.09447"', html)

    def test_pages_include_shared_nav_and_mobile_toggle_hook(self) -> None:
        for path in ["index.html", "publications.html"]:
            html = read_text(path)
            self.assertIn('class="site-nav"', html)
            self.assertIn("data-nav-toggle", html)
            self.assertIn('src="Files/site.js"', html)

    def test_homepage_title_matches_new_branding(self) -> None:
        html = read_text("index.html")
        self.assertIn("<title>Zhirui Zhang</title>", html)

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


if __name__ == "__main__":
    unittest.main()
