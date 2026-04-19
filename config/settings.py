import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BASE_URL = os.getenv("BASE_URL", "https://demoqa.com")

    # Данные для успешного входа
    VALID_USER = os.getenv("VALID_USER", "test123")
    VALID_PASSWORD = os.getenv("VALID_PASSWORD", "Qwerty123!")

    # Данные для проверки ошибки
    INVALID_USER = os.getenv("INVALID_USER", "wrong_user")
    INVALID_PASSWORD = os.getenv("INVALID_PASSWORD", "wrong_pass")