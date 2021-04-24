import argparse
import requests


def update_dob(new_dob: str):

    cookies = {
        "__cfduid": "dd6b23b7cadfe86861449903da86003a31617222746",
        "_biz_ABTestA": "[-2087499830,-1822848077,-1579042556]",
        "_biz_flagsA": '{"Version":1,"Mkto":"1","ViewThrough":"1","XDomain":"1","Frm":"1"}',
        "_biz_nA": "65",
        "_biz_pendingA": "[]",
        "_biz_uid": "aec4c54d020b428ca03110efe4e8d422",
        "_derived_epik": "dj0yJnU9UkhoUFppdFgwTXdGMnh5OVhLWmNjNVJhSVhRcHJkb0Imbj1TeWZaZzYyaDNDQXNlVUJlbFh5N1hnJm09NyZ0PUFBQUFBR0NCM0xNJnJtPTQmcnQ9QUFBQUFHQ0JuaXM",
        "_fbp": "fb.1.1600726859779.110887315",
        "_ga": "GA1.2.1582427605.1599669114",
        "_ga_0J54E9SV5Y": "GS1.1.1619212107.16.0.1619212107.60",
        "_gcl_au": "1.1.386803100.1616083734",
        "_gid": "GA1.2.1143222416.1619056385",
        "_lfa": "eyJ5d1ZrTzRYUkFuMThaNkJqIjoiTEYxLjEuZjM2NGZiNDI3MmZmZmQ3Yi4xNjA0MjA0NDQ4NDkzIn0=",
        "_mkto_trk": "id:180-GFH-982&token:_mch-zenefits.com-1599669114062-37682",
        "_pin_unauth": "dWlkPVpqQXlOMk5sTlRjdE1EQTNPUzAwTlRkbExXSXpaV1V0TkRCaE16RmtaakZtTkRJeQ",
        "_sp_id.4c97": "1208c9ad-e7f1-409b-9e12-4526da013ace.1599669113.39.1619211400.1619200483.26e97da2-daee-4230-9a59-3825c1a04459",
        "_uetsid": "79c64200a30d11eb880b95a153fbde0a",
        "_uetvid": "f744b87085ea11eb8c2c11bdbd98f5a8",
        "ajaxtoken": "0b0fa89208a4d4bf1404670754dc36a20ff80c0bac4921313fe73c1b",
        "ajs_anonymous_id": '"35063681-0ba8-4fae-a4cc-1dad7c9f147b"',
        "ajs_user_id": '"chetan@instabase.com"',
        "cb_anonymous_id": '"1f9298aa-b007-429c-953a-3f85d907b3d8"',
        "cb_group_id": "null",
        "cb_user_id": "null",
        "csrftoken": "DHGyyqsKU5anekm3dtr3vO4kHPwS5zl6",
        "democenter": '{"accessToken":"d1b08335-2195-4b25-bdc3-2c01ed14c017","companySize":3,"startTimestamp":"2021-04-22T01:54:54.182Z","endTimestamp":"2021-05-06T01:54:54.183Z","email":"chetan@instabase.com","company_id":474596,"user_id":11375537,"employee_id":20233673,"name":"Chetan Mishra","companyName":"Instabase","firstName":"Chetan","lastName":"Mishra","companyZip":95343}',
        "DO_NOT_SHOW_ME_ANY_POPUP_ANYMORE": "1",
        "drift_aid": "83785821-bc51-4ee4-89d7-c583efe70442",
        "drift_campaign_refresh": "364c0490-6e7c-4599-93cb-2733b09178a8",
        "driftt_aid": "83785821-bc51-4ee4-89d7-c583efe70442",
        "fs_uid": "rs.fullstory.com#E2AHG#5926616156348416:6162773079891968#ad76e0e7#/1648758750",
        "IR_PI": "1619056398433.spvt321ko4|1619142798433",
        "KD_eff": "7f1",
        "OptanonConsent": "isIABGlobal=false&datestamp=Tue+Dec+01+2020+16:34:11+GMT-0600+(Central+Standard+Time)&version=6.5.0&hosts=&landingPath=NotLandingPage&groups=C0001:1,C0002:0,C0003:0,C0004:0&AwaitingReconsent=false",
        "optimizelyEndUserId": "oeu1599669111371r0.8700820588311232",
        "RT": '"z=1&dm=zenefits.com&si=vv2owqxgzg8&ss=knv4kwa9&sl=2&tt=3hs&ld=350"',
        "sessionid": "p3xoc3u8wh582y5e0akl7yn86ee3ch9n",
        "subscriptionInfo": '{"tier":"STATER_TIER","addons":[],"isRenewing":false,"numEmployees":0,"contractLength":0,"renewalDate":null,"isAdmin":true,"visitorId":"61ae9a645bd632c213529b305cbd3aae6ca6d9505aeceb0deef854ace45c3c3c","accountId":"474596"}',
        "TEAL": "v:117889fcca7700396603314130902585272198f6b60$t:1617224548796$s:1617222748794;exp-sess$sn:1$en:1",
        "user_names": "sxep740hzlure55p2vkr2jkuo",
        "user_type": "1",
        "user987ca02c27d9ee09bb2237a027104f628b8cfb1468f7f1053cbe9163": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6ZW5lZml0cyIsInRva2VuIjoiOTg3Y2EwMmMyN2Q5ZWUwOWJiMjIzN2EwMjcxMDRmNjI4YjhjZmIxNDY4ZjdmMTA1M2NiZTkxNjMiLCI2YmI1YWYyZDZlNTc0ZTNhOWJjYTMyNWU1NGNkYmI5OCI6IjA1ZTUyNDQ2OTIzNDQ1M2M5ZmNhMmZhYmYwMDM0MDg3In0.YA1WQeQ-YZNjwJuWdmHL0FvPjx-V7nF4y22MXQ_6hr8",
        "utag_main": "v_id:01789af63f0f001aca38e3d3aea500052001900f00b78$_sn:8$_se:1$_ss:1$_st:1619201754892$dc_visit:8$ses_id:1619199954892;exp-session$_pn:1;exp-session$dc_event:1;exp-session$dc_region:us-east-1;exp-session",
    }

    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.5",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Length": "1486",
        "content-type": "application/json",
        "Cookie": 'OptanonConsent=isIABGlobal=false&datestamp=Tue+Dec+01+2020+16%3A34%3A11+GMT-0600+(Central+Standard+Time)&version=6.5.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0&AwaitingReconsent=false; optimizelyEndUserId=oeu1599669111371r0.8700820588311232; _sp_id.4c97=1208c9ad-e7f1-409b-9e12-4526da013ace.1599669113.37.1619197601.1619156314.8f934c52-c918-4834-a6f2-aaacccd6d9d2; _derived_epik=dj0yJnU9UkhoUFppdFgwTXdGMnh5OVhLWmNjNVJhSVhRcHJkb0Imbj1TeWZaZzYyaDNDQXNlVUJlbFh5N1hnJm09NyZ0PUFBQUFBR0NCM0xNJnJtPTQmcnQ9QUFBQUFHQ0JuaXM; _pin_unauth=dWlkPVpqQXlOMk5sTlRjdE1EQTNPUzAwTlRkbExXSXpaV1V0TkRCaE16RmtaakZtTkRJeQ; _biz_uid=aec4c54d020b428ca03110efe4e8d422; _biz_nA=63; _biz_pendingA=%5B%22m%2Fipv%3F_biz_r%3D%26_biz_h%3D-131651014%26_biz_u%3Daec4c54d020b428ca03110efe4e8d422%26_biz_s%3D4bbd7%26_biz_l%3Dhttps%253A%252F%252Fwww.zenefits.com%252F%26_biz_t%3D1619197601170%26_biz_i%3D%25231%2520HR%2520Software%2520%257C%2520Human%2520Capital%2520Management%2520%257C%2520Zenefits%26_biz_n%3D62%26rnd%3D825116%22%5D; _ga=GA1.2.1582427605.1599669114; _mkto_trk=id:180-GFH-982&token:_mch-zenefits.com-1599669114062-37682; cb_user_id=null; cb_group_id=null; cb_anonymous_id=%221f9298aa-b007-429c-953a-3f85d907b3d8%22; _biz_flagsA=%7B%22Version%22%3A1%2C%22Mkto%22%3A%221%22%2C%22ViewThrough%22%3A%221%22%2C%22XDomain%22%3A%221%22%2C%22Frm%22%3A%221%22%7D; _biz_ABTestA=%5B-2087499830%2C-1822848077%2C-1579042556%5D; csrftoken=DHGyyqsKU5anekm3dtr3vO4kHPwS5zl6; ajs_anonymous_id=%2235063681-0ba8-4fae-a4cc-1dad7c9f147b%22; user_names=sxep740hzlure55p2vkr2jkuo; ajaxtoken=0b0fa89208a4d4bf1404670754dc36a20ff80c0bac4921313fe73c1b; user987ca02c27d9ee09bb2237a027104f628b8cfb1468f7f1053cbe9163=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6ZW5lZml0cyIsInRva2VuIjoiOTg3Y2EwMmMyN2Q5ZWUwOWJiMjIzN2EwMjcxMDRmNjI4YjhjZmIxNDY4ZjdmMTA1M2NiZTkxNjMiLCI2YmI1YWYyZDZlNTc0ZTNhOWJjYTMyNWU1NGNkYmI5OCI6IjA1ZTUyNDQ2OTIzNDQ1M2M5ZmNhMmZhYmYwMDM0MDg3In0.YA1WQeQ-YZNjwJuWdmHL0FvPjx-V7nF4y22MXQ_6hr8; _fbp=fb.1.1600726859779.110887315; DO_NOT_SHOW_ME_ANY_POPUP_ANYMORE=1; _lfa=eyJ5d1ZrTzRYUkFuMThaNkJqIjoiTEYxLjEuZjM2NGZiNDI3MmZmZmQ3Yi4xNjA0MjA0NDQ4NDkzIn0%3D; _ga_0J54E9SV5Y=GS1.1.1619197600.14.0.1619197604.56; sessionid=p3xoc3u8wh582y5e0akl7yn86ee3ch9n; _gcl_au=1.1.386803100.1616083734; __cfduid=dd6b23b7cadfe86861449903da86003a31617222746; TEAL=v:117889fcca7700396603314130902585272198f6b60$t:1617224548796$s:1617222748794%3Bexp-sess$sn:1$en:1; fs_uid=rs.fullstory.com#E2AHG#5926616156348416:6269786791223296#ad76e0e7#/1648758750; utag_main=v_id:01789af63f0f001aca38e3d3aea500052001900f00b78$_sn:7$_se:1$_ss:1$_st:1619199400460$dc_visit:7$ses_id:1619197600460%3Bexp-session$_pn:1%3Bexp-session$dc_event:1%3Bexp-session$dc_region:us-east-1%3Bexp-session; RT="z=1&dm=zenefits.com&si=gnin4enqo1n&ss=knukg377&sl=4&tt=85a&ld=btf&nu=39c2982b6f0554e1be5021833bbd8f88&cl=9nt"; KD_eff=7f1; _gid=GA1.2.1143222416.1619056385; ajs_user_id=%22chetan%40instabase.com%22; democenter={%22accessToken%22:%22d1b08335-2195-4b25-bdc3-2c01ed14c017%22%2C%22companySize%22:3%2C%22startTimestamp%22:%222021-04-22T01:54:54.182Z%22%2C%22endTimestamp%22:%222021-05-06T01:54:54.183Z%22%2C%22email%22:%22chetan@instabase.com%22%2C%22company_id%22:474596%2C%22user_id%22:11375537%2C%22employee_id%22:20233673%2C%22name%22:%22Chetan%20Mishra%22%2C%22companyName%22:%22Instabase%22%2C%22firstName%22:%22Chetan%22%2C%22lastName%22:%22Mishra%22%2C%22companyZip%22:95343}; IR_PI=1619056398433.spvt321ko4%7C1619142798433; subscriptionInfo=%7B%22tier%22%3A%22STATER_TIER%22%2C%22addons%22%3A%5B%5D%2C%22isRenewing%22%3Afalse%2C%22numEmployees%22%3A0%2C%22contractLength%22%3A0%2C%22renewalDate%22%3Anull%2C%22isAdmin%22%3Atrue%2C%22visitorId%22%3A%2261ae9a645bd632c213529b305cbd3aae6ca6d9505aeceb0deef854ace45c3c3c%22%2C%22accountId%22%3A%22474596%22%7D; drift_aid=83785821-bc51-4ee4-89d7-c583efe70442; driftt_aid=83785821-bc51-4ee4-89d7-c583efe70442; user_type=1; _sp_ses.4c97=*; _biz_sid=4bbd7; _uetsid=79c64200a30d11eb880b95a153fbde0a; _uetvid=f744b87085ea11eb8c2c11bdbd98f5a8; _gat=1; drift_campaign_refresh=565a1cda-a67d-4571-a728-7702224c1210',
        "Host": "secure.zenefits.com",
        "Origin": "https://secure.zenefits.com",
        "Pragma": "no-cache",
        "Referer": "https://secure.zenefits.com/",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0",
        "X-AJAXToken": "0b0fa89208a4d4bf1404670754dc36a20ff80c0bac4921313fe73c1b",
        "X-COMPANY-ID": "474596",
        "X-CSRFToken": "DHGyyqsKU5anekm3dtr3vO4kHPwS5zl6",
        "X-EMPLOYEE-ID": "20233673",
        "x-origin": "https://secure.zenefits.com",
        "X-PAGEUrl": "https://secure.zenefits.com/dashboard/#/employee-profile/20234267/personal-info",
        "X-REQUEST-ID": "08657878-426b-4c1e-bc6d-218bcb7bebe5",
        "X-TRANSITION-ID": "null",
        "X-USER-ID": "11375537",
        "zenefits-appname": "hr-employee",
        "TE": "Trailers",
    }
    # [
    #     {"name": "Accept", "value": "application/json"},
    #     {"name": "Accept-Encoding", "value": "gzip, deflate, br"},
    #     {"name": "Accept-Language", "value": "en-US,en;q=0.5"},
    #     {"name": "Cache-Control", "value": "no-cache"},
    #     {"name": "Connection", "value": "keep-alive"},
    #     {"name": "Content-Length", "value": "1486"},
    #     {"name": "content-type", "value": "application/json"},
    #     {
    #         "name": "Cookie",
    #         "value": 'OptanonConsent=isIABGlobal=false&datestamp=Tue+Dec+01+2020+16%3A34%3A11+GMT-0600+(Central+Standard+Time)&version=6.5.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0&AwaitingReconsent=false; optimizelyEndUserId=oeu1599669111371r0.8700820588311232; _sp_id.4c97=1208c9ad-e7f1-409b-9e12-4526da013ace.1599669113.37.1619197601.1619156314.8f934c52-c918-4834-a6f2-aaacccd6d9d2; _derived_epik=dj0yJnU9UkhoUFppdFgwTXdGMnh5OVhLWmNjNVJhSVhRcHJkb0Imbj1TeWZaZzYyaDNDQXNlVUJlbFh5N1hnJm09NyZ0PUFBQUFBR0NCM0xNJnJtPTQmcnQ9QUFBQUFHQ0JuaXM; _pin_unauth=dWlkPVpqQXlOMk5sTlRjdE1EQTNPUzAwTlRkbExXSXpaV1V0TkRCaE16RmtaakZtTkRJeQ; _biz_uid=aec4c54d020b428ca03110efe4e8d422; _biz_nA=63; _biz_pendingA=%5B%22m%2Fipv%3F_biz_r%3D%26_biz_h%3D-131651014%26_biz_u%3Daec4c54d020b428ca03110efe4e8d422%26_biz_s%3D4bbd7%26_biz_l%3Dhttps%253A%252F%252Fwww.zenefits.com%252F%26_biz_t%3D1619197601170%26_biz_i%3D%25231%2520HR%2520Software%2520%257C%2520Human%2520Capital%2520Management%2520%257C%2520Zenefits%26_biz_n%3D62%26rnd%3D825116%22%5D; _ga=GA1.2.1582427605.1599669114; _mkto_trk=id:180-GFH-982&token:_mch-zenefits.com-1599669114062-37682; cb_user_id=null; cb_group_id=null; cb_anonymous_id=%221f9298aa-b007-429c-953a-3f85d907b3d8%22; _biz_flagsA=%7B%22Version%22%3A1%2C%22Mkto%22%3A%221%22%2C%22ViewThrough%22%3A%221%22%2C%22XDomain%22%3A%221%22%2C%22Frm%22%3A%221%22%7D; _biz_ABTestA=%5B-2087499830%2C-1822848077%2C-1579042556%5D; csrftoken=DHGyyqsKU5anekm3dtr3vO4kHPwS5zl6; ajs_anonymous_id=%2235063681-0ba8-4fae-a4cc-1dad7c9f147b%22; user_names=sxep740hzlure55p2vkr2jkuo; ajaxtoken=0b0fa89208a4d4bf1404670754dc36a20ff80c0bac4921313fe73c1b; user987ca02c27d9ee09bb2237a027104f628b8cfb1468f7f1053cbe9163=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6ZW5lZml0cyIsInRva2VuIjoiOTg3Y2EwMmMyN2Q5ZWUwOWJiMjIzN2EwMjcxMDRmNjI4YjhjZmIxNDY4ZjdmMTA1M2NiZTkxNjMiLCI2YmI1YWYyZDZlNTc0ZTNhOWJjYTMyNWU1NGNkYmI5OCI6IjA1ZTUyNDQ2OTIzNDQ1M2M5ZmNhMmZhYmYwMDM0MDg3In0.YA1WQeQ-YZNjwJuWdmHL0FvPjx-V7nF4y22MXQ_6hr8; _fbp=fb.1.1600726859779.110887315; DO_NOT_SHOW_ME_ANY_POPUP_ANYMORE=1; _lfa=eyJ5d1ZrTzRYUkFuMThaNkJqIjoiTEYxLjEuZjM2NGZiNDI3MmZmZmQ3Yi4xNjA0MjA0NDQ4NDkzIn0%3D; _ga_0J54E9SV5Y=GS1.1.1619197600.14.0.1619197604.56; sessionid=p3xoc3u8wh582y5e0akl7yn86ee3ch9n; _gcl_au=1.1.386803100.1616083734; __cfduid=dd6b23b7cadfe86861449903da86003a31617222746; TEAL=v:117889fcca7700396603314130902585272198f6b60$t:1617224548796$s:1617222748794%3Bexp-sess$sn:1$en:1; fs_uid=rs.fullstory.com#E2AHG#5926616156348416:6269786791223296#ad76e0e7#/1648758750; utag_main=v_id:01789af63f0f001aca38e3d3aea500052001900f00b78$_sn:7$_se:1$_ss:1$_st:1619199400460$dc_visit:7$ses_id:1619197600460%3Bexp-session$_pn:1%3Bexp-session$dc_event:1%3Bexp-session$dc_region:us-east-1%3Bexp-session; RT="z=1&dm=zenefits.com&si=gnin4enqo1n&ss=knukg377&sl=4&tt=85a&ld=btf&nu=39c2982b6f0554e1be5021833bbd8f88&cl=9nt"; KD_eff=7f1; _gid=GA1.2.1143222416.1619056385; ajs_user_id=%22chetan%40instabase.com%22; democenter={%22accessToken%22:%22d1b08335-2195-4b25-bdc3-2c01ed14c017%22%2C%22companySize%22:3%2C%22startTimestamp%22:%222021-04-22T01:54:54.182Z%22%2C%22endTimestamp%22:%222021-05-06T01:54:54.183Z%22%2C%22email%22:%22chetan@instabase.com%22%2C%22company_id%22:474596%2C%22user_id%22:11375537%2C%22employee_id%22:20233673%2C%22name%22:%22Chetan%20Mishra%22%2C%22companyName%22:%22Instabase%22%2C%22firstName%22:%22Chetan%22%2C%22lastName%22:%22Mishra%22%2C%22companyZip%22:95343}; IR_PI=1619056398433.spvt321ko4%7C1619142798433; subscriptionInfo=%7B%22tier%22%3A%22STATER_TIER%22%2C%22addons%22%3A%5B%5D%2C%22isRenewing%22%3Afalse%2C%22numEmployees%22%3A0%2C%22contractLength%22%3A0%2C%22renewalDate%22%3Anull%2C%22isAdmin%22%3Atrue%2C%22visitorId%22%3A%2261ae9a645bd632c213529b305cbd3aae6ca6d9505aeceb0deef854ace45c3c3c%22%2C%22accountId%22%3A%22474596%22%7D; drift_aid=83785821-bc51-4ee4-89d7-c583efe70442; driftt_aid=83785821-bc51-4ee4-89d7-c583efe70442; user_type=1; _sp_ses.4c97=*; _biz_sid=4bbd7; _uetsid=79c64200a30d11eb880b95a153fbde0a; _uetvid=f744b87085ea11eb8c2c11bdbd98f5a8; _gat=1; drift_campaign_refresh=565a1cda-a67d-4571-a728-7702224c1210',
    #     },
    #     {"name": "Host", "value": "secure.zenefits.com"},
    #     {"name": "Origin", "value": "https://secure.zenefits.com"},
    #     {"name": "Pragma", "value": "no-cache"},
    #     {"name": "Referer", "value": "https://secure.zenefits.com/"},
    #     {
    #         "name": "User-Agent",
    #         "value": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0",
    #     },
    #     {
    #         "name": "X-AJAXToken",
    #         "value": "0b0fa89208a4d4bf1404670754dc36a20ff80c0bac4921313fe73c1b",
    #     },
    #     {"name": "X-COMPANY-ID", "value": "474596"},
    #     {"name": "X-CSRFToken", "value": "DHGyyqsKU5anekm3dtr3vO4kHPwS5zl6"},
    #     {"name": "X-EMPLOYEE-ID", "value": "20233673"},
    #     {"name": "x-origin", "value": "https://secure.zenefits.com"},
    #     {
    #         "name": "X-PAGEUrl",
    #         "value": "https://secure.zenefits.com/dashboard/#/employee-profile/20234267/personal-info",
    #     },
    #     {"name": "X-REQUEST-ID", "value": "08657878-426b-4c1e-bc6d-218bcb7bebe5"},
    #     {"name": "X-TRANSITION-ID", "value": "null"},
    #     {"name": "X-USER-ID", "value": "11375537"},
    #     {"name": "zenefits-appname", "value": "hr-employee"},
    # ]

    body = {
        "operationName": "UpdateBasicInfoMutation",
        "variables": {
            "request": {
                "targetEmployeeId": "20234267",
                "first_name": "Deborah",
                "middle_name": "",
                "last_name": "Bennett",
                "preferredName": "",
                "tShirtSize": "",
                "dietaryRestrictions": "",
                "dob": new_dob,
                "gender": "F",
                "isWaitingForSSNInfo": False,
                "personalPronounsId": None,
                "genderIdentity": "",
                "socialSecurity": None,
            }
        },
        "query": "mutation UpdateBasicInfoMutation($request: UpdateEmployeeProfileBasicInfo!) {\n  updateProfileBasicInfo(request: $request) {\n    success\n    errorMessage\n    employee {\n      ...EmployeeBasicInfoFragment\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment EmployeeBasicInfoFragment on AllEmployee {\n  id\n  first_name\n  middle_name\n  last_name\n  dietaryRestrictions\n  tShirtSize\n  preferredName\n  personalPronouns\n  personalPronounsId\n  profile {\n    basicInfo {\n      dob\n      gender\n      maskedSocialSecurity\n      cardMode\n      showSensitive\n      shouldShowSSN\n      employeeSSNUrl\n      showLegalGender\n      isSelf\n      canAdminister\n      isDietary\n      isTshirtSize\n      isWaitingForSSNInfo\n      isInternational\n      showTaxIDOrNationalID\n      hasNationalId\n      hasTaxId\n      employeeNationalIdUrl\n      nationalID\n      employeeTaxIdUrl\n      taxID\n      nationalIdLabel\n      taxIdLabel\n      genderIdentity\n      hasCustomGenderFilledOut\n      employeeLegalFullName\n      legalNameLabel\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n",
    }

    resp = requests.post(
        "https://secure.zenefits.com/graphql/",
        data=body,
        headers=headers,
        cookies=cookies,
    )
    print(resp.content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--new-dob", dest="new_dob")
    args = parser.parse_args()

    update_dob(args.new_dob)

