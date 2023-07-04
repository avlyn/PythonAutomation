import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


def test_Facebook(): ##- test1
    driver = webdriver.Chrome('./chromedriver')
    driver.get("https://facebook.com")
    driver.maximize_window()  ##maimize the window
    print(driver.title)

    assert driver.title == "Testing"


def test_MouseHovering(): ##Test2
    driver = webdriver.Chrome('./chromedriver');
    driver.get("https://amazon.com")
    driver.maximize_window()  ##maimize the window
    print(driver.title)

    accountlist = driver.find_element(By.XPATH, "//span[text()='Account & Lists']")

    act = ActionChains(driver);

    act.move_to_element(accountlist).perform()

    driver.find_element(By.XPATH, "//span[text()='Account']").click();

    sleep(3);

def test_SelectDropDown(): ##Test3
    driver = webdriver.Chrome('./chromedriver');
    driver.get("https://amazon.com")
    driver.maximize_window()  ##maimize the window
    print(driver.title)

    dropdown = driver.find_element(By.XPATH, "//select[@aria-describedby='searchDropdownDescription']")

    sel = Select(dropdown)

    sel.select_by_index(3)  ##low priority

    sel.select_by_value("search-alias=baby-products")

    sel.select_by_visible_text("Electronics")  ##high priority

    sleep(5)