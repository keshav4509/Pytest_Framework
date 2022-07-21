
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest
from Config.config import TestData


def pytest_addoption(parser):
    parser.addoption("--chrome", action="store", default="chrome")


@pytest.fixture()
def get_browser(request):
    _browser = request.config.getoption("--browser")
    return _browser


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request, get_browser):
    # if request.param == 'chrome':
    if get_browser == "chrome":
        # web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
        _web_driver = webdriver.Chrome(ChromeDriverManager().install())
        _web_driver.delete_all_cookies()
        _web_driver.get(TestData.BASE_URL)
        _web_driver.maximize_window()
    if request.param == 'firefox':
        _web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = _web_driver
    yield
    # web_driver.close()


