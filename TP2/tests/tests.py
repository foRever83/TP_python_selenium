from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages import dynamic_controls_page
from pages import dynamic_loading_page
import os
from datetime import datetime
import time


options = Options()
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")
#options.add_argument("--headless")

prefs = {
        "profile.password_manager_leak_detection": False,
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
options.add_experimental_option("prefs", prefs)


os.makedirs('screenshots', exist_ok=True)

def test_dynamic_controls():
    driver = webdriver.Chrome(options=options)
    page = dynamic_controls_page.DynamicControlsPage(driver)
    text = "coucou"
    attribute = "value"

    try :
        print(f"Opening url {page.DYNAMIC_CONTROLS_URL}")
        page.open(page.DYNAMIC_CONTROLS_URL)
        print("checking url")
        page.check_url(page.DYNAMIC_CONTROLS_URL)
        print("checking box")
        page.click_button(page.CHECKBOX_LOCATOR)
        print("clicking on REMOVE button")
        page.click_button(page.ADD_REMOVE_BUTTON)
        print("waiting for checkbox to disappear")
        checkbox = page.get_element(page.CHECKBOX_LOCATOR)
        page.check_absence_of_element(checkbox)
        print("clicking on ADD button")
        page.click_button(page.ADD_REMOVE_BUTTON)
        print("waiting for checkbox to appear")
        page.check_presence_of_element(page.CHECKBOX_LOCATOR)
        print("checking if form is disbaled")
        page.check_if_enabled(page.INPUT, False)
        print("clicking on ENABLE button ")
        page.click_button(page.ENABLE_DISABLE_BUTTON)
        print("waiting for presence of message")
        page.check_presence_of_element(page.ENABLED_MESSAGE)
        print("checking if form is enabled")
        page.check_if_enabled(page.INPUT, True)
        print("waiting for form to be clickable")
        page.wait_for_ready_element(page.INPUT)
        print("inputing text")
        page.fill_input(page.INPUT, text)
        print("checking text content")
        page.check_attribute(page.INPUT, attribute, text)

    except Exception as e:
        print(e)
        screenshot_name = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        driver.save_screenshot(f"screenshots/{screenshot_name}")

    finally:
        print("exiting driver")
        driver.quit()


def test_dynamic_loading():
    driver = webdriver.Chrome(options=options)
    page = dynamic_loading_page.DynamicLoadingPage(driver)

    try :
        print(f"Opening url {page.DYNAMIC_LOADING_URL}")
        page.open(page.DYNAMIC_LOADING_URL)
        print("checking url")
        page.check_url(page.DYNAMIC_LOADING_URL)
        print("clicking on link")
        page.click_button(page.EXEMPLE_2_LINK_LOCATOR)
        print("checking presence of START button")
        page.check_presence_of_element(page.START_BUTTON_LOCATOR)
        print("clicking on START button")
        page.click_button(page.START_BUTTON_LOCATOR)
        print("waiting for message to appear")
        page.check_presence_of_element(page.MESSAGE)

    except Exception as e:
        print(e)
        screenshot_name = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        driver.save_screenshot(f"screenshots/{screenshot_name}")

    finally:
        print("exiting driver")
        driver.quit()