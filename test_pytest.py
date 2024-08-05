import time

from selene import browser, be, have

def test_first():
    browser.open("")
    time.sleep(5)
    browser.element('[name="q"]').should(be.blank).type('qweretrertyuyu').press_enter()
    browser.element('[id="search"]').should(be.not_.visible)

def test_second():
    browser.open("")
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))