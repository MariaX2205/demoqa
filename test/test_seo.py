from pages.demoqa import DemoQa
from conftest import browser
from components.components import WebElement
from pages.elements_page import ElementsPage


def test_seo(browser):
    page = DemoQa(browser)
    page.visit()
    assert page.get_title() == 'DEMOQA'
