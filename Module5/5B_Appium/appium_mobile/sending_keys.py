import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    desired_caps = {
        "deviceName": "Android Emulator",
        "platformName": "Android",
        "platformVersion": "12",
        "appPackage": "com.google.android.apps.maps",
        "appActivity": "com.google.android.maps.MapsActivity",
        "noSign": True
    }

    driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)
    # click the Okay button on the pop-up

    # Using Class_Name location strategy
    skip_Button = driver.find_element(MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget"
                                                      ".LinearLayout/android.widget.FrameLayout/android.widget"
                                                      ".LinearLayout/android.widget.FrameLayout/android.widget"
                                                      ".FrameLayout/android.widget.LinearLayout/android.view"
                                                      ".ViewGroup/android.widget.FrameLayout["
                                                      "2]/android.widget.LinearLayout/android.widget.FrameLayout"
                                                      "/android.widget.RelativeLayout/android.widget.Button")
    print(skip_Button.tag_name)
    skip_Button.click()
    time.sleep(5)
    search_box = driver.find_element(MobileBy.ID, "com.google.android.apps.maps:id/search_omnibox_text_box")
    search_box.click()
    time.sleep(5)
    edit_search_box = driver.find_element(MobileBy.ID, "com.google.android.apps.maps:id/search_omnibox_edit_text")
    edit_search_box.send_keys("Lagos")
    time.sleep(10)
    edit_search_box.clear()
    time.sleep(10)
    driver.quit()


if __name__ == '__main__':
    main()
