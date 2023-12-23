#Navigate to the website https://www.facebook.com/
#Find the email box and enter an email value
#Find the password box and enter a password value
#Find the Login button and click it
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_element(elements, *keys):
    elements.send_keys(keys)

def actions_chains(action, element):
    action.move_to_element(element).perform()
    time.sleep(2)
    action.scroll_by_amount(0, 15)
    time.sleep(2)
    action.scroll_by_amount(0, 15)
    time.sleep(2)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.facebook.com")
    time.sleep(5)
    action = ActionChains(driver)
    actions_chains(action, driver.find_element(By.XPATH, '//*[@id="pageFooter"]'))
    time.sleep(5)
    get_form = driver.find_element(By.TAG_NAME, "form")
    get_email = get_form.find_element(By.XPATH, '//*[@id="email"]')
    get_password = get_form.find_element(By.XPATH, '//*[@id="pass"]')
    get_element(get_email, "minniedion@gmail.com")
    get_element(get_password, Keys.CONTROL, "v")
    time.sleep(5)
    mask_password = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/div/a/div/div').click()
    time.sleep(2)
    Unmask_password = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/div/a/div/div').click()
    time.sleep(2)
    click_login = get_form.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click()
    time.sleep(5)

main()