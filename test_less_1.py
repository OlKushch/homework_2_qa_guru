from selene.support.shared import browser
from selene import be, have
import pytest
from selenium import webdriver

@pytest.fixture
def browser_test():
    driver = webdriver.Chrome()
    browser.config.driver = driver
    browser.config.window_width = 750
    browser.config.window_height = 900

    yield
    browser.quit()
def test_selen(browser_test):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in'))

def test_invalid_search(browser_test):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('qaswedfrtggtt').press_enter()
    browser.element('[id="search"]').should(have.text('По запросу qaswedfrtggtt ничего не найдено'))
