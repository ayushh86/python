import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver= webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Ayush Srivastav")
driver.find_element(By.CSS_SELECTOR,"input[name='email']").send_keys("ayushsrivastav00@gmail.com")
driver.find_element(By.ID,'exampleInputPassword1').send_keys("hello")
driver.find_element(By.ID,'exampleCheck1').click()
dropdown = Select(driver.find_element(By.ID,'exampleFormControlSelect1'))
dropdown.select_by_visible_text('Male')
dropdown.select_by_visible_text('Female')
driver.find_element(By.ID,'inlineRadio1').click()
driver.find_element(By.NAME,'bday').send_keys("01/17/1999")
time.sleep(10)
