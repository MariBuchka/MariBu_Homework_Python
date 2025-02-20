from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Для Google Chrome
# 1. Нажать на кнопку

driver = webdriver.Chrome()
driver.maximize_window()

# переход на сайт
driver.get("http://uitestingplayground.com/ajax")

# нажатие на синюю кнопку
driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

# ожидание получения текста зеленой плашки
waiter = WebDriverWait(driver, 20)
txt = waiter.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p.bg-success")))

# вывод в консоль полученного текста
print(txt.text)

driver.quit()