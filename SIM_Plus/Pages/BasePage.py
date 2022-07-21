from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


"""This class is Parent of all Pages """
"""It contains all the generic methods and utilities for all the Pages"""


class BasePage:

    def __init__(self, driver):
        self.driver = driver


    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()


    def send_key(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)


    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)


    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def hover(self, by_locator):
        ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        act_chains = ActionChains(self.driver)
        act_chains.move_to_element(ele).perform()

    def esacpe_button(self, by_locator):
        ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

    def send_key_to_upload_file(self, by_locator, text):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_locator)).send_keys(str(text))

    def get_find_element(self, by_locator):
        table = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_locator))
        return table

    def do_logout(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def get_find_all_elements(self, by_locator):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(by_locator))






















