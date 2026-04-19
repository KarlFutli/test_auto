import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.settings import Config
from pages.home_page import HomePage


@pytest.fixture(scope="function")
def driver():
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    drv = webdriver.Chrome(options=options)
    drv.implicitly_wait(5)
    yield drv

    drv.quit()

@pytest.fixture(scope="function")
def home_page(driver):

    driver.get(Config.BASE_URL)
    return HomePage(driver)