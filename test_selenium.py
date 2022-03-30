from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(ChromeDriverManager().install())
print("Testcase started")

driver.maximize_window()
driver.get("https://www.google.co.in/")
driver.find_element_by_name("q").send_keys("facebook")
time.sleep(2)
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(20)
driver.close()
print("testcase completed")

