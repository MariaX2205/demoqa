from pages.form_page import FormPage
from pages.text_box import TextBox
from conftest import browser
import time


def test_text_box(browser):
    page = TextBox(browser)
    page.visit()
    page.full_name.send_keys('Mr. Sherlock Holmes')
    page.current_address.send_keys('London, Baker str., 221-B')
    time.sleep(4)
    page.submit_btn.click()
    time.sleep(10)
    assert page.output_name.exist()
    assert page.output_cur_address.exist()
