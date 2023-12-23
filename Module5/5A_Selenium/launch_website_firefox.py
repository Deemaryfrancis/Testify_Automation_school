from time import sleep
from selenium import webdriver

def main():
    driver = webdriver.Firefox(executable_path=r"C:\Users\Mary_Thompson\OneDrive\Documents\TAutomationSchool\Test_Automation _School\Test_Automation_School_Assessments\Web_Driver\geckodriver-v0.32.0-win32/geckodriver.exe")
    driver.get("https://www.google.com/")
    sleep(1000)
    driver.close()

main()