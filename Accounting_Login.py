from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("http://demo2.msampleqa.in/login")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, value="input.form-control[formcontrolname=email]").send_keys("varun.b@gmail.com")
driver.find_element(By.CSS_SELECTOR, value="input.form-control[formcontrolname=password]").send_keys("Admin@123")
time.sleep(5)
driver.find_element(By.XPATH, "//app-login//button//span[1]").click()
time.sleep(10)
if "Dashboard" in driver.title:
    print("Login Successfull")
else:
    print("Login Failed")
time.sleep(10)
print(driver.title)
