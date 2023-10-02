import time

from conftest import browser
from selenium.common.exceptions import NoSuchElementException
from pages.webtables import Webtables


def test_webtables(browser):
    page = Webtables(browser)
    page.visit()

    assert not page.block.exist()

    while page.btn_delete_row.exist():
        page.btn_delete_row.click()

    assert page.block.exist()


def test_add_btn(browser):
    page = Webtables(browser)
    page.visit()

    page.add_btn.click()

    page.w_firstName.send_keys("Ivan")
    page.w_LastName.send_keys("Ivanovich")
    page.w_userEmail.send_keys("Ivam@gmail.com")
    page.w_age.send_keys("35")
    page.w_salary.send_keys("100000")
    page.w_department.send_keys("QA")
    # time.sleep(5)
    page.submit_btn.click()
    time.sleep(3)

    page.pencil.click_force()
    page.w_firstName.clear()

    page.w_firstName.send_keys('NICK')
    page.submit_btn.click_force()
    assert page.tableFirstName.get_text() == 'NICK'
    time.sleep(2)

    page.btn_delete_row.click()
    time.sleep(2)


def test_next_prev(browser):
    page = Webtables(browser)
    page.visit()

    page.select_area.scroll_to_element()
    page.select_area.click()
    page.select_5.click()

    assert page.previous_btn.get_dom_attribute('class') == '-btn'
    assert page.next_button.get_dom_attribute('class') == '-btn'

    for i in range(3):
        page.add_btn.click()

        page.w_firstName.send_keys("Ivan")
        page.w_LastName.send_keys("Ivanovich")
        page.w_userEmail.send_keys("Ivam@gmail.com")
        page.w_age.send_keys("35")
        page.w_salary.send_keys("100000")
        page.w_department.send_keys("QA")
        page.submit_btn.click()
    time.sleep(2)

    assert page.page2.exist()

    page.next_button.click()
    assert page.jump_to_page.get_dom_attribute('value') == '2'
    time.sleep(3)
    page.previous_btn.click()
    assert page.jump_to_page.get_dom_attribute('value') == '1'
