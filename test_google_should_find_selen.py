import string
import pytest
import random
from selene import be, have
from selene.support.shared import browser


@pytest.fixture
def browser_open():
    browser.open('https://google.com')
    browser.driver.maximize_window()


def test_successful_search(browser_open):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_unsuccessful_search(browser_open):
    browser.element('[name="q"]').should(be.blank).type(
        ''.join(random.choice(string.ascii_letters) for _ in range(12))).press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
    print('  Поиск не дал результатов')
