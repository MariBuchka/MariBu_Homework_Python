import allure
from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):
        """
        Конструктор класса CartPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Нажатие на иконку 'Корзина'")
    def get_counter(self):
        """
        Нажимает на иконку корзины для перехода на страницу корзины.
        """
        self.driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
