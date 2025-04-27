from selenium.webdriver.common.by import By

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://baranbellini.ru/grill/kebab-beef")

    def add_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "product-detail__add-btn").click()