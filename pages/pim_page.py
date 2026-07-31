from selenium.webdriver.common.by import BY

from core.base_page import Basepage

class Pimpage(BasePage):

     Add_BUTTON = (By.XPATH, "//button[normalize-space()='Add']")

     FIRST_NAME = (By.NAME, "firstNAME")
     MIDDLE_NAME = (By.NAME, "middlename")
     LAST_NAME = (By.NAME, "lastNAME")

     SAVE_BUTTON =(By.XPATH,"//button[@type='submit']")

     def add_employee(self,first,middle,last):
         self.click(self.Add_BUTTON)
         self.type(self.FIRST_NAME,first)
         self.type(self.MIDDLE_NAME,middle)
         self.type(self.LAST_NAME,last)

         self.click(self.SAVE_BUTTON)

     SEARCH_NAME = (By.XPATH, "(//input[@placeholder='Type for hints...'])[1]")
     SEARCH_BUTTON = (By.XPATH, "//button[normalize-space()='Search']")

     def search_employee(self, employee_name):
         self.type(self.SEARCH_NAME, employee_name)
         self.click(self.SEARCH_BUTTON)