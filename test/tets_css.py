from pages.elements_page import ElementsPage
from conftest import browser


def test_flex_menu(browser):
    page = ElementsPage(browser)
    page.visit()

    assert page.block_menu.check_css('flex', '0 0 25%')
    assert page.block_menu.check_css('max-width', '25%')

    browser.set_window_size(375, 628)

    assert page.block_menu.check_css('flex', '0 0 100%')
    assert page.block_menu.check_css('max-width', '100%')

    browser.set_window_size(1000, 1000)
