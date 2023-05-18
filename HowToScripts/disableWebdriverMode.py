import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from authentication import USEREMAIL, PASSWORD

# options
options = webdriver.ChromeOptions()

# to leave the browser open and can be interacted with manually
options.add_experimental_option("detach", True)

# disable webdriver mode for ChromeDriver for version 79.0.3945.16 or over
options.add_argument("--disable-blink-features=AutomationControlled")

# # disable webdriver mode for older ChromeDriver under version 79.0.3945.16
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(options=options)

url = 'https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html'

try:
    driver.get(url)
    time.sleep(3)

except Exception as ex:
    print(ex)

finally:
    # time.sleep(100)
    driver.close()
    driver.quit()
