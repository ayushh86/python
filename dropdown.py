import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.ID,"autocomplete").send_keys("ind")
time.sleep(2)
country =driver.find_elements(By.CLASS_NAME,"ui-menu-item-wrapper")
print(len(country))

for count in country:
    if count.text =="india":
        count.click()
        break