from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

wait = WebDriverWait(browser, 10)
jobsButton = wait.until(EC.presence_of_element_located((By.ID, "jobs-widget")))
jobsButton.click()

firstJob = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "job-details-link")))
firstJob.click()


selectButton = wait.until(EC.presence_of_element_located((By.ID, "template_select")))
selectButton.click()
