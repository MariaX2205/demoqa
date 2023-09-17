from pages.demoqa import DemoQa
from conftest import browser
from components.components import WebElement
from pages.elements_page import ElementsPage


def test_page_elements(browser):
    page = ElementsPage(browser)
    page.visit()
    assert page.text_elements.get_text() == 'Elements'
    assert page.icon.exist()
    assert page.btn_sidebar_first.exist()
    assert page.btn_sidebar_first_textbox.exist()

