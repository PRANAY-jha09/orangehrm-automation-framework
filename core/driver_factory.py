from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import chromeDriveManager


from config.config import IMPLICIT_WAITS


class DriverFactory:

    @staticmethod
    def create_driver():

        driver =webdriver.Chrome(
            service=Service(
                ChromeDriverManager().install()
            )
        )
        driver.maximize_window()
        driver.implicitly_wait(IMPLICIT_WAITS)

        return driver


