from selenium.webdriver.common.by import By


class AddProperty():
    def __int__(self, driver):
        self.driver = driver
        self.addproperty = "//span[normalize-space()='Post Property FREE']"
        self.rent = "//div[@id='manage_property']//li[@class='MuiListItem-root MuiListItem-gutters MuiListItem-padding css-1yo8bqd']"
        self.highrise = "//span[@class='icon-apartment']"
        self.propertyname = "propertyName"

    def click_addproperty(self):
        self.driver.find_element(By.XPATH, self.addproperty).click()

    def click_rent(self):
        self.driver.find_element(By.XPATH, self.rent).click()

    def enter_propertyname(self, prop):
        self.driver.find_element(By.ID, self.propertyname).send_keys(prop)
