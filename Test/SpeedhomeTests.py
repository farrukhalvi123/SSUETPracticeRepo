import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from Pages.AddProperty import AddProperty


class SpeedHomeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.get("beta.speedhome.com")
        cls.driver.maximize_window()

    def test_addproperty(self):
        driver = self.driver
        add = AddProperty(driver)
        add.click_addproperty()
        add.click_rent()
        add.enter_propertyname("abcxyz")

    def tearDownClass(cls):
        cls.driver.quit()
        cls.driver.close()
