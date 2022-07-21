import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import pytest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


class Test_Simplus(BaseTest):


    def test_simplus_rtv(self):
        login = self.driver.find_element(By.ID, 'id_username')
        paswd = self.driver.find_element(By.ID, 'id_password')
        submit = self.driver.find_element(By.TAG_NAME, "button")
        login.send_keys('store_uat_2040')
        paswd.send_keys('more2021')
        submit.click()
        ship_recv = self.driver.find_element(By.XPATH, "//a[contains(text(),'Ship/Receive')]")
        act_chains = ActionChains(self.driver)
        act_chains.move_to_element(ship_recv).perform()

        rtv_ele = self.driver.find_element(By.XPATH, "//a[contains(text(),'RTV')]")
        rtv_ele.click()
        upload_file = self.driver.find_element(By.XPATH, "//input[@value='Upload CSV']")
        upload_file.send_keys(
            "/Users/keshavsinha/pythonProject/API_Testing/Test_Data/csv_rtv_data/rtv_upload_template.csv")
        time.sleep(3)
        modal_alert = self.driver.find_element(By.XPATH, "//button[@id='infoModalButton']")
        modal_alert.click()
        table = self.driver.find_element(By.CSS_SELECTOR, "#rtv-table")
        # self.driver.get_screenshot_as_file('RTV_table_data')
        # header = table.find_elements(By.TAG_NAME, 'th')
        # value = table.find_elements(By.TAG_NAME, 'tr')
        body = table.find_element(By.TAG_NAME, 'tbody')
        cells = body.find_elements(By.TAG_NAME, 'td')
        for cell in cells:
            assert cell.text == '2110861', 'Supplier value doesnt matched'
            break
        submit_rtv = self.driver.find_element(By.CSS_SELECTOR, "#submitBtn")
        submit_rtv.click()
        time.sleep(3)
        submit_confirm = self.driver.find_element(By.CSS_SELECTOR, "#onlyHeaderModal-btn-submit")
        submit_confirm.click()
        time.sleep(3)
        submit_successful = self.driver.find_element(By.XPATH, "//button[contains(text(),'Ok')]")
        submit_successful.click()


    def test_simplus_rtv_negative_scenario(self):
        login = self.driver.find_element(By.ID, 'id_username')
        paswd = self.driver.find_element(By.ID, 'id_password')
        submit = self.driver.find_element(By.TAG_NAME, "button")
        login.send_keys('store_uat_2040')
        paswd.send_keys('more2021')
        submit.click()
        ship_recv = self.driver.find_element(By.XPATH, "//a[contains(text(),'Ship/Receive')]")
        act_chains = ActionChains(self.driver)
        act_chains.move_to_element(ship_recv).perform()

        rtv_ele = self.driver.find_element(By.XPATH, "//a[contains(text(),'RTV')]")
        rtv_ele.click()
        upload_file = self.driver.find_element(By.XPATH, "//input[@value='Upload CSV']")
        upload_file.send_keys(
            "/Users/keshavsinha/pythonProject/API_Testing/Test_Data/csv_rtv_data/rtv_upload_template_neg.csv")
        time.sleep(3)
        rtv_error_table = self.driver.find_element(By.CSS_SELECTOR, "#error-table")
        body = rtv_error_table.find_element(By.TAG_NAME, 'tbody')
        cells = body.find_elements(By.TAG_NAME, 'td')
        error_row_values = []
        for cell in cells:
            error_row_values.append(cell.text)
        assert error_row_values[5] == 'Quantity should be less than or equal to SOH', \
                                                            'REASON for RTV error Table not found'
        error_modal_alert = self.driver.find_element(By.CSS_SELECTOR, "#infoModalButton").click()



    def test_grn_module(self):
        self.driver.find_element(By.ID, 'id_username').send_keys('store_uat_2040')
        self.driver.find_element(By.ID, 'id_password').send_keys('more2021')
        self.driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Sign In')]").click()
        self.driver.find_element(By.ID, 'navbarDropdownMenuLink').click()
        self.driver.find_element(By.LINK_TEXT, 'Inventory Adjustment').click()
        self.driver.find_element(By.ID, 'select2-reason-dropdown-container').click()
        # reason_list = driver.find_element(By.CSS_SELECTOR, "li.select2-results__option--highlighted")
        reason_list = self.driver.find_elements(By.CSS_SELECTOR, 'span.select2-results')

        print(reason_list)
        for reason in reason_list:
            print("reason:", reason.text)
        self.driver.implicitly_wait(3)
        reason_dump = self.driver.find_element(By.XPATH, "/html/body/span/span/span[2]/ul/li[2]")
        reason_dump.click()
        print(reason_dump)

        # add row
        self.driver.find_element(By.ID, 'addInventoryRow').click()

        # select the item
        self.driver.find_element(By.ID, 'select2-item0-select-container').click()
        time.sleep(10)
        item_list = self.driver.find_elements(By.CSS_SELECTOR, "#select2-item0-select-results")
        for item in item_list:
            print(item.text)

        # item_list = Select(WebDriverWait(self.driver, 20).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.select2-results'))))
        # print([option.get_attribute("value") for option in item_list.options])
        # time.sleep(5)
        # for opt in item_list1.options:
        #     # get option text
        #     print(opt.text)

