import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
            "a[href='master_thesis_docs/index.html']",
            "a[href='engineer_thesis_docs/index.html']",
            "a[href='rk_comparison_docs/index.html']",
            "a[href='matrix_library_docs/index.html']",
            "a[href='portfolio_docs/index.html']",
        ]

        texts = [
            "Development of a program for numerical solving Maxwell Equations for electromagnetic field of metal exposed to high power laser beam in the vacuum-metal system.",
            "Development of a program for numerical analysis of heating process and energy transfer in metals exposed to high power laser beam in piko- and femtosecond regime",
            "Development of a program for comparison of Runge-Kutta and Runge-Kutta-Fehlberg methods of various orders based on the analytical solution to nuclear decay problem.",
            "Development of C++ Library for Matrix Calculations",
            "Portfolio Website",
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
            "a[data-i18n='nav-project']",
            "a[data-i18n='scope']",
            "a[data-i18n='nav-project']",
            "a[data-i18n='requirements']",
            "a[data-i18n='nav-project']",
            "a[data-i18n='statistics']",
            "a[data-i18n='nav-project']",
        ]

        texts = [
            "Master Thesis Documentation",
            "Master Thesis Documentation",
            "Master Thesis Scope",
            "Master Thesis Documentation",
            "Master Thesis Requirements",
            "Master Thesis Documentation",
            "Master Thesis Statistics",
            "Master Thesis Documentation",
        ]

        self.check(values, texts)

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

        self.check(values, texts)

    def test_master_thesis_home_button(self):
        """Method that checks if the home button on the master thesis documentation pages works correctly."""

        values = [
            "a[href='master_thesis_docs/index.html']",
            "a[data-i18n='nav-home']",
            "a[href='master_thesis_docs/index.html']",
            "a[data-i18n='scope']",
            "a[data-i18n='nav-home']",
            "a[href='master_thesis_docs/index.html']",
            "a[data-i18n='requirements']",
            "a[data-i18n='nav-home']",
            "a[href='master_thesis_docs/index.html']",
            "a[data-i18n='statistics']",
            "a[data-i18n='nav-home']",

        ]

        texts = [
            "Master Thesis Documentation",
            "Software Documentation Website",
            "Master Thesis Documentation",
            "Master Thesis Scope",
            "Software Documentation Website",
            "Master Thesis Documentation",
            "Master Thesis Requirements",
            "Software Documentation Website",
            "Master Thesis Documentation",
            "Master Thesis Statistics",
            "Software Documentation Website",
        ]

        self.check(values, texts)

    def test_engineer_thesis_pages(self):
        """Method that checks if the engineer thesis documentation is displayed correctly."""

        values = [
            "a[href='engineer_thesis_docs/index.html']",
            "a[data-i18n='nav-project']",
            "a[data-i18n='scope']",
            "a[data-i18n='nav-project']",
            "a[data-i18n='requirements']",
            "a[data-i18n='nav-project']",
            "a[data-i18n='statistics']",
            "a[data-i18n='nav-project']",
        ]

        texts = [
            "Engineer Thesis Documentation",
            "Engineer Thesis Documentation",
            "Engineer Thesis Scope",
            "Engineer Thesis Documentation",
            "Engineer Thesis Requirements",
            "Engineer Thesis Documentation",
            "Engineer Thesis Statistics",
            "Engineer Thesis Documentation",
        ]

        self.check(values, texts)

    def test_engineer_thesis_navigation(self):
        """Method that checks if the engineer thesis documentation navigation works correctly."""

        values = [
            "a[href='engineer_thesis_docs/index.html']",
            "a[data-i18n='next']",
            "a[class='next-link']",
            "a[class='next-link']",
            "a[class='prev-link']",
            "a[class='prev-link']",
            "a[class='prev-link']",
        ]
        texts = [
            "Engineer Thesis Documentation",
            "Engineer Thesis Scope",
            "Engineer Thesis Requirements",
            "Engineer Thesis Statistics",
            "Engineer Thesis Requirements",
            "Engineer Thesis Scope",
            "Engineer Thesis Documentation",
        ]

        self.check(values, texts)

    def test_engineer_thesis_home_button(self):
        """Method that checks if the home button on the engineer thesis documentation pages works correctly."""

        values = [
            "a[href='engineer_thesis_docs/index.html']",
            "a[data-i18n='nav-home']",
            "a[href='engineer_thesis_docs/index.html']",
            "a[data-i18n='scope']",
            "a[data-i18n='nav-home']",
            "a[href='engineer_thesis_docs/index.html']",
            "a[data-i18n='requirements']",
            "a[data-i18n='nav-home']",
            "a[href='engineer_thesis_docs/index.html']",
            "a[data-i18n='statistics']",
            "a[data-i18n='nav-home']",
        ]

        texts = [
            "Engineer Thesis Documentation",
            "Software Documentation Website",
            "Engineer Thesis Documentation",
            "Engineer Thesis Scope",
            "Software Documentation Website",
            "Engineer Thesis Documentation",
            "Engineer Thesis Requirements",
            "Software Documentation Website",
            "Engineer Thesis Documentation",
            "Engineer Thesis Statistics",
            "Software Documentation Website",
        ]

        self.check(values, texts)

    def test_RK_comparison_pages(self):
        """Method that checks if the RK comparison documentation pages are working correctly."""

        values = [
            "a[href='rk_comparison_docs/index.html']",
            "a[data-i18n='nav-project']",
            "a[data-i18n='scope']",
            "a[data-i18n='nav-project']",
            "a[data-i18n='requirements']",
            "a[data-i18n='nav-project']",
            "a[data-i18n='interface']",
            "a[data-i18n='nav-project']",
            "a[data-i18n='bibliography']",
            "a[data-i18n='nav-project']",
        ]

        texts = [
            "RK Comparison Documentation",
            "RK Comparison Documentation",
            "RK Comparison Scope",
            "RK Comparison Documentation",
            "RK Comparison Requirements",
            "RK Comparison Documentation",
            "RK Comparison Interface Documentation",
            "RK Comparison Documentation",
            "RK Comparison Bibliography",
            "RK Comparison Documentation",
        ]

        self.check(values, texts)

    def test_RK_comparison_navigation(self):
        """Method that checks if the RK comparison documentation navigation works correctly."""

        values = [
            "a[href='rk_comparison_docs/index.html']",
            "a[data-i18n='next']",
            "a[class='next-link']",
            "a[class='next-link']",
            "a[class='next-link']",
            "a[class='prev-link']",
            "a[class='prev-link']",
            "a[class='prev-link']",
            "a[class='prev-link']",
        ]

        texts = [
            "RK Comparison Documentation",
            "RK Comparison Scope",
            "RK Comparison Requirements",
            "RK Comparison Interface Documentation",
            "RK Comparison Bibliography",
            "RK Comparison Interface Documentation",
            "RK Comparison Requirements",
            "RK Comparison Scope",
            "RK Comparison Documentation",
        ]

        self.check(values, texts)

    def test_RK_comparison_home_button(self):
        """Method that checks if the home button on the RK comparison documentation pages works correctly."""

        values = [
            "a[href='rk_comparison_docs/index.html']",
            "a[data-i18n='nav-home']",
            "a[href='rk_comparison_docs/index.html']",
            "a[data-i18n='scope']",
            "a[data-i18n='nav-home']",
            "a[href='rk_comparison_docs/index.html']",
            "a[data-i18n='requirements']",
            "a[data-i18n='nav-home']",
            "a[href='rk_comparison_docs/index.html']",
            "a[data-i18n='interface']",
            "a[data-i18n='nav-home']",
            "a[href='rk_comparison_docs/index.html']",
            "a[data-i18n='bibliography']",
            "a[data-i18n='nav-home']",
        ]

        texts = [
            "RK Comparison Documentation",
            "Software Documentation Website",
            "RK Comparison Documentation",
            "RK Comparison Scope",
            "Software Documentation Website",
            "RK Comparison Documentation",
            "RK Comparison Requirements",
            "Software Documentation Website",
            "RK Comparison Documentation",
            "RK Comparison Interface Documentation",
            "Software Documentation Website",
            "RK Comparison Documentation",
            "RK Comparison Bibliography",
            "Software Documentation Website",
        ]

        self.check(values, texts)

    def test_RK_comparison_sphinx(self):
        original_window = self.driver.current_window_handle
        self.assertEqual(len(self.driver.window_handles), 1)

        self.driver.find_element(
            By.CSS_SELECTOR, "a[href='rk_comparison_docs/index.html']"
        ).click()
        self.driver.find_element(
            By.CSS_SELECTOR, "a[data-i18n='sphinx']"
        ).click()

        WebDriverWait(self.driver, 10).until(EC.new_window_is_opened([original_window]))

        for handle in self.driver.window_handles:
            if handle != original_window:
                self.driver.switch_to.window(handle)
                break

        self.assertEqual(
            self.driver.title,
            "rk_comparison documentation — rk_comparison 1.0.0 documentation"
        )

        self.assertIn("sphinx_docs/index.html", self.driver.current_url)

        self.driver.find_element(
            By.CSS_SELECTOR, "a[data-i18n='project_mainpage_link']"
        ).click()

        self.assertEqual(
            self.driver.title,
            "RK Comparison Documentation"
        )

    def test_mcl_pages(self):
        """Method that checks if the MCL documentation pages are working correctly."""

        values = [
            "a[href='matrix_library_docs/index.html']",
            "a[data-i18n='nav-project']",
            "a[data-i18n='scope']",
            "a[data-i18n='nav-project']",
            "a[data-i18n='requirements']",
            "a[data-i18n='nav-project']",
            "a[data-i18n='interface']",
            "a[data-i18n='nav-project']",
            "a[data-i18n='code_documentation']",
            "a[data-i18n='nav-project']",
            "a[data-i18n='bibliography']",
            "a[data-i18n='nav-project']",
        ]

        texts = [
            "MCL Documentation",
            "MCL Documentation",
            "MCL Scope",
            "MCL Documentation",
            "MCL Requirements",
            "MCL Documentation",
            "MCL Interface Documentation",
            "MCL Documentation",
            "MCL Code Documentation",
            "MCL Documentation",
            "MCL Bibliography",
            "MCL Documentation",
        ]

        self.check(values, texts)

    def test_mcl_code_documentation_pages(self):
        """Method that checks if the MCL code documentation pages are working correctly."""
        values = [
            "a[href='matrix_library_docs/index.html']",
            "a[data-i18n='code_documentation']",
            "a[data-i18n='matrixcalculations']",
            "a[data-i18n='nav-project']",
            "a[data-i18n='code_documentation']",
            "a[data-i18n='matrixchecks']",
            "a[data-i18n='nav-project']",
            "a[data-i18n='code_documentation']",
            "a[data-i18n='matrixio']",
            "a[data-i18n='nav-project']",
            "a[data-i18n='code_documentation']",
            "a[data-i18n='matrixcalculationsapi']",
            "a[data-i18n='nav-project']",
            "a[data-i18n='code_documentation']",
            "a[data-i18n='matrixcalculationstests']",
            "a[data-i18n='nav-project']",
            "a[data-i18n='code_documentation']",
            "a[data-i18n='matrixcheckstests']",
            "a[data-i18n='nav-project']",
            "a[data-i18n='code_documentation']",
            "a[data-i18n='matrixcapitests']",
            "a[data-i18n='nav-project']",
        ]

        texts = [
            "MCL Documentation",
            "MCL Code Documentation",
            "MCL Code Documentation - MatrixCalculations",
            "MCL Documentation",
            "MCL Code Documentation",
            "MCL Code Documentation - MatrixChecks",
            "MCL Documentation",
            "MCL Code Documentation",
            "MCL Code Documentation - MatrixIO",
            "MCL Documentation",
            "MCL Code Documentation",
            "MCL Code Documentation - MatrixCalculationsAPI",
            "MCL Documentation",
            "MCL Code Documentation",
            "MCL Code Documentation - MatrixCalculationsLibraryTests",
            "MCL Documentation",
            "MCL Code Documentation",
            "MCL Code Documentation - MatrixChecksTests",
            "MCL Documentation",
            "MCL Code Documentation",
            "MCL Code Documentation - MatrixApiTests",
            "MCL Documentation",
        ]

        self.check(values, texts)

    def test_mcl_navigation(self):
        """Method that checks if the MCL documentation navigation works correctly."""

        values = [
            "a[href='matrix_library_docs/index.html']",
            "a[data-i18n='next']",
            "a[class='next-link']",
            "a[class='next-link']",
            "a[class='next-link']",
            "a[class='next-link']",
            "a[class='next-link']",
            "a[class='next-link']",
            "a[class='next-link']",
            "a[class='next-link']",
            "a[class='next-link']",
            "a[class='next-link']",
            "a[class='next-link']",
            "a[class='prev-link']",
            "a[class='prev-link']",
            "a[class='prev-link']",
            "a[class='prev-link']",
            "a[class='prev-link']",
            "a[class='prev-link']",
            "a[class='prev-link']",
            "a[class='prev-link']",
            "a[class='prev-link']",
            "a[class='prev-link']",
            "a[class='prev-link']",
            "a[class='prev-link']",
        ]

        texts = [
            "MCL Documentation",
            "MCL Scope",
            "MCL Requirements",
            "MCL Interface Documentation",
            "MCL Code Documentation",
            "MCL Code Documentation - MatrixCalculations",
            "MCL Code Documentation - MatrixChecks",
            "MCL Code Documentation - MatrixIO",
            "MCL Code Documentation - MatrixCalculationsAPI",
            "MCL Code Documentation - MatrixCalculationsLibraryTests",
            "MCL Code Documentation - MatrixChecksTests",
            "MCL Code Documentation - MatrixApiTests",
            "MCL Bibliography",
            "MCL Code Documentation - MatrixApiTests",
            "MCL Code Documentation - MatrixChecksTests",
            "MCL Code Documentation - MatrixCalculationsLibraryTests",
            "MCL Code Documentation - MatrixCalculationsAPI",
            "MCL Code Documentation - MatrixIO",
            "MCL Code Documentation - MatrixChecks",
            "MCL Code Documentation - MatrixCalculations",
            "MCL Code Documentation",
            "MCL Interface Documentation",
            "MCL Requirements",
            "MCL Scope",
            "MCL Documentation",
        ]

        self.check(values, texts)

    def test_mcl_home_button(self):
        """Method that checks if the home button on the MCL documentation pages works correctly."""

        values = [
            "a[href='matrix_library_docs/index.html']",
            "a[data-i18n='nav-home']",
            "a[href='matrix_library_docs/index.html']",
            "a[data-i18n='scope']",
            "a[data-i18n='nav-home']",
            "a[href='matrix_library_docs/index.html']",
            "a[data-i18n='requirements']",
            "a[data-i18n='nav-home']",
            "a[href='matrix_library_docs/index.html']",
            "a[data-i18n='interface']",
            "a[data-i18n='nav-home']",
            "a[href='matrix_library_docs/index.html']",
            "a[data-i18n='code_documentation']",
            "a[data-i18n='nav-home']",
            "a[href='matrix_library_docs/index.html']",
            "a[data-i18n='code_documentation']",
            "a[data-i18n='matrixcalculations']",
            "a[data-i18n='nav-home']",
            "a[href='matrix_library_docs/index.html']",
            "a[data-i18n='code_documentation']",
            "a[data-i18n='matrixchecks']",
            "a[data-i18n='nav-home']",
            "a[href='matrix_library_docs/index.html']",
            "a[data-i18n='code_documentation']",
            "a[data-i18n='matrixio']",
            "a[data-i18n='nav-home']",
            "a[href='matrix_library_docs/index.html']",
            "a[data-i18n='code_documentation']",
            "a[data-i18n='matrixcalculationsapi']",
            "a[data-i18n='nav-home']",
            "a[href='matrix_library_docs/index.html']",
            "a[data-i18n='code_documentation']",
            "a[data-i18n='matrixcalculationstests']",
            "a[data-i18n='nav-home']",
            "a[href='matrix_library_docs/index.html']",
            "a[data-i18n='code_documentation']",
            "a[data-i18n='matrixcheckstests']",
            "a[data-i18n='nav-home']",
            "a[href='matrix_library_docs/index.html']",
            "a[data-i18n='code_documentation']",
            "a[data-i18n='matrixcapitests']",
            "a[data-i18n='nav-home']",
            "a[href='matrix_library_docs/index.html']",
            "a[data-i18n='bibliography']",
            "a[data-i18n='nav-home']",
        ]

        texts = [
            "MCL Documentation",
            "Software Documentation Website",
            "MCL Documentation",
            "MCL Scope",
            "Software Documentation Website",
            "MCL Documentation",
            "MCL Requirements",
            "Software Documentation Website",
            "MCL Documentation",
            "MCL Interface Documentation",
            "Software Documentation Website",
            "MCL Documentation",
            "MCL Code Documentation",
            "Software Documentation Website",
            "MCL Documentation",
            "MCL Code Documentation",
            "MCL Code Documentation - MatrixCalculations",
            "Software Documentation Website",
            "MCL Documentation",
            "MCL Code Documentation",
            "MCL Code Documentation - MatrixChecks",
            "Software Documentation Website",
            "MCL Documentation",
            "MCL Code Documentation",
            "MCL Code Documentation - MatrixIO",
            "Software Documentation Website",
            "MCL Documentation",
            "MCL Code Documentation",
            "MCL Code Documentation - MatrixCalculationsAPI",
            "Software Documentation Website",
            "MCL Documentation",
            "MCL Code Documentation",
            "MCL Code Documentation - MatrixCalculationsLibraryTests",
            "Software Documentation Website",
            "MCL Documentation",
            "MCL Code Documentation",
            "MCL Code Documentation - MatrixChecksTests",
            "Software Documentation Website",
            "MCL Documentation",
            "MCL Code Documentation",
            "MCL Code Documentation - MatrixApiTests",
            "Software Documentation Website",
            "MCL Documentation",
            "MCL Bibliography",
            "Software Documentation Website",
        ]

        self.check(values, texts)

    def test_portfolio_documentation_pages(self):
        """Method that checks if the Portfolio Website documentation is displayed correctly."""

        values = [
            "a[href='portfolio_docs/index.html']",
            "a[data-i18n='scope']",
            "a[data-i18n='nav-project']",
            "a[data-i18n='requirements']",
            "a[data-i18n='nav-project']",
            "a[data-i18n='interface']",
            "a[data-i18n='nav-project']",

        ]

        texts = [
            "Portfolio Website Documentation",
            "Portfolio Website Scope",
            "Portfolio Website Documentation",
            "Portfolio Website Requirements",
            "Portfolio Website Documentation",
            "Portfolio Website Interface Documentation",
            "Portfolio Website Documentation",
        ]

        self.check(values, texts)

    def test_portfolio_documentation_navigation(self):
        """Method that checks if the Portfolio Website documentation navigation works correctly."""

        values = [
            "a[href='portfolio_docs/index.html']",
            "a[data-i18n='next']",
            "a[class='next-link']",
            "a[class='next-link']",
            "a[class='prev-link']",
            "a[class='prev-link']",
            "a[class='prev-link']",
        ]

        texts = [
            "Portfolio Website Documentation",
            "Portfolio Website Scope",
            "Portfolio Website Requirements",
            "Portfolio Website Interface Documentation",
            "Portfolio Website Requirements",
            "Portfolio Website Scope",
            "Portfolio Website Documentation",
        ]

        self.check(values, texts)

    def test_portfolio_documentation_home_button(self):
        """Method that checks if the home button on the Portfolio Website documentation pages works correctly."""

        values = [
            "a[href='portfolio_docs/index.html']",
            "a[data-i18n='nav-home']",
            "a[href='portfolio_docs/index.html']",
            "a[data-i18n='scope']",
            "a[data-i18n='nav-home']",
            "a[href='portfolio_docs/index.html']",
            "a[data-i18n='requirements']",
            "a[data-i18n='nav-home']",
            "a[href='portfolio_docs/index.html']",
            "a[data-i18n='interface']",
            "a[data-i18n='nav-home']",

        ]

        texts = [
            "Portfolio Website Documentation",
            "Software Documentation Website",
            "Portfolio Website Documentation",
            "Portfolio Website Scope",
            "Software Documentation Website",
            "Portfolio Website Documentation",
            "Portfolio Website Requirements",
            "Software Documentation Website",
            "Portfolio Website Documentation",
            "Portfolio Website Interface Documentation",
            "Software Documentation Website",
        ]

        self.check(values, texts)


    def test_software_documentation_pages(self):
        """Method that checks if the Software Documentation Website documentation is displayed correctly."""

        values = [
            "a[href='software_docs/index.html']",
            "a[data-i18n='scope']",
            "a[data-i18n='nav-project']",
            "a[data-i18n='requirements']",
            "a[data-i18n='nav-project']",
            "a[data-i18n='interface']",
            "a[data-i18n='nav-project']",

        ]

        texts = [
            "Software Documentation Website Documentation",
            "Software Documentation Website Scope",
            "Software Documentation Website Documentation",
            "Software Documentation Website Requirements",
            "Software Documentation Website Documentation",
            "Software Documentation Website Interface Documentation",
            "Software Documentation Website Documentation",
        ]

        self.check(values, texts)

    def test_software_documentation_navigation(self):
        """Method that checks if the Software Documentation Website documentation navigation works correctly."""

        values = [
            "a[href='software_docs/index.html']",
            "a[data-i18n='next']",
            "a[class='next-link']",
            "a[class='next-link']",
            "a[class='prev-link']",
            "a[class='prev-link']",
            "a[class='prev-link']",
        ]

        texts = [
            "Software Documentation Website Documentation",
            "Software Documentation Website Scope",
            "Software Documentation Website Requirements",
            "Software Documentation Website Interface Documentation",
            "Software Documentation Website Requirements",
            "Software Documentation Website Scope",
            "Software Documentation Website Documentation",
        ]

        self.check(values, texts)

    def test_software_documentation_home_button(self):
        """Method that checks if the home button on the Software Documentation Website documentation pages works correctly."""

        values = [
            "a[href='software_docs/index.html']",
            "a[data-i18n='nav-home']",
            "a[href='software_docs/index.html']",
            "a[data-i18n='scope']",
            "a[data-i18n='nav-home']",
            "a[href='software_docs/index.html']",
            "a[data-i18n='requirements']",
            "a[data-i18n='nav-home']",
            "a[href='software_docs/index.html']",
            "a[data-i18n='interface']",
            "a[data-i18n='nav-home']",

        ]

        texts = [
            "Software Documentation Website Documentation",
            "Software Documentation Website",
            "Software Documentation Website Documentation",
            "Software Documentation Website Scope",
            "Software Documentation Website",
            "Software Documentation Website Documentation",
            "Software Documentation Website Requirements",
            "Software Documentation Website",
            "Software Documentation Website Documentation",
            "Software Documentation Website Interface Documentation",
            "Software Documentation Website",
        ]

        self.check(values, texts)

    @classmethod
    def tearDownClass(cls):
        """Method that runs after testing."""
        cls.driver.quit()


    def check(self, values, texts):
        """Method that runs checks during tests."""

        self.assertEqual(len(values), len(texts))

        def run(val, expected_text):
            """Method that runs checks with given parameters."""
            self.driver.find_element(
                By.CSS_SELECTOR, val
            ).click()
            page_title = self.driver.title
            self.assertEqual(expected_text, page_title)

        for i in range(len(values)):
            run(values[i], texts[i])

if __name__ == "__main__":
    unittest.main()
