import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# When writing the app name, always change backward slash "\" to forward slash "/"
def main():
    desired_caps = {
        "deviceName": "Android Emulator",
        "platformName": "Android",
        "platformVersion": "12",
        "app": "C:/Users/Mary_Thompson/OneDrive/Documents/mobileTestingApks/Calculator_1.12.0_Apkpure.apk",
        "appPackage": "com.tricolorcat.calculator",
        "noSign": True
    }

    driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)
    # click the Okay button on the pop-up

    # Using Class_Name location strategy
    frameWork = driver.find_element(MobileBy.CLASS_NAME, "android.widget.LinearLayout")
    okButton = frameWork.find_element(MobileBy.CLASS_NAME, "android.widget.Button")
    okButton.click()

    # Calculate sum of two numbers
    # Using Class_Name location strategy
    num1_el = driver.find_element(MobileBy.ID, "com.tricolorcat.calculator:id/one")
    plus_el = driver.find_element(MobileBy.ID, "com.tricolorcat.calculator:id/plus")
    num2_el = driver.find_element(MobileBy.ID, "com.tricolorcat.calculator:id/six")
    eq_el = driver.find_element(MobileBy.ID, "com.tricolorcat.calculator:id/equal")

    num1_el.click()
    plus_el.click()
    num2_el.click()
    eq_el.click()

    time.sleep(10)
    driver.quit()


if __name__ == '__main__':
    main()


def main2():
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
    frameWork = driver.find_element(MobileBy.CLASS_NAME, "android.widget.LinearLayout")
    okButton = frameWork.find_element(MobileBy.CLASS_NAME, "android.widget.Button")
    okButton.click()

    # Calculate sum of two numbers
    # Using Class_Name location strategy
    num1_el = driver.find_element(MobileBy.ID, "com.tricolorcat.calculator:id/one")
    plus_el = driver.find_element(MobileBy.ID, "com.tricolorcat.calculator:id/plus")
    num2_el = driver.find_element(MobileBy.ID, "com.tricolorcat.calculator:id/six")
    eq_el = driver.find_element(MobileBy.ID, "com.tricolorcat.calculator:id/equal")

    num1_el.click()
    plus_el.click()
    num2_el.click()
    eq_el.click()

    time.sleep(10)
    driver.quit()


if __name__ == '__main2__':
    main2()
