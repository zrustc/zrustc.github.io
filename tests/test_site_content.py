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


if __name__ == "__main__":
    unittest.main()
