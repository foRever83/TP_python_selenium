from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages import login_page
from pages import dropdown_page
import os
from datetime import datetime


options = Options()
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")
options.add_argument("--headless")



def test_loging():
    driver = webdriver.Chrome(options=options)
    os.makedirs('screenshots', exist_ok=True)

    page = login_page.LoginPage(driver)

    try :
        print(f"Opening url {page.LOGIN_URL}")
        page.open(page.LOGIN_URL)
        print("checking url")
        page.check_url(page.LOGIN_URL)
        print("Waiting for elements to charge")
        page.check_presence_of_element(page.LOGIN_FORM_LOCATOR)
        print("filling login field")
        page.fill_input(page.LOGIN_LOCATOR, page.USERNAME)
        print("filling password field")
        page.fill_input(page.PASSWORD_LOCATOR, page.PASSWORD)
        print("submitting login request")
        page.click_button(page.LOGIN_BUTTON_LOCATOR)
        #print("taking screenshot")
        #driver.save_screenshot("screenshots/test_login_screenshot.png")
        print("checking url")
        page.check_url(f"{page.BASE_URL}secure")
        print("checking presence of welcome message")
        page.check_presence_of_element(page.MESSAGE_LOCATOR)
        print("checking presence of logout button")
        page.check_presence_of_element(page.LOGOUT_BUTTON_LOCATOR)
        print("logging out")
        page.click_button(page.LOGOUT_BUTTON_LOCATOR)
        print("checking url")
        page.check_url(page.LOGIN_URL)

    except Exception as e:
        print(e)
        screenshot_name = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        driver.save_screenshot(f"screenshots/{screenshot_name}")

    finally:
        print("exiting driver")
        driver.quit()

def test_dropdown():

    driver = webdriver.Chrome(options=options)
    os.makedirs('screenshots', exist_ok=True)
    page = dropdown_page.DropdownPage(driver)

    try :
        print(f"Opening url {page.DROPDOWN_URL}")
        page.open(page.DROPDOWN_URL)
        print("checking url")
        page.check_url(page.DROPDOWN_URL)
        print("checking presence of dropdown list")
        page.check_presence_of_element(page.DROPDOWN_LIST)
        print(f"selecting option {page.OPTION_1}")
        page.select_in_list(page.OPTION_1)
        print(f"checking if selected option is {page.OPTION_1}")
        page.check_selection("Option 1")
        print(f"selecting option {page.OPTION_1}")
        page.select_in_list(page.OPTION_2)
        print(f"checking if selected option is {page.OPTION_2}")
        page.check_selection("Option 2")



    except Exception as e:
        print(e)

    finally:
        print("exiting driver")
        driver.quit()