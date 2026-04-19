from selenium.webdriver.common.by import By
from .base_page import BasePage
from .login_page import LoginPage


class HomePage(BasePage):
    BOOK_STORE_SECTION = (By.XPATH, "//h5[text()='Book Store Application']/..")
    LOGIN_LINK = (By.LINK_TEXT, "Login")

    def go_to_login(self):
        self.click(self.BOOK_STORE_SECTION)
        self.click(self.LOGIN_LINK)
        return LoginPage(self.driver)