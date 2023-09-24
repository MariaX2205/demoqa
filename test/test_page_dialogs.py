from conftest import browser
from pages.modal_dialogs import Modal_dialogs
from components.components import WebElement
from pages.base_page import BasePage
from pages.demoqa import DemoQa


def test_modal_elements(browser):
    page = Modal_dialogs(browser)
    page.visit()
    assert page.btn_loc_5.check_count_elements(count=5)


def test_navigation_modal(browser):
    page = Modal_dialogs(browser)
    page2 = DemoQa(browser)
    page.visit()
    page.refresh()
    page.main_p_icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    assert page2.equal_url()
    assert page2.get_title() == 'DEMOQA'
    browser.set_window_size(1000, 1000)
