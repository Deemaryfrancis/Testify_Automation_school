#Navigate to the website https://academy.testifyltd.com/
#Get the element with the text "© 2022 Testify Limited. All rights reserved."
#Print out the element text, and properties, and it attributes


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def get_rights(elements):
    print("Text: ", elements.text)
    #Element attributes
    print("Attributes -ID: ", elements.get_attribute("id"))
    print("Attributes - Class: ", elements.get_attribute("class"))
    print("Attributes - Style: ", elements.get_attribute("style"))
    print("Attributes - Inner Text: ", elements.get_attribute("innerText"))
    print("Attributes - inner HTMl:  ", elements.get_attribute("innerHTML"))
    #Element Property
    print("Properties - Value:  ", elements.get_property("value"))
    print("Properties - href:  ", elements.get_property("href"))
    print("Properties - Text_length:  ", elements.get_property("text_length"))


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://academy.testifyltd.com")
    getrights = driver.find_element(By.XPATH, '//*[@id="__next"]/section/div/div[2]/div[2]')
    get_rights(getrights)

main()


