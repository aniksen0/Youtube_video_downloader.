import pathlib
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BaseTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        # options.add_argument("--start-fullscreen")
        # options.add_argument("--headless")
        # options.add_argument("--no-sandbox")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-notifications")
        # self.driver = webdriver.Chrome(executable_path=pathlib.Path(__file__).parent / "../browser/chromedriver", options=options)
        self.driver = webdriver.Chrome(executable_path=pathlib.Path(__file__).parent / "../browser/chromedriver.exe", options=options)
        self.driver.maximize_window()
        # self.driver.set_page_load_timeout(3000)
    def tearDown(self):
        self.driver.close()


class TestCase(object):
    pass


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
    unittest.TextTestRunner(verbosity=1).run(suite)
