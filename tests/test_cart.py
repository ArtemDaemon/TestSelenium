from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.CartPage import CartPage
from pages.ProductPage import ProductPage


def test_cart_shows_product_after_adding(driver):
    product = ProductPage(driver)
    product.open()
    product.add_to_cart()

    cart = CartPage(driver)
    cart.open()
    # Ждём появления товара в списке корзины
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Люля-кебаб из говядины')]"))
    )
    assert "Люля-кебаб из говядины" in driver.page_source

def test_add_button_does_not_break_on_repeat_click(driver):
    product = ProductPage(driver)
    product.open()
    for _ in range(5):
        product.add_to_cart()
    # Проверим, что после кликов страница не сломалась
    assert driver.title != "Ошибка"
    assert "ошибка" not in driver.page_source.lower()

def test_change_quantity_updates_total(driver):
    product = ProductPage(driver)
    product.open()
    product.add_to_cart()

    cart = CartPage(driver)
    cart.open()

    old_total = cart.get_total()
    cart.increase_quantity()

    new_total = cart.get_total()
    assert new_total > old_total