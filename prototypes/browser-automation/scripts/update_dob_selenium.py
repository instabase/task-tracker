import argparse
import enum
import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class SupportedBrowsers(enum.Enum):
    chrome = "chrome"
    firefox = "firefox"

    def __str__(self):
        return self.value

    def create_browser(self):
        if self.value == "firefox":
            return self.create_firefox_browser()
        elif self.value == "chrome":
            return self.create_chrome_browser()
        else:
            assert False, f"Browser type not supported: {self.value}"

    def create_chrome_browser(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        return driver

    def create_firefox_browser(self):
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument("--headless")
        driver = webdriver.Firefox(options=firefox_options)
        return driver


def update_dob(new_dob, browser):
    cookies = {
        "name": "democenter",
        "value": '{"accessToken":"d1b08335-2195-4b25-bdc3-2c01ed14c017","companySize":3,"startTimestamp":"2021-04-22T01:54:54.182Z","endTimestamp":"2021-05-06T01:54:54.183Z","email":"chetan@instabase.com","company_id":474596,"user_id":11375537,"employee_id":20233673,"name":"Chetan Mishra","companyName":"Instabase","firstName":"Chetan","lastName":"Mishra","companyZip":95343}',
        "name": "DO_NOT_SHOW_ME_ANY_POPUP_ANYMORE",
        "value": "1",
    }

    logging.info(f"About to start the driver")
    driver = browser.create_browser()
    logging.info(f"Started the driver")
    driver.get("https://www.zenefits.com/")
    driver.add_cookie(cookies)
    driver.refresh()
    driver.get(
        "https://secure.zenefits.com/accounts/access-trial/d1b08335-2195-4b25-bdc3-2c01ed14c017"
    )

    driver.get("https://www.zenefits.com/dashboard/#/employeedirectory")
    WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'input[aria-labelledby="zf-name-label"]',)
        )
    )
    logging.info(f"Waiting for name input text")
    name_input = driver.find_element_by_css_selector(
        'input[aria-labelledby="zf-name-label"]'
    )
    name_input.send_keys("Deborah")
    driver.find_element_by_link_text("Bennett, Deborah").click()
    logging.info(f"Waiting for input to appear")
    WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Edit"]',))
    )
    driver.find_element_by_css_selector('button[aria-label="Edit"]').click()
    logging.info(f"Clicked on edit")
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "dob")))
    dob_input = driver.find_element_by_id("dob")
    dob_input.clear()
    dob_input.send_keys(new_dob)
    dob_input.send_keys(Keys.ENTER)
    # needed because the browser needs time to trigger the enter + send the request
    time.sleep(3)
    driver.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--new-dob", dest="new_dob", help="What should the DOB be updated to",
    )
    parser.add_argument("--log-level", dest="log_level", default="warning")
    parser.add_argument(
        "--browser",
        help="which browser should the test be conducted in",
        type=SupportedBrowsers,
        choices=SupportedBrowsers,
        required=True,
    )
    args = parser.parse_args()
    logging.basicConfig(
        level=getattr(logging, args.log_level.upper()),
        format="[%(levelname)s] (%(module)s.%(funcName)s) %(message)s",
    )

    update_dob(args.new_dob, args.browser)

