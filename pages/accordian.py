from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from components.components import WebElement


class Accordian(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)
        self.element = WebElement(driver, '#section1Content > p')
        self.heading = WebElement(driver, '#section1Heading')
        self.section21 = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.section22 = WebElement (driver, '#section2Content > p:nth-child(2)')
        self.section3 = WebElement(driver, '#section3Content > p')