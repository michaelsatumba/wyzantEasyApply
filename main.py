from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get('https://www.wyzant.com/login')

from dotenv import load_dotenv
load_dotenv()

import os
#print(os.environ)
nameInsert = os.getenv("NAME")
passwordInsert = os.getenv("PASSWORD")
# print(nameInsert)
# print(passwordInsert)

username = browser.find_element("xpath", '/html/body/div[1]/div[3]/div[1]/div/div/div/div/div[8]/form/div[1]/input')
username.send_keys(nameInsert)


password = browser.find_element("xpath", '/html/body/div[1]/div[3]/div[1]/div/div/div/div/div[8]/form/div[2]/input')
password.send_keys(passwordInsert)

loginButton = browser.find_element("xpath", "/html/body/div[1]/div[3]/div[1]/div/div/div/div/div[8]/form/button")
loginButton.click()

jobsButton = browser.find_element(By.CSS_SELECTOR, "#jobs-widget > a")
jobsButton.click()

#/html/body/div[1]/div/div[2]/main/section[1]/div[2]/a
#jobs-widget > a
