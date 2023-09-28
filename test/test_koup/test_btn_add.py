from pages.herokuapp import HerokuappPage
from pages.herokuapp_elemnts import AddRemElem
from conftest import browser


def test_btn_add(browser):
    page = HerokuappPage(browser)
    page2 = AddRemElem(browser)
    page.visit()
    page.link.click()
    assert page2.equal_url()

    assert page2.button.get_text() == 'Add Element'

    assert page2.button.get_dom_attribute('onclick') == 'addElement()'
    for i in range(4):
        page2.button.click()
    assert page2.btn_del.check_count_elements(4)
    for element in page2.btn_del.find_elements():
        assert element.text == 'Delete'
    while page2.btn_del.exist():
        page2.btn_del.click()

    assert not page2.btn_del.exist()
