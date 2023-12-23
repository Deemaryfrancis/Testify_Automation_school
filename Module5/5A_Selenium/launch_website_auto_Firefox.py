import manager as manager
from selenium import webdriver
from selenium.webdriver.firefox.service import service, Service
from webdriver_manager.firefox import GeckoDriverManager

def main():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get("https://www.google.com/")
    from time import sleep
    sleep(1000)
    driver.close()


main()