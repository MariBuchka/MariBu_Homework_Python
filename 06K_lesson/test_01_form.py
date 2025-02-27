import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class User:
    def __init__(self, first_name, last_name, address, zip_code, city, country, mail, phone, job_position, company):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.zip_code = zip_code
        self.city = city
        self.country = country
        self.mail = mail
        self.phone = phone
        self.job_position = job_position
        self.company = company

    def fill_form(self, driver):
        fields = {
            "first-name": self.first_name,
            "last-name": self.last_name,
            "address": self.address,
            "zip-code": self.zip_code,
            "city": self.city,
            "country": self.country,
            "e-mail": self.mail,
            "phone": self.phone,
            "job-position": self.job_position,
            "company": self.company
        }

        for field_name, value in fields.items():
            driver.find_element(By.NAME, field_name).send_keys(value)


# инициализация и завершение работы драйвера
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


# проверка заполнения полей
def test_form_filling(driver):
    # переходим на сайт
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # заводим пользователя
    my_user = User("Иван", "Петров", "Ленина, 55-3", "", "Москва", "Россия",
                   "test@skypro.com", "+7985899998787", "QA", "SkyPro")

    # заполняем поля данными
    my_user.fill_form(driver)

    # нажимаем кнопку
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-outline-primary.mt-3").click()

    # ожидание подсветки полей
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.alert.py-2.alert-success, div.alert.py-2.alert-danger"))
    )

    # проверка, что поле Zip code подсвечено красным
    zip_code_alert = driver.find_element(By.ID, "zip-code")
    assert "alert-danger" in zip_code_alert.get_attribute("class"), "Поле Zip code не подсвечено красным"

    # проверка, что остальные поля подсвечены зеленым
    #success_alerts = driver.find_elements(By.CSS_SELECTOR, "div.alert.py-2.alert-success")
    #for alert in success_alerts:
    #    assert "alert-success" in alert.get_attribute("class"), "Не все поля подсвечены зеленым"
    fields_to_check = [
        "first-name", "last-name", "address", "e-mail", "phone",
        "city", "country", "job-position", "company"
    ]

    for field_id in fields_to_check:
        field = driver.find_element(By.ID, field_id)
        assert "alert-success" in field.get_attribute("class"), (
            f"Поле {field_id} не подсвечено зеленым"
        )