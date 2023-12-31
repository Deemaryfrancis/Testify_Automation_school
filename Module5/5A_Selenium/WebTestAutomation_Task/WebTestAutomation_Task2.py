#Visit the website https://academy.testifyltd.com/
#Locate the button with the text "Explore Courses" and print out the element
#Locate the element with the text "Subscribe to receive training updates from Testify" and print it.


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def exploreCourses(driver):
    explore_courses = driver.find_element(By.XPATH, "//html/body/div/main/section[1]/div/div/div[1]/div/button")
    print(explore_courses.text)

def Subscribe(element):
    print(element.accessible_name)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://academy.testifyltd.com")
    subscribe = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[11]/div/div/div[1]/h2')
    Subscribe(subscribe)
    exploreCourses(driver)
main()