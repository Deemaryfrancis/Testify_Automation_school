# Navigate any browser to https://weather.com/
# get the current  temperature and print  it  out  in  the  terminal.
# Then print out the temperature for Morning, Afternoon, Evening, and Overnight.
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

def main():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get("https://weather.com/")

    # Current Temperature:
    current_temperature = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/main/div[1]/div/section/div/div[2]/div[1]/div[1]/span')
    print("Current Temperature: ", current_temperature.text)
    time.sleep(5)

    #Morning Temperature:
    morning_temperature = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/main/div[3]/section/div/ul/li[1]/a/div[1]/span')
    print("Morning temperature: ", morning_temperature.text)
    time.sleep(5)

   #Afternoon Temperature:
    afternoon_temperature = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/main/div[3]/section/div/ul/li[2]/a/div[1]/span')
    print("Afternoon temperature: ", afternoon_temperature.text)
    time.sleep(5)

    #Evening Temperature:
    evening_temperature = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/main/div[3]/section/div/ul/li[3]/a/div[1]/span' )
    print("Evening temperature: ", evening_temperature.text)
    time.sleep(15)

    driver.close()


main()