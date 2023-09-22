import pytest
from selenium import webdriver


@pytest.fixture(
    scope="session")  # запускается до теста. отрбатывает на сессиюб есть еще на кукию это фича пйтеста. Есть еще декораторы, это элементы языка программирования
def browser():
    driver = webdriver.Chrome()
    driver.set_window_size(1000, 1000)
    yield driver  # это аналог return но не возвращает ничего
    driver.quit()  # функция - это три этих строчки
