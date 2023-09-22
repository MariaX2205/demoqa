from pages.demoqa import DemoQa
from conftest import browser
from components.components import WebElement
from pages.accordian import Accordian
import time


def test_visible_accordian(browser):
    page = Accordian(browser)
    page.visit()
    assert page.element.visible()
    page.heading.click()
    time.sleep(2)
    assert not page.element.visible()
def test_visible_accordion_default(browser):
    page = Accordian(browser)
    page.visit()
    assert not page.section21.visible()
    assert not page.section22.visible()
    assert not page.section3.visible()

