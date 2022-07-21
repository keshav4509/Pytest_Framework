import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import pytest


driver = None


@pytest.fixture(scope='module')
def init_driver():
    global driver
    print('------------Initialising Setup-------------')
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("https://simplus-mdm-uat.moreconnect.co.in/accounts/login/")
    driver.maximize_window()
    yield
    print('---------------Tear Down----------------')
    # driver.quit()


@pytest.mark.usefixtures('init_driver')
def test_simplus_rtv():
    login = driver.find_element(By.ID, 'id_username')
    paswd = driver.find_element(By.ID, 'id_password')
    submit = driver.find_element(By.TAG_NAME, "button")
    login.send_keys('store_uat_2040')
    paswd.send_keys('more2021')
    submit.click()
    ship_recv = driver.find_element(By.XPATH, "//a[contains(text(),'Ship/Receive')]")
    act_chains = ActionChains(driver)
    act_chains.move_to_element(ship_recv).perform()

    rtv_ele = driver.find_element(By.XPATH, "//a[contains(text(),'RTV')]")
    rtv_ele.click()
    upload_file = driver.find_element(By.XPATH, "//input[@value='Upload CSV']")
    # upload_file.click()
    upload_file.send_keys("/Users/keshavsinha/pythonProject/API_Testing/Test_Data/csv_rtv_data/rtv_upload_template.csv")
    print('hello')




