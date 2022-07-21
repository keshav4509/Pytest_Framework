from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest


@pytest.fixture(scope='class')
def init_chrome_driver(request):
    driver_chrome = webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver = driver_chrome
    yield
    driver_chrome.close()


@pytest.mark.usefixtures('init_chrome_driver')
class Base_Chrome_Test:
    pass


class Test_google_chrome(Base_Chrome_Test):
    def test_google_title_with_chrome(self):
        self.driver.get("https://www.google.com/")
        assert self.driver.title == 'Google'





