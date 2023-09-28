import logging
from lib2to3.pgen2 import driver

from components.components import WebElement


class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver  # в селениум всегда работаем через обьект driver
        self.base_url = base_url
        self.head_viewport = WebElement(driver, 'head>meta')

    def visit(self):  # отправляемся на сайт demoqa.com
        return self.driver.get(self.base_url)

    def back(self):
        return self.driver.back()

    def forward(self):
        return self.driver.forward()

    def refresh(self):
        return self.driver.refresh()

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def equal_url(self):
        if self.get_url() == self.base_url:
            return True
        return False

    def alert(self):
        try:
            return self.driver.switch_to.alert
        except Exception as ex:
            logging.log(1, ex)
            return False





