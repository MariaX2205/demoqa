import time
from pages.slider import Slider
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


def test_slider(browser):
    page = Slider(browser)

    page.visit()

    #move = ActionChains(browser)
    arrow = page.sliderArrow

    while not page.sliderValue.get_dom_attribute('value') == '50':
        arrow.send_keys(Keys.ARROW_RIGHT)

    # move.click_and_hold(arrow).move_by_offset(25, 0).release().perform()

    # move.click_and_hold(page.find_element() sliderArrow).pause(1).move_by_offset(50, 0).release().perform()
    # time.sleep(2)

    assert page.sliderValue.get_dom_attribute('value') == '50'
