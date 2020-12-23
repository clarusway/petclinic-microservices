from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("no-sandbox")
chrome_options.add_argument("disable-dev-shm-usage")
driver = webdriver.Chrome(options=chrome_options)
base_url = "https://www.google.com/"
driver.get(base_url)
source = driver.page_source
if "I'm Feeling Lucky" in source:
  print("Test passed")
else:
  print("Test failed")
driver.close()