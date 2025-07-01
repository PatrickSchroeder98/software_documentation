import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class FractalArtWebsiteTests(unittest.TestCase):
    """Class for Fractal Art Website Tests."""

    @classmethod
    def setUpClass(cls):
        """Method that prepares the driver for testing"""
        cls.driver = webdriver.Chrome()
        # cls.base_url = "https://patrickschroeder98.github.io/software_documentation/index.html"
        cls.base_url = "http://127.0.0.1:5500/index.html"
        cls.driver.get(cls.base_url)

    def setUp(self):
        """Method that runs before each test."""
        self.driver.get(self.base_url)

    def test_title(self):
        """Method that checks if the title is displayed correctly."""
        title = self.driver.title
        self.assertEqual("Software Documentation Website", title)

    def test_project_titles(self):
        """Method that checks if the titles of projects are displayed correctly."""

        values = [
            "a[href='master_thesis_docs/index.html']"
        ]

        texts = [
            "Development of a program for numerical solving Maxwell Equations for electromagnetic field of metal exposed to high power laser beam in the vacuum-metal system."
        ]

        self.assertEqual(len(values), len(texts))

        def run(val, expected_text):
            """Method that runs the test with given parameters."""
            self.driver.find_element(By.CSS_SELECTOR, val).click()
            text = self.driver.find_element(By.CSS_SELECTOR, "h1[class='title']")
            self.assertEqual(expected_text, text.text)

        for i in range(len(values)):
            run(values[i], texts[i])
            self.setUp()

    def test_master_thesis_pages(self):
        """Method that checks if the master thesis documentation is displayed correctly."""

        values = [
            "a[href='master_thesis_docs/index.html']",
            "a[data-i18n='scope']",
            "a[data-i18n='nav-project']",
            "a[data-i18n='requirements']",
            "a[data-i18n='nav-project']",
            "a[data-i18n='statistics']",
            "a[data-i18n='nav-project']",
        ]

        texts = [
            "Master Thesis Documentation",
            "Master Thesis Scope",
            "Master Thesis Documentation",
            "Master Thesis Requirements",
            "Master Thesis Documentation",
            "Master Thesis Statistics",
            "Master Thesis Documentation",
        ]

        self.assertEqual(len(values), len(texts))

        def run(val, expected_text):
            self.driver.find_element(
                By.CSS_SELECTOR, val
            ).click()
            page_title = self.driver.title
            self.assertEqual(expected_text, page_title)

        for i in range(len(values)):
            run(values[i], texts[i])

    def test_master_thesis_navigation(self):
        """Method that checks if the master thesis documentation navigation works correctly."""

        values = [
            "a[href='master_thesis_docs/index.html']",
            "a[data-i18n='next']",
            "a[class='next-link']",
            "a[class='next-link']",
            "a[class='prev-link']",
            "a[class='prev-link']",
            "a[class='prev-link']",
        ]

        texts = [
            "Master Thesis Documentation",
            "Master Thesis Scope",
            "Master Thesis Requirements",
            "Master Thesis Statistics",
            "Master Thesis Requirements",
            "Master Thesis Scope",
            "Master Thesis Documentation",
        ]

        self.assertEqual(len(values), len(texts))

        def run(val, expected_text):
            self.driver.find_element(
                By.CSS_SELECTOR, val
            ).click()
            page_title = self.driver.title
            self.assertEqual(expected_text, page_title)

        for i in range(len(values)):
            run(values[i], texts[i])

    @classmethod
    def tearDownClass(cls):
        """Method that runs after testing."""
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
