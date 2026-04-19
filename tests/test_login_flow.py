import allure
import pytest
import time
from config.settings import Config

@allure.feature("Авторизация DemoQA")
class TestDemoQALoginFlow:
    @allure.story("Негативный сценарий")
    @allure.title("Проверка ошибки при неверных данных")
    def test_login_invalid_credentials(self, home_page):
        #переходим на страницу входа
        login_page = home_page.go_to_login()
        #входим с НЕВЕРНЫМИ данными
        current_page = login_page.login(Config.INVALID_USER, Config.INVALID_PASSWORD)

        assert "/login" in current_page.get_current_url(), \
            "При ошибке входа URL изменился"
        error_text = current_page.get_error_message_text()

        #проверка текста ошибки
        assert "Invalid username or password!" in error_text, \
            f"Текст ошибки не совпал! Ожидалось: 'Invalid...', Получено: '{error_text}'"

        time.sleep(3)

    @allure.story("Позитивный сценарий")
    @allure.title("Успешный вход и выход из системы")
    def test_login_valid_credentials_and_logout(self, home_page):
        login_page = home_page.go_to_login()

        #верные данные
        profile_page = login_page.login(Config.VALID_USER, Config.VALID_PASSWORD)

        #попали в личный кабинет
        current_url = profile_page.get_current_url()
        assert "/profile" in current_url or "/account" in current_url, \
            f"Вход не удался! Текущий URL: {current_url}. Ожидалось наличие '/profile'."

        #выход
        returned_login_page = profile_page.logout()

        #страница после после выхода
        final_url = returned_login_page.get_current_url()
        assert "/login" in final_url, \
            f"После выхода нас не вернуло на страницу входа! Текущий URL: {final_url}"