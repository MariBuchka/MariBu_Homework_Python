from selenium.webdriver.common.by import By

class FormPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()


    def fill_form(self, User):
        fields = {
            "first-name": User.first_name,
            "last-name": User.last_name,
            "address": User.address,
            "zip-code": User.zip_code,
            "city": User.city,
            "country": User.country,
            "e-mail": User.mail,
            "phone": User.phone,
            "job-position": User.job_position,
            "company": User.company
        }

        for field_name, value in fields.items():
            self.driver.find_element(By.NAME, field_name).send_keys(value)


    def submit_form(self):
        self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-outline-primary.mt-3").click()
