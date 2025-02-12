from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# Для FireFox
# 2. Поле ввода
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/inputs")
sleep(2)

# Ввод в поле 1000
number_box = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
number_box.send_keys("1000")
sleep(2)

# Очищение поля
number_box.clear()
sleep(2)

# Ввод в поле 999
number_box.send_keys("999")
sleep(2)
driver.quit()