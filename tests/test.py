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
        # cls.base_url = ""
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

        def run(val, expected_text):
            """Method that runs the test with given parameters."""
            self.driver.find_element(By.CSS_SELECTOR, val).click()
            text = self.driver.find_element(By.CSS_SELECTOR, "h1[class='title']")
            self.assertEqual(expected_text, text.text)

        for i in range(len(values)):
            run(values[i], texts[i])
            self.setUp()

    def test_msa(self):
        """Method that checks if the MSA documentation is displayed correctly."""
        self.driver.find_element(
            By.CSS_SELECTOR, "a[href='master_thesis_docs/index.html']"
        ).click()
        title = self.driver.title
        self.assertEqual("Master Thesis Documentation", title)

    @classmethod
    def tearDownClass(cls):
        """Method that runs after testing."""
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
