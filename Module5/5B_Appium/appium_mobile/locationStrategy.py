import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# To get the package name
# start the android Device Bridge, use : adb shell
# then type: pm list packages -f

# To know the app activities
# adb shell dumpsys package | grep -i "<packagename>" | grep Activity

# To view adb log
# type  adb logcat

def main():
    desired_caps = {
        "deviceName": "Android Emulator",
        "platformName": "Android",
        "platformVersion": "12",
        "appPackage": "com.android.dialer",
        "appActivity": ".debug.ContactsDumpActivity",
        "noSign": True
    }

    driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)
    time.sleep(10)
    driver.quit()


if __name__ == '__main__':
    main()
