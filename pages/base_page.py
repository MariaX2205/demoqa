from selenium.webdriver.common.by import By
import logging
from components.components import WebElement

import requests

class BasePage:
    def __init__(self, driver, base_url='https://demoqa.com'):
        self.driver = driver
        self.base_url = base_url  # 'https://demoqa.com'
        self.viewport = WebElement(driver, 'head>meta[name = "viewport"]')
        self.h5_locators = WebElement(driver, 'div.card-body > h5')

    def code_status(self):
        resp = requests.get(self.base_url)
        return resp.status_code == 200

    def visit(self):
        return self.driver.get(self.base_url)

    def back(self):
        self.driver.back()  # эти методы также можно использовать от browser, zb: browser.back

    def forward(self):
        self.driver.forward()

    def refresh(self):
        self.driver.refresh()

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def equal_url(self):
        if self.get_url() == self.base_url:
            return True
        return False

    def alert(self):
        try:
            return self.driver.switch_to.alert
        except Exception as ex:
            logging.log(1, ex)
            return False
