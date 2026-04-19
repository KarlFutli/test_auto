@allure.story("Позитивный сценарий")
@allure.title("Успешный вход и выход из системы")
def test_login_valid_credentials_and_logout(self, home_page):
    login_page = home_page.go_to_login()
    profile_page = login_page.login(Config.VALID_USER, Config.VALID_PASSWORD)

    assert profile_page.is_loaded(), "Не удалось попасть на страницу профиля."
    returned_login_page = profile_page.logout()

    assert "/login" in returned_login_page.get_current_url(), \
        f"После выхода нас не вернуло на страницу логина. Текущий URL: {returned_login_page.get_current_url()}"