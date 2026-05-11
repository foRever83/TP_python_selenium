from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import yaml


global urls
global credentials
with open("pages/urls.yaml", 'r') as stream:
    urls = yaml.safe_load(stream)

with open("pages/credentials.yaml", 'r') as stream:
    credentials = yaml.safe_load(stream)

class LoginPage(BasePage):
    #urls
    LOGIN_URL = urls["URLS"]["LOGIN_URL"]
    #credentials
    USERNAME = credentials["credentials"]["USERNAME"]
    PASSWORD = credentials["credentials"]["PASSWORD"]
    #locators
    LOGIN_FORM_LOCATOR = (By.ID, "login")
    LOGIN_LOCATOR = (By.ID, "username")
    PASSWORD_LOCATOR = (By.ID, "password")
    LOGIN_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".fa-sign-in")
    MESSAGE_LOCATOR = (By.CLASS_NAME, 'subheader')
    LOGOUT_BUTTON_LOCATOR = (By.CSS_SELECTOR, '.button')

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

    