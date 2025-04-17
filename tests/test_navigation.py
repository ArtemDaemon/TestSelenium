import pytest
from pages.HomePage import HomePage

@pytest.mark.parametrize("section_name, expected_url_part", [
    ("Постный стол", "postnyy_stol"),
    ("Горячее", "main"),
    ("Мангал", "grill"),
    ("Хинкали и манты", "khinkali_i_manty"),
    ("Выпечка", "bakery"),
    ("Супы", "soups"),
    ("Закуски", "snacks"),
    ("Детское", "detskoe"),
    ("Десерты", "sweets"),
    ("Бизнес-ланчи", "lunch"),
    ("На компанию", "na_kompaniyu"),
    ("Баку", "baku"),
    ("Полуфабрикаты", "semifinished"),
    ("Соусы", "sauces"),
    ("Напитки", "drinks"),
])
def test_navigate_menu(driver, section_name, expected_url_part):
    home = HomePage(driver)
    home.open()
    home.go_to_section(section_name)
    assert expected_url_part in home.get_url()

@pytest.mark.parametrize("section_name, expected_url_part", [
    ("Акции", "promo"),
    ("Доставка и оплата", "delivery-and-payment"),
    ("Контакты", "contacts"),
    ("Правовая информация", "legal-information"),
    ("Бонусная программа", "loyalty-program")
])
def test_navigate_sections(driver, section_name, expected_url_part):
    home = HomePage(driver)
    home.open()
    home.accept_cookies()
    home.go_to_section(section_name)
    assert expected_url_part in home.get_url()