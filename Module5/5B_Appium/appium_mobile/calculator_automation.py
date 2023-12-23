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
    okButton = driver.find_element(MobileBy.ID, "com.tricolorcat.calculator:id/btOK")
    okButton.click()

    # Calculate sum of two numbers
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
