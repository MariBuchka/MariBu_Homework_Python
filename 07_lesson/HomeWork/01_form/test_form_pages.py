from selenium import webdriver
from User import User
from FormPage import FormPage
from ResultFormPage import ResultPage


def test_form_filling():
    driver = webdriver.Chrome()

    my_user = User("Иван", "Петров", "Ленина, 55-3", "", "Москва", "Россия",
                   "test@skypro.com", "+7985899998787", "QA", "SkyPro")

    form_page = FormPage(driver)
    form_page.fill_form(my_user)
    form_page.submit_form()

    result_page = ResultPage(driver)
    result_page.wait_for_alerts()

    zip_code_alert_class = result_page.get_field_alert_class("zip-code")
    assert "alert-danger" in zip_code_alert_class, "Поле Zip code не подсвечено красным"

    fields_to_check = [
        "first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"
    ]

    for field_id in fields_to_check:
        field_alert_class = result_page.get_field_alert_class(field_id)
        assert "alert-success" in field_alert_class, f"Поле {field_id} не подсвечено зеленым"

    driver.quit()
