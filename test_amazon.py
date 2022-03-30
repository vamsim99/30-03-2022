from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
print("test case started")
driver.maximize_window()
driver.get("https://www.amazon.in/")
driver.find_element_by_id("twotabsearchtextbox").send_keys("samsung ultra")
time.sleep(1)
driver.find_element_by_id("nav-search-submit-button").click()
time.sleep(5)
driver.close()
print("test case completed")

