from time import sleep

from selenium import webdriver

from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By



driver = webdriver.Chrome('./chromedriver');
driver.get("https://yatra.com")
driver.maximize_window() ##maimize the window
print(driver.title)

support = driver.find_element(By.XPATH,"//a[text()='Support ']")

act = ActionChains(driver);

act.move_to_element(support).perform()

driver.find_element(By.XPATH,"//a[text()='Talk To Us']").click();

driver.switch_to.frame("iframeChatBot"); ## user inside into the frame now

driver.find_element(By.XPATH,"//button[text()='Cancellation']").click();

driver.switch_to.default_content(); ## user come out from th eframe

driver.find_element(By.ID,"chatbot_close_button").click()

sleep(5)