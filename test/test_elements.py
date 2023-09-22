from pages.demoqa import DemoQa
from conftest import browser
from components.components import WebElement
from pages.elements_page import ElementsPage


def test_find_elements(browser):
    page = ElementsPage(browser)
    page.visit()
    assert page.btns_first_menu.check_count_elements(count=9)
