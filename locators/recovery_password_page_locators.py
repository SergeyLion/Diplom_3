from selenium.webdriver.common.by import By


class RecoveryLocators:
    #Форма авторизации пользователя - страница авторизации
    INPUT_USERNAME = (By.NAME, "name")
    INPUT_AUTH_PASSWORD = (By.NAME, "Пароль")
    BUTTON_ENTER = (By.XPATH, "//button[text()='Войти']")
    LINK_RESET_PASSWORD = (By.XPATH, "//a[contains(@class,'Auth_link') and contains(text(),'Восстановить пароль')]")  # Ссылка "Восстановить пароль" в форме "Регистрация"
    #Форма восстановления пароля
    INPUT_EMAIL_RESET = (By.NAME, "name") #Поле ввода Email формы восстановления пароля
    BUTTON_RECOVER = (By.XPATH, "//button[text()='Восстановить']") #Кнопка "Восстановить"
    #Форма ввода нового пароля
    INPUT_COD_FROM_MAIL = (By.XPATH, "//label[text()='Введите код из письма']") # Поле ввода "Введите код из письма"
    ICON_SHOW = (By.XPATH, "//div[contains(@class,'icon-action')]/*") # Иконка показать/скрыть
    INPUT_PASSWORD = (By.XPATH, "//input[@name='Введите новый пароль']/..")