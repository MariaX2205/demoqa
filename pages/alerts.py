from pages.base_page import BasePage
from components.components import WebElement


class Alerts(BasePage):
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/alerts"
        super().__init__(driver, self.base_url)
        self.alert_button = WebElement(driver, '#alertButton')
        self.confirm_btn = WebElement(driver, '#confirmButton')
        self.confirm_result = WebElement(driver, '#confirmResult')
        self.prompt = WebElement(driver, '#promtButton')
        self.promptResult = WebElement(driver, '#promptResult')
