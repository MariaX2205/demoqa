from components.components import WebElement
from pages.base_page import BasePage
class AddRemElem(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://the-internet.herokuapp.com/add_remove_elements/"
        super().__init__(driver, self.base_url)
        self.button = WebElement(driver, '#content > div > button')
        self.btn_del = WebElement(driver, '#elements > button')