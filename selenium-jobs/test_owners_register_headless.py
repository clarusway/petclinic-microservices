from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
# Set chrome options for working with headless mode (no screen)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
# Update webdriver instance of chrome-driver with adding chrome options
driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=chrome_options)
# Connect to the application
url = "http://3.236.242.104:8080"
driver.get(url)
owners_link = driver.find_element_by_link_text("OWNERS")
owners_link.click()
all_link = driver.find_element_by_link_text("REGISTER")
all_link.click()
# Register new Owner to Petclinic App
fn_field = driver.find_element_by_name('firstName')
fn = 'Edip' + str(random.randint(0, 100))
fn_field.send_keys(fn)
fn_field = driver.find_element_by_name('lastName')
fn_field.send_keys('Clarusway')
fn_field = driver.find_element_by_name('address')
fn_field.send_keys('Ridge Corp. Street')
fn_field = driver.find_element_by_name('city')
fn_field.send_keys('McLean')
fn_field = driver.find_element_by_name('telephone')
fn_field.send_keys('+1230576803')
fn_field.send_keys(Keys.ENTER)
# Wait until Owner List table loaded
verify_table = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "table")))
# Verify that new user is added to Owner List
if fn in driver.page_source:
    print(fn, 'is added and found in the Owners Table')
    print("Test Passed")
else:
    print(fn, 'is not found in the Owners Table')
    print("Test Failed")
driver.quit()