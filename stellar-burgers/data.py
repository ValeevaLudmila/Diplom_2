class StatusCode:
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    FORBIDDEN = 403
    NOT_FOUND = 404
    UNAUTHORIZED = 401
    INTERNAL_SERVER_ERROR = 500


class ResponseBody:
    # Создание пользователя
    USER_ALREADY_EXISTS = {'success': False, 'message': 'User already exists'}
    REQUIRED_FIELDS_MISSING = {'success': False, 'message': 'Email, password and name are required fields'}
    
    # Логин пользователя
    LOGIN_INCORRECT_CREDENTIALS = {'success': False, 'message': 'email or password are incorrect'}
    
    # Создание заказа
    UNAUTHORIZED = {'success': False, 'message': 'You should be authorised'}
    INGREDIENTS_REQUIRED = {'success': False, 'message': 'Ingredient ids must be provided'}
    
    # Обновление пользователя
    EMAIL_ALREADY_EXISTS = {'success': False, 'message': 'User with such email already exists'}


class TestData:
    # Существующий пользователь для тестов
    EXISTING_USER_EMAIL = "test-existing-user@yandex.ru"
    EXISTING_USER_PASSWORD = "password123"
    EXISTING_USER_NAME = "Existing User"
    
    # Ингредиенты
    VALID_INGREDIENTS = ["60d3b41abdacab0026a733c6", "609646e4dc916e00276b2870"]
    INVALID_INGREDIENT_HASH = "invalid_hash_12345"
    
    # Для логина с неверными данными
    NONEXISTENT_EMAIL = "nonexistent@yandex.ru"
    WRONG_PASSWORD = "wrongpassword"


class Flags:
    SUCCESS = 'success'
    ACCESS_TOKEN = 'accessToken'
    REFRESH_TOKEN = 'refreshToken'
    USER_DATA = 'user'
    ORDER_DATA = 'order'
    NAME = 'name'
    MESSAGE = 'message'