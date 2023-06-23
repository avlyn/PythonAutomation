from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys

from selenium.webdriver.common.by import By

driver = webdriver.Chrome('./chromedriver');
driver.get("https://google.com")
driver.maximize_window() ##maimize the window
print(driver.title)

driver.find_element(By.XPATH,"//textarea[@type='search']").send_keys("Testing")


##act######DDFFF = ActionChains(driver);
sleep(3)

driver.find_element(By.XPATH,"//textarea[@type='search']").send_keys(Keys.D)
sleep(5)
driver.find_element(By.XPATH,"//textarea[@type='search']").send_keys(Keys.DOWN)
driver.find_element(By.XPATH,"//textarea[@type='search']").send_keys(Keys.ENTER)

##act.key_down(Keys.CONTROL).key_down(Keys.CONTROL).send_keys(Keys.ENTER).perform()

sleep(7)

