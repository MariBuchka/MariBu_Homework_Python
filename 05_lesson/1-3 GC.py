from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# Для Google Chrome
# 3. Клик по кнопке с CSS-классом
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://uitestingplayground.com/classattr")

driver.find_element(By.CSS_SELECTOR, "[class~='btn-primary']").click()
sleep(2)
driver.quit()