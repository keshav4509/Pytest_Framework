from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class Inventory_Adjustment(BasePage):


    """ Locators for INVENTORY ADJUSTMENT Page - Object repository"""
    DROP_DOWN_INVENTORY_MANAGEMENT = (By.ID, 'navbarDropdownMenuLink')
    LINK_INVENTORY_ADJUSTMENT = (By.LINK_TEXT, 'Inventory Adjustment')
    DROP_DOWN_SELECT_REASON = (By.ID, 'select2-reason-dropdown-container')
    REASON_LIST = (By.CSS_SELECTOR, 'span.select2-results')
    REASON_STORE_DUMP = (By.XPATH, "/html/body/span/span/span[2]/ul/li[2]")
    ADD_INVENTORY_ROW = (By.ID, 'addInventoryRow')
    DROP_DOWN_ITEM = (By.ID, 'select2-item0-select-container')
    ALL_ITEM_LIST = (By.CSS_SELECTOR, "#select2-item0-select-results")


    """ Constructor of the Page class"""

    def __init__(self, driver):
        super().__init__(driver)

    """ Page Actions"""

    """This is used to click INVENTORY MANAGEMENT Drop Down."""
    def click_inventory_management(self):
        self.click(self.DROP_DOWN_INVENTORY_MANAGEMENT)


    """This is used to click INVENTORY ADJUSTMENT from Inventory Management Drop Down List."""
    def click_inventory_adjustment_link(self):
        self.click(self.LINK_INVENTORY_ADJUSTMENT)

    """This is used to click SELECT REASON Drop Down."""
    def click_select_reason_drop_down(self):
        self.click(self.DROP_DOWN_SELECT_REASON)

    """This is used to get all SELECT REASON values from Drop Down."""
    def get_select_reason_list(self):
        return self.get_find_all_elements(self.REASON_LIST)

    """This is used to click 7-STORE DUMP from Select Reason Drop Down."""
    def click_store_dump(self):
        self.click(self.REASON_STORE_DUMP)

    """This is used to click ADD INVENTORY ROW ."""
    def click_add_inventory_row(self):
        self.click(self.ADD_INVENTORY_ROW)

    """This is used to click ITEM Drop Down ."""
    def click_item(self):
        self.click(self.DROP_DOWN_ITEM)

    """This is used to get ALL ITEM values from ITEM Drop Down."""
    def get_all_item_list(self):
        return self.get_find_all_elements(self.ALL_ITEM_LIST)







