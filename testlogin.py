from tkinter import image_types

from selenium import webdriver
import re
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('http://demo4.msampleqa.in/login')
driver.find_element(By.CSS_SELECTOR,"input.form-control[formcontrolname=userId]").send_keys('1')
driver.find_element(By.CSS_SELECTOR,"input.form-control[formcontrolname=password]").send_keys('Admin@123')
time.sleep(5)
driver.find_element(By.XPATH, "//app-login//button").click()
time.sleep(10)
title = driver.title
if "dashboard" in driver.title:
    print("Login successful!")
else:
    print("Login failed!")
print(driver.title)
time.sleep(10)
driver.find_element(By.XPATH, value="//mat-expansion-panel-header//span[1]//mat-panel-title//div//span").click()
time.sleep(5)
driver.find_element(By.XPATH, value="//div[@id='cdk-accordion-child-0']//mat-list-item//div").click()
time.sleep(5)
driver.find_element(By.XPATH, value="//app-resident-list//app-table//button[1]").click()
time.sleep(5)
driver.find_element(By.XPATH, "//select[@formcontrolname='residenceTypeId']/option[@value='1']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//select[@formcontrolname='blockId']/option[@value='3']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//select[@formcontrolname='flatId']/option[@value='32']").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "input.form-control[formcontrolname=firstName]").send_keys('Parthiban')
# time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "input.form-control[formcontrolname=lastName]").send_keys('Leo')
# time.sleep(4)
def validate_mobileNo(mobileNo):
    pattern = r"^\d{10}$"
    if re.match(pattern, mobileNo):
        return True
    else:
       return False

driver.find_element(By.CSS_SELECTOR, "input.form-control[formcontrolname=mobileNo]").send_keys('95059680001')
# time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "input.form-control[formcontrolname=email]").send_keys('parthiban@gmail.com')
time.sleep(5)
driver.find_element(By.XPATH, "//select[@formcontrolname='documentTypeId']/option[@value='1']").click()
driver.find_element(By.CSS_SELECTOR, "input[type='app-file-upload']")
image_types('https://drive.google.com/open?id=1J-BQ_zOxsKtZ8wdgPseMBi8hvC9eGTQD&usp=drive_copy')
driver.find_element(By.CSS_SELECTOR, "input.form-control[formcontrolname=comments]").send_keys('comments for the resident')
driver.find_element(By.XPATH, "//app-resident-add-update-view//form//div[4]//div[2]//div//span").click()
time.sleep(5)
driver.find_element(By.XPATH, "//select[@formcontrolname='ageGroup']/option[@value='Adult']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//select[@formcontrolname='relationshipId']/option[@value='1']").click()
driver.find_element(By.CSS_SELECTOR, "input.form-control[formcontrolname=firstName]").send_keys('satyabhama')
driver.find_element(By.CSS_SELECTOR, "input.form-control[formcontrolname='lastName']").send_keys('Parthiban')


# driver.find_element(By.XPATH, "//button[@id='addButton']").click()
# if "resident" in driver.title:
#     print("resident added succesfully")
# else:
#     print("error occurred while adding resident")
#     print(driver.title)
# time.sleep(10)


driver.close()
