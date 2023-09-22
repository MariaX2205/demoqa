from pages.demoqa import DemoQa
from conftest import browser
from components.components import WebElement
from pages.elements_page import ElementsPage
import time


def test_visible_btn_sidebar(browser):
    page2 = ElementsPage(browser)
    page2.visit()
    # page2.btn_sidebar_first.click()
    # time.sleep(3)
    # assert page2.btn_sidebar_first_textbox.exist()
    assert page2.btn_sidebar_first_textbox.visible()


def test_not_visible_btn_sidebar(browser):
    page2 = ElementsPage(browser)
    page2.visit()
    assert page2.btn_sidebar_first_checkbox.visible()
    page2.btn_sidebar_first.click()
    time.sleep(2)
    assert not page2.btn_sidebar_first_checkbox.visible()
