from selenium import webdriver

def main():
    driver = webdriver.Chrome(executable_path=r"C:\Users\Mary_Thompson\OneDrive\Documents\TAutomationSchool\Test_Automation _School\Test_Automation_School_Assessments\Web_Driver\chromedriver_win32/chromedriver.exe")
    driver.get("https://www.google.com/")
    from time import sleep
    sleep(1000)
    driver.close()

main()