from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from components.components import WebElement

class Checkbox(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/checkbox'
        super().__init__(driver, self.base_url)
        self.checkbox = WebElement(driver, '.rct-icon.rct-icon-uncheck')
        self.cl_cbx = WebElement(driver, 'button.rct-option.rct-option-expand-all > svg')
