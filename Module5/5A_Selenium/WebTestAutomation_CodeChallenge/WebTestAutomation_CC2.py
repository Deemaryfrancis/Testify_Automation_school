# Using the firefox browser navigate to https://www.google.com/
# enter the text Python in  the search  box, then send the Enter  key.
# Get  the  text  from  the Wikipedia  brief  on  the  right  side  and
# print  the  value  in  the console.
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

def main():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get("https://www.google.com/")
    searchBox_input = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Python", Keys.ENTER)
    time.sleep(15)
    wikipedia_get_brief = driver.find_element(By.XPATH, "/html/body/div[7]/div/div[11]/div[2]/div/div/div[2]/div/div[5]/div/div/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div/div")
    print(wikipedia_get_brief.text)
    time.sleep(20)
    driver.close()


main()