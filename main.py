# Description: This script will automatically apply to jobs on Wyzant.com
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
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
service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=options)
browser.implicitly_wait(5)

# Login function
def login(browser, username, password):
    browser.get('https://www.wyzant.com/login')
   
    #/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/div[8]/div/div[2]/div/form/div[1]/input
    browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/div[8]/div/div[2]/div/form/div[1]/input').send_keys(username)
    #import pdb; pdb.set_trace()
    browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/div[8]/div/div[2]/div/form/div[2]/input').send_keys(password)
   #/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/div[8]/div/div[2]/div/form/div[2]/input
    #import pdb; pdb.set_trace()
    browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/div[8]/div/div[2]/div/form/button").click()
    print("Logged in")
    #/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/div[8]/div/div[2]/div/form/button

# Go to jobs page function
def go_to_jobs_page(browser):
    browser.find_element(By.CSS_SELECTOR, "#jobs-widget").click()
    print("Clicked jobs widget")

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
        print("Clicked job details")
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
        print(subject_text)
        print("selected appropriate template")
    except NoSuchElementException:
        print("No option with text '{}' found in the select tag.".format(subject_text))
        
# Get name and format it function
def get_name(browser):
    # Find the element that contains the name
    name = browser.find_element(By.CSS_SELECTOR, "#wyzantResponsiveColumns > div.columns.medium-8.small-12 > h4").text
    # Capitalize the name
    formatted_name = name.capitalize()
    # Find the text area element
    text_area = browser.find_element(By.CSS_SELECTOR, "#personal_message")
    # Get current text from the text area
    current_text = text_area.get_attribute("value")
    # Clear the existing text
    text_area.clear()
    # Send the formatted greeting message
    text_area.send_keys(f"Hello {formatted_name}! " + current_text)
    # Print the formatted name in the console
    print(f"Got name: {formatted_name} and formatted it")

# Check and click checkbox function
def check_and_click_checkbox(browser):
    checkbox = None
    try:
        checkbox = browser.find_element(By.CSS_SELECTOR, "#agree_partner_hourly_rate")
        print("Found checkbox")
    except Exception as e:
        print("Checkbox not found.")
        try:
            hourlyRate = browser.find_element(By.CSS_SELECTOR, "#job_application_form > div:nth-child(17) > div.columns.small-12.partner-rate-optional > p")
            rate_text = hourlyRate.text  # "$ 70"
            rate_parts = rate_text.split()  # ["$", "70"]
            rate = float(rate_parts[1])  # 70.0
            print(rate)
            rateInput = browser.find_element(By.CSS_SELECTOR, "#hourly_rate")
            rateInput.clear()  # Clear the input field
            rateInput.send_keys(rate)  # Send the new rate
            print(f"Entered hourly rate '{rate}'")
        except Exception as e:
            print("Hourly rate not found or could not be processed.")

    try:
        checkbox.click()
        print(f"Clicked element with tag name '{checkbox.tag_name}' and attribute '{checkbox.get_attribute('name')}'")
    except Exception as e:
        print(f"Could not click the checkbox. Exception: {e}")

# Submit application function
def submit_application(browser):
    submit_button = browser.find_element(By.CSS_SELECTOR, "#job_application_form > input.btn.old-button-color ")
    submit_button.click()
    print("Submitted application")

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