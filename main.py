from selenium import webdriver
#browser = webdriver.Chrome()

#browser.get('https://www.wyzant.com/login')

from dotenv import load_dotenv
load_dotenv()

import os
#print(os.environ)
nameInsert = os.getenv("NAME")
print(nameInsert)
