import argparse
import enum
import logging
from playwright.sync_api import sync_playwright
import time


class SupportedBrowsers(enum.Enum):
    chrome = "chrome"
    firefox = "firefox"

    def __str__(self):
        return self.value


def update_dob(new_dob, browser):
    cookies = [
        {
            "name": "democenter",
            "value": '{"accessToken":"d1b08335-2195-4b25-bdc3-2c01ed14c017","companySize":3,"startTimestamp":"2021-04-22T01:54:54.182Z","endTimestamp":"2021-05-06T01:54:54.183Z","email":"chetan@instabase.com","company_id":474596,"user_id":11375537,"employee_id":20233673,"name":"Chetan Mishra","companyName":"Instabase","firstName":"Chetan","lastName":"Mishra","companyZip":95343}',
            "url": "https://www.zenefits.com",
        },
        {
            "name": "DO_NOT_SHOW_ME_ANY_POPUP_ANYMORE",
            "value": "1",
            "url": "https://www.zenefits.com",
        },
    ]

    with sync_playwright() as p:
        if browser.value == "chrome":
            browser = p.chromium.launch(channel="chrome")
        elif browser.value == "firefox":
            browser = p.firefox.launch()
        else:
            assert False, f"Browser not supported: {browser.value}"
        page = browser.new_page(storage_state={"cookies": cookies})
        page.goto(
            "https://secure.zenefits.com/accounts/access-trial/d1b08335-2195-4b25-bdc3-2c01ed14c017"
        )
        page.goto("https://www.zenefits.com/dashboard/#/employeedirectory")
        page.type('input[aria-labelledby="zf-name-label"]', "deborah")
        page.click("text=Bennett, Deborah")
        page.click('button[aria-label="Edit"]')
        page.fill("id=dob", new_dob)
        page.press("id=dob", "Enter")
        page.wait_for_selector("id=dob", state="detached")
        browser.close()


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

