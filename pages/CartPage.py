from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

import re

def extract_quantity(text):
    """Извлекает число из строки, игнорируя пробелы"""
    digits = re.sub(r"[^\d]", "", text)
    value = int(digits) if digits else -1
    if value == -1:
        print(text)
        raise Exception
    return value

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://baranbellini.ru/cart")

    def get_total(self):
        return extract_quantity(self.driver.find_element(By.CLASS_NAME, 'discount_total').text)

    def increase_quantity(self):
        cart_item = self.driver.find_element(By.CLASS_NAME, "cart-item")
        inc_button = cart_item.find_element(By.CLASS_NAME, "counter-changer__btn_inc")

        total_element = self.driver.find_element(By.CLASS_NAME, 'discount_total')
        old_total = extract_quantity(total_element.text)

        inc_button.click()

        try:
            WebDriverWait(self.driver, 5).until(
                lambda d: (
                    print("Current total:", d.find_element(By.CLASS_NAME, 'discount_total').text),
                    extract_quantity(d.find_element(By.CLASS_NAME, 'discount_total').text) > old_total
                )[1]
            )
        except TimeoutException:
            print("Timeout! Old total:", old_total, "Current total:",
                  self.driver.find_element(By.CLASS_NAME, 'discount_total').text)
            raise