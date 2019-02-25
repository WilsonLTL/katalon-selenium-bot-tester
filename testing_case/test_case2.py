import time
import datetime
from selenium import webdriver

error_limit = 10
filename = "log/test_case2-" + str(datetime.datetime.now()) + ".txt"


def test_case(num):
    try:
        start = time.time()
        time.sleep(3)
        global error_limit
        if error_limit > 0:
            print("Start:" + str(num))
            if num == 1:
                global filename
                global browser
                browser.get("https://www.messenger.com/t/DrCareAi")
                time.sleep(1)
                email = browser.find_element_by_id("email")
                password = browser.find_element_by_id("pass")
                submit = browser.find_element_by_id("loginbutton")
                email.send_keys("vincentlo1997@yahoo.com.hk")
                # your email address
                password.send_keys("Vi26151851@")
                # your_password
                submit.click()
                num += 1
            elif num == 2:
                browser.find_element_by_link_text(u"開始使用").click()
                print("Finish:" + str(num))
                num += 1
            elif num == 3:
                browser.find_element_by_xpath(u"//a[contains(text(),'可以問什麼? 🛂')]").click()
                browser.find_element_by_link_text(u"可以問什麼? 🛂").click()
                print("Finish:" + str(num))
                num += 1
            elif num == 4:
                browser.execute_script("window.scrollTo(0, 320)")
                browser.find_element_by_xpath(u"//div[contains(text(),'可以了 👌🏻')]").click()
                print("Finish:" + str(num))
                num += 1
            elif num == 5:
                browser.find_element_by_link_text(u"回主菜單 🏠").click()
                print("Finish:" + str(num))
                clear_chat()
                num += 1
            else:
                print("No match step number:" + num)
            latency = time.time() - start
            millis = int(round(latency * 1000))
            with open(filename, "a") as f:
                f.write(str(datetime.datetime.now()) + ",success," + str(millis) + "\n")
            f.close()
            if num <= 5:
                error_limit = 10
                test_case(num)
        else:
            print("Logging false")
            with open(filename, "a") as f:
                f.write(str(datetime.datetime.now()) + ",false" + "\n")
            f.close()
            time.sleep(2)
            clear_chat()
    except Exception as e:
        print(e)
        print("error_limit:" + str(error_limit))
        error_limit -= 1
        test_case(num)


def clear_chat():
    time.sleep(5)
    browser.find_element_by_css_selector("div._3-ne > div._3d85 > div._5blh._4-0h").click()
    time.sleep(1)
    browser.find_element_by_xpath("//li[4]/a/span/span").click()
    time.sleep(1)
    browser.find_element_by_xpath("//span[2]/button").click()
    time.sleep(3)


if __name__ == '__main__':
    browser = webdriver.Chrome()
    test_case(1)
    browser.close()