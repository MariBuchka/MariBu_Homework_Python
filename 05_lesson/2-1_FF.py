from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# Для FireFox
# 1. Модальное окно
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/entry_ad")

# Нажатие кнопки в модальном окне
try:
    driver.find_element(By.CSS_SELECTOR, "div.modal-footer p").click()
except:
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, "div.modal-footer p").click()
sleep(2)
driver.quit()
