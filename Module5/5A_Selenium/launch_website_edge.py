from time import sleep

from selenium import webdriver

def main():
    driver = webdriver.Edge(executable_path="C:/Users/Mary_Thompson/OneDrive/Documents/TAutomationSchool/Test_Automation _School/Test_Automation_School_Assessments/Web_Driver/edgedriver_win64/msedgedriver.exe")
    driver.get("https://www.google.com/")
    sleep(1000)
    driver.close()

main()