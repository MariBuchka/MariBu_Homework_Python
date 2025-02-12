from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# Для Google Chrome
# 1. Клик по кнопке
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# 5 кликов по кнопке
i = 1
while i < 6:
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, '[onclick="addElement()"]').click()
    i = i+1

sleep(2)
# сбор списка кнопок
elements = driver.find_elements(By.CSS_SELECTOR, '[onclick="deleteElement()"]')

# вывод на экран размера списка
print(len(elements))

driver.quit()