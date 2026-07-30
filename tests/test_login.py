from config.config import BASE_URL
from pages.login_page import LoginPage


def test_valid_login(driver):
    login =LoginPage(driver)

    login.open(BASE_URL)

    login.login(
        "Admin"
        "admin123"
    )

    assert "dashboard" in driver.current_url.lower()
