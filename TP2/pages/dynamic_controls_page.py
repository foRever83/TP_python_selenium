from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import yaml

global urls
with open("pages/urls.yaml", 'r') as stream:
    urls = yaml.safe_load(stream)


class DynamicControlsPage(BasePage):
    #urls
    DYNAMIC_CONTROLS_URL = urls["DYNAMIC_CONTROLS_URL"]
    #locators
    CHECKBOX_LOCATOR = (By.XPATH, "//input[@type = 'checkbox']")
    ADD_REMOVE_BUTTON = (By.XPATH, "//button[@onclick = 'swapCheckbox()']")
    INPUT = (By.XPATH, "//form[@id='input-example']//input")
    DISABLED_INPUT = (By.CSS_SELECTOR, "input:disabled")
    ENABLED_MESSAGE = (By.XPATH, "//p[@id='message' and contains(text(), 'enabled')]")
    DISABLED_MESSAGE = (By.XPATH, "//p[@id='message' and contains(text(), 'disabled')]")
    #ENABLED_INPUT = (By.CSS_SELECTOR, "input:enabled")
    ENABLE_DISABLE_BUTTON = (By.XPATH, "//button[@onclick = 'swapInput()']")

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

    def check_box(self, locator):
        checkbox = self.driver.find_element(*locator)
        checkbox.click()