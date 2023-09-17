from pages.demoqa import DemoQa
from conftest import browser
from components.components import WebElement
from pages.elements_page import ElementsPage


def test_demoqa_footer(browser):
    page1 = DemoQa(browser)
    page1.visit()
    assert page1.footer.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'


def test_visit_via_page(browser):
    page1 = DemoQa(browser)
    page1.visit()
    page1.icon.click()
    page = ElementsPage(browser)
    page.visit()
    assert page.text_in_center.get_text() == 'Please select an item from left to start practice.'
