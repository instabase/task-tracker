import argparse
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def update_dob(new_dob):
    # firefox_profile = webdriver.FirefoxProfile(
    #     "/Users/chetanmishra/Library/Application Support/Firefox/Profiles/e3ycs00t.default copy"
    # )
    cookies = {
        "name": "__cfduid",
        "value": "dd6b23b7cadfe86861449903da86003a31617222746",
        "name": "_biz_ABTestA",
        "value": "[-2087499830,-1822848077,-1579042556]",
        "name": "_biz_flagsA",
        "value": '{"Version":1,"Mkto":"1","ViewThrough":"1","XDomain":"1","Frm":"1"}',
        "name": "_biz_nA",
        "value": "65",
        "name": "_biz_pendingA",
        "value": "[]",
        "name": "_biz_uid",
        "value": "aec4c54d020b428ca03110efe4e8d422",
        "name": "_derived_epik",
        "value": "dj0yJnU9UkhoUFppdFgwTXdGMnh5OVhLWmNjNVJhSVhRcHJkb0Imbj1TeWZaZzYyaDNDQXNlVUJlbFh5N1hnJm09NyZ0PUFBQUFBR0NCM0xNJnJtPTQmcnQ9QUFBQUFHQ0JuaXM",
        "name": "_fbp",
        "value": "fb.1.1600726859779.110887315",
        "name": "_ga",
        "value": "GA1.2.1582427605.1599669114",
        "name": "_ga_0J54E9SV5Y",
        "value": "GS1.1.1619212107.16.0.1619212107.60",
        "name": "_gcl_au",
        "value": "1.1.386803100.1616083734",
        "name": "_gid",
        "value": "GA1.2.1143222416.1619056385",
        "name": "_lfa",
        "value": "eyJ5d1ZrTzRYUkFuMThaNkJqIjoiTEYxLjEuZjM2NGZiNDI3MmZmZmQ3Yi4xNjA0MjA0NDQ4NDkzIn0=",
        "name": "_mkto_trk",
        "value": "id:180-GFH-982&token:_mch-zenefits.com-1599669114062-37682",
        "name": "_pin_unauth",
        "value": "dWlkPVpqQXlOMk5sTlRjdE1EQTNPUzAwTlRkbExXSXpaV1V0TkRCaE16RmtaakZtTkRJeQ",
        "name": "_sp_id.4c97",
        "value": "1208c9ad-e7f1-409b-9e12-4526da013ace.1599669113.39.1619211400.1619200483.26e97da2-daee-4230-9a59-3825c1a04459",
        "name": "_uetsid",
        "value": "79c64200a30d11eb880b95a153fbde0a",
        "name": "_uetvid",
        "value": "f744b87085ea11eb8c2c11bdbd98f5a8",
        "name": "ajaxtoken",
        "value": "0b0fa89208a4d4bf1404670754dc36a20ff80c0bac4921313fe73c1b",
        "name": "ajs_anonymous_id",
        "value": '"35063681-0ba8-4fae-a4cc-1dad7c9f147b"',
        "name": "ajs_user_id",
        "value": '"chetan@instabase.com"',
        "name": "cb_anonymous_id",
        "value": '"1f9298aa-b007-429c-953a-3f85d907b3d8"',
        "name": "cb_group_id",
        "value": "null",
        "name": "cb_user_id",
        "value": "null",
        "name": "csrftoken",
        "value": "DHGyyqsKU5anekm3dtr3vO4kHPwS5zl6",
        "name": "democenter",
        "value": '{"accessToken":"d1b08335-2195-4b25-bdc3-2c01ed14c017","companySize":3,"startTimestamp":"2021-04-22T01:54:54.182Z","endTimestamp":"2021-05-06T01:54:54.183Z","email":"chetan@instabase.com","company_id":474596,"user_id":11375537,"employee_id":20233673,"name":"Chetan Mishra","companyName":"Instabase","firstName":"Chetan","lastName":"Mishra","companyZip":95343}',
        "name": "DO_NOT_SHOW_ME_ANY_POPUP_ANYMORE",
        "value": "1",
        "name": "drift_aid",
        "value": "83785821-bc51-4ee4-89d7-c583efe70442",
        "name": "drift_campaign_refresh",
        "value": "364c0490-6e7c-4599-93cb-2733b09178a8",
        "name": "driftt_aid",
        "value": "83785821-bc51-4ee4-89d7-c583efe70442",
        "name": "fs_uid",
        "value": "rs.fullstory.com#E2AHG#5926616156348416:6162773079891968#ad76e0e7#/1648758750",
        "name": "IR_PI",
        "value": "1619056398433.spvt321ko4|1619142798433",
        "name": "KD_eff",
        "value": "7f1",
        "name": "OptanonConsent",
        "value": "isIABGlobal=false&datestamp=Tue+Dec+01+2020+16:34:11+GMT-0600+(Central+Standard+Time)&version=6.5.0&hosts=&landingPath=NotLandingPage&groups=C0001:1,C0002:0,C0003:0,C0004:0&AwaitingReconsent=false",
        "name": "optimizelyEndUserId",
        "value": "oeu1599669111371r0.8700820588311232",
        "name": "RT",
        "value": '"z=1&dm=zenefits.com&si=vv2owqxgzg8&ss=knv4kwa9&sl=2&tt=3hs&ld=350"',
        "name": "sessionid",
        "value": "p3xoc3u8wh582y5e0akl7yn86ee3ch9n",
        "name": "subscriptionInfo",
        "value": '{"tier":"STATER_TIER","addons":[],"isRenewing":false,"numEmployees":0,"contractLength":0,"renewalDate":null,"isAdmin":true,"visitorId":"61ae9a645bd632c213529b305cbd3aae6ca6d9505aeceb0deef854ace45c3c3c","accountId":"474596"}',
        "name": "TEAL",
        "value": "v:117889fcca7700396603314130902585272198f6b60$t:1617224548796$s:1617222748794;exp-sess$sn:1$en:1",
        "name": "user_names",
        "value": "sxep740hzlure55p2vkr2jkuo",
        "name": "user_type",
        "value": "1",
        "name": "user987ca02c27d9ee09bb2237a027104f628b8cfb1468f7f1053cbe9163",
        "value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6ZW5lZml0cyIsInRva2VuIjoiOTg3Y2EwMmMyN2Q5ZWUwOWJiMjIzN2EwMjcxMDRmNjI4YjhjZmIxNDY4ZjdmMTA1M2NiZTkxNjMiLCI2YmI1YWYyZDZlNTc0ZTNhOWJjYTMyNWU1NGNkYmI5OCI6IjA1ZTUyNDQ2OTIzNDQ1M2M5ZmNhMmZhYmYwMDM0MDg3In0.YA1WQeQ-YZNjwJuWdmHL0FvPjx-V7nF4y22MXQ_6hr8",
        "name": "utag_main",
        "value": "v_id:01789af63f0f001aca38e3d3aea500052001900f00b78$_sn:8$_se:1$_ss:1$_st:1619201754892$dc_visit:8$ses_id:1619199954892;exp-session$_pn:1;exp-session$dc_event:1;exp-session$dc_region:us-east-1;exp-session",
    }

    driver = webdriver.Firefox()
    driver.get("https://www.zenefits.com")
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
    time.sleep(
        3
    )  # needed because the browser needs time to trigger the enter + send the request
    driver.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--new-dob", dest="new_dob", help="What should the DOB be updated to",
    )
    args = parser.parse_args()
    update_dob(args.new_dob)

