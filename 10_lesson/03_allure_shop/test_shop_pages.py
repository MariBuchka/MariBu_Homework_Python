import allure
import pytest
from selenium import webdriver
from MainPageAllure import MainPage
from ProductsPageAllure import ProductsPage
from CartPageAllure import CartPage
from CheckoutPageAllure import CheckoutPage
from SummaryPageAllure import SummaryPage


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.mark.parametrize(
    "user, password, items, first_name, last_name, post_code, expected_total",
    [
        (
            'standard_user', 'secret_sauce',
            ['Sauce Labs Backpack',
             'Sauce Labs Bolt T-Shirt',
             'Sauce Labs Onesie'],
            'Mary', 'Withoutlastname', '12345',
            '$58.29'
         ),
    ],
)
@allure.title("Тестирование оформления заказа в интернет-магазине")
@allure.description("Проверка корректности расчета итоговой суммы заказа")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_saucedemo_checkout(driver, user, password, items,
                            first_name, last_name, post_code, expected_total):
    """
    Тест проверяет корректность формирование итоговой суммы заказа.

    :param driver: WebDriver - объект драйвера, переданный фикстурой.
    :param user: str - логин пользователя для входа в интернет-магазин.
    :param password: str - пароль пользователя для входа в интернет-магазин.
    :param items: list - список наименований добавляемых продуктов.
    :param first_name: str - имя пользователя.
    :param last_name: str - фамилия пользователя.
    :param post_code: str - почтовый код.
    :param expected_total: str - ожидаемая итоговая сумма заказа
                                 в формате '$XX.XX'.
    """

    main_page = MainPage(driver)
    with allure.step("Открытие страницы магазина"):
        main_page.open()
    with allure.step(f"Авторизация пользователя {user}: {password}"):
        main_page.authorization(user, password)

    products_page = ProductsPage(driver)
    with allure.step("Добавление нескольких продуктов в корзину"):
        products_page.add_products(items)

    cart_page = CartPage(driver)
    with allure.step("Нажатие на иконку 'Корзина'"):
        cart_page.get_counter()

    checkout_page = CheckoutPage(driver)
    with allure.step("Нажатие кнопки 'Checkout'"):
        checkout_page.get_checkout()

    with allure.step(f"Заполнение формы заказа данными пользователя "
                     f"{first_name} {last_name}: {post_code}"):
        checkout_page.fill_form(first_name, last_name, post_code)

    with allure.step("Нажатие кнопки 'Continue'"):
        checkout_page.get_continue()

    summary_page = SummaryPage(driver)
    with allure.step("Получение итоговой суммы"):
        total = summary_page.get_summary()

    with allure.step("Проверка результата"):
        assert total == expected_total, \
            (f"Ожидаемая сумма: {expected_total}, "
             f"Фактическая сумма: {total}")
