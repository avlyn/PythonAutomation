from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome('./chromedriver');
driver.get("https://demo.guru99.com/test/drag_drop.html")
driver.maximize_window() ##maimize the window
print(driver.title)

sleep(5);


StartingPoint = driver.find_element(By.XPATH,"//a[text()=' BANK ']")

target = driver.find_element(By.ID ,"bank");

act = ActionChains(driver);

act.drag_and_drop(StartingPoint ,target).perform();

