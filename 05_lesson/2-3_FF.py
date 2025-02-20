from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# Для FireFox
# 3. Форма авторизации
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/login")
sleep(2)

# Ввод в поле username
username = driver.find_element(By.NAME, "username")
username.send_keys("tomsmith")
sleep(2)

# Ввод в поле password
password = driver.find_element(By.NAME, "password")
password.send_keys("SuperSecretPassword!")
sleep(2)

# Нажатие кнопки Login
driver.find_element(By.CSS_SELECTOR, 'button.radius').click()
sleep(2)
driver.quit()
