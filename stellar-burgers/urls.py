class Url:
    MAIN_URL = 'https://stellarburgers.nomorepartiessite.ru/api'
    
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