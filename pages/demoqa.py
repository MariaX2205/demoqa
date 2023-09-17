from pages.base_page import BasePage

from components.components import WebElement

# import time - нужен для визуализации отработки теста.


class DemoQa(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver,
                         self.base_url)  # метод инит по-другому не назвать,
        # поэтому нужн супер. без супер по умолчанию возьмется только 1 метод, поледний.
        # супер нужен когда у нас в разных классах одинаковые методы. она нужна в любом специальном (магическом) методе
        self.icon = WebElement(driver, '#app > header > a')
        self.btn_elements = WebElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')
        self.footer = WebElement(driver, '#app > footer > span')


    # это стандартные строчки, они всегда есть в проектах вначале
    # эти переменные исп-ся только в методах, не в тестах, поэтому тх лучше сделать
    # приватными (доб __ перед названием, от этих обьектов мы не сможем получить данные)
    # def exist_icon(self):
    #     time.sleep(3)
    #     try:
    #         self.icon.find_element(locator='#app > header > a')
    #     except NoSuchElementException:
    #         return False
    #     return True

    # def click_on_the_icon(self):
    #     self.find_element(locator='#app > header > a').click()
    #
    # def click_on_the_btn_element(self):
    #     self.find_element(locator='#app > div > div > div.home-body > div > div:nth-child(1)').click()
