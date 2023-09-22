from pages.demoqa import DemoQa
from conftest import browser
from components.components import WebElement
from pages.elements_page import ElementsPage


def test_navigation(browser):
    page = DemoQa(browser)
    page.visit()
    page.btn_elements.click()
    page1 = ElementsPage(browser)
    page1.refresh()
    browser.refresh()
    browser.back()
    browser.forward()
    assert page1.equal_url()
