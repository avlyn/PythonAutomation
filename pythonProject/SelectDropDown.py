from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome('./chromedriver');
driver.get("https://amazon.com")
driver.maximize_window() ##maimize the window
print(driver.title)

dropdown = driver.find_element(By.XPATH,"//select[@aria-describedby='searchDropdownDescription']")

sel = Select(dropdown)

sel.select_by_index(3) ##low priority

sel.select_by_value("search-alias=baby-products")

sel.select_by_visible_text("Electronics") ##high priority

sleep(5)