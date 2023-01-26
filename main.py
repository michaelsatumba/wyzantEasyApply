from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

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
print("logged in")


wait = WebDriverWait(browser, 10)
jobsButton = wait.until(EC.presence_of_element_located((By.ID, "jobs-widget")))
jobsButton.click()

print("jobs page")

'''
i = 0
while i < 50:
    firstJob = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "job-details-link")))
    firstJob.click()

    SubjectOne = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    subjectText = SubjectOne.text
    # print(subjectText)

    select_element = wait.until(EC.presence_of_element_located((By.ID, "template_select")))
    choose = Select(select_element)

    try:
        choose.select_by_visible_text(subjectText)
    except NoSuchElementException:
        print("No option with text '{}' found in the select tag.".format(subjectText))

    try:
        checkbox = browser.find_element_by_xpath("//input[@type='checkbox']")
        print("has checkbox")
        checkbox.click()
    except:
        pass

    submitApplication = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#job_application_form > input.btn.old-button-color ")))
    submitApplication.click()
    i += 1
    print("applied to " + str(i) + " jobs")
'''

def click_job_details(browser, wait):
    first_job = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "job-details-link")))
    print("click job details")
    first_job.click()

def select_subject(browser, wait):
    subject_one = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    subject_text = subject_one.text
    select_element = wait.until(EC.presence_of_element_located((By.ID, "template_select")))
    choose = Select(select_element)

    try:
        choose.select_by_visible_text(subject_text)
        print("selected apprpriate template")
    except NoSuchElementException:
        print("No option with text '{}' found in the select tag.".format(subject_text))

def check_and_click_checkbox(browser, wait):
    try:
        checkbox = wait.until(EC.presence_of_element_located((By.ID, "agree_partner_hourly_rate")))
        #//*[@id="agree_partner_hourly_rate"]
        #/html/body/div[1]/div[1]/form/div[5]/div[3]/input
        print("checkbox found")
        checkbox.click()
    except:
        print("no checkbox")
        pass

def submit_application(browser, wait):
    submit_application = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#job_application_form > input.btn.old-button-color ")))
    submit_application.click()

i = 0
while i < 50:
    click_job_details(browser, wait)
    select_subject(browser, wait)
    check_and_click_checkbox(browser, wait)
    submit_application(browser, wait)
    i += 1
    print("applied to " + str(i) + " jobs")


