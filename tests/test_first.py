import time

import allure
from selenium.webdriver.remote.webelement import WebElement


def test_1(browser):
    url = 'https://google.com'
    query = 'Query'

    with allure.step(f'Открываем страницу "{url}"'):
        browser.get(url)
    with allure.step('Проверяем что поле поиска отображается'):
        main_input: WebElement = browser.find_element_by_css_selector('[name=q]')
        assert main_input.is_displayed()
    with allure.step(f'Вводим поисковой запрос "{query}"'):
        main_input.send_keys(query)
        with allure.step('Ждем 1 сек'):
            time.sleep(1)
    with allure.step('Проверяем что листбокс быстрого поиска отобразился'):
        assert browser.find_element_by_css_selector('ul[role="listbox"]').is_displayed()

