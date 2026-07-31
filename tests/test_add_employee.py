import json

from config.config import BASE_URL
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PimPage


def test_add_employee(driver):
     login =loginpage(driver)
     dashboard = DashboardPage(driver)
     pim = PimPage(driver)

     login.open(BASE_URL)
     login.login("Admin","admin123")

     dashboard.open_pim()

     with open("test_data/employee_data.json") as file:
         data = json.load(file)

     pim.add_employee(
         data["first_name"],
         data["middle_name"],
         data["last_name"]
     )

     assert "pim" in driver.current_url.lower()