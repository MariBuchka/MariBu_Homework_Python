from selenium.webdriver.common.by import By

class SummaryPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)


    def get_summary(self):
        total_text = self.driver.find_element(By.CLASS_NAME, 'summary_total_label').text
        total = total_text.split('$')[-1].strip()
        total = f"${total}"
        return total