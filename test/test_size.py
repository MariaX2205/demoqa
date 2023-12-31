from pages.demoqa import DemoQa
from conftest import browser
from components.components import WebElement
from pages.elements_page import ElementsPage
import time


def test_seo(browser):
    page = DemoQa(browser)
    page.visit()
    browser.set_window_size(1000, 300)
    time.sleep(2)
    browser.set_window_size(1000, 1000)
def test_visible_nav_bar(browser):
    page = ElementsPage(browser)
    page.visit()
    browser.set_window_size(320, 628)
    assert page.size_check.visible()
    browser.set_window_size(1024, 1396)
    assert not page.size_check.visible()
    browser.set_window_size(1000, 1000)