from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import yaml
import time

global urls
with open("pages/urls.yaml", 'r') as stream:
    urls = yaml.safe_load(stream)

class BasePage:
    #URLs
    BASE_URL = urls["BASE_URL"]

    def __init__(self,driver,timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver,timeout)

    def open(self, url):
        self.driver.get(url)

    def check_url(self, url):
        self.wait.until(EC.url_matches(url))

    def check_presence_of_element(self, element):
        self.wait.until(EC.presence_of_element_located(element))

    def fill_input(self, locator, text):
        search = self.driver.find_element(*locator)
        search.clear()
        search.send_keys(text)

    def click_button(self, element):
        button = self.wait.until(EC.element_to_be_clickable(element))
        button.click()

    def wait_for_ready_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))

    def check_if_enabled(self, locator, value):
        element = self.driver.find_element(*locator)
        enabled = element.is_enabled()
        assert enabled == value, f" value should be {value}, but is {enabled}"

    def find_all_elements(self, locator):
        elements = self.driver.find_elements(*locator)
        return elements

    def check_length(self, container, lenght):
        length_container = len(container)
        assert length_container == lenght, f"Lenght of the container should be {lenght} but is {length_container}"

    def check_absence_of_element(self, element):
        absence_of_element = self.wait.until(EC.staleness_of(element))
        assert absence_of_element == True, "Elements should be gone, but aren't"

    def get_element(self, element_locator):
        element =  self.driver.find_element(*element_locator)
        return element


    