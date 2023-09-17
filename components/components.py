from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class WebElement:
    def __init__(self, driver, locator=''):
        self.icon = '#app > header > a > img'
        self.driver = driver
        self.locator = locator


    def click(self):  # click the element(icon):
        self.driver.find_element(By.CSS_SELECTOR, self.locator).click()

    def find_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    def get_text(self):
        return str(self.find_element().text)
