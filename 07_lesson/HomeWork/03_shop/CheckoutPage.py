from selenium.webdriver.common.by import By

class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver


    def get_checkout(self):
        self.driver.find_element(By.ID, 'checkout').click()


    def fill_form(self):
        self.driver.find_element(By.ID, 'first-name').send_keys('Mary')
        self.driver.find_element(By.ID, 'last-name').send_keys('Withoutlastname')
        self.driver.find_element(By.ID, 'postal-code').send_keys('12345')
