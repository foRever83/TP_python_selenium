from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from pages.base_page import BasePage
import time
import yaml


global urls
global credentials
with open("pages/urls.yaml", 'r') as stream:
    urls = yaml.safe_load(stream)

with open("pages/credentials.yaml", 'r') as stream:
    credentials = yaml.safe_load(stream)

class DropdownPage(BasePage):
    #urls
    DROPDOWN_URL = urls["URLS"]["DROPDOWN_URL"]
    #credentials
    USERNAME = credentials["credentials"]["USERNAME"]
    PASSWORD = credentials["credentials"]["PASSWORD"]
    #locators
    DROPDOWN_LIST = (By.ID, "dropdown")
    OPTION_1 = "Option 1"
    OPTION_2 = "Option 2"

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

    def select_in_list(self, option):
        dropdown_element = self.driver.find_element(*self.DROPDOWN_LIST)
        dropdown = Select(dropdown_element)
        dropdown.select_by_visible_text(option)

    def check_selection(self, text):
        dropdown_element = self.driver.find_element(*self.DROPDOWN_LIST)
        dropdown = Select(dropdown_element)
        selected_option = dropdown.first_selected_option
        selected_text = selected_option.text
        assert selected_text == text, f"Incorrect option {selected_text} selected instead of expected option {text} "


    