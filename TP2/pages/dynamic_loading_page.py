from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import yaml

global urls
with open("pages/urls.yaml", 'r') as stream:
    urls = yaml.safe_load(stream)


class DynamicLoadingPage(BasePage):
    #urls
    DYNAMIC_LOADING_URL = urls["DYNAMIC_LOADING_URL"]
    #locators
    EXEMPLE_2_LINK_LOCATOR = (By.XPATH, "//a[contains(text(), 'Example 2')]")
    START_BUTTON_LOCATOR = (By.XPATH, "//button[contains(text(), Start)]")
    MESSAGE = (By.XPATH, "//h4[contains(text(), 'Hello World')]")


    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
