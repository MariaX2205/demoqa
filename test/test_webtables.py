from conftest import browser
from pages.webtables import Webtables


def test_webtables(browser):
    page = Webtables(browser)
    page.visit()

    assert not page.block.exist()

    while page.btn_delete_row.exist():
        page.btn_delete_row.click()

    assert page.block.exist()
