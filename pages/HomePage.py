from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://baranbellini.ru/")

    def go_to_postnyy_stol(self):
        self.driver.find_element(By.LINK_TEXT, "Постный стол").click()

    def get_url(self):
        return self.driver.current_url