from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class Login_page(BasePage):


    """ Locators for Login Page - Object repository"""
    DOMAIN_ID = (By.ID, 'id_username')
    PASSWORD = (By.ID, 'id_password')
    SIGN_IN = (By.TAG_NAME, "button")
    LOGOUT = (By.XPATH, "//a[contains(text(),'Logout')]")

    """ Locators for RTV module"""
    SHIP_RECEIVE = (By.XPATH, "//a[contains(text(),'Ship/Receive')]")
    RTV_ELE = (By.XPATH, "//a[contains(text(),'RTV')]")
    UPLOAD_FILE = (By.XPATH, "//input[@value='Upload CSV']")
    OK_UPLOAD = (By.XPATH, "//button[@id='infoModalButton']")
    RTV_TABLE = (By.CSS_SELECTOR, "#rtv-table")
    RTV_TABLE_BODY = (By.TAG_NAME, 'tbody')
    RTV_TABLE_CELL = (By.TAG_NAME, 'td')
    SUBMIT_RTV = (By.CSS_SELECTOR, "#submitBtn")
    SUBMIT_CONFIRM_RTV = (By.CSS_SELECTOR, "#onlyHeaderModal-btn-submit")
    SUBMIT_SUCCESSFUL_RTV = (By.XPATH, "//button[contains(text(),'Ok')]")
    # SUBMIT_SUCCESSFUL_RTV = (By.XPATH, "//button[normalize-space()='Ok']")


    """ Constructor of the Page class"""
    def __init__(self, driver):
        super().__init__(driver)

    """ Page Actions"""

    """This is used to get the page title"""
    def get_login_page_title(self, title):
        return self.get_title(title)

    """This used to get the SIGIN link is visible or not"""
    def is_signin_link_exists(self):
        return self.is_visible(self.SIGN_IN)

    """This used to Login to App"""
    def do_login(self, username, password):
        self.send_key(self.DOMAIN_ID, username)
        self.send_key(self.PASSWORD, password)
        self.click(self.SIGN_IN)

    """This is used to hover on SHIP/RECEIVE bootstrap dropdown"""
    def hover_ship_receive(self):
        return self.hover(self.SHIP_RECEIVE)

    """This is used to click on RTV in dropdown SHIP/RECEIVE """
    def click_rtv(self):
        self.click(self.RTV_ELE)

    def send_csv_file(self, text):
        self.send_key_to_upload_file(self.UPLOAD_FILE, text)

    def click_ok_uplaod(self):
        self.click(self.OK_UPLOAD)

    def click_upload(self):
        self.click(self.UPLOAD_FILE)

    def is_upload_link_visible(self):
        return self.is_visible(self.UPLOAD_FILE)

    def simplus_logout(self):
        return self.do_logout(self.LOGOUT)

    def rtv_table(self):
        return self.get_find_element(self.RTV_TABLE)

    def submit_rtv(self):
        self.click(self.SUBMIT_RTV)

    def submit_confirm_rtv(self):
        self.click(self.SUBMIT_CONFIRM_RTV)

    def submit_successful_rtv(self):
        self.click(self.SUBMIT_SUCCESSFUL_RTV)
























