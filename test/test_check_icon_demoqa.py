from pages.demoqa import DemoQa
from conftest import browser
from components.components import WebElement

def test_icon_exist(browser):
    demo_page = DemoQa(browser)
    demo_page.visit()
    demo_page.icon.click()
    assert demo_page.equal_url()
    assert demo_page.icon.exist()





    # browser.get("https://demoqa.com/")
    # icon = browser.find_elements(By.CSS_SELECTOR, '#app > header > a')
    #
    # if icon is None:
    #     print('элемент не найден')
    # else:
    #     print("Элемент найден")
