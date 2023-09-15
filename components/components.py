from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class WepElement:
    def __init__(self, driver, locator=''):
        self.driver = driver
        self.locator = locator

    def click(self):
        self.find_element().click()

    def find_element(self):   #метод поиска
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def exist(self):
        try:
            self.find_element()  #вызываем метод который мы создале в родителе
        except NoSuchElementException:
            return False
        return True
    def get_text(self):
        return str(self.find_element().text)