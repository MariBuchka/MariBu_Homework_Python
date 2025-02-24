import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# данные для авторизации
username = 'standard_user'
password = 'secret_sauce' # взят с сайта вручную

# данные пользователя для заполнения формы покупки
first_name = 'Mary'
last_name = 'Withoutlastname'
postal_code = '12345'

# ожидаемая итоговая сумма
expected_total = '$58.29'

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_saucedemo_checkout(driver):
    # открытие страницы магазинна
    driver.get('https://www.saucedemo.com/')

    # авторизация пользователя standard_user
    driver.find_element(By.NAME, 'user-name').send_keys(username)
    driver.find_element(By.NAME, 'password').send_keys(password)
    driver.find_element(By.NAME, 'login-button').click()

    # добавление товаров в корзину
    items_to_add = ['Sauce Labs Backpack', 'Sauce Labs Bolt T-Shirt', 'Sauce Labs Onesie']
    for item in items_to_add:
        driver.find_element(By.XPATH, f"//div[text()='{item}']/following::button[text()='Add to cart']").click()

    # переход в корзину
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()

    # нажатие кнопки Checkout
    driver.find_element(By.ID, 'checkout').click()

    # заполнение формы покупки данными пользователя
    driver.find_element(By.ID, 'first-name').send_keys(first_name)
    driver.find_element(By.ID, 'last-name').send_keys(last_name)
    driver.find_element(By.ID, 'postal-code').send_keys(postal_code)

    # нажатие кнопки Continue
    driver.find_element(By.ID, 'continue').click()

    # чтение итоговой стоимости
    total_text = driver.find_element(By.CLASS_NAME, 'summary_total_label').text

    # извлекаем только часть для сравнения с ожидаемым результатом (убираем префикс "Total: ")
    total = total_text.split('$')[-1].strip()
    total = f"${total}"  # возврат символа "$" обратно

    # проверка, что итоговая сумма равна $58.29
    assert total == expected_total, f"Ожидаемая сумма: {expected_total}, Фактическая сумма: {total}"
