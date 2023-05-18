import os
import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By


# Retrieve username and password from environment variables
username = os.environ.get('USEREMAIL')
password = os.environ.get('PASSWORD')

# Options for Edge
browser_options = Options()
browser_options.add_experimental_option("detach", True)
browser_options.add_argument("--inPrivate")  # option to open browser in incognito mode

# Instantiate webdriver object with options
driver = webdriver.Edge(options=browser_options)
driver.get('http://linkedin.com')
driver.maximize_window()
# driver.delete_all_cookies()

time.sleep(3)
# Specify the fields and Submit the login form
driver.find_element(By.ID, 'session_key').send_keys(username)
driver.find_element(By.ID, 'session_password').send_keys(password)
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, '#main-content > section.section.min-h-\[560px\].flex-nowrap.pt-\[40px\].babybear\:flex-col.babybear\:min-h-\[0\].babybear\:px-mobile-container-padding.babybear\:pt-\[24px\] > div > div > form:nth-child(7) > div.flex.justify-between.sign-in-form__footer--full-width > button').click()

# Close the browser session
driver.quit()
