from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProfilePage(BasePage):
    PAGE_HEADER = (By.CLASS_NAME, "text-center")
    LOGOUT_BUTTON = (By.ID, "submit")

    def is_loaded(self):
        return "/profile" in self.get_current_url()
    def logout(self):
        from .login_page import LoginPage

        self.click(self.LOGOUT_BUTTON)
        return LoginPage(self.driver)