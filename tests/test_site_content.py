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
