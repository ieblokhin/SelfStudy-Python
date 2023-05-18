from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
import time

# Retrieve values from environment variables
firstname = os.environ.get('FNAME')
lastname = os.environ.get('LNAME')
username = os.environ.get('USER')
password = os.environ.get('PASS')
confirm_password = os.environ.get('CPASS')
phoneNumber = os.environ.get('PHONE')
recoveryEmail = os.environ.get('RECOVERYEMAIL')

# Options for Edge
browser_options = Options()
browser_options.add_experimental_option("detach", True)
browser_options.add_argument("--inPrivate")  # option to open browser in incognito mode

# Set up the webdriver
driver = webdriver.Edge(options=browser_options)
# Navigate to the Gmail sign-up page
driver.get('https://accounts.google.com/signup/v2/webcreateaccount?hl=en&flowName=GlifWebSignIn&flowEntry=SignUp')
driver.maximize_window()
driver.delete_all_cookies()

# Fill in the required information
driver.find_element(By.ID, 'firstName').send_keys(firstname)
driver.find_element(By.ID, 'lastName').send_keys(lastname)
driver.find_element(By.ID, 'username').send_keys(username)
driver.find_element(By.NAME, 'Passwd').send_keys(password)
driver.find_element(By.NAME, 'ConfirmPasswd').send_keys(confirm_password)

# Click the button to create the account
driver.find_element(By.XPATH, '//*[@id="accountDetailsNext"]').click()

# Wait for the verification page to load
time.sleep(3)
# driver.implicitly_wait(300)
# Enter your phone number for verification
driver.find_element(By.ID, 'phoneNumberId').send_keys(phoneNumber)
driver.find_element(By.CLASS_NAME, 'VfPpkd-vQzf8d').click()

time.sleep(3)
# Enter the verification code sent to your phone
verification_code = input('Enter the verification code sent to your phone: ')
driver.implicitly_wait(300)
driver.find_element(By.NAME, 'code').send_keys(verification_code)
driver.find_element(By.CLASS_NAME, 'VfPpkd-vQzf8d').click()
print('Your new Gmail account has been created!')

time.sleep(3)
driver.find_element(By.NAME, 'recoveryEmail').send_keys(recoveryEmail)
birthday_month = Select(driver.find_element(By.ID, 'month')).select_by_value('4')
driver.find_element(By.NAME, 'day').send_keys('20')
driver.find_element(By.NAME, 'year').send_keys('1985')
gender = Select(driver.find_element(By.ID, 'gender')).select_by_value('1')
time.sleep(3)
driver.find_element(By.XPATH, "//span[contains(text(), 'Next')]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[contains(text(), 'Yes, I’m in')]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[contains(text(), 'I agree')]").click()

# Close the webdriver
driver.quit()
