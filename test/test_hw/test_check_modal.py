import time

from conftest import browser
from pages.modal_dialogs import Modal_dialogs
from selenium.webdriver import ActionChains
import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

timeout = 5


def test_check_modal(browser):
    page = Modal_dialogs(browser)

    try:
        WebDriverWait(browser, timeout).until(page.large_modal)
    except:
        TimeoutException
        pytest.skip


    page.visit()

    assert page.small_modal.exist()
    assert page.large_modal.exist()

    page.small_modal.click()
    assert page.small_m_dial.exist()
    page.close_small_modal.click()

    page.large_modal.click()
    assert page.large_modal.exist()
    page.close_large_modal.click()
