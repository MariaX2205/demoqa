import time

from conftest import browser
from pages.droppable import Droppable
from selenium.webdriver import ActionChains
from components.components import WebElement
from pages.base_page import BasePage


# action_chains = ActionChains(browser)
# action_chains.drag_and_drop(element, target).perform


def test_drag_and_drop(browser):
    page = Droppable(browser)
    page.visit()
    action_chains = ActionChains(browser)
    assert page.drop.check_css('backgroundColor', 'rgba(0, 0, 0, 0)')
    action_chains.drag_and_drop(page.drag.find_element(), page.drop.find_elements()).perform()
    time.sleep(1)

    assert page.drop.check_css('backgroundColor', 'rgba(70, 130, 180, 1)')
    time.sleep(1
               )
    action_chains.drag_and_drop_by_offset(page.drag.find_element(), -200, 0).perform()

    time.sleep(1)
    assert page.drop.check_css('backgroundColor', 'rgba(70, 130, 180, 1)')
