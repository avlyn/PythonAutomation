from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By

driver = webdriver.Chrome('./chromedriver');
driver.get("https://www.ebay.com/")
##to maximize window
driver.maximize_window()

Elm = driver.find_element(By.XPATH,"(//a[text()='Electronics'])[2]")
Act1 = ActionChains(driver)
Act1.move_to_element(Elm).perform()
sleep(3)

driver.find_element(By.XPATH,"//a[text()='Video Games']").click()
sleep(3)