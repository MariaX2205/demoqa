from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from components.components import WebElement

class Modal_dialogs(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)
        self.btn_loc_5 = WebElement(driver, '#app > div > div > div.row > div:nth-child(1) > div > div > div:nth-child(5) > div > ul > li')
        self.main_p_icon = WebElement(driver, '#app > header > a > img')