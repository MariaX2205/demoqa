from conftest import browser
from pages.base_page import BasePage
from components.components import WebElement


class Webtables(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)
        self.block = WebElement(driver, 'div.rt-noData')
        self.btn_delete_row = WebElement(driver, "[title = 'Delete']")