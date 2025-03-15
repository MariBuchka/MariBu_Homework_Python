from selenium.webdriver.common.by import By

class CartPage:

    def __init__(self, driver):
        self.driver = driver


    def get_counter(self):
        self.driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
