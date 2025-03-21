from selenium import webdriver
from MainPage import MainPage
from ProductsPage import ProductsPage
from CartPage import CartPage
from CheckoutPage import CheckoutPage
from SummaryPage import SummaryPage


def test_saucedemo_checkout():
    driver = webdriver.Chrome()

    main_page = MainPage(driver)
    main_page.authorization()

    products_page = ProductsPage(driver)
    products_page.add_products(['Sauce Labs Backpack', 'Sauce Labs Bolt T-Shirt', 'Sauce Labs Onesie'])

    cart_page = CartPage(driver)
    cart_page.get_counter()

    checkout_page = CheckoutPage(driver)
    checkout_page.get_checkout()
    checkout_page.fill_form('Mary', 'Withoutlastname', '12345')
    checkout_page.get_continue()

    summary_page = SummaryPage(driver)
    total = summary_page.get_summary()
    expected_total = '$58.29'
    assert total == expected_total, f"Ожидаемая сумма: {expected_total}, Фактическая сумма: {total}"

    driver.quit()
