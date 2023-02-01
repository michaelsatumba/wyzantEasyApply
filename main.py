# Description: This script will automatically apply to jobs on Wyzant.com
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from dotenv import load_dotenv

# Load login credentials from .env file
load_dotenv()
username = os.getenv("NAME")
password = os.getenv("PASSWORD")

# Login function
def login(browser, username, password):
    browser.get('https://www.wyzant.com/login')
    browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/div/div/div/div[8]/form/div[1]/input').send_keys(username)
    browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/div/div/div/div[8]/form/div[2]/input').send_keys(password)
    browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div/div/div/div/div[8]/form/button").click()
    print("Logged in")

# Go to jobs page function
def go_to_jobs_page(browser, wait):
    wait.until(EC.presence_of_element_located((By.ID, "jobs-widget"))).click()
    print("Clicked jobs widget")

# Click job details function
def click_job_details(browser, wait):
    try:
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "job-details-link"))).click()
        print("Clicked job details")
    except:
        print("No more jobs.")
        sys.exit()


# Select subject function
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
        
# Get name and format it function
def get_name(browser, wait):
    name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#wyzantResponsiveColumns > div.columns.medium-8.small-12 > h4"))).text
    formatted_name = name.capitalize()
    text_area = wait.until(EC.presence_of_element_located((By.ID, "personal_message")))
    current_text = text_area.get_attribute("value")
    text_area.clear()
    text_area.send_keys(f"Hello {formatted_name}! " + current_text)
    print("Got name and formatted it")

# Check and click checkbox function
def check_and_click_checkbox(browser, wait):
    try:
        # checkbox = wait.until(EC.presence_of_element_located((By.ID, "agree_partner_hourly_rate")))
        # checkbox = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/form/div[5]/div[3]/input")))
        checkbox = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#agree_partner_hourly_rate")))
        print("Checkbox found.")
        checkbox.click()
        print("Checkbox clicked.")
    except:
        print("Checkbox not found.")
        pass
  

# Submit application function
def submit_application(browser, wait):
    submit_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#job_application_form > input.btn.old-button-color ")))
    submit_button.click()

# Main function
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
login(browser, username, password)
go_to_jobs_page(browser, wait)

# Loop through jobs
for i in range(50):
    click_job_details(browser, wait)
    select_subject(browser, wait)
    get_name(browser, wait)
    check_and_click_checkbox(browser, wait)
    submit_application(browser, wait)
    print("Applied to job", i + 1)




