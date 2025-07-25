
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.yatra.com")
driver.find_element(By.ID,"mobile-number").send_keys("8798909876")
driver.find_element(By.NAME, "Login" ).click()
driver.close()
