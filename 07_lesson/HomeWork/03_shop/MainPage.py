from selenium.webdriver.common.by import By

class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()


    def authorization(self):
        self.driver.find_element(By.NAME, 'user-name').send_keys('standard_user')
        self.driver.find_element(By.NAME, 'password').send_keys('secret_sauce')
        self.driver.find_element(By.NAME, 'login-button').click()
