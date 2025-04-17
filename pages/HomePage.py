from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://baranbellini.ru/")

    def go_to_section(self, name: str):
        old_url = self.driver.current_url
        self.driver.find_element(By.LINK_TEXT, name).click()
        WebDriverWait(self.driver, 5).until(EC.url_changes(old_url))

    def get_url(self):
        return self.driver.current_url