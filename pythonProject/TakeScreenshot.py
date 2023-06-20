from time import sleep


from selenium import webdriver
from PIL import Image
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('./chromedriver')
driver.get("https://facebook.com")
driver.maximize_window() ##maimize the window
print(driver.title)

driver.save_screenshot("image.png")

image =Image.open("image.png")

image.show()
