@allure.story("Негативный сценарий")
@allure.title("Проверка ошибки при неверных данных")
def test_login_invalid(self, home_page):
    login_page = home_page.go_to_login()
    current_page = login_page.login(Config.INVALID_USER, Config.INVALID_PASSWORD)
    assert "/login" in current_page.get_current_url(), "При ошибке URL изменился!"
    error_text = current_page.get_error_message_text()
    assert "Invalid username or password!" in error_text, f"Ошибка не совпала: {error_text}"
