



class BaseData:
    TIMEOUT = 10  # Тайм-аут ожидания элемента страницы в секундах
    URL_STELLAR_BURGERS = "https://stellarburgers.nomoreparties.site/" #Ссылка для тестирования страницы авторизации
    URL_API_STELLAR_BURGERS = "https://stellarburgers.nomoreparties.site" #Ссылка для API
    # Endpoint
    # Ингредиенты
    ENDPOINT_GET_INGREDIENTS = "api/ingredients"

    # Заказы
    ENDPOINT_CREATE_ORDER = "api/orders"
    ENDPOINT_GET_ALL_ORDERS = "api/orders/all"
    ENDPOINT_GET_USER_ORDERS = "api/orders"

    # Восстановление и сброс пароля
    ENDPOINT_PASSWORD_RESET = "api/password-reset"
    ENDPOINT_PASSWORD_RESET_CONFIRM = "api/password-reset/reset"

    # Регистрация и авторизация
    ENDPOINT_REGISTER = "api/auth/register"
    ENDPOINT_LOGIN = "api/auth/login"
    ENDPOINT_LOGOUT = "api/auth/logout"
    ENDPOINT_TOKEN_REFRESH = "api/auth/token"

    # Пользователь
    ENDPOINT_GET_USER_INFO = "api/auth/user"
    ENDPOINT_UPDATE_USER_INFO = "api/auth/user"
    ENDPOINT_DELETE_USER = "api/auth/user"
