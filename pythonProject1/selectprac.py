from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome('./chromedriver');
driver.get("https://demo.guru99.com/test/newtours/register.php")
driver.maximize_window() ##maimize the window
print(driver.title)

cntry = driver.find_element(By.NAME,"country")
sel = Select(cntry)
sel.select_by_index(2)
sel.select_by_index(5)
sel.select_by_index(7)
sleep(5)

sel.select_by_value("ANGOLA")
sel.select_by_visible_text("ARGENTINA")
sleep(5)

driver.get("https://byjus.com/us/")
driver.maximize_window()
driver.find_element(By.XPATH,"(//span[text()='USA'])[1]").click()
driver.find_element(By.XPATH,"//span[text()='India']").click()
sleep(5)