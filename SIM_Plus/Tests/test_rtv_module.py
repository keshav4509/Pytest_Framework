import time
import pytest
from Config.config import TestData
from Tests.test_base import BaseTest
from Pages.Login_Page import Login_page
from selenium.webdriver.common.by import By


class Test_login(BaseTest):

    def test_signin_link(self):
        self.loginPage = Login_page(self.driver)
        flag = self.loginPage.is_signin_link_exists()
        assert flag

    def test_rtv_module(self):
        self.loginPage = Login_page(self.driver)
        self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)
        self.loginPage.hover_ship_receive()
        self.loginPage.click_rtv()
        time.sleep(2)
        csv_file_path = r"/Users/keshavsinha/pythonProject/SIM_Plus/Test_Data/csv_rtv_data/rtv_upload_template.csv"
        self.loginPage.send_csv_file(csv_file_path)
        time.sleep(3)
        table = self.loginPage.rtv_table()
        body = table.find_element(By.TAG_NAME, 'tbody')
        cells = body.find_elements(By.TAG_NAME, 'td')
        table_row = []
        for cell in cells:
            table_row.append(cell.text)
        assert table_row[0] == "2110861", "Supplier value doesnt matched"
        self.loginPage.click_ok_uplaod()
        self.loginPage.submit_rtv()
        self.loginPage.submit_confirm_rtv()
        time.sleep(2)
        self.loginPage.submit_successful_rtv()
