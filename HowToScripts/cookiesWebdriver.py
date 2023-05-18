import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from authentication import USEREMAIL, PASSWORD
import pickle

# options
options = webdriver.ChromeOptions()
# to leave the browser open and can be interacted with manually
options.add_experimental_option("detach", True)

# disable webdriver mode for ChromeDriver for version 79.0.3945.16 or over
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=options)

url = 'https://www.linkedin.com/'

try:
    # driver.get(url)
    # time.sleep(3)
    #
    # email_input = driver.find_element(By.ID, 'session_key')
    # email_input.clear()
    # email_input.send_keys(USEREMAIL)
    # time.sleep(1)
    #
    # password_input = driver.find_element(By.ID, 'session_password')
    # password_input.clear()
    # password_input.send_keys(PASSWORD)
    # time.sleep(1)
    # password_input.send_keys(Keys.ENTER)
    # time.sleep(3)
    #
    # # Create and save cookies file for Login
    # pickle.dump(driver.get_cookies(), open(f"{USEREMAIL}_cookies", "wb"))

    #Load saved cookies for Login
    driver.get(url)
    for cookie in pickle.load(open(f"{USEREMAIL}_cookies", "rb")):
        driver.add_cookie(cookie)

    time.sleep(3)
    driver.refresh()
    time.sleep(10)

except Exception as ex:
    print(ex)

finally:
    # time.sleep(100)
    driver.close()
    driver.quit()
