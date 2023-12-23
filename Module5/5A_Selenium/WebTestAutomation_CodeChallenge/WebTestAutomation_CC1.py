# Using the chrome browser navigate to https://www.facebook.com/
# fill  in  the  email/phone  and password text box then click the Login Button.
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.facebook.com/")
    time.sleep(5)
    email_input = driver.find_element(By.NAME, "email").send_keys("minniedion@gmail.com")
    password_input = driver.find_element(By.NAME, "pass").send_keys(Keys.CONTROL, "v")
    login_click = driver.find_element(By.NAME, "login").click()
    time.sleep(5)
    driver.close()

main()