from selenium import webdriver
from MainPage import MainPage
from ProductsPage import ProductsPage
from CartPage import CartPage
from CheckoutPage import CheckoutPage

# ожидаемая итоговая сумма
expected_total = '$58.29'


def test_saucedemo_checkout():
    driver = webdriver.Chrome()

    main_page = MainPage(driver)
    main_page.authorization()

    products_page = ProductsPage(driver)
    products_page.add_products(['Sauce Labs Backpack', 'Sauce Labs Bolt T-Shirt', 'Sauce Labs Onesie'])

    cart_page = CartPage(driver)
    cart_page.get_counter()

    # заполнение формы покупки данными пользователя
    checkout_page = CheckoutPage(driver)
    checkout_page.get_checkout()
    checkout_page.fill_form()

    # нажатие кнопки Continue
    driver.find_element(By.ID, 'continue').click()

    # чтение итоговой стоимости
    total_text = driver.find_element(By.CLASS_NAME, 'summary_total_label').text

    # извлекаем только часть для сравнения с ожидаемым результатом (убираем префикс "Total: ")
    total = total_text.split('$')[-1].strip()
    total = f"${total}"  # возврат символа "$" обратно

    # проверка, что итоговая сумма равна $58.29
    assert total == expected_total, f"Ожидаемая сумма: {expected_total}, Фактическая сумма: {total}"

    driver.quit()
