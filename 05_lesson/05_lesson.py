from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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

# 2. Клик по кнопке без ID
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://uitestingplayground.com/dynamicid")

driver.find_element(By.CSS_SELECTOR, '[class="btn btn-primary"]').click()
sleep(3)
driver.quit()

# 3. Клик по кнопке с CSS-классом
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://uitestingplayground.com/classattr")

driver.find_element(By.CSS_SELECTOR, "[class~='btn-primary']").click()
sleep(2)
driver.quit()

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