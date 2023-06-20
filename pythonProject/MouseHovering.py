from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By

driver = webdriver.Chrome('./chromedriver');
driver.get("https://amazon.com")
driver.maximize_window() ##maimize the window
print(driver.title)

accountlist = driver.find_element(By.XPATH,"//span[text()='Account & Lists']")

act = ActionChains(driver);

act.move_to_element(accountlist).perform()

driver.find_element(By.XPATH,"//span[text()='Account']").click();

sleep(3);