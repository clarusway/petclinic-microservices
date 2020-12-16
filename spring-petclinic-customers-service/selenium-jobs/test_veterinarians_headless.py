from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
# Set chrome options for working with headless mode (no screen)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
# Update webdriver instance of chrome-driver with adding chrome options
driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=chrome_options)
# Connect to the application
url = "http://3.235.239.146:8080"
driver.get(url)
vet_link = driver.find_element_by_link_text("VETERINARIANS")
vet_link.click()
# Verify that table loaded
sleep(1)
verify_table = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "table")))
print("Table loaded")
driver.quit()