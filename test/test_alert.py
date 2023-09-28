from pages.alerts import Alerts
from conftest import browser
import time


def test_alert(browser):
    page = Alerts(browser)
    page.visit()
    assert not page.alert()
    page.alert_button.click()
    time.sleep(2)
    assert page.alert()
    page.alert().accept()  # это имитация кнопки ОК. Чтобы закрыть окно.


def test_alert_text(browser):
    page = Alerts(browser)
    page.visit()
    page.alert_button.click()
    assert page.alert().text == 'You clicked a button'
    page.alert().accept()
    assert not page.alert()
def test_confirm(browser):
    page = Alerts(browser)
    page.visit()
    page.confirm_btn.click()
    time.sleep(2)
    page.alert().dismiss()
    assert page.confirm_result.get_text() == 'You selected Cancel'

def test_prompt(browser):
    page = Alerts(browser)
    page.visit()
    page.prompt.click()
    time.sleep(2)
    page.alert().send_keys('Maria')
    page.alert().accept()
    assert page.promptResult.get_text() == 'You entered Maria'
    time.sleep(2)