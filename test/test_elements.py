from pages.demoqa import DemoQa
from conftest import browser
from pages.checkbox import Checkbox
from pages.elements_page import ElementsPage


def test_find_elements(browser):
    page = ElementsPage(browser)
    page.visit()
    assert page.btns_first_menu.check_count_elements(count=9)


def test_count_checkbox(browser):
    page = Checkbox(browser)
    page.visit()
    assert page.checkbox.check_count_elements(count=1)
    page.cl_cbx.click()
    assert page.checkbox.check_count_elements(count=17)
    page.refresh()
    assert page.checkbox.check_count_elements(count=1)
