import time
import pytest
from Config.config import TestData
from Pages.Inventory_Adjustment import Inventory_Adjustment
from Tests.test_base import BaseTest
from Pages.Login_Page import Login_page
from selenium.webdriver.common.by import By


class Test_Inventory_Adjustment(BaseTest):

    def test_inventory_adjustment_flow(self):
        self.loginPage = Login_page(self.driver)
        self.inventoryAdjustment = Inventory_Adjustment(self.driver)
        self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)
        self.inventoryAdjustment.click_inventory_management()
        self.inventoryAdjustment.click_inventory_adjustment_link()
        self.inventoryAdjustment.click_select_reason_drop_down()
        reason_list = self.inventoryAdjustment.get_select_reason_list()
        for reason in reason_list:
            print("Reason:", reason.text)

        self.inventoryAdjustment.click_store_dump()
        self.inventoryAdjustment.click_add_inventory_row()
        self.inventoryAdjustment.click_item()
        time.sleep(10)
        item_list = self.inventoryAdjustment.get_all_item_list()
        for item in item_list:
            print(item.text)









