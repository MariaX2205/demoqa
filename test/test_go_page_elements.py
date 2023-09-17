from pages.demoqa import DemoQa
from conftest import browser
from pages.elements_page import ElementsPage


def test_go_to_page_elements(browser):
    g_page = DemoQa(browser)
    elem = ElementsPage(browser)
    g_page.visit()
    assert g_page.equal_url()
    g_page.btn_elements.click()
    assert elem.equal_url()
