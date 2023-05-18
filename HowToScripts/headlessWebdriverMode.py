import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from authentication import USEREMAIL, PASSWORD

# options
options = webdriver.ChromeOptions()

# to leave the browser open and can be interacted with manually
options.add_experimental_option("detach", True)

# disable webdriver mode for ChromeDriver for version 79.0.3945.16 or over
options.add_argument("--disable-blink-features=AutomationControlled")

# enable headless mode (the browser will not open)
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)

url = 'https://www.linkedin.com/'

try:
    driver.get(url)
    time.sleep(3)

    print("Open browser")

    email_input = driver.find_element(By.ID, 'session_key')
    email_input.clear()
    email_input.send_keys(USEREMAIL)
    time.sleep(1)

    print("Input Email")

    password_input = driver.find_element(By.ID, 'session_password')
    password_input.clear()
    password_input.send_keys(PASSWORD)
    time.sleep(1)

    print("Input Password")

    password_input.send_keys(Keys.ENTER)

    print("User has been logged")

except Exception as ex:
    print(ex)

finally:
    # time.sleep(100)
    driver.close()
    driver.quit()
