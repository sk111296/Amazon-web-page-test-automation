import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#open browser
driver = webdriver.Chrome()
driver.maximize_window()

#navigate to https://www.amazon.de/
driver.get("https://www.amazon.de/")

#declining cookies
cookies_decline = driver.find_element(By.XPATH, "/html//button[@id='sp-cc-rejectall-link']")
cookies_decline.click()

time.sleep(2)

#user login
account_list = driver.find_element(By.ID,"nav-link-accountList")
account_list.click()

time.sleep(1)

#pass credentials
email = driver.find_element(By.ID, "ap_email")
email.send_keys("sakshigauravkulkarni@gmail.com")

time.sleep(1)

continue_button = driver.find_element(By.CLASS_NAME, "a-button-input")
continue_button.click()

password = driver.find_element(By.NAME, "password")
password.send_keys("SWARGATE.amazon4")

sign_in_button = driver.find_element(By.ID, "auth-signin-button")
sign_in_button.click()

time.sleep(3)

#search for any item from search bar
search_bar = driver.find_element(By.NAME, "field-keywords")
search_bar.send_keys("Kindle Paperwhite (16GB)")

search_icon = driver.find_element(By.ID, "nav-search-submit-text")
search_icon.click()

time.sleep(4)

div = driver.find_elements(By.CLASS_NAME,'a-declarative')
for i in div:

    href = i.find_element(By.CLASS_NAME, 'a-declarative').get_attribute('href')
    print(href)




