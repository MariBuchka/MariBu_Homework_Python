from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ResultPage:

    def __init__(self, driver):
        self.driver = driver


    def wait_for_alerts(self):
        WebDriverWait(self.driver, 50).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), '15')
        )


    def get_result(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.screen').text
