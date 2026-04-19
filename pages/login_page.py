from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "userName")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login")
    ERROR_MESSAGE = (By.ID, "name")

    def login(self, username, password):
        from .profile_page import ProfilePage

        self.input_text(self.USERNAME_INPUT, username)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

        time.sleep(2)

        if "/profile" in self.get_current_url():
            return ProfilePage(self.driver)
        else:
            return self

    def get_error_message_text(self):
        element = self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
        return element.text