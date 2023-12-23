#Create a page object model for this page https://academy.testifyltd.com/courses/test-automation-simplified
#Create another object model for this page https://academy.testifyltd.com/courses/switch-to-software-testing
#The web elements in each of your object models should not be more than 5.
import time

from WebTestAutomation_Task.WebTestAutomation_Task5.pom.TestAutomationSimplied import testAutomationSimplied
from WebTestAutomation_Task.WebTestAutomation_Task5.pom.SwitchToSoftwareTesting import switchToSoftwareTesting
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def main():
 driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
 driver.maximize_window()

 # Switch to Software Testing
 Switch_To_Software_Testing = switchToSoftwareTesting(driver)
 time.sleep(15)
 print("STST Page Title: ", Switch_To_Software_Testing.title.text)
 Switch_To_Software_Testing.Enroll_button.click()
 time.sleep(10)
 print("STST Course Overview: ", Switch_To_Software_Testing.Course_overview.text)
 time.sleep(10)
 print("STST Course module: ", Switch_To_Software_Testing.Course_module.text)
 print(" ")
 time.sleep(5)

 #TestAutomation Simplified
 Test_Automation_simplified = testAutomationSimplied(driver)
 time.sleep(15)
 print("TAS Page Title: ", Test_Automation_simplified.title.text)
 Test_Automation_simplified.Enroll_button.click()
 time.sleep(10)
 print("TAS Course Overview: ", Test_Automation_simplified.Course_overview.text)
 time.sleep(10)
 print("TAS Course module: ", Test_Automation_simplified.Course_module.text)


main()