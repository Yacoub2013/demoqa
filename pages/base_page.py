
from selenium.webdriver.common.by import By
import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver # в селениум всегда работаем через обьект driver
        self.base_url = "https://demoqa.com/"
    def visit(self): #отправляемся на сайт demoqa.com
        return self.driver.get(self.base_url)


    def find_element(self,locator): #метод поиска
        time.sleep(3)
        return self.driver.find_element(By.CSS_SELECTOR, locator)

    def get_url(self):
        return self.driver.current_url
    def equale_url(self):
        if self.get_url() == "https://demoqa.com/":
            return True
        return False









