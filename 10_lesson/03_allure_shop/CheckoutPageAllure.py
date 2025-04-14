import allure
from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        """
        Конструктор класса CheckoutPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Нажатие кнопки 'Checkout'")
    def get_checkout(self):
        """
        Нажимает на кнопку 'Checkout' для начала оформления заказа.
        """
        self.driver.find_element(By.ID, 'checkout').click()

    @allure.step(
        "Заполнение формы заказа данными пользователя "
        "{first_name} {last_name}: {post_code}"
    )
    def fill_form(self, first_name: str, last_name: str, post_code: str):
        """
        Заполняет поля формы данными пользователя.

        :param first_name: str - имя пользователя.
        :param last_name: str - фамилия пользователя.
        :param post_code: str - почтовый код.
        """
        self.driver.find_element(By.ID, 'first-name').send_keys(first_name)
        self.driver.find_element(By.ID, 'last-name').send_keys(last_name)
        self.driver.find_element(By.ID, 'postal-code').send_keys(post_code)

    @allure.step("Нажатие кнопки 'Continue'")
    def get_continue(self):
        """
        Нажимает на кнопку 'Continue' для продолжения оформления заказа.
        """
        self.driver.find_element(By.ID, 'continue').click()
