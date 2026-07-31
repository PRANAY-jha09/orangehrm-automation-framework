from selenium.webdriver.common.by import By

from core.base_page import BasePage

class DashboardPage(BasePage):

    PIM_MENU = (by.XPATH,"//SPAN[TEST()='PIM']")

    def open_pim(self):
        self.click(self.PIM_MENU)