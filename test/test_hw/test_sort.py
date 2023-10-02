import pytest
from pages.webtables import Webtables

def test_sort(browser):
    page = Webtables(browser)
    page.visit()
    assert page.tableElement.get_text() == "Cierra"
    page.table_1_Column.click()
    assert page.tableElement.get_text() == "Alden"

