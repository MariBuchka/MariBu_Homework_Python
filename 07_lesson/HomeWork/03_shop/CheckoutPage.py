from selenium.webdriver.common.by import By

class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver


    def get_checkout(self):
        self.driver.find_element(By.ID, 'checkout').click()


    def fill_form(self, first_name, last_name, post_code):
        self.driver.find_element(By.ID, 'first-name').send_keys(first_name)
        self.driver.find_element(By.ID, 'last-name').send_keys(last_name)
        self.driver.find_element(By.ID, 'postal-code').send_keys(post_code)


    def get_continue(self):
        self.driver.find_element(By.ID, 'continue').click()
