import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class MainPage:

    def __init__(self, driver):
        """
        Конструктор класса MainPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    @allure.step("Открытие страницы магазина")
    def open(self):
        """
        Открывает страницу магазина.
        """
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Авторизация пользователя {user}: {password}")
    def authorization(self, user: str, password: str):
        """
        Авторизация пользователя.

        :param user: str - логин пользователя для входа в интернет-магазин.
        :param password: str - пароль пользователя
        для входа в интернет-магазин.
        """
        self.driver.find_element(By.NAME, 'user-name').send_keys(user)
        self.driver.find_element(By.NAME, 'password').send_keys(password)
        self.driver.find_element(By.NAME, 'login-button').click()
