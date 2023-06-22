from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('./chromedriver')
driver.get("https://demo.guru99.com/test/newtours/register.php")
driver.maximize_window()
print(driver.title)

sleep(7)

driver.find_element(By.NAME,"firstName").send_keys("Jesse")
driver.find_element(By.NAME,"lastName").send_keys("Kour")
driver.find_element(By.NAME,"phone").send_keys("1234567")
driver.find_element(By.ID,"userName").send_keys("abc@gmail.com")
driver.find_element(By.NAME,"address1").send_keys("11303 Coral Ave")
driver.find_element(By.NAME,"city").send_keys("Riverside")
driver.find_element(By.NAME,"state").send_keys("Newyork")
driver.find_element(By.NAME,"postalCode").send_keys("97364")
driver.find_element(By.ID,"email").send_keys("testing")
driver.find_element(By.NAME,"password").send_keys("123")
driver.find_element(By.NAME,"confirmPassword").send_keys("123")
driver.find_element(By.NAME,"submit").click()
sleep(7)