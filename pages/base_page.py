from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchFrameException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_lacated(locator))

    def click(self, locator):
        element = self.find_element(locator)
        # Скроллим до видимости
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        # Ждем и кликаем
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

    def get_current_url(self):
        return self.driver.current_url
