from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from conftest import browser

def test(browser):
    browser.get("https://demoqa.com/")
    icon = browser.find_elements(By.CSS_SELECTOR, '#app > header > a')

    if icon is None:
        print('элемент не найден')
    else:
        print("Элемент найден")
