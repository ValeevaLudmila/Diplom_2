import os
from urllib.parse import urljoin


class Url:
    """
    Класс для управления API-эндпоинтами проекта Stellar Burgers.
    Поддерживает разные стенды через переменные окружения.
    """

    MAIN_URL = os.getenv('MAIN_URL', 'https://stellarburgers.nomorepartiessite.ru/api')

    # Авторизация и пользователи
    CREATE_USER = '/auth/register'
    LOGIN_USER = '/auth/login'
    LOGOUT_USER = '/auth/logout'
    USER_PROFILE = '/auth/user'
    REFRESH_TOKEN = '/auth/token'

    # Заказы и ингредиенты
    CREATE_ORDER = '/orders'
    GET_ORDERS = '/orders'
    GET_ALL_ORDERS = '/orders/all'
    GET_INGREDIENTS = '/ingredients'

    # Восстановление пароля
    PASSWORD_RESET = '/password-reset'
    PASSWORD_RESET_CONFIRM = '/password-reset/reset'

    @classmethod
    def full(cls, path: str) -> str:
        """
        Возвращает полный URL на основе базового MAIN_URL.
        Например:
            Url.full(Url.CREATE_USER) → https://stellarburgers.../api/auth/register
        """
        return urljoin(cls.MAIN_URL, path)
