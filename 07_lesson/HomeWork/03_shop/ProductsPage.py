from selenium.webdriver.common.by import By

class ProductsPage:

    def __init__(self, driver):
        self.driver = driver


    def add_product_to_cart(self, item):
        self.driver.find_element(By.XPATH, f"//div[text()='{item}']/following::button[text()='Add to cart']").click()

    def add_products(self, items):
        for item in items:
            self.add_product_to_cart(item)
