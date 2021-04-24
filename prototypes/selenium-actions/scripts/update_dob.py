import argparse
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def update_dob(new_dob):
    firefox_profile = webdriver.FirefoxProfile(
        "/Users/chetanmishra/Library/Application Support/Firefox/Profiles/e3ycs00t.default copy"
    )
    driver = webdriver.Firefox(firefox_profile=firefox_profile)
    driver.get("https://www.zenefits.com")
    driver.find_element_by_css_selector(".sign-in").click()

    driver.get("https://www.zenefits.com/dashboard/#/employeedirectory")
    WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'input[aria-labelledby="zf-name-label"]',)
        )
    )
    print(f"Waiting for name input text")
    name_input = driver.find_element_by_css_selector(
        'input[aria-labelledby="zf-name-label"]'
    )
    name_input.send_keys("Deborah")
    driver.find_element_by_link_text("Bennett, Deborah").click()
    print(f"Waiting for input to appear")
    WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Edit"]',))
    )
    driver.find_element_by_css_selector('button[aria-label="Edit"]').click()
    print(f"Clicked on edit")
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "dob")))
    dob_input = driver.find_element_by_id("dob")
    dob_input.clear()
    dob_input.send_keys(new_dob)
    dob_input.send_keys(Keys.ENTER)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--new-dob", dest="new_dob", help="What should the DOB be updated to",
    )
    args = parser.parse_args()
    update_dob(args.new_dob)

