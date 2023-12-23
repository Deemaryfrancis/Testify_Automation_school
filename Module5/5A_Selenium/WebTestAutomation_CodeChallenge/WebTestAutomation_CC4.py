# Navigate to https://www.bbc.com/ and
# print  out  the top 10 latest news from the home page
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

def main():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get("https://www.bbc.com/")
    time.sleep(15)
    Header = driver.find_element(By.XPATH, '/html/body/div[6]/header/div/div')
    navigate_to_new_section = Header.find_element(By.XPATH, '/html/body/div[6]/header/div/div/nav[2]/ul/li[2]/a/span').click()
    top_stories = driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div[4]/div[2]/div/div")
    time.sleep(15)
    print(top_stories.text)
    time.sleep(10)
    #driver.close()

main()