#  Using any browser navigate to any Youtube video of your choice,
#  allow your script to wait for the comments to load
#  then get the first two comments, and print them in the terminal.
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def main():
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    driver.get("https://www.youtube.com/watch?v=oqDfLunw_BU")
    time.sleep(50)

main()