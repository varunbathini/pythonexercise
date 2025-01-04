import code
from operator import index
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome()

# Open the login page URL
driver.get('http://demo4.msampleqa.in/login')  # Replace with your login page URL

# Wait for the page to load
time.sleep(2)

# Locate the username and password fields (you need to replace the element identifiers)
username_field = driver.find_element(By.CSS_SELECTOR,"input.form-control[formcontrolname=userId]")  # or another method like By.ID
password_field = driver.find_element(By.CSS_SELECTOR,"input.form-control[formcontrolname=password]")

# Input credentials into the form
username_field.send_keys('1')
password_field.send_keys('Admin@123')
time.sleep(5)

driver.find_element(By.XPATH, "//*[text()='Login']")  # Replace with actual XPath of login button, we can use * instead of button in the above code line
title = driver.title

# Wait for login to complete (adjust time as necessary)
time.sleep(5)

# Optionally, verify successful login or navigate further
if "Dashboard" in driver.title:  # Check for specific page or title after login
    print("Login successful!")
else:
    print("Login failed!")

# Close the browser after the operation
driver.quit()
