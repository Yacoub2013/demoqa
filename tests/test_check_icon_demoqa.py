from selenium.webdriver.common.by import By
from conftest import browser


def test_site_visit(browser):
    browser.get("https://demoqa.com/")
    icon = browser.find_element(By.CSS_SELECTOR, '#app > header > a')
    if icon is None:
        print('Элемент не найден')
    else:
        print('Элемент найдне')
