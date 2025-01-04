from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the login page URL
driver.get('https://example.com/login')  # Replace with your login page URL

# Wait for the page to load
time.sleep(2)

# Locate the username and password fields (you need to replace the element identifiers)
username_field = driver.find_element(By.NAME, 'username')  # or another method like By.ID
password_field = driver.find_element(By.NAME, 'password')

# Input credentials into the form
username_field.send_keys('your_username')  # Replace with your username
password_field.send_keys('your_password')  # Replace with your password

# Find and click the login button
login_button = driver.find_element(By.XPATH, '//*[@id="loginButton"]')  # Replace with actual XPath of login button
login_button.click()

# Wait for login to complete (adjust time as necessary)
time.sleep(5)

# Optionally, verify successful login or navigate further
if "Dashboard" in driver.title:  # Check for specific page or title after login
    print("Login successful!")
else:
    print("Login failed!")

# Close the browser after the operation
driver.quit()
