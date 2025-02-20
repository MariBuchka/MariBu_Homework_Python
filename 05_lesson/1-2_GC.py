from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# Для Google Chrome
# 2. Клик по кнопке без ID
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://uitestingplayground.com/dynamicid")

driver.find_element(By.CSS_SELECTOR, '[class="btn btn-primary"]').click()
sleep(3)
driver.quit()
