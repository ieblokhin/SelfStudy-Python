import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from authentication import USEREMAIL, PASSWORD

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

url = 'https://www.linkedin.com/'

try:
    driver.get(url)
    time.sleep(3)

    email_input = driver.find_element(By.ID, 'session_key')
    email_input.clear()
    email_input.send_keys(USEREMAIL)
    time.sleep(1)

    password_input = driver.find_element(By.ID, 'session_password')
    password_input.clear()
    password_input.send_keys(PASSWORD)
    time.sleep(1)
    password_input.send_keys(Keys.ENTER)

except Exception as ex:
    print(ex)

finally:
    time.sleep(100)
    driver.close()
    driver.quit()
