                         #файл conftest.py должен быть всегда, даже если пустой
import pytest
from selenium import webdriver

@pytest.fixture(scope="session") # декоратор, говорит о том что фун-ция (pytest) становится фекстурой
def browser():
    driver = webdriver.Chrome()
    yield driver   # аналог return но не завершает её выполнение (возвращаем driver)
    driver.quit()    # драйвер закрывется


