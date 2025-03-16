from selenium.webdriver.common.by import By


class HeaderLocators:
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//p[contains(text(),'Кабинет')]")  # Кнопка "Личный кабенет"
    LINK_LOGO = (
    By.XPATH, "//div[contains(@class,'header__logo')]/a")  # Ссылка на домашнюю страницу в логотипе "Stellar Burgers"
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")  # Кнопка "Конструктор в хедере программы
    BUTTON_LIST_ORDERS = (By.XPATH, "//p[text()='Лента Заказов']")  # Кнопка "Лента Заказов в хедере программы
