from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('./chromedriver')
driver.get("https://facebook.com")
driver.maximize_window() ##maimize the window
print(driver.title)


##driver.find_element(By.NAME,"q").send_keys("testing")


driver.find_element(By.ID,"email").send_keys("abc@gmail.com")
driver.find_element(By.NAME,"pass").send_keys("123456")
driver.find_element(By.NAME,"login").click();
sleep(2)





