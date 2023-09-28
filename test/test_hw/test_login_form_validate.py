from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from components.components import WebElement
from pages.form_page import FormPage
from conftest import browser


def test_login_form(browser):
    page = FormPage(browser)
    page.visit()

    assert page.first_name.get_dom_attribute('placeholder') == 'First Name'
