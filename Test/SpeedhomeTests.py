import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class SpeedHomeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.get("beta.speedhome.com")
        cls.driver.maximize_window()

    def tearDownClass(cls):
        cls.driver.quit()
        cls.driver.close()
