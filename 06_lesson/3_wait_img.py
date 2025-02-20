from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Для Google Chrome
# 3. Дождаться картинки

driver = webdriver.Chrome()
driver.maximize_window()

# переход на сайт
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# ожидание загрузки картинок
waiter = WebDriverWait(driver, 20)
waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "p#text.lead"), "Done!")
    )

# получение значения атрибута src у 3-й картинки
atribut_src = driver.find_element(
    By.CSS_SELECTOR, 'img[id="award"]').get_attribute("src")

# вывод в консоль значения атрибута src
print(atribut_src)

driver.quit()
