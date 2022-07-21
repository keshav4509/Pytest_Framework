from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import os
import pytest


@pytest.fixture(params=['chrome'], scope='class')
def init_driver(request):
    if request.param == 'chrome':
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
        web_driver.implicitly_wait(10)
        web_driver.delete_all_cookies()
        web_driver.get("https://simplus-mdm-uat.moreconnect.co.in/accounts/login/")
        web_driver.maximize_window()
    if request.param == 'firefox':
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        web_driver.implicitly_wait(10)
        web_driver.delete_all_cookies()
        web_driver.get("https://simplus-mdm-uat.moreconnect.co.in/accounts/login/")
        web_driver.maximize_window()
    request.cls.driver = web_driver
    yield
    # web_driver.close()
