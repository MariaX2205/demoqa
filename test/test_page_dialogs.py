from pages.demoqa import DemoQa
from conftest import browser
from components.components import WebElement
from pages.modal_dialogs import Modal_dialogs


def test_modal_elements(browser):
    page = Modal_dialogs(browser)
    page.visit()
    assert page.btn_loc_5.check_count_elements(count=5)
