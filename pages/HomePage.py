from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://baranbellini.ru/")

    def go_to_section(self, name: str):
        old_url = self.driver.current_url
        element = self.driver.find_element(By.LINK_TEXT, name)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        WebDriverWait(self.driver, 5).until(EC.url_changes(old_url))

    def accept_cookies(self):
        try:
            wait = WebDriverWait(self.driver, 5)
            button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "biscuit-button"))
            )
            button.click()

            wait.until(
                EC.invisibility_of_element_located((By.CLASS_NAME, "biscuit"))
            )
        except TimeoutException:
            pass  # баннер не появился — ок

    def get_url(self):
        return self.driver.current_url