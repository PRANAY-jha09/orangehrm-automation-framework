from selenium.webdriver.common.by import By
from core.base_page import BasePage



class LoginPage(BasePage):

    USERNAME = (By.Name, "username")
    PASSWORD = (By.Name, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def open(self,url):
        self.driver.get(url)

    def login(self,username,password):

        self.type(self.USERNAME,username)
        self.type(self.PASSWORD,password)
        self.click(self.LOGIN_BUTTON)
