import code
from operator import index
from turtledemo.sorting_animate import Block

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome()
driver.get('http://demo4.msampleqa.in/login')  # Replace with your login page URL
time.sleep(2)
username_field = driver.find_element(By.CSS_SELECTOR,"input.form-control[formcontrolname=userId]")  # or another method like By.ID
password_field = driver.find_element(By.CSS_SELECTOR,"input.form-control[formcontrolname=password]")
username_field.send_keys('1')
password_field.send_keys('Admin@123')
time.sleep(5)
login_button = driver.find_element(By.XPATH, "//*[text()='Login']")  # Replace with actual XPath of login button
login_button.click()
time.sleep(5)
if "Dashboard" in driver.title:  # Check for specific page or title after login
    print("Login successful!")
else:
    print("Login failed!")
time.sleep(5)
# driver.get('http://demo4.msampleqa.in/auth/resident')
# time.sleep(5)
# login_button = driver.find_element(By.XPATH, "//button[@class='button-uxcl btn-new']")
time.sleep(5)
# driver.get('http://demo4.msampleqa.in/auth/resident/add-resident/Add')
# residentType_field = driver.find_element(By.CSS_SELECTOR,"input.form-control[formcontrolname="residenceTypeId"]")
# block_field = driver.find_element(By.CSS_SELECTOR,"input.form-control[formcontrolname="blockId"]")
driver.quit()