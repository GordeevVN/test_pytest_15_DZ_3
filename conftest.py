import pytest
from selene import browser


@pytest.fixture(autouse=True)
def setting_browser():
    # задаем размер окна браузера (вместо этого комментария нужно подставить код из примера выше как задать размер окна браузера)
    browser.config.window_height = 1000  # задает высоту окна браузера
    # закрываем браузер после выполнения теста (вместо этого комментария нужно подставить код из примера выше как закрыть браузер)
    browser.config.window_width = 1600  # задает ширину окна браузера
    browser.config.base_url = 'https://www.google.com'
    yield
    browser.quit() # закрывает браузер после выполнения теста
