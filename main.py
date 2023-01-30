import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# load login credentials from .env file
from dotenv import load_dotenv
load_dotenv()
nameInsert = os.getenv("NAME")
passwordInsert = os.getenv("PASSWORD")

def login(browser):
    browser.get('https://www.wyzant.com/login')
    username = browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/div/div/div/div[8]/form/div[1]/input')
    username.send_keys(nameInsert)
    password = browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/div/div/div/div[8]/form/div[2]/input')
    password.send_keys(passwordInsert)
    login_button = browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div/div/div/div/div[8]/form/button")
    login_button.click()
    # print("logged in")

def go_to_jobs_page(browser, wait):
    jobs_button = wait.until(EC.presence_of_element_located((By.ID, "jobs-widget")))
    jobs_button.click()
    # print("jobs page")


def click_job_details(browser, wait):
    first_job = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "job-details-link")))
    # print("click job details")
    first_job.click()

def select_subject(browser, wait):
    subject_one = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    subject_text = subject_one.text
    select_element = wait.until(EC.presence_of_element_located((By.ID, "template_select")))
    choose = Select(select_element)

    try:
        choose.select_by_visible_text(subject_text)
        # print("selected apprpriate template")
    except NoSuchElementException:
        print("No option with text '{}' found in the select tag.".format(subject_text))

# TODO: get name of student and insert into message
'''
def get_name(browser, wait):
    name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#wyzantResponsiveColumns > div.columns.medium-8.small-12 > h4")))
    name_text = name.text
    lowercase_string = name_text.lower()
    uppercase_first_letter_string = lowercase_string.capitalize()
    print(upercase_first_letter_string)
    
    text_area = wait.until(EC.presence_of_element_located((By.ID, "personal_message")))
    text_area.click()
    text_area.send_keys("Hello" + uppercase_first_letter_string + ",")
'''
def check_and_click_checkbox(browser, wait):
    try:
        checkbox = wait.until(EC.presence_of_element_located((By.ID, "agree_partner_hourly_rate")))
        print("checkbox found")
        checkbox.click()
    except:
        print("no checkbox")
        pass

def submit_application(browser, wait):
    submit_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#job_application_form > input.btn.old-button-color ")))
    submit_button.click()

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
login(browser)
go_to_jobs_page(browser, wait)

i = 0
while i < 50:
    click_job_details(browser, wait)
    select_subject(browser, wait)
    #get_name(browser, wait)
    check_and_click_checkbox(browser, wait)
    submit_application(browser, wait)
    i += 1
    print("applied to " + str(i) + " jobs")


