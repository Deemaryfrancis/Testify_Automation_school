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
        "appPackage": "com.android.dialer",
        "appActivity": ".main.impl.MainActivity",
        "noSign": True
    }

    driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)
    # click the Okay button on the pop-up

    # Using Class_Name location strategy
    Add_Favorite = driver.find_element(MobileBy.ID, "com.android.dialer:id/empty_list_view_action")
    print("Text: ", Add_Favorite.text)
    print("Tagname: ", Add_Favorite.tag_name)
    print("Rectangle: ", Add_Favorite.rect)
    print("Location: ", Add_Favorite.location)
    print("is Displayed: ", Add_Favorite.is_displayed())
    print("is Enabled: ", Add_Favorite.is_enabled())
    print("is Selected: ", Add_Favorite.is_selected())
    print("Get attribute - Package: ", Add_Favorite.get_attribute("package"))
    print("Get attribute - resource-id: ", Add_Favorite.get_attribute("resource-id"))
    print("Get attribute - bounds: ", Add_Favorite.get_attribute("bounds"))

    time.sleep(10)
    driver.quit()


if __name__ == '__main__':
    main()
