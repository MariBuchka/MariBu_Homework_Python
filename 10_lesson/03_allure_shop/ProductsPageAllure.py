import allure
from selenium.webdriver.common.by import By


class ProductsPage:

    def __init__(self, driver):
        """
        Конструктор класса ProductsPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver

    @allure.step("Добавление конкретного продукта в корзину")
    def add_product_to_cart(self, item):
        """
        Добавляет в корзину указанный товар.

        :param item: str - наименование продукта.
        """
        self.driver.find_element(
            By.XPATH, f"//div[text()='{item}']"
                      "/following::button[text()='Add to cart']").click()

    @allure.step("Добавление нескольких продуктов в корзину")
    def add_products(self, items):
        """
        Добавляет в корзину указанные товары по очереди.

        :param items: list - список наименований добавляемых продуктов.
        """
        for item in items:
            self.add_product_to_cart(item)
