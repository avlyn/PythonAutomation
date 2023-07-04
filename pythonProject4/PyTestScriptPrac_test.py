import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from PIL import Image
from selenium.webdriver.support.select import Select


def test_byjus(): ##- test1
    driver = webdriver.Chrome('./chromedriver')
    driver.get("https://byjus.com/us/")
    driver.maximize_window()  ##maimize the window
    print(driver.title)



def test_MouseHovering(): ##Test2
    driver = webdriver.Chrome('./chromedriver');
    driver.get("https://byjus.com/us/")
    driver.maximize_window()  ##maimize the window
    print(driver.title)

    subjectlist = driver.find_element(By.XPATH, "//div[text()='Subjects']")

    act = ActionChains(driver);

    act.move_to_element(subjectlist).perform()

    driver.find_element(By.XPATH, "//span[text()='Math']").click();

    sleep(3);

def test_Screenshot():
    driver = webdriver.Chrome('./chromedriver')
    driver.get("https://byjus.com/us/")
    driver.maximize_window()  ##maimize the window
    print(driver.title)

    driver.save_screenshot("image.png")

    image = Image.open("image.png")

    image.show()
