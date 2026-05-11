from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import yaml


global urls
global credentials
with open("pages/urls.yaml", 'r') as stream:
    urls = yaml.safe_load(stream)


class AddRemoveElementsPage(BasePage):
    #urls
    ADD_REMOVE_ELEMENTS_URL = urls["URLS"]["ADD_REMOVE_ELEMENTS_URL"]
    ADD_ELEMENT_BUTTON = (By.XPATH, "//button[@onclick = 'addElement()']")
    DELETE_ELEMENT_LOCATORS = (By.XPATH, "//button[@onclick = 'deleteElement()']")
    FIRST_BUTTON = (By.XPATH, "//*[@id='elements']/button[1]")

    #locators

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

    def get_element(self, element_locator):
        element =  self.driver.find_element(*element_locator)
        return element

    def check_absence_of_element(self, element):
        absence_of_element = self.wait.until(EC.staleness_of(element))
        assert absence_of_element == True, "Elements should be gone, but aren't"
