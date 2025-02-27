import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    # открытие страницы
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

    # ввод значения 45 в поле ввода
    delay_input = driver.find_element(By.CSS_SELECTOR, '#delay')
    delay_input.clear()
    delay_input.send_keys('45')

    # нажатие на кнопки 7, +, 8, =
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    # проверка результата через 45 секунд
    result = WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), '15')
    )
    assert result, "Результат не равен 15"
