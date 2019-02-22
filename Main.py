from selenium import webdriver
import datetime
import time
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome()


def login():
    browser.get("https://www.messenger.com/t/DrCareAi")
    try:
        time.sleep(1)
        email = browser.find_element_by_id("email")
        password = browser.find_element_by_id("pass")
        submit = browser.find_element_by_id("loginbutton")

        email.send_keys("")
        # your email address
        password.send_keys("")
        # your_password
        submit.click()
    except Exception as e:
        login()


def test_case1(num):
    try:
        print("Start:" + str(num))
        start = time.time()
        time.sleep(1)
        if num == 1:
            browser.find_element_by_link_text(u"開始使用").click()
            print("Finish:" + str(num))
            num += 1
        elif num == 2:
            browser.find_element_by_xpath(u"//a[contains(text(),'可以問什麼? 🛂')]").click()
            browser.find_element_by_link_text(u"可以問什麼? 🛂").click()
            print("Finish:" + str(num))
            num += 1
        elif num == 3:
            browser.execute_script("window.scrollTo(0, 320)")
            browser.find_element_by_xpath(u"//div[contains(text(),'可以了 👌🏻')]").click()
            print("Finish:" + str(num))
            num += 1
        elif num == 4:
            browser.find_element_by_link_text(u"回主菜單 🏠").click()
            print("Finish:" + str(num))
            num += 1
        elif num == 5:
            # browser.find_element_by_class_name("viewBox='0 0 64 64'").click()
            # print("Finish:" + str(num))
            num += 1
        elif num == 6:
            browser.find_element_by_css_selector("div._3-ne > div._3d85 > div._5blh._4-0h").click()
            print("Finish:" + str(num))
            num += 1
        elif num == 7:
            browser.find_element_by_xpath("//li[4]/a/span/span").click()
            print("Finish:" + str(num))
            num += 1
        elif num == 8:
            browser.find_element_by_xpath("//span[2]/button").click()
            print("Finish:" + str(num))
            num += 1
        else:
            print("No match step number:"+num)
        latency = time.time() - start
        millis = int(round(latency * 1000))
        with open(filename, "a") as f:
            f.write(str(datetime.datetime.now()) + ",success," + str(millis) + "\n")
        f.close()
        if num <= 8:
            test_case1(num)
    except Exception as e:
        with open(filename, "a") as f:
            f.write(str(datetime.datetime.now()) + ",false" + "\n")
        f.close()
        test_case1(num)


login()
filename = "log/test_case1-" + str(datetime.datetime.now()) + ".txt"
test_case1(1)
browser.close()