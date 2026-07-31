from config.config import BASE_URL
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pimpage import Pimpage


def test_search_employee(driver):
    login =LoginPage(driver)
    dashboard =DashboardPage(driver)
    pim =Pimpage(driver)

    login.open(Base_URL)
    login.login("Admin","admin")

    dashabord.open_pim()

    pim.search_employee("Pranay")

    assert "Pranay" in driver.page_dource

