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
        # Start a server on the folder containing the apk by writing the code below in the command prompt
        # python -m -http.server 9010 (you can use any port number)
        "app": "http://127.0.0.1:9010/Calculator_1.12.0_Apkpure.apk",  # add server address
        "appPackage": "com.tricolorcat.calculator",
        "noSign": True
    }

    driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)
    time.sleep(10)
    driver.quit()


if __name__ == '__main__':
    main()
