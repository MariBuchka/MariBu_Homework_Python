from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Для Google Chrome
# 2. Переименовать кнопку

driver = webdriver.Chrome()
driver.maximize_window()

# переход на сайт
driver.get("http://uitestingplayground.com/textinput")

# указание текста в поле ввода
element = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
element.send_keys("SkyPro")

# нажатие на синюю кнопку
driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

# ожидание смены текста кнопки
waiter = WebDriverWait(driver, 20)
waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#updatingButton"), "SkyPro")
    )

# получение (нового) текста кнопки
UB_txt = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text

# вывод в консоль нового текста кнопки
print(UB_txt)

driver.quit()