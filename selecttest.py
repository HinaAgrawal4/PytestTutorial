import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver= webdriver.Chrome()
driver.get("https://www.salesforce.com/in/form/signup/freetrial-salesforce-starter/?d=jumbo1-btn-ft")
driver.maximize_window()
ddl=driver.find_element(By.NAME,"UserTitle")
dropdown=Select(ddl)
dropdown.select_by_index(2)
print(dropdown)
#driver.implicitly_wait(10)
wait= WebDriverWait(driver,10)
element=wait.until(EC.presence_of_element_located(By.NAME('UserTitle')))