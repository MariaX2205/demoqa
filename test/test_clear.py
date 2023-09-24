from pages.text_box import TextBox
from components.components import WebElement
from pages.base_page import BasePage
from conftest import browser
import time


def test_clear(browser):
    page = TextBox(browser)
    page.visit()
    page.full_name.send_keys('My Name Is...')
    time.sleep(2)
    page.full_name.clear()
    time.sleep(2)
    assert page.full_name.get_text() == ''
