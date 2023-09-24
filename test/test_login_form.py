from selenium import webdriver
from conftest import browser
from selenium.common.exceptions import NoSuchElementException
from pages.form_page import FormPage
import time
from selenium.webdriver.support.ui import Select


def test_login_form(browser):
    form_page = FormPage(browser)

    form_page.visit()
    assert not form_page.modal_dialog.exist()
    time.sleep(2)
    form_page.first_name.send_keys('tester')  # заполнение всех полей лучше выынести в отдельный метод,
    form_page.last_name.send_keys('testerovich')  # под классом страницы FormPage, т.к. они работ. только на ней
    form_page.user_email.send_keys('test@ttt.tt')
    form_page.gender_radio_1.click_force()
    form_page.user_number.send_keys('9992223344')
    time.sleep(2)
    form_page.hobbies.click_force()
    time.sleep(4)
    form_page.address.send_keys('my address is the Earth')
    form_page.btn_submit.click_force()
    time.sleep(2)

    assert form_page.modal_dialog.exist()
    form_page.btn_close_modal.click_force()


def test_state_n_city_fill_in(browser):
    page = FormPage(browser)
    page.visit()
    page.state.click_force()
    page.state.send_keys('NCR')
    page.state.enter()
    time.sleep(4)
    page.city.click_force()
    page.city.send_keys('Dehli')
    page.city.enter()
    time.sleep(4)



    # page.city_arrow.click_force()
    # page.city.click_force()
    # page.city.send_keys('Dehli')
