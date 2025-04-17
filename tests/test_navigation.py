from pages.HomePage import HomePage


def test_navigate_to_postnii_stol(driver):
    home = HomePage(driver)
    home.open()
    home.go_to_postnyy_stol()
    assert "postnyy_stol" in home.get_url()