import time
from pages.slider import Slider
from selenium.webdriver import ActionChains
from components.components import WebElement


def test_slider(browser):
    page = Slider(browser)
    page.visit()

    move = ActionChains(browser)

    move.click_and_hold(page.sliderArrow).pause(1).move_by_offset(50, 0).release().perform()
    time.sleep(2)

    assert page.sliderValue.get_text() == '50'
