from config.config import BASE_URL
from pages.login_page import LoginPage

def test_invalid_login(driver):
    login = LoginPage(driver)

    login.open(BASE_URL)

    login.login(
        "WrongUser"
        "WrongPassword"
    )

    assert "Invalid credentials" in driver.page_source
