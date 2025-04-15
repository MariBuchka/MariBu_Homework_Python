import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class SummaryPage:

    def __init__(self, driver):
        """
        Конструктор класса SummaryPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Получение итоговой суммы")
    def get_summary(self) -> str:
        """
        Возвращает текущий результат.

        :return: str - итоговая сумма заказа в формате '$XX.XX'.
        """
        total_text = self.driver.find_element(
            By.CLASS_NAME, 'summary_total_label').text
        total = total_text.split('$')[-1].strip()
        total = f"${total}"
        return total
