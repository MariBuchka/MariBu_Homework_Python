from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ResultPage:

    def __init__(self, driver):
        self.driver = driver


    def wait_for_alerts(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.alert.py-2.alert-success, div.alert.py-2.alert-danger"))
        )


    def get_field_alert_class(self, field_id):
        return self.driver.find_element(By.ID, field_id).get_attribute("class")
