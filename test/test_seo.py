import time

import pytest

from pages.demoqa import DemoQa
from conftest import browser
from components.components import WebElement
from pages.elements_page import ElementsPage


def test_seo(browser):
    page = DemoQa(browser)
    page.visit()
    assert page.get_title() == 'DEMOQA'


from pages.accordian import Accordian
from pages.alerts import Alerts
from pages.demoqa import DemoQa
from pages.browser_tab import BrowserTab


@pytest.mark.parametrize("pages", [Accordian, Alerts, DemoQa, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert page.get_title() == 'DEMOQA'
