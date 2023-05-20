# Description: This script will automatically apply to jobs on Wyzant.com
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from dotenv import load_dotenv

# Load login credentials from .env file
load_dotenv()
username = os.getenv("NAME")
password = os.getenv("PASSWORD")

# Setup web driver
options = Options()
# options.add_argument("--headless")
browser = webdriver.Chrome(options=options)
browser.implicitly_wait(1)

# Login function
def login(browser, username, password):
    browser.get('https://www.wyzant.com/login')
    browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/div/div/div/div[8]/form/div[1]/input').send_keys(username)
    browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/div/div/div/div[8]/form/div[2]/input').send_keys(password)
    browser.find_element(By.CSS_SELECTOR, "#sso_login-landing > form > button").click()
    print("Logged in")

# Go to jobs page function
def go_to_jobs_page(browser):
    browser.find_element(By.CSS_SELECTOR, "#jobs-widget").click()
    # print("Clicked jobs widget")

# Click job details function         
def click_job_details(browser):
    try:
        element = WebDriverWait(browser, 2).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#jobs-list > div:nth-child(1) > div > div > h3 > a"))
        )
    except TimeoutException:
        print("timeout exception")
        return False

    try:
        element.click()
        return True
    except:
        print("Could not click job details")
        return False



# Select subject function
def select_subject(browser):
    subject_one = browser.find_element(By.CSS_SELECTOR, "#wyzantResponsiveColumns > div.columns.medium-8.small-12 > h1")
    subject_text = subject_one.text
    select_element = browser.find_element(By.CSS_SELECTOR, "#template_select")
    choose = Select(select_element)

    try:
        choose.select_by_visible_text(subject_text)
        # print("selected apprpriate template")
    except NoSuchElementException:
        print("No option with text '{}' found in the select tag.".format(subject_text))
        
# Get name and format it function
def get_name(browser):
    name = browser.find_element(By.CSS_SELECTOR, "#wyzantResponsiveColumns > div.columns.medium-8.small-12 > h4").text
    formatted_name = name.capitalize()
    text_area = browser.find_element(By.CSS_SELECTOR, "#personal_message")
    current_text = text_area.get_attribute("value")
    text_area.clear()
    text_area.send_keys(f"Hello {formatted_name}! " + current_text)
    # print("Got name and formatted it")

# Check and click checkbox function
def check_and_click_checkbox(browser):
    checkbox = None
    try:
        checkbox = browser.find_element(By.CSS_SELECTOR, "#agree_partner_hourly_rate")
    except:
        # print("Checkbox not found.")
        return

    try:
        checkbox.click()
        print(f"Clicked element with tag name '{checkbox.tag_name}' and attribute '{checkbox.get_attribute('name')}'")
    except Exception as e:
        print(f"Could not click the checkbox. Exception: {e}")

# Submit application function
def submit_application(browser):
    submit_button = browser.find_element(By.CSS_SELECTOR, "#job_application_form > input.btn.old-button-color ")
    submit_button.click()

# Login function
login(browser, username, password)

# Go to jobs page function
go_to_jobs_page(browser)

# Loop through jobs
i = 0
while True:
    if not click_job_details(browser):
        print("No more jobs.")
        break
    select_subject(browser)
    get_name(browser)
    check_and_click_checkbox(browser)
    submit_application(browser)
    i += 1
    print("Applied to job", i)


browser.quit()

