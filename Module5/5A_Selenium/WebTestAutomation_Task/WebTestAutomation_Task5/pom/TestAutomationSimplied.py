from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class testAutomationSimplied():

    def __init__(self, driver):
        driver.get("https://academy.testifyltd.com/courses/test-automation-simplified")
        self.title = driver.find_element(By.TAG_NAME, "h1")
        self.Enroll_button = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/div/div/div[1]/div/button')
        self.Course_overview = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[5]/div')
        self.Course_module = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[6]/div/div[1]')
