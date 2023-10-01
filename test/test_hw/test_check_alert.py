import time

from pages.form_page import BasePage
from pages.alerts import Alerts
from conftest import browser


def test_timer_alert(browser):
    page = Alerts(browser)
    page.visit()
    assert not page.alert()
    page.timer_alert_btn.click()
    time.sleep(6)
    assert page.alert()
    page.alert().accept()


