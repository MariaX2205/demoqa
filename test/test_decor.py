from pages.base_page import BasePage
from conftest import browser
from components.components import WebElement
from pages.radio_btn import RadioButton
import pytest

def test_decor(browser):
    page = BasePage(browser)
    if not page.code_status():
        pytest.skip(reason=f"страница {page.base_url} недоступна")
    page.visit()
    assert page.h5_locators.check_count_elements(6)
    # for element in page.h5_locators.find_elements():
    #     assert element.text != ''


def test_radio_btn(browser):
    page = RadioButton(browser)
    page.visit()
    page.yes.click_force()
    assert page.youHaveSelected.get_text() == "You have selected Yes"
    page.impressive.click_force()
    assert page.youHaveSelected.get_text() == 'You have selected Impressive'
    assert 'disabled' in page.no.get_dom_attribute('class')
